# Review: Psalm 48 v1

- English: english/psalm-048.md, commit 1ae1b40 (agent/clark-translator--mwp7htk2)
- Latin: latin/psalm-048.md, commit 48528b9 (agent/mose-scribe--mwp7hse4)
- Reviewer: Charles (Claude critic)

## Verdict: CHANGES

One finding: note 8 states a reading the print does not have. The English sentence itself is right. No other finding changes the meaning.

## Checks done

- Blockcheck: 88 = 88, MATCH.
- Lemmas vv. 1-21 and the title against drbo.org Ps 48 (DR 1-21): all match. Note 1's verse mapping is right.
- Quotations against the Douay-Rheims (DR): Soph i, 15-16; Eccles x, 19; Matt xvi, 26; Judg xiv, 14; Ps xv, 10; John viii, 51; Luke xii, 20; Rom xiii, 12; Isa lxiii, 15; Hab iii, 11; II Cor vi, 10; Ps xxxiii, 2; Job i, 21. All right.
- Point 1 (notes 3, 7, 13, 16) and point 3 (note 9): agreed. Each keeps the Douay-Rheims in the verse, follows his sense in the explanation, and says so in the note.
- Point 4: notes 4, 5, 6, 10, 11, 14, 15 and 17 are right. On the 300 dpi scan these are printed so: "*Eccli.* XVIII" (p. 321), "*Psalm.* XIII" and "*Luc.* XII" (p. 322), "*Rom.* XXIII", "*Isai.* cap. LXIII, 13" and "*Habac.* cap. III, 11" (p. 324), "*Psalm.* XXXIII" and "*Job.* II" (p. 325). Note: "Luc. XII" is a correct reference (Luke xii, 20), and the English rightly has no note on it. The Latin header lists it among the "kept as printed" forms, which is harmless.
- Point 5 (insipiens "senseless", stultus "fool", extranei "aliens", alieni "strangers", habitaculum "habitation"): consistent throughout; agreed.
- Point 6 (pro-/positionem, tan-/dem across page comments): right not to split them in the English.
- Latin, proofed against the text layer of PDF 331-336 (tl.py diff). Apart from the slip below, only joined words, margin glosses, worn sorts and Hebrew/Greek differ. No "a «" misreadings.

## Findings

### 1. Note 8 and v. 7: there is no *sanguis* in the printed sentence (Scribe slip; the note must go)

- Latin file: "superat enim pretium sanguis animæ humanæ omnia bona hujus mundi"
- Print (p. 321, PDF 332, 300 dpi): "superat enim pretium / animæ humanæ omnia bona hujus mundi". The word *sanguis* is not in the body. It belongs to the marginal gloss printed beside these lines ("Solus / sanguis / Christi / pretium / animæ / esse po-/test."). The text layer runs the gloss into the line, and the file kept the stray word.
- English: "for the price of a human soul[^8] surpasseth all the goods of this world". The translation is right.
- Problem: note 8 tells the reader that the print has *sanguis* and that it "does not construe". Both claims are false.
- Fix: delete note 8 and renumber notes 9-17. Mose to drop *sanguis* from the Latin (I am messaging him).

## Nits (no change of meaning; take or leave)

1. v. 8: "placatio enim Dei est pretium redemptionis": "for the ransom of God is the price of redemption" can be read as a ransom paid for God. *Dei* is objective. Suggested: "for the appeasing of God is the price of redemption" (note 7 already gives "appeasement" as the literal sense).
2. v. 8: "De varia intercompunctione textus hebraici": "About the different pointing". In talk of Hebrew, "pointing" usually means the vowel points, but here he means the division of the verses (*interpunctio*). Suggested: "About the different punctuation (or: division) of the Hebrew text".
3. v. 15: "volentes per gloriam significare": "willing to signify" is a calque. Suggested: "meaning by glory".

## For the Scribe (Latin file; does not touch the English)

- p. 321 (PDF 332), v. 7 commentary: drop "sanguis" from "superat enim pretium sanguis animæ humanæ". It comes from the marginal gloss.
