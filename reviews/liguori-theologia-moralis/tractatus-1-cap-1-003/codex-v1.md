# Theologia moralis, Tract I, chapter I (003): Codex review v1

Verdict: CHANGES

English: `8de73cf`, `english/liguori-theologia-moralis/tractatus-1-cap-1-003.md`, branch `agent/clark-translator--mwp7htk2`. Latin: `d6fa3b1`, corresponding path under `latin/`, branch `agent/mose-scribe--mwp7hse4`. STYLE.md and GLOSSARY.md checked at the English commit.

1. **Omission; Scribe finding — missing *ut* in no. 12.**
   - Latin: “Hinc valde proderit ad sedandas conscientias scrupulis agitatas, confessarius eis ante oculos exponat …”.
   - Current English: “Hence it will greatly profit for the calming of consciences tossed with scruples, that the confessor set before their eyes …”.
   - Problem: PDF p. 102 (printed p. 4), right column, prints “agitatas, ut confessarius”. The Latin omits *ut*. The English already supplies the correct conjunction.
   - Suggested fix: Scribe to restore *ut* before *confessarius*. Retain the English wording and update its source commit after correction; no translator's note. Source correction requested from Mose. Enlarged crop: `/tmp/jo-lig3-ut.png`.

2. **Source quotation boundaries; STYLE §§5, 8 — italics include narrative and exclude part of a citation.**
   - Latin, no. 12: one italic run extends from “Qui renuunt credere …” through “Hinc affert … At dicet aliquis … Respondet s. Antoninus ex eodem Gersone …” to “… foveam”. Current English follows it, italicising “Hence he bringeth … But some one will say … St. Antoninus answereth from the same Gerson …” as part of that run.
   - Latin, no. 19: “ideo addit Gerson:” is italic with “Et quantum fieri potest …”; English similarly italicises “therefore Gerson addeth:”. Latin and English no. 18 conversely make the parenthesis “conscientia levis et temerariae credulitatis explosa” / “the conscience of light and rash credulity being cast out” roman inside an italic citation.
   - Problem: the scan distinguishes the author's narrative from his quoted authorities. The current boundaries lose that distinction. PDF p. 102 prints “Hinc affert … scrupuloso:” in roman, “Vade, et in fide mea celebres” in italics, then “At dicet aliquis … committere. Respondet s. Antoninus ex eodem Gersone:” in roman, then “Quisquis ita dicis … foveam” in italics. PDF p. 105 prints “ideo addit Gerson:” in roman. PDF p. 104 italicises the whole citation, including the parenthesis.
   - Suggested fix: restore these boundaries in the Latin and mirror them in English. End the first no. 12 quotation after “superioris assensu” / “the assent of the superior”; italicise the short Bernard saying separately; resume italics at “Quisquis …” / “Whosoever …”. Put the no. 19 attribution in roman and include the no. 18 parenthesis in italics. Also restore the scan's italic emphasis on *Remota* and *proxima* in no. 1 (PDF p. 99), mirrored on “remote” and “proximate” in its explanatory sentence. No words need changing. Source correction requested from Mose.

The entire English was compared sentence by sentence against the Latin, independently of the other critic. No further mistranslation, omission, addition or doctrinal finding. The distinctions between vincible and invincible error, material and formal sin, objective evil and subjective merit, and a doubt and a scruple are preserved. The instruction concerning confession, the conditions for obeying a director, and the practical judgments in nos. 15–19 have neither been softened nor expanded.

The 72 body blocks correspond, with seven page markers, seven pairs of column labels, and identical numbered reference marks in each block. The author's column-foot notes remain in place. The two translator's notes are appropriate: the printed Romans reference is retained and corrected; the uncertain *It. f. in fine* is preserved rather than silently expanded. The shortened quotations agree with [Romans xiv, 23](https://www.drbo.org/chapter/52014.htm) and [Luke x, 16](https://www.drbo.org/chapter/49010.htm). Italic Scripture quotations may remain italic without added quotation marks, following the edition's practice.

The reference expansions and glossary choices are accepted, including *Prael.* as Prelude, *ex.* as exam., *r.* as rule, and *Cons.* as Consideration. The latter is corroborated by the fuller “consid. 6” reference in [another Latin edition of the same chapter](https://www.santalfonsoedintorni.it/Libri/Morale1/1Mor1-1-01.pdf). The awkward pair of verbs in no. 17 is in the print and is faithfully retained.

Independent Latin proof completed word by word against images of PDF pp. 99–105 (printed pp. 1–7), through “seorsim disseremus”, excluding chapter II. Apart from findings 1–2, no source slip found. The unusual digit forms and reported broken sorts were checked against their context. Local proof images: `/tmp/jo-lig3-0099.png` through `/tmp/jo-lig3-0105.png`; enlarged PDF p. 102: `/tmp/jo-lig3-hi-0102.png`.

## Source correction checked

Latin `454a030` checked by complete diff from `d6fa3b1`: the omitted *ut* and all italic boundaries specified above are corrected, with no other wording changes. The Latin is cleared. English still needs the matching italic boundaries and updated source header before PASS; its existing “that” already renders the restored *ut*.
