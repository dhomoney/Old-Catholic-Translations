# Psalm 4, English v1: Claude critic review

- English: `english/psalm-004.md` at 83621ec (branch agent/clark-translator--mwp7htk2)
- Latin: `latin/psalm-004.md` at d0e51ba (branch agent/mose-scribe--mwp7hse4)
- STYLE.md and GLOSSARY.md at 83621ec
- Reviewer: Charles (Claude critic), 2026-11-20

## Verdict: PASS

No finding affects meaning. Two minor findings below.

## What was checked

- Every paragraph, verse lemma, marginal gloss and heading read against the Latin, sentence by sentence. No omission, addition or mistranslation found.
- Title and the 10 verse lemmas against the Douay-Rheims (Ps. iv, 1-10): exact, except finding 1.
- Commentary quotations against the Douay-Rheims and the Vulgate: Ps. xii, 1; Ps. xc, 15; II Cor. vii, 4; Luke xxi, 34 (note 2); Mark i, 24; Ps. vi, 7; Matt. v, 16 (note 3); Phil. iv, 18; Rom. xii, 1 (note 4); Luke xviii, 11-12; Acts xiv, 16; Ps. ci, 28. All correct; shortened quotations rightly have no note.
- STYLE.md and GLOSSARY.md (new Psalm 4 rows): no breach found.
- Block-for-block format check (`blockcheck.py`): Latin 49 blocks, English 49 blocks, MATCH.

## The three points the Translator raised

1. Title after Bellarmine's *in Hymnis*, and his verses 1-2 as one Douay-Rheims verse (note 1): accepted.
2. "dull of heart" with (*graves corde*, heavy of heart), and "overcharged (*gravantur*)" in Luke xxi: accepted; this is the new STYLE.md 3 rule and keeps his link between the two places visible.
3. Margin "Verse 7." beside verse 8, as printed: accepted (the header comment says so).

## Findings (all minor)

1. **Douay-Rheims wording of verse 8.**
   - Latin: A FRUCTU FRUMENTI, VINI, ET OLEI SUI MULTIPLICATI SUNT.
   - English (lemma, and the quotation after Acts xiv): "BY THE FRUIT OF THEIR CORN, THEIR WINE, AND OIL, THEY ARE MULTIPLIED."
   - Problem: the Challoner Douay-Rheims (Ps. iv, 8) reads "By the fruit of their corn, their wine and oil, they **rest** multiplied." "They are multiplied" is not the Douay-Rheims wording. Bellarmine's point (that *multiplicati sunt* means "they are increased") still works with the Douay-Rheims wording, since the paragraph keeps *multiplicati sunt* (they are multiplied) in Latin where he discusses the word.
   - Fix: "THEY REST MULTIPLIED" in the lemma and "they rest multiplied" in the quotation; leave "*multiplicati sunt* (they are multiplied)" in the word discussion as it is. Please check against your Douay-Rheims copy.

2. **Stiff phrase (register/clarity).**
   - Latin (Title and Argument): ex Hebræo, ut hodie habetur.
   - English: "from the Hebrew, as it is had to-day".
   - Problem: "as it is had" is not idiomatic even in the older register.
   - Fix: "from the Hebrew, as it is now found" (or "as it standeth to-day").
