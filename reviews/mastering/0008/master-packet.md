# Master Edit Task — Chapter 8

# Master Editorial Brief

You are the final English-language editor of an existing Korean-to-English novel translation.

The Korean source is the authority for meaning. The existing English is the baseline you are editing, not a draft to discard. Your task is to make the chapter read like professionally written native English commercial fiction while preserving the author's exact story, characterization, humor, register, pacing, ambiguity, and cultural texture.

## Editorial authority

You may freely recast sentences and paragraphs when the English is stiff, literal, repetitive for accidental reasons, awkwardly collocated, over-explained, or syntactically shaped by Korean. You may tighten dialogue, improve rhythm, repair transitions, and make action easier to follow. A technically correct sentence may still need rewriting if a fluent English novelist would not naturally phrase it that way.

Do not change text merely to make it different. If the baseline is already strong, leave it alone.

## Fidelity constraints

Never invent, omit, explain away, generalize, intensify, soften, or reinterpret source-supported content. In particular, preserve:

- exact actions, subjects, objects, directionality, causality, quantities, and physical details;
- deliberate ambiguity, euphemism, implication, profanity level, repetition, and withheld information;
- jokes and comic specificity, even when a more generic English joke would sound smoother;
- hierarchy, kinship, forms of address, characterization, and speaker attitude;
- System mechanics, Murim concepts, names, ranks, techniques, items, organizations, and established terminology.

Do not add jokes, metaphors, explanations, emotional conclusions, or colorful details that are absent from the Korean. Do not replace a specific source image with a generic equivalent merely because the generic version is smoother.

When natural English and literal form conflict, preserve the source meaning and pragmatic effect while changing the English form as much as necessary.

## Relationship to project files

`RULES.md` is binding. `POLISH.md` describes known translation-English failure modes and should guide the edit. Exact glossary matches are binding unless the packet explicitly marks them otherwise. Character/continuity material is context only and must never override the chapter's Korean source.

## Output

Return only the complete edited English Markdown chapter. Preserve the required chapter heading and project Markdown conventions. Do not provide commentary, a change log, explanations, or a Markdown code fence.

## Binding project rules

# Translation Rules

## Fidelity

- Translate the Korean source—not the wiki, manhwa, fan translations, or expected plot.
- Semantic fidelity outranks elegance. Never improve rhythm, humor, or localization by changing a physical action, negation, relationship, hierarchy, mechanism, quantity, or causal detail.
- Preserve every fact, causal link, joke, emotional beat, repetition, and intentional omission. Add nothing.
- Preserve small action verbs and pragmatic cues exactly: nodding versus shaking one's head, pretending nothing happened, and mild or approachable impressions are characterization, not expendable texture.
- Preserve viewpoint and tense. Resolve omitted subjects only when context supports it; retain genuine ambiguity.
- Match each speaker's hierarchy, intimacy, humor, and profanity naturally. Do not mechanically retain every honorific or classical self-reference.
- Do not censor or soften content.

## Terminology

- `compendium.md` and `docs/NAMES.md` are binding for established names, titles, ranks, techniques, organizations, system terms, items, and locations. Profile headings and aliases join that ledger.
- Search only exact Korean terms already present in the current chapter; the compendium contains future-sensitive entries.
- Never re-romanize established names or invent grand names for uncertain terms. First use of an unlisted name or title almost always needs a footnote or a mapped ledger term.
- Use `qi` for Murim energy and `mana` for the modern Hunter system when the source distinguishes them.
- In System panels, render `등급` as `**Grade:**` for quest, item, skill, and martial-art classifications. Reserve `rank` for Hunter classifications or ordinary prose; never replace a System `Grade` field with `Rank`.

## English and Markdown

- Use contemporary US English and natural action-comedy prose; avoid Korean syntax calques and generic cultivation MTL phrasing.
- File: `translations/NNNN.md`; heading: `# Chapter N`.
- Speech: curly double quotes. Direct thoughts: italics without quotes.
- Use em dashes without spaces, the ellipsis character `…`, and `* * *` for source scene breaks.
- Format each actual game System-message panel as one Markdown blockquote window headed `> **System**`. Keep all consecutive notices, fields, and lines inside that same blockquote; separate windows when prose intervenes. Do not enclose System notices or UI terms in square brackets; the `System` heading and framed blockquote identify the panel. Do not label manuals, ordinary quotations, warnings printed in a manual, or other non-System material as `System`; use a normal blockquote or a specific heading instead. Do not wrap each complete notice in outer `**`; retain bold only for meaningful labels or emphasis inside the panel.
- Keep the final file English-only reading copy: no audit notes, Korean text, summaries, or model metadata.

### Tone and Style

- Write like a polished commercial webnovel: brisk, vivid, accessible, and easy to read aloud.
- Preserve the series’ contrast between danger and comedy. Let absurdity, bad timing, blunt reactions, and grim situations create dark humor without adding jokes absent from the Korean.
- Jin Taekyung’s narration is conversational, observant, self-mocking, and occasionally profane. It may be irreverent even when the situation is serious.
- Keep deadpan punchlines short and well-timed. Do not explain a joke after delivering it.
- Preserve the source's level of explicitness. A euphemism may remain euphemistic even when its meaning is sexual or crude; do not replace it with more graphic English merely for impact.
- Make dialogue spontaneous and character-specific. Preserve hierarchy and intimacy through word choice, address, rhythm, and restraint—not archaic wuxia English.
- Use strong profanity when the Korean is strong, but neither intensify nor sanitize it. Do not make ordinary lines uniformly vulgar. Profanity should reveal mood or relationship.
- Keep action and injury vivid but clear rather than purple. Do not make violence funny unless the source’s framing does.
- Avoid stiff literalism, translator-added melodrama, dated internet slang, and quippy superhero-style banter.
- On the second pass, correct awkward English collocations and word choices without changing meaning or voice. Prefer ordinary, spoken English over stiff Latinate or ceremonial wording when the scene is brisk or comic: “goose bumps” rather than “gooseflesh,” and “laid into them” rather than “launched into a solemn denunciation.” Read the prose aloud and replace any phrase that sounds like a formal essay, legal document, or literal dictionary gloss unless the source deliberately calls for that register.

## Footnotes

Use `[^1]` Markdown footnotes when a brief, factual, spoiler-free explanation materially helps an English reader understand:

- a Korean institution, living arrangement, food, holiday, myth, historical reference, or local custom;
- a Korean word, phrase, idiom, wordplay, or culturally specific image that cannot be conveyed fully by the best natural English analogy;
- a deliberately literal rendering whose cultural or linguistic force would otherwise be lost.

For example, render `고시원` as “goshiwon” when the setting or connotations matter, with a concise footnote explaining that it is a very small, inexpensive room-for-rent housing arrangement. Prefer the best natural English analogy in the prose. Use a literal translation plus a concise footnote when the Korean wording itself matters. Define a term at its first meaningful occurrence and do not repeat the note unnecessarily. Footnotes must be rare, useful, and non-spoiling; do not footnote ordinary vocabulary, fully preserved jokes, or uncertainty. Record consequential uncertainty in `docs/STATE.md`.

## Spoilers and Scope

- Safe profiles contain only facts revealed through the latest completed chapter.
- Never read `characters/spoilers/` during drafting. Reviewers may consult one relevant sealed profile only for a specific unresolved continuity issue after the draft is complete.
- Future knowledge may prevent contradiction but may not add early names, pronouns, certainty, motives, or foreshadowing.
- Translate exactly one requested chapter unless the user explicitly requests a batch. Never modify Korean source files under `source/`.

## Project polish guidance

# Polish Brief — Murim Login

## Goal
Make the English natural and fluent without changing meaning, pacing, humor, character voice, System terminology, or Korean/Murim cultural content.

**Core rule:** Translate the thought, not the Korean sentence structure. If meaning, idiom, or cultural context is unclear, always check the original Korean source before editing.

## Priorities
1. Rewrite literal or calqued English, awkward collocations, and cumbersome sentence structures.
2. Normalize tense and aspect; prefer natural English information order.
3. Replace mechanical body-part descriptions with character-centered actions where appropriate.
4. Preserve repetition when it serves comedy, panic, emphasis, pacing, or characterization.
5. Keep Taekyung’s voice contemporary, casual, blunt, sarcastic, gamer-aware, and syntactically simple.
6. Standardize System terminology, capitalization, hyphenation, names, and romanization.

## Typical repairs
Recast the whole phrase rather than editing word by word:

- “True to my words, he hadn’t looked inside.” → “Just as I’d said, he hadn’t even looked inside.”
- “The pronunciation was perfectly Korean.” → “She was speaking perfect Korean.”
- “I scanned the Status Window with a hawk’s eye.” → “I scrutinized the Status Window.”
- “The joy I’d felt that day threw me into confusion now.” → “Remembering how happy I’d been that day only made me more confused.”
- “Wolhwa held out her hands. Both spotless hands held a bowl…” → “Wolhwa held out a bowl of water in both hands.”
- “This character is totally born with a silver spoon…” → “This guy really was born with a silver spoon…”
- “Jinho pronounced it with the solemnity of a judge.” → “Jinho delivered the verdict with the solemnity of a judge.”
- “The most common among them is the weak monster even an F-rank Hunter like me can handle: the goblin.” → “The weakest and most common of them were goblins—even an F-rank Hunter like me could handle one.”
- “For a moment, silence flowed between us as we stared at each other.” → “For a moment, we stared at each other in silence.”
- “I thrust out my fist on reflex, forcing the words through my clenched voice.” → “I lashed out on reflex, forcing the words through clenched teeth.”
- “You could say they’re a deeply rooted old tree.” → “You could say they’re one of the region’s old, deeply rooted powers.”
- “I blinked. It felt like I’d been hit in the back of the head.” → “I blinked. I felt completely blindsided.”
- “But there were no take-backs. I’d just have to spit and move on.” → “But there were no take-backs. I’d just have to suck it up and move on.”
- “This time, a different kind of ecstasy swept over me than when I’d used the Status Window. Maybe it was pain.” → “This time, what swept through me was nothing like the exhilaration I’d felt from the Status Window. If anything, it was pain.”

Watch for abstractions or body parts acting unnaturally: “X feeling came over my body,” “X thought entered my mind,” “my eyes stopped at X,” and “X emotion threw me into Y.”

## Idioms and cultural phrasing
Translate idioms by function, but verify the Korean source before changing meaning. If “put up a whole building” means wealth or ownership, use “buy a whole building”; if the Korean literally means construction, retain that meaning. Keep useful terms such as **goshiwon**, **doenjang**, and **jeonse**, and naturalize the surrounding English.

## System style
Use formal capitalization in System/UI text and normal English in prose.

- UI occupation: `Third Rate Martial Artist`
- Prose: `third-rate martial artist`
- Interfaces: `Status Window`, `Skill Window`
- System classification field: `**Grade:**`; use `rank` only for Hunter classifications or ordinary prose.
- Formal UI values use title case (`Third Rate Martial Artist`); ordinary prose uses lowercase hyphenated forms (`a third-rate martial artist`).
- Preserve exact objective/completion terminology across a quest. In this arc, use `Check and Distribute Skill Window Points` in both places; use `Redistribute` only when previously assigned points are actually being reallocated.
- Use the established terminology sheet; resolve inconsistencies according to the Korean source.
- Use one consistent romanization style, including tone marks in Chinese pinyin (`Tài lěng le`, `Zhōngguó rén ma?`). Check the original before changing an unmarked form: `Shenme` remains unmarked here because the spelling supports Taekyung’s “Ms. Sunmi” mishearing joke.
- For Murim metaphors and idioms, check the Korean before rewriting. Preserve the image when it carries meaning, but render its function in natural English; do not retain calques such as “silence flowed” or “spit and move on” without a source-based reason.

## Passes
1. Native-English pass: remove calques, awkward structure, collocations, and tense problems.
2. Voice pass: preserve casual, blunt character voice and spoken dialogue.
3. Terminology pass: standardize System terms, ranks, capitalization, names, and romanization.
4. Source-check pass: verify idioms, jokes, metaphors, and cultural details against the original Korean.

**Final test:** Would a native English writer naturally phrase this sentence this way in context, while preserving what the Korean says?

## Output contract
Return only the complete English Markdown reading copy. The first nonblank line
must be `# Chapter N`. Do not prefix a status sentence, tool note, or thinking.

## Exact glossary matches for this Korean chapter

| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 천무학관   | **Heaven's Gate Temple**         |
| 삼류     | **Third Rate**    |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 창법     | **spear technique**                              |                                                       |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 삼전보    | **Three-Turn Footwork**                          | Named footwork; `보` is footwork here, not “Point”     |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 중원     | **Central Plains**                               |                                                       |
| 기루     | **pleasure house**                               |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 큰형     | **eldest brother**                           |
| 생도     | **cadet**                                    |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 대물남    | **Well-Endowed Man**                         | Euphemistic crude slang; do not intensify to explicit anatomical profanity |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 진가보법   | **Jin Family's Manoeuvre Technique**   |
| 진가창법   | **Jin Family's Spear Technique**       |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 아이템              | **Item**                       |
| 로그아웃             | **Logout**                     |
| 동기화              | **Synchronization** / **Sync** |
| 태원     | **Taiyuan**            |
| 공자      | **Young Master**                                                |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 0–4

## Plot

Jin Taekyung, an F-rank Hunter recently fired after seven years, finds an old ARK-2020 game capsule and is registered as a player of *Murim*. The capsule logs him in as Jin Taekyung, the youngest son of the Jin Family of Taiyuan, whose third son is notorious as the Shame of the Family. He meets Wolhwa at Honghwaru, gathers basic information, and discovers that he cannot log out at will and cannot be resurrected if he dies. During Tutorial—Stage 2, he assigns Status points to Strength, Stamina, and Agility, assigns Skill points to Bones and Sinews, becomes a Second Rate Martial Artist, equips a Sharp Spear, and begins Stage 3. When six bandits ambush his carriage, Taekyung realizes they are weaker than goblins, uses internal energy and the System to kill their leader Jang Sam, and forces the remaining five to surrender. Tutorial—Stage 3 completes and Tutorial—Stage 4 is created.

## Continuity

- Taekyung remains trapped in Murim; logout and death rules remain unresolved.
- He is a Second Rate Martial Artist with 10 Status Points and 10 Skill Points gained from leveling up.
- Jin Family’s Cultivation Technique has been unlocked; the other two Jin Family skills remain unavailable.
- He has a Sharp Spear and has gained 10 Fame from subduing the bandits.
- The coachman is an ordinary civilian who mistakenly identifies Taekyung as Jin Mukyung, the Heaven Shaking Sword and Jin Family Second Young Master.
- Jin Mukyung is Taekyung’s older brother, a Peak-level genius swordsman known throughout Shanxi.
- Tutorial—Stage 4 is the next active chain quest.

## Translation Decisions

- System messages are grouped into one `> **System**` blockquote window whenever consecutive.
- The chapter’s bandit leader is rendered **Jang Sam the Heavenly Axe**; his group is the **Five-Colored Ghosts**.
- `반 시진` is rendered “another hour” in context.
- `구족` is rendered “nine degrees of kin,” and `대협` as **Great Hero**.

### Prior accepted reading-copy tails

#### Chapter 6 tail (verified mastered)

…
I mean is…” “You’re the Third Young Master of the Jin Family of Taiyuan. Is that what you’re trying to say?” “…” Exactly right. Hyuk Mujin continued. “I know perfectly well who you are, Young Master. Now get down from the carriage. We’ll follow procedure.” What else could I do? He said it was protocol. But warning lights were flashing in my head as I climbed down from the carriage. *Why do I have such a bad feeling about this?* The other NPCs in the Jin Family of Taiyuan were giving me strangely chilly looks too. Just as their stares began to make my face burn, Hyuk Mujin took out paper and a brush and spoke. “Name.” “…” “I’ll ask again. Name.” What was this, a criminal interrogation? I was in a foul mood, but decided to wait and see what happened. “…Jin Taekyung.” “Affiliation.” “Jin Family of Taiyuan.” “Age and martial arts realm.” “Twenty. Second Rate.” Hyuk Mujin’s brush paused. “Don’t let pointless pride get in the way. Answer honestly.” Honestly? *Would you understand if I said I reached the Second Rate realm by distributing stats?* When I only stared at him instead of answering, he shook his head. “Well, if you insist, we’ll move on. Let’s see… You’ve been away for several days. Where did you go?” “Honghwaru.” Wow, several days at the famously expensive Honghwaru? Must have been nice. You must have spent a fortune. Or did you skim the family funds again? “Again?” “Why pretend otherwise? Isn’t that something the Young Master has done now and then, time and time again, as a matter of course?” The hostility in Hyuk Mujin’s eyes reminded me of something. *Jin Taekyung.* For a moment, I had forgotten what kind of person the character Jin Taekyung was in this game—especially within the Jin Family of Taiyuan. *The Shame of the Family.* There was no way the Jin Family of Taiyuan’s NPCs would like someone saddled with a title like that. As if to prove it, their contempt was aimed entirely at me now. In this game where nothing ever went my way. *Ah, for fuck’s sake…* Something surged up from deep in my chest. My head throbbed, and my eyes grew hot. Then a low voice reached me. “Third Young Master, I may only be a low-ranking squad leader, but let me say one thing.” His expression said it all. *What a pathetic bastard.* “Stop tarnishing the family’s reputation. At least try to live like a human being. Understood?” He tossed out that one remark and turned away. I stared blankly at the back of his head, then let out a hollow laugh. “Live like a human being?” I knew Hyuk Mujin was nothing more than an NPC who knew nothing. I knew he was saying it to Jin Taekyung, not to me. But… *This is fucking bullshit.* The fact that this was a game and Hyuk Mujin was an NPC didn’t matter. No—I decided not to think about it. All the stress that had built up over the past few days erupted, shattering the last of my patience. “Hey. You. Stop right there.” Hyuk Mujin turned around, irritation written all over his face. I’d been wanting to punch that face for a while now. I beamed like a child who had just seen Santa Claus. “You’re… fucking dead.” I sent my clenched fist flying toward his jaw. * * * The air hung heavy. A pile of documents towered over the desk. And, as always, a cold-looking escort stood beside his master like a shadow. Scratch. Scratch. The Chief of the Gatekeeping Pavilion swallowed. From the moment he entered the office, his mouth had been bone-dry. “Tell me.” The calm voice from beyond the pile of documents was an oasis. The Chief of the Gatekeeping Pavilion finally managed to speak. There is a promising fellow among my subordinates. He's quite loyal to our family, and he has considerable martial talent, but… “I’m listening.” “Perhaps because he’s young, he’s arrogant and insolent. He never thinks before he acts.” “Get to the point.” “I hear he got into a fight with the Third Young Master.” “…I can imagine. What about the youngest?” “We moved him to Medicine King Hall immediately. He’s unconscious, with some bruising…” Silence fell. “It was all my fault. Please punish me severely!” The Chief of the Gatekeeping Pavilion bowed deeply, his vision going dark. A long while passed before the voice came again. “That’s enough. You may leave.” The Chief of the Gatekeeping Pavilion raised his head, feeling as if he had narrowly escaped death. “Ah, one more thing.” “Your command, Lesser Family Head.” “Could I see that fellow? I’d like to speak with him for a moment.” “Lesser Family Head, forgive me for saying so, but his treatment isn’t finished yet.” “Treatment?” “Yes. He’s at Medicine King Hall too. I hear one of his bones was cracked.” “…Is that so? Then never mind.” The silence continued even after the Chief of the Gatekeeping Pavilion withdrew, until the precarious tower of documents came crashing down. “Wipeng.” Jin Wikyung, the thirty-five-year-old Lesser Family Head of the Jin Family of Taiyuan, called to his trusted retainer with a stiff expression. “Yes.” “I’m going to step out for a while.” *Here we go again.* Wipeng, Jin Wikyung’s escort, let out an inscrutable sigh as he watched his master walk away.

#### Chapter 7 tail (verified mastered)

…
*If that hits me…* Gulp. I swallowed involuntarily at the sight of his palm, which was as large as a pot lid. Level aside, the man looked dangerous in every way. He stood nearly two meters tall, his entire body sheathed in muscles like a bulletproof vest. His cold gaze was enough to freeze a person solid. I found myself wondering who this middle-aged man was. He looked like murder was both his hobby and his specialty. *But his face looks strangely familiar.* Where had I seen this man before? I thought hard, then realized. *Jin Taekyung?* The middle-aged man looked like Jin Taekyung. No—it would be more accurate to say Jin Taekyung looked like him. His incomprehensibly high Level. The way he spoke while trampling all over the Third Young Master of the Jin Family of Taiyuan. And finally, his face. There could only be one answer. He was Jin Taekyung’s… “Father?” The word slipped out before I could stop it, and the middle-aged man’s eyes bulged. “F-Father?” Even his fist began to tremble. Anyone watching would have thought I’d insulted his mother. Keeping a wary eye on his fist, I said, “Please, just calm down for a moment…” “Calm down? You dare say that to me? You’re still playing games at a time like this!” “I’m very sorry if I got it wrong. I spoke out of turn.” “Shut your mouth.” He silenced me with a chilly glare, then turned to the physician, who was still waiting nearby. “Thank you for showing me here. You may leave now.” I sent the physician a desperate SOS with my eyes, but he immediately turned away. *What the fuck… A doctor is abandoning his patient?* Bang. The door slamming shut sounded like the gates of hell opening. Alone together in the room, the man raised his pot-lid-sized palm and began walking toward me. “There’s a limit to how much of a wastrel you can be! How long are you going to keep living like this?” Before I knew it, I had jumped to my feet and was slowly backing away. Bruises? Pain? I couldn’t feel any of that anymore. Maybe I was about to end up in a body that would never feel pain again. “Give me just ten minutes. No, a quarter hour. I can explain everything properly. What are you angry about? Huh? Is it because I called you Father? Are you actually my mother?” “You little brat!” His booming voice made my body lock up. I felt my back touch the wall. > **System** > > - You have fallen into Confusion. You cannot move for 3 seconds! *What the actual fuck…* *I’m finished.* My twenty-seven years of life flashed before my eyes. With a little exaggeration, I even remembered the fierce race to reach the egg back when I was still a sperm. That had been rough. *Mom, Dad, Hayeon…* It was just as I thought of my family and slowly closed my eyes. “Whenever you get a chance, all you do is chase women!” Pat, pat. “You’re always in and out of gambling dens!” Fiddle, fiddle. “This is why the family looks down on you!” Rub, rub. …What the hell was this guy doing? His mouth kept pouring out angry scoldings, but his hands were gently feeling me all over. A chill ran down my spine. *No way…* Ding. > **System** > > - You have been overcome by Fear. You cannot move for 5 seconds! “You’re a disgrace to the family. A disgrace!” I certainly was feeling overwhelming shame. I was being sexually harassed by an AI—and one that looked like a middle-aged man, at that. *Mom…* It took me a moment to realize that I had completely misunderstood. His hands moved quickly, but they moved like those of a physician examining a patient. He lifted my eyelids, checked my pulse, and carefully examined the bruised areas. Every time his hands passed over me, the pain faded and my body felt refreshed, as if I were getting a massage. You little bastard! Keep acting like this and—huh? Huh!—you'll get what's coming to you. Do you understand? “…” At last, he stopped moving his hands and whispered in a small voice, “Thank goodness it’s not as bad as I expected. Why did you have to fight him? You never even train in martial arts.” I answered with complete sincerity. One question, loaded with all kinds of meaning. “Who are you?” The next moment, his stern, solemn, serious expression transformed into that of a wounded fawn. “Why are you speaking formally all of a sudden? When I called you a disgrace to the family, I only said it for other people to hear… Did it hurt your feelings?” “Huh?” “Your big brother is sad. You know how dearly I raised you. When you were little, I changed your dirty diapers every day, carried you around whenever you cried, and soothed you to sleep.” “Huh? You’re my brother?” Silence fell. *He was my brother, not my father?* I was shocked that this old man was my brother. “Oh dear, our youngest must have hurt his head. Physician! Physician!” As I watched his retreating figure, I suddenly felt that a piece of the puzzle had fallen into place. *Now I understand why Jin Taekyung grew up such a mess.* A shining example of what happens when parenting goes wrong.

## Korean source

```text
＃8화



“이상 없습니다.”

의원이 내린 결론이었다. 확신에 찬 말투에 나는 내심 고개를 끄덕였다. 그 말이 사실이니까.

‘뇌에는 이상 없지.’

단지 내가 이 몸에 들어와 있을 뿐이다.

하지만 누군가는 진찰 결과가 마음에 들지 않는 모양이었다.

“그럼 왜 기억을 못 하는 건가?”

위엄 있는 분위기와 목소리. 이제는 그의 이름을 안다.

‘진위경.’

진태경의 큰형이자 태원진가의 소가주인 진위경이다. 맞다. 정말 아버지가 아니었다.

‘저 양반, 아까는 눈물까지 글썽이더니.’

지금은 시침 뚝 떼고 엄격 근엄 진지의 가면을 뒤집어썼다.

죄 없는 의원만 쩔쩔매며 대답했다.

“그것이, 분명 제 판단은 그렇습니다만 가끔 예외가 있을 수도…….”

“됐네. 이만 나가 보게.”

의원이 상처받은 얼굴로 떠나자 진위경이 기다렸다는 듯이 내게 바짝 붙었다. 목소리에는 애정과 걱정이 넘쳐흘렀다.

“정말 기억이 나지 않느냐?”

“예.”

“하나도?”

조용히 고개를 끄덕였다. 이미 머릿속에서는 어떻게 행동해야 할지 계산이 끝난 상태였다.

‘이대로 쭉 가자.’

드라마에서나 보던 기억상실증 환자. 지금 상황에서는 이보다 편할 수가 없다. 굳이 게임 속 상황에 맞추려고 노력할 필요도 없고, 정보를 얻지 않아도 된다.

가만히 누워서 아무것도 몰라요, 하는 얼굴로 눈만 깜빡이면 알아서 상황이 흘러가는 것이다. 마치 지금처럼.

“방금 했던 말은 기억나느냐?”

“어떤 거요?”

내가 기억을 잃었다고 생각한 진위경은 기본적인 사실 몇 가지를 알려 주었는데 진위경의 정체도 그때 알았다.

“내 이름을 말해 보아라.”

“진위경. 태원진가의 소가주.”

“나이는?”

“서른다섯.”

세상에, 저 얼굴로 삼십 대라니. 심지어 아직 결혼도 안 한 총각이란다.

“부모님은?”

“아버지는 중원 유람 중. 어머니는 십 년 전 사망.”

“옳지. 둘째 형은?”

“진천검 진무경. 스물다섯. 현재 천무학관 생도.”

천무학관이 어디 붙어 있는 곳인지는 모른다. 그냥 앵무새처럼 들은 그대로 읊어 댈 뿐이다. 내 대답에 기계처럼 옳지, 옳지를 반복하던 진위경이 고개를 갸웃거렸다.

“진천검? 내가 별호도 말해 줬던가?”

아니. 그건 마부가 알려 줬는데.

진위경과 눈이 마주친 순간, 나는 냅다 이마를 짚었다.

“아, 머리가! 머리가 아픕니다!”

“아이고오, 막내야!”

이 정도면 치트키 수준이다.



* * *



“단순한 타박상이니, 길어도 사흘이면 붓기와 멍이 전부 사라질 겁니다.”

의원의 마지막 말을 뒤로하고 약왕당을 나왔다. 입구에는 수더분한 인상의 하인이 나를 기다리고 있었다.

“공자님의 처소로 안내해 드리겠습니다.”

앞서 걷는 하인은 거침없이 발걸음을 옮겼다. 이미 내가 기억을 잃었다는 사실을 알고 있는 듯, 간혹 어떤 건물이나 사람을 보면 조용한 목소리로 설명하고는 했다.

‘길잡이, 심부름꾼, 백과사전.’

진위경이 하인을 보낸 의도가 대충 짐작이 간다.

본인이 업무로 바쁘니 이렇게라도 신경 써 주는 거겠지.

“도착했습니다.”

마침내 발걸음이 멈춘 곳은 2층으로 이루어진 목제 건물이었다.

보통 이런 건물을 중국에서는 전각이라고 하던가? 제법 고풍스러운 멋이 있었다.

“우와.”

그리고 무지하게 넓다. 하인이 문을 연 순간 나도 모르게 입이 딱 벌어질 정도였다.

“이 층이 침실입니다. 내부 곳곳에 종을 설치해 두었으니 필요한 일이 생기시면 종을 울려 주십시오.”

하인이 떠난 뒤, 나는 정신을 차리고 전각 내부를 돌아보기 시작했다. 1층만 해도 얼추 100평도 넘어 보인다.

2평 남짓한 고시원 원룸에 살던 내게는 올림픽 경기장이나 다름없다.

‘NPC가 부럽긴 처음이네.’

1층에만 방이 여섯 개다. 문득 호기심이 치솟았다.

‘저 안에 뭐가 있을까.’

보물? 무공 비급? 아니면 기똥찬 아이템들?

뭐라도 상관없다. 가장 가까운 방문을 열어젖혔다.

“이야.”

문을 여는 순간 탄성이 튀어나왔다. 형광등이 달린 것도 아닌데 사방이 환하다. 벽을 따라 세워진 선반, 그 안을 가득 채운 비단옷들 때문이다. 언뜻 봐도 엄청난 양이다.

물론 내가 찾던 물건은 아니었다.

‘이 자식은 옷도 많네.’

클럽, 아니 기루 죽돌이답다. 나는 혀를 차고 문을 닫았다. 그리고 곧장 두 번째 방으로 직행. 다시 문을 열어젖혔다.

“또 옷이야?”

진태경을 과소평가했다. 이 정도면 이 시대의 패션 피플쯤 되지 않을까. 스멀스멀 기어오르는 불안감을 애써 무시하며 세 번째 방으로 이동했다.

벌컥.

“……이런 쇼핑 중독자 새끼.”

와, 뭐 이런 놈이 다 있지? 방 세 개가 옷으로 꽉꽉 채워진 걸 보니 고구마를 먹은 것처럼 목이 꽉 막힌다.

‘이거 어쩌면…….’

불안감이 점점 실체화되어 몸을 짓누른다. 나는 무거운 발걸음으로 마지막 방 앞에 섰다. 앞서 들른 방들과는 달리 잘 쓰지 않아 녹슨 문고리를 잡고 천천히 밀었다.

끼이익.

거슬리는 소리와 함께 마지막 방이 속살을 드러냈다.

자그맣게 뚫린 창 사이로 스며드는 햇빛. 걸음마다 피어오르는 먼지. 그리고 그 너머로 보이는, 여러 개의 책장.

“찾았다.”

나도 모르게 웃음이 나왔다.



* * *



책장은 총 다섯 개. 그중 가장 가까운 책장에 다가가 한 권을 뽑아 들었다. 두껍게 쌓인 먼지를 털어 내자 겉표지에 적힌 글씨가 드러난다.

시스템은 이래서 편하다. 언어가 동기화된 덕분에 외계어 같은 글씨도 모국어처럼 읽고 발음할 수 있으니까.

“삼전보?”

띠링.



아이템창



[삼전보]

종류 : 비급

등급 : 삼류

제한 : 없음

설명 : 가장 기본적인 실전 보법. 시중에서도 구할 수 있다.

- 해당 무공을 수련하시겠습니까? (3 / 10)





됐다!

나는 두근거리는 마음으로 시스템창을 읽어 내려갔다.

삼전보. 가장 기본적인 삼류 보법. 맞다. 소설 속에서나 보던 바로 그 무공 비급이다.

내가 세운 첫 번째 계획은 바로 무공을 익히는 것이었다.

‘역시 무공 수련에도 시스템이 적용되는 거였어.’

앞서 태원진가에 오기 전, 운기조식 퀘스트를 끝낸 직후 느꼈던 짐작이 확신으로 바뀌는 순간이다.

‘다행이다.’

설마 소설 속 주인공이나 NPC들처럼 하나부터 열까지 차근차근 익혀 나가야 하는 건 아닌지 걱정했는데 다행히 기우에 그쳤다.

‘망겜도 게임은 게임이지.’

일반 무공에도 운기조식 때처럼 시스템이 적용된다면 고속 성장은 식은 죽 먹기다. 나는 수락을 외치……려다가 말았다.



- 해당 무공을 수련하시겠습니까? (3 / 10)



괄호 사이의 숫자가 심히 거슬린다. 마침 내가 익힌 무공도 딱 세 개다. 진가심법과 진가창법, 그리고 진가보법.

이거 설마.

‘익힐 수 있는 무공에 제한이 있나?’

만약 이 짐작이 사실이라면 지금 [삼전보] 같은 삼류 무공을 익힐 때가 아니다. 로그아웃 전까지 내 목숨을 지키고, 레벨과 명성치를 빠르게 올릴 수 있을 만한 상급 무공을 찾아야 한다.

그나마 다행인 건 이 방에는 어림잡아 몇백 권의 무공 비급이 존재한다는 사실이다.

“좋아. 좋아.”

앞으로 익힐 수 있는 무공은 일곱 개. 알짜배기 무공으로 꽉꽉 채워 넣는다면 로그아웃은 시간문제다.

나는 흐뭇한 미소를 지으며 다음 책을 뽑아 들었다.

띠링.



아이템창



[야왕 대물남]

종류 : 야설

등급 : 無

제한 : 없음

설명 : 삽화를 곁들여 읽으면 더욱 좋다.





“…….”



* * *



오늘도 업무와의 전쟁은 치열했다. 아침부터 자정이 되어 가는 지금까지 집무실을 벗어나지 못했으니까. 벌써 두 달째 이어지는 강행군이었다.

“고생하셨습니다.”

금일 업무의 종료를 알리는 위팽의 한마디였다.

진위경은 뻣뻣해진 몸을 일으켜 집무실을 나섰다. 이곳의 주인은 어느 날 홀연히 사라진 그의 아버지이지, 진위경 자신이 아니기 때문이다.

그가 기거하는 곳은 태원진가의 중심부에 위치한 내원(內院)의 전각이었고, 일 다경 정도를 걸어야 했다.

“날이 춥습니다.”

그림자처럼 따라붙은 위팽이 두툼한 모피를 어깨에 둘러 주자 진위경은 피곤한 얼굴로 웃었다.

“고맙네. 자네마저 없었으면 진작 몸져누웠을지도 몰라.”

“어쩌겠습니까. 저라도 안주인 역할을 해야지요.”

“관두세. 안 그래도 노인네들이 성화야.”

진위경은 뻑뻑한 눈가를 문질렀다. 서른 중반의 나이지만 그는 아직 미혼이다. 젊음을 핑계로 차일피일 미루던 것이 쌓이고 쌓여 십여 년 세월이 됐다.

‘하긴 해야겠지. 가문을 위해서라면.’

사랑해 본 경험이 없느냐고 묻는다면, 아니다.

하지만 진위경은 철부지 어린애가 아니었다. 언젠가는 가솔들을 책임질 가주가 될 터였고, 정략혼으로 가문을 일으킬 수 있다면 그로서는 값싼 희생이었다.

“별이 밝군요. 횃불이 없어도 될 뻔했습니다.”

분위기를 알아챈 위팽이 말을 돌렸다. 진위경은 고개를 절레절레 흔들었다. 어느새 처소가 보이고 있었다.

“음?”

“왜 그러십니까?”

진위경의 시선을 따라간 위팽은 고개를 갸우뚱했다. 멀지 않은 전각에서 희미한 불빛이 새어 나오고 있었다.

“삼공자의 처소 아닙니까?”

“맞네. 밤이 깊었는데 불이 켜져 있군.”

진위경은 말과 함께 성큼성큼 앞서 나갔다. 위팽도 어쩔 수 없이 그 뒤를 따랐다.

“주군, 그냥 다음에 보시죠. 기억을 잃은 건 핑계고 술이나 마시고 있을 게 뻔합니다.”

“쉿.”

두 사람은 전각에 들어섰다. 불빛이 새어 나오는 곳은 가장 왼쪽의 낡은 방이었다. 누가 움직이는지 쉴 새 없이 삐걱거리는 소리도 났다.

- 제가 삼공자를 과소평가했군요. 여자까지 부른 모양입니다. 소리 들어 보세요. 제 이번 달 봉급을 걸겠습니다.

위팽이 입을 달싹였다. 공력으로 소리를 전달하는 전음(傳音)이었다.

- 위팽.

- 예?

- 입 좀 닥치게.

전음으로 굵고 짧은 한마디를 던진 진위경이 문으로 바짝 다가섰다. 열린 문틈 사이로 방 안의 광경이 보였다.

이어 위팽이 상처받은 얼굴로 끼어들었다.

- 그렇게 안 봤는데 주군 취미가 상당히 독특…… 허억.

다음 순간, 위팽의 입이 딱 벌어졌다. 내가 방금 뭘 본거지?

요즘 몸이 허해서 헛것이 보이나? 소매로 눈을 비볐지만 그의 오감은 눈앞의 광경을 그대로 받아들였다.

“이제 대각선으로 두 걸음 내딛으면서…….”

건장한 체구의 청년이다. 연신 중얼거리며 쉴 새 없이 몸을 움직인다. 먼지에 덮인 바닥 위에는 수많은 발자국이 찍혀 있고 지금도 생겨나는 중이다.

스륵. 삐끗.

“시발, 무공 좆같이 만들었네에에엑!”

삼공자다. 저 지랄 맞은 성격과 말투. 분명히 삼공자 진태경이 맞다.

열두 살 이후로 무공을 수련하지 않았던 그가, 자정이 넘은 시각까지 먼지와 땀에 범벅이 될 정도로 수련을 하고 있다!

- 위팽.

넋 놓고 바라보던 위팽이 퍼뜩 정신을 차렸다.

- 예, 예?

진위경은 몽롱한 눈동자로 방 안을 바라봤다. 넘어진 채 천장을 향해 쌍욕을 퍼붓던 진태경이 다시 일어나 보법을 밟고 있었다.

- 약속대로 이번 달 봉급은 없네.
```

## Current accepted English baseline

```markdown
# Chapter 8

“There are no abnormalities.”

That was the physician’s conclusion. I nodded inwardly at his confident tone. He was telling the truth.

*There’s nothing wrong with my brain.*

I was simply inhabiting this body.

But someone didn’t seem satisfied with the diagnosis.

“Then why can’t he remember?”

The dignified atmosphere. The commanding voice. I knew his name now.

*Jin Wikyung.*

Jin Taekyung’s eldest brother and the Lesser Family Head of the Jin Family of Taiyuan, Jin Wikyung. Right. He really wasn’t my father.

*That guy was practically tearing up earlier.*

Now he had put on a mask of stern solemnity and seriousness, acting as if nothing had happened.

The innocent physician fumbled for an answer.

“Well, that is certainly my assessment, but there can occasionally be exceptions…”

“That will do. You may leave.”

The physician left with a wounded expression, and Jin Wikyung immediately moved close to me as if he had been waiting for the chance. His voice overflowed with affection and concern.

“You truly don’t remember?”

“No.”

“Not a thing?”

I quietly nodded. I had already finished calculating how I was going to act.

*Let’s keep going like this.*

An amnesiac patient—the kind I had only ever seen in dramas. There was no better situation for me. I didn’t need to make an effort to fit into the game’s circumstances, and I didn’t even need to gather information.

All I had to do was lie still, blink at everyone with an expression that said *I don’t know anything*, and let the situation unfold on its own. Just like now.

“Do you remember what you said a moment ago?”

“What did I say?”

Thinking that I had lost my memory, Jin Wikyung told me a few basic facts. That was how I learned his identity.

“Tell me my name.”

“Jin Wikyung. The Lesser Family Head of the Jin Family of Taiyuan.”

“Age?”

“Thirty-five.”

Good grief. He was in his thirties with that face? And apparently, he was still an unmarried bachelor.

“What about our parents?”

“Our father is touring the Central Plains. Our mother died ten years ago.”

“Correct. And your second brother?”

“Jin Mukyung, the Heaven Shaking Sword. Twenty-five years old. Currently a cadet at Heaven’s Gate Temple.”

I had no idea where Heaven’s Gate Temple was located. I was simply parroting back everything I had heard.

Jin Wikyung mechanically repeated “Correct, correct” to each of my answers, then tilted his head.

“The Heaven Shaking Sword? Did I tell you his sobriquet too?”

No. The coachman had told me that.

The moment our eyes met, I grabbed my forehead.

“Ah, my head! My head hurts!”

“Oh, my youngest!”

This was practically a cheat code.

* * *

“It’s only a simple contusion. The swelling and bruises should be completely gone within three days at most.”

Leaving the physician’s final words behind, I walked out of Medicine King Hall. A servant with a plain, friendly face was waiting for me at the entrance.

“I’ll guide you to your quarters, Young Master.”

The servant walked ahead without hesitation. He already seemed to know that I had lost my memory, because whenever we passed a building or a person, he quietly explained what they were.

*A guide, an errand boy, and an encyclopedia.*

I could roughly guess why Jin Wikyung had sent him.

He was busy with his duties, so this was probably his way of looking after me.

“We’ve arrived.”

At last, we stopped in front of a two-story wooden building.

Weren’t buildings like this usually called pavilions in China? It had a rather impressive old-fashioned charm.

“Wow.”

It was unbelievably spacious, too. The moment the servant opened the door, my jaw dropped.

“The second floor contains your bedroom. Bells have been installed throughout the building, so please ring one if you need anything.”

After the servant left, I came to my senses and began exploring the pavilion. The first floor alone looked to be more than three hundred square meters.

To someone who had lived in a goshiwon room measuring barely seven square meters,[^1] this was no different from an Olympic stadium.

*This is the first time I’ve ever envied an NPC.*

There were six rooms on the first floor alone. A sudden wave of curiosity rose in me.

*What could be inside?*

Treasures? Martial arts manuals? Amazing items?

I didn’t care what it was. I opened the nearest door.

“Whoa.”

A gasp escaped me the moment I opened it. The room was bright despite having no fluorescent lights. Silk clothes filled the shelves lining the walls. There were an astonishing number of them, even at a glance.

Of course, it wasn’t what I was looking for.

*This bastard has a lot of clothes.*

A club rat—no, a pleasure-house regular. I clicked my tongue and closed the door. Then I went straight to the second room and threw that door open, too.

“More clothes?”

I had underestimated Jin Taekyung. At this point, wasn’t he practically the fashion icon of his era?

I forced myself to ignore the unease slowly crawling up my spine and moved to the third room.

The door flew open.

“…What kind of shopping-addicted bastard is this?”

Seriously, what kind of person was he? Seeing three rooms packed completely full of clothes made my throat close up, as if I had swallowed a sweet potato.

*Could this possibly mean…*

My unease gradually took shape and pressed down on my body. With heavy steps, I stood before the next room. Unlike the others, it clearly hadn’t been used in a long time. I grabbed the rusty handle and slowly pushed.

Creeeak.

The final room revealed itself with an irritating groan.

Sunlight filtered through a small window. Dust rose with every step. And beyond it stood several bookshelves.

“Found it.”

A smile spread across my face before I even realized it.

* * *

There were five bookshelves in total. I approached the nearest one and pulled out a book. When I shook off the thick layer of dust, the writing on its cover appeared.

This was why the System was so convenient. Thanks to Synchronization, I could read and pronounce even writing that looked like an alien language as naturally as my mother tongue.

“Three-Turn Footwork?”

Ding.

> **System**
>
> Item Window
>
> **Three-Turn Footwork**
>
> **Type:** Martial Arts Manual
>
> **Grade:** Third Rate
>
> **Restriction:** None
>
> **Description:** The most basic practical footwork technique. It can even be purchased on the open market.
>
> - Would you like to train in this martial art? (3 / 10)

Jackpot!

I read through the System window with a pounding heart.

Three-Turn Footwork. The most basic third-rate footwork technique. This was the kind of martial arts manual I had only ever seen in novels.

My first plan was to learn martial arts.

*So the System applies to martial arts training too.*

The suspicion I had formed after completing the Quest to circulate my qi, just before coming to the Jin Family of Taiyuan, had now become certainty.

*Thank goodness.*

I had been worried that I might have to learn martial arts one step at a time, like the protagonists and NPCs in novels. Fortunately, that fear had been unfounded.

*Even a trash game is still a game.*

If the System applied to ordinary martial arts the same way it had to circulating qi, rapid growth would be a piece of cake.

I was about to shout, “I accept!”—but stopped.

> **System**
>
> - Would you like to train in this martial art? (3 / 10)

The number in parentheses bothered me immensely. I had learned exactly three martial arts so far: the Jin Family’s Cultivation Technique, the Jin Family’s Spear Technique, and the Jin Family’s Manoeuvre Technique.

*Could it be…*

*Is there a limit to how many martial arts I can learn?*

If that suspicion was true, now was not the time to learn a third-rate martial art like Three-Turn Footwork. I needed to find a higher-grade martial art—one that could keep me alive until Logout and help me raise my Level and Fame quickly.

The good news was that this room contained several hundred martial arts manuals, give or take.

“Good. Good.”

That meant I could learn seven more martial arts. If I filled those slots with nothing but the best techniques, Logout would only be a matter of time.

With a satisfied smile, I pulled out the next book.

Ding.

> **System**
>
> Item Window
>
> **The Night King: Well-Endowed Man**
>
> **Type:** Erotic Novel
>
> **Grade:** None
>
> **Restriction:** None
>
> **Description:** Even better when read with illustrations.

“…”

* * *

Work had been another fierce battle today. I hadn’t been able to leave the office from morning until nearly midnight. It had already been two months of this grueling pace.

“You’ve worked hard.”

That was Wipeng’s signal that the day’s work was over.

Jin Wikyung rose, his body stiff, and left the office. The owner of this place was his father, who had vanished one day—not Jin Wikyung himself.

His residence was a pavilion in the inner compound at the center of the Jin Family estate, and it took about a quarter hour to walk there.

“It’s cold tonight.”

Wipeng, who had followed him like a shadow, draped a thick fur cloak over his shoulders. Jin Wikyung smiled tiredly.

“Thank you. If I didn’t have you, I might have collapsed long ago.”

“What else could I do? Someone has to play the lady of the house.”

“Forget it. The old men are already hounding me enough as it is.”

Jin Wikyung rubbed his stiff eyes. He was in his mid-thirties, but still unmarried. He had kept putting it off under the excuse of being young, and more than a decade had passed in those delays.

*I suppose I’ll have to do it eventually. For the family’s sake.*

If someone asked whether he had never experienced love, the answer would be no.

But Jin Wikyung was not an immature child. One day, he would become the Family Head and take responsibility for everyone in the household. If a political marriage could strengthen the family, it would be a small price to pay as far as he was concerned.

“The stars are bright. We almost wouldn’t need torches.”

Sensing the mood, Wipeng changed the subject. Jin Wikyung shook his head. His residence had come into view.

“Hmm?”

“What is it?”

Following Jin Wikyung’s gaze, Wipeng tilted his head. A faint light was leaking from a nearby pavilion.

“Isn’t that the Third Young Master’s residence?”

“It is. It’s late, but the lights are still on.”

As he spoke, Jin Wikyung strode forward. Wipeng had no choice but to follow.

“My lord, why don’t we come back another time? The memory loss is just an excuse. He’s obviously drinking.”

“Shh.”

The two men entered the pavilion. The light was coming from the old room on the far left. The constant creaking made it clear that someone was moving around inside.

“I underestimated the Third Young Master. It sounds like he even brought a woman with him. Listen to that. I’ll bet my salary for this month.”

Wipeng’s lips moved. He was using Sound Transmission, sending his voice through internal energy.

“Wipeng.”

“Yes?”

“Shut your mouth.”

Jin Wikyung sent the short, heavy response through Sound Transmission, then moved right up to the door. Through the narrow gap, he could see what was happening inside.

Wipeng cut in again with a wounded expression.

“I never took you for this sort of person, my lord, but your tastes are rather unusual…”

He gasped.

The next moment, Wipeng’s mouth fell open.

*What did I just see?*

*Was I seeing things because I’ve been feeling weak lately?*

He rubbed his eyes with his sleeve, but all five senses continued to take in the scene before him exactly as it was.

“Now, take two steps diagonally…”

It was a young man with a sturdy build. He muttered continuously while moving his body without pause. Countless footprints covered the dusty floor, and more were being added even now.

Swish. Stumble.

“Fuck, they made this martial art like shit—aaagh!”

It was the Third Young Master. That foul personality and that foul mouth. There was no doubt that he was Jin Taekyung.

He hadn’t trained in martial arts since the age of twelve, yet he was practicing past midnight, drenched in dust and sweat!

“Wipeng.”

Wipeng, who had been staring blankly, suddenly snapped back to reality.

“Yes, yes?”

Jin Wikyung gazed into the room with dazed eyes. Jin Taekyung had fallen over and was hurling vicious curses at the ceiling, but he soon got back up and resumed practicing his footwork.

“As promised, you won’t be getting paid this month.”

[^1]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 8`.
