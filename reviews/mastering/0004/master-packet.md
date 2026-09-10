# Master Edit Task — Chapter 4

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
| 진무경    | **Jin Mukyung**    |
| 월화     | **Wolhwa**         |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 태원진가   | **Jin Family of Taiyuan**        |
| 삼류     | **Third Rate**    |
| 이류     | **Second Rate**   |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 스킬               | **Skill**                      |
| 레벨               | **Level**                      |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

(No prior chapter summary available.)

### Prior accepted reading-copy tails

#### Chapter 2 tail (verified mastered)

…
Check it later through the Status Window. *A title? Scion of a Prestigious Family?* I guessed it was something like a title in a fantasy game. *Dragon Slayer, or something like that.* You received one after accomplishing a certain feat, and equipping it granted additional effects. In that respect, I had to say I was pretty lucky. *This guy really was born with a silver spoon in his mouth.* Being born into a prestigious family counted as an achievement. It pissed me off and made me happy at the same time. That meant the random character selected against my will had turned out to be a lottery winner. But the story didn’t end there. “I’ve heard there are problems inside and outside the family these days.” “Problems? What kind of problems?” Come to think of it, the quest window’s information-gathering mission was still marked *Incomplete*. That meant there was more information to collect. “Externally, there’s the conflict with the Mount Heng Sword Sect, which is constantly eyeing the position of Shanxi’s hegemon. Internally…” Wolhwa leisurely tapped the ash from her pipe. “I hear that family’s third son is a notorious good-for-nothing.” “Ah. There’s always one of those wherever you go.” I nodded unconsciously, then was seized by a strange feeling. “Excuse me.” “Yes?” “I’m only asking as a joke, but how many sons does the Jin Family of Taiyuan have?” She answered with a sunny smile. “Three.” The Jin Family of Taiyuan had three sons, and I was the youngest of them. But the third son was a notorious good-for-nothing. Which meant— *Fuck. That’s me, isn’t it?* Ding. > **System** > > Title Shame of the Family acquired. Check it later through the Status Window. > > Gather Information complete. I couldn’t decide whether to laugh or cry. Then I saw Wolhwa snickering and let out a hollow laugh myself. *Well, better to look on the bright side. So what if I’m the shame of the family? It’s only a game, anyway.* I opened the quest window and confirmed that *Gather Information* had changed to *Complete*. *The problem is understanding the situation.* This damn quest was so vague that I had no idea what exactly it wanted. In the end, was Wolhwa my only solution? “Where are we?” “Honghwaru, the finest pleasure house in Shanxi. This is my room.” Through our conversation, I learned a few more miscellaneous facts. We were in Honghwaru, located in the heart of Taiyuan. Wolhwa was a fairly high-ranking courtesan, and I had spent the night with her… Ahem. Despite all the various things we discussed, no System notification appeared. Eventually, I ran out of questions to ask. At the very end, I was reduced to asking this: “What’s my situation right now?” Wolhwa sighed. “Young Master Jin, I’m sorry to say this, but you seem a little crazy right now. How about getting some rest?” *Yeah. I feel like I’m going crazy, too.* As sunlight streamed through the window, I began to wonder what on earth I was doing. *This isn’t some kind of mystery game.* The graphics and artificial intelligence were all great, but being stuck at the tutorial had completely drained the fun out of it. If there was one thing I’d learned, it was that the capsule I’d found yesterday was a much better piece of equipment than it looked. A game this advanced had to require serious hardware, yet I hadn’t experienced a single bit of lag. It should sell for a decent price on the used market. *I need to start looking for a new job today, too.* Still, the game hadn’t been bad for the little while I’d played it. I gave Wolhwa a final nod and shouted: “Log out!” > **System** > > Logout is impossible. *Huh?* “Log out.” > **System** > > Logout is impossible. *What’s going on?* An error? Or had the ancient capsule finally started lagging? “…Log out?” > **System** > > Logout is impossible. There was no doubt about it. Error or lag, the damn old capsule had finally caused trouble. I tried ten more times after that, but every attempt failed. By this point, my anger had gradually turned into worry and regret. *Is something bad going to happen to me?* *I shouldn’t have picked it up just because it was free. I should have thrown it away the moment Jinho called it garbage. Or at least the moment I read that insane instruction manual…* *No. Wait.* The instruction manual. That was right—I’d read it. More precisely, I’d read a few of the warnings before tossing it aside, but I had read them. *What did they say?* The moment I finally remembered every warning I’d managed to read, a chill ran through my entire body. > **Warning** > > - The player cannot log out at will. > - If the player dies during gameplay, resurrection is impossible. *I’m trapped inside the game? Me?* The System notification answered my question for me. Ding. > **System** > > Understand the Situation complete. > > Tutorial—Stage 1 complete. Rewards will be distributed. > > Status Window activated. > > Skill Window activated. > > Inventory activated. > > Chain Quest Tutorial—Stage 2 created. At that moment, a single thought filled my head. *I’m fucked.* [^1]: A room salon is a Korean private-room entertainment venue where customers are served food, alcohol, and conversation by hostesses.

#### Chapter 3 tail (verified mastered)

…
and blood vessels, while Bones meant muscles and the skeletal frame. In other words, Sinews were for an internal-energy-focused build, while Bones were for external martial arts. I decided to lean a little more toward Bones. The reason was simple. *I’ll have a better chance of surviving if I choose what I’m already familiar with.* In the real world, I was an F-rank Hunter. In Murim terms, I was a third-rate martial artist, or maybe even worse. Magic and aura… I’d seen them with my own eyes, but using them myself was out of the question. I couldn’t even dream of it. *You’re always better at something you’ve done before.* You had to have used internal energy before to know how to use it. The way I’d fought over the past seven years was closer to that of an external martial artist. *Sixty into Bones. Forty into Sinews.* > **System** > > Apply these settings? *Yes. Apply.* This time, what swept through me was nothing like the exhilaration I’d felt from the Status Window. If anything, it was pain. I could hear the bones deep inside my body twisting. *Urgh.* Seconds? Minutes? I had no idea. When the pain passed, all that remained was my ragged breathing—and the reward for enduring it. *My build…* It had changed. My shoulders had broadened by half a span, and muscle had hardened across my front and back. The silk clothes that had felt a little loose now felt constricting. When I clenched my fists, I felt strength and springiness I hadn’t been able to sense before. I’d grown stronger. It was an experience I’d never had in the real world. *Because there’s no System there.* I could build strength, stamina, and flexibility through training in the real world, but until I underwent a measurement, I could only sense the changes vaguely. But Murim was different. I could see my abilities through the Status Window and improve the ones I needed. I didn’t know where the endpoint was, but I could keep moving forward. *I’ll get stronger. And I’ll survive.* I’d fought countless monsters over the past seven years. Some days I’d returned without a scratch; other days I’d barely escaped with my life. F-rank Hunter Jin Taekyung had something Murim’s Jin Taekyung didn’t: experience. And desire. Stronger, stronger, stronger. And survive. Just as I clenched my fist and made that vow, another notification rang out. Ding. > **System** > > Check and Distribute Skill Window Points complete. Only one thing remained. *Check the Inventory.* Ding. > **System** > > Inventory > > Sturdy Martial Uniform Set > > **Grade:** Third Rate > > **Restriction:** None > > **Effect:** None > > **Description:** Made from light, durable cloth. Suitable for beginners. The description was simple, befitting a basic item. *Equip item.* A refreshing sensation swept over me, and I found myself dressed in a black martial uniform. It wasn’t just my clothes that had changed. A headband—commonly called a hero’s headband in martial-arts novels—was tied firmly around my forehead, and I was wearing leather shoes instead of silk ones. Did I at least look like a run-of-the-mill martial artist now? *Store item.* The moment I thought about storing the silk clothes I’d taken off, they vanished from my hands. *An Inventory. This is incredibly convenient.* It might even be useful in combat, depending on how I used it. *Having an Inventory would make raids so much easier.* With one of these, I could hang back and collect Magic Gems without even fighting the monsters. I’d make enough in a year to put up a whole building. *But that’s not going to happen.* Because this was a game. Once I logged out, it would all be over. …Though I wasn’t even sure I’d survive long enough to log out. Ding. > **System** > > Check and Equip Inventory Items complete. > > Tutorial—Stage 2 complete. Rewards will be distributed. > > Chain Quest Tutorial—Stage 3 created. A new reward! I immediately opened the Inventory to check the new item. > **System** > > Inventory > > Sharp Spear > > **Grade:** Second Rate > > **Restriction:** None > > **Effect:** 5% chance to inflict Bleeding on hit > > **Description:** A reasonably usable spear. It’s sharp, so be careful when handling it. “…” If my Status Window and Skill Window were going to be such a mess, couldn’t they at least give me a good item? Then again, considering everything that had happened so far, this was practically generous. *Equip item.* The moment the shaft of the spear appeared in my grasp— Ding. > **System** > > Tutorial—Stage 3 begins. Prepare yourself. “…Huh?” Prepare myself? For what? I hadn’t even opened the quest window yet. The answer came from an unexpected place. The taciturn coachman spoke for the first time. “Young Master.” “Yes?” “A minor problem has arisen.” “What are you talking about all of a sudden—” Ding. > **System** > > Quest > > Tutorial—Stage 3 > > You have learned how to grow stronger through the System. > > What you learn must produce results. > > Defeat the bandits who have appeared without warning! > > **Grade:** Tutorial (Chain Quest) > > **Restriction:** First-time player > > **Objective:** Defeat the bandits (Incomplete) > > **Reward:** Recover from all injuries > > Chain Quest > > **Failure:** Death *Some minor problem.* My ass.

## Korean source

```text
＃4화



장삼은 산적이다.

생전 오대산(五臺山) 인근을 벗어난 적 없는 토박이였고 약관 무렵부터 만만한 산객들을 대상으로 통행료를 뜯어내 왔다.

밤낮을 가리지 않는 성실 영업 덕분인지 언제부턴가 천력부 장삼, 하면 제법 알아주었다.

오늘도 그랬다. 꼭두새벽부터 일어나 충실한 다섯 부하, 오색귀(五色鬼)를 거느리고 영업을 나왔는데…… 이상하게 발걸음이 멈추지 않는다.

앞마당인 오대산을 한참 벗어나 얼마나 걸었을까, 마침내 발걸음이 멈췄을 때 저 멀리 다가오는 마차가 보였다.

‘어쩌다 여기까지 왔지?’

귀신에 홀렸나? 장삼은 어리둥절했지만 고급스러운 사두마차를 본 순간 자신의 직업 정신이 깨어나는 것을 느꼈다.

‘저건 꼭 뺏어야 해.’

장삼과 오색귀가 길을 막아서자 마부가 고삐를 잡아당겼다.

털에 윤기가 자르르 흐르는 준마 네 마리가 콧김을 뿜어내며 멈췄다. 척 봐도 마리당 천 냥은 거뜬하게 나올 물건들이다.

오늘은 일진이 좋군. 장삼은 흐뭇하게 웃으며 도끼를 고쳐 잡았다. 자, 이제 단전에 힘을 빡 주고. 하나, 둘.

“돈 내놔!”



* * *



발성 뭐야, 성악가야?

하지만 이 정도로는 눈 하나 깜짝 안 한다. 헌터 외길 인생 7년에 산전수전 공중전까지 다 겪은 나다.

……근데 좀 무섭다.

“총 여섯 명. 매복은 없어 보입니다.”

마부는 비밀 요원처럼 침착한 목소리로 상황을 전달했다.

이 아저씨는 믿는 구석이라도 있나. 왜 이렇게 여유롭지.

물끄러미 바라보자 머리를 긁적인다.

“간혹 있는 일입니다. 이 근방에서는 처음이지만요.”

“왜요?”

“왜긴요. 어지간한 대형 산채가 아닌 이상 무림세가를 건드리는 건 자살행위나 다름없습니다. 태원진가의 앞마당에서 도적질이라니, 어느 간 큰 놈들인지 궁금하군요.”

‘누구긴. 튜토리얼 NPC지.’

그보다 태원진가의 앞마당 운운하는 걸 보니 제법 가까운 거리인가 보다.

‘시간을 끌어 볼까?’

현재 내 경지는 이류.

스탯 분배 후 느껴지는 체감은 F급 헌터의 그것을 뛰어넘지만, 무림에서 먹힐 만한 수준인지는 모르겠다.

6 대 1. 마부까지 끼워 넣어도 6 대 2.

‘될까?’

중과부적이라는 말이 괜히 있는 게 아니다. 손발이 묶이는 순간 골로 간다.

“목적지까지 얼마나 남았습니까?”

“거의 다 왔습니다. 앞으로 반 시진이면 충분합니다.

반 시진이면…… 한 시간이나 남았다고?

짐작은 했지만 마부와 나의 ‘가깝다’는 서로 기준이 달랐다.

‘거의 다 오기는 무슨.’

대륙 배경이라 그런가. 스케일이 다르다, 스케일이.

어쨌든 그렇다면 이제 증원군은 없는 셈 쳐야 한다. 그나마 다행인 것은 혼자가 아니라는 점이다.

시종일관 여유로운 태도를 보이는 마부는 고수의 냄새를 풍겼다. 지금처럼.

“제가 처리할까요?”

그러면서 말채찍을 말아 쥐는데, 채찍질 한 번으로 산적들의 뼈와 살을 분리시킬 기세다.

‘고수다!’

그럼 그렇지. 내가 명색이 명문세가의 후계자요, 홍화루의 특급 고객인데 평범한 마부를 보내 줬을 리가 있나.

‘월화가 신경 써 줬구나. 얼굴만 예쁜 게 아니라 마음도 예쁘네.’

불안감이 사라지고 절로 흐뭇한 웃음이 지어진다. 내 웃음을 승낙의 의미로 받아들인 마부가 돌아섰을 때, 두 번째 고함이 터져 나왔다.

“이놈들! 이 천력부의 말이 들리지 않느냐!”

마차 창문 너머로 넘겨다보니 거대한 양날 도끼를 든 털북숭이가 소리를 치고 있었다. 우람한 상반신에 팔다리가 기둥처럼 두껍다.

하지만 마부는 가소롭다는 듯이 중얼거렸다.

“하룻강아지 같은 놈들이 어딜 감히.”

캬, 기세에 취한다.

그리고 마부의 준엄한 질타가 시작됐다.

“양민의 고혈을 빨아먹는 산적 따위가 감히 뉘 앞을 막아서느냐! 네놈을 관아로 압송하여 지엄한 국법으로 다스려 주마!”

판관 포청천 뺨치는 연설이었지만 털북숭이, 천력부와 그 부하들은 그리 감동한 것 같지 않았다.

“그래, 막아섰다. 이제 어쩔래?”

“무수한 악행을 저질러 온 네놈들의 눈알을 파내고 사지를 절구로 빻아 그 가루를 구주에 뿌려 주마! 또한 구족을 멸하여…….”

……형벌 수위가 장난이 아닌데. 거의 역모죄다, 역모죄.

내 생각을 읽은 것처럼 천력부가 입을 열었다.

“거, 안에 황족 나리라도 타셨소? 듣고 있자니 오금이 저려서 못 참겠네. 그 귀하신 얼굴 구경 좀 합시다.”

“이분의 정체를 알면 지금 물러나지 않은 것을 후회하게 될 것이다!”

“알겠어. 알겠으니까 이제 좀 나와 보라고.”

“어리석은 놈들……!”

마부가 혀를 차며 내게 고개를 돌렸다. 이제 드디어 진짜 무림 고수의 활약을 볼 수 있는 건가 싶어 가슴이 두근거린다.

“공자님. 나와 보셔야 할 것 같습니다.”

“응?”

나? 나 왜?

“관을 봐야 눈물을 흘릴 놈들입니다. 감히 공자의 앞을 막아서다니, 고수를 몰라본 죗값을 똑똑히 치르겠군요.”

그러면서 결의에 찬 표정으로 마차 문을 열어 준다.

“진천검(振天劍)의 위명은 익히 들었습니다. 불과 약관의 나이로 절정의 경지에 오른 천재 검수! 공자의 이야기를 들을 때마다 늙은 제 가슴이 얼마나 떨렸는지 모릅니다.”

……진천검? 천재 검수?

‘뭐라는 거야.’

머리가 뒤죽박죽이다. 진천검은 누구고, 절정에 오른 천재 검수는 누구며 이 마부는 뭐 하는 새끼인가?

처리하겠다며. 당신 고수 아니었어?

“이놈들! 이분이 누구신지 알아보겠느냐!”

틀렸다. 마부는 핸들이 고장 난 8톤 트럭처럼 폭주 중이다.

안 돼, 그만해. 멈춰!

마부의 손목을 꽉 움켜잡자 그가 나를 돌아본다.

다 안다는 듯한 웃음. 무한한 신뢰의 눈빛.

“자, 잠깐만. 저는 진…….”

내가 뭐라 할 틈도 없이 쩌렁쩌렁한 외침이 터져 나왔다.

“태원진가의 이공자, 산서성을 떨어 울리는 절정 고수! 진천검 진무경 공자이시다!”

“저는 진……태경인데요.”

순간, 싸늘한 찬바람이 불었다.

“예?”

“그러니까 저는 진무경이 아니라 진태경이고 이공자가 아니라 삼공자…….”

“……삼공자? 바로 그 삼공자?”

그래, 이 양반아.

마부의 동공이 흔들린다. 진도 8.0의 강진이다.

“그, 그럼 진무경 공자는요.”

“저야 모르죠.”

이 시간이면 자고 있지 않을까?

마부는 나라 잃은 표정으로 나를 바라보다가 바람 빠진 풍선 인형처럼 쓰러졌다. 졸도다.

‘시바. 고수는 무슨.’

마부의 손목을 놔줬다.

닭 뼈처럼 가느다란 손목이다. 잡는 순간부터 뭔가 쎄하다 싶었다. 그렇게 허세를 부려 놓고 일반인이라니.

“으하, 으하하하!”

산적들이 자지러지게 웃었다. 나? 언제 식은땀이 났는지 벌써 등허리가 축축하다.

‘이거, 진짜 재수 없으면.’

죽음이란 단어는 차마 꺼내지 못하고 꿀꺽 삼켰다.

나는 긴장 어린 눈으로 산적들을 훑었다.

시발. 차라리 고블린 여섯 마리랑 싸우고 말지. 저런 덩치들을 내가 어떻게 이겨…… 어라?

“엥?”

뭐야, 기분 탓인가? 하지만 아무리 봐도 기분 탓이 아니다.

우람한 상반신, 두꺼운 팔다리. 그리고…… 짧다.

옆에 다섯 놈도 별반 다르지 않다. 천력부는 몸이라도 좋지, 이놈들은 아무리 봐도 ‘건장한’이라는 단어와는 오백 광년쯤 차이가 있다.

그러니까 산적들의 체격이 꼭…….

“고블린이네?”

고블린이여?

예상치 못한 상황에 잠시 멍해 있다가 갑자기 날아오는 도끼에 정신을 차렸다. 머릿수도 많은 새끼들이 선제공격까지 하다니.

“야, 야! 잠깐만 타임!”

그 순간 도끼가 그대로 10m 앞 땅에 처박혔다. 아니, 고꾸라졌다. 도끼를 날린 산적이 쑥스러운 듯이 뒤통수를 긁적였다.

“조금 더 위로 던졌어야 했나?”

……이거 어쩌면.

‘살 수 있겠는데?’

7년 동안 가장 많이 상대한 몬스터를 꼽자면 고블린이다.

그러다 보니 놈들에 관한 모든 것을 속속들이 알게 됐다. 견습 헌터 시절에 주력 무기로 창을 선택한 것도 그 이유였다. 공격 범위에서 엄청난 우위를 점할 수 있으니까.

마침 산적들이 딱 그 정도 체격이다. 내 눈에는 산적이 아니라 고블린 여섯 마리로 보인다. 천력부는 대장 고블린 정도?

‘나머지 다섯은 고블린보다 약할 수도 있고.’

고블린은 독침이라도 잘 쏘지. 방금 도끼 던지는 꼴을 보아하니 촉이 온다. 촉이 와.

나는 바짝 마른 입술을 핥은 다음 두 손을 번쩍 들어 올렸다.

항복 의사에 몇 놈은 당황하고 천력부는 전역한 아들을 보는 아버지처럼 흐뭇하게 웃었다.

“기특한 놈일세.”

‘그래, 많이 웃어 둬라.’

한 발, 두 발. 천천히 30m에 이르는 거리를 좁혀 나간다.

일정한 보폭과 균형 잡힌 자세로. 한 발에 한 호흡. 입에서 김이 새벽 공기를 뚫고 새어 나왔다.

단순히 발을 내딛는 것만으로도 느껴진다.

‘다르다!’

다시 한번 깨달았다.

이 게임에서의 나는, 현실의 나보다 강하다.

가슴이 뛴다. 동시에 경각심이 고개를 쳐들었다.

마지막 순간까지 집중해야 한다.

“태원진가에 내놓은 자식이 있다는 풍문을 들었지. 무공은 삼류, 계집질은 일류라고. 오늘 보니 눈치도 제법이야.”

천력부가 말했다. 도끼를 쥔 손은 느슨하게 늘어트린 채다.

놈들의 눈에 내가 어떻게 보일지 뻔했다.

무공은 형편없는, 가문만 좋은 한량. 텅 빈 두 손.

천력부는 지금 방심했다.

‘그리고 방심은 죽음이지.’

가족들에게 월급 대부분을 보내고 고시원 단칸방에서 궁상맞게 살지만 나도 헌터다.

F급 헌터도 게이트에서는 목숨을 걸고 싸운다. 아니, 고작 F급이라 목숨을 걸고 싸워야 한다.

7년을 하루도 빠짐없이 싸워 온 승부사이자, 헌터라는 이름의 무림인이었다.

그래서 안다.

생사는 한 끗 차이라는 것을. 방심은 곧 죽음이라는 사실을.

남은 거리가 절반으로 좁혀졌다. 서서히 발걸음이 빨라진다.

천력부가 나를 향해 손짓한다.

“어허. 천천히 오게, 천천히. 오다가 넘어지기라도 하면 몸값 떨어져.”

20m.

“두목. 쫄래쫄래 걸어오는 꼴이 꼭 강아지 같지 않습니까?”

15m.

“강아지? 으허허! 네 말이 딱 맞다!”

10m.

다음 발을 내딛는 바로 그 순간, 뱃속이 뜨겁게 끓어올랐다.

난생처음 느껴 보는 생소한 감각. 그러나 묘하게 익숙한 이 느낌은 도대체 뭘까?

‘설마. 공력?’

단전에서 흘러나온 열기는 하반신을 향해 질주했다.

그 목적은 오로지 하나다. 좀 더 빠르게, 가볍게, 강하게!

훅. 길게 숨을 들이마신다. 온몸의 근육이 활시위처럼 팽팽하게 당겨졌다. 그리고 마지막, 한 걸음.

쾅!

정면을 향해 쏘아졌다. 지면이 움푹 패고 소리가 그 뒤를 잇는다. 정지된 시간 속, 천력부의 입이 천천히 벌어졌다.

“말도 안…….”

천력부도, 그 부하들도 믿을 수 없다는 표정이다.

놈들의 모든 것이 지금의 내게는 보였다. 느껴졌다.

빳빳하고 기름진 머리카락, 가뭄철 논바닥처럼 갈라진 입술과 보기만 해도 악취를 풍기는 이빨…….

그 모든 것들이.

나도 모르게 입꼬리가 올라갔다.

‘인벤토리 오픈. [예리한 창] 장착.’

허공을 향해 뻗은 손아귀에 서늘한 창자루가 잡혔다.

그대로 힘껏 내지른다. 엉겁결에 들어 올린 도끼가 창날을 막아 냈지만 예리한 창날은 도끼날을 그대로 부숴 버리고 천력부의 가슴을 관통했다.

동시에.



- 치명적인 일격! 상태 이상 [출혈]이 발동됩니다!



“커헉.”

피 분수가 터져 나왔다. 한차례 파르르 떨리던 천력부의 눈동자에서 빛이 사그라졌다.



- [Lv.10 장삼]을 처치했습니다.

- 레벨 업!

- 레벨 업의 보상으로 스탯 포인트 10을 획득했습니다.

- 레벨 업의 보상으로 스킬 포인트 10을 획득했습니다.

- [진가심법]의 잠금이 해제됩니다.



후우.

길게 숨을 내뱉었다. 알림이 울렸지만, 오롯이 심장 뛰는 소리만 내 안을 가득 채웠다.

한 호흡. 이 모든 일이 한 호흡 만에 벌어진 일이었다. 나는 숨이 끊긴 천력부의 가슴에서 창을 뽑아냈다.

‘이런 게 가능하단 말이지.’

포인트로 능력치를 올리고, 공력으로 강화하며 스킬로 연계한다. 이게 바로 나만이 가지고 있는 시스템의 힘이었다.

F급 헌터 진태경은 꿈꿀 수 없었던 힘.

‘할 수 있다. 반드시.’

돌아갈 길이 점점 밝고 넓게 보이기 시작한다.

나는 창 자루를 움켜쥐고 돌아섰다.

“그래서…….”

내게 못 박혀 있던 다섯 쌍의 시선이 위태롭게 흔들린다.

“더 덤빌 사람?”

아까 도끼 던진 새끼부터 나와.

“…….”

털썩. 털썩. 챙그랑.

눈치를 보던 다섯 놈이 무기를 버리고 넙죽 엎드렸다.

“용서해 주십시오. 대협!”



- 우두머리를 잃은 적들이 전의를 상실하고 항복합니다.

- [산적 퇴치]를 완료했습니다.

- 모든 피로와 부상이 회복됩니다.

- 산적을 토벌했습니다. 명성이 10 상승합니다.

- [튜토리얼 - 3단계]를 완료했습니다. 보상이 지급됩니다.

- 연계 퀘스트, [튜토리얼 - 4단계]가 생성되었습니다.



이제 숨 좀 돌리자.
```

## Current accepted English baseline

```markdown
# Chapter 4

Jang Sam was a bandit.

A local born and raised near Mount Wutai, he had never once left the area. Since around the age of twenty, he had made a living extorting tolls from travelers who looked easy to bully.

Perhaps thanks to his diligent round-the-clock operation, Jang Sam the Heavenly Axe had eventually become fairly well known.

Today was no different. He had risen before dawn and set out to work with his five loyal underlings, the Five-Colored Ghosts… but for some reason, his feet refused to stop.

How long had he walked, leaving his home turf of Mount Wutai far behind? At last, when his feet finally stopped, he saw a carriage approaching in the distance.

*How did I get all the way here?*

Had a ghost possessed him? Jang Sam was bewildered, but the moment he saw the luxurious four-horse carriage, his professional instincts came roaring back to life.

*I have to take that.*

When Jang Sam and the Five-Colored Ghosts blocked the road, the coachman pulled on the reins.

Four fine steeds, their coats gleaming, snorted clouds of vapor as they came to a halt. At a glance, each one looked worth a thousand nyang at least.

*Today’s my lucky day.*

Jang Sam smiled contentedly and adjusted his grip on his axe. Now, tighten the muscles in the dantian. One, two—

“Hand over your money!”

* * *

*What was that voice? Is he an opera singer?*

But it would take more than that to make me blink. I’d spent seven years as a Hunter and been through every kind of hell imaginable—even aerial combat.

…Still, he was kind of scary.

“There are six of them in total. I don’t see any signs of an ambush.”

The coachman reported the situation in a voice as calm as a secret agent’s.

*Does this guy have some kind of hidden ace? Why is he so relaxed?*

When I stared at him, he scratched his head.

“It happens from time to time. Though this is a first in this area.”

“Why?”

“Why? Unless it’s a sizable mountain stronghold, attacking a martial family is practically suicide. I wonder what kind of reckless fools would try robbing people in the Jin Family of Taiyuan’s own backyard.”

*Who else? Tutorial NPCs.*

Judging by the way he kept calling it the Jin Family’s backyard, we must have been fairly close.

*Should I stall for time?*

My current realm was second-rate.

The way my body felt after distributing my stats was beyond what I’d experienced as an F-rank Hunter, but I had no idea whether it was enough to hold its own in Murim.

Six against one. Six against two, if I counted the coachman.

*Could I do it?*

There was a reason people said numbers could overcome skill. The moment my hands and feet were tied, I’d be finished.

“How much farther to our destination?”

“We’re nearly there. Another hour should be enough.”

*Another hour…?*

I’d suspected it, but apparently, the coachman and I had very different definitions of *nearby*.

*What do you mean, nearly there?*

Maybe it was because this was a continent-sized setting. The scale was different. The scale.

Either way, I had to assume no reinforcements were coming. At least I wasn’t alone.

The coachman’s unflappable attitude practically screamed that he was a master.

“Shall I handle this?”

As he said it, he coiled the whip in his hand with enough force to suggest that one crack would separate the bandits’ bones from their flesh.

*He’s a master!*

Of course. I was a scion of a prestigious martial family and a VIP customer of Honghwaru. There was no way they would have sent an ordinary coachman with me.

*Wolhwa must have arranged this. She isn’t just beautiful—she’s kind, too.*

My anxiety vanished, replaced by a pleased smile. The coachman must have taken it as my permission, because the moment he turned away, a second shout rang out.

“You bastards! Can’t you hear what the Heavenly Axe is saying?”

I leaned out past the carriage window and saw a hairy man shouting while holding an enormous double-bladed axe. His upper body was massive, and his arms and legs were as thick as pillars.

But the coachman muttered as if the sight were laughable.

“Where do these little pups get off blocking our way?”

*Damn, that aura.*

Then the coachman laid into them.

“How dare bandits who suck the blood from innocent civilians block the road before us! I will have you dragged to the authorities and subjected to the full severity of the law!”

It was a speech worthy of Judge Bao, but the hairy man—the Heavenly Axe—and his underlings didn’t seem particularly moved.

“Yeah, we blocked the road. What are you going to do about it?”

“I will gouge out your eyes, grind your limbs to powder in a mortar, and scatter them across the Nine Provinces! I will also exterminate all nine degrees of your kin—”

*…Those punishments are getting a little extreme. That’s practically treason.*

As if he had read my thoughts, the Heavenly Axe spoke up.

“Hey, is there an imperial prince riding inside? Listening to you is making my knees shake. Why don’t you show us that precious face of yours?”

“You will regret not retreating now once you learn this man’s identity!”

“Okay, okay. We get it. Now come out already.”

“You fools…!”

The coachman clicked his tongue and turned toward me. My heart began to race. Was I finally about to see a true Murim master in action?

“Young Master, I believe you’ll have to come out.”

“Huh?”

*Me? Why me?*

“They won’t shed tears until they see the coffin. Blocking your path so brazenly—they’ll pay dearly for failing to recognize a master.”

With a determined look, he opened the carriage door for me.

“I have heard much of the Heaven Shaking Sword’s fame. A genius swordsman who reached the Peak realm at barely twenty! You cannot imagine how my old heart trembled whenever I heard stories about you, Young Master.”

*…The Heaven Shaking Sword? A genius swordsman?*

My thoughts tangled together. Who was the Heaven Shaking Sword? Who was this genius swordsman who had reached the Peak realm? And what the hell was this coachman playing at?

*You said you’d handle it. Aren’t you a master?*

“You bastards! Do you know who this man is?”

This was bad. The coachman was careening out of control like an eight-ton truck with a broken steering wheel.

*No. Stop. Please stop!*

I grabbed his wrist tightly, and he turned to look at me.

He smiled as if he knew everything. His eyes shone with boundless trust.

“W-wait. I’m Jin—”

Before I could say another word, his thunderous voice rang out.

“He is the Second Young Master of the Jin Family of Taiyuan, the Peak master whose name resounds throughout Shanxi! The Heaven Shaking Sword, Young Master Jin Mukyung!”

“I’m Jin…Taekyung.”

At that moment, a cold wind blew.

“Pardon?”

“I mean, I’m Jin Taekyung, not Jin Mukyung. And I’m the Third Young Master, not the Second…”

“…The Third Young Master? That Third Young Master?”

*Yes, you idiot.*

The coachman’s pupils began to tremble. It was an earthquake measuring 8.0 on the Richter scale.

“Th-then where is Young Master Jin Mukyung?”

“How should I know?”

*He’s probably sleeping right now.*

The coachman stared at me with the expression of a man who had lost his country, then collapsed like an inflatable toy with the air let out of it.

He had fainted.

*Fuck. Some master.*

I released his wrist.

His wrist was as thin as a chicken bone. Something had felt off from the moment I grabbed it. He had put on quite a show, only to turn out to be an ordinary civilian.

“Ha-ha! Ha-ha-ha!”

The bandits shrieked with laughter. My back was already damp with cold sweat, and I hadn’t even noticed when it started.

*If things go really badly…*

I couldn’t bring myself to say the word *death*. I swallowed it instead.

I swept my tense gaze over the bandits.

*Fuck. I’d rather fight six goblins than deal with this. How am I supposed to beat bodies that huge…?*

Wait.

“Huh?”

Was it my imagination? No matter how I looked at them, it wasn’t.

Massive upper bodies. Thick arms and legs. And…short.

The other five weren’t much different. The Heavenly Axe at least had a decent physique, but these guys were five hundred light-years away from anything you could call “well-built.”

In other words, the bandits’ physiques looked a lot like—

“They’re goblins?”

*Goblins?*

I stood there dazed for a moment, but a flying axe snapped me back to reality. They had the numbers and they were launching a preemptive attack, too?

“Hey, hey! Wait a second!”

The axe slammed into the ground ten meters ahead of me. No—it toppled over. The bandit who had thrown it scratched the back of his head sheepishly.

“Should I have thrown it a little higher?”

*…Maybe.*

*Could I actually survive this?*

The monster I had fought more than any other over the past seven years was the goblin.

Naturally, I knew everything there was to know about them. It was even why I had chosen a spear as my primary weapon when I was a novice Hunter. A spear gave me an enormous advantage in attack range.

And these bandits were exactly that size. To me, they didn’t look like bandits at all. They looked like six goblins. The Heavenly Axe was the goblin chieftain.

*The other five might be even weaker than goblins.*

At least goblins could shoot poison darts. Judging by the way this one had thrown that axe, I had a hunch. A very strong hunch.

I licked my dry lips, then raised both hands high.

A few of them looked confused at my gesture of surrender, while the Heavenly Axe smiled proudly, like a father looking at a son freshly discharged from the military.

“Good lad.”

*Yeah. Enjoy your laugh while it lasts.*

One step, two. I slowly closed the thirty-meter distance between us.

With a steady stride and balanced posture. One breath per step. My breath escaped my mouth in white clouds that pierced the dawn air.

I could feel it from the simple act of putting one foot in front of the other.

*It’s different!*

I realized it once more.

The version of me inside this game was stronger than the real me.

My heart pounded. At the same time, a warning stirred in the back of my mind.

I had to stay focused until the very last moment.

“I heard the Jin Family had a son they’d given up on. third-rate at martial arts, first-rate with women. Looks like you’ve got decent instincts, too.”

The Heavenly Axe spoke with the hand holding his axe hanging loose at his side.

I knew exactly how I looked to them.

A useless playboy with a good family name. Empty hands.

The Heavenly Axe had let his guard down.

*And letting your guard down gets you killed.*

I might send most of my salary to my family and live miserably in a tiny goshiwon room, but I was still a Hunter.

Even an F-rank Hunter risked his life fighting inside Gates. No—an F-rank Hunter had to risk his life precisely because he was only F-rank.

I was a fighter who had battled every day for seven years without missing one, a martial artist in all but name.

So I knew.

Life and death were separated by a hair’s breadth. Letting your guard down was the same as dying.

The distance had been cut in half. My steps gradually quickened.

The Heavenly Axe beckoned me over.

“Now, now. Take your time. Don’t lower your price by tripping on the way.”

Twenty meters.

“Boss, doesn’t the way he’s toddling over look just like a puppy?”

Fifteen meters.

“A puppy? Ha-ha-ha! You’ve got that exactly right!”

Ten meters.

The moment I took my next step, something hot began to churn in my stomach.

It was a sensation I had never experienced before, yet somehow, it felt strangely familiar. What was it?

*Could it be…internal energy?*

The heat flowing from my dantian raced toward my lower body.

It had only one purpose: to make me faster, lighter, stronger!

Whoosh. I drew in a long breath. Every muscle in my body drew taut like a bowstring. Then came the final step.

Boom!

I shot straight forward. The ground sank beneath my foot, and the sound followed after me. In frozen time, the Heavenly Axe’s mouth slowly fell open.

“No way…”

The Heavenly Axe and his underlings stared at me in disbelief.

I could see everything about them now. Feel it.

Their stiff, greasy hair. Their cracked lips, like a rice paddy in a drought. Their teeth that reeked just from looking at them…

I could see all of it.

The corners of my mouth lifted before I knew it.

*Open Inventory. Equip [Sharp Spear].*

A cold spear shaft appeared in the hand I had thrust into empty air.

I drove it forward with all my strength. The Heavenly Axe hastily raised his axe to block, but the sharp spearhead shattered the axe blade and punched straight through his chest.

At the same time—

> **System**
>
> Critical One Strike! Status effect Bleeding activated!

“Ghk!”

A fountain of blood erupted. The Heavenly Axe’s eyes flickered once, then went dark.

> **System**
>
> Lv. 10 Jang Sam defeated.
>
> Level up!
>
> You received 10 Stat Points as a level-up reward.
>
> You received 10 Skill Points as a level-up reward.
>
> Jin Family’s Cultivation Technique unlocked.

*Whew.*

I let out a long breath. A notification had sounded, but all I could hear was my own pounding heart.

One breath. Everything had happened in a single breath. I pulled the spear from the Heavenly Axe’s lifeless chest.

*So this is possible.*

Raise my abilities with points, reinforce them with internal energy, and chain them together with skills. This was the power of the System—the one power that belonged to me alone.

A power F-rank Hunter Jin Taekyung could never have dreamed of.

*I can do this. I will.*

The road home suddenly looked brighter and wider.

I gripped the spear shaft and turned around.

“So…”

The five pairs of eyes fixed on me wavered uncertainly.

“Who else wants to try me?”

*Start with the bastard who threw that axe.*

“…”

Thud. Thud. Clatter.

The five bandits exchanged glances, then dropped their weapons and prostrated themselves.

“Please forgive us, Great Hero!”

> **System**
>
> The enemies have lost their will to fight and surrendered after losing their leader.
>
> Defeat the Bandits complete.
>
> You have fully recovered from all fatigue and injuries.
>
> You have subdued the bandits. Fame increased by 10.
>
> Tutorial—Stage 3 complete. Rewards will be distributed.
>
> Chain Quest Tutorial—Stage 4 created.

*Now I can finally catch my breath.*
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 4`.
