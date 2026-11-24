# Psalm 39: Codex review v1

Verdict: CHANGES

English: `51587d2`, `english/psalm-039.md`, branch `agent/clark-translator--mwp7htk2`. Latin: `edf1c13`, `latin/psalm-039.md`, branch `agent/mose-scribe--mwp7hse4`. STYLE.md and GLOSSARY.md checked at the English commit.

1. **Scribe addition and damaged sort — the Trent sentence.**
   - Latin, verses 9–10 commentary: “tum quia lectio latina vulgata edit.o approbata est in concilio Tridentino”.
   - Current English: “and because the Latin reading of the Vulgate edition was approved in the council of Trent”.
   - Problem: PDF p. 271 (printed p. 260), left column, has “tum quia latina vulgata edit.o approbata est in concilio Tridentino”. There is no *lectio* before *latina*. The inserted word changes the statement about approval of the edition into a statement about approval of the reading. The damaged word is *editio*.
   - Suggested fix: Scribe to remove *lectio*, restore *editio*, and record the damaged sort in the header. English: “and because the Latin Vulgate edition was approved in the council of Trent”. No translator's note for a Scribe error. Source correction requested from Mose. Clear enlarged crop: `/tmp/jo39-trident.png`.

2. **Scribe damaged sort — *forta-se*.**
   - Latin, same commentary: “et forta-se in textu hebraico antiquo”.
   - Current English: “and perhaps in the ancient Hebrew text”.
   - Problem: PDF p. 271 has a broken sort within *fortasse*, represented in the transcription by a hyphen. It is not a compound or a word divided between lines.
   - Suggested fix: transcribe *fortasse* under the standing worn-sort rule, with the header noting the damaged sort. Retain the English. Source correction requested from Mose; same enlarged crop as finding 1.

3. **STYLE §3 — the Baptism/Transfiguration reference needs a note.**
   - Latin, verse 12 commentary: “Deinde a Baptismo, in quo dictum est a Patre: « Ipsum audite »”. Earlier in the paragraph stands “Matth. III et XVII”.
   - Current English: “Then from his Baptism, in which it was said by the Father: ‘Hear ye him’”. The earlier reference is retained as *Matt.* iii and xvii.
   - Problem: the English faithfully reproduces the print, including its reference placement, but “Hear ye him” belongs to the Transfiguration at [Matthew xvii, 5](https://www.drbo.org/chapter/47017.htm). The Father's words at the Baptism in [Matthew iii, 17](https://www.drbo.org/drl/chapter/47003.htm) do not include that command. The source has conflated the two occasions.
   - Suggested fix: retain the text and its reference placement; add a short translator's note at “Hear ye him”: “So the print. These words were spoken at the Transfiguration, Matt. xvii, 5, not at the Baptism, Matt. iii, 17.”

4. **Addition; STYLE §3 — do not restore the omitted *Dei* inside the Psalm quotation.**
   - Latin, verse 11 commentary: “De justis dicitur in Psalm. XXXVI: « Lex ejus in corde ipsius »”.
   - Current English: “Of the just it is said in Ps. xxxvi: ‘The law of his God is in his heart’”, with note 9 explaining the difference.
   - Problem: *God* renders the *Dei* of the full [Psalm xxxvi, 31](https://www.drbo.org/drl/chapter/21036.htm), but Bellarmine omits that word. STYLE §3 requires translating the author's shortened quotation as given. A note identifying his wording does not justify restoring the omitted word in the body.
   - Suggested fix: “Of the just it is said in Ps. xxxvi: ‘His law is in his heart’”. Note 9 may remain to identify the full Vulgate reading.

The entire English was compared sentence by sentence against the Latin, independently of the other critic. No further mistranslation or doctrinal finding. The treatment of preventing grace, the sacrifice of Christ, his knowledge of every sin, and the difference between literal ignorance and outward signs of wonder preserves the author’s distinctions.

The verse 9 lemma may keep “thou hast pierced ears for me” under the standing Douay-Rheims rule. Note 5 clearly distinguishes it from the Vulgate *perfecisti* which Bellarmine defends, and the full commentary preserves the competing readings. No exception to STYLE §3 or ruling from god is needed for the present treatment. The shortened title correctly omits “himself”.

The 101 body blocks correspond, including all seven page markers and marginal glosses; ten translator's notes. Note 1 correctly maps the twenty-four verses to the eighteen of [Douay-Rheims Psalm 39](https://www.drbo.org/chapter/21039.htm). The existing notes on John xiv, Psalm xviii, *replebit*, Hebrews x, the Kings reference, *In auditu auris perfecisti mihi* and the misplaced Matthew xvii reference are appropriate. The Latin supplied beside words discussed as readings preserves the argument; the glossary choices are sound.

Independent Latin proof completed word by word against PDF pp. 268–274 (printed pp. 257–263), excluding the editor's notes before the exposition. Findings 1–2 are the source corrections required; no other source slip found. The printed “Matth. III et XVII” and “Psalm. XXXVI” were verified in enlarged images, as were the disputed words in the Trent sentence. The Greek, Hebrew (including the print's reported defective forms), damaged margins, quotations and page divisions were checked. Local proof images: `/tmp/jo39-268.png` through `/tmp/jo39-274.png`; enlarged PDF pp. 271–272: `/tmp/jo39-hi-271.png`, `/tmp/jo39-hi-272.png`.

## Source correction checked

Latin `7728cdc` checked by complete diff from `edf1c13`: the inserted *lectio* is removed, *editio* and *fortasse* are restored, and the header records the damaged sorts. No other changes. Findings 1–2 are resolved in the source and the Latin is cleared. The English still needs finding 1's matching Trent sentence, findings 3–4, and the updated source header before PASS.
