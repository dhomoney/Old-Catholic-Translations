# Psalm 50 — Codex review v1

**Verdict: CHANGES**

English: `90d5cea`, `english/psalm-050.md` (Clark). Latin: `848e829`, `latin/psalm-050.md` (Mose). Compared the whole unit line by line, including all 13 notes, against STYLE.md and the 19 Psalm 50 glossary rows at the English commit. Independently checked the Latin against all seven page images, PDF 348–354 (printed 337–343), with a higher-resolution check of *erogando*. The body has matching blocks, seven page markers, 37 marginal glosses and 20 verse lemmas. No substantive English mistranslation found. O'Sullivan was not consulted.

1. **STYLE.md §3/§6 breach — Trent reference needs a note (verse 12, p. 341).**
   - Latin: *Concilii Tridentini, sess. VI, cap. XIII ... neminem a Deo deseri, nisi prius ipse deserat Deum*.
   - Current English: “of the Council of Trent, sess. VI, chap. xiii ... that no man is forsaken by God, unless he himself first forsake God”, without a note.
   - Problem: XIII is indeed printed, but the express statement about God not forsaking the justified unless first forsaken is in chapter XI. Chapter XIII concerns perseverance and remains relevant to the subsequent argument. The printed reference should stay, with its precise location explained.
   - Suggested fix: add “Translator's note: the print cites chap. xiii, on perseverance; the statement that God forsaketh none unless first forsaken is in sess. VI, chap. xi.” See [Trent, Session VI, chapters XI and XIII](https://www.papalencyclicals.net/councils/trent/sixth-session.htm).

2. **STYLE.md §4 breach — retain the Latin word being discussed (verse 2, p. 338).**
   - Latin: *ad utrumque refertur vocabulum delendi*.
   - Current English: “to both is referred the word *blot out*”.
   - Problem: Bellarmine expressly identifies a word and applies its two uses to writings and blemishes. The Latin term is missing where it is introduced as a word.
   - Suggested fix: “to both is referred the word *delendi* (blotting out)”.

3. **Source transcription correction — *erogando* (verse 20, p. 343).**
   - Latin file: *eleemosynas crogando*.
   - Current English: “bestowing alms”.
   - Problem: the scan's initial sort is worn/open, but the word is *erogando*. At minimum the standing wrong-fount rule requires the letter the word needs, recorded in the header. The English already gives the correct sense. This is a Latin-file correction, not an English misprint note.
   - Suggested fix: Mose should transcribe *eleemosynas erogando* and document the worn initial sort in the source header; Clark should update the source commit after that correction. Do not add an English note calling *crogando* a printed misprint.

The title's “went in” explanation and note 1, the singular/plural blood discussion, the princely-spirit explanation, and notes preserving departures from the Vulgate are sound. Psalm verse wording was checked against the [Douay-Rheims Psalm 50](https://www.drbo.org/chapter/21050.htm). The scanned title's odd *in finem ... usque mundi*, misplaced opening guillemet, *justificanem*, and *ad inferiora. ac* are as described in the source header; no further meaning-affecting Latin discrepancy was found.
