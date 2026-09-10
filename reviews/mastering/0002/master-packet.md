# Master Edit Task — Chapter 2

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
| 항산검문   | **Mount Heng Sword Sect**        |
| 마적     | **mounted bandits**                              |                                                       |
| 기루     | **pleasure house**                               |                                                       |
| 기녀     | **courtesan**                                    |                                                       |
| 곰방대   | **long-stemmed tobacco pipe**                    |                                                       |
| 시스템              | **System**                     |
| 상태창              | **Status Window**              |
| 상태               | **Status**                     |
| 스킬               | **Skill**                      |
| 스킬창              | **Skill Window**               |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 로그인              | **Login**                      |
| 로그아웃             | **Logout**                     |
| 지능               | **Intelligence**               |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 공자      | **Young Master**                                                |
| 성진호 | **Seong Jinho** |
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

## Korean source

```text
＃2화



찬 바람이 얼굴에 닿았다. 나는 어릴 적부터 추위를 많이 타는 체질이라 사시사철 창문을 닫고 산다. 그럼 누가 창문을 열었단 말인가?

‘뻔하지.’

성진호, 이 원수 같은 인간.

투덜거리며 이불을 목 끝까지 끌어올렸다. 옆에 누운 여자가 작게 칭얼거렸다.

“……어?”

여자? 여자 누구?

순간 잠이 확 깼다. 나는 기상나팔 소리를 들은 이등병처럼 벌떡 일어났다. 그리고 천천히 고개를 돌렸다.

“타이렁러太冷了.”

세상에. 두 번 놀랐다. 첫 번째, 지금 이 상황을 이해할 수 없어서, 두 번째, 옆에 누워 있는 여자가 너무 예뻐서.

연신 알아들을 수 없는 말을 중얼거리면서 이불로 파고드는데, 정신이 없는 와중에도 가슴이 떨릴 정도로 아름답다.

때마침 불어온 찬 바람이 아니었다면 한참을 넋 놓고 바라봤을 것이다.

‘그런데 여기가 어디지?’

주위를 둘러봤다. 은은하게 감도는 붉은 촛불. 이상하게 자극적인 향기와 이불로 벗은 몸을 가린 미녀.

가 본 적은 없지만 어디선가 많이 들어 본 그곳.

‘룸살롱?’

아니, 근데 내가 왜 여기 있어?

그저 어리둥절하다. 뭐가 어떻게 된 거지? 어제는 진호 형이랑 한잔하고 고시원에 있는 내 방으로 돌아왔는데.

요란한 코골이 소리를 피해 캡슐로 들어간 것까지, 전날의 기억이 생생하다.

‘꿈을 꾸고 있나?’

팔뚝을 강하게 꼬집었다. 아프다. 꿈이 아니다.

점점 미궁으로 빠지는 상황이다. 멍하니 주위를 둘러보던 나는 여자의 어깨를 잡고 흔들었다.

“저, 저기요.”

여자가 게슴츠레한 눈으로 나를 바라봤다. 검푸른색으로 반짝이는 눈동자에 가슴이 또 쿵쾅거린다.

“누구세요?”

“션머?”

“아, 선미 씨구나. 그런데 제가 물어본 건 그 뜻이 아닌데……”

“션머?”

“예……?”

“션머……?”

뭐야, 이게.

잠시 흐르는 적막 속에서 우리는 서로를 응시했다. 그리고 깨달았다. 이 여자, 한국인이 아니다.

“혹시 중국인이세요? 아니면 필리핀?”

“……짜이나오런마?”

‘이건 뭐, 말이 안 통하네.’

답답함에 뒤통수를 벅벅 긁은 나는 다음 순간 용수철처럼 튀어 올랐다.

띠링.



읽지 않은 메시지를 확인하시겠습니까?

수락    /    거절



어디선가 들려온 종소리.

유령처럼 허공에 둥둥 떠 있는 네모난 창.

어디서 튀어나왔는지, 그전에 왜 이런 게 보이는지 짐작도 가지 않는다. 소름이 쫙 끼쳤다.

“시발, 뭐야 이거.”

억지로 쥐어 짜낸 목소리와 함께 반사적으로 주먹을 뻗었다.

주먹이 그대로 네모 창을 관통, 아니, 통과했다. 정확히는 [수락]이라는 단어를.

띠링.



- 오랫동안 응답이 없어 캐릭터를 랜덤 선택 합니다.

- [무림]을 탐색 중…… 캐릭터, [진태경]으로 플레이를 시작합니다!

- [무림]에 로그인했습니다.

- 최초 접속 보상이 주어집니다.

.

.

- 현재 사용 중인 플레이어의 언어를 변경할 수 있습니다. [통합 언어 팩]을 적용하시겠습니까?



캐릭터? 무림? 로그인?

“어? 어어?”



- [통합 언어 팩]이 적용됩니다.



“잠깐, 잠깐만!”

그때 여자가 말했다.

“진 공자. 어디 아파요?”

정확한 한국어 발음이다. 나는 [통합 언어 팩]이 적용됐다는 네모 창과 여자를 번갈아 보다가 생각했다.

뭐가 어떻게 돌아가는 거야?



* * *



월화(月華). 여자의 이름이다.

희고 매끄러운 피부에 주먹만 한 얼굴. 오밀조밀한 이목구비에 눈은 얼마나 크고 맑은지, 연예인 뺨 칠 정도다.

나는 다시 한번 감탄했다.

‘그래픽 끝내준다.’

대강의 상황 파악은 끝난 후였다. 몇 가지만 맞춰 보면 간단한 사실이었다.

무림. 캐릭터. 로그인. 플레이. 내가 마지막으로 잠든 곳은 게임 캡슐. 그리고 결정적으로.



메시지창을 여시겠습니까?

수락    /    거절



시스템창이 있다. 소리 내서 말해도 되고, 속으로 생각해도 된다. 머리를 긁는 것은 일종의 단축키다. 허공에 원하는 항목을 클릭하는 것도 가능하다.

‘이건 볼수록 신기하네.’

마지막으로 플레이한 게임과는 상당한 괴리감이 있지만, 이곳은 게임 안이다. 나는 지금 게임을 하고 있다.

‘그런데 언제 로그인이 됐지?’

선을 꽂아 뒀던 기억은 없는데. 전날의 기억을 떠올리려는 찰나, 월화가 불쑥 손을 내밀었다. 잡티 하나 없는 두 손에는 물이 가득 찬 대접이 들려 있다.

“마셔요. 잠이 덜 깬 것 같은데.”

‘인공지능도 끝내주네.’

월화의 얼굴을 힐끔거리면서 물을 들이켰다. 그리고 깜짝 놀랐다.

‘뭐야, 이거?’

냉수를 삼킬 때 느껴지는 청량감. 식도를 타고 배 속까지 시원해지는 느낌. 팔뚝에 닭살이 돋을 정도로 생생하다.

실사 그래픽에 NPC의 인공지능, 하다못해 냉수 한 모금을 마셔도 게임이라곤 믿기 힘들 정도였다.

이야, 요즘 기술이 엄청나다는 소문은 들었지만 이 정도일 줄이야. 게임 폐인이 생기는 이유를 알겠다.

‘이래서 가상현실, 가상현실 하는구나.’

놀이공원에 온 유치원생처럼 입을 벌리고 주위를 둘러보는데, 어디선가 매캐한 연기가 피어올라 눈 앞을 가렸다.

고개를 돌려보니 어느새 곰방대를 문 월화가 나를 물끄러미 바라보는 중이었다.

“왜……요?”

워낙 사람 같아서 나도 모르게 존댓말이 튀어나왔다. 물론 그녀가 엄청난 미인이라는 이유도 한몫했다.

월화는 연기를 후, 내뿜으며 대답했다.

“그냥. 보고 싶어서?”

얘는 얼굴만 예쁜 줄 알았더니 분위기도 장난 아니구나.

여고생들이 봤으면 언니를 외치며 쌍코피를 터뜨릴 정도의 포스다. 머리부터 발끝까지 딱 이렇게 쓰여 있다.

‘팜므파탈.’

캐릭터 컨셉 잘 잡았네. 월화만 보고 게임 시작하는 유저들도 꽤 있을 것 같다.

“진 공자, 오늘 좀 이상한 거 알아요?”

진 공자? 오글거리는 호칭이다. 하지만 나는 시치미를 뚝 뗐다. 뭐랄까, 조금은 이 상황을 즐기고 싶었다.

‘게임이니까.’

“뭐가요?”

“전부 다? 실성한 것처럼 허공을 바라보질 않나, 갑자기 존댓말을 쓰질 않나. 도무지 종잡을 수가 없네.”

월화가 말을 마친 순간이었다.

띠링.



- [튜토리얼 퀘스트]가 생성되었습니다.



게임 진행 방식이 참신하다. 보통은 다짜고짜 ‘드디어 정신이 들었군.’으로 시작해서 튜토리얼 퀘스트를 줬던 것 같은데.

이런 걸 자유도라고 하나?

‘어…… 퀘스트 확인?’

하면서도 이게 맞나 헷갈렸는데, 예의 효과음과 함께 곧바로 퀘스트창이 떴다.



퀘스트



[튜토리얼 - 1단계]

이제 당신은 무림에서의 첫발을 내딛습니다.

기본적인 정보를 수집하고 상황을 인지하십시오.



등급 : 튜토리얼 (연계 퀘스트)

제한 : 최초 접속자

임무 : 정보 수집 (미완료)

         상황 인지 (미완료)

보상 : 단단한 무복 세트

        캐릭터 상태창 활성화

        인벤토리 기능 활성화

        스킬창 기능 활성화

        연계 퀘스트





‘정보 파악, 상황 인지?’

게임을 많이 해 본 건 아니지만 이런 퀘스트는 또 처음이다.

보통은 토끼를 몇 마리 잡으라거나, 게임 인터페이스 사용법을 연습시키지 않나?

어쨌건 시도는 해 봐야지.

“나에 대해서 얼마나 알아요?”

내가 생각해도 단도직입적인 질문이다. 담배 연기 너머로 웃고 있는 월화의 얼굴이 보였다.

“재밌는 질문이네요. 소문 그대로라고 해야 하나?”

“소문?”

“공자도 익히 알고 있는 그런 이야기들이죠. 당사자 면전에 대고 말할 만큼 좋은 이야기는 아니지만.”

“괜찮으니까 들어나 봅시다.”

나는 점점 이 게임에 대해 흥미가 생기기 시작했다. 오랜만에 하는 게임이기도 했지만, 기존의 방식과는 다른 참신함 때문이었다. 어디서 만든 건지, 게임 한번 잘 만들었다.

“궁금해서 그래요. 내가 들은 소문이랑 같은지. 뭐 하루 이틀도 아닌데 기분 나쁘고 자시고가 있나.”

“……뭐 그렇다면야.”

물었군. 나는 내심 흐뭇하게 웃었다. 이제 본격적으로 정보를 캐낼 일만 남았다.

“첫 번째. 내가 누군지 알아요?”

아까보다 더 괴상해진 질문이었지만 월화는 순순히 대답했다. 이 상황을 즐기는 것 같기도 했다.

“올해로 약관이 된 태원진가의 막내 도련님. 이름까지 알려 드릴 필요는 없겠죠?”

나는 자신 있게 대답했다.

“압니다. 진태경.”

제 이름은 진태경. 태원진가의 막내죠.

내 자신만만한 대답을 들은 월화는 연기를 내뱉다 말고 사레가 들렸다.

“두 번째. 태원진가는 어떤 곳입니까?”

간신히 기침을 멈춘 월화가 대답했다.

“세간의 평판이 좋아요. 이따금 마적 떼 토벌도 하고, 가뭄이 오면 관아보다 먼저 구휼미를 풀기도 하니까.”

이게 끝?

내 실망을 알아차리기라도 한 것처럼 월화의 말이 이어졌다.

“무엇보다 산서성을 대표하는 명가(名家)죠. 뿌리 깊은 거목이랄까.”

“오오!”

나도 모르게 탄성을 터트렸다. 태원진가의 대단함에 감동한 게 아니라, 시스템 알림 때문이다.

띠링.



- [태원진가]에 대한 정보를 수집했습니다.

- 칭호, [명가의 자제]를 얻었습니다. 추후 상태창을 통해 확인할 수 있습니다.



‘칭호? 명가의 자제?’

판타지 장르 게임에서의 타이틀 같은 건가 보다.

‘드래곤 슬레이어라든지. 뭐 그런 거.’

일정 업적을 달성하면 주어지고, 타이틀을 장착하면 부가 효과가 따라붙는다. 그런 면에서 나 같은 경우에는 상당히 운이 좋다고 할 수 있겠다.

‘이거 완전히 금수저 캐릭터잖아.’

명문가에서 태어난 것 자체가 업적이라니. 열받으면서도 기쁘다. 제멋대로 선택된 랜덤 캐릭터가 로또였다는 말이니까. 그러나 이야기는 거기서 끝이 아니었다.

“하지만 요즘은 안팎으로 문제가 있다고 들었어요.”

“문제? 무슨 문제요?”

그러고 보니 퀘스트창의 정보 수집은 여전히 [미완료]인 상태다. 아직 남은 정보가 있다는 뜻.

“밖의 문제는 호시탐탐 산서성의 맹주 자리를 노리는 항산검문(恒山劍門)과의 대립이고, 안의 문제는…….”

월화는 느긋하게 담뱃재를 털어 냈다.

“그 집안 셋째 아들이 그렇게 망나니라고 하더라고요.”

“아하, 어딜 가든 그런 놈들이 꼭 하나씩 있죠.”

나는 무의식적으로 고개를 끄덕이다가 이상한 기분에 사로잡혔다.

“저기요.”

“네?”

“이건 정말 장난삼아 묻는 건데, 태원진가에 아들이 몇 명이죠?”

해맑은 웃음과 함께 대답이 돌아왔다.

“셋이요.”

태원진가에는 아들이 셋이고 내가 그중 막내인데, 셋째 아들이 망나니란다. 그러니까 그게.

‘시벌. 나네?’

띠링.



- 칭호, [가문의 수치]를 얻었습니다. 추후 상태창을 통해 확인할 수 있습니다.

- [정보 수집]을 완료했습니다.



이걸 웃어야 할지, 울어야 할지. 고민하다가 피식거리는 월화를 보고 나도 허허 웃어 버렸다.

그래. 좋은 게 좋은 거지. 가문의 수치면 뭐 어때. 어차피 게임인데.

나는 퀘스트창을 열어 정보 수집이 [완료]로 바뀐 것을 확인했다.

‘문제는 상황 인지인데.’

이놈의 퀘스트는 두루뭉술해서 정확히 뭘 요구하는 건지 모르겠다. 결국 해결책은 월화밖에 없나?

“여기가 어디죠?”

“홍화루, 산서 제일의 기루죠. 여긴 내 방이고.”

대화를 통해 추가로 자질구레한 사실들을 알 수 있었다.

이곳이 태원 중심부에 위치한 홍화루라는 것. 월화는 상당히 높은 직급의 기녀이며 나와 하룻밤을…… 흠흠.

별의별 이야기가 다 나왔음에도 불구하고 시스템 알림은 뜨지 않았고, 급기야 물어볼 것은 바닥이 드러났다.

마지막에는 이런 질문까지 할 정도로.

“제 지금 상황은요?”

월화가 한숨을 내쉬었다.

“진 공자. 이런 말 해서 미안한데, 지금 살짝 미친놈 같아. 좀 쉬는 게 어때요?”

그러게. 나도 미칠 것 같다.

창문 사이로 햇살이 비치는 걸 보고 있자니 이게 무슨 짓인가 싶다.

‘무슨 추리 게임도 아니고.’

그래픽, 인공지능, 뭐 다 좋은데 튜토리얼부터 막히니까 재미가 뚝 떨어진다. 그나마 한 가지 수확이 있다면 어제 주운 캡슐이 보기보다 좋은 물건이라는 사실이다.

이 정도 게임이면 상당한 고사양인데, 렉 한번 걸리지 않았다. 중고 시장에 올려도 괜찮겠지.

‘오늘부터 새 일자리도 구해 봐야 하고.’

그래도 뭐, 잠깐 플레이한 것치곤 나쁘지 않았다.

나는 마지막으로 월화에게 눈인사를 건네고 외쳤다.

“로그아웃!”

- 로그아웃이 불가능합니다.

어라?

“로그아웃.”

- 로그아웃이 불가능합니다.

이거 왜 이래.

오류? 아니면 고물 캡슐이 드디어 렉이 걸렸나?

“……로그아웃?”

- 로그아웃이 불가능합니다.

확실하다. 오류건 렉이건, 빌어먹을 고물 캡슐이 드디어 일을 냈다. 그 뒤로도 열 번을 더 시도했지만 모두 실패했다.

이쯤 되니 분노는 슬슬 걱정과 후회로 바뀌고 있었다.

‘이거 무슨 일 나는 거 아니야?’

공짜라고 막 주워 오지 말걸. 진호 형이 쓰레기라고 했을 때 바로 갖다 버릴걸. 아니면 정신병자 같은 사용 설명서를 읽자마자…….

‘아니. 잠깐만.’

사용 설명서. 맞아, 그걸 읽었었지. 정확히는 주의 사항만 몇 개 읽고 집어 던졌지만 읽긴 했다.

‘그게 무슨 내용이었지?’

그리고 가까스로 읽었던 주의 사항의 내용을 모두 떠올린 순간, 온몸에 오한이 들었다.



- 플레이어 임의로 로그아웃할 수 없습니다.

- 플레이 도중 사망 시, 부활할 수 없습니다.



게임 안에 갇혔다고? 내가?

질문에 대한 대답은 시스템 알림이 대신했다.

띠링.



- [상황 인지]를 완료했습니다.

- [튜토리얼 - 1단계]를 완료했습니다. 보상이 지급됩니다.

- [상태창]이 활성화됩니다.

- [스킬창]이 활성화됩니다.

- [인벤토리]가 활성화됩니다.

- 연계 퀘스트, [튜토리얼 - 2단계]가 생성되었습니다.



그 순간, 단 한 가지 생각만이 머리를 채웠다.

‘좆 됐다.’
```

## Current accepted English baseline

```markdown
# Chapter 2

A cold wind brushed my face.

I’d been sensitive to the cold since I was a kid, so I kept my windows closed all year round. So who had opened the window?

*Obviously.*

Seong Jinho, that miserable excuse for a human being.

Grumbling, I pulled the blanket up to my neck. The woman lying beside me let out a small whine.

“…Huh?”

*A woman? Which woman?*

I woke up in an instant and shot upright, like a private startled awake by reveille. Then I slowly turned my head.

“Tài lěng le.”

Good heavens. I was startled twice. First, because I couldn’t make sense of the situation. Second, because the woman lying beside me was unbelievably beautiful.

She kept muttering words I couldn’t understand and burrowed deeper beneath the blanket. Even in my dazed state, she was beautiful enough to make my heart skip.

If that cold wind hadn’t blown in right then, I might have stared at her for quite a while.

*But where am I?*

I looked around. Red candlelight glowed softly around the room. A strangely stimulating fragrance filled the air, and a beautiful woman lay beside me, covering herself with a blanket.

A place I’d never visited but had heard about plenty of times.

*A room salon?[^1]*

But why was I here?

I was completely bewildered. What had happened? Yesterday, I’d had a drink with Jinho and returned to my room at the goshiwon.

I clearly remembered climbing into the capsule to escape Jinho’s thunderous snoring.

*Am I dreaming?*

I pinched my forearm hard. It hurt. This wasn’t a dream.

The mystery deepened. I stared blankly around the room, then grabbed the woman by the shoulder and shook her.

“Excuse me?”

The woman looked at me through half-lidded eyes. Her irises shimmered a dark blue, and my heart began pounding again.

“Who are you?”

“Shenme?”

“Ah, Ms. Sunmi. But that wasn’t what I meant…”

“Shenme?”

“…Yes?”

“Shenme…?”

*What the hell is this?*

For a moment, we stared at each other in silence. Then I realized it. This woman wasn’t Korean.

“Are you Chinese? Or Filipino?”

“…Zhōngguó rén ma?”

*This is useless. We can’t communicate at all.*

I scratched vigorously at the back of my head in frustration. The next moment, I sprang up like a compressed spring.

Ding.

> **System**
>
> Would you like to check your unread messages?
>
> Accept / Decline

A bell rang from somewhere.

A square window floated in midair like a ghost.

I had no idea where it had come from—or, more importantly, why I could see something like this. I broke out in goose bumps.

“What the fuck is this?”

I lashed out on reflex, forcing the words through clenched teeth.

My fist pierced the square window—or rather, passed through it. More precisely, it passed through the word *Accept*.

Ding.

> **System**
>
> No response for an extended period. Randomly selecting a character.
>
> Searching Murim… Starting play as character Jin Taekyung!
>
> Logged in to Murim.
>
> First-login rewards granted.
>
> You can change the language of the player currently in use. Apply the Universal Language Pack?

*A character? Murim? Login?*

“Huh? Huh?”

> **System**
>
> Applying the Universal Language Pack.

“Wait, hold on!”

That was when the woman spoke.

“Young Master Jin. Are you feeling ill?”

She was speaking perfect Korean. I looked back and forth between the square window announcing that the Universal Language Pack had been applied and the woman, then thought:

*What the hell is going on?*

* * *

Wolhwa. That was the woman’s name.

She had smooth, pale skin and a face the size of my fist. Her delicate features were perfectly arranged, and her eyes were so large and clear that she could have put a celebrity to shame.

I admired her once again.

*The graphics are incredible.*

I’d already worked out the general situation. Once I put a few things together, the truth was simple.

Murim. Character. Login. Play. The last place I’d fallen asleep was inside a game capsule. And most importantly—

> **System**
>
> Would you like to open the message window?
>
> Accept / Decline

There was a System window. I could speak aloud or think my commands. Scratching my head acted as a kind of shortcut. I could even click the options I wanted in midair.

*The more I see, the more amazing this gets.*

It was a far cry from the last game I’d played, but this was a game. I was inside a game right now.

*But when did I log in?*

I didn’t remember plugging anything in. Just as I was trying to recall what had happened the night before, Wolhwa suddenly held out a bowl of water in both hands.

“Drink. You don’t seem fully awake yet.”

*The AI is incredible, too.*

I glanced at Wolhwa’s face as I drank the water, then nearly jumped out of my skin.

*What the hell?*

Cold water slid down my throat, then spread through my stomach in a wave of coolness. The sensation was so vivid that goose bumps rose on my forearms.

The lifelike graphics and the NPC’s artificial intelligence were one thing, but even a sip of cold water felt too real for this to be a game.

Wow. I’d heard that technology had advanced by leaps and bounds, but I never imagined it had come this far. Now I understood why people became gaming addicts.

*So this is why they call it virtual reality.*

I looked around with my mouth hanging open like a kindergartener at an amusement park. Then acrid smoke rose from somewhere and obscured my view.

I turned my head. Wolhwa was already watching me intently, a long-stemmed tobacco pipe between her lips.

“Why…?”

She seemed so much like a real person that I slipped into polite speech without thinking. Of course, the fact that she was stunningly beautiful had something to do with it.

Wolhwa exhaled a stream of smoke and answered.

“Just because. I wanted to see you?”

*I thought she was just a pretty face, but she had one hell of a presence, too.*

If a bunch of high school girls saw her, they’d be screaming “Big Sis!” while blood poured from both nostrils. From head to toe, she practically had one phrase written all over her.

*Femme fatale.*

*They really nailed her character concept. Plenty of players probably start the game just for Wolhwa.*

“Young Master Jin, did you know you’ve been acting strange today?”

*Young Master Jin? What an embarrassing way to be addressed.*

Still, I pretended not to notice. Somehow, I wanted to enjoy the situation a little.

*It’s a game, after all.*

“What do you mean?”

“Everything? You keep staring into empty air as if you’ve lost your mind, and now you’re suddenly speaking formally. I can’t make heads or tails of you.”

The instant Wolhwa finished speaking—

Ding.

> **System**
>
> Tutorial Quest created.

*The game’s progression is pretty innovative.*

Usually, games started with something like, “At last, you’re awake,” before immediately handing out a tutorial quest.

*Is this what they call freedom?*

“Uh… Check quest?”

Even as I said it, I wasn’t sure whether that was the right command. But with the familiar sound effect, a quest window appeared at once.

> **System**
>
> Quest
>
> Tutorial—Stage 1
>
> You are now taking your first step into Murim.
>
> Gather basic information and understand the situation.
>
> **Grade:** Tutorial (Chain Quest)
>
> **Restriction:** First-time players
>
> **Missions:** Gather information (Incomplete)
>
> Understand the situation (Incomplete)
>
> **Rewards:** Sturdy martial uniform set
>
> Character Status Window unlocked
>
> Inventory function unlocked
>
> Skill Window function unlocked
>
> Chain Quest

*Gather information? Understand the situation?*

I hadn’t played many games, but I’d never seen a quest like this before.

Usually, they had you kill a few rabbits or practice using the game interface.

Still, I had to give it a try.

“How much do you know about me?”

Even I thought it was a very blunt question. I could see Wolhwa smiling through the smoke from her pipe.

“That’s an interesting question. Should I say you’re just like the rumors?”

“Rumors?”

“The stories you already know so well, Young Master. They aren’t exactly flattering enough to tell you to your face.”

“That’s fine. Let’s hear them.”

I was growing more interested in this game by the minute. It was the first game I’d played in a long time, but more than that, its approach was refreshingly different from the usual. Whoever had made it knew how to build a game.

“I’m just curious whether they match the rumors I’ve heard. It’s not like this has only been going on for a day or two. Why would I get offended?”

“…If you insist.”

*Got her.*

I smiled inwardly, pleased. Now all that remained was to pry out some real information.

“First. Do you know who I am?”

It was an even stranger question than the one before, but Wolhwa answered without hesitation. She almost seemed to be enjoying the situation, too.

“The youngest son of the Jin Family of Taiyuan, who came of age at twenty this year. Surely I don’t need to tell you his name as well?”

I answered confidently.

“I know. Jin Taekyung.”

*My name is Jin Taekyung. I’m the youngest son of the Jin Family of Taiyuan.*

At my confident reply, Wolhwa choked on the smoke she was exhaling.

“Second. What kind of place is the Jin Family of Taiyuan?”

After barely managing to stop coughing, Wolhwa answered.

“They have a good reputation among the public. From time to time, they wipe out bands of mounted bandits, and when droughts come, they release relief grain before even the local government does.”

*That’s it?*

As if she had noticed my disappointment, Wolhwa continued.

“More than anything, they’re a prestigious family representing Shanxi. You could say they’re one of the region’s old, deeply rooted powers.”

“Oh!”

I let out an involuntary exclamation—not because I was moved by the greatness of the Jin Family of Taiyuan, but because of the System notification.

Ding.

> **System**
>
> Information about the Jin Family of Taiyuan gathered.
>
> Title Scion of a Prestigious Family acquired. Check it later through the Status Window.

*A title? Scion of a Prestigious Family?*

I guessed it was something like a title in a fantasy game.

*Dragon Slayer, or something like that.*

You received one after accomplishing a certain feat, and equipping it granted additional effects. In that respect, I had to say I was pretty lucky.

*This guy really was born with a silver spoon in his mouth.*

Being born into a prestigious family counted as an achievement. It pissed me off and made me happy at the same time. That meant the random character selected against my will had turned out to be a lottery winner. But the story didn’t end there.

“I’ve heard there are problems inside and outside the family these days.”

“Problems? What kind of problems?”

Come to think of it, the quest window’s information-gathering mission was still marked *Incomplete*. That meant there was more information to collect.

“Externally, there’s the conflict with the Mount Heng Sword Sect, which is constantly eyeing the position of Shanxi’s leader. Internally…”

Wolhwa leisurely tapped the ash from her pipe.

“I hear that family’s third son is a notorious good-for-nothing.”

“Ah. There’s always one of those wherever you go.”

I nodded unconsciously, then was seized by a strange feeling.

“Excuse me.”

“Yes?”

“This is just a joke, but how many sons does the Jin Family of Taiyuan have?”

She answered with a sunny smile.

“Three.”

The Jin Family of Taiyuan had three sons, and I was the youngest of them. But the third son was a notorious good-for-nothing. Which meant—

*Fuck. That’s me, isn’t it?*

Ding.

> **System**
>
> Title Shame of the Family acquired. Check it later through the Status Window.
>
> Gather Information complete.

Whether I should laugh or cry, I had no idea. When I saw Wolhwa snickering, I let out a hollow laugh too.

*Well, better to look on the bright side. So what if I’m the shame of the family? It’s only a game, anyway.*

I opened the quest window and confirmed that *Gather Information* had changed to *Complete*.

*The problem is understanding the situation.*

This damn quest was so vague that I had no idea what exactly it wanted. In the end, was Wolhwa my only solution?

“Where are we?”

“Honghwaru, the finest pleasure house in Shanxi. This is my room.”

Through our conversation, I learned a few more miscellaneous facts.

We were in Honghwaru, located in the center of Taiyuan. Wolhwa was a high-ranking courtesan, and I had spent the night with her… Ahem.

Despite all the various things we discussed, no System notification appeared. Eventually, I ran out of questions to ask.

At the very end, I was reduced to asking this:

“What’s my situation right now?”

Wolhwa sighed.

“Young Master Jin, I’m sorry to put it this way, but you seem a little crazy right now. How about getting some rest?”

*Well, I feel like I’m going crazy, too.*

As sunlight streamed through the window, I began to wonder what on earth I was doing.

*This isn’t some kind of mystery game.*

The graphics and artificial intelligence were all great, but being stuck at the tutorial had completely drained the fun out of it. If there was one thing I’d learned, it was that the capsule I’d found yesterday was a much better piece of equipment than it looked.

A game this advanced had to require serious hardware, yet I hadn’t experienced a single bit of lag. It should sell for a decent price on the used market.

*I need to start looking for a new job today, too.*

Still, the game had been fun for a little while.

I gave Wolhwa a final nod and shouted:

“Log out!”

> **System**
>
> Logout is impossible.

*Huh?*

“Log out.”

> **System**
>
> Logout is impossible.

*What’s going on?*

An error? Or had the ancient capsule finally started lagging?

“…Log out?”

> **System**
>
> Logout is impossible.

There was no doubt about it. Error or lag, the damn old capsule had finally caused trouble. I tried ten more times after that, but every attempt failed.

By this point, my anger had gradually turned into worry and regret.

*Is something bad going to happen to me?*

*I shouldn’t have picked it up just because it was free. I should have thrown it away the moment Jinho called it garbage. Or at least, the moment I read that insane instruction manual…*

*No. Wait.*

The instruction manual. That was right—I’d read it. More precisely, I’d read a few of the warnings before tossing it aside, but I had read them.

*What did they say?*

The moment I finally remembered every warning I’d managed to read, a chill ran through my entire body.

> **System**
>
> The player cannot log out at will.
>
> If the player dies during gameplay, resurrection is impossible.

*I’m trapped inside the game? Me?*

The System notification answered my question for me.

Ding.

> **System**
>
> Understand the Situation complete.
>
> Tutorial—Stage 1 complete. Rewards will be distributed.
>
> Status Window activated.
>
> Skill Window activated.
>
> Inventory activated.
>
> Chain Quest Tutorial—Stage 2 created.

At that moment, a single thought filled my head.

*I’m fucked.*

[^1]: A room salon is a Korean private-room entertainment venue where customers are served food, alcohol, and conversation by hostesses.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 2`.
