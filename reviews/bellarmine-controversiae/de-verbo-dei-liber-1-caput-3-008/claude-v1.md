# Review: Controversiae 008 v1 (De verbo Dei, Book I, Chapter III)

- English: english/bellarmine-controversiae/de-verbo-dei-liber-1-caput-3-008.md, commit 2c213e9 (agent/clark-translator--mwp7htk2)
- Latin: latin/bellarmine-controversiae/de-verbo-dei-liber-1-caput-3-008.md, commit f84ac94 (agent/mose-scribe--mwp7hse4)
- Scan: bellermine-de-controversiis-fidei-1.pdf, PDF pp. 94-97
- Reviewer: Charles (Claude critic)

## Verdict: PASS

No finding affects meaning. One STYLE finding (a missing misprint note) for v2.

## Checks done

- Block-for-block: blockcheck.py, Latin 40 blocks, English 40 blocks, MATCH.
- Every sentence compared with the Latin. No omission, addition or mistranslation found.
- Douay-Rheims (Challoner, drbo.org) checked word for word for every italic quotation: II Cor. iii, 6-8; John i, 17; John v, 39; I Tim. iv, 13; Deut. xxvii, 26; Lev. xviii, 5; Rom. iv, 15; Rom. vii, 7, 8, 11-13, 24-25; Rom. iii, 20, 31; Rom. viii, 3-4; Luke i, 6; Matt. v, 21-22; John iii, 5; Matt. xxviii, 19-20; Jer. xxxi, 31-33; Gal. iv, 24. All agree. Leaving out "therefore"/"then" where Bellarmine leaves out *ergo* is a shortening and needs no note (STYLE).
- Scan, 300 dpi crops: PDF 96 right column has *cum patribus vestris* (so note 8 is right: a reading of Bellarmine's text, not a Scribe slip). PDF 94 right column has *Origines* (finding 1).
- GLOSSARY rows: vitium "fault", vitiositas "viciousness", dilectio "love" applied consistently.

## Findings

1. **STYLE breach (misprint not noted).** Latin p. 71 right column: *Origines Contra Celsum (5)*. The 300 dpi crop of PDF 94 confirms the print has *Origines* (it has *Origenes* at the top of p. 72). Current English: "Origen, *Against Celsus* (5)", with no note. Problem: STYLE says a misprint of the printed edition is translated by the sense and gets a note; the Latin header does not list it either. Fix: add a translator's note "the print has *Origines* for *Origenes*." Mose should add it to the header's misprint list in the final Latin commit Clark has asked for.

## Translator's points

- (1) Notes for iu, prœvaricatio, regum, Testamenmentum, Infellix, Joannis and the missing (6): agreed.
- (2) Deut. xxvii, 26; John iii, 5; Matt. xxviii, 19: agreed, DR checked.
- (3) *patribus vestris*: agreed; confirmed in the scan.
- (4) Header-only v2 after Mose's commit: fine; include *Origines* (finding 1).
- (5) Ovid in Latin, italics, English in brackets: agrees with STYLE 4 (classical verse).
- (6) *qua ratione ... excludit* as relative ("whereby he shutteth out"): acceptable. An interrogative reading ("on what ground doth he shut out ...?") is also possible; the sense, the question why the letter is excluded, is the same either way. No change needed.
- (7) *vitium* "fault" in both Augustine passages: agreed; matches the new GLOSSARY row.
