# Master Edit Task — Chapter 13

# Master Editorial Brief

You are the final English-language editor of an existing Korean-to-English novel translation.

The Korean source is the authority for meaning. The existing English is the baseline you are editing, not a draft to discard. Your task is to make the chapter read like professionally written native English commercial fiction while preserving the author's exact story, characterization, humor, register, pacing, ambiguity, and cultural texture.

## Editorial authority

You may freely recast sentences and paragraphs when the English is stiff, literal, repetitive for accidental reasons, awkwardly collocated, over-explained, or syntactically shaped by Korean. You may tighten dialogue, improve rhythm, repair transitions, and make action easier to follow. A technically correct sentence may still need rewriting if a fluent English novelist would not naturally phrase it that way.

Do not change text merely to make it different. If the baseline is already strong, leave it alone.

The accepted baseline is also the project's style and terminology anchor. Do not
replace an established rendering, cultural term, System label, Markdown form, or
recurring phrase with a synonym merely because the synonym sounds smoother.
Make that change only when the Korean source, `RULES.md`, or the exact glossary
requires it. In particular, do not turn a source-specific image into a nearby
English image, or change a gold-spoon joke, item name, technique name, or UI
label into a different expression without source support.

## Fidelity constraints

Never invent, omit, explain away, generalize, intensify, soften, or reinterpret source-supported content. In particular, preserve:

- exact actions, subjects, objects, directionality, causality, quantities, and physical details;
- deliberate ambiguity, euphemism, implication, profanity level, repetition, and withheld information;
- jokes and comic specificity, even when a more generic English joke would sound smoother;
- hierarchy, kinship, forms of address, characterization, and speaker attitude;
- System mechanics, Murim concepts, names, ranks, techniques, items, organizations, and established terminology.
- chapter-level logical consistency: interpret labels, counters, notifications, and repeated facts from how they behave across the scene, not from an isolated surface gloss;
- idioms by their narrative function rather than their component words, and jokes with their setup, recognition, and punchline timing intact;
- cross-sentence implications: do not create a claim that contradicts “again,” an increasing value, an earlier action, or the explanation immediately around it;
- repeated terminology and formatting: once the baseline or glossary establishes a rendering, keep it consistent throughout the chapter unless the source clearly changes the sense;

Do not add jokes, metaphors, explanations, emotional conclusions, or colorful details that are absent from the Korean. Do not replace a specific source image with a generic equivalent merely because the generic version is smoother.

When natural English and literal form conflict, preserve the source meaning and pragmatic effect while changing the English form as much as necessary.

Before returning the chapter, perform a silent continuity pass: trace every
counter, quantity, repeated System label, item or technique name, joke setup and
payoff, and physical cause-and-effect sequence from the Korean through the
finished English. Correct any local sentence that contradicts the sequence.

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
- Use `qi` for Murim energy and `mana` for the modern Hunter system when the source distinguishes them. Preserve an established chapter-specific rendering such as `internal energy` when the exact glossary and surrounding Korean distinguish accumulated `공력` from resulting `기운`.
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
| 위팽     | **Wipeng**         |
| 혁무진    | **Hyuk Mujin**     |
| 이소군    | **Lee Seogeun**    |
| 월화     | **Wolhwa**         |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 이류     | **Second Rate**   |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 창법     | **spear technique**                              |                                                       |
| 초식     | **form**                                         | Numbered technique movement                           |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 기루     | **pleasure house**                               |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 사형     | **Senior Brother**                           |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 진가보법   | **Jin Family's Manoeuvre Technique**   |
| 진가창법   | **Jin Family's Spear Technique**       |
| 시스템              | **System**                     |
| 상태창              | **Status Window**              |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 칭호               | **Title**                      |
| 로그아웃             | **Logout**                     |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 매력               | **Charm**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 본가      | **our family / this family**                                    |
| 공자      | **Young Master**                                                |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 5–9

## Plot

Taekyung completes the tutorial, learns that Logout requires First Rate, Lv. 30, and 500 Fame, and is taken to the Medicine King Hall after his fight with Hyuk Mujin. He begins cultivating the Jin Family’s Cultivation Technique, pretends that his memory has not returned, and discovers an unused room filled with martial arts manuals. The System reveals that martial arts occupy ten slots, three of which are already filled. Jin Wikyung and Wipeng catch him practicing footwork at night, but accept his explanation. In Chapter 9, Taekyung sorts the manuals, acquires the Jin Family’s Manoeuvre Technique, completes its achievement, and earns the title Novice Trainee. Seeking a proper place to practice, he asks for an empty room. Jin Wikyung instead orders his indefinite confinement in the training hall as a protective measure against the Elder Council’s coming attack. Wipeng secretly explains the plan through Sound Transmission and promises to release him within seven days; Taekyung negotiates that down to three days before being escorted away.

## Continuity

- Taekyung remains trapped in Murim; Logout and death rules remain unresolved.
- Logout requires First Rate, Lv. 30, and 500 Fame.
- He is practicing the Jin Family’s Cultivation Technique and has acquired the Jin Family’s Manoeuvre Technique; he has also located the Jin Family’s Spear Technique.
- His martial arts interface has ten slots, with three already filled.
- Taekyung continues pretending that his memory has not fully returned.
- Jin Wikyung is the Lesser Family Head and Taekyung’s protective older brother; Wipeng is his capable aide and can use Sound Transmission.
- The Elder Council is preparing to challenge Jin Wikyung’s authority by attacking Taekyung’s conduct.
- Taekyung is being held in the training hall for an indefinite period, with Wipeng promising release within three days after their negotiation.

## Translation Decisions

- The hereditary martial art is rendered **Jin Family’s Manoeuvre Technique**, using British spelling consistently with the chapter’s terminology.
- The achievement reward is rendered as the title **Novice Trainee**.
- `음성 전송` is rendered **Sound Transmission**.
- `소가주` is rendered **Lesser Family Head**.
- System messages remain grouped into `> **System**` blockquote windows whenever consecutive.

### Prior accepted reading-copy tails

#### Chapter 11 tail (accepted)

…
it had felt as if tangled threads were being pulled in every direction. This time, it felt as if gears were slipping past each other by a hair. How many times had I tried? Whoosh—Bang! It was a simple thrust. For a moment, I wondered if I had performed all the way through the seventh and final form without realizing it, but it was only one movement from the fifth form. “What was that?” A shiver ran down my spine. For one brief moment, the footwork and spear technique had meshed perfectly. The spear in my hand trembled. > **System** > > - You did not gain Mastery for Jin Family’s Spear Technique. (6 / 100) I shoved the System notification into a corner of my mind and tightened my grip on the spear. Recalling the sensation from a moment ago, I stepped forward. And again. Swish—Whoosh— *This is it.* I felt it the instant I thrust the spear. The footwork and the spear technique. The two gears meshed perfectly. Overwhelmed by indescribable pleasure, I turned those two gears again and again. My steps were fast and precise. The spearhead that thrust, slashed, and swung was fast, precise, and powerful. My dantian grew hot. My internal energy became a ball of fire and seeped into the spear. I had to release it. *Right now!* “Hah!” The Sky-Piercing Strike—the final blow of the Jin Family’s Spear Technique, said to pierce the heavens—shot forward. A deep, muffled boom erupted through the cavern. Bang! Dust rose, and stones scattered in every direction. The spear embedded in the training hall’s wall trembled. A massive hole had formed around the spearhead, which had plunged so deeply that it was no longer visible. A hole? No. This was a crater. The sight was breathtaking. “Huff, huff…” The exhilaration sent a shiver down my spine. *Fuck, it was me. I did it!* I had unleashed that insane strike—the kind that could take down a troll in one blow. Me! I staggered. *Huh?* I needed to shout my head off and take a proof photo. I needed to put Big Brother Jinho in his place—he used to call me a freeloader. *Oh, right. This was a game.* My vision blurred. The strength drained from my body. An unbearable wave of sleepiness washed over me. *I’m sleepy.* I stopped thinking and surrendered my body to instinct. A familiar sound gradually faded into the distance. Ding. Ding. Ding. . . . > **System** > > - All internal energy has been depleted. > > - You feel extreme fatigue. > > - You have completed the achievement **Unity of Self and Object**. A reward will be granted! > > - You have realized the connection between martial arts on your own. As a reward, the realms of your martial arts will rise substantially. > > - The realm of **Jin Family’s Cultivation Technique**… > > - The realm of **Jin Family’s Manoeuvre Technique**… > > - The realm of **Jin Family’s Spear Technique**… > > - Level up! > > - Level up! * * * > **System** > > - Sleep mode has ended. I opened my eyes. The cave ceiling, with stalactites hanging from it, came into view. *The training hall.* How long had I been unconscious? Half a day? Or a full day? I didn’t know. What mattered was that I was still in the game and had gotten plenty of rest. *I feel great, too.* My physical condition was strangely excellent. Come to think of it, I seemed to have heard System notifications just before I passed out. “Open Message Window.” The next moment, unread messages covered my vision. By the time I finished reading them all and sorting through my thoughts, more than ten minutes had passed. I muttered a brief reaction. “I really hit the jackpot.” The Jin Family’s Manoeuvre Technique and Spear Technique had risen all the way to the Third Stage—two whole stages. The Jin Family’s Cultivation Technique had reached the Second Stage. And on top of that… “I went up two Levels?” I was happy, but also bewildered. I hadn’t seriously expected to Level up in the training hall. “Don’t you usually Level up by completing Quests or killing monsters?” Apparently, learning martial arts and gaining insight like I had could also lead to a Level Up. Was it because this was a martial-arts game? It was definitely impossible to predict. “No wonder my body felt so light.” The Level Up effect must have restored my condition. The bruises and slight pain that had remained before I leveled up had vanished completely. “Open Status Window.” The Status Window had changed too. Reaching Level 13 had given me twenty remaining points, and the effects of training had slightly increased my Strength, Stamina, and Agility. “Level 13…” The Quest completion requirements were reaching the first-rate realm, Level 30, and 500 Fame. I wasn’t progressing quickly, but I was steadily leveling up through training alone. That meant I was cruising along. *Once I leave the training hall, I can spread my sails and surge forward.* I smiled contentedly and distributed my points. Now, all that remained was to check the reward I’d received for completing the Unity of Self and Object achievement. “Open Inventory.” > **System** > > - You have 1 new Item. Would you like to check it? Yeah. Give it here.

#### Chapter 12 tail (accepted)

…
were the words he had used when he toyed with me last time. He was nothing more than an illusion I had created, but… *God, that’s pissing me off.* *If you’re so confident, stop dodging and come at me.* Hyuk Mujin picked up on my thought and rushed at me in a smooth glide. But this was a fight between a spear and a fist. If I let him land that attack, it would mean I had spent the last seven years digging holes for nothing. “Where do you think you’re going!” Whoom— I swung the spear shaft. If the illusion had been real, it would have made a solid *thwack*. Even if he had dodged it, he would have failed to close the distance. *Let’s see how far you can dodge.* I launched into the form. Faced with the torrent of attacks, Hyuk Mujin didn’t even dare to approach. He retreated step after step. Combat had a flow. I had caught that flow, and Hyuk Mujin had been swept along by it. Looking at Hyuk Mujin rolling across the ground with an exhausted expression, I thought, *He’s weak.* I could see his movements. The Hyuk Mujin projected here was a fist fighter. I could tell how he would move by watching his feet, and I could predict his next action. His fists couldn’t reach me. Ssshk-swish-swish! In a single instant, I thrust three times in succession. It was an attack F-rank Hunter Jin Taekyung couldn’t perform. But Jin Taekyung the Murim martial artist, drawing on internal energy, could. “Kraaagh!” Hyuk Mujin seemed to scream as the spear pierced his chest. Without hesitation, I shoved the spear deeper and twisted it. The spearhead crushed through his breastbone and split his heart. The fallen Hyuk Mujin slowly faded away. “Ah. This is way too easy.” The fight had already been decided in less than five seconds. I had even held the upper hand throughout the entire battle, only for it to end anticlimactically. *Was half just too weak?* I fell into thought while recovering the internal energy I had depleted by circulating qi. Hyuk Mujin was Level 20 and a martial artist who had trained in martial arts for at least several years. There was no way he could be this weak. *All right. Again.* I stood up with the spear in my hand and closed my eyes, imagining a new Hyuk Mujin. A height of 180 centimeters. Lean muscles and insolent eyes. I infused him with the movements I had seen back then. When I opened my eyes, an illusion exactly as I had imagined stood before me. But it still wasn’t over. Hyuk Mujin had to be stronger. *Your physical abilities are superior to mine.* After I fed in a few more conditions, Hyuk Mujin’s illusion smiled pleasantly. He had become much faster and gained stamina that would never run out. “Yeah. Now this is worth fighting.” Those words were the starting signal. I thrust my spear at Hyuk Mujin as he charged toward me like a ray of light. Ssshk-swish! * * * Vroooom. Boom! The spearhead tore through the air. The air burst with the sound of a swarm of bees, bringing a gust of wind with it. It was the final form of the Jin Family’s Spear Technique: Sky-Piercing Strike. “Kheugh…” Hyuk Mujin’s illusion looked down at his gaping chest. His eyes held pure disbelief. Then his knees buckled, and the illusion scattered. “This isn’t right.” I scratched my head roughly as I heard the message that my Mastery of the Jin Family’s Spear Technique had increased. *Why am I still winning?* Had the System made a mistake, or… *Did I simply become stronger?* I brushed the thought away as soon as it came to me. That couldn’t be it. I wasn’t some peerless genius. I had only learned a couple of martial arts. *At this rate, this isn’t very useful.* This was supposed to be a simulation for testing what happened when I fought a powerful opponent. If I kept winning, what was the point? If I at least knew which martial arts Hyuk Mujin had learned, I could draw out their power. But wait. “There’s an easier way.” The Jin Family’s Manoeuvre Technique and Spear Technique. What if I grafted those two onto the Level 20 Hyuk Mujin? I might even be able to identify their strengths and weaknesses from a third-party perspective. Yeah. That would be better. “You think so too, right?” Hyuk Mujin’s illusion had reappeared at some point. It grinned and nodded. “Then let’s fight again.” I raised the spear diagonally and took one step forward with my left foot. The illusion assumed the same stance as if it were looking in a mirror. “You’ll regret this.” “Regret, my ass.” I was even talking to an illusion now. Anyone who saw me would have no choice but to call me a certifiable lunatic. “Crazy bastard.” …It was my imagination, but it still pissed me off. “You’re dead.” Without hesitation, I pointed the spear at him. Same weapon. Same martial arts. It looked like it would be an interesting fight. “Interesting? You really are a lunatic.” Yeah. I suppose so. Finding this fun in a situation like this meant I was pretty damn crazy, too. [^1]: A goshiwon is cheap boarding made up of tiny private rooms, often rented by exam students.

## Korean source

```text
＃13화



다섯 마리의 말은 힘차게 달렸다. 산과 들, 강을 지나 마침내 목적지에 도착했을 때는 정오 무렵이었다.

“어디에서 오셨습니까?”

태원진가 수문위사의 긴장 섞인 물음에 선두의 청년이 웃었다. 비뚜름하게 올라간 입술에는 감출 수 없는 적의가 배어 있었다.

“항산(恒山).”

진위경이 가문 중진들을 소집한 것은 일 다경 후였다.



* * *



혁무진은 변화무쌍했다. 나는 그저 머릿속에 녀석의 모습을 그려 넣으면 되었다. 창, 검, 도, 활……. 이길 때도, 질 때도 있었지만 한 가지는 확실했다.

“이제 감 잡았다.”

무공이 몸에 익었다. 처음에는 처음부터 끝까지 차례차례 풀어내는 것에 집중했지만 이제는 다르다.

상황에 따라 초식도 변한다. 꼭 초식 하나하나가 순서대로 이어져야만 무공인 건 아니다. 지금의 나는 초식의 순서를 뛰어넘어 무공을 연계할 수 있을 정도의 수준이 됐다.

‘지금처럼 말이지.’

쐐애애액!

바람 소리가 들렸을 때는 이미 늦었다. 복부를 꿰뚫린 혁무진이 탄식했다.

- 실력이 빨리도 느는군.

“창질만 7년을 했다. 이 새끼야.”

눈을 감았다 뜨니 텅 빈 수련동이 보인다. 내 승리를 축하하듯 시스템 알림이 울렸다.

띠링.



- [진가창법]이 사 성으로 올랐습니다!

- [진가보법]이 사 성으로 올랐습니다!

- 초식이 정교해지고 파괴력이 상승합니다.

- 레벨 업!



“이제 14레벨인가?”

사흘 만에 3레벨을 올렸다.

수련동에서 사흘을 짱박혀 있던 것치고는 가파른 상승세다.

거기에 진가심법은 삼 성, 보법과 창법은 사 성에 도달했다.

“상태창 오픈.”

잔여 포인트를 분배하고 나자 어쩐지 코끝이 찡하다.



상태창



[Lv.14 진태경]

직업 : 이류 무인

명성 : 10

칭호 : 3개 (칭호 효과 적용 중)

- 명가의 자제 (모든 능력치 +5, 명성 +50)

- 가문의 수치 (모든 능력치 –5, 명성 –50)

- 초보 수련자 (수련 속도 +10%)

근력 : 51체력 : 61

민첩 : 61 지력 : 10

매력 : 10 공력 : 10년

잔여 포인트 : 0





“아름답다. 아름다워.”

이 균형 잡힌 능력치를 보라.

이게 바로 전투의, 전투에 의한, 전투를 위한 능력치다.

‘거기에 무공까지.’

그때의 내가 아니다. 혁무진? 붙어도 이길 자신 있다.

무공의 무자도 모르는 F급 헌터는 죽었다. 지금의 나는 절정 심법에 일류 무공을 두 개나 익힌 무림인이다.

‘오늘부터 시작이야.’

모든 준비는 끝났다. 오늘, 수련동에서 나가게 되면 생각해 둔 물건들을 챙겨 태원진가를 빠져나갈 것이다.

‘진위경의 도움을 받을 수도 있겠지.’

천력부 같은 얼뜨기 산적들만 처리해도 빠른 속도로 목표치에 도달할 수 있을 것이다. 길어 봤자 이틀. 그 후에는 따뜻한 가족의 품으로 돌아갈 수 있다.

‘엄마, 하연아. 보고 싶다.’

눈시울이 붉어지려던 그때였다.

그그긍-

“오, 오오오!”

기다리던 순간이다. 수련동 입구를 막은 철문이 열리고 있었다. 그 거무튀튀하고 무거운 쇳덩어리가, 천국의 문처럼 아름답게 보였다.

“드디어! 나간다!”

나는 환희에 찬 얼굴로 천국 입구를 향해 달려 나갔다.

날 이곳에서 꺼내 줄 천사가 문 뒤에서 모습을 드러냈다.

“삼공자. 사흘 만이군요.”

반가운 얼굴은 아니지만 지금은 마냥 기쁘다.

“저 꺼내 주시려고 오신 거죠? 예? 맞죠?”

사막여우를 닮은 천사, 위팽이 미묘한 말투로 대답했다.

“예. 일단은요.”

“……?”

“나가긴 할 겁니다. 하지만 바로 들러야 할 곳이 있습니다.”

“들러야 할 곳?”

순간 등줄기가 오싹하다. 왠지 모를 생존 본능이 고개를 쳐들었다.

“어딜 가는데요?”

“대회의장입니다. 소가주님께서도 그곳에서 기다리고 계십니다. 그리고…….”

위팽이 덧붙였다.

“본가의 중진들과 항산검문의 사자(使者)도 와 있지요.”

“항산검문이요? 걔네가 여길 왜 와요?”

홍화루에서 월화가 그랬었다. 태원진가와 항산검문은 숙적관계라고. 그런데 그놈들이 왜 여기 있어?

‘일이 잘못 돌아가고 있다.’

불길하다. 불길해. 어떻게든 방법을 찾아야 한다.

“저 그럼 잠깐 처소에서 옷만 갈아입고 가면 안 될까요?”

“안 됩니다.”

“중요한 자리인 것 같은데 냄새나면 안 되니까…….”

“도망칠 생각이십니까?”

생긴 건 사막여운데 눈치는 미어캣 저리 가라다. 내가 뭐라 할 새도 없이 위팽의 손이 어깨를 짓눌렀다.

“삼공자. 지금부터 제가 묻는 말에 사실대로 대답해 주십시오. 아시겠습니까?”

목소리는 건조하고 눈동자는 서늘하다. 그에게서 느껴지는 기세에 입을 뗄 수 없었다. 내가 할 수 있는 것이라곤 고개를 끄덕이는 것뿐이었다.

‘진태경.’

순간 머릿속에 떠오른 세 글자.

확실했다. 분명히 이 새끼다. 나도 모르는 똥을 싸질러 놓은 거다.

그리고…….

“항산검문의 여식을 범하려 한 것이 사실입니까?”

그 똥은 상상 이상으로 거대했다.



* * *



위팽을 따라 대회의장으로 향하는 길, 머릿속이 온통 백지장이었다.

‘성폭행 미수?’

미수에 그쳤다고는 하나, 때려죽여도 시원찮을 성범죄다.

한 사람의 인간으로서, 여동생을 둔 오빠로서 성범죄자는 사형시켜야 한다고 입버릇처럼 말하던 기억이 떠올랐다.

‘이런 미친 새끼.’

손바닥이 식은땀으로 축축하다. 나는 몇 번째인지 모를 말을 내뱉었다.

“저 진짜 아닙니다. 믿어 주세요.”

위팽은 뒤도 돌아보지 않고 대답했다.

“기억이 돌아오셨습니까?”

“아니, 그게 아니고요. 저 진짜 아니라니까요. 제가 그럴 놈으로 보이세요? 그런 쓰레기 짓을 하고 다닐 정도로?”

“예.”

아니, 시발.

숨도 안 쉬고 대답하네.

“저기요. 그럼 저 화장실, 아니 변소 좀 들렀다 갈게요.”

“안 됩니다.”

“아니, 볼일은 보게 해 줘야지!”

“그냥 싸십시오.”

이런 개새끼. 나는 포기하고 곧장 뒤돌아 뛰기 시작했다. 모든 공력을 끌어올려 발에 집중시켰고.

덥석.

“삼공자.”

세 걸음 만에 붙잡혔다. 내 목덜미를 움켜쥔 위팽이 서늘한 눈동자로 나를 내려다봤다.

“계속 이러시면…… 제가 무례해질지도 모릅니다.”

저항은 무의미하다. 위팽은 [기감]으로도 레벨을 파악할 수 없는 고수다.

‘어쩔 수 없다.’

참담한 마음으로 얼마나 걸었을까, 우뚝 선 전각이 눈에 들어왔다.

앞에는 무사 여럿이 경계를 서는 중이었는데, 태원진가 특유의 남색 복장은 눈에 익었지만 몇 명은 처음 보는 붉은 색 옷을 걸치고 있었다.

‘저놈들이 항산검문이구나.’

양 문파의 평소 관계를 생각해 보면 견원지간일 텐데, 지금은 한마음 한뜻으로 나를 노려보는 중이다.

“시발…….”

내 중얼거림을 들은 위팽이 고개를 돌렸다.

“소가주께서는 삼공자를 믿고 계십니다. 그 사실을 잊지 마십시오.”

그래. 진위경이 있다. 내 가장 큰 희망이자 방패.

그 사실을 되새길 때, 위팽이 대회의장의 문을 열어젖혔다.

“삼공자를 데려왔습니다.”

크게 심호흡한 나는 전각으로 발을 디뎠다. 속으로는 끊임없이 되뇌는 중이었다.

‘호랑이한테 물려 가도 정신만 차리면 산다. 호랑이한테 물려 가도 정신만 차리면…….’

내가 회의장 안으로 들어서자 낮게 웅성거리던 목소리가 뚝, 끊겼다. 젊고 늙은 남자 십여 명이 좌우로 도열해 있고 상석에는 진위경이 자리했다.

그리고 중앙의 한 청년.

“오랜만이오. 진 공자.”

그 꺼림칙한 미소와 마주한 순간이었다.

띠링.



- [살기]를 감지했습니다!



……깜빡이 좀 켜고 들어와라.



* * *



살기.

익숙하다. 몬스터들은 말 그대로 악의와 살기로 똘똘 뭉친 녀석들이니까. 수도 없이 느껴 왔고, 이제는 익숙하다고 생각했다. 그런데 이놈은…….

‘달라.’

내가 겪어 온 그것과는 차원이 다르다.

굳이 비교하자면 하급 몬스터와 중급 몬스터의 차이라고 하겠다. 훨씬 다듬어져 있고, 은밀하며 소름 끼친다.

“지난번 저잣거리에서 스치듯이 본 적이 있었는데. 기억할지 모르겠소.”

한 마디, 한 마디. 씹어뱉는 이소군의 머리 위로 시스템창이 둥둥 떠다닌다.



[Lv.30 이소군]



앞서 살기를 감지하자마자 [기감]으로 읽어 낸 녀석의 레벨이었다. 내 레벨의 두 배가 넘어간다.

‘미치겠네.’

더 서글픈 것은 다른 사람들의 눈초리다.

젊은 사람, 늙은 사람 가릴 것 없이 흉험한 눈빛 수십 개가 나를 노려보는 광경에 오금이 저려 온다. 그런 분위기 속에서 이소군이 입을 열었다.

“아쉽구려. 조금만 일찍 왔다면 더 깊은 대화를 나눠 볼 수 있었을 터인데. 방금까지 흥미로운 이야기를 하고 있던 참이어서 말이오.”

“……그래요?”

“무슨 이야기인지 궁금하지 않소?”

“괘, 괜찮습니다.”

목을 자를까, 불알을 자를까에 관한 토론이 아니길 바랄 뿐이다. 그리고 만약 이 불행한 짐작이 사실이라면, 목 대신 불알이 잘렸으면 했다.

‘잘만 하면 레벨 업으로 회복할 수 있…… 내가 이런 것까지 생각해야 하나.’

참담할 뿐이다. 그런 내 표정을 지그시 바라보던 이소군이 말했다.

“며칠 전 가문에 돌아왔다 들었소만. 어디 있었소?”

“홍화루요.”

“그럼 홍화루에 가기 전에는 어디 있었소?”

‘고시원에 있었다. 임마.’

나도 솔직하게 다 털어놓고 싶다. 그날 저는 길드에서 잘리고, 고시원 형이랑 소주 한잔 걸친 다음에 캡슐에 들어가서 잤습니다. 눈 떠 보니까 홍화루였고, 로그아웃을 목표로 열심히 하고 있습니다. 뭐, 이렇게.

‘칼이나 안 뽑으면 다행이지.’

대답을 못 하고 머뭇거릴 때 이소군이 품에서 뭔가를 꺼내 들었다. 정말 칼이라도 뽑나 싶었는데, 웬 종이 뭉치다.

“기억을 못 하는 것 같으니 내 알려 주겠소. 홍화루에 가기 전날 밤, 공자는 명월루에 들렀소. 예약해 두었던 특급 객실로 향했지.”

“명월루요?”

“한때 뻔질나게 드나들던 기루 아니오? 처음 들어 봤다고 변명하진 마시오. 그날 명월루에서 당신을 목격한 사람들의 증언과 수결이 여기 있으니.”

말하자면 증언 목록인 셈이다. 나는 어디 한번 읽어나 보자 하는 심정으로 종이를 읽어 내렸다.

그리고 이상한 점을 발견했다.

“뭐야, 이거?”

“직접 보고도 모르겠나?”

이 자식이 은근슬쩍 말 놓네.

“보니까 하는 소리지. 제대로 된 증언이 없잖아요.”

수십 명의 증언을 빠짐없이 읽어 봤지만 결정적인 증언은 어디에도 없었다.

하는 말도 비슷비슷하다. 진태경이 거나하게 취해서 방을 잘못 찾았고, 그 방의 주인이 항산검문의 여식이었다는 것. 그리고 비명을 지르는 소리가 났다는 것.

“내 누이의 옷을 찢고 범하려 한 놈이 뻔뻔하기 그지없구나. 과연 소문 그대로야.”

“아니, 그게 아니고…….”

“이놈!”

촤르륵!

“아.”

얼굴을 때린 종이 뭉치가 바닥에 흩어졌다. 이소군이 그 위로 가래를 탁 뱉었다.

‘이 새끼 봐라.’

짜증이 아니다. 그저 의심이 들 뿐이다.

뭐라 할까, 이런 일련의 상황들. 특히 증언에 관련해서 굉장히 작위적인 느낌이 든다고나 할까?

하지만 더 이상 찝찝함을 느낄 새도 없었다.

“따라 나와라, 네놈이 저지른 짓의 대가를 치르게 해 주마!”

이소군이 고함을 내지른 그 순간이었다.

띠링.



- [비무] 퀘스트가 생성되었습니다.



이건 또 뭐야.
```

## Current accepted English baseline

```markdown
# Chapter 13

The five horses ran hard. They passed mountains, fields, and rivers, finally reaching their destination around noon.

“Where are you coming from?”

When the Jin Family of Taiyuan’s gate guard asked the tense question, the young man in the lead smiled. Hostility he could not hide seeped from his crooked, lifted lips.

“Mount Heng.”

Jin Wikyung summoned the family’s senior members fifteen minutes later.

* * *

Hyuk Mujin could take on any form. All I had to do was picture him in my mind. Spear, sword, saber, bow… There were times I won and times I lost, but one thing was certain.

“I’ve got the hang of it now.”

The martial arts had become second nature. At first, I had focused on executing them from beginning to end, one form after another. But things were different now.

The forms changed depending on the situation. Martial arts didn’t have to consist of one form flowing into the next in a fixed order. I had reached the point where I could skip the prescribed sequence and link forms together.

*Like this.*

Whoooosh!

By the time I heard the wind, it was already too late. Hyuk Mujin, his abdomen pierced through, let out a rueful sigh.

- You’re improving quickly.

“I trained with a spear for seven years, you bastard.”

When I opened my eyes again, the empty training hall came into view. As if celebrating my victory, the System notification rang out.

Ding.

> **System**
>
> - **Jin Family’s Spear Technique** has risen to the Fourth Stage!
>
> - **Jin Family’s Manoeuvre Technique** has risen to the Fourth Stage!
>
> - The forms have become more refined, and destructive power has increased.
>
> - Level up!

“So I’m Level 14 now?”

I had gained three Levels in three days.

That was a steep rise for someone who had holed up in the training hall for three days.

On top of that, the Jin Family’s Cultivation Technique had reached the Third Stage, while the Manoeuvre Technique and Spear Technique had reached the Fourth Stage.

“Open Status Window.”

After distributing my remaining points, I felt a sting at the tip of my nose for some reason.

> **System**
>
> **Status Window**
>
> **Lv. 14 Jin Taekyung**
>
> **Occupation:** Second Rate Martial Artist
>
> **Fame:** 10
>
> **Titles:** 3 (Title effects active)
>
> - **Child of a Prestigious Family:** All stats +5, Fame +50
>
> - **Shame of the Family:** All stats –5, Fame –50
>
> - **Novice Trainee:** Training speed +10%
>
> **Strength:** 51  
> **Stamina:** 61
>
> **Agility:** 61  
> **Intelligence:** 10
>
> **Charm:** 10  
> **Internal Energy:** 10 years
>
> **Remaining Points:** 0

“Beautiful. Just beautiful.”

Look at those perfectly balanced stats.

These were stats *of* combat, *by* combat, and *for* combat.

*And that’s not even counting the martial arts.*

I wasn’t the same person I had been back then. Hyuk Mujin? I was confident I could beat him now.

The F-rank Hunter Jin Taekyung, who didn’t know the first thing about martial arts, was dead. I was now a Murim martial artist who had learned a Peak cultivation technique and two first-rate martial arts.

*It starts today.*

Everything was ready. Once I left the training hall today, I would gather the things I had in mind and leave the Jin Family of Taiyuan.

*I might even be able to get Jin Wikyung’s help.*

I could reach my target quickly just by dealing with idiot bandits like the Heavenly Axe. Two days at most. After that, I could return to my warm family.

*Mom. Hayeon. I miss you.*

That was when the rims of my eyes started to go red.

Grrrrrr—

“O-oh! Ohhh!”

This was the moment I had been waiting for. The iron door blocking the entrance to the training hall was opening. That ugly, heavy chunk of metal looked as beautiful as the gates of heaven.

“Finally! I’m getting out!”

I ran toward the entrance to heaven with a face full of joy.

The angel who would free me from this place appeared behind the door.

“Third Young Master. It’s been three days.”

He wasn’t exactly a welcome sight, but I was too happy to care.

“You came to let me out, right? Huh? You did, right?”

Wipeng, an angel who resembled a desert fox, answered in a strangely qualified tone.

“Yes. For now.”

“…What?”

“You will be leaving. But there’s somewhere we need to stop by first.”

“Somewhere we need to stop by?”

A chill ran down my spine. Some kind of survival instinct raised its head.

“Where are we going?”

“The main assembly hall. The Lesser Family Head is waiting there as well. And…”

Wipeng added,

“Senior members of our family and an envoy from the Mount Heng Sword Sect have also arrived.”

“The Mount Heng Sword Sect? Why the hell are they here?”

Wolhwa had told me at Honghwaru. The Jin Family of Taiyuan and the Mount Heng Sword Sect were sworn enemies. So why were those bastards here?

*Things are going wrong.*

This was ominous. Very ominous. I had to find some kind of way out of this.

“Then could I stop by my residence and change clothes first?”

“No.”

“It seems like an important occasion, and I can’t show up smelling like this…”

“Are you thinking of running away?”

He looked like a desert fox, but his instincts put a meerkat to shame. Before I could say anything, Wipeng’s hand pressed down hard on my shoulder.

“Third Young Master. From now on, answer my questions truthfully. Understood?”

His voice was dry, and his eyes were cold. The aura coming from him made it impossible for me to open my mouth. All I could do was nod.

*Jin Taekyung.*

The three-syllable name flashed through my mind.

There was no doubt about it. This bastard was responsible. He had dumped a load of shit without me even knowing.

And then…

“Is it true that you tried to rape the daughter of the Mount Heng Sword Sect?”

That shit was far bigger than I could have imagined.

* * *

On the way to the main assembly hall behind Wipeng, my mind was completely blank.

*Attempted rape?*

Even if it had ended at an attempt, it was a sex crime so vile that beating the culprit to death wouldn’t have been enough.

I remembered how I had always said that, as a human being and an older brother with a younger sister, sex offenders should be executed.

*What kind of fucking lunatic was he?*

My palms were damp with cold sweat. I said it again, not knowing how many times I had repeated it already.

“I really wasn’t the one. Please believe me.”

Without turning around, Wipeng replied,

“Has your memory returned?”

“No, that’s not what I mean. I’m telling you, it really wasn’t me. Do I look like the kind of guy who’d do that? The kind of guy who’d go around committing trash like that?”

“Yes.”

No, fuck.

He answered without even taking a breath.

“Look, then let me stop by the bathroom. Or the privy, I mean.”

“No.”

“You have to let me take care of business!”

“Just go here.”

Son of a bitch. I gave up and immediately turned around and ran, drawing up all my internal energy and concentrating it in my feet.

Grab.

“Third Young Master.”

I was caught in three steps. Wipeng had me by the back of the neck, looking down at me with cold eyes.

“If you keep this up… I might have to stop being polite.”

Resistance was pointless. Wipeng was a master whose Level I couldn’t determine even with Qi Sense.

*No choice.*

With a sinking heart, I walked for who knew how long before a tall pavilion came into view.

Several warriors were standing guard outside. I recognized the Jin Family of Taiyuan’s distinctive navy uniforms, but some of the men wore red clothes I had never seen before.

*Those must be members of the Mount Heng Sword Sect.*

Considering the usual relationship between the two sects, they should have been sworn enemies. Yet right now, they were united in glaring at me.

“Fuck…”

Wipeng turned his head at my mutter.

“The Lesser Family Head believes in you. Don’t forget that.”

Right. Jin Wikyung was there. My greatest hope and my shield.

As I reminded myself of that fact, Wipeng threw open the doors to the main assembly hall.

“I’ve brought the Third Young Master.”

I took a deep breath and stepped into the pavilion. Inside my head, I kept repeating the same words.

*Even if a tiger carries you off, you can survive if you keep your wits about you. Even if a tiger carries you off, you can keep your wits—*

The moment I entered the hall, the low murmuring abruptly stopped. A dozen men, young and old, stood arrayed along either side, while Jin Wikyung occupied the seat of honor.

And in the center stood a young man.

“It’s been a while, Young Master Jin.”

The instant I met that unpleasant smile—

Ding.

> **System**
>
> - **Killing intent** detected!

…At least use your blinker before pulling in.

* * *

Killing intent.

I knew it well. Monsters were literally bundles of malice and killing intent. I had felt it countless times and thought I had grown used to it.

But this guy…

*He was different.*

This was on an entirely different level from anything I had experienced.

If I had to compare it to something, it was like the difference between a low-level monster and a mid-level monster. His killing intent was far more refined, more furtive, and more chilling.

“I believe I caught a glimpse of you in the marketplace last time. I don’t know whether you’ll remember me.”

Each word was spat out by Lee Seogeun. Above his head, a System window floated in the air.

> **System**
>
> **Lv. 30 Lee Seogeun**

That was the Level I had seen with Qi Sense the instant I detected his killing intent. It was more than twice my Level.

*This is insane.*

Even worse were the looks from everyone else.

Dozens of sinister gazes, young and old alike, were fixed on me. My knees began to tremble. In that atmosphere, Lee Seogeun opened his mouth.

“What a shame. If you had come a little earlier, we could have had a deeper conversation. We were discussing something interesting until just now.”

“…Were you?”

“Wouldn’t you like to know what we were discussing?”

“N-no, I’m fine.”

I only hoped it wasn’t a discussion about whether to cut off my head or my balls. And if that miserable guess was correct, I preferred them to cut off my balls instead of my head.

*I might be able to recover with a Level Up if they did that… Why am I even thinking about this?*

It was simply miserable. Lee Seogeun studied my expression before speaking again.

“I heard you returned to the family a few days ago. Where have you been?”

“Honghwaru.”

“Then where were you before you went to Honghwaru?”

*I was at a goshiwon, you bastard.*

I wanted to tell him everything honestly.

*I got fired from my Guild that day, had a glass of soju with the hyung from the goshiwon, then went into the capsule and fell asleep. When I woke up, I was at Honghwaru, and now I’m working hard toward Logout. Something like that.*

*It’d be a miracle if he didn’t draw his sword.*

As I hesitated, unable to answer, Lee Seogeun pulled something from inside his robes. I thought he really was drawing a sword, but it turned out to be a bundle of papers.

“Since you don’t seem to remember, I’ll tell you. The night before you went to Honghwaru, you visited Myeongwollu. You went to the top-tier room you had reserved.”

“Myeongwollu?”

“The pleasure house you used to visit all the time? Don’t try to make excuses by saying you’ve never heard of it. These are the testimonies and seals of the people who saw you there that day.”

In other words, it was a list of witness statements. I read through the papers, thinking I might as well take a look.

Then I noticed something strange.

“What is this?”

“You don’t know even after seeing it yourself?”

This bastard was dropping the formal speech now, too.

“I’m saying that because I read it. There isn’t a single proper testimony here.”

I read every one of the dozens of statements, but there wasn’t a decisive testimony anywhere.

They all said roughly the same thing: Jin Taekyung had gotten thoroughly drunk, gone to the wrong room, and found that the room belonged to the daughter of the Mount Heng Sword Sect. Then someone had heard screaming.

“The bastard who tore my sister’s clothes and tried to rape her is shameless beyond belief. You really are exactly as the rumors say.”

“No, that’s not what—”

“You bastard!”

Flutter!

“Ah.”

The bundle of papers smacked me in the face and scattered across the floor. Lee Seogeun spat a wad of phlegm onto them.

*Well, look at this asshole.*

It wasn’t irritation. I was simply suspicious.

How should I put it? This whole chain of events—especially the testimonies—felt incredibly contrived.

But I had no time to dwell on that unease.

“Come out with me, you bastard! I’ll make you pay for what you’ve done!”

The instant Lee Seogeun shouted—

Ding.

> **System**
>
> - The **Duel** Quest has been generated.

What’s this now?
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 13`.
