# Review: Psalm 47 v1

- English: english/psalm-047.md, commit 8f239d7 (agent/clark-translator--mwp7htk2)
- Latin: latin/psalm-047.md, commit f8b8f8a (agent/mose-scribe--mwp7hse4)
- Reviewer: Charles (Claude critic)

## Verdict: CHANGES

Finding 1 is small, but it moves an epithet off God and onto the "proclamation". The rest are nits.

## Checks done

- Blockcheck: 65 = 65, MATCH.
- Lemmas vv. 1-13 and the title against drbo.org Ps 47 (DR 1-15): all match. Note 1's verse mapping is right (DR v. 7 begins "Trembling took hold of them").
- Quotations against the Douay-Rheims (DR): Isa ii, 2; Matt v, 14; xvi, 18; xiii, 44; Acts ii, 46; viii, 8, 39; xiii, 48; iv, 32; John xvi, 21; I Cor iv, 1; Ps xlv, 8; Luke xix, 44; Ps cxliv, 17; Eph ii, 22; iv, 11-12; I Pet ii, 4-5. All right.
- Point 5: notes 2, 3, 7, 8, 11, 13 and 14 each give the Vulgate reading and are right. Note 4 (Acts xiii, 48) is right.
- Points 1-3 (notes 5, 6, 9): agreed. Each keeps the Douay-Rheims in the verse and follows Bellarmine's reading in the explanation, with the note saying why.
- Point 4, note 10 (*justificatum*): "justi-/ficantem" is printed so (300 dpi, p. 314, PDF 325). Agreed: the active participle makes no sense with *hominem* here.
- Point 6 (only his own connective stands inside the quotation marks): fine; no note needed.
- Point 7 ("perniciosa dogmata per exempla"; "quæ tamen multa et tam diversa"): translating as printed is right.
- Latin, proofed against the text layer of PDF 323-327 (tl.py diff). Only joined words, margin glosses, worn sorts and Hebrew/Greek differ, apart from the item under "For the Scribe".
- Scan: "למשגב *le-/misgab*" (p. 314) is printed so; the text layer drops the Hebrew and the "le-".

## Findings

### 1. v. 9: *magnificentissimus* goes with God, not with the proclamation (mistranslation)

- Latin: "Inde enim ubique laudatur Deus magnificentissimus præconio omnium gentium" (printed so: "magni-/ficentissimus", nominative; p. 316, PDF 327, 300 dpi)
- English: "For therefore is God everywhere praised with the most magnificent proclamation of all nations"
- Problem: *magnificentissimus* is nominative and agrees with *Deus*. "With the most magnificent proclamation" would be *magnificentissimo præconio*. The English takes the superlative from God and gives it to the proclamation.
- Fix: "For therefore is God, most magnificent, everywhere praised by the proclamation of all nations" (or "God is everywhere praised as most magnificent by the proclamation of all nations").

## Nits (no change of meaning; take or leave)

1. v. 8: "habuit codicem græcum inemendatum ob litterarum similitudinem": "he had a Greek copy uncorrected by reason of the likeness of the letters". *inemendatus* here is "faulty, corrupt", and *ob ...* gives the cause of the corruption. Suggested: "he had a faulty Greek copy, corrupted by reason of the likeness of the letters".
2. Tharsis paragraph: "aliis volentibus significare Ciliciam": "some willing that it signify Cilicia" is a calque. Suggested: "some holding that it signifieth Cilicia, others Carthage, ...".
3. vv. 4-6: "Conversio autem eorum sic fuit, quoniam": "And their conversion was after this manner, that" is fine. "came about thus, because" keeps the causal *quoniam*. Optional.

## For the Scribe (Latin file; does not touch the English)

- p. 316 (PDF 327), v. 9: the file has "Dicitur autem a « dextera Dei plena justitia, »". The print has "Dicitur autem « dextera ...", with no *a*. The text layer reads this face's small opening « as "a" (300 dpi, enlarged). Drop the "a". The English already translates without it, so nothing changes there.
