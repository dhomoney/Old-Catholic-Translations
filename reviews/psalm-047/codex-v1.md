# Psalm 47 — Codex review v1

**CHANGES**

English: `8f239d7`, `english/psalm-047.md`. Latin: `f8b8f8a`, `latin/psalm-047.md`.

1. **Scribe addition — verse 9 commentary, printed p. 316 / PDF 327, left column, line beginning “autem”.** Current Latin: *Dicitur autem a « dextera Dei plena justitia, »*. The scan has only the opening quotation mark before *dextera*, not an additional letter *a*. Suggested fix: *Dicitur autem « dextera Dei plena justitia, »*. Confirmed in the 600 dpi crop `/tmp/jo47-praise.png`. Current English, “Now ‘the right hand’ of God is said to be ‘full of justice,’” already gives the intended sentence; no English note is needed. Update its header to the corrected Latin commit.

2. **Mistranslation — verse 9 commentary, printed p. 316.** Latin: *Inde enim ubique laudatur Deus magnificentissimus præconio omnium gentium*. Current English: “For therefore is God everywhere praised with the most magnificent proclamation of all nations”. The scan confirms *magnificentissimus*, nominative, agreeing with *Deus*: it describes God, rather than the ablative *præconio*. Suggested fix: “For therefore is the most magnificent God everywhere praised by the proclamation of all nations”. Keep the following reason concerning his justice. No misprint note is required.

3. **Reference labels — STYLE 3.** The Latin has *Ephes. II* in the closing commentary; current English uses *Eph.* ii there and in note 13. The prescribed English form is *Ephes.* Change both labels. The quotation and note's distinction between *in Spiritu Sancto* and the Vulgate *in Spiritu* are otherwise sound.

## Verification

Independently compared all English prose, the title, thirteen lemmas, twenty-three margins, fourteen notes and nine Ps 47 glossary rows against the Latin and STYLE.md. The content blocks correspond (65 including the document heading), as do all five page markers. The verse concordance and lemmas agree with [Douay-Rheims Psalm 47](https://www.drbo.org/chapter/21047.htm). Checked the extended [Ephesians iv quotation](https://www.drbo.org/chapter/56004.htm), [I Peter ii quotation](https://www.drbo.org/chapter/67002.htm) and [John xvi quotation](https://www.drbo.org/chapter/50016.htm). No further meaning-affecting omission, addition or doctrinal issue found.

Independently proofed Bellarmine's entire Latin against `bellermine-on-psalms-1.pdf`, PDF 323–327 (printed 312–316), excluding the later editor's apparatus. Full pages rendered at 2800-pixel height; doubtful v. 6 and v. 9 wording and punctuation checked at 600 dpi. Apart from finding 1, the transcription matches the print. Greek and Hebrew forms, margins and page breaks were included.

In particular, the print really has *hominem justificantem*: note 10 correctly discloses the intended *justificatum*, and “the justified man” is sound. The print also confirms *perniciosa dogmata per exempla*, *quæ tamen multa et tam diversa*, *Jurusalem*, and the malformed opening quotation before *ibat*. The reported quotation differences are represented transparently by notes; supplying sensible English quotation boundaries around the verse words does not change the author's reasoning. The distinction between *suscipere* and the Douay-Rheims “protect”, and the explanation of *sic*, are preserved.

O'Sullivan and the other critic's review were not consulted.

## Source-proof correction after Mose's follow-up

4. **Additional Scribe margin intrusion — verse 1 commentary, printed p. 313 / PDF 324, left column, line beginning “miracula”.** Original Latin `f8b8f8a` has *Atque ut hujus ædificii Ecclesiæ miracula brevissime attingamus*. The scan body has *Atque ut hujus ædificii miracula brevissime attingamus*; *Ecclesiæ* belongs to the adjacent margin *Ecclesiæ præstantia*. Mose caught this after my review; I missed it in the first proof. Independently confirmed at 600 dpi in `/tmp/jo47-ecclesiae.png`. Latin `f33c8cf` correctly removes it. Current English `8f239d7`, “the miracles of this building of the Church,” carries the intrusive word; change to “the miracles of this building”. This does not alter the surrounding identification of the building as the Church.

The complete Latin diff `f8b8f8a..f33c8cf` has been checked: finding 1 and this fourth finding are fixed, and the header now records the genuinely printed *justificantem*. Findings 2–3 still await revised English. The earlier statement that no other source slip was present is superseded by this correction.
