# Master Edit Task — Chapter 3

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
| 월화     | **Wolhwa**         |
| 태원진가   | **Jin Family of Taiyuan**        |
| 삼류     | **Third Rate**    |
| 이류     | **Second Rate**   |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 내공     | **internal energy**                              |                                                       |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 창법     | **spear technique**                              |                                                       |
| 구결     | **formula**                                      | Mnemonic/oral formula for a martial art               |
| 영약     | **elixir**                                       |                                                       |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 진가보법   | **Jin Family's Manoeuvre Technique**   |
| 진가창법   | **Jin Family's Spear Technique**       |
| 시스템              | **System**                     |
| 상태창              | **Status Window**              |
| 상태               | **Status**                     |
| 스킬               | **Skill**                      |
| 스킬창              | **Skill Window**               |
| 레벨               | **Level**                      |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 아이템              | **Item**                       |
| 로그아웃             | **Logout**                     |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 매력               | **Charm**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 마정석     | **Magic Gem**         |
| 태원     | **Taiyuan**            |
| 공자      | **Young Master**                                                |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

(No prior chapter summary available.)

### Prior accepted reading-copy tails

#### Chapter 1 tail (verified mastered)

…
curiosity made me examine the capsule more closely. “First, the exterior is… not great.” The surface was stained yellow with nicotine or something, and there seemed to be rust in places. Once I let go of my lingering hopes and took a proper look, I could see why Jinho had called it garbage. “Is this how you open it?” I pressed the single protruding button. The lid opened, revealing the interior. I’d been expecting something impressive, but there wasn’t much to see. Just an ergonomically designed chair for extended play and a VR helmet that enclosed the entire head… Huh? “What’s this? An instruction manual?” More precisely, it was a small booklet labeled *Product User Manual*. Did people really leave instruction manuals inside things they were throwing away? Especially junk like this? Curious, I opened it to the first page. > **Product User Manual** > > **Product name:** Virtual Reality Interface > **Model:** Ark-2020 > **Manufacturer:** H Soft > **Manufacturing date:** January 1, 2020 I skimmed the text without much thought until my eyes stopped on the manufacturing date. January 1, 2020. It had to be a printing error. Surely. *What kind of lunatic would have been making a game machine on that day—no, during that whole period?* That period was the Great Cataclysm. On January 1, 2015, humanity received more than a New Year’s sunrise. Gates—or dungeons, as they were also called—appeared all over the world, and monsters no one had ever seen or heard of poured through them. Monsters and the Awakened. War and destruction… The unreal invaded reality, and the greatest war in Earth’s history ended only with the death of the monsters’ lord, the Demon King Asmodeus. That day was January 1, 2020—the so-called Victory Day. *So this is impossible.* I clicked my tongue and turned the page. > **Warning** > > - The player cannot log out at will. > - If the player dies during gameplay, resurrection is impossible. “Oh. I see.” I nodded and lay down on the narrow mattress. There were still a few pages left, but who cared? “I should get some sleep.” Sleeping was better than reading an instruction manual written by a lunatic. I shoved Jinho into a corner and closed my eyes. “Gwaah. Gwaah.” “…” “Gwaah. Gwaah.” “…” Did that capsule have a soundproofing function? * * * The chair was hard. It had been made in 2020, which made it the same age as me. A chair in the bloom of youth at twenty-seven. Its cushion had gone flat long ago. I took comfort in the fact that it didn’t smell and pulled the blanket up to my neck. “Gwaah. Gwaah.” …I even put on the VR helmet. *Sleeping in this thing is going to make my neck hurt.* That minor complaint vanished the moment I put on the helmet. Complete silence. A stillness without so much as a whisper of noise. But instead of sleep, thoughts came flooding in. *What am I going to do tomorrow?* Hunters were certainly well paid, but that depended on their rank. F-rank Hunters like me were a dime a dozen, and unless you belonged to a Guild, you had to report to a day-labor agency before the crack of dawn. Being an unaffiliated Hunter was miserable. Government policy was never kind to unaffiliated Hunters, and the crushing tax rates imposed on Hunters were enough to leave you short of breath just hearing about them. *And now I’m one of them.* Unlike me, my mother and younger sister lived in an apartment in a Safety Sector. It was an extravagant expense on an F-rank Hunter’s income, but nothing mattered more to me than my family’s safety. Until now, I’d barely managed to scrape together enough money each year to renew their jeonse lease.[^3] But from now on… who knew? *Fuck. I don’t know.* My late father suddenly came to mind. He had devoted himself to his family and earned the respect of those around him, but he died when I was seven. Monsters had attacked after a Gate breach. As an ordinary office worker, he probably hadn’t stood a chance. If my father were still by my side, could he have shown his son which way to go? *I’ve done my best all this time. Please believe me.* Maybe the alcohol was finally catching up with me, or maybe it was the memories. Either way, my body went slack, and my eyes began to close. As I surrendered to the wave of drowsiness, I thought: *I hope things will be a little better when I open my eyes.* Someone’s voice reached my ears, but I no longer cared. I slipped gently into sleep. > **System** > > Player detected. …Unregistered player. Register as a new player? > > No response for an extended period. Proceeding automatically. > > 1%… 27%… 94%… Complete. > > Player Jin Taekyung registered to the device. > > Proceeding to selection. Would you like to log in to Murim? > > No response for an extended period. Proceeding automatically. > > …May fortune favor you in battle! [^1]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement, often with shared facilities. [^2]: Doenjang is a fermented Korean soybean paste commonly used as the base of a savory stew. [^3]: A Korean jeonse lease is secured by a large refundable deposit in place of monthly rent.

#### Chapter 2 tail (verified mastered)

…
acquired. Check it later through the Status Window. *A title? Scion of a Prestigious Family?* I guessed it was something like a title in a fantasy game. *Dragon Slayer, or something like that.* You received one after accomplishing a certain feat, and equipping it granted additional effects. In that respect, I had to say I was pretty lucky. *This guy really was born with a silver spoon in his mouth.* Being born into a prestigious family counted as an achievement. It pissed me off and made me happy at the same time. That meant the random character selected against my will had turned out to be a lottery winner. But the story didn’t end there. “I’ve heard there are problems inside and outside the family these days.” “Problems? What kind of problems?” Come to think of it, the quest window’s information-gathering mission was still marked *Incomplete*. That meant there was more information to collect. “Externally, there’s the conflict with the Mount Heng Sword Sect, which is constantly eyeing the position of Shanxi’s hegemon. Internally…” Wolhwa leisurely tapped the ash from her pipe. “I hear that family’s third son is a notorious good-for-nothing.” “Ah. There’s always one of those wherever you go.” I nodded unconsciously, then an uneasy feeling came over me. “Excuse me.” “Yes?” “I’m only asking as a joke, but how many sons does the Jin Family of Taiyuan have?” She answered with a sunny smile. “Three.” The Jin Family of Taiyuan had three sons, and I was the youngest of them. But the third son was a notorious good-for-nothing. Which meant— *Fuck. That’s me, isn’t it?* Ding. > **System** > > Title Shame of the Family acquired. Check it later through the Status Window. > > Gather Information complete. I couldn’t decide whether to laugh or cry. Then I saw Wolhwa snickering and let out a hollow laugh myself. *Well, better to look on the bright side. So what if I’m the shame of the family? It’s only a game, anyway.* I opened the quest window and confirmed that *Gather Information* had changed to *Complete*. *The problem is understanding the situation.* This damn quest was so vague that I had no idea what exactly it wanted. In the end, was Wolhwa my only solution? “Where are we?” “Honghwaru, the finest pleasure house in Shanxi. This is my room.” Through our conversation, I learned a few more miscellaneous facts. We were in Honghwaru, located in the heart of Taiyuan. Wolhwa was a fairly high-ranking courtesan, and I had spent the night with her… Ahem. Despite all the things we discussed, no System notification appeared. Eventually, I ran out of questions to ask. At the very end, I was reduced to asking this: “What’s my situation right now?” Wolhwa sighed. “Young Master Jin, I’m sorry to say this, but you seem a little crazy right now. How about getting some rest?” *Yeah. I feel like I’m going crazy, too.* As sunlight streamed through the window, I began to wonder what on earth I was doing. *This isn’t some kind of mystery game.* The graphics and artificial intelligence were all great, but getting stuck on the tutorial had completely drained the fun out of it. If there was one thing I’d learned, it was that the capsule I’d found yesterday was a much better piece of equipment than it looked. A game this advanced had to require serious hardware, yet I hadn’t experienced a single bit of lag. It should sell for a decent price on the used market. *I need to start looking for a new job today, too.* Still, the game hadn’t been bad for the little while I’d played it. I gave Wolhwa a final nod and shouted: “Log out!” > **System** > > Logout is impossible. *Huh?* “Log out.” > **System** > > Logout is impossible. *What’s going on?* An error? Or had the ancient capsule finally started lagging? “…Log out?” > **System** > > Logout is impossible. There was no doubt about it. Error or lag, the damn old capsule had finally caused trouble. I tried ten more times after that, but every attempt failed. By this point, my anger had gradually turned into worry and regret. *Is something bad going to happen to me?* *I shouldn’t have picked it up just because it was free. I should have thrown it away the moment Jinho called it garbage. Or at least the moment I read that insane instruction manual…* *No. Wait.* The instruction manual. That was right—I’d read it. More precisely, I’d read a few of the warnings before tossing it aside, but I had read them. *What did they say?* The moment I finally remembered every warning I’d managed to read, a chill ran through my entire body. > **Warning** > > - The player cannot log out at will. > - If the player dies during gameplay, resurrection is impossible. *I’m trapped inside the game? Me?* The System notification answered my question for me. Ding. > **System** > > Understand the Situation complete. > > Tutorial—Stage 1 complete. Rewards will be distributed. > > Status Window activated. > > Skill Window activated. > > Inventory activated. > > Chain Quest Tutorial—Stage 2 created. At that moment, a single thought filled my head. *I’m fucked.* [^1]: A room salon is a Korean private-room entertainment venue where customers are served food, alcohol, and conversation by hostesses.

## Korean source

```text
＃3화



잔잔한 수면 위로 한 청년이 비친다.

짙은 눈썹, 뚜렷한 이목구비. 입꼬리를 올리자 움푹 팬 보조개가 드러난다. 하지만 꾸며 낸 웃음은 다음 순간 씻은 듯이 사라졌다.

쨍그랑.

세숫물이 담긴 접시를 내던지자 파편이 사방으로 튀었다.

“시발, 시바알!”

잘생기면 뭐 해. 로그아웃이 안 되는데.

지난 사흘간 온갖 지랄 발광을 떨었지만 돌아오는 대답은 똑같았다.

- 로그아웃이 불가능합니다.

‘이런 걸 만들 생각을 하다니. 미친놈들.’

쉬지 않고 욕설을 퍼부으며 주의 사항을 떠올렸다.



- 플레이어 임의로 로그아웃할 수 없습니다.

- 플레이 도중 사망 시, 부활할 수 없습니다.



요약하자면 간단하다.

나는 [무림]이라는 무협 장르 게임을 하는 중인데, 마음대로 로그아웃할 수 없고 캐릭터가 죽으면 나도 죽는단다.

허허허.

‘이게 무슨 개소리야.’

그러나 실제로 벌어지고 있는 일이다.

로그아웃은 되지 않았고, 밖에서 구조해 주기를 기다리며 사흘을 버텼지만 아무 일도 없다. 죽음에 관해서는 확인해 보지 못했지만…… 정황상 사실일 확률이 높다.

‘하지만 방법은 있다.’

플레이어 임의로 로그아웃할 수 없다는 말은 어떤 조건을 충족하면 로그아웃이 가능해진다는 말과 같다.

‘이를테면, 퀘스트나 레벨 업.’

이곳, [무림]이 게임이기 때문에 유추해 낸 답이다.

게임에서는 퀘스트를 깨고 레벨을 올릴 때마다 보상이 주어진다. 앞서 튜토리얼 1단계를 완료함으로써 증명된 사실이다.

‘우선 퀘스트와 레벨 업에 초점을 맞춘다.’

사흘간의 고민 끝에 내린 결론이다. 그리고 거기에는 필수 요건이 존재했다. 바로 생존.

생명이 위협받지 않을 만한 장소에서 활동해야 한다. 누군가의 도움까지 얻을 수 있다면 더할 나위 없이 좋고.

‘마침 딱 알맞은 곳이 하나 있지.’

그때 문밖에서 월화의 목소리가 흘러 들어왔다.

“진 공자, 마차 준비됐어요.”

F급 헌터 진태경이 아닌, 태원진가의 진태경을 집으로 데려다줄 마차다.



* * *



월화, 아니 홍화루에서 내준 사두마차는 크고 화려했다.

마부는 과묵한 사람이어서 말 한마디 건네는 법이 없었고, 내 입장에서도 그게 편했다.

지금은 누구에게도 방해받고 싶지 않았으니까.

‘퀘스트 확인.’



[튜토리얼 - 2단계]를 시작하시겠습니까?

수락    /    거부



사흘간 수십 번도 넘게 열고, 끝내 닫았던 퀘스트창이다. 미지에 대한 두려움 때문이었다. 하지만 이제 망설이지 않는다.

수락.

띠링.



퀘스트



[튜토리얼 - 2단계]

앞서 당신은 기본적인 정보와 상황을 숙지했습니다.

그러나 무림은 예측할 수 없는 곳. 지금부터 당신만이 가진 유일한 힘인 ‘시스템’을 활용하십시오.



등급 : 튜토리얼 (연계 퀘스트)

제한 : 최초 접속자

임무 : 상태창 확인 및 분배 (미완료)

         스킬창 확인 및 분배 (미완료)

        인벤토리 확인 및 장착 (미완료)

보상 : 예리한 창

       연계 퀘스트





……이런 거였으면 진작 끝냈지. 어쩌면 당연한 수순이다.

아무리 비정상적이어도 결국 본질은 게임이라 이건가.

나는 과거 가뭄에 콩 나듯 했던 온라인 게임을 떠올리며 생각했다.

‘상태창 확인.’



상태창



LV.10 진태경

직업 : 삼류 무인

명성 : 0

칭호 : 명가의 자제 / 가문의 수치 (칭호 효과 적용 중)

근력 : 10체력 : 10

민첩 : 10 지력 : 10

매력 : 10 공력 : 10년

잔여 포인트 : 100

- 잔여 포인트를 분배하십시오.

- 명가의 자제 (모든 능력치 +5, 명성 +50)

- 가문의 수치 (모든 능력치 -5, 명성 -50)





‘뭐야, 이게.’

눈을 깜빡였다. 뒤통수를 얻어맞은 기분이다.

근방에서 방귀깨나 뀐다는 태원진가. 그것도 무림세가 출신인 놈이…… 고작 레벨 10에 삼류 무인?

‘실화냐.’

특이 사항을 읽을 때는 뒷목이 다 뻐근했다.

[명가의 자제] 칭호 효과를 [가문의 수치]가 완벽하게 틀어막고 있었다.

‘기대했던 내가 바보지.’

좋은 집안에서 태어나 무공 수련은 뒷전, 여자와 술에 빠져서 허우적거리는 돈 많은 한량. 괜히 가문의 수치가 아니다.

‘엿 됐다.’

하지만 낙장불입이다. 침 한번 뱉고 넘겨야 한다.

그나마 다행인 점은 모든 능력치가 초기화되었다는 부분이다. 원하는 능력치를 올릴 수 있는 건 엄청난 장점이니까.

나는 매의 눈으로 상태창을 훑었다.

‘이건 단순한 게임이 아니다. 생각하자, 생각, 생각…….’

이 공간을 단순한 게임으로 받아들여선 안 된다.

이건 목숨이 걸린 문제다. 학창 시절 했던 RPG게임처럼 힘에 몰빵, 민첩에 몰빵. 이런 거 했다가는 바로 골로 가는 거다.

그때 쉴 새 없이 굴러가던 눈동자가 멈칫했다.

‘공력에 투자할까?’

공력, 혹은 내공.

현실에서 상위 헌터들이 사용하는 마나, 오러 같은 기(氣)를 달리 부르는 말이다.

대부분의 무협 소설에서는 오늘내일하는 노인네가 젊고 팔팔한 무림 고수들을 씹고 뜯고 맛보고 즐기는데, 그럴 수 있었던 이유는 바로 엄청난 공력의 소유자기 때문이다.

무협 하면 공력. 고수 하면 내가고수. 오죽하면 고수의 척도를 가르는 것이 공력이라는 말까지 있을까.

‘우선은 신중하게…… 공력에 1포인트 부여.’

삑!



- [공력]은 수련과 영약 등의 아이템을 통해서만 증가시킬 수 있습니다.



그래. 그럴 줄 알았어. 이럴 줄 알고 기대 하나도 안 했어.

……망할 놈의 시스템.

‘그럼 공력은 제외.’

공력을 빼면 남은 능력치는 다섯 개다.

근력, 체력, 민첩, 지력, 매력.

나는 그중 지력과 매력을 제외하기로 마음먹었다.

‘도움이 안 돼.’

목표는 생존과 로그아웃이지, 수능, 연애가 아니다.

다행히 나는 7년 경력의 직업 헌터였고, 살아남기 위해 어떤 것들이 필요한지 아주 잘 알고 있다.

‘근력, 체력에 각각 30. 민첩은 40.’

고심 끝에 내린 결정이다. 적당한 힘과 뛰어난 회피. 그리고 체력. 7년 동안 익숙해진 전투 스타일이기도 했다.



- 이대로 적용하시겠습니까?



‘그래.’

그 순간이었다.

띠링.



- [이류 무인]으로 전직하셨습니다!



총 100포인트.

잔여 포인트의 숫자가 증발함과 동시에 나는 몸의 변화를 느꼈다. 머리부터 발끝까지, 그리고 내가 보지 못하는 몸속 깊은 곳까지. 시스템이 부여한 힘이 스며든다. 잇는다. 뭉치고 풀어낸다.

순간 태양을 삼킨 것처럼 열기가 몸을 휩쓸었고, 그 여운이 가신 후에야 간신히 눈을 뜰 수 있었다.

그리고 경악했다.

“이, 이거.”

나도 모르게 목소리가 떨렸다. 낯선 감각에 대한 놀라움이 아니다. 오래전 단 한 번 느꼈던, 그러나 결코 잊을 수 없는 감각이 이 순간 떠올랐기 때문이었다.

어떻게 잊을 수 있을까. 7년 전 그날을.

‘각성……!’

예고 없이 찾아온 감각에 스무 살의 나는 속수무책이었다.

그리고 다시 눈을 떴을 때, 내가 선택받았다는 사실을 깨달았다. 선택받은 0.1%. 각성자가 된 것이다.

그날에 느꼈던 환희가 지금의 나를 혼란스럽게 했다.

“이게 왜, 여기서?”

갈팡질팡하고 있는 나를 깨운 것은 시스템 알림이었다.

띠링.



- [상태창 확인 및 분배]를 완료했습니다.



어느새 바짝 마른 입술을 혀로 핥으며 생각했다.

그래, 우선 현재에 집중하자. 튜토리얼 2단계 완료까지 두 개밖에 남지 않았다.

‘스킬창 확인.’



스킬창



LV.10 진태경

심법 : 진가심법 (사용 불가)

무공 : 진가창법 / 진가보법 (사용 불가)

근골 : 10

근맥 : 10

잔여 포인트 : 100

- 잔여 포인트를 분배하십시오.

- 무공을 사용할 수 없습니다.

- 오랫동안 무공 수련을 하지 않아 구결을 잊은 상태입니다.





스킬창을 열어 보길 잘했다. 보는 순간 다른 잡념이 싹 사라지고 현자 타임이 찾아왔으니까.

‘하나, 둘, 셋.’

내가 숫자를 잘못 셌나? 아니면 글자가 너무 작아서 미처 보지 못했을 수도 있다. 눈을 부릅뜨고 스킬창을 응시했다.

하나, 둘, 셋…… 그리고 셋.

진가심법과 진가창법, 그리고 진가보법. 그것이 진태경이 가진, 내가 가진 스킬의 전부다. 심지어 다 까먹었단다.

‘돌겠네.’

만약 내가 죽는다면 사인은 화병이다. 화병.

어느 정도 마음을 가라앉히고서야 냉철하게 스킬창을 바라볼 수 있게 됐다.

그래. 무공이야 앞으로 많이 배우면 되지.

‘잔여 포인트가 있는 게 어디냐.’

애써 자위하며 다시 스킬창을 바라봤다. 워낙 텅텅 비어 있어서 그런지 몰라도 금방 눈에 띄는 단어가 있었다.

‘근맥과 근골. 이거 무협 소설에서 많이 봤는데.’

근맥은 힘줄과 핏줄, 근골은 근육과 뼈대를 의미한다.

그 말인즉슨 내공 위주면 근맥, 외공 위주면 근골이라는 결론이 나온다. 그중 근골에 조금 더 치중하기로 마음먹었다.

이유는 간단했다.

‘그나마 익숙한 걸 골라야 생존 확률이 올라간다.’

현실에서 나는 F급 헌터다. 무림으로 치자면 삼류 무사고, 어쩌면 그 이하일 수도 있다.

마법을 쓰고, 오라를 일으키고…… 눈으로 본 적은 있어도 내 능력으로는 언감생심. 꿈도 꿀 수 없었다.

‘고기도 먹어 본 놈이 잘 먹지.’

내공도 써 본 놈이 써 보는 거다. 지난 7년간 내가 해 왔던 전투 방식은 외공 수련자의 그것에 가깝다.

‘근골에 60. 근맥에 40.’



- 이대로 적용하시겠습니까?



‘그래, 적용.’

그 순간, 상태창 때와는 다른 쾌감이 나를 휩쓸었다. 어쩌면 고통일지도 모르겠다. 몸 깊은 곳에서 뼈가 뒤틀리는 소리가 들렸으니까.

‘큭.’

몇 초? 몇 분? 모르겠다. 고통이 지나간 자리에는 헐떡이는 숨소리와 인내에 대한 보상이 기다리고 있었다.

‘체격이…….’

달라졌다. 양쪽 어깨가 반 뼘은 벌어졌고 앞뒤로 근육이 단단하다. 조금은 넉넉했던 비단옷이 답답하게 느껴졌다.

주먹을 쥐자 아까까지만 해도 느낄 수 없었던 힘과 탄력이 느껴진다. 강해졌다. 현실에서는 느껴 보지 못했던 경험이다.

‘시스템이 없으니까.’

훈련을 통해 근력을, 체력을, 유연성을 기를 수는 있지만 측정 전까지는 어렴풋이 기분으로 느낄 뿐이다.

그러나 이곳, 무림은 다르다.

상태창을 통해 능력을 볼 수 있고 필요한 능력을 향상시킬 수 있다. 끝이 어딘지는 모르지만 계속해서 나아갈 수 있다.

‘더 강해진다. 그리고 살아남는다.’

지난 7년간 수많은 몬스터와 싸웠다. 상처 하나 없이 돌아온 날도, 죽을 고비를 넘긴 날도 있었다.

F급 헌터 진태경에게는 무림의 진태경에게 없는 것이 있다. 경험. 그리고 욕망.

더, 더, 더, 강해진다. 그리고 살아남는다.

그렇게 다짐하며 주먹을 불끈 쥐는 순간, 알림이 울렸다.

띠링.



- [스킬창 확인 및 재분배]를 완료했습니다.



이제 남은 건 하나다.

‘인벤토리 확인.’

띠링.



인벤토리



[단단한 무복 세트]

등급 : 삼류

제한 : 없음

효과 : 없음

설명 : 가볍고 질긴 천으로 만들어졌다. 초심자가 쓸 만하다.





기본 아이템인 만큼 설명도 심플하다.

‘아이템 착용.’

순간 전신이 시원해진다 싶더니 어느새 검은 무복을 걸친 나를 발견했다.

바뀐 건 상, 하의뿐만이 아니다. 무협 소설에서 흔히 영웅건이라고 불리는 두건이 이마에 단단히 묶여 있고 비단 신발 대신 가죽신을 신었다.

이제 그럭저럭 무사1 정도로는 보이려나?

‘아이템 보관.’

벗겨진 비단옷을 손에 쥐고 생각하자 순식간에 사라진다.

인벤토리. 이거 엄청 편리한데? 어떻게 쓰느냐에 따라 전투에 응용할 수도 있겠다.

‘인벤토리 하나 있으면 레이드 뛸 때 진짜 편할 텐데.’

이거 하나면 몬스터와 싸울 필요도 없이 뒤에서 마정석만 챙겨도 연봉으로 빌딩을 세우겠다.

‘근데 안 될 거야.’

게임이니까. 로그아웃하면 끝이니까.

……살아서 로그아웃할 수 있을지도 의문이지만.

띠링.



- [인벤토리 확인 및 장착]을 완료했습니다.

- [튜토리얼 - 2단계]를 완료했습니다. 보상이 지급됩니다.

- 연계 퀘스트, [튜토리얼 - 3단계]가 생성되었습니다.



새로운 보상!

나는 바로 인벤토리를 열어 새 아이템을 확인했다.



인벤토리



[예리한 창]

등급 : 이류

제한 : 없음

효과 : 명중 시 5% 확률로 [출혈] 발동

설명 : 그럭저럭 쓸 만한 창. 예리하니 손질 시 주의할 것.





“…….”

상태창이랑 스킬창이 개판이면 아이템이라도 좋은 거 줘야 하는 거 아닌가. 하긴 앞서 벌어진 일들을 생각하면 이 정도는 양반이다.

‘아이템 착용.’

손아귀에 창자루가 잡힌 순간이었다.

띠링.



- [튜토리얼 - 3단계]를 시작합니다. 준비하십시오.



“……어?”

준비? 뭘?

아직 퀘스트창 열어 보지도 않았는데?

대답은 엉뚱한 곳에서 들려왔다.

과묵한 마부가 처음으로 입을 연 것이다.

“공자님.”

“네?”

“사소한 문제가 생겼습니다.”

“갑자기 그게 무슨…….”

띠링.



퀘스트



[튜토리얼 - 3단계]

당신은 시스템을 통해 강해지는 방법을 깨달았습니다.

배움에는 결과가 있어야 하는 법.

갑작스럽게 출현한 산적들을 물리치십시오!



등급 : 튜토리얼 (연계 퀘스트)

제한 : 최초 접속자

임무 : 산적 퇴치 (미완료)

보상 : 모든 부상 회복

         연계 퀘스트

실패 : 사망





……사소한 문제는 개뿔이.
```

## Current accepted English baseline

```markdown
# Chapter 3

A young man’s reflection shimmered across the calm surface of the water.

Dark eyebrows. Sharp, well-defined features. When he lifted the corners of his mouth, deep dimples appeared. But the forced smile vanished as if washed away the very next moment.

Crash.

I threw the basin of wash water to the floor, sending shards flying in every direction.

“Fuck! Fuuuck!”

What good was being handsome if I couldn’t log out?

I’d spent the past three days throwing every kind of tantrum imaginable, but the answer never changed.

> **System**
>
> Logout is impossible.

*What kind of lunatics thought this was a good thing to make?*

As I continued hurling curses, I remembered the warnings.

> **System**
>
> The player cannot log out at will.
>
> If the player dies during gameplay, resurrection is impossible.

In short, it was simple.

I was playing a martial-arts genre game called *Murim*, but I couldn’t log out whenever I wanted—and if my character died, so would I.

Ha. Ha. Ha.

*What kind of bullshit is this?*

And yet, it was really happening.

I couldn’t log out. I’d spent three days waiting for someone outside to come rescue me, but nothing had happened. I hadn’t tested the death part, but judging by the circumstances, there was a good chance it was true too.

*But there is a way.*

If “the player cannot log out at will” was the wording, that implied logging out might become possible after meeting certain conditions.

*For example, completing a quest or leveling up.*

That was the answer I’d deduced because this place, *Murim*, was a game.

In games, you received rewards whenever you completed a quest or leveled up. The completion of Tutorial—Stage 1 had already proved that much.

*For now, I’ll focus on quests and leveling up.*

That was the conclusion I’d reached after three days of thinking. And it came with one essential requirement: survival.

I had to stay somewhere my life wouldn’t be in danger. If I could get someone’s help too, even better.

*As it happens, I know exactly the right place.*

Just then, Wolhwa’s voice drifted in from outside the door.

“Young Master Jin, the carriage is ready.”

It was a carriage to take Jin Taekyung of the Jin Family of Taiyuan home—not F-rank Hunter Jin Taekyung.

* * *

The four-horse carriage Wolhwa—or rather, Honghwaru—had provided was large and extravagant.

The coachman was a taciturn man who never tried to make conversation, and I found that perfectly convenient.

I didn’t want anyone bothering me right now.

*Check the quest.*

> **System**
>
> Would you like to begin Tutorial—Stage 2?
>
> Accept / Decline

This was the quest window I’d opened dozens of times over the past three days, only to close it again. I’d been afraid of the unknown. But I wasn’t hesitating anymore.

*Accept.*

Ding.

> **System**
>
> Quest
>
> Tutorial—Stage 2
>
> You have familiarized yourself with the basic information and situation.
>
> But Murim is an unpredictable place. From this point on, use your only unique power: the System.
>
> **Grade:** Tutorial (Chain Quest)
>
> **Restriction:** First-time player
>
> **Objective:** Check and distribute Status Window points (Incomplete)
>
> Check and distribute Skill Window points (Incomplete)
>
> Check and equip Inventory items (Incomplete)
>
> **Reward:** Sharp Spear
>
> Chain Quest

*If that was all it wanted, I could have finished it ages ago.* It was the obvious next step, really.

No matter how strange things were, this place was still a game at its core.

I thought back to the online games I’d played every once in a blue moon in the past.

*Check the Status Window.*

> **System**
>
> Status Window
>
> LV. 10 Jin Taekyung
>
> **Occupation:** Third Rate Martial Artist
>
> **Fame:** 0
>
> **Titles:** Scion of a Prestigious Family / Shame of the Family (Title effects active)
>
> **Strength:** 10 **Stamina:** 10
>
> **Agility:** 10 **Intelligence:** 10
>
> **Charm:** 10 **Internal Energy:** 10 years
>
> **Unassigned Points:** 100
>
> - Distribute your unassigned points.
> - Scion of a Prestigious Family (All stats +5, Fame +50)
> - Shame of the Family (All stats -5, Fame -50)

*What the hell is this?*

I blinked. I felt completely blindsided.

The Jin Family of Taiyuan was a big deal in the area. And this guy was even from a prestigious Murim family…but he was only Level 10, a third-rate martial artist?

*Is this for real?*

My neck grew stiff as I read the special notes.

The effect of the Scion of a Prestigious Family title was completely canceled out by Shame of the Family.

*I was an idiot for getting my hopes up.*

A rich wastrel born into a good family, neglecting martial arts training while drowning in women and alcohol. No wonder they called him the shame of the family.

*I’m screwed.*

But there were no take-backs. I’d just have to suck it up and move on.

The one silver lining was that all my stats had been reset. Being able to raise the stats I wanted was a huge advantage.

I scrutinized the Status Window.

*This isn’t just a game. Think. Think, think…*

I couldn’t treat this place as an ordinary game.

My life was on the line. If I dumped everything into Strength or Agility like I had in the RPGs I played as a student, I’d be dead in no time.

Then something caught my eye.

*Should I invest in Internal Energy?*

Internal energy, or inner power.

It was another name for the kind of qi—mana or aura—that high-ranking Hunters used in the real world.

In most martial-arts novels, old geezers with one foot in the grave could chew up vigorous young masters and toy with them however they pleased—all because they possessed enormous internal energy.

Martial arts meant internal energy. And when you thought of a master, you thought of a master of internal energy. There was a reason people called internal energy the yardstick of a martial artist’s strength.

*I’ll be cautious for now…one point into Internal Energy.*

Beep.

> **System**
>
> Internal Energy can only be increased through training and items such as elixirs.

Right. I knew that would happen. I hadn’t gotten my hopes up at all.

…Damn this System.

*Then Internal Energy is out.*

That left five stats.

Strength, Stamina, Agility, Intelligence, and Charm.

I decided to exclude Intelligence and Charm.

*They won’t help me.*

My goal was survival and logging out—not taking the college entrance exam or dating.

Fortunately, I was a professional Hunter with seven years of experience, and I knew exactly what was needed to stay alive.

*Thirty points each into Strength and Stamina. Forty into Agility.*

That gave me decent power and endurance, with Agility as my strongest stat. It was also the fighting style I’d grown accustomed to over seven years.

> **System**
>
> Apply these settings?

*Yes.*

That was when it happened.

Ding.

> **System**
>
> You have changed class to Second Rate Martial Artist!

One hundred points in total.

As the number of unassigned points vanished, I felt the System’s power seep through me from head to toe, reaching even the parts of my body I couldn’t see. It connected, gathered, and dispersed.

For an instant, heat swept through my body as if I’d swallowed the sun. Only after the lingering warmth faded could I finally open my eyes.

And then I was stunned.

“Th-this…”

My voice trembled despite myself. It wasn’t the shock of an unfamiliar sensation. It was a feeling I’d experienced only once long ago—but could never forget—coming rushing back to me.

How could I forget? That day, seven years ago.

*Awakening…!*

The sensation had come without warning, leaving my twenty-year-old self completely helpless.

When I opened my eyes again, I realized that I had been chosen. The chosen 0.1 percent. I had become an Awakened.

Remembering how happy I’d been that day only made me more confused.

“Why is this happening here?”

The System notification snapped me out of my turmoil.

Ding.

> **System**
>
> Check and Distribute Status Window Points complete.

I licked my lips, already dry, and thought.

*Right. Focus on the present for now. There are only two things left before Tutorial—Stage 2 is complete.*

*Check the Skill Window.*

> **System**
>
> Skill Window
>
> LV. 10 Jin Taekyung
>
> **Cultivation Technique:** Jin Family’s Cultivation Technique (Unavailable)
>
> **Martial Arts:** Jin Family’s Spear Technique / Jin Family’s Manoeuvre Technique (Unavailable)
>
> **Sinews:** 10
>
> **Bones:** 10
>
> **Unassigned Points:** 100
>
> - Distribute your unassigned points.
> - Martial arts cannot be used.
> - You have forgotten the formula because you have not trained in martial arts for a long time.

Opening the Skill Window had been a good idea. The moment I saw it, every stray thought vanished and post-nut clarity hit me.

*One, two, three.*

Had I counted wrong? Or were the letters too small for me to see? I widened my eyes and stared at the Skill Window.

One, two, three…and three.

The Jin Family’s Cultivation Technique, the Jin Family’s Spear Technique, and the Jin Family’s Manoeuvre Technique. Those were all the skills Jin Taekyung—or rather, I—had. And apparently, I’d forgotten every one of them.

*This is driving me insane.*

If I died, the cause would be pent-up rage. Pure pent-up rage.

Only after calming down somewhat could I look at the Skill Window with a clear head.

Right. I could learn martial arts later.

*At least I have unassigned points.*

Trying to comfort myself with that thought, I looked at the Skill Window again. Maybe because it was so empty, one word immediately caught my eye.

*Sinews and Bones. I’ve seen those a lot in martial-arts novels.*

Sinews referred to tendons and veins, while bones meant muscles and the skeletal frame.

In other words, Sinews were for an internal-energy-focused build, while Bones were for external martial arts. I decided to lean a little more toward Bones.

The reason was simple.

*I’ll have a better chance of surviving if I choose what I’m already familiar with.*

In the real world, I was an F-rank Hunter. In Murim terms, I was a third-rate martial artist, or maybe even worse.

Magic and aura… I’d seen them with my own eyes, but using them myself was out of the question. I couldn’t even dream of it.

*You can only handle what you’ve tried before.*

You had to have used internal energy before to know how to use it. The way I’d fought over the past seven years was closer to that of an external martial artist.

*Sixty into Bones. Forty into Sinews.*

> **System**
>
> Apply these settings?

*Yes. Apply.*

This time, what swept through me was nothing like the exhilaration I’d felt from the Status Window. If anything, it was pain. I could hear the bones in my body twisting deep inside.

*Urgh.*

Was it seconds? Minutes? I had no idea. When the pain passed, I was left panting—and rewarded for my endurance.

*My build…*

It had changed. My shoulders had broadened by half a span, and muscle had hardened across my front and back. The silk clothes that had felt a little loose now felt constricting.

When I clenched my fists, I felt strength and springiness I hadn’t been able to sense before. I’d grown stronger. It was an experience I’d never had in the real world.

*Because there’s no System there.*

I could build strength, stamina, and flexibility through training in the real world, but until I underwent a measurement, I could only sense the changes vaguely.

But Murim was different.

I could see my abilities through the Status Window and improve the ones I needed. I didn’t know where the endpoint was, but I could keep moving forward.

*I’ll get stronger. And I’ll survive.*

I’d fought countless monsters over the past seven years. Some days I’d returned without a scratch; other days I’d barely escaped with my life.

F-rank Hunter Jin Taekyung had something Murim’s Jin Taekyung didn’t: experience. And desire.

Stronger, stronger, stronger. And survive.

Just as I clenched my fist and made that vow, another notification rang out.

Ding.

> **System**
>
> Check and Distribute Skill Window Points complete.

Only one thing remained.

*Check the Inventory.*

Ding.

> **System**
>
> Inventory
>
> Sturdy Martial Uniform Set
>
> **Grade:** Third Rate
>
> **Restriction:** None
>
> **Effect:** None
>
> **Description:** Made from light, durable cloth. Suitable for beginners.

The description was simple, befitting a basic item.

*Equip item.*

A refreshing sensation swept over me, and I found myself dressed in a black martial uniform.

It wasn’t just my clothes that had changed. A headband—commonly called a hero’s headband in martial-arts novels—was tied firmly around my forehead, and I was wearing leather shoes instead of silk ones.

Did I at least look like a run-of-the-mill martial artist now?

*Store item.*

The moment I thought about storing the silk clothes I’d taken off, they vanished from my hands.

*An Inventory. This is incredibly convenient.* It might even be useful in combat, depending on how I used it.

*Having an Inventory would make raids so much easier.*

With one of these, I could hang back and collect Magic Gems without even fighting the monsters. I’d make enough in a year to put up a whole building.

*But that’s not going to happen.*

Because this was a game. Once I logged out, it would all be over.

…Though I wasn’t even sure I’d survive long enough to log out.

Ding.

> **System**
>
> Check and Equip Inventory Items complete.
>
> Tutorial—Stage 2 complete. Rewards will be distributed.
>
> Chain Quest Tutorial—Stage 3 created.

A new reward!

I immediately opened the Inventory to check the new item.

> **System**
>
> Inventory
>
> Sharp Spear
>
> **Grade:** Second Rate
>
> **Restriction:** None
>
> **Effect:** 5% chance to inflict Bleeding on hit
>
> **Description:** A reasonably usable spear. It’s sharp, so be careful when handling it.

“…”

If my Status Window and Skill Window were going to be such a mess, couldn’t they at least give me a good item? Then again, considering everything that had happened so far, this was practically generous.

*Equip item.*

The moment the shaft of the spear appeared in my grasp—

Ding.

> **System**
>
> Tutorial—Stage 3 begins. Prepare yourself.

“…Huh?”

Prepare myself? For what?

I hadn’t even opened the quest window yet.

The answer came from an unexpected place.

The taciturn coachman spoke for the first time.

“Young Master.”

“Yes?”

“A minor problem has arisen.”

“What are you talking about all of a sudden—”

Ding.

> **System**
>
> Quest
>
> Tutorial—Stage 3
>
> You have learned how to grow stronger through the System.
>
> What you learn must be put into practice.
>
> Defeat the bandits who have appeared without warning!
>
> **Grade:** Tutorial (Chain Quest)
>
> **Restriction:** First-time player
>
> **Objective:** Defeat the bandits (Incomplete)
>
> **Reward:** Recover from all injuries
>
> Chain Quest
>
> **Failure:** Death

*Some minor problem.* My ass.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 3`.
