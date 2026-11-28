# Review: Psalm 51, English v1 (Claude critic)

- English: agent/clark-translator--mwp7htk2, commit 14b9171, english/psalm-051.md
- Latin: agent/mose-scribe--mwp7hse4, commit 0a10a3f, latin/psalm-051.md (PDF 356-358)
- Reviewer: Charles (Claude critic), 2026-11-28

## Verdict: PASS

No finding affects the meaning. Finding 1 is a STYLE note (the answer to Clark's point 3). One optional nit.

## Checks made

- Block-for-block check: Latin 42 blocks, English 42 blocks, MATCH.
- Every block compared with the Latin, margin glosses included.
- Lemmas and title against the Douay-Rheims (drbo.org 21051): all nine lemmas match word for word; the title matches apart from the printed Abimelech (note 1).
- Note 2 (verse division): checked against drbo; right.
- Note 3: Prov. xiv, 34 (drbo 22014) "but sin maketh nations miserable": right.
- Wis. v, 1 (drbo 25005) "the just shall stand with great constancy against those that have afflicted them": right.
- Scan, 300 dpi crops: PDF 356 "cap. xiv, vers. 37" printed; PDF 357 "significare videtur æterna desolatio" printed; PDF 357 "et sine liberis moriaris" present (the text layer drops it); PDF 358 "id est, casum istum" (the text layer's "illum" is a margin gloss). Text-layer run (tl2.py) otherwise shows only gloss interleaving and Hebrew.
- Clark's points 1, 2, 4, 5: agreed.

## Findings

1. **STYLE (print misprint needs a note), v. 5 commentary.**
   Latin: *quibus significare videtur æterna desolatio in hoc sæculo, et æterna damnatio in futuro*
   English: "by which words eternal desolation in this world, and eternal damnation in the world to come, seem to be signified"
   Problem: the print has *significare* (PDF 357, checked), but *desolatio* and *damnatio* are nominative, so the active infinitive does not construe; the sense needs *significari*. The English rightly gives the passive, but STYLE says a misprint translated by the sense gets a translator's note, and Mose's header should list the form.
   Fix: add a note: "the print has *significare* (to signify); translated as *significari* (to be signified), which the nominatives require." Mose adds "significare videtur" (p. 346) to "Forms kept as printed".

## Nit (optional)

1. v. 1 commentary: *sic enim ad verbum legitur in hebraico* "for so to the word it is read in the Hebrew". Suggest "for so it is read word for word in the Hebrew".
