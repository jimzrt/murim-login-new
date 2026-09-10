# Master Edit Task — Chapter 1

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
| 상태               | **Status**                     |
| 로그아웃             | **Logout**                     |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 성진호 | **Seong Jinho** |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

(No prior chapter summary available.)

### Prior accepted reading-copy tails

(None.)

## Korean source

```text
＃1화



“쓰레기네.”

진호 형이 판사처럼 엄숙하게 선고했다. 그는 내가 살고 있는 고시원의 총무로, 올해 나이 서른의 고시생이었다.

나와는 세 살 차이로 제법 친한 사이기도 했고, IT계열에 빠삭하다고 입버릇처럼 말하던 것이 생각나 주워 온 캡슐을 보여 준 건데…….

“그렇게 별로야?”

“아니. 쓰레기라니까.”

와, 한 치의 망설임도 없는 것 보소. 왠지 모르게 자존심이 상하는 느낌이다.

“제대로 보지도 않았잖아.”

말마따나 내부는 보지도 않았다. 그저 위아래로만 쓱 훑더니 대뜸 쓰레기란다. 적당한 중고 판매 가격을 생각하고 있던 나로서는 크나큰 심적 충격을 받았다.

“태경아. 태경아. 진태경아. 너는 큰 오해를 하고 있구나.”

“……?”

“똥은 똥일 뿐이란다. 굳이 똥을 파헤쳐서 어제 먹은 콩나물까지 확인할 필요가 없는 거지. 딱 보기에도 똥이거든.”

“아.”

“쉿. 그 이상은 말하지 마. 우리 사이에 공치사 들으려고 한 말은 아니니까.”

“형…….”

죽여 버리고 싶다. 충동이 반영된 주먹이 부르르 떨리자 진호 형이 흠칫한다. 평생 책상머리에 앉아 있던 그와는 달리 나는 제법 위협적인 덩치의 소유자였다.

“태경아. 우리 각성자 특별법 1조 12항을 되새겨 보자. 네가 지금 하려는 일은 각성자에 의한 민간인 폭행…….”

“나 같은 F급 헌터는 각성자도 아니라면서?”

“내가? 언제? 나 만취 상태였니?”

호들갑 떠는 모습을 보니 한숨만 나온다.

주먹이 스르륵 내려갔다.

“그래, 잘 생각했다. 가뜩이나 바닥 좁은데 민간인 폭행했다고 소문나면 길드에서도 잘리고…….”

“잘렸어.”

“어?”

“출근하자마자 팀장이 그러더라. 지금까지 고생했다고.”

스무 살에 시작한 일이었다. 돌아가신 아버지 대신 생계를 책임져야 했고, 그래서 선택한 직업이 헌터다.

F급. 이렇다 할 재능도 없는 최하급 헌터였지만 열심히 해 왔다고 자부한다. 그렇게 번 돈으로 어머니 병도 고치고 하나뿐인 동생 뒷바라지도 했다.

그런데 지금은…… 지난 7년이 송두리째 사라져 버린 기분이다. 몇 시간 전, 해고를 통보하던 팀장의 덤덤한 얼굴이 떠올라 가슴이 뻐근했다.

“어, 음.”

진호 형의 허둥대는 모습에 피식 웃음이 나왔다.

“미안하지?”

“솔직히…… 좀 그렇지.”

이 인간. 어울리지 않게 갑자기 진지한 표정 짓기는.

“그럼 술이나 한잔 사 줘라. 이럴 때 형 노릇 해야지.”

“말하는 싸가지 보소. 형 취급이나 해 주면서 그런 말을 해라.”

말은 그렇게 하면서도 나오라며 턱짓한다. 표정을 보니 오늘은 코가 비뚤어지게 마실 것 같다.



* * *



게이트(Gate)는 세상의 경계다. 게이트 밖, 즉 현대는 우리가 아는 문명사회지만 안으로 들어가면 듣도 보도 못한 괴물들이 우글거린다.

그중 가장 흔한 것이 나 같은 F급 헌터도 잡을 수 있는 약체 몬스터, 고블린이다.

지금 왜 이런 이야기를 하냐면.

쿠워어. 쿠워어.

‘사람이 어떻게 저러지?’

저게 인간이냐, 몬스터냐. 전봇대에 기대서 토악질을 해 대는 진호 형의 모습이 꼭 명치 세게 맞은 고블린 같다.

“보쇼. 진호 형. 성진호 씨. 정신 좀 차려 봐요.”

“쿠워?”

……그냥 하시던 일 계속 하세요.

‘천천히 좀 마시라니까.’

1차에서부터 혼자 미친 듯이 들이붓더니 이 모양 이 꼴이다. 내가 계산한 건 둘째치고, 인사불성이 된 인간을 업고 고시원까지 오느라 온몸이 흠뻑 젖었다.

땀은 기본이요, 토사물은 옵션이다. 누구 입에서 흐른 것인지는 명백하다.

간헐적으로 들려오는 구토 사운드를 배경음으로 깔고 뉘엿뉘엿 지는 해를 바라봤다.

‘잘린 것도 서러운데, 시바.’

오늘 하루의 기억들이 파노라마처럼 스쳐 지나간다.

일진이 아주 그냥, 끝내주는구나.

“끄윽. 끄으으. 여기가 어딥니까, 기사님. 예?”

그중에 당신이 제일 압권이야.

“집이지 어디야. 다 왔으니까 정신 좀 차려 봐.”

“집? 우리 집은 강원도에 있는데. 아, 엄마. 엄마! 엄마가 해 주신 된장찌개가 먹고 싶어요.”

“아, 제발. 고시원이라고, 형.”

“고시원? 희망 고시원?”

“어. 그러니까 정신 좀.”

“희망…… 그래, 희망은 돈으로 살 수 없어. 모두의 가슴속에 있는 거라고 우리 엄마가 그러셨지. 된장찌개를 끝내주게 잘 끓이셔.”

나는 참을성 있게 기다리다가 된장찌개 부분에서 진호 형의 배를 갈겼다.

그는 토하는 와중에도 각성자 특별법 1조 12항을 웅얼거림으로써 자신이 고시생이라는 사실을 증명했다.



* * *



“더럽게 찝찝하네.”

고시원 내 샤워실로 직행해 30분을 씻었건만, 아직도 토사물 냄새가 코끝에 맴도는 것 같다.

그렇게 킁킁거리며 돌아온 방에는 애물단지가 기다리고 있었다. 그것도 둘이나.

“쿠워어…….”

하나는 인사불성이 된 진호 형이고, 다른 하나는.

“아, 이걸 깜빡했네.”

캡슐. 3평 남짓한 방에 냉장고만 한 녀석을 놔뒀더니 방이 꽉 찬 것 같다. 나는 침대 위로 피신해서 이 녀석을 어떻게 할까 궁리하기 시작했다.

‘도로 갖다 버려?’

아니면 고물상에 넘겨도 된다. 요즘 고철 시세가 어떻게 되더라? 못해도 50kg은 나가는 물건이니까 간식값 정도는 나오겠지.

‘꽤 쓸 만한 물건인 줄 알았는데.’

똥이라. 이게 그 정도로 고물인가?

그러고 보니까 내부는 열어 보지도 않았다. 나는 갑자기 드는 호기심에 캡슐을 살펴보기 시작했다.

“우선 외관은…… 별로군.”

니코틴인지 뭔지 캡슐 표면이 누렇게 찌들어 있다. 군데군데 녹도 슬어 있는 것 같고. 미련을 버리고 살펴보니 진호 형의 말이 이해됐다.

“이렇게 여는 거였나?”

홀로 툭 튀어나와 있는 버튼을 누르자 뚜껑이 열리면서 내부가 드러났다. 뭔가 대단한 걸 기대했는데 역시나 별거 없다.

장시간 플레이를 위해 인체공학적으로 설계된 의자와 머리 전체를 감싸는 VR 헬멧이 전부…… 어?

“뭐야, 이건. 사용 설명서?”

정확히는 ‘제품 사용 설명서’라고 적혀 있는 소형 책자다.

버리는 물건에 사용 설명서까지 넣어 놓는 경우도 있나? 더군다나 이런 고물을?

나는 호기심에 첫 장을 펼쳤다.



[제품 사용 설명서]

제품명 : 가상현실 접속기

모델명 : Ark - 2020

제조사 : H 소프트

제조일 : 2020년 1월 1일



아무 생각 없이 활자를 훑던 눈동자가 멈춘 곳은 제조일이었다.

2020년 1월 1일이라. 인쇄 오류겠지. 아무렴.

‘어떤 정신 나간 놈이 그 날에, 아니, 그 시기에 게임기를 만들고 있었겠어?’

그 시기란 ‘대격변’을 일컫는다. 2015년 1월 1일. 인류에게 찾아온 것은 새해 일출만이 아니었다.

게이트, 혹은 던전이라 불리는 것이 세계 곳곳에 생성되었고 듣도 보도 못한 괴물들이 게이트를 통해 쏟아져 나왔다.

몬스터와 각성자, 전쟁과 파괴…….

비현실이 현실을 침범했고 지구 역사상 다시 없을 대전쟁은 몬스터들의 군주, 마왕 아스모데우스의 죽음으로 종식됐다.

그날이 2020년 1월 1일. 이른바 ‘승리의 날’이다.

‘그러니까 말도 안 되는 거지.’

쯧쯧. 나는 혀를 차며 페이지를 넘겼다.



[주의사항]

- 플레이어 임의로 로그아웃할 수 없습니다.

- 플레이 도중 사망 시, 부활할 수 없습니다.



아하, 그렇구나. 나는 고개를 끄덕이고 좁은 매트리스에 몸을 눕혔다. 남은 페이지가 몇 장 있었지만 알 바 아니다.

“잠이나 자야겠다.”

정신병자 같은 사용 설명서나 읽고 있을 바에는 잠이라도 자는 게 낫다. 나는 진호 형을 구석으로 밀어 낸 뒤 눈을 감았다.

쿠워어. 쿠워어.

“…….”

쿠워어. 쿠워어.

“…….”

저 캡슐, 방음 기능이 있던가?



* * *



의자는 딱딱했다. 2020년에 제작된 물건이니 나와는 동갑내기다. 의자, 방년 27세. 쿠션은 꺼진 지 오래였다.

냄새가 안 난다는 점에서 위안을 얻으며 이불을 목까지 끌어 올렸다.

쿠워어. 쿠워어.

……VR 헬멧까지 썼다.

‘이런 거 쓰고 자면 목 아픈데.’

소소한 불평은 헬멧을 쓰는 순간 싹 사라졌다. 완전한 무음의 세계. 작은 소음 하나 없는 고요가 찾아들었다.

그러나 그 뒤를 잇는 것은 졸음 대신 생각이었다.

‘내일부터 어떡하지?’

헌터는 분명히 고액 연봉을 받는 직종이지만 그것도 수준 나름이다.

나처럼 별 볼 일 없는 F급 헌터는 널리고 널렸고 길드 소속이 아니라면 꼭두새벽부터 인력 사무소에 도장을 찍어야 한다.

소속되지 않은 헌터는 서럽다. 정부 정책은 무소속 헌터에게 결코 호의적이지 않고, 헌터에게 부과되는 무지막지한 세율은 듣기만 해도 숨이 턱턱 막힐 지경이다.

‘이제 내가 그 꼴이 됐군.’

나와는 달리 어머니와 여동생은 안전 구역(Safety Sector)의 아파트에 거주 중이다. F급 헌터의 수입으로는 턱없는 사치지만 내게는 가족의 안전이 최우선이었다.

지금까지는 간신히 매년 갱신되는 전세 계약 기간까지 금액을 맞춰 왔지만, 이제부터는…… 글쎄.

‘시바, 모르겠다.’

문득 돌아가신 아버지가 생각났다.

가족에게 헌신하고 사회적으로 인정받던 아버지는 내가 일곱 살이 되던 해에 돌아가셨다.

게이트 균열로 인한 몬스터들의 습격. 평범한 회사원이었던 아버지로서는 피할 길이 없었을 것이다.

만약 아버지가 아직 내 곁에 있었더라면, 아들이 가야 할 방향을 알려 줄 수 있었을까?

‘그래도 지금까지 열심히 살았어요. 믿어 줘요.’

아까 마신 술기운이 슬슬 올라오는지, 옛날 생각을 해서인지, 나도 모르게 몸이 늘어지고 눈이 감겼다.

쏟아져 내리는 졸음을 받아들이며 나는 생각했다.

‘눈을 뜨면, 좀 더 나아져 있기를.’

누군가의 목소리가 귓가를 파고들었지만, 이제는 아무래도 좋다. 스르륵 잠에 빠져들었다.



- 플레이어를 인지합니다. ……등록되지 않은 플레이어입니다. 신규 등록 하시겠습니까?

- 오랜 시간 응답이 없으므로 자동 진행 됩니다.

- 1%…… 27%…… 94%…… 완료.

- 플레이어, [진태경]이 기기에 등록되었습니다.

- 선택지로 이동합니다. [무림]에 접속하시겠습니까?

- 오랜 시간 응답이 없으므로 자동 진행 됩니다.



- ……무운을 빕니다!
```

## Current accepted English baseline

```markdown
# Chapter 1

“It’s garbage.”

Jinho delivered the verdict with the solemnity of a judge. He was the manager of the goshiwon[^1] where I lived, a thirty-year-old exam candidate.

We were fairly close, only three years apart, and I remembered how he was always going on about how much he knew about IT. That was why I showed him the capsule I’d picked up, but…

“Is it really that bad?”

“No. I said it’s garbage.”

Wow. Not even a hint of hesitation. For some reason, I felt personally insulted.

“You didn’t even look at it properly.”

Just as I’d said, he hadn’t even looked inside. He’d merely given it a quick once-over, top to bottom, before declaring it garbage. Since I’d been thinking about how much I could get for it secondhand, the blow hit me hard.

“Taekyung. Taekyung. Jin Taekyung. You’re laboring under a serious misunderstanding.”

“…?”

“Shit is shit. You don’t have to dig through it to check for yesterday’s bean sprouts. You can tell it’s shit just by looking at it.”

“Oh.”

“Shh. Don’t say anything more. I wasn’t fishing for praise.”

“Jinho…”

I wanted to kill him. My fist trembled with the urge, and Jinho flinched. Unlike him, who had spent his entire life hunched over a desk, I had a fairly intimidating build.

“Taekyung. Let’s recall Article 1, Clause 12 of the Awakened Persons Special Act. What you’re about to do falls under assault of a civilian by an Awakened…”

“I thought you said an F-rank Hunter like me didn’t even count as an Awakened?”

“I did? When? Was I blackout drunk?”

Watching him make such a fuss, I could only sigh.

My fist slowly dropped.

“That’s right. Good thinking. This field is small enough as it is. If word got around that you assaulted a civilian, you’d get fired from your Guild too…”

“I already got fired.”

“Huh?”

“The moment I showed up, my Team Leader thanked me for all my hard work.”

I’d started that job at twenty. I’d needed to support my family in place of my late father, which was why I’d chosen to become a Hunter.

F-rank. The lowest possible grade, with no particular talent to speak of, but I prided myself on having worked hard. With what I earned, I paid for my mother’s medical treatment and supported my only younger sibling.

But now… it felt as though the past seven years had vanished all at once. I remembered the Team Leader’s impassive face as he informed me of my dismissal a few hours earlier, and my chest tightened.

“Uh… well.”

I gave a short laugh at Jinho’s flustered expression.

“You feel bad, don’t you?”

“Honestly… kind of.”

This guy. A serious expression really didn’t suit him.

“Then buy me a drink. This is when you’re supposed to act like my big brother.”

“Listen to the disrespect on you. Try treating me like your big brother before you say something like that.”

He said that, but still jerked his chin for me to follow. From his expression, we were going to drink until one of us fell over tonight.

* * *

A Gate marks the boundary of the world. Outside it—in other words, in the modern world—is the civilized society we know. Go inside, though, and it’s crawling with monsters no one has ever seen or heard of.

The weakest and most common of them were goblins—even an F-rank Hunter like me could handle one.

The reason I’m bringing this up now is…

“Gwaah. Gwaah.”

*How can a person even do that?*

Was that thing human or a monster? Leaning against a utility pole and vomiting, Jinho looked just like a goblin that had taken a hard blow to the solar plexus.

“Hey, Jinho. Mr. Seong Jinho. Try to come to your senses.”

“Gwaah?”

…Just carry on.

*I told you to drink slowly.*

He had been pounding drinks like a lunatic from the very first round, and this was how he’d ended up. Never mind that I’d had to pay the bill—I was soaked through after carrying the dead-drunk man all the way back to the goshiwon.

Sweat was a given. Vomit was extra. It was obvious whose it was.

While he retched intermittently in the background, I watched the sun sink toward the horizon.

*Getting fired wasn’t bad enough. Fuck.*

The memories of the day flashed through my mind like a panorama.

*What a day this is turning out to be.*

“Urp. Urrrgh. Where are we, driver? Huh?”

You were the highlight of it all.

“We’re home. We’re here, so try to wake up.”

“Home? My home’s in Gangwon Province. Oh, Mom. Mom! I want some of my mom’s doenjang stew[^2].”

“Oh, for crying out loud. It’s the goshiwon, Jinho.”

“The goshiwon? Hope Goshiwon?”

“Yeah. So try to wake up.”

“Hope… Right. Hope can’t be bought with money. My mom always said it was in everyone’s heart. She makes incredible doenjang stew.”

I waited patiently until he reached the part about doenjang stew, then punched him in the gut.

Even while vomiting, he mumbled Article 1, Clause 12 of the Awakened Persons Special Act, proving that he was, in fact, an exam candidate.

* * *

“I feel gross.”

I went straight to the shower room in the goshiwon and showered for thirty minutes, but I still felt as if the smell of vomit were clinging to the tip of my nose.

When I returned, sniffing all the way, two nuisances were waiting in my room.

“Gwaah…”

One was Jinho, dead drunk, and the other was…

“Oh, I forgot about this.”

The capsule. I’d left the refrigerator-sized thing in my room, barely ten square meters, and it felt as if it had filled the entire space. I retreated onto the bed and began wondering what to do with it.

*Should I take it back where I found it?*

I could hand it over to a scrap dealer instead. What were scrap-metal prices like these days? It weighed at least fifty kilograms, so I could probably get enough for a few snacks.

*I thought it was a fairly useful piece of equipment.*

Shit, huh? Was it really that much of a piece of junk?

Come to think of it, I hadn’t even looked inside. Curiosity got the better of me, and I examined the capsule.

“First, the exterior is… not great.”

The capsule’s surface was yellowed with nicotine or something, and rust seemed to have formed in places. Once I let go of my attachment and took a proper look, I understood what Jinho had meant.

“Is this how you open it?”

I pressed the lone button sticking out, and the lid opened to reveal the interior. I had expected something impressive, but there was nothing much to see after all.

There was only an ergonomically designed chair for extended play and a VR helmet that enclosed the entire head… Huh?

“What’s this? An instruction manual?”

More precisely, it was a small booklet labeled *Product User Manual*.

Did people really leave instruction manuals inside things they were throwing away? Especially in a piece of junk like this?

Curious, I opened to the first page.

> **Product User Manual**
>
> **Product name:** Virtual Reality Interface  
> **Model:** ARK-2020  
> **Manufacturer:** H Soft  
> **Manufacturing date:** January 1, 2020

I skimmed the print without much thought until the manufacturing date stopped me.

January 1, 2020. It had to be a printing error. Surely.

*What kind of lunatic would have made a game machine on that day—no, during that period?*

That period was the Great Cataclysm.

January 1, 2015. Humanity received more than a New Year’s sunrise.

Gates—or dungeons, as they were also called—began appearing all over the world, and monsters no one had ever seen or heard of poured through them.

Monsters and Awakened. War and destruction…

The unreal invaded reality, and the greatest war in Earth’s history ended only with the death of the monsters’ lord, the Demon King Asmodeus.

That day was January 1, 2020. It was known as Victory Day.

*So that’s impossible.*

I clicked my tongue and turned the page.

> **Warning**
>
> - The player cannot log out at will.
> - If the player dies during gameplay, resurrection is impossible.

“Oh. I see.”

I nodded and lay down on the narrow mattress. There were still a few pages left, but who cared?

“I should get some sleep.”

Rather than read an instruction manual written by a lunatic, I might as well sleep. I pushed Jinho into a corner and closed my eyes.

“Gwaah. Gwaah.”

“…”

“Gwaah. Gwaah.”

“…”

Did that capsule have a soundproofing function?

* * *

The chair was hard. It had been made in 2020, so it was the same age as me. A twenty-seven-year-old chair. Its cushion had gone flat long ago.

I took comfort in the fact that it didn’t smell and pulled the blanket up to my neck.

“Gwaah. Gwaah.”

…I even put on the VR helmet.

*Wearing something like this is going to make my neck hurt.*

That minor complaint vanished the moment I put on the helmet. A world of complete silence. A stillness without so much as a whisper of noise.

But instead of sleep, my thoughts began to stir.

*What am I going to do tomorrow?*

Hunters were certainly a highly paid profession, but that depended on your rank.

F-rank Hunters like me were a dime a dozen, and unless you belonged to a Guild, you had to show up at a day-labor agency before dawn.

Being unaffiliated was miserable. Government policy was never kind to unaffiliated Hunters, and the punishing tax rates imposed on Hunters were enough to take your breath away just hearing about them.

*So now I’m one of them.*

Unlike me, my mother and younger sister lived in an apartment in a Safety Sector. It was an extravagant expense for an F-rank Hunter, but nothing mattered more to me than my family’s safety.

Until now, I had barely managed to come up with enough money to renew their jeonse lease each year.[^3] But from now on… who knew?

*Fuck. I don’t know.*

I suddenly thought of my late father.

He had devoted himself to his family and was respected by society, but he died when I was seven.

A monster attack caused by a Gate breach. As an ordinary office worker, he probably never had a chance.

If my father were still by my side, could he have shown his son which way to go?

*I’ve still done my best all this time. Please believe in me.*

Maybe it was the alcohol finally catching up with me. Maybe it was thinking about the past. Without realizing it, I went slack and my eyes began to close.

As I surrendered to the wave of sleep pouring over me, I thought:

*I hope things will be a little better when I open my eyes.*

Someone’s voice pierced my ears, but I didn’t care anymore. I slipped gently into sleep.

> **System**
>
> Player detected. …Unregistered player. Register as a new player?
>
> No response for an extended period. Proceeding automatically.
>
> 1%… 27%… 94%… Complete.
>
> Player Jin Taekyung registered to the device.
>
> Proceeding to selection. Would you like to log in to Murim?
>
> No response for an extended period. Proceeding automatically.
> …May fortune favor you in battle!

[^1]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement, often with shared facilities.
[^2]: Doenjang is a fermented Korean soybean paste commonly used as the base of a savory stew.
[^3]: A Korean jeonse lease is secured by a large refundable deposit in place of monthly rent.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 1`.
