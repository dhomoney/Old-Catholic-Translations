# Psalm 36: Codex review v1

Verdict: CHANGES

English: `f31e76f`, `english/psalm-036.md`, branch `agent/clark-translator--mwp7htk2`. Latin: `07e4154`, `latin/psalm-036.md`, branch `agent/mose-scribe--mwp7hse4`.

1. **Scribe finding; STYLE §5 — PDF p. 244 marker is late.**
   - Latin: the verse 10–11 commentary currently includes “Beati mites, quo- / niam ipsi possidebunt terram” and the rest through “quam pax adferre secum solet” before `<!-- p. 233 (PDF 244) -->`.
   - Current English: “Blessed are the meek: for they shall possess the land” and the remaining commentary through “which peace is wont to bring with it” likewise precede that marker.
   - Problem: PDF p. 243 ends with “quo-”; PDF p. 244 begins “niam ipsi possidebunt terram”. The first nine lines of printed p. 233 are consequently assigned to the wrong page in both files. This is a source-layout error, not an English omission.
   - Suggested fix: move the marker inside this paragraph to a whole-word boundary beside the joined *quoniam* (for example, immediately before it), and rejoin the word. Split the corresponding English beside “for they shall possess the land”. Keep the following commentary after the marker. Source correction requested from Mose.

2. **Scribe finding; STYLE §5 — PDF p. 248 marker is missing.**
   - Latin, verse 37–38 commentary: “Ita nulla supersunt vestigia tantæ / potentiæ: et tamen humana superbia …”.
   - Current English: “So no traces remain of so great / power: and yet human pride …”.
   - Problem: printed p. 236 ends after *tantæ*; printed p. 237 begins *potentiæ*. Neither file contains `<!-- p. 237 (PDF 248) -->`. Both silently run into the final page.
   - Suggested fix: insert that marker after *tantæ* and before *potentiæ*, and after “so great” and before “power” in English. Preserve paired paragraph continuations. Source correction requested from Mose.

3. **STYLE §3 — the Apocalypse quotation differs from the Vulgate and needs a note.**
   - Latin, verse 39–40 commentary: “Opera enim bona sequuntur illos, qui in Domino moriuntur”.
   - Current English: “For good works follow them who die in the Lord,” followed by *Apoc.* xiv.
   - Problem: the English correctly follows Bellarmine, but *bona* is an added qualification, not merely shortening or changed word order. He also joins the reference to those who die in the Lord to the statement about their works. [Apocalypse xiv, 13](https://www.drbo.org/drl/chapter/73014.htm) has “opera enim illorum sequuntur illos”, in the Douay-Rheims “for their works follow them”. His quotation is printed as given on PDF p. 248, right column, verse 39–40 commentary, lines beginning “post mortem ejus. « Opera enim bona sequun-”.
   - Suggested fix: retain the English and add a short translator’s note: “Bellarmine paraphraseth Apoc. xiv, 13, joining its clauses; the Vulgate has opera enim illorum sequuntur illos, in the Douay-Rheims ‘for their works follow them’.”

Independent English comparison completed sentence by sentence for the entire unit. No meaning-affecting English findings. The treatment of providence, poverty, temporal prosperity, grace and final recompense preserves the author’s distinctions. The marginal question at verse 23 is awkward but faithfully translates the surviving printed reading. The readings discussed as words, the literal glosses beside the Douay-Rheims wording, and the glossary choices are sound. No note is needed for the spelling-only forms *possesionem* and *Suzannæ*.

The verse mapping in note 1 was checked against [Douay-Rheims Psalm 36](https://www.drbo.org/chapter/21036.htm), including the unnumbered Daleth and Caph clauses, the divided verse 14, and the divided verse 28. His cross-reference to common verse 16 is properly explained. The existing notes correctly distinguish source readings from the intended words or references. The extended [Wisdom v](https://www.drbo.org/chapter/25005.htm) quotation is shortened as the author shortens it; no further note is needed for those omissions. His [Psalm lxxii](https://www.drbo.org/chapter/21072.htm) quotation is preserved with the words his argument discusses beside it.

Independent Latin proof completed word by word against zoomed images of PDF pp. 240–248 (printed pp. 229–237), excluding the editorial material. No lexical Scribe slips found; the source findings are the two page-marker errors above. Printed *cum justitia*, the incorrect book/chapter reference, *justus semper loquitur*, the Hebrew initial iod and the source’s other reported oddities were checked. The text currently has 138 corresponding blocks including eight page markers, and ten English footnotes. Correcting the page divisions will change the block count; recheck after both files are amended.

Local proof images: `/tmp/jo-ps36-240.png` through `-248.png`; enlarged reading crop `/tmp/jo-ps36-endreading.png` and margin crop `/tmp/jo-ps36-margin.png`.

## Source correction checked

Latin `17f6b14` checked by complete diff from `07e4154`: both page-marker findings are resolved. PDF p. 244 now starts at the printed continuation *niam ipsi possidebunt terram*; the retained *quo-/niam* split follows the scan and is accepted. PDF p. 248 begins before *potentiæ*. No words were changed. The Latin is cleared. The English still needs the matching paragraph divisions and updated source header, together with finding 3’s Apocalypse note, before the unit passes.
