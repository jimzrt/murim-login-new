# Master Edit Task — Chapter 9

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
| 위팽     | **Wipeng**         |
| 태원진가   | **Jin Family of Taiyuan**        |
| 일류     | **First Rate**    |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 창법     | **spear technique**                              |                                                       |
| 구결     | **formula**                                      | Mnemonic/oral formula for a martial art               |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 장로     | **Elder**                                    |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 대물남    | **Well-Endowed Man**                         | Euphemistic crude slang; do not intensify to explicit anatomical profanity |
| 진가보법   | **Jin Family's Manoeuvre Technique**   |
| 진가창법   | **Jin Family's Spear Technique**       |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 스킬               | **Skill**                      |
| 스킬창              | **Skill Window**               |
| 레벨               | **Level**                      |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 습득               | **Acquired**                   |
| 로그아웃             | **Logout**                     |
| 지능               | **Intelligence**               |
| 헌터      | **Hunter**            |
| 태원     | **Taiyuan**            |
| 본가      | **our family / this family**                                    |
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

#### Chapter 7 tail (verified mastered)

…
*If that hits me…* Gulp. I swallowed involuntarily at the sight of his palm, which was as large as a pot lid. Level aside, the man looked dangerous in every way. He stood nearly two meters tall, his entire body sheathed in muscles like a bulletproof vest. His cold gaze was enough to freeze a person solid. I found myself wondering who this middle-aged man was. He looked like murder was both his hobby and his specialty. *But his face looks strangely familiar.* Where had I seen this man before? I thought hard, then realized. *Jin Taekyung?* The middle-aged man looked like Jin Taekyung. No—it would be more accurate to say Jin Taekyung looked like him. His incomprehensibly high Level. The way he spoke while trampling all over the Third Young Master of the Jin Family of Taiyuan. And finally, his face. There could only be one answer. He was Jin Taekyung’s… “Father?” The word slipped out before I could stop it, and the middle-aged man’s eyes bulged. “F-Father?” Even his fist began to tremble. Anyone watching would have thought I’d insulted his mother. Keeping a wary eye on his fist, I said, “Please, just calm down for a moment…” “Calm down? You dare say that to me? You’re still playing games at a time like this!” “I’m very sorry if I got it wrong. I spoke out of turn.” “Shut your mouth.” He silenced me with a chilly glare, then turned to the physician, who was still waiting nearby. “Thank you for showing me here. You may leave now.” I sent the physician a desperate SOS with my eyes, but he immediately turned away. *What the fuck… A doctor is abandoning his patient?* Bang. The door slamming shut sounded like the gates of hell opening. Alone together in the room, the man raised his pot-lid-sized palm and began walking toward me. “There’s a limit to how much of a wastrel you can be! How long are you going to keep living like this?” Before I knew it, I had jumped to my feet and was slowly backing away. Bruises? Pain? I couldn’t feel any of that anymore. Maybe I was about to end up in a body that would never feel pain again. “Give me just ten minutes. No, a quarter hour. I can explain everything properly. What are you angry about? Huh? Is it because I called you Father? Are you actually my mother?” “You little brat!” His booming voice made my body lock up. I felt my back touch the wall. > **System** > > - You have fallen into Confusion. You cannot move for 3 seconds! *What the actual fuck…* *I’m finished.* My twenty-seven years of life flashed before my eyes. With a little exaggeration, I even remembered the fierce race to reach the egg back when I was still a sperm. That had been rough. *Mom, Dad, Hayeon…* It was just as I thought of my family and slowly closed my eyes. “Whenever you get a chance, all you do is chase women!” Pat, pat. “You’re always in and out of gambling dens!” Fiddle, fiddle. “This is why the family looks down on you!” Rub, rub. …What the hell was this guy doing? His mouth kept pouring out angry scoldings, but his hands were gently feeling me all over. A chill ran down my spine. *No way…* Ding. > **System** > > - You have been overcome by Fear. You cannot move for 5 seconds! “You’re a disgrace to the family. A disgrace!” I certainly was feeling overwhelming shame. I was being sexually harassed by an AI—and one that looked like a middle-aged man, at that. *Mom…* It took me a moment to realize that I had completely misunderstood. His hands moved quickly, but they moved like those of a physician examining a patient. He lifted my eyelids, checked my pulse, and carefully examined the bruised areas. Every time his hands passed over me, the pain faded and my body felt refreshed, as if I were getting a massage. You little bastard! Keep acting like this and—huh? Huh!—you'll get what's coming to you. Do you understand? “…” At last, he stopped moving his hands and whispered in a small voice, “Thank goodness it’s not as bad as I expected. Why did you have to fight him? You never even train in martial arts.” I answered with complete sincerity. One question, loaded with all kinds of meaning. “Who are you?” The next moment, his stern, solemn, serious expression transformed into that of a wounded fawn. “Why are you speaking formally all of a sudden? When I called you a disgrace to the family, I only said it for other people to hear… Did it hurt your feelings?” “Huh?” “Your big brother is sad. You know how dearly I raised you. When you were little, I changed your dirty diapers every day, carried you around whenever you cried, and soothed you to sleep.” “Huh? You’re my brother?” Silence fell. *He was my brother, not my father?* I was shocked that this old man was my brother. “Oh dear, our youngest must have hurt his head. Physician! Physician!” As I watched his retreating figure, I suddenly felt that a piece of the puzzle had fallen into place. *Now I understand why Jin Taekyung grew up such a mess.* A shining example of what happens when parenting goes wrong.

#### Chapter 8 tail (verified mastered)

…
I was about to shout, “I accept!”—but stopped. > **System** > > - Would you like to train in this martial art? (3 / 10) The number in parentheses bothered me immensely. I had learned exactly three martial arts so far: the Jin Family’s Cultivation Technique, the Jin Family’s Spear Technique, and the Jin Family’s Manoeuvre Technique. *Could it be…* *Is there a limit to how many martial arts I can learn?* If that suspicion was true, now was not the time to learn a third-rate martial art like Three-Turn Footwork. I needed to find a higher-grade martial art—one that could keep me alive until Logout and help me raise my Level and Fame quickly. The good news was that this room contained several hundred martial arts manuals, give or take. “Good. Good.” That meant I could learn seven more martial arts. If I filled those slots with nothing but the best techniques, Logout would only be a matter of time. With a satisfied smile, I pulled out the next book. Ding. > **System** > > Item Window > > **The Night King: Well-Endowed Man** > > **Type:** Erotic Novel > > **Grade:** None > > **Restriction:** None > > **Description:** Even better when read with illustrations. “…” * * * Today’s battle against work had been fierce. Jin Wikyung had not left the office once between morning and the present hour, which was approaching midnight. This grueling pace had already continued for two months. “You’ve worked hard.” Wipeng’s words signaled the end of the day’s work. Jin Wikyung rose, stretching his stiff body, and left the office. After all, the owner of that room was not Jin Wikyung, but his father, who had vanished without warning one day. His residence was a pavilion in the inner compound at the center of the Jin Family estate, and it took about a quarter hour to walk there. “It’s cold tonight.” Wipeng, who had followed him like a shadow, draped a thick fur cloak over his shoulders. Jin Wikyung smiled tiredly. “Thank you. Without you, I might have collapsed long ago.” “What else can I do? Someone has to play the lady of the house.” “Forget it. The old men are already hounding me enough as it is.” Jin Wikyung rubbed his dry eyes. Though he was in his mid-thirties, he remained unmarried. He had kept putting marriage off on the grounds that he was still young, and those delays had added up to more than a decade. *I suppose I’ll have to do it eventually. For the family’s sake.* Had he ever been in love? Yes. But Jin Wikyung was no immature child. One day, he would become the Family Head and bear responsibility for everyone in the household. If a political marriage could strengthen the family, he considered it a small price to pay. “The stars are bright. We almost wouldn’t need torches.” Sensing the mood, Wipeng changed the subject. Jin Wikyung shook his head. His residence had come into view. “Hmm?” “What is it?” Following Jin Wikyung’s gaze, Wipeng tilted his head. A faint light was leaking from a nearby pavilion. “Isn’t that the Third Young Master’s residence?” “It is. It’s late, but the lights are still on.” As he spoke, Jin Wikyung strode forward. Wipeng had no choice but to follow. “My lord, why don’t we come back another time? The memory loss is just an excuse. He’s obviously drinking.” “Shh.” The two men entered the pavilion. The light came from the old room on the far left. Constant creaking sounded from within, as if someone were moving around without pause. “I underestimated the Third Young Master. It sounds like he even brought a woman in. Listen to that. I’ll bet this month’s salary on it.” Wipeng’s lips moved. He was using Sound Transmission, sending his voice through internal energy. “Wipeng.” “Yes?” “Shut your mouth.” Jin Wikyung sent the short, heavy reply through Sound Transmission, then moved right up to the door. Through the open crack, he could see what was happening inside. Then Wipeng cut in with a wounded expression. “I never took you for this sort of person, my lord, but your tastes are rather unusual…” He gasped. The next moment, Wipeng’s mouth fell open. *What did I just see?* *Am I seeing things because I’ve been feeling weak lately?* He rubbed his eyes with his sleeve, but all five senses continued to take in the scene before him exactly as it was. “Now, take two steps diagonally…” A sturdy young man muttered continuously as he moved without pause. Countless footprints covered the dusty floor, and more were appearing even now. Swish. Stumble. “Fuck, they made this martial art like shit—aaagh!” It was the Third Young Master. That foul personality and that foul mouth. There was no doubt that he was Jin Taekyung. He had not trained in martial arts since he was twelve, yet here he was, practicing past midnight until he was drenched in dust and sweat. “Wipeng.” Wipeng, who had been staring blankly, snapped back to his senses. “Yes, yes?” Jin Wikyung gazed into the room with dazed eyes. Jin Taekyung had fallen over and was hurling vicious curses at the ceiling, but he soon got back up and resumed practicing his footwork. “As promised, you won’t be getting paid this month.” [^1]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement.

## Korean source

```text
＃9화



띠링.



- [진가보법]을 습득하셨습니다.

- 해당 무공을 대성할 시 여러 효과를 얻을 수 있습니다.

- 업적, [무공을 익히다]를 달성하셨습니다.

- 업적 달성 보상으로 칭호, [초보 수련자]를 획득합니다.



“어이고.”

시스템 알림이 뜬 순간 털썩 주저앉았다. 먼지가 풀풀 피어올랐지만 무슨 상관이냐, 어차피 이미 거지꼴이다.

‘뭐가 이렇게 빡세냐.’

진태경의 서재에는 단 두 종류의 책이 존재했다.

야설. 그리고 야설이 아닌 것. 사백여 권에 달하는 책 중 야설을 제외하니 백여 권이 남았다.

‘대단한 놈.’

한국에서 태어났으면 불법 성인 사이트 운영자, 미국에서 태어났다면 징역을 살았을 놈이다. 어쨌든 그렇게 분류를 끝내 놓으니 무공 비급은 삼십여 권에 불과했다.

‘비급을 야설의 절반만 모았어도.’

나로서는 애석한 일이었지만 수확은 있었다. 당장 필요한 무공 비급을 발견했으니까.

진가창법과 진가보법. 너무 오랫동안 수련을 하지 않아 잊고 있었다는 태원진가의 가전 무공이다.

‘진가보법 확인.’

띠링.



스킬창



[진가보법]

종류 : 보법

등급 : 일류

제한 : 태원진가의 직계

경지 : 일 성

설명 : 태원진가의 시조가 창안한 보법. 변화가 적고 단조로우나 실전적이다.





진가창법의 설명도 크게 다르지 않았다. 다만.

‘변화가 적고 단조롭긴 개뿔.’

시조인가 시조새인가 하는 양반이 만들었다는 가전 무공은 더럽게 복잡했다. 어젯밤 일만 생각하면 저절로 이가 갈릴 정도다.



- [진가보법]의 습득을 시작합니다.

- 구결을 암기 중입니다. 무공의 등급과 지력 수치에 따라 속도가 달라집니다.



그래, 딱 여기까지는 괜찮았다. 문제는 그다음부터였다.



- [진가보법]의 투로를 표시합니다. (0 / 100)



시스템이 표시한 발자국을 따라 보법을 밟는데, 얼마나 꼬장꼬장하고 칼 같은지 표시한 발자국에서 조금이라도 벗어나면 실패. 다음 동작이 늦어도 실패다.

그렇게 전체 투로를 정확히 밟아야 1회 완수다.

‘미친 좆망겜.’

현실에서의 나와 지금의 캐릭터는 체격의 차이가 크다. 키는 반 뼘 가까이 줄어들었고 리치도 짧다. 세밀한 조정이 안 되니 실수가 연이어 터졌다.

‘성공한 게 기적이다.’

100회를 채우고 나니 손발이 덜덜 떨렸다.

‘그래도 하나는 얻었어.’

오랜 헌터 생활로 전투, 특히 집단전이라면 이골이 났다. 생사를 오가는 싸움에서 가장 중요한 것은 첫째가 운, 둘째가 발이다.

전진. 후퇴. 혹은 정지. 팔이 잘려도 다리만 움직이면 살 수 있다. 하지만 다리가 잘리면 그걸로 끝이다.

발이 나가야 팔이 나간다. 내가 겪은 전투들은 그랬고, 그것이 보법을 먼저 익힌 이유였다.

‘하지만…….’

너무 느리다. 시스템의 힘을 빌렸음에도 반나절이 훌쩍 흘렀는데 창술까지 익히려면 얼마나 더 시간이 필요할까.

‘오늘로 5일째.’

가상현실 게임은 현실에 비해 시간이 빠르게 흐른다고 했다. 하지만 시간 배율을 감안하더라도 5일은 긴 시간이다.

“후우.”

나는 한숨과 함께 잡념을 애써 털어 버렸다.

구조? 로그아웃? 지금은 가능성에 매달리기보다 혼자서라도 계속 나아가야 할 때다.

‘그럼 오늘은 여기까지.’

나는 무공 비급들을 챙겨 일어났다.

그리고 2층 침실에 도착했을 때, 비급들 사이에 이색적인 책 한 권이 끼어 있다는 사실을 깨달았다.



[야왕 대물남]



“크흠.”

아이고, 이런 실수를.



* * *



“벌써 기침하셨습니까?”

하인은 휘둥그레진 눈으로 나를 바라봤다. 그의 손에는 아침 식사가 놓인 쟁반이 들려 있었다.

“잠이 잘 안 와서…….”

내 대답은 사실이다. 그 원인은 운기조식에 있었다.

‘이거 효과 죽이네.’

운기조식은 정신과 오감을 맑게 하는 것 외에도 피로를 해소하는 효능이 있었다. 곰곰이 생각해 보니 운기조식을 하게 된 이후로 피곤한 적은 없었던 것 같다.

‘통증도 거의 사라졌고.’

“상처가 덧날 수도 있으니 너무 무리하지 마십시오.”

하인의 말에 가슴 한구석이 따뜻해진다. 이 거지 같은 게임에도 한 줄기 빛 같은 NPC가 있구나. 드디어 정상인을 만났어.

‘이게 뭐라고 울컥하냐.’

나는 먹먹해진 얼굴로 아침 식사를 시작했다.

하나같이 짜거나 싱거운 반찬들이었지만 허기를 반찬 삼아 해치우고 탕약 그릇을 한 번에 들이켰다.

“크으.”

저절로 눈살이 찌푸려지는 맛이다. 이윽고 상을 모두 치운 하인이 고개를 조아렸다.

“그럼 소인은 이만.”

“아, 잠깐만요.”

“말씀 낮추십시오. 어찌 제게 말을 높이십니까?”

생각해 보니 그러네.

처음에는 그래픽과 인공지능이 너무 현실적이라 만나는 NPC마다 존대를 썼지만 이제는 어느 정도 익숙해진 상태.

비로소 유저의 존엄성을 되찾을 때가 온 것이다. 나는 준엄하게 대답했다.

“당분간은 저 편한 대로 할게요.”

시바, 차마 말을 못 놓겠다. 딱 봐도 마흔은 넘어 보이는 아저씨한테 이놈 저놈 할 수는 없는 일 아닌가.

망할 게임, 쓸데없이 그래픽만 좋아서 반말도 못 하겠다.

‘이러다가 NPC랑 친구도 먹겠네.’

내가 머리를 다쳤다는 사실을 어필하자 하인도 마지못해 고개를 끄덕였다.

“어쩔 수 없군요. 한데 시키실 일이?”

“비는 방 없나 해서요.”

하인이 고개를 갸웃했다.

“구해 드릴 수는 있습니다만, 혹 용도가 어찌 되시는지.”

“무공 수련을 하려고요.”

“예?”

“여기 있는 방들은 죄다 더럽거나 답답해서…… 그런데 표정이 왜 그러세요?”



* * *



전각을 나온 하인이 곧장 달려간 곳은 가주 집무실이었다.

하인의 보고가 끝나자 서류 탑 너머로 진위경의 근엄한 목소리가 울렸다.

“수고했네.”

하인이 떠나기가 무섭게 벌떡 일어난 진위경이 서류를 허공에 흩뿌렸다.

“경사다! 오늘 일 안 해!”

“누구 맘대로요?”

흩날리는 서류를 남김없이 잡아챈 위팽이 한숨을 내쉬었다.

“이러시는 거 다른 사람들이 알면 또 말 나옵니다.”

“지금 셋째가 본격적으로 무공을 익히겠다는데 뭐가 더 중요한가!”

“그것보다는 장로원에서 벼르고 있다는 사실이 중요하죠.”

장로원. 그 단어에 진위경의 표정이 가라앉았다.

“망할 노친네들.”

“조만간 가로회의가 열릴지도 모르겠습니다. 저들 입장에서는 틈이 보이니 물어뜯는 것이 당연하지요.”

회의 안건은 보나 마나 뻔하다. 진태경의 평소 행실로 시작해서 소문주인 자신에 대한 공격으로 끝날 것이다.

“그 작자들도 참 끈질겨.”

“하루 이틀 일입니까? 오래된 기둥에는 벌레가 끓는 법입니다.”

“방법이 없을까?”

“결국 또 삼공자의 방패 역할을 자처하시는군요.”

위팽이 한숨을 내쉬었다.

“주군. 속하가 한 말씀 올려도 되겠습니까?”

“거절하겠네.”

“그럼 저도 거절하겠습니다. 문파 공금 횡령만 다섯 번쨉니다. 다른 것들은 셀 수도 없어요. 본가의 문규대로 집행했으면 삼공자는 살아 있는 게 기적입니다.”

“어허. 이 사람.”

“말이 나왔으니 하는 얘긴데, 본가 식솔 아무나 붙잡고 물어보십쇼. 주군 입장에서야 사랑하는 동생이지, 다른 사람들은…… 어휴, 말도 못 합니다.”

“자네 우리 막내한테 무슨 불만 있나? 말투가 왜 그래?”

“답답해서 그럽니다. 답답해서. 삼공자가 사고 치면 주군이 수습하고, 그거 막아 주느라 장로원 요구 들어주고. 이렇게 야금야금 주도권을 뺏기고 있잖습니까. 요즘 어떤 소문까지 도는 줄 아십니까?”

“어떤 소문?”

“삼공자가 장로파라는 말도 있습니다. 장로원 쪽에서 용돈 받아서 쓰고 일부러 사고 치는 거라고요.”

진위경의 눈꺼풀이 파르르 떨렸다.

“이런 천인공노할!”

“저는 차라리 그랬으면 좋겠습니다. 장로원 쪽에서 은전이라도 찔러 주면 공금 횡령은 안 할 테니까요.”

“자네…….”

“할 말 다 했습니다. 자를 거면 자르십쇼.”

끙. 진위경이 깊은 한숨을 내쉬었다.

“나도 슬슬 이대로는 안 된다고 생각하고 있네.”

“생각 좋죠. 실행에 안 옮기시니 문제죠.”

“그래도 이번만큼은 최대한 힘써 봐야지.”

“아이고, 주군…….”

“이번이 마지막일세. 내 분명히 약속하지.”

진위경이 정색하고 말했다. 위팽이 의뭉스러운 목소리로 물었다.

“정말이십니까?”

“아직 기억도 온전치 않은 아이야. 게다가…… 하루아침에 다른 사람처럼 변했어. 자네도 느끼고 있잖은가.”

“그거야 그렇지만…….”

위팽이 말꼬리를 흐렸다.

확실히 삼공자는 변했다. 기억을 잃은 것이 거짓말이든, 사실이든 현재 보여 주는 모습은 확실히 희망적이다.

잠시 생각에 잠겨 있던 진위경이 입을 뗐다.

“위팽.”

“예.”

“내 이름으로 명령서 하나 만들게.”

“어떤……?”

“적당한 죄목 몇 개 가져다 쓰고 처벌로 수련동에 강제 폐관 시켜.”

“아하.”

위팽은 이마를 탁 쳤다. 다분히 보여 주기식이지만 현재 상황에서는 훌륭한 응급 처치다. 곧 있을 가로회의에서 받을 압박을 해소하면서 진태경에 대한 처벌 수위를 낮출 수 있기 때문이다.

거기에 덧붙여…….

“삼공자의 부탁도 들어주게 됐군요. 수련할 곳을 찾고 있었으니 말입니다.”

이거야말로 일석삼조 아닌가. 위팽은 진심으로 감탄했다.

“역시 주군이십니다.”

“우리 집안사람들이 이래. 아, 내가 그거 말했나? 태경이도 어릴 때 참 영특했는데, 어느 하루는…….”

“……명령서 작성하러 가 보겠습니다.”



* * *



“하여, 열네 가지 법규를 어겨 문내 기강을 흐트러트린 삼공자 진태경에게 무기한의 수련동 폐관을 명한다.”

이름이…… 위팽이라고 했던가? 밥맛없게 생긴 놈의 말을 잠자코 듣고 있다가 번쩍 손을 들었다.

“저, 질문 있는데요.”

“하십시오.”

“무기한의 뜻이 뭡니까?”

위팽이 떨떠름하게 대답했다.

“정해진 기한이 없다는 겁니다.”

“아.”

난 또 게임 언어 시스템이 오류 난 줄 알았지. 다행히 내가 아는 뜻이랑 같다. 하하.

“하하하.”

“허허허.”

원래 웃음은 전염되기 마련이다. 위팽과 같이 온 무사들도 나를 따라 웃기 시작했다.

그렇게 훈훈해진 분위기에서 위팽이 마지막 줄을 읊었다.

“죄인 진태경은 오라를 받들라.”

“싫어.”

“……?”

“……?”

“싫다고. 시바.”

포승줄을 들고 다가오던 두 놈이 이게 아닌데, 하는 눈으로 위팽을 바라봤다. 그러거나 말거나 나는 내 할 말을 했다.

“내가 수련하게 방 하나만 구해 달랬지 감옥에 넣어 달랬냐?”

완전히 정신병자 새끼들 아냐, 이거?

“자, 삼공자. 진정하고 내 말을 들어 보시오.”

“듣기는 시벌, 수련동에는 수련에 필요한 모든 것이 있습니다. 복지도 나쁘지 않습니다. 이딴 말이나 할 거 아냐.”

표정을 보니 제대로 짚었다. 나는 쐐기를 박아 넣었다.

“군인 월급 오르니까 행복하게 군대 다녀오라고 할 놈들이네, 이거. 몰라, 나 안 들어가. 그냥 방이나 마당에서 나 혼자 수련할래.”

솔직히 수련동이라는 곳, 단편적으로 생각해 봤을 때는 나쁘지 않다.

하지만 무기한이라는 말이 가시처럼 걸린다. 당장 무공 익히고 레벨 업이 시급한데 수련동에서 백날 천날 목 빼고 꺼내 주기만 기다릴 수는 없으니까.

나는 그대로 벌렁 누워 버렸다.

“배 째!”

“삼공자. 적당히 하고 일어나시지요.”

위팽이 인상을 쓰고 노려보았다.

“다 공자를 위해 소가주께서 결정하신 겁니다.”

“진위경, 아니 형님이?”

그 동생 바보가 이런 명령을 내렸다고?

그때 위팽의 입술이 달싹였다. 동시에 귓가로 어떤 음성이 들려왔다. 육성과는 다른 기묘한 느낌이었다.

- 전음입니다. 놀라지 말고 들으십시오.

전음. 무협지에서 본 기억이 있다. 고수들만 사용한다는 일종의 텔레파시.

- 기억을 잃어서 잘 모르시겠지만, 삼공자는 요주의 인물입니다. 조만간 더 큰 처벌이 내려질 수 있어 그전에 소가주께서 미리 조치하시는 겁니다.

27년 한평생 열심히 살았는데 가중 처벌이 웬 말이냐.

슬퍼하는 내 귓가로 위팽의 전음이 이어졌다.

- 말이 무기한이지, 소가주께서 공자를 평생 수련동에 처박아 놓으실 거라 생각하십니까?

나는 고개를 저었다. 그 양반이라면 그럴 리가 없다. 수련동에 단둘이 처박히기를 원한다면 모를까.

- 길어도 칠주야(七晝夜) 안에 꺼내 드리겠습니다. 어떻습니까?

위팽의 눈에서 강렬한 의지가 엿보였다. 이것까지 거절하면 두들겨 패서라도 데려갈 것 같다.

‘시벌, 여기 NPC들은 죄다 깡패야, 뭐야.’

야, 이 새끼야. 니가 그렇게 싸움을 잘해?

나는 [기감]을 끌어올려 위팽의 레벨을 확인했다.



[Lv.???]



“…….”

깡패 맞네. 레벨 깡패. 저놈도 진위경 못지않은 인간 백정일 것이다. 위팽이 눈을 부릅뜨고 물었다.

- 어쩌시렵니까?

나는 두려움에 떨면서도 손가락 세 개를 펴 보였다.

- ……사흘 안에 빼 달라고요?

뭐 이런 새끼가 다 있냐. 그런 얼굴로 나를 노려보던 위팽이 이내 한숨과 함께 말했다.

“뫼셔라.”

#수련동 #폐관 #협상 #성공적.
```

## Current accepted English baseline

```markdown
# Chapter 9

Ding.

> **System**
>
> - You have acquired **Jin Family’s Manoeuvre Technique**.
>
> - You can obtain various effects upon mastering this martial art.
>
> - You have completed the achievement **Learn a Martial Art**.
>
> - As an achievement completion reward, you have acquired the title **Novice Trainee**.

“Good grief.”

The moment the System notification appeared, I slumped to the floor. Dust billowed into the air, but who cared? I already looked like a bum anyway.

*Why is this so damn hard?*

There were only two kinds of books in Jin Taekyung’s study.

Erotic novels. And books that weren’t erotic novels.

Of the more than four hundred books, only about a hundred remained after I took out the erotic novels.

*What an incredible bastard.*

If he’d been born in Korea, he would’ve been running an illegal adult website. If he’d been born in America, he’d be serving a prison sentence.

At any rate, once I finished sorting them, there were only about thirty martial arts manuals.

*If only he’d collected half as many manuals as erotic novels.*

It was a shame from my perspective, but I had still made a worthwhile discovery. I’d found the martial arts manuals I needed right now.

The Jin Family’s Spear Technique and the Jin Family’s Manoeuvre Technique. They were hereditary martial arts of the Jin Family of Taiyuan—arts I’d forgotten because I hadn’t practiced them in far too long.

*Let’s check the Jin Family’s Manoeuvre Technique.*

Ding.

> **System**
>
> Skill Window
>
> **Jin Family’s Manoeuvre Technique**
>
> **Type:** Manoeuvre Technique
>
> **Grade:** First Rate
>
> **Restriction:** Direct descendants of the Jin Family of Taiyuan
>
> **Realm:** First Stage
>
> **Description:** A manoeuvre technique devised by the founder of the Jin Family of Taiyuan. It has few variations and is monotonous, but it is practical.

The description of the Jin Family’s Spear Technique wasn’t much different. Except…

*“Few variations and monotonous,” my ass.*

The hereditary martial art created by some fellow called the founder—or was it the family’s founding granddad?—was unbelievably complicated. Just thinking about last night made my teeth grind.

> **System**
>
> - You are beginning to acquire **Jin Family’s Manoeuvre Technique**.
>
> - You are memorizing the formula. The speed varies according to the martial art’s grade and your Intelligence stat.

Right. Everything was fine up to that point.

The problem started after that.

> **System**
>
> - The movement sequence for **Jin Family’s Manoeuvre Technique** is being displayed. (0 / 100)

I followed the footprints displayed by the System and practiced the manoeuvre technique. But the footprints were so fussy and razor-precise that stepping even slightly outside them meant failure. Taking too long to perform the next movement also meant failure.

I had to follow the entire sequence perfectly to complete it once.

*What a fucking garbage game.*

There was a major difference between my real-world physique and the character’s. My height was shorter by nearly half a handspan, and my reach was shorter too. I couldn’t make the fine adjustments I needed, so one mistake followed another.

*It’s a miracle I succeeded at all.*

After completing the sequence one hundred times, my hands and feet were trembling.

*Still, I gained something.*

After years of working as a Hunter, I was thoroughly familiar with combat—especially group battles. In fights where life and death were on the line, the most important thing was luck first and your feet second.

Moving forward. Retreating. Or stopping.

Even if your arm was cut off, you could survive as long as your legs still moved. But if your legs were cut off, it was over.

Your feet had to move before your arms. That was how all my battles had gone, and it was why I had chosen to learn a manoeuvre technique first.

*But…*

It was too slow. Even with the System’s help, half a day vanished in the blink of an eye. How much longer would it take if I also had to learn spear techniques?

*Today makes five days.*

I’d heard that time passed faster in virtual-reality games than in the real world. But even after accounting for the time multiplier, five days was a long time.

“Fuu…”

I forced away my distractions with a sigh.

Rescue? Logout?

This wasn’t the time to cling to possibilities. I had to keep moving forward, even if I had to do it alone.

*That’s enough for today.*

I gathered up the martial arts manuals and stood.

When I reached the bedroom on the second floor, I realized that one unusual book had been mixed in among the manuals.

**The Night King: Well-Endowed Man**

“Ahem.”

Oh dear. What a mistake.

* * *

“Are you up already?”

The servant stared at me with wide eyes. He was holding a tray with breakfast on it.

“I couldn’t sleep…”

My answer was the truth. That was because I’d been circulating my qi.

*This is ridiculously effective.*

Circulating my qi didn’t just clear my mind and sharpen my senses. It also relieved fatigue. Looking back, I didn’t think I’d felt tired even once since I started circulating my qi.

*The pain is almost gone too.*

“Your wounds could worsen, so please don’t push yourself too hard.”

A warm feeling spread through one corner of my chest at the servant’s words.

*Even this shitty game has an NPC who’s like a ray of light. I’ve finally met a normal person.*

*Why does this make me feel so emotional?*

Feeling strangely choked up, I began eating breakfast.

Every side dish was either too salty or too bland, but I demolished the entire meal because hunger was the best seasoning, then downed the bowl of herbal decoction in one gulp.

“Ugh.”

The taste made me frown instinctively. Once the servant had cleared away the table, he bowed his head.

“Then I shall take my leave.”

“Ah, wait a second.”

“Please speak less formally. Why are you using honorifics with me?”

Come to think of it, he had a point.

At first, the graphics and artificial intelligence had been so realistic that I had used polite speech with every NPC I met. But by now, I had grown somewhat accustomed to them.

The time had finally come to reclaim the dignity of a user.

I answered sternly.

“For now, I’ll speak however I’m comfortable.”

*Fuck, I can’t bring myself to drop the honorifics.*

I couldn’t exactly talk down to a man who clearly looked over forty and call him “you bastard” or “you punk.”

*Damn game. The graphics are so good I can’t even speak informally.*

*At this rate, I’ll end up becoming friends with an NPC.*

When I emphasized the fact that I had suffered a head injury, the servant reluctantly nodded.

“I suppose it can’t be helped. Is there something you require?”

“I was wondering if there was an empty room.”

The servant tilted his head.

“I can arrange one for you, but what might you need it for?”

“I want to practice martial arts.”

“Pardon?”

“All the rooms here are either dirty or stuffy… Why do you look like that?”

* * *

After leaving the pavilion, the servant went straight to the Family Head’s office.

Once his report was finished, Jin Wikyung’s solemn voice rang out from beyond a tower of documents.

“You’ve done well.”

The instant the servant left, Jin Wikyung sprang to his feet and scattered the documents into the air.

“It’s cause for celebration! I’m not working today!”

“Who said you could decide that?”

Wipeng caught every last one of the fluttering documents and sighed.

“If the others find out you’re acting like this, they’ll start talking again.”

“The Third Young Master says he’s going to take up martial arts in earnest. What could possibly be more important than that?”

“The fact that the Elder Council is waiting to pounce on you is more important.”

At the words *Elder Council*, Jin Wikyung’s expression darkened.

“Damn old men.”

“A family council meeting may be held soon. From their perspective, they’ve spotted an opening, so naturally they’ll sink their teeth into it.”

The agenda was obvious. It would begin with Jin Taekyung’s usual conduct and end with an attack on Jin Wikyung himself, the Lesser Family Head.

“Those bastards are persistent.”

“Is this something that started yesterday? Old pillars always end up crawling with bugs.”

“Isn’t there any way around it?”

“So you’re volunteering to serve as the Third Young Master’s shield again.”

Wipeng sighed.

“My lord, may I offer a word?”

“I refuse.”

“Then I refuse as well. This is the fifth time he’s embezzled the family’s public funds. I’ve lost count of the other things. If we had enforced the family rules properly, it would be a miracle if the Third Young Master were still alive.”

“Now, now.”

“Since we’re on the subject, grab anyone in the family and ask them. From your perspective, he’s your beloved little brother. To everyone else…”

Wipeng shook his head.

“Honestly, I can’t even say it.”

“Do you have some complaint against our youngest? Why are you speaking like that?”

“I’m frustrated. That’s all. I’m frustrated. The Third Young Master causes trouble, you clean it up, and you accept the Elder Council’s demands to keep them from making things worse. They’re slowly taking away your authority. Do you know what kind of rumor is going around these days?”

“What rumor?”

“Some people say the Third Young Master is part of the Elder faction. That he gets pocket money from the Elder Council and deliberately causes trouble.”

Jin Wikyung’s eyelids began to tremble.

“That’s an outrage!”

“I’d actually prefer that to be true. If the Elder Council slipped him even a few silver coins, he wouldn’t have to embezzle the family’s funds.”

“You…”

“I’ve said my piece. Fire me if you want.”

With a groan, Jin Wikyung let out a deep sigh.

“I’ve been thinking things can’t go on like this, either.”

“Thinking is good. The problem is that you never put it into action.”

“Even so, I should do my best this time.”

“Oh, my lord…”

“This will be the last time. I give you my word.”

Jin Wikyung spoke with a serious expression. Wipeng asked, sounding skeptical,

“Do you really mean it?”

“He’s still a child whose memory hasn’t fully returned. And besides… he changed into an entirely different person overnight. You’ve noticed it too.”

“That’s true, but…”

Wipeng let his voice trail off.

The Third Young Master had definitely changed. Whether the memory loss was a lie or the truth, the way he was behaving now was undeniably hopeful.

Jin Wikyung thought for a moment before speaking.

“Wipeng.”

“Yes.”

“Prepare an order in my name.”

“What sort of…?”

“Use a few appropriate charges and order him to undergo indefinite confinement in the training hall.”

“Ah.”

Wipeng slapped his forehead.

It was mostly for show, but under the circumstances, it was an excellent emergency measure. It would relieve the pressure Jin Wikyung was about to receive at the upcoming family council meeting while lowering the severity of the punishment imposed on Jin Taekyung.

And on top of that…

“It fulfills the Third Young Master’s request too. He was looking for somewhere to train.”

Wasn’t this three birds with one stone? Wipeng was genuinely impressed.

“As expected, you’re my lord.”

“That’s how my family is. Oh, did I ever tell you? Taekyung was a clever child when he was young, but one day…”

“…I’ll go write the order.”

* * *

“Therefore, for violating fourteen regulations and disrupting discipline within the family, the Third Young Master, Jin Taekyung, is hereby ordered to undergo indefinite confinement in the training hall.”

Was his name Wipeng? I listened silently to the sour-looking bastard, then raised my hand.

“I have a question.”

“Go ahead.”

“What does ‘indefinite’ mean?”

Wipeng answered reluctantly.

“It means there is no set deadline.”

“Oh.”

I’d thought the game’s language system had malfunctioned. Fortunately, it meant the same thing I knew it meant.

Ha ha.

“Ha ha ha.”

“Ho ho ho.”

I thought the game’s language system had glitched. Fortunately, it meant exactly what I thought it meant.

In that warm atmosphere, Wipeng read the final line.

“The convict, Jin Taekyung, shall submit to the bonds.”

“No.”

“…”

“…”

“I said no. Fuck.”

The two men approaching with rope restraints looked at Wipeng as if to say, *This isn’t how it was supposed to go.*

I ignored them and said what I had to say.

“I asked you to find me a room so I could practice, not put me in prison. Are you people completely fucking insane?”

“Now, Third Young Master. Calm down and listen to me.”

“Listen to what, for fuck’s sake? You’re going to say the training hall has everything needed for practice and the living conditions aren’t bad. You’ll spout that kind of nonsense.”

Judging by Wipeng’s expression, I’d hit the nail on the head. I drove the point home.

“You people would tell someone to go happily serve in the army because military pay had gone up. Forget it. I’m not going in. I’ll practice by myself in my room or in the yard.”

Honestly, on the surface, the training hall didn’t sound so bad.

But the word *indefinite* stuck in my mind like a thorn. I needed to learn martial arts and Level up immediately. I couldn’t spend day after day in the training hall, craning my neck and waiting to be let out.

I flopped onto the floor.

“Go ahead and gut me!”

“Third Young Master, that’s enough. Please get up.”

Wipeng scowled at me.

“The Lesser Family Head made this decision entirely for your sake.”

“Jin Wikyung—I mean, my brother?”

That brother-obsessed idiot had given this order?

At that moment, Wipeng’s lips moved.

At the same time, a voice reached my ears. It felt strange, unlike an actual spoken voice.

> “This is Sound Transmission. Don’t be alarmed—just listen.”

Sound Transmission. I remembered seeing it in martial arts novels. A kind of telepathy that only masters could use.

> “You may not know this because you’ve lost your memory, but the Third Young Master is a person of concern. A harsher punishment may be handed down soon, so the Lesser Family Head is taking action beforehand.”

I had worked hard for twenty-seven years. What did I do to deserve an aggravated sentence?

As I lamented, Wipeng’s Sound Transmission continued in my ear.

> “It may be called indefinite confinement, but do you really think the Lesser Family Head intends to bury you in the training hall for the rest of your life?”

I shook my head.

*There’s no way he’d do that.*

Not unless he wanted the two of us locked up together in the training hall.

> “I’ll get you out within seven days and nights at the latest. How does that sound?”

There was fierce determination in Wipeng’s eyes. If I refused this too, he looked ready to beat me and drag me there if he had to.

*Fuck, are all the NPCs here thugs or what?*

*Hey, you bastard. Are you really that good at fighting?*

I raised my Qi Sense and checked Wipeng’s Level.

> **System**
>
> - **Lv. ???**

“…”

*He really is a thug.*

A Level thug, at least.

He was probably every bit the human butcher Jin Wikyung was.

Wipeng opened his eyes wide and asked,

> “What will you do?”

Even as I trembled with fear, I held up three fingers.

> “…You want me to get you out in three days?”

*What kind of bastard is this?*

Wipeng glared at me with that exact look, then finally sighed.

“Escort him.”

#TrainingHall #ClosedDoorTraining #Negotiation #Successful.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 9`.
