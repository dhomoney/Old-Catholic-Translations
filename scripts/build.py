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
SITE = "Old Catholic Translations"
LICENCE = ('Translation &copy; its translators, licensed '
           '<a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>. ')
# Works: slug -> metadata. "bellarmine-psalms" is the flat latin/psalm-NNN.md series;
# every other work lives in latin/<slug>/<unit>-NNN.md. An unknown slug gets defaults.
WORKS = {
    "bellarmine-psalms": dict(title="Bellarmine on the Psalms", author="St. Robert Bellarmine",
                              source="St. Robert Bellarmine, Opera Omnia"),
    "bellarmine-controversiae": dict(title="Bellarmine on the Controversies of the Christian Faith",
                                     author="St. Robert Bellarmine",
                                     source="St. Robert Bellarmine, Disputationes de controversiis christianae fidei (Opera omnia, ed. Fèvre)"),
    "liguori-theologia-moralis": dict(title="Liguori, Moral Theology", author="St. Alphonsus Liguori",
                                      source="St. Alphonsus Liguori, Theologia moralis (Marietti, Turin, 1879)"),
    "liguori-homo-apostolicus": dict(title="Liguori, Homo apostolicus", author="St. Alphonsus Liguori",
                                     source="St. Alphonsus de Liguori, Homo apostolicus instructus ad audiendas confessiones (Paris, Godbert, 1837), from the archive.org OCR text only; no page scan, so the Latin is not proofed against an image"),
    "suarez-de-gratia": dict(title="Suárez, On Grace (De gratia)", author="Francisco Suárez, S.J.",
                             source="Francisci Suarez e Societate Jesu Opera omnia, ed. Carolus Berton, tomus septimus (Paris, Vivès), from the archive.org OCR text only; no page scan, so the Latin is not proofed against an image"),
}
PSALMS = "bellarmine-psalms"


def work_meta(slug):
    w = dict(title=slug.replace("-", " ").title(), author="", source="the cited edition")
    w.update(WORKS.get(slug, {}))
    return w


def credit_html(slug):
    return LICENCE + "Latin text from " + html.escape(work_meta(slug)["source"]) + "."


def credit_md(slug):
    return "Translation licensed CC BY 4.0. Latin text from " + work_meta(slug)["source"] + "."


EDITOR = re.compile(r"\(\\?\*\)\s*\[Editor's note")


def editor_split(text):
    """(label, body) of an editor's-note block: '(*) [Editor's note, X] body'."""
    m = re.match(r"\(\\?\*\)\s*\[([^\]]*)\]\s*(.*)", text, re.S)
    return (m.group(1), m.group(2)) if m else ("Editor's note", text)


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
        fn = re.match(r"\[\^([^\]]+)\]:\s*(.*)", raw, re.S)
        if fn:
            blocks.append(("note", (fn.group(1), fn.group(2).strip())))
        elif EDITOR.match(raw):
            blocks.append(("editor", raw))
        elif raw.startswith("## "):
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
    s = s.replace("\\*", "\x00").replace("(*)", "(\x00)")  # literal asterisks stay literal
    s = html.escape(s, quote=False)
    s = re.sub(r"\[\^([^\]]+)\]", r'<sup><a id="r-\1" href="#fn-\1">[\1]</a></sup>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    return re.sub(r"\*(.+?)\*", r"<em>\1</em>", s).replace("\x00", "*")


def page(title, body, work=PSALMS, depth=0):
    up = "../" * depth
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{html.escape(title)}</title><link rel="stylesheet" href="{up}style.css"></head>'
            f'<body><main>{body}<footer>{credit_html(work)}</footer></main></body></html>')


def load_unit(lp, ep, work, label, fallback_title):
    """Pair one Latin file with its English file. Returns a unit dict, or None."""
    if not ep.exists():
        print(f"skip {lp.name}: no english file", file=sys.stderr)
        return None
    lt, lb = parse(lp)
    et, eb = parse(ep)
    notes = [t for k, t in eb if k == "note"]  # translator's footnotes (English only)
    lb = [b for b in lb if b[0] != "note"]
    eb = [b for b in eb if b[0] != "note"]
    paired = [k for k, _ in lb] == [k for k, _ in eb]
    if not paired:
        print(f"WARNING {lp.name}: Latin and English blocks do not match "
              f"({len(lb)} vs {len(eb)}); showing unpaired", file=sys.stderr)
    return dict(work=work, slug=lp.stem, label=label, ltitle=lt or fallback_title,
                etitle=et or label, lat=lb, eng=eb, paired=paired, notes=notes,
                depth=0 if work == PSALMS else 1)


def collect(src):
    """The Psalms: flat latin/psalm-NNN.md files."""
    out = []
    for lp in sorted((src / "latin").glob("psalm-*.md")):
        num = int(re.search(r"(\d+)", lp.stem).group(1))
        u = load_unit(lp, src / "english" / lp.name, PSALMS, f"Psalm {num}", f"Psalmus {num}")
        if u:
            u["num"] = num
            out.append(u)
    return out


def collect_works(src):
    """List of (work slug, units) in reading order: the Psalms first, then each latin/<work>/."""
    works = []
    psalms = collect(src)
    if psalms:
        works.append((PSALMS, psalms))
    for d in sorted(p for p in (src / "latin").iterdir() if p.is_dir()):
        units = []
        for lp in sorted(d.glob("*.md")):
            u = load_unit(lp, src / "english" / d.name / lp.name, d.name, None, lp.stem)
            if u:
                u["label"] = u["etitle"]
                units.append(u)
        if units:
            works.append((d.name, units))
    return works


def block_html(kind, text):
    if kind == "editor":
        label, body = editor_split(text)
        return (f'<p class="editor"><span class="lbl">{md_inline(label)}</span> '
                f'{md_inline(body)}</p>')
    t = md_inline(text)
    return {"heading": f"<h2>{t}</h2>", "margin": f'<p class="margin">{t}</p>',
            "verse": f'<p class="verse">{t}</p>'}.get(kind, f"<p>{t}</p>")


def unit_html(p, prev, nxt):
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
    up = "../" * p["depth"]
    nav = ('<nav>' + (f'<a href="{prev["slug"]}.html">&larr; {html.escape(prev["label"])}</a>' if prev else "")
           + f'<a href="{up}index.html">Index</a>'
           + (f'<a href="{nxt["slug"]}.html">{html.escape(nxt["label"])} &rarr;</a>' if nxt else "") + "</nav>")
    head = f'<h1>{html.escape(p["etitle"])}</h1><p class="sub">{html.escape(p["ltitle"])}</p>'
    notes = ""
    if p["notes"]:
        notes = ('<section class="notes"><h2>Translator\'s notes</h2><ol>' + "".join(
            f'<li id="fn-{html.escape(i)}">[{html.escape(i)}] {md_inline(t)} '
            f'<a href="#r-{html.escape(i)}">&uarr;</a></li>' for i, t in p["notes"]) + "</ol></section>")
    return page(p["etitle"], nav + head + f'<section class="pair">{rows}</section>' + notes + nav,
                p["work"], p["depth"])


def pandoc(*args):
    subprocess.run(["pandoc", *args], check=True)


def _unique_notes(p, n):
    """Prefix footnote labels with the unit's position so labels stay unique in a book."""
    ren = lambda t: re.sub(r"\[\^([^\]]+)\]", rf"[^u{n}-\1]", t)
    q = dict(p)
    q["eng"] = [(k, ren(t)) for k, t in p["eng"]]
    q["notes"] = [(f"u{n}-{i}", ren(t)) for i, t in p["notes"]]
    return q


def md_block(kind, text, latin):
    """Stacked-book Markdown for one block; Latin is set as a block quote."""
    if kind == "page":
        return f"*— {text} —*" if latin else ""
    if kind == "heading":
        return f"## {text}" if not latin else f"*{text}*"
    if kind == "margin":
        return f"*[{text}]*"
    if kind == "editor":
        label, body = editor_split(text)
        t = f"**{label}.** {body}".replace("(*)", "(\\*)").replace("(\\\\*)", "(\\*)")
        return ("> " + t) if latin else t
    return ("> " + text) if latin else text


def book_md(units, work=PSALMS):
    meta = work_meta(work)
    units = [_unique_notes(p, n) for n, p in enumerate(units, 1)]
    parts = [f"---\ntitle: {meta['title']}\nsubtitle: Latin and English\n"
             f"author: {meta['author']}\nlang: en\n---\n\n{credit_md(work)}\n"]
    for p in units:
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
        for i, t in p["notes"]:
            parts.append(f"[^{i}]: {t}\n")
    return "\n".join(x for x in parts if x) + "\n"


def build_books(work, units, out):
    b = out / "books"; b.mkdir(exist_ok=True)
    md = b / f"{work}.md"
    md.write_text(book_md(units, work), encoding="utf-8")
    pandoc(str(md), "--toc", "-o", str(out / "site" / f"{work}.epub"))
    pdf = out / "site" / f"{work}.pdf"
    try:
        pandoc(str(md), "--pdf-engine=xelatex", "--toc",
               "-V", "mainfont=FreeSerif", "-V", "geometry:margin=2.2cm", "-o", str(pdf))
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"xelatex PDF failed ({e}); trying weasyprint", file=sys.stderr)
        pandoc(str(md), "--toc", "-s", "--pdf-engine=weasyprint",
               "--css", str(ROOT / "site-assets" / "style.css"), "-o", str(pdf))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default=str(ROOT))
    ap.add_argument("--out", default=str(ROOT / "_build"))
    a = ap.parse_args()
    src, out = Path(a.src), Path(a.out)
    shutil.rmtree(out, ignore_errors=True)
    (out / "site").mkdir(parents=True)
    shutil.copy(ROOT / "site-assets" / "style.css", out / "site" / "style.css")

    works = collect_works(src)
    sections = ""
    for work, units in works:
        meta = work_meta(work)
        for i, u in enumerate(units):
            d = out / "site" / (work if u["depth"] else "")
            d.mkdir(parents=True, exist_ok=True)
            (d / f"{u['slug']}.html").write_text(
                unit_html(u, units[i-1] if i else None,
                          units[i+1] if i + 1 < len(units) else None), encoding="utf-8")
        links = "".join(
            f'<li><a href="{(work + "/") if u["depth"] else ""}{u["slug"]}.html">{html.escape(u["label"])}</a></li>'
            for u in units)
        sections += (f'<section class="work"><h2>{html.escape(meta["title"])}</h2>'
                     f'<ul class="idx">{links}</ul>'
                     f'<p class="dl"><a href="{work}.pdf">PDF</a> &middot; '
                     f'<a href="{work}.epub">EPUB</a></p></section>')
    body = (f'<h1>{SITE}</h1><p class="sub">English translations of old Catholic texts, '
            f'with the Latin beside them.</p>'
            + (sections or "<p>The first texts are in preparation.</p>"))
    (out / "site" / "index.html").write_text(page(SITE, body), encoding="utf-8")

    if works:
        if not shutil.which("pandoc"):
            sys.exit("pandoc not found")
        for work, units in works:
            build_books(work, units, out)
    print(f"built {sum(len(u) for _, u in works)} unit(s) in {len(works)} work(s) into {out}")


if __name__ == "__main__":
    main()
