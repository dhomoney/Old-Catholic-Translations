# Review: Liguori, Theologia moralis, Tract. I, cap. 2 (unit 004), English v1 (Claude critic)

- English: branch agent/clark-translator--mwp7htk2, commit 376cff2, english/liguori-theologia-moralis/tractatus-1-cap-2-004.md
- Latin: branch agent/mose-scribe--mwp7hse4, commit b9075b1, latin/liguori-theologia-moralis/tractatus-1-cap-2-004.md (PDF pp. 105-112)
- Reviewer: Charles (Claude critic), 2026-11-28

## Verdict: PASS

No finding affects the meaning. Finding 1 is a STYLE note that Clark already offered to add; finding 2 is for the Latin file. Five nits, all optional.

## Checks made

- Block-for-block check: Latin 79 blocks, English 79 blocks, MATCH.
- Every block compared with the Latin: the list of sections, nn. 20-39, and all page footnotes.
- Doctrine: negative and positive doubt; speculative and practical doubt; never to act with a practically doubtful conscience; reflex principles; *lex dubia non obligat* and *melior est conditio possidentis*; presumption and burden of proof; law, vow, obedience, fast, marriage debt, payment of debt; the possessor in good faith (nn. 35-37, with Liguori's reconciliation in n. 36 and his own opinion in n. 37); communion when in doubt of having broken the fast (nn. 38-39). All rendered faithfully.
- Scripture: Ecclus. iii, 27 matches the Douay-Rheims (drbo.org): "he that loveth danger shall perish in it".
- GLOSSARY: the 19 new rows are followed throughout (in possession, we must stand for, in proportion to the doubt, opinative assent, to ask / to render, positive / prohibitive law, resol. / resp.).
- Scan crops at 300 dpi: PDF 107 "29. Dicunt tamen plures auctores, quod si quis"; PDF 109 "In re communi melior est conditio possidentis (5)" and footnote "(5) Reg. 56. de reg. iur. in 6."; PDF 110 "unicumque iudicium opinativum tunc ipsa haberet". All three are printed as in the Latin file.

## Clark's points

1. n. 29 *Dicunt ... an teneatur*: agreed, printed so (PDF 107); the sense ("ask") and note 1 are right.
2. n. 35 Reg. 56: the print has *melior ... possidentis* and "Reg. 56" (PDF 109). Reg. 56 of the Sext's title *de regulis iuris* is *In re communi potior est conditio prohibentis* (confirmed in the list of the Sext's rules, Wikipedia "Regulae Iuris"). Note 2 stands.
3. n. 36 *ipsa*: printed (PDF 110). See finding 1.
4. p. 10 footnote (4): agreed, it is the Marietti editors' note ("s. Alphonsus" could only be written after his canonization, 1839). See finding 2.
5. Agreed. *The royal priesthood* is right: Sfondrati's *Regale sacerdotium Romano Pontifici assertum* (St. Gall, 1684). See nit 5 on "book 1".

## Findings

1. **STYLE (print misprint needs a note), n. 36.**
   Latin: *tunc enim vere nulla probabilitas ipsi assisteret, unicumque iudicium opinativum tunc ipsa haberet rem esse alienam.*
   English: "and he would then have the single opinative judgment that the thing is another's."
   Problem: the print has *ipsa*, which agrees with nothing that can hold a judgment; the subject must be the possessor (*ipse*). The English is right by the sense, but STYLE says a print misprint translated by the sense gets a translator's note, and the Latin header should list it (Mose's header says "Misprints kept as printed: none noted").
   Fix: add a translator's note at "he would then have": "the print has *ipsa* (she / it), for *ipse* (he)". Mose adds the reading to the header.

2. **Latin file: editors' footnote, p. 10 (4).**
   Latin: *(4) Vide Homo apost. tr. 5. n. 51. ubi s. Alphonsus eamdem quaestionem discutit.*
   English: "(4) See the *Homo apostolicus*, tract 5, no. 51, where St. Alphonsus discusseth the same question."
   Problem: this is the Marietti editors' note, not Liguori's. decisions.md (god, 2026-11-20): an editor's note is left out unless god names it a reading key. It is not one.
   Fix: Mose drops the note text and keeps the mark (4) with "[Editor's note omitted, see header.]", as for (19) on p. 11; Clark follows. No effect on meaning; a quick diff check of the next version is enough.

## Nits (optional)

1. n. 21: "for a speculative doubt, though obliquely, and rather by consequence, it regardeth the lawful, yet directly ..." The "it" breaks the grammar. Suggest: "for a speculative doubt, though obliquely and rather by consequence it regard the lawful, yet directly and principally regardeth the true".
2. p. 9 (n. 26): *ego tamen nescio, quomodo in omnibus negari possit* "yet I know not how it can be denied in all things" can be read as "denied universally". Liguori means it holds in all matters. Suggest: "yet I know not how it can be denied to hold in all things".
3. n. 32: *qui est in sabbato* "who is in the Saturday": "who is on the Saturday".
4. n. 38: *Ad secundam autem rationem irreverentiae oppositam respondent* "But to the second reason, objected, of irreverence": suggest "But to the second reason objected, that of irreverence, they answer".
5. p. 11 footnote (17): *Reg. sac. 1. §. 20. n. 11.* "book 1" is supplied; the work is laid out in four *propositiones*, so the unit is not sure. Suggest giving the number bare: "*The royal priesthood*, 1, § 20, no. 11."

Sources checked: drbo.org chapter 26003 (Ecclus. iii); Wikipedia "Regulae Iuris" (list of the Sext's rules, Reg. 56); Tübingen opendigi 15A12440 and Paderborn catalogue (Sfondrati, *Regale sacerdotium*, 1684).
