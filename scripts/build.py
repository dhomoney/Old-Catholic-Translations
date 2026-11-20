#!/usr/bin/env python3
"""Build the site (HTML) and books (EPUB, PDF) from latin/ and english/ Markdown.

Usage: scripts/build.py [--src DIR] [--out DIR]
  --src  folder holding latin/ and english/ (default: repo root)
  --out  output folder (default: _build; never committed)
Needs: pandoc. PDF: xelatex, else weasyprint. Reviews are never published.
"""
import argparse, html, re, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TITLE = "Bellarmine on the Psalms"
CREDIT = ('Translation &copy; its translators, licensed '
          '<a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>. '
          "Latin text from St. Robert Bellarmine, <em>Opera Omnia</em>.")
CREDIT_MD = ("Translation licensed CC BY 4.0. "
             "Latin text from St. Robert Bellarmine, *Opera Omnia*.")


def parse(path):
    """Return (title, blocks). A block is (kind, text); kinds:
    page (<!-- p. N ... --> marker), heading (## ), margin ([Margin: ...]),
    verse (starts with **), para. Other <!-- comments --> are dropped."""
    text = path.read_text(encoding="utf-8").strip()
    title = None
    m = re.match(r"#\s+(.+)\n", text + "\n")
    if m:
        title, text = m.group(1).strip(), text[m.end():]
    blocks = []
    for raw in re.split(r"\n\s*\n", text):
        raw = raw.strip()
        if not raw:
            continue
        c = re.fullmatch(r"<!--(.*?)-->", raw, re.S)
        if c:
            pm = re.match(r"\s*p\.\s*(\d+)", c.group(1))
            if pm:
                blocks.append(("page", "p. " + pm.group(1)))
            continue
        raw = re.sub(r"<!--.*?-->", "", raw, flags=re.S).strip()  # inline comments
        raw = re.sub(r"\s*\n\s*", " ", raw)
        if not raw:
            continue
        if raw.startswith("## "):
            blocks.append(("heading", raw[3:].strip()))
        elif raw.startswith("[Margin:"):
            blocks.append(("margin", re.sub(r"^\[Margin:\s*|\]$", "", raw).strip()))
        elif raw.startswith("**"):
            blocks.append(("verse", raw))
        else:
            blocks.append(("para", raw))
    return title, blocks


def md_inline(s):
    """Minimal inline Markdown (*em*, **strong**) to HTML."""
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    return re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)


def page(title, body, css="style.css"):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{html.escape(title)}</title><link rel="stylesheet" href="{css}"></head>'
            f'<body><main>{body}<footer>{CREDIT}</footer></main></body></html>')


def collect(src):
    out = []
    for lp in sorted((src / "latin").glob("psalm-*.md")):
        ep = src / "english" / lp.name
        if not ep.exists():
            print(f"skip {lp.name}: no english file", file=sys.stderr)
            continue
        lt, lb = parse(lp)
        et, eb = parse(ep)
        num = int(re.search(r"(\d+)", lp.stem).group(1))
        paired = [k for k, _ in lb] == [k for k, _ in eb]
        if not paired:
            print(f"WARNING {lp.name}: Latin and English blocks do not match "
                  f"({len(lb)} vs {len(eb)}); showing unpaired", file=sys.stderr)
        out.append(dict(num=num, slug=lp.stem, ltitle=lt or f"Psalmus {num}",
                        etitle=et or f"Psalm {num}", lat=lb, eng=eb, paired=paired))
    return out


def block_html(kind, text):
    t = md_inline(text)
    return {"heading": f"<h2>{t}</h2>", "margin": f'<p class="margin">{t}</p>',
            "verse": f'<p class="verse">{t}</p>'}.get(kind, f"<p>{t}</p>")


def psalm_html(p, prev, nxt):
    if p["paired"]:
        rows = ""
        for (k, l), (_, e) in zip(p["lat"], p["eng"]):
            if k == "page":
                rows += f'<div class="pg">{html.escape(l)}</div>'
            else:
                rows += (f'<div class="row {k}"><div lang="la">{block_html(k, l)}</div>'
                         f'<div lang="en">{block_html(k, e)}</div></div>')
    else:  # unpaired fallback: whole texts in two columns
        col = lambda bl: "".join(block_html(k, t) for k, t in bl if k != "page")
        rows = (f'<div class="row"><div lang="la">{col(p["lat"])}</div>'
                f'<div lang="en">{col(p["eng"])}</div></div>')
    nav = ('<nav>' + (f'<a href="{prev["slug"]}.html">&larr; Psalm {prev["num"]}</a>' if prev else "")
           + '<a href="index.html">Index</a>'
           + (f'<a href="{nxt["slug"]}.html">Psalm {nxt["num"]} &rarr;</a>' if nxt else "") + "</nav>")
    head = f'<h1>{html.escape(p["etitle"])}</h1><p class="sub">{html.escape(p["ltitle"])}</p>'
    return page(p["etitle"], nav + head + f'<section class="pair">{rows}</section>' + nav)


def pandoc(*args):
    subprocess.run(["pandoc", *args], check=True)


def md_block(kind, text, latin):
    """Stacked-book Markdown for one block; Latin is set as a block quote."""
    if kind == "page":
        return f"*\u2014 {text} \u2014*" if latin else ""
    if kind == "heading":
        return f"## {text}" if not latin else f"*{text}*"
    if kind == "margin":
        return f"*[{text}]*"
    return ("> " + text) if latin else text


def book_md(psalms):
    parts = [f"---\ntitle: {TITLE}\nsubtitle: Latin and English\n"
             f"author: St. Robert Bellarmine\nlang: en\n---\n\n{CREDIT_MD}\n"]
    for p in psalms:
        parts.append(f"\n# {p['etitle']}\n")
        if p["paired"]:  # stacked Latin-then-English; long blocks may break across pages
            for (k, l), (_, e) in zip(p["lat"], p["eng"]):
                if k == "page":
                    parts.append(md_block(k, l, True) + "\n")
                elif k == "heading":
                    parts.append(md_block(k, e, False) + "\n\n" + md_block(k, l, True) + "\n")
                else:
                    parts.append(md_block(k, l, True) + "\n\n" + md_block(k, e, False) + "\n")
        else:
            for blocks, latin in ((p["lat"], True), (p["eng"], False)):
                parts += [md_block(k, t, latin) + "\n" for k, t in blocks if k != "page"]
    return "\n".join(x for x in parts if x) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default=str(ROOT))
    ap.add_argument("--out", default=str(ROOT / "_build"))
    a = ap.parse_args()
    src, out = Path(a.src), Path(a.out)
    shutil.rmtree(out, ignore_errors=True)
    (out / "site").mkdir(parents=True)
    shutil.copy(ROOT / "site-assets" / "style.css", out / "site" / "style.css")

    psalms = collect(src)
    for i, p in enumerate(psalms):
        (out / "site" / f"{p['slug']}.html").write_text(
            psalm_html(p, psalms[i-1] if i else None,
                       psalms[i+1] if i + 1 < len(psalms) else None), encoding="utf-8")

    links = "".join(f'<li><a href="{p["slug"]}.html">Psalm {p["num"]}</a></li>' for p in psalms)
    body = (f"<h1>{TITLE}</h1><p class=\"sub\">English translation, with the Latin beside it.</p>"
            + (f'<ul class="idx">{links}</ul>' if psalms else "<p>The first Psalms are in preparation.</p>")
            + ('<p class="dl"><a href="bellarmine-psalms.pdf">PDF</a> &middot; '
               '<a href="bellarmine-psalms.epub">EPUB</a></p>' if psalms else ""))
    (out / "site" / "index.html").write_text(page(TITLE, body), encoding="utf-8")

    if psalms:
        if not shutil.which("pandoc"):
            sys.exit("pandoc not found")
        b = out / "books"; b.mkdir()
        (b / "book.md").write_text(book_md(psalms), encoding="utf-8")
        pandoc(str(b / "book.md"), "--toc", "-o", str(out / "site" / "bellarmine-psalms.epub"))
        pdf = out / "site" / "bellarmine-psalms.pdf"
        try:
            pandoc(str(b / "book.md"), "--pdf-engine=xelatex", "--toc",
                   "-V", "mainfont=DejaVu Serif", "-V", "geometry:margin=2.2cm", "-o", str(pdf))
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            print(f"xelatex PDF failed ({e}); trying weasyprint", file=sys.stderr)
            pandoc(str(b / "book.md"), "--toc", "-s", "--pdf-engine=weasyprint",
                   "--css", str(ROOT / "site-assets" / "style.css"), "-o", str(pdf))
    print(f"built {len(psalms)} psalm(s) into {out}")


if __name__ == "__main__":
    main()
