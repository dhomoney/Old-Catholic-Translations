# Psalm 5, English v1: Claude critic review

- English: `english/psalm-005.md` at ea751eb (branch agent/clark-translator--mwp7htk2)
- Latin: `latin/psalm-005.md` at 21245b6 (branch agent/mose-scribe--mwp7hse4)
- STYLE.md and GLOSSARY.md at ea751eb
- Reviewer: Charles (Claude critic), 2026-11-20

## Verdict: CHANGES

One finding affects meaning (finding 1); it is a one-line fix. Two minor findings.

## What was checked

- Every paragraph, verse lemma, marginal gloss and heading read against the Latin, sentence by sentence.
- Title and the 15 verse lemmas against the Douay-Rheims (Ps. v, 1-13), and the verse mapping in note 1: the mapping is correct (Douay 2-6 = his 1-5; 7 = 6+7; 8-10 = 8-10; 11 = 11+12; 12-13 = 13-15).
- Commentary quotations against the Douay-Rheims and the Vulgate: Ps. l, 17; Matt. x, 36; I Kings viii, 7; Acts v, 4; Ps. cii, 4. All correct.
- STYLE.md and GLOSSARY.md (new Psalm 5 rows): no breach found apart from finding 3.
- Block-for-block format check (`blockcheck.py`): Latin 57 blocks, English 57 blocks, MATCH.

## The four points the Translator raised

1. Fifteen headings against thirteen Douay-Rheims verses (note 1): accepted; mapping checked.
2. Heading 13 "AND ALL THEY SHALL BE GLAD" after the printed *lætabuntur*, with note 2, and the Douay-Rheims "Let all them be glad" in the commentary for *Lætentur*: accepted.
3. *et est Deus in eis* "and God is in them": accepted; it keeps his present tense between two futures.
4. *iniqui* "men of iniquity": accepted.

## Findings

1. **Mistranslation: who is "whole" (meaning).**
   - Latin (Title and Argument): Ecclesiæ, quæ hæreditatem salutis æternæ quotidie in suis membris consequitur, et in fine mundi tota consequetur.
   - English: "which daily obtaineth the inheritance of eternal salvation in her members, and at the end of the world shall obtain it whole."
   - Problem: *tota* is feminine nominative and agrees with the Church, the subject (the inheritance, *hæreditatem*, would need *totam*). Bellarmine contrasts the Church obtaining the inheritance piecemeal, in her members one by one, with the whole Church obtaining it at the end of the world. "Shall obtain it whole" makes the inheritance the thing that is whole.
   - Fix: "and at the end of the world shall the whole Church" / page marker / "obtain it." (Or, keeping the order: "and at the end of the world shall, the whole of her," / marker / "obtain it.")

2. **Douay-Rheims wording of the title (minor).**
   - Latin: *In finem pro ea, quæ hæreditatem consequitur, Psalmus David.*
   - English: "*Unto the end, for her that obtaineth the inheritance. A psalm of David.*"
   - Problem: the Challoner Douay-Rheims title of Ps. v reads "A psalm **for** David", as in Ps. iv (only Ps. iii has "The psalm of David").
   - Fix: "A psalm for David." Please check against your Douay-Rheims copy.

3. **Douay-Rheims wording of verse 12 (minor).**
   - Latin: SECUNDUM MULTITUDINEM IMPIETATUM EORUM EXPELLE EOS.
   - English (lemma and commentary): "ACCORDING TO THE MULTITUDE OF THEIR WICKEDNESS CAST THEM OUT".
   - Problem: the Challoner Douay-Rheims (Ps. v, 11) has the plural, "the multitude of their wickednesses", after the Vulgate *impietatum*. The GLOSSARY.md row "impietates | wickedness" should then read "wickednesses".
   - Fix: "WICKEDNESSES" in the lemma and "wickednesses" in the commentary quotation; correct the glossary row. Please check against your Douay-Rheims copy.
