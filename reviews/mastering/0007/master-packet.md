# Master Edit Task — Chapter 7

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
| 혁무진    | **Hyuk Mujin**     |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 태원진가   | **Jin Family of Taiyuan**        |
| 이류     | **Second Rate**   |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 시스템              | **System**                     |
| 상태창              | **Status Window**              |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 명성               | **Fame**                       |
| 칭호               | **Title**                      |
| 로그아웃             | **Logout**                     |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 지능               | **Intelligence**               |
| 매력               | **Charm**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 태원     | **Taiyuan**            |
| 공자      | **Young Master**                                                |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |

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

#### Chapter 5 tail (verified mastered)

…
Family’s Cultivation Technique greatly increases stability. I had never missed my family as much as I did then. My beloved mother. My adorable little sister…or rather, my pain-in-the-ass little sister, Hayeon. *When I get out, your big brother will buy you enough fried chicken to make your stomach burst.* *If I ever get out.* > **System** > > The Qi Circulation Helper will run for the first session only. This wasn’t a case of stabbing someone and then applying medicine to the wound… > **System** > > Would you like to skip the Helper System? > > Accept / Decline I fixed my trembling gaze on the message window. “D-Decline.” > **System** > > Continuing. *That was a coincidence, right? Yeah. It had to be.* Before my uneasy feeling had even faded, my vision flipped upside down. And when I came to, I was in an unfamiliar gray space. “Over here.” I whipped my head around in surprise and saw an old man beckoning me. *If an old man who looked like that called me over in a dream, I’d turn around and run for my life. But this was a game.* *So he’s the helper.* Even if I hadn’t reasoned it out, I would have followed him without much suspicion. It was strange, even to me, but that was how I felt. An inexplicable sense of familiarity. And trust. “Take the most comfortable position.” *Huh? Aren’t you supposed to sit cross-legged when circulating qi?* As if he had read my thoughts, the old man answered. “Weaklings fuss over things like that. Masters don’t need to.” I could smell it in his calm voice. I could smell it. *This was the scent of a master. The real deal had finally appeared!* “Good grief. What a handful.” His wrinkled hand seemed to reach toward me, then vanished in a blur. Huh? Tap. Tap-tap. Something flashed past, and the next moment, I was frozen stiff. *Was this what it felt like to be a corpse with its eyes still open?* I couldn’t move a muscle. “It’s only a simple acupoint-sealing technique, so don’t be alarmed. Focus from this point on.” As he spoke, the old man placed a hand on my back. Then he rapidly rattled off words in a low voice. “Circulating qi is the most important training for a martial artist. It not only allows you to accumulate internal energy, but also refines essence, qi, and spirit, enabling you to advance to a higher realm. Therefore…” I listened closely, but I couldn’t understand a word of what came after that. I only understood that circulating qi was extremely important. “Clear your mind like a stream, maintain your focus, and draw out the flow. Now I will recite the formula of the Jin Family’s Cultivation Technique.” Without giving me time to stop him, he rattled off the formula at breakneck speed—like beans popping in a pan—but I could hear it all. It felt as though words in a foreign language were being translated automatically inside my head. *What is this?* The formula was exactly 318 characters long. The moment I felt it become perfectly engraved in my mind, something changed. “Descend.” One word from the old man. *Where to?* Before the question could fade, I felt myself being drawn somewhere deep. No—it only felt as though I was being drawn in. My eyes were definitely closed, but I could see. I could feel. The breeze that gently blew in before scattering. Sunlight. The coachman’s breathing and the horses’ snorts… I pushed all of it away. There was only one place to focus on: my body. > **System** > > Beginning the circulation of Jin Family’s Cultivation Technique. Follow the glowing acupoints. I didn’t notice the old man disappear. I didn’t even hear the System’s voice. My consciousness, awakened in my head, slid downward. I didn't know the points shining like stars were acupoints. Everything simply felt familiar, as though it had always been this way. At last, I reached my dantian. A small but pure energy. Ten years of internal energy. *But what’s that?* In one corner of my dantian was something else, as large and hard as a boulder. I understood instinctively. *More internal energy.* It was energy that I—Jin Taekyung—had not yet assimilated and made my own. It was almost as vast as the internal energy I already possessed. *What if I absorb it?* There was no question that I would become stronger. But for me, right now, it would be a reckless challenge. An adventure without a purpose. *I can’t push my luck and die out here.* I steadied my mind and stirred my internal energy. Following the path the System voice had shown me, I slowly guided it along. At some point, I thought I faintly heard someone’s voice. “Good judgment.” * * * > **System** > > Qi circulation complete. > > Tutorial—Stage 4 complete. Rewards will be distributed! > > You have gained insight into the Skill Qi Sense. You can now manipulate qi more freely and sense the energy of others. > > A small amount of turbid qi has been expelled. > > . > > . > > . > > You have completed all Tutorial stages. > > Main Quest created. With the System’s final voice, the coachman spoke. “We’ve arrived. This is the Jin Family of Taiyuan.” *Yeah. At last.*

#### Chapter 6 tail (verified mastered)

…
I mean is…” “You’re the Third Young Master of the Jin Family of Taiyuan. Is that what you’re trying to say?” “…” Exactly right. Hyuk Mujin continued. “I know perfectly well who you are, Young Master. Now get down from the carriage. We’ll follow procedure.” What else could I do? He said it was protocol. But warning lights were flashing in my head as I climbed down from the carriage. *Why do I have such a bad feeling about this?* The other NPCs in the Jin Family of Taiyuan were giving me strangely chilly looks too. Just as their stares began to make my face burn, Hyuk Mujin took out paper and a brush and spoke. “Name.” “…” “I’ll ask again. Name.” What was this, a criminal interrogation? I was in a foul mood, but decided to wait and see what happened. “…Jin Taekyung.” “Affiliation.” “Jin Family of Taiyuan.” “Age and martial arts realm.” “Twenty. Second Rate.” Hyuk Mujin’s brush paused. “Don’t let pointless pride get in the way. Answer honestly.” Honestly? *Would you understand if I said I reached the Second Rate realm by distributing stats?* When I only stared at him instead of answering, he shook his head. “Well, if you insist, we’ll move on. Let’s see… You’ve been away for several days. Where did you go?” “Honghwaru.” Wow, several days at the famously expensive Honghwaru? Must have been nice. You must have spent a fortune. Or did you skim the family funds again? “Again?” “Why pretend otherwise? Isn’t that something the Young Master has done now and then, time and time again, as a matter of course?” The hostility in Hyuk Mujin’s eyes reminded me of something. *Jin Taekyung.* For a moment, I had forgotten what kind of person the character Jin Taekyung was in this game—especially within the Jin Family of Taiyuan. *The Shame of the Family.* There was no way the Jin Family of Taiyuan’s NPCs would like someone saddled with a title like that. As if to prove it, their contempt was aimed entirely at me now. In this game where nothing ever went my way. *Ah, for fuck’s sake…* Something surged up from deep in my chest. My head throbbed, and my eyes grew hot. Then a low voice reached me. “Third Young Master, I may only be a low-ranking squad leader, but let me say one thing.” His expression said it all. *What a pathetic bastard.* “Stop tarnishing the family’s reputation. At least try to live like a human being. Understood?” He tossed out that one remark and turned away. I stared blankly at the back of his head, then let out a hollow laugh. “Live like a human being?” I knew Hyuk Mujin was nothing more than an NPC who knew nothing. I knew he was saying it to Jin Taekyung, not to me. But… *This is fucking bullshit.* The fact that this was a game and Hyuk Mujin was an NPC didn’t matter. No—I decided not to think about it. All the stress that had built up over the past few days erupted, shattering the last of my patience. “Hey. You. Stop right there.” Hyuk Mujin turned around, irritation written all over his face. I’d been wanting to punch that face for a while now. I beamed like a child who had just seen Santa Claus. “You’re… fucking dead.” I sent my clenched fist flying toward his jaw. * * * The air hung heavy. A pile of documents towered over the desk. And, as always, a cold-looking escort stood beside his master like a shadow. Scratch. Scratch. The Chief of the Gatekeeping Pavilion swallowed. From the moment he entered the office, his mouth had been bone-dry. “Tell me.” The calm voice from beyond the pile of documents was an oasis. The Chief of the Gatekeeping Pavilion finally managed to speak. There is a promising fellow among my subordinates. He's quite loyal to our family, and he has considerable martial talent, but… “I’m listening.” “Perhaps because he’s young, he’s arrogant and insolent. He never thinks before he acts.” “Get to the point.” “I hear he got into a fight with the Third Young Master.” “…I can imagine. What about the youngest?” “We moved him to Medicine King Hall immediately. He’s unconscious, with some bruising…” Silence fell. “It was all my fault. Please punish me severely!” The Chief of the Gatekeeping Pavilion bowed deeply, his vision going dark. A long while passed before the voice came again. “That’s enough. You may leave.” The Chief of the Gatekeeping Pavilion raised his head, feeling as if he had narrowly escaped death. “Ah, one more thing.” “Your command, Lesser Family Head.” “Could I see that fellow? I’d like to speak with him for a moment.” “Lesser Family Head, forgive me for saying so, but his treatment isn’t finished yet.” “Treatment?” “Yes. He’s at Medicine King Hall too. I hear one of his bones was cracked.” “…Is that so? Then never mind.” The silence continued even after the Chief of the Gatekeeping Pavilion withdrew, until the precarious tower of documents came crashing down. “Wipeng.” Jin Wikyung, the thirty-five-year-old Lesser Family Head of the Jin Family of Taiyuan, called to his trusted retainer with a stiff expression. “Yes.” “I’m going to step out for a while.” *Here we go again.* Wipeng, Jin Wikyung’s escort, let out an inscrutable sigh as he watched his master walk away.

## Korean source

```text
＃7화



나는 꿈을 꾸고 있다.

어떻게 꿈인 줄 알았느냐 묻는다면, 글쎄.

‘내가 나를 보고 있으니까?’

말 그대로다. 나는 나를 구경하고 있다. 정확히 말하면 현실의 내가 아닌 게임 속의 진태경을 보는 중이다.

“헉, 허억.”

진태경이 가쁜 숨을 몰아쉬었다. 옷은 찢어졌고, 얼굴과 몸 곳곳이 멍들고 부어오른 모습이다.

반면에.

‘저 새낀 멀쩡하네.’

혁무진은 쌩쌩했다. 상대를 비웃어 줄 여유까지 있었다.

“생각보다 제법이긴 한데…… 그렇게 무식하게 싸워서야 쓰나. 무인이라면 응당 무공을 써야지.”

아오, 저 얄미운 새끼. 당장이라도 달려가 놈의 뒤통수를 후려치고 싶었지만 꿈이라 그런지 몸을 움직일 수도, 소리 내어 말할 수도 없었다.

‘이렇게 보니까 더 열받네.’

맞다. 이 꿈은 앞서 혁무진과의 싸움을 제삼자의 시선으로 나에게 보여 주고 있었다.

“이런 개애새끼가아!”

진태경이 악을 쓰며 달려들었지만 소용없는 일이다. 내가 해 봐서 안다.

‘저땐 이미 지쳐 있었지.’

팔다리는 무겁고 숨은 가쁘다. 동작이 커지니 빈틈도 많다.

아니나 다를까, 간단히 주먹을 피해 낸 혁무진은 진태경의 다리를 걷어차 중심을 무너트렸다.

물 흐르듯 매끄럽고 날렵한 동작이다. 놈과의 싸움은 그런 장면의 반복이었다.

‘새끼, 잘 싸우긴 하네.’

인정해야 한다. 혁무진은 나보다 강하다. 공력을 효율적으로 운용했고 매번 알 수 없는 무공으로 나를 무력화시켰다.

한마디로 놈은 ‘무림인’이었다.

‘충격이었지.’

천력부를 해치운 직후라 자만심에 빠져 있었다. 이 정도면 어느 정도 먹힐 거란 막연한 기대감. 거기에 헌터로서 쌓은 전투 경험과 시스템의 힘이 합쳐지면 로그아웃은 시간문제라고 생각했다.

‘죽기 딱 좋은 생각이었어.’

천력부와 그 산적들은 튜토리얼 몬스터에 불과한 존재다.

초보자 사냥터의 1레벨 토끼를 잡아 놓고 희희낙락했던 거다. 7년 차 헌터? 경력이 우스울 정도로 얄팍한 생각이었다.

‘무공을 익혀야 해.’

이건 단순한 게임이 아니다. 내 목숨이 걸려 있다.

살아남기 위해서는 뭐든 해야 한다. 레벨 업, 무공. 뭐든 익히고 발버둥 칠 각오가 되어 있다.

F급 헌터가 아닌 무림인이 될 각오.

퍽. 퍽. 퍽.

“시발. 맷집만 더럽게 좋아 가지고. 놔! 안 놔!”

“크아아악!”

쓰러져도, 넘어져도 계속해서 일어나는 진태경. 아니, 내 모습이 보였다.

‘결국 마지막에 한 방 먹였지.’

빡!

그래, 저렇게 하는 거다. 지난 7년처럼. 지금까지 그래 왔던 것처럼.

‘그런데 혁무진 저놈은 레벨이 몇이야?’

그 순간, 누가 대답이라도 하듯 혁무진의 머리 위로 시스템창이 솟아올랐다.



[Lv.20 혁무진]



……닥치고 레벨부터 올려야 되나?



* * *



- 수면 모드가 종료되었습니다.



시스템 음성과 함께 눈을 떴다. 아주 잠깐, 고시원 내 방에서 깨어나는 상상을 했지만 부질없는 짓이었다.

“정신이 드십니까?”

흰옷을 걸친 남자의 말에 주위를 둘러봤다. 깨끗하게 정돈된 방 안에는 희한한 냄새가 감돌고 있었다.

여기가 어디지?

내 의문을 알아차리기라도 한 것처럼 남자가 대답했다.

“약왕당입니다. 공자께서는 혼절하신 지 반 시진 만에 깨어나셨고요.”

한의원이었군. 이 NPC는 의원이고.

‘반 시진이면…… 한 시간이나 기절해 있었다고?’

혁무진 그 자식, 야무지게도 때렸다.

“타박상 때문에 상당히 아프실 겁니다. 움직이지 마시고 잠시만 누워 계십시오.”

그 말을 끝으로 의원이 방을 나갔다. 발소리가 멀어지는 것을 확인한 나는 조용히 중얼거렸다.

“상태창 오픈.”

띠링.



상태창



[Lv.11 진태경]

직업 : 이류 무인

명성 : 10

칭호 : 명가의 자제 / 가문의 수치 (칭호 효과 적용 중)

근력 : 40체력 : 40

민첩 : 50 지력 : 10

매력 : 10 공력 : 10년

잔여 포인트 : 10

- 잔여 포인트를 분배하십시오.





천력부를 잡으면서 얻은 10포인트가 그대로 남아 있다. 혹시 모를 상황을 대비해서 포인트 분배를 미뤘었는데, 혁무진과 싸우게 될 줄은 몰랐다.

‘이렇게 얻어터질 줄도 몰랐고.’

나는 잠시 고민하다가 10포인트를 모두 체력에 투자했다.

혁무진과의 싸움에서 지쳐 헐떡거리던 내 모습이 떠올랐기 때문이었다.

‘포인트를 미리 분배해 뒀으면 승산이 있었을까?’

문득 그런 생각이 들었지만 이내 고개를 저었다.

‘결과는 달라지지 않았겠지.’

어른과 아이의 싸움. 혁무진과 나 사이에는 그 정도로 큰 격차가 있었다.

그리고 내가 생각하기에 그것은 레벨과 스탯의 문제가 아니라 무공의 유무로 벌어진 격차였다.

‘어떻게 그런 대응이, 움직임이 가능하지?’

현실에서도 무공이란 게 존재하긴 한다. 권투, 크라브마가, 주짓수 등등. 현대에 들어 실전 무술이라 불리는 것들이다.

하지만 이곳에서의 무공은 차원이 다르다.

동작 하나하나가 실전적이면서도 정교하다. 공력을 중심으로 움직이는 톱니바퀴를 연상시킨다.

‘무공을 익혀야 해.’

튜토리얼에서 마주친 게 천력부가 아니라 혁무진이었다면?

패배, 죽음이라는 단어가 자연스럽게 떠올랐다.

무공을 익혀야 한다. 익혀야 살아남을 수 있다.

“씨이발…….”

폐부 깊은 곳에서 우러나온 쌍욕을 내뱉었을 때였다.

문밖에서 인기척이 들려왔다.

“이 방입니다.”

“고맙네.”

드르륵.

뭐라 반응할 새도 없이 열린 문. 그리고 그곳에…….

“가관이로구나.”

싸늘한 눈빛을 쏟아내는 한 중년인이 있었다.



* * *



“상태는 어떤가?”

“타박상이 있지만 그리 심한 정도는 아닙니다.”

“아쉽군. 다리라도 부러졌어야 했는데.”

“…….”

중년인이 흉흉한 시선으로 나를 바라봤다.

“이 천둥벌거숭이 같은 놈!”

나는 잠자코 눈을 내리깔았다. 생전 처음 보는 사람, 아니 NPC였지만 왠지 그래야 할 것 같았다.

아니, 반드시 그래야 한다.



[Lv.???]



물음표 세 개. [기감]으로도 파악할 수 없는 고레벨이다.

‘최소 30레벨 이상.’

혁무진이 귀여워 보일 정도다. 무엇보다 의원의 태도나 나에게 하는 언행으로 보건대 결코 보통 NPC가 아니다.

최소한 태원진가 삼공자의 아구창을 시원하게 날려 버릴 정도의 권한은 있을 것 같다.

‘저걸로 한 대 맞으면…….’

꿀꺽.

솥뚜껑만 한 손바닥을 보는 순간 나도 모르게 침을 삼켰다.

레벨이고 자시고, 전체적으로 그냥 위험하게 생겼다.

2m에 가까운 거구, 온몸을 감싼 근육은 방탄조끼 같았고 차가운 눈빛은 사람을 얼어붙게 만든다.

취미도 살인, 특기도 살인일 것 같은 이 중년인의 정체가 궁금해지는 순간이었다.

‘그런데 묘하게 낯익은 얼굴이란 말이야.’

이 아저씨를 어디서 봤더라. 곰곰이 생각하다가 깨달았다.

‘진태경?’

중년인은 진태경을 닮았다. 아니, 진태경이 그를 닮았다고 해야 맞다.

까마득히 높은 레벨에 태원진가 삼공자를 깔아뭉개는 언행. 그리고 마지막으로 얼굴.

결론은 하나다. 바로 진태경의…….

“아버지?”

나도 모르게 내뱉은 그 말에 중년인이 눈을 부릅떴다.

“아, 아버지이?”

주먹까지 파르르 떨린다. 누가 보면 내가 엄마 욕이라도 한 줄 알겠다. 나는 그의 주먹을 주의 깊게 바라보며 말했다.

“저, 저기. 잠깐만 진정하시고…….”

“진정? 네놈 입에서 그딴 소리가 나와? 이 상황에서도 장난질을 쳐!”

“아니라면 정말 죄송합니다. 제가 실례했어요.”

“입 다물어.”

서늘한 눈빛으로 내 입을 틀어막더니 아직도 대기 중인 의원에게 고개를 돌렸다.

“안내해 줘서 고맙네. 이만 나가 보게.”

나는 간절한 눈빛으로 구조 신호를 보냈지만, 의원은 잽싸게 돌아섰다.

‘아니, 시바…… 의사가 환자를 외면해?’

쾅. 문이 닫히는 소리가 지옥문 입장 소리처럼 들린다.

단둘이 남게 된 방 안. 그가 솥뚜껑만 한 손바닥을 치켜들고 다가오기 시작했다.

“망나니 짓거리도 정도가 있지, 언제까지 이렇게 살 테냐!”

어느새 나는 벌떡 일어나 슬금슬금 뒷걸음질을 치는 중이었다.

타박상? 고통? 그런 건 이미 느껴지지 않았다. 어쩌면 더 이상 고통을 느낄 수 없는 몸이 될지도 모른다.

“저, 저한테 딱 십 분만. 아니, 일 다경만 주시면 제가 잘 설명해 드릴 수 있거든요. 뭐 때문에 화가 나신 건데요. 네? 아버지라고 부른 것 때문에 그러세요? 혹시 어머니세요?”

“이노옴!”

쩌렁쩌렁한 음성에 순간 몸이 굳는다. 등이 벽에 닿는 것이 느껴졌다.



- 당신은 [혼란]에 빠졌습니다. 3초간 몸을 움직일 수 없습니다!



이런 개 같은 경우를 봤나…….

‘끝났구나.’

27년 인생이 주마등처럼 스쳐 지나간다. 거짓말 조금 보태서 정자 시절 치열했던 착상 레이스까지 떠오른다. 그때 참 힘들었지.

‘엄마, 아빠, 하연아…….’

가족들을 생각하며 스르륵 눈을 감은 그 순간이었다.

“틈만 나면 계집질이나 하고!”

쓰담쓰담.

“도박장이나 들락거리고!”

만지작만지작.

“네놈이 이따위로 행동하니 가문에서 멸시받는 것이다!”

문질문질.

……이 아저씨 지금 뭐 하는 거야?

입으로는 분노와 질책 어린 말들을 쏟아 내면서, 손은 부드럽게 내 몸 곳곳을 어루만진다. 등골이 오싹했다.

‘설마 이거.’

띠링.



- 당신은 [공포]에 휩싸였습니다. 5초간 몸을 움직일 수 없습니다!



“너는 가문의 수치다, 수치!”

극도의 수치심을 느끼고 있긴 하다. 인공지능에게, 그것도 중년 남성의 모습을 한 NPC에게 성추행을 당하다니.

‘엄마…….’

모든 게 내 오해라는 걸 깨달은 것은 잠시 후였다.

손은 바쁘게 움직인다. 그런데 그게 꼭 환자를 살피는 의사의 그것 같다.

눈꺼풀도 뒤집고, 맥도 한 번 짚어 보고, 타박상 부위도 세심하게 살핀다. 그의 손이 스쳐 갈 때마다 안마를 받는 것처럼 시원해지고 고통이 사라졌다.

“너 이 녀석! 계속 이따위로 행동하면, 어? 어! 아주 경을 칠 것이다. 알겠느냐?”

“…….”

마침내 손을 멈춘 그가 작은 목소리로 속삭였다.

“생각보다 경미해서 다행이다. 그러게 왜 싸웠느냐. 평소에 무공 수련도 안 하던 녀석이.”

나는 진심을 담아 입을 열었다. 여러 가지가 함축된 한마디였다.

“누구세요?”

다음 순간, 엄격. 근엄. 진지. 세 가지가 모두 담겨 있던 얼굴이 돌연 상처받은 아기 사슴으로 변했다.

“갑자기 왜 존댓말을 쓰고 그러느냐. 아까 가문의 수치라고 한 건 그냥 사람들 들으라고 한 소린데…… 혹시 섭섭했던 거냐?”

“예?”

“형은 슬프구나. 너 어릴 때 내가 매일 똥 기저귀도 갈고, 울면 업어 주고, 달래서 재우고. 얼마나 애지중지 키웠는지 알면서.”

“예? 형이요?”

순간 침묵이 찾아왔다.

‘아버지가 아니라 형이었어?’

나는 이 나이 든 아저씨가 형이라는 사실에 놀랐고.

“아이고, 우리 막내가 머리를 다쳤나 보네. 이보게. 의원! 의원!”

중년인은 의원을 부르짖으며 뛰쳐나갔다. 그 뒷모습을 보면서 문득 퍼즐 하나가 맞춰졌다는 생각이 들었다.

‘진태경이 개판으로 자란 이유를 알겠네.’

잘못된 가정교육의 훌륭한 사례다.
```

## Current accepted English baseline

```markdown
# Chapter 7

I’m dreaming.

How do I know? Well…

*Because I’m watching myself?*

I mean that literally. I’m watching myself. More precisely, I’m watching Jin Taekyung in the game—not the me in the real world.

“Gasp… Hah, hah.”

Jin Taekyung panted for breath. His clothes were torn, and bruises and swelling covered his face and body.

Meanwhile…

*That bastard’s perfectly fine.*

Hyuk Mujin was full of energy. He even had enough breathing room to sneer at his opponent.

“You’re better than I expected, but… what good is fighting so crudely? A martial artist ought to use martial arts.”

*God, what an annoying bastard.* I wanted to run over and smack him in the back of the head, but maybe because it was a dream, I couldn’t move my body or make a sound.

*Seeing it like this just pisses me off more.*

Right. This dream was showing me the fight with Hyuk Mujin from a third party’s point of view.

“You fucking sooon of a bitch!”

Jin Taekyung charged at him, screaming, but it was pointless. I knew because I’d been there.

*By then, I was already exhausted.*

My arms and legs were heavy, my breathing ragged. With my movements growing wider, I was leaving plenty of openings.

Sure enough, Hyuk Mujin easily dodged the punch, then kicked Taekyung’s leg out from under him.

His movements were smooth and nimble, like water flowing. The fight was just a repetition of scenes like that.

*Bastard, he can fight.*

I had to admit it. Hyuk Mujin was stronger than me. He used his internal energy efficiently and neutralized me every time with martial arts I couldn’t understand.

In a word, he was a martial artist of Murim.

*It was a shock.*

I’d been too full of myself after taking down the Heavenly Axe. I’d had this vague expectation that my strength would get me somewhere. Add seven years of combat experience as a Hunter and the power of the System, and I’d thought logging out was only a matter of time.

*That was exactly the kind of thought that gets you killed.*

The Heavenly Axe and those bandits had been nothing more than tutorial monsters.

I’d been gloating after killing a Level 1 rabbit in a beginner hunting ground. A seven-year Hunter? My thinking had been so shallow it made a joke of my experience.

*I have to learn martial arts.*

This wasn’t just a game. My life was on the line.

I had to do whatever it took to survive. Level up, learn martial arts—learn anything I could and fight tooth and nail. I was ready to become a martial artist of Murim, not an F-rank Hunter.

Thud. Thud. Thud.

“Fuck. You’re ridiculously tough. Let go! I said let go!”

“Graaagh!”

Jin Taekyung kept getting knocked down and getting back up. No—that was me.

*I landed one good hit at the very end, though.*

Smack!

*Yeah. That’s how you do it. Like I did for the last seven years. Like I always have.*

*But what Level is Hyuk Mujin?*

At that moment, as if answering my question, a System window rose above Hyuk Mujin’s head.

> **System**
>
> Lv. 20 Hyuk Mujin

…Should I just shut up and level up first?

* * *

> **System**
>
> - Sleep mode has ended.

I opened my eyes to the sound of the System’s voice. For a split second, I imagined waking up in my room at the goshiwon, but it was a pointless hope.

“Are you conscious, Young Master?”

I looked around at the man in white. The neat, clean room was filled with a strange smell.

*Where am I?*

As if he had noticed my question, the man answered.

“This is Medicine King Hall. You regained consciousness half a shichen after you fainted.”

So this was a clinic. And this NPC was a physician.

*Half a shichen… Was I unconscious for an hour?*

That bastard Hyuk Mujin had really laid into me.

“You’ll be in considerable pain because of the bruises. Please lie still for a while.”

With that, the physician left the room. Once I heard his footsteps receding, I quietly muttered,

“Open Status Window.”

Ding.

> **System**
>
> Status Window
>
> Lv. 11 Jin Taekyung
>
> **Occupation:** Second Rate Martial Artist
>
> **Fame:** 10
>
> **Titles:** Scion of a Prestigious Family / Shame of the Family (Title effects active)
>
> **Strength:** 40 **Stamina:** 40
>
> **Agility:** 50 **Intelligence:** 10
>
> **Charm:** 10 **Internal Energy:** 10 years
>
> **Unassigned Points:** 10
>
> - Distribute your unassigned points.

The ten points I’d earned from defeating the Heavenly Axe were still sitting there. I’d held off on distributing them in case something unexpected happened, but I hadn’t expected to end up fighting Hyuk Mujin.

*I hadn’t expected to get beaten to a pulp, either.*

After thinking for a moment, I put all ten points into Stamina.

I’d remembered how exhausted and breathless I’d been during my fight with Hyuk Mujin.

*If I’d distributed the points beforehand, would I have stood a chance?*

The thought crossed my mind, but I soon shook my head.

*The outcome wouldn’t have changed.*

It had been a fight between an adult and a child. That was how vast the gap between Hyuk Mujin and me had been.

And as far as I was concerned, that gap had less to do with Levels and stats than with whether or not we knew martial arts.

*How was he able to react like that? Move like that?*

Martial arts did exist in the real world too. Boxing, krav maga, jiu-jitsu, and so on—the things people called practical martial arts these days.

But martial arts here were on an entirely different level.

Every movement was practical and precise at the same time. They reminded me of interlocking gears driven by internal energy.

*I have to learn martial arts.*

What if I’d encountered Hyuk Mujin in the tutorial instead of the Heavenly Axe?

The words defeat and death came naturally to mind.

I had to learn martial arts. I wouldn’t survive without them.

“Fuuuck…”

That was when I let out a long, vicious curse from the bottom of my lungs.

I heard someone outside the door.

“This is the room.”

“Thank you.”

Creak.

The door opened before I had a chance to react. And there, standing in the doorway…

“Well, aren’t you a sight.”

A middle-aged man was glaring at me with icy eyes.

* * *

“What’s his condition?”

“He has bruises, but nothing too serious.”

“That’s a shame. His leg should at least have been broken.”

“…”

The middle-aged man looked at me with a threatening glare.

“You reckless little bastard!”

I quietly lowered my eyes. He was a man—or rather, an NPC—I had never seen before, but for some reason, it felt like I should do that.

No. I absolutely had to.

> **System**
>
> Lv. ???

Three question marks. Even Qi Sense couldn’t identify his Level.

*Over Level 30, at minimum.*

He made Hyuk Mujin look cute. Judging by the physician’s attitude and the way this man spoke to me, he was no ordinary NPC. At the very least, he seemed to have enough authority to smack the Third Young Master of the Jin Family of Taiyuan right across the mouth.

*If I took one hit from that…*

Gulp.

I swallowed involuntarily when I saw his palm, as large as a pot lid.

Level aside, the man looked dangerous in every way.

He was nearly two meters tall, with muscles wrapped around his entire body like a bulletproof vest. His cold eyes were enough to freeze a person solid.

I found myself wondering who this middle-aged man was. His hobby looked like murder, and his specialty probably was too.

*But his face looks strangely familiar.*

Where had I seen this man before? I thought hard, then realized.

*Jin Taekyung?*

The middle-aged man looked like Jin Taekyung. No—the truth was that Jin Taekyung looked like him.

His incomprehensibly high Level. The way he spoke while trampling all over the Third Young Master of the Jin Family of Taiyuan. And finally, his face.

There could only be one answer. He was Jin Taekyung’s…

“Father?”

The word slipped out before I could stop it, and the middle-aged man’s eyes went wide.

“F-Father?”

Even his fists began to tremble. Anyone watching would have thought I’d insulted his mother. I watched his fist carefully and said,

“Please, just calm down for a moment…”

“Calm down? How dare you say that to me! You’re still joking around at a time like this!”

“I’m sorry if that wasn’t it. I spoke out of turn.”

“Shut your mouth.”

He silenced me with a chilly glare, then turned to the physician, who was still waiting nearby.

“Thank you for showing me here. You may leave now.”

I sent the physician an urgent distress signal with my eyes, but he turned away in a hurry.

*What the fuck… A doctor is abandoning his patient?*

Bang. The door closing sounded like the gates of hell opening.

Left alone with him in the room, I watched as he raised his pot-lid-sized palm and started walking toward me.

“There’s a limit to acting like a wastrel. How long are you planning to live like this?”

Before I knew it, I had jumped to my feet and was slowly backing away.

Bruises? Pain? I couldn’t feel any of that anymore. Maybe I was about to end up in a body that would never feel pain again.

“Give me just ten minutes. No, a quarter hour. I can explain everything properly. What are you angry about? Huh? Is it because I called you Father? Are you actually my mother?”

“You little brat!”

His booming voice made my body lock up. I felt my back touch the wall.

> **System**
>
> - You have fallen into Confusion. You cannot move for 3 seconds!

*What the actual fuck…*

*I’m finished.*

My twenty-seven years of life flashed before my eyes. With a little exaggeration, even the fierce race to fertilize the egg back when I was still a sperm came to mind. That had been a rough one.

*Mom, Dad, Hayeon…*

It was just as I closed my eyes and thought of my family.

“Whenever you get a chance, all you do is chase women!”

Pat, pat.

“You’re always in and out of gambling dens!”

Fiddle, fiddle.

“This is why the family looks down on you!”

Rub, rub.

…What the hell was this guy doing?

He kept spewing angry scoldings, but his hands were gently feeling me all over. A chill ran down my spine.

*No way…*

Ding.

> **System**
>
> - You have been overcome by Fear. You cannot move for 5 seconds!

“You’re a disgrace to the family. A disgrace!”

I was overwhelmed by shame. I was being sexually harassed by an AI—and one that looked like a middle-aged man, at that.

*Mom…*

It took me a moment to realize that I had completely misunderstood.

His hands were moving quickly, but they were moving just like a physician examining a patient.

He lifted my eyelids, checked my pulse, and carefully examined the bruised areas. Every time his hands passed over me, the pain faded and my body felt refreshed, as if I were getting a massage.

“You little bastard! Keep acting like this and, huh? Huh! You’ll get what’s coming to you! Do you understand?”

“…”

At last, he stopped moving his hands and whispered in a small voice,

I opened my mouth with complete sincerity. It was a single question that contained a great many things.

“Who are you?”

The next moment, his strict, solemn, serious face suddenly transformed into that of a wounded baby deer.

“Why are you speaking formally all of a sudden? When I called you a disgrace to the family, I only said it for other people to hear… Did it hurt your feelings?”

“Huh?”

“Your big brother is sad. Do you know how dearly I raised you? When you were little, I changed your dirty diapers every day, carried you around whenever you cried, and soothed you to sleep.”

“Huh? You’re my brother?”

Silence fell.

*He was my brother, not my father?*

I was shocked that this old man was my brother.

“Oh, dear. It looks like our youngest hit his head. Physician! Physician!”

The middle-aged man rushed out, shouting for the physician. As I watched his back disappear, I suddenly felt as if a missing piece of the puzzle had fallen into place.

*Now I understand why Jin Taekyung grew up such a mess.*

A shining example of what happens when parenting goes wrong.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 7`.
