# Master Edit Task — Chapter 6

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

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 혁무진    | **Hyuk Mujin**     |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 태원진가   | **Jin Family of Taiyuan**        |
| 이류     | **Second Rate**   |
| 일류     | **First Rate**    |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 기루     | **pleasure house**                               |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 수문조장   | **Captain of the Gatekeepers**               |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 스킬               | **Skill**                      |
| 스킬창              | **Skill Window**               |
| 레벨               | **Level**                      |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 로그아웃             | **Logout**                     |
| 헌터      | **Hunter**            |
| 태원     | **Taiyuan**            |
| 본가      | **our family / this family**                                    |
| 공자      | **Young Master**                                                |
| 대사      | **Master** for a senior Buddhist monk                           |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |

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

#### Chapter 4 tail (verified mastered)

…
chieftain. *The other five might be even weaker than goblins.* At least goblins were good with poison darts. Judging by that axe throw, I had a hunch. A very strong hunch. I licked my parched lips, then raised both hands high. A few of them looked confused by my gesture of surrender, while the Heavenly Axe smiled proudly, like a father watching his son return from military service. “Good lad.” *Yeah. Laugh while you can.* One step, two. I slowly closed the thirty-meter distance between us. With a steady stride and balanced posture. One breath per step. My breath escaped my mouth in white clouds that pierced the dawn air. I could feel it just from putting one foot in front of the other. *It’s different!* I realized it once more. The version of me inside this game was stronger than the real me. My heart pounded. At the same time, a warning stirred in the back of my mind. I had to stay focused until the very last moment. “I heard the Jin Family had a son they’d given up on. Third-rate at martial arts, first-rate with women. Now that I see you, you’ve got pretty good instincts too.” The Heavenly Axe spoke with the hand holding his axe hanging loosely at his side. I knew exactly how I looked to them. A useless playboy with nothing but a good family name. Empty hands. The Heavenly Axe had let his guard down. *And letting your guard down gets you killed.* I might send most of my salary to my family and live miserably in a tiny goshiwon room, but I was still a Hunter. Even an F-rank Hunter risked his life fighting inside Gates. No—an F-rank Hunter had to risk his life precisely because he was only F-rank. For seven years, I had fought every single day. I was a competitor—and a martial artist called a Hunter. So I knew. Life and death were separated by a hair’s breadth. Letting your guard down meant death. The distance had been cut in half. My steps gradually quickened. The Heavenly Axe beckoned me over. “Now, now. Take your time. If you trip on the way over, you’ll lower your ransom.” Twenty meters. “Boss, doesn’t the way he’s toddling over look just like a puppy?” Fifteen meters. “A puppy? Ha-ha-ha! You’ve got that exactly right!” Ten meters. The moment I took my next step, heat began to churn in my stomach. It was a sensation I had never experienced before, yet somehow, it felt strangely familiar. What was it? *Could it be… internal energy?* The heat flowing from my dantian raced toward my lower body. It had only one purpose: faster, lighter, stronger! Whoosh. I drew a long breath. Every muscle in my body pulled taut like a bowstring. Boom! I shot straight forward. The ground sank beneath my foot, and the sound followed after me. In that frozen moment, the Heavenly Axe’s mouth slowly fell open. “No way…” The Heavenly Axe and his underlings stared at me in disbelief. I could see everything about them now. Feel it. Their stiff, greasy hair. Their cracked lips, like a rice paddy in a drought. Their teeth that reeked just from looking at them… All of it. The corners of my mouth lifted before I knew it. *Open Inventory. Equip Sharp Spear.* A cold spear shaft appeared in the hand I had thrust into empty air. I drove it forward with all my strength. The Heavenly Axe hastily raised his axe to block, but the sharp spearhead shattered the axe blade and punched straight through his chest. At the same time— > **System** > > Critical One Strike! Status effect Bleeding activated! “Ghk!” A fountain of blood erupted. The Heavenly Axe’s eyes trembled once, then went dark. > **System** > > Lv. 10 Jang Sam defeated. > > Level up! > > You received 10 Stat Points as a level-up reward. > > You received 10 Skill Points as a level-up reward. > > Jin Family’s Cultivation Technique unlocked. *Whew.* I let out a long breath. Notifications had sounded, but all I could hear was my own pounding heart. One breath. Everything had happened in a single breath. I pulled the spear from the Heavenly Axe’s lifeless chest. *So this is possible.* Raise my abilities with points, enhance them with internal energy, and link them together with skills. This was the power of the System—the power that belonged to me alone. A power F-rank Hunter Jin Taekyung could never have dreamed of. *I can do this. I will.* The road home was beginning to look brighter and wider. I gripped the spear shaft and turned around. “So…” The five pairs of eyes fixed on me wavered uncertainly. “Anyone else want to try?” *The bastard who threw that axe can go first.* “…” Thud. Thud. Clatter. The five bandits exchanged glances, dropped their weapons, and threw themselves flat on the ground. “Please forgive us, Great Hero!” > **System** > > The enemies have lost their will to fight and surrendered after losing their leader. > > Defeat the Bandits complete. > > You have fully recovered from all fatigue and injuries. > > You have subdued the bandits. Fame increased by 10. > > Tutorial—Stage 3 complete. Rewards will be distributed. > > Chain Quest Tutorial—Stage 4 created. *Now I can finally catch my breath.*

#### Chapter 5 tail (verified mastered)

…
Family’s Cultivation Technique greatly increases stability. I had never missed my family as much as I did then. My beloved mother. My adorable little sister…or rather, my pain-in-the-ass little sister, Hayeon. *When I get out, your big brother will buy you enough fried chicken to make your stomach burst.* *If I ever get out.* > **System** > > The Qi Circulation Helper will run for the first session only. This wasn’t a case of stabbing someone and then applying medicine to the wound… > **System** > > Would you like to skip the Helper System? > > Accept / Decline I fixed my trembling gaze on the message window. “D-Decline.” > **System** > > Continuing. *That was a coincidence, right? Yeah. It had to be.* Before my uneasy feeling had even faded, my vision flipped upside down. And when I came to, I was in an unfamiliar gray space. “Over here.” I whipped my head around in surprise and saw an old man beckoning me. *If an old man who looked like that called me over in a dream, I’d turn around and run for my life. But this was a game.* *So he’s the helper.* Even if I hadn’t reasoned it out, I would have followed him without much suspicion. It was strange, even to me, but that was how I felt. An inexplicable sense of familiarity. And trust. “Take the most comfortable position.” *Huh? Aren’t you supposed to sit cross-legged when circulating qi?* As if he had read my thoughts, the old man answered. “Weaklings fuss over things like that. Masters don’t need to.” I could smell it in his calm voice. I could smell it. *This was the scent of a master. The real deal had finally appeared!* “Good grief. What a handful.” His wrinkled hand seemed to reach toward me, then vanished in a blur. Huh? Tap. Tap-tap. Something flashed past, and the next moment, I was frozen stiff. *Was this what it felt like to be a corpse with its eyes still open?* I couldn’t move a muscle. “It’s only a simple acupoint-sealing technique, so don’t be alarmed. Focus from this point on.” As he spoke, the old man placed a hand on my back. Then he rapidly rattled off words in a low voice. “Circulating qi is the most important training for a martial artist. It not only allows you to accumulate internal energy, but also refines essence, qi, and spirit, enabling you to advance to a higher realm. Therefore…” I listened closely, but I couldn’t understand a word of what came after that. I only understood that circulating qi was extremely important. “Clear your mind like a stream, maintain your focus, and draw out the flow. Now I will recite the formula of the Jin Family’s Cultivation Technique.” Without giving me time to stop him, he rattled off the formula at breakneck speed—like beans popping in a pan—but I could hear it all. It felt as though words in a foreign language were being translated automatically inside my head. *What is this?* The formula was exactly 318 characters long. The moment I felt it become perfectly engraved in my mind, something changed. “Descend.” One word from the old man. *Where to?* Before the question could fade, I felt myself being drawn somewhere deep. No—it only felt as though I was being drawn in. My eyes were definitely closed, but I could see. I could feel. The breeze that gently blew in before scattering. Sunlight. The coachman’s breathing and the horses’ snorts… I pushed all of it away. There was only one place to focus on: my body. > **System** > > Beginning the circulation of Jin Family’s Cultivation Technique. Follow the glowing acupoints. I didn’t notice the old man disappear. I didn’t even hear the System’s voice. My consciousness, awakened in my head, slid downward. I didn't know the points shining like stars were acupoints. Everything simply felt familiar, as though it had always been this way. At last, I reached my dantian. A small but pure energy. Ten years of internal energy. *But what’s that?* In one corner of my dantian was something else, as large and hard as a boulder. I understood instinctively. *More internal energy.* It was energy that I—Jin Taekyung—had not yet assimilated and made my own. It was almost as vast as the internal energy I already possessed. *What if I absorb it?* There was no question that I would become stronger. But for me, right now, it would be a reckless challenge. An adventure without a purpose. *I can’t push my luck and die out here.* I steadied my mind and stirred my internal energy. Following the path the System voice had shown me, I slowly guided it along. At some point, I thought I faintly heard someone’s voice. “Good judgment.” * * * > **System** > > Qi circulation complete. > > Tutorial—Stage 4 complete. Rewards will be distributed! > > You have gained insight into the Skill Qi Sense. You can now manipulate qi more freely and sense the energy of others. > > A small amount of turbid qi has been expelled. > > . > > . > > . > > You have completed all Tutorial stages. > > Main Quest created. With the System’s final voice, the coachman spoke. “We’ve arrived. This is the Jin Family of Taiyuan.” *Yeah. At last.*

## Korean source

```text
＃6화



언덕에서 내려다본 태원진가는 하나의 마을 같았다.

너른 대지 위, 크고 작은 수십 채의 건물이 펼쳐져 있었고 높이 쌓아 올린 돌담은 가문의 외곽을 빈틈없이 둘러쌌다.

그뿐인가, 태원진가의 뒤에 드리워진 절벽은 장관 그 자체다.

세월을 품은 자연과 그 아래 웅크린 하나의 가문.

보는 것만으로도 상당한 위압감이 느껴졌다.

“우와.”

마부도 감탄할 정도다. 아니, 잠깐만.

“여기 자주 와 보신 거 아니었어요?”

“두 번짼데요.”

“……혹시 일 시작하신 지가?”

“달포도 안 됐습니다.”

이런 양파 같은 인간을 봤나.

얼굴이나 분위기는 20년 차 베테랑인데 신입 사원이라니.

‘하긴, 그 정도 경력이면 이 얼굴을 못 알아봤을 리가 없지.’

홍화루 문지방이 닳도록 드나들던 얼굴이다. 신입 사원이라면 나를 진무경으로 착각할 법도 하다.

‘일이 잘 풀려서 다행이지.’

마지막 튜토리얼 퀘스트도 끝냈고, 태원진가도 코앞에 둔 상황이라 나는 조금 안심할 수 있었다.

“조금만 천천히 몰아 주세요.”

“아, 예.”

마차의 속도가 줄어드는 것을 느끼며 스킬창을 열었다.



스킬창



[기감]

등급 : 無

제한 : 無

경지 : 일 성

효과 : 30레벨 이하의 대상을 파악할 수 있다.

설명 : 지정 범위 내의 대상을 탐색한다. 경지가 오를수록 탐색 가능한 범위와 레벨이 상승한다.





설명을 다 읽고 나니 문득 떠오르는 게 있었다.

‘딱 그거네. 전투력 측정기.’

유명 만화에서는 기계 장치로 상대의 전투력을 수치화해서 파악하던데 [기감]은 어떨지 모르겠다.

나는 호기심을 느끼며 명령어를 떠올렸다.

‘기감 발동.’

이게 맞나? 잠깐 멈칫한 그 순간 발밑에 푸른 원이 생성됐다. 동시에 알림이 울렸다.

띠링.



- [기감]을 사용하셨습니다. 현재 1성의 경지이므로 Lv.30 이하, 10장 이내의 대상을 탐색할 수 있습니다.



10장이면 30m다.

솨아악. 쭉 뻗어 나가는 푸른 동심원에 한 사람이 걸려들었다. 마부의 둥그런 뒤통수 위로 시스템창이 불쑥 솟아오른다.



- [기감]으로 상대를 파악했습니다.



[Lv.4 장삼]



아하, 이런 식이구만.

‘쉽고, 간단하고, 무엇보다…….’

생존을 위해서 꼭 필요한 스킬이다. 적이 강한지, 약한지, 혹은 나랑 비등한지. 기감을 사용한다면 바로 파악할 수 있다.

‘괜찮은 거 하나 건졌네.’

고개를 끄덕이고 퀘스트창을 열었다. 그리고 새로 받은 [메인 퀘스트]를 확인한 순간, 나도 모르게 입이 벌어졌다.

“……어?”

눈앞이 환하게 밝아지는 기분이다. [기감]이 시궁창에 비친 한 줄기 빛이라면 이건 태양이다. 가슴이 쿵쿵 뛰고 머리가 뜨겁게 달아오른다.



퀘스트



[로그아웃]

이제 당신은 이 험난한 무림을 헤쳐 나가야 합니다.

더욱더 강해지고, 유명해지십시오.

언젠가 다가올 그 날을 위해…….



등급 : 메인 퀘스트

제한 : 진태경

임무 : [일류] 경지 달성 (미완료)

         Lv.30 달성 (미완료)

         명성 500 달성 (미완료)

보상 : [로그아웃]





간절히 바랐던 네 글자.

‘로그아웃!’

기쁘면서도 얼떨떨했다. 무슨 수를 써서라도 살아남겠다는 의지는 있었지만 일말의 불안감이 마음 한구석에 자리했던 탓이다. 내가 나갈 수 있을까? 영영 나가지 못하는 건 아닐까? 하는 그런 불길한 짐작.

‘나갈 수 있다.’

하지만 이제는 다르다. 로그아웃할 수 있다는 확신이 생겼다. 정신이 새로 깨어나는 기분이다.

‘그래, 시발. 기껏해야 게임이지.’

퀘스트? 그까짓 게 뭐 얼마나 어렵다고.

7년간 하루가 멀다고 사선을 넘나들었다. 헌터의 생존력과 의지는 일반인의 그것에 비할 바가 아니다.

‘그리고 이 힘.’

자연스럽게 주먹이 쥐어진다. 이 모든 것은 가상에 불과하지만, 몸에 넘쳐흐르는 힘만큼은 생생하게 느껴진다.

그래서 알 수 있었다.

게임에서의 내가, 현실의 나보다 강하다는 사실을.

아주 근소한 차이에 불과하지만 확실했다.

‘시스템 덕분이지.’

레벨 업, 퀘스트, 스탯 분배와 스킬. 이 모든 게 시스템의 힘이다. 게임이라서, 유저라서 가능한 일.

헌터로서의 경험과 시스템을 활용한다면 로그아웃은 시간문제에 불과하다.

‘나가면 다 뒤졌어.’

게임 개발진부터 족친다. 시발 새끼들. 부득부득 이를 가는 내 귓가로 누군가의 외침이 들려왔다.

“정지!”



* * *



통일된 복장. 절도 있는 자세와 딱딱한 목소리.

태원진가의 대문을 지키는 무사들을 본 순간 ‘무림인’이라는 단어가 뇌리를 스쳤다.

‘명문가라더니.’

확실히 다르다. 앞서 맞닥트린 천력부와 산적들이 오합지졸이라면 이쪽은 훈련받은 정규군이라고 해야 하나.

그중 한 NPC가 마부를 향해 다가왔다. 앳된 얼굴에 굵은 송충이 눈썹이 인상적인 무사였다.

“대태원진가의 수문조장 혁무진입니다. 신원과 방문 목적을 밝혀 주십시오.”

수문조장이라. 그러고 보니 혼자 완장 비슷한 띠를 두르고 있다. 딱 봐도 스물이나 됐을까 싶은 젊은 녀석인데.

‘하긴, 능력만 좋으면 장땡이지.’

내가 그런 생각을 하고 있을 때 마부가 대답했다.

“홍화루에서 왔습니다.”

“홍화루? 설마 기루를 말하는 거요?”

“예.”

창문 너머로 NPC. 아니, 혁무진의 얼굴이 찡그려지는 게 보였다. 제법 정중했던 말투도 대번에 반 토막이 났다.

“기루에서 본가에 무슨 용무가 있다고?”

“아, 그게…….”

어딜 가나 꼭 저런 놈들이 있다. 대기업에서 근무한다고 본인이 재벌인 줄 아는 놈. 정작 재벌은 따로 있는데 말이지. 나는 조용히 창문을 열고 기침했다.

“커험. 흠흠.”

다분히 의도된 헛기침이다. 성공한 인생들만 할 수 있다는 일명 ‘나 누군지 몰라?’ 헛기침.

“음.”

아니나 다를까, 혁무진은 한눈에 나를 알아봤다. 나는 잔잔한 미소와 함께 입을 열었다.

고위급 정치인, 군인, 기업인들 사이에서 폭넓게 사용되는 마법의 대사다.

“음. 그래. 수고.”

그리고 창문을 닫으려는데…….

턱. 덜컥.

“응?”

안 닫힌다. 불쑥 튀어나온 손이 창문을 붙잡고 있었다.

손의 주인은 당연하게도 혁무진이었다. 닫히다 만 창문 사이로 딱딱하게 굳은 얼굴이 보였다.

“내리시오.”

“어, 나?”

“그럼 내가 허공에 대고 얘기했겠소?”

뭐야, 이거. 이 자식 반응이 왜 이래?

‘못 알아봤군.’

나는 너그러운 미소를 지어 보였다.

“모르나 본데, 나 이 집 사는 사람이야.”

“나도 여기 사는 사람이오.”

“아니, 내 말은 그러니까…….”

“태원진가의 삼공자다. 뭐 그런 말을 하고 싶은 거요?”

“…….”

정확히 맞췄다. 혁무진이 말을 이었다.

“공자가 누군지는 충분히 알고 있으니 이제 마차에서 내리시오. 절차대로 진행하겠소.”

별수 있나. 절차라는데. 하지만 마차에서 내리는 내 머릿속에서는 경고등이 울리고 있었다.

‘어째 느낌이 쎄한데.’

태원진가의 다른 NPC들도 왠지 모르게 싸늘한 눈빛을 던졌다. 얼굴이 따가워지려고 할 때 혁무진이 종이와 붓을 꺼내 들고 말했다.

“이름.”

“…….”

“다시 묻겠소. 이름.”

이건 뭐 범죄자 취조하는 것도 아니고.

기분이 더러웠지만 일단 상황을 지켜보기로 마음먹었다.

“……진태경.”

“소속.”

“태원진가.”

“나이와 무공 경지.”

“스물. 이류.”

그 순간 혁무진의 붓이 멈칫했다.

“괜한 자존심 부리지 말고 정직하게 대답하시오.”

정직하게?

‘스탯 분배해서 이류로 올랐습니다. 하면 알아듣겠냐?’

대답 대신 혁무진의 얼굴을 빤히 바라보자 놈이 고개를 절레절레 저었다.

“뭐, 정 그렇다면 넘어갑시다. 그럼 어디 보자…… 며칠간 자리를 비우셨는데, 어딜 다녀오셨는지?”

“홍화루.”

“이야, 그 비싸다는 홍화루에서 며칠씩이나? 좋았겠소. 한 재산 썼겠구먼. 아니면 이번에도 문파 공금을 슬쩍하셨나?”

“이번에도?”

“뭘 발뺌을 하고 그러시오. 공자가 종종, 왕왕, 으레 해 왔던 일 아니오?”

혁무진의 적의 어린 눈빛을 본 순간, 어떤 사실 하나가 떠올랐다.

‘진태경.’

잠시 잊고 있었다. 이 게임에서, 특히 태원진가에서 진태경이라는 캐릭터가 어떤 존재인지.

‘가문의 수치.’

이따위 칭호까지 달고 있는 놈을, 태원진가의 NPC들이 좋아할 리 만무했다. 그걸 증명이라도 하듯 이 순간 저들의 경멸은 오롯이 나를 향하고 있다.

뭐 하나 내 뜻대로 되지 않는 이 게임 속에서.

‘아, 진짜…….’

폐부 깊숙한 곳에서 뭔가가 울컥거렸다. 머리가 아프고 눈이 뜨겁게 달아오른다. 그런 내게 나지막한 목소리가 들려왔다.

“삼공자, 내 비록 말단 조장이지만 한마디만 합시다.”

한심한 놈. 혁무진이 그런 표정으로 말했다.

“더 이상 가문의 명성에 먹칠하지 마시오. 최소한 사람답게 살란 말이오. 알겠소?”

한마디를 툭 던져 놓고 돌아서는 놈의 뒤통수를 멍하니 바라봤다. 헛웃음이 나온다.

“사람답게 살라고?”

안다. 혁무진은 아무것도 모르는 NPC에 불과하다는 것을.

내가 아니라 진태경에게 하는 말이라는 것을.

하지만…….

‘좆 같네.’

이곳이 게임 안이고 혁무진이 NPC라는 사실은 중요하지 않았다. 아니, 생각하지 않기로 했다.

그동안 쌓인 모든 스트레스가 터져 나오면서 마지막 인내심마저 허물어졌다.

“야. 거기 딱 서.”

혁무진이 돌아섰다. 짜증 난 얼굴이다. 아까부터 저 면상에 한 대 꽂아 주고 싶었지.

나는 산타클로스를 본 아이처럼 활짝 웃었다.

“넌…… 뒤졌어.”

불끈 쥔 주먹을 놈의 턱주가리를 향해 날렸다.



* * *



묵직한 공기. 탁자 위로 높게 솟은 서류 더미. 그리고 늘 그림자처럼 주인의 곁을 지키는 서늘한 인상의 호위 무사.

사각. 사각.

수문각주는 침을 삼켰다. 집무실에 들어온 순간부터 그의 입은 바싹바싹 타들어 가고 있었다.

“말해 보게.”

서류 더미 너머로 들리는 담담한 목소리는 오아시스다.

수문각주가 간신히 말문을 뗐다.

“제 수하 중에 아까운 놈이 하나 있습니다. 본가에 대한 충성심도 제법이고 무재가 뛰어난 녀석인데…….”

“듣고 있네.”

“어린놈이라 그런지 오만불손하고, 앞뒤 재는 법을 모릅니다.”

“본론만.”

“삼공자와 시비가 붙었답니다.”

“……알 만하군. 막내는?”

“신속히 약왕당으로 옮겼습니다. 지금은 혼절 상태인데 타박상이 조금…….”

순간 침묵이 흘렀다.

“모두 속하의 잘못입니다. 엄벌을 내려 주십시오!”

눈앞이 캄캄해진 수문각주는 고개를 깊게 숙였다. 재차 목소리가 들려온 것은 한참 후였다.

“그만하면 되었네. 이만 나가 보게.”

수문각주가 기사회생의 심정으로 고개를 들었을 때였다.

“아, 하나만 더.”

“하명하십시오.”

“그 친구 좀 볼 수 있겠나? 잠시 이야기를 나눠 보고 싶은데.”

“저어, 소가주님. 말씀드리기 송구스럽지만, 아직 치료가 덜 끝났습니다.”

“치료?”

“예. 그 친구도 약왕당에 있습니다. 듣기로는 뼈에 금이 갔다더군요.”

“……그런가? 그럼 되었네.”

수문각주가 물러난 후에도 이어지던 침묵은 위태롭게 쌓여 있던 서류 탑이 와르르 무너지면서 깨졌다.

“위팽.”

태원진가의 소가주이자 올해 서른다섯이 된 진위경이 굳은 얼굴로 자신의 충복을 불렀다.

“예.”

“잠시 자리 좀 비우겠네.”

또 시작이군. 진위경의 호위 무사, 위팽은 의미를 알 수 없는 한숨을 내쉬며 진위경의 뒷모습을 바라봤다.
```

## Current accepted English baseline

```markdown
# Chapter 6

The Jin Family of Taiyuan looked like an entire village from the hill above it.

Dozens of buildings, large and small, spread across the broad grounds, while high stone walls wrapped around the family estate without leaving a single gap.

And that wasn’t all. The cliff rising behind the Jin Family of Taiyuan was a spectacle in itself.

Nature that had weathered the ages, and one family crouched beneath it.

The sight alone was deeply imposing.

“Wow.”

Even the coachman was impressed. Wait, hold on.

“Didn’t you say you’d been here often?”

“This is my second time.”

“…You’ve only been working for how long?”

“Not even half a month.”

This guy had more layers than an onion.

He looked and carried himself like a twenty-year veteran, but he was a new hire.

*Then again, if he really had that much experience, there was no way he wouldn’t recognize this face.*

I’d practically worn a path to Honghwaru’s door from coming and going so often. If he was a new hire, it made sense that he might mistake me for Jin Mukyung.

*Good thing everything worked out.*

I had completed the final Tutorial Quest, and the Jin Family of Taiyuan was right in front of me. I could finally relax a little.

“Could you slow down a bit?”

“Ah, yes.”

As I felt the carriage slow, I opened my Skill Window.

> **System**
>
> Skill Window
>
> **Qi Sense**
>
> **Grade:** None
>
> **Restriction:** None
>
> **Realm:** 1st Mastery
>
> **Effect:** Can identify targets at or below Lv. 30.
>
> **Description:** Scans targets within a designated range. As the realm rises, the scan range and maximum target level increase.

When I finished reading the description, something suddenly occurred to me.

*That’s exactly what it is. A power-level scanner.*

In a famous manga, a mechanical device quantified an opponent’s battle power. I wondered what Qi Sense would be like.

Curious, I called to mind the command.

*Activate Qi Sense.*

Was that right? I hesitated for a moment, and then a blue circle appeared beneath my feet. At the same time, a notification chimed.

Ding.

> **System**
>
> - You used Qi Sense. Since your current realm is 1st Mastery, you can scan targets at or below Lv. 30 within 10 jang.

Ten jang—that was 30 meters.

Whoosh. A blue concentric wave stretched outward and caught one person in its radius. A System window sprang up over the coachman’s round head.

> **System**
>
> - You identified the target with Qi Sense.
>
> **Lv. 4 Jang Sam**

Aha. So that was how it worked.

*Easy, simple, and most of all…*

It was an essential skill for survival. Whether an enemy was strong, weak, or roughly on my level—I could find out at once by using Qi Sense.

*I got a pretty good one.*

I nodded and opened the Quest Window. The moment I checked the new Main Quest, my mouth fell open before I knew it.

“…Huh?”

The world before me seemed to flare into light. If Qi Sense was a single ray reflected in a sewer, this was the sun. My heart pounded, and heat rushed to my head.

> **System**
>
> Quest
>
> **Logout**
>
> Now you must make your way through this harsh Murim.
>
> Grow stronger and become famous.
>
> For that day, when it finally comes…
>
> **Grade:** Main Quest
>
> **Restriction:** Jin Taekyung
>
> **Objective:** Reach the First Rate realm (Incomplete)
>
> Reach Lv. 30 (Incomplete)
>
> Reach 500 Fame (Incomplete)
>
> **Reward:** Logout

The one word I had been desperate to see.

*Logout!*

I was happy, but dazed too. I had been determined to survive by any means necessary, yet a sliver of anxiety had always remained in the back of my mind. *Can I get out? What if I can never leave?* Those ominous suspicions had been there all along.

*I can get out.*

But now things were different. I was certain I could log out. It felt as if my mind had awakened anew.

*Yeah, fuck it. At the end of the day, it’s just a game.*

A quest? How hard could it be?

For seven years, I had crossed the line between life and death almost every day. A Hunter’s ability to survive—and sheer willpower—were beyond comparison with an ordinary person’s.

*And then there’s this power.*

My fist clenched on its own. All of this might be virtual, but the power surging through my body felt real enough.

That was how I knew.

I was stronger in the game than I was in reality.

The difference was tiny, but it was definite.

*It’s all thanks to the System.*

Leveling up, Quests, distributing stats, and skills. All of it was the power of the System—things that were possible because this was a game and I was a player.

With my experience as a Hunter and the System at my disposal, logging out was only a matter of time.

*Once I get out, they’re all fucking dead.*

I’d start by beating the shit out of the game’s developers. Fucking bastards. I was grinding my teeth when someone shouted in my ear.

“Stop!”

* * *

Uniforms. Disciplined postures. Clipped voices.

The moment I saw the martial artists guarding the main gate of the Jin Family of Taiyuan, the word *martial artist* flashed through my mind.

*So this is what a prestigious family is like.*

They were definitely different. The Heavenly Axe and the bandits I’d run into before had been a rabble. These people were more like a trained regular army.

One of the NPCs approached the coachman. He was a martial artist with a young face and thick caterpillar eyebrows.

“I’m Hyuk Mujin, Captain of the Gatekeepers of the great Jin Family of Taiyuan. State your identity and the purpose of your visit.”

Captain of the Gatekeepers. Come to think of it, he was the only one wearing a band resembling an armband. He looked young enough to be twenty, at most.

*Then again, if you’re talented enough, that’s all that matters.*

While I was thinking that, the coachman answered.

“We’re from Honghwaru.”

“Honghwaru? You mean the pleasure house?”

“Yes.”

Through the window, I saw the NPC’s face—or rather, Hyuk Mujin’s face—twist into a frown. His previously polite manner turned curt on the spot.

“What business could a pleasure house possibly have with our family?”

“Ah, well…”

No matter where you went, there were always people like this. The kind who worked for a conglomerate and thought that made them a chaebol. The actual chaebols were somewhere else entirely.

I quietly opened the window and coughed.

“Ahem. Hmm-hmm.”

It was a deliberately conspicuous cough. The famous *Don’t you know who I am?* cough, available only to people who had made it big in life.

“Hmm.”

Sure enough, Hyuk Mujin recognized me at a glance. I opened my mouth with a mild smile.

It was a magic phrase used by high-ranking politicians, soldiers, and businessmen.

“Hmm. Right. Good work.”

I was about to close the window when…

Clack. Rattle.

“Huh?”

It wouldn’t close. A hand had shot forward and caught the window.

The owner of that hand was, of course, Hyuk Mujin. Through the half-closed window, I saw his face, stiff as a board.

“Get down.”

“Me?”

“Who else? Did you think I was talking to the air?”

What the hell? Why was this guy reacting like that?

*He didn’t recognize me after all.*

I put on a generous smile.

“You might not know this, but I live in this house.”

“So do I.”

“No, what I mean is…”

“The Third Young Master of the Jin Family of Taiyuan. Is that what you’re trying to say?”

“…”

He had hit the nail on the head. Hyuk Mujin continued.

“I know perfectly well who you are, Young Master. Now get down from the carriage. We’ll follow procedure.”

What else could I do? He said it was protocol. But warning lights were flashing in my head as I climbed down from the carriage.

*Why does this feel so ominous?*

The other NPCs in the Jin Family of Taiyuan were giving me strangely chilly looks too. Just as their stares began to make my face burn, Hyuk Mujin took out paper and a brush and spoke.

“Name.”

“…”

“I’ll ask again. Name.”

What was this, a criminal interrogation?

I was in a foul mood, but decided to wait and see what happened.

“…Jin Taekyung.”

“Affiliation.”

“Jin Family of Taiyuan.”

“Age and martial arts realm.”

“Twenty. Second Rate.”

Hyuk Mujin’s brush paused.

“Don’t let pointless pride get in the way. Answer honestly.”

Honestly?

*I raised my rank to second-rate by assigning stats. Would that mean anything to you?*

When I simply stared at Hyuk Mujin’s face instead of answering, he shook his head.

“Well, if that’s how you want it, we’ll move on. Now, let’s see… You’ve been away for several days. Where have you been?”

“Honghwaru.”

“Wow, you spent several days at expensive Honghwaru? Must have been nice. You must have blown a fortune. Or did you skim the family funds again?”

“Again?”

“Why pretend otherwise? Isn’t that something the Young Master has done now and then, time and time again, as a matter of course?”

The hostility in Hyuk Mujin’s eyes reminded me of one fact.

*Jin Taekyung.*

I had forgotten for a moment what the character Jin Taekyung was in this game—especially in the Jin Family of Taiyuan.

*The Shame of the Family.*

There was no way the Jin Family of Taiyuan’s NPCs would like someone saddled with a title like that. As if to prove it, their contempt was aimed entirely at me now.

In this game where nothing went the way I wanted.

*Ah, for fuck’s sake…*

Something surged up from deep in my chest. My head throbbed, and heat rose behind my eyes. Then I heard a low voice.

“Third Young Master, I may only be a low-ranking squad leader, but let me say one thing.”

He said it with a look that made it clear what he thought of me: *What a pathetic bastard.*

“Stop disgracing the family’s reputation. At least try to live like a human being. Understood?”

He tossed out that one remark and turned away. I stared blankly at the back of his head, then let out a hollow laugh.

“Live like a human being?”

I knew Hyuk Mujin was nothing more than an NPC who knew nothing.

I knew he was saying it to Jin Taekyung, not to me.

But…

*This is fucking bullshit.*

The fact that this was a game and Hyuk Mujin was an NPC didn’t matter. No—I decided not to think about it.

All the stress that had piled up over the past few days burst out, and even the last of my patience crumbled.

“Hey. You. Stop right there.”

Hyuk Mujin turned around with an annoyed look on his face. I’d wanted to punch that face since earlier.

I beamed like a child who had just seen Santa Claus.

“You’re… fucking dead.”

I sent my clenched fist flying toward his jaw.

* * *

The air was heavy. A pile of documents rose high above the desk. And, as always, a cold-looking escort stood beside his master like a shadow.

Scratch. Scratch.

The Chief of the Gatekeeping Pavilion swallowed. From the moment he entered the office, his mouth had been bone-dry.

“Tell me.”

The calm voice drifting from beyond the pile of documents was an oasis.

The Chief of the Gatekeeping Pavilion finally managed to speak.

“There’s one promising man among my subordinates. He’s quite loyal to the main family, and he has considerable martial talent, but…”

“I’m listening.”

“Perhaps because he’s young, he’s arrogant and insolent. He doesn’t know how to think things through.”

“Get to the point.”

“I hear he got into a fight with the Third Young Master.”

“…I can imagine. What about the youngest?”

“We moved the youngest to Medicine King Hall immediately. He’s unconscious now, with some bruising…”

Silence fell.

“It was all my fault. Please punish me severely!”

The Chief of the Gatekeeping Pavilion bowed deeply, his vision going dark. A long while passed before the voice came again.

“That’s enough. You may leave.”

The Chief of the Gatekeeping Pavilion raised his head, feeling as if he had narrowly escaped death.

“Ah, one more thing.”

“Yes, Lesser Family Head.”

“Could I see that fellow? I’d like to speak with him for a moment.”

“Lesser Family Head, I’m sorry to say this, but his treatment isn’t finished yet.”

“Treatment?”

“Yes. He’s at Medicine King Hall too. I hear one of his bones was cracked.”

“…I see. Then never mind.”

The silence that continued after the Chief of the Gatekeeping Pavilion withdrew was broken when the precariously stacked tower of documents came crashing down.

“Wipeng.”

The thirty-five-year-old Lesser Family Head of the Jin Family of Taiyuan, Jin Wikyung, called to his trusted retainer, his expression stiff.

“Yes.”

“I’m going to step out for a while.”

*Here we go again.*

Wipeng, Jin Wikyung’s escort, let out an inscrutable sigh as he watched his master walk away.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 6`.
