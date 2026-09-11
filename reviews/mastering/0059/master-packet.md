# Master Edit Task — Chapter 59

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
| 진위경    | **Jin Wikyung**    |
| 위팽     | **Wipeng**         |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 영약     | **elixir**                                       |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 일격     | **One Strike**                         |
| 헌터      | **Hunter**            |
| 레이드     | **raid**              |
| 탱커      | **tank**              |
| 힐러      | **healer**            |
| 대격변     | **Great Cataclysm**   |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 정마대전   | **Great Faction War**         |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 50–54

## Plot

Taekyung enters Choi Minwoo’s exclusive D-rank Gate and clears a colony of about twenty Level 40 swamp Lizardmen alone. Choi reveals the encounter was a test, then releases female-Lizardman pheromones that summon a much stronger horde. Taekyung spends all 100 Remaining Points—30 Strength, 30 Stamina, and 40 Agility—and uses One Flash to kill the Level 52 Lizardman Great Chieftain and dozens of monsters. He and Choi clear three C-rank Gates in one day, earning Taekyung 300 million won, while Choi privately recognizes that Taekyung may be stronger than himself.

Sopung Guild’s Guild Master learns that Kim Sangshik dismissed Taekyung and filed a false report. He expels Kim and orders the resignation of Kim’s son, Kim Sangho, provoking Guild-wide gossip about Taekyung’s reawakening.

Taekyung returns home with his C-rank Hunter license and cash, gives his mother and younger sister Hayeon an edited account of his reawakening, and spends the day treating them to clothes and an expensive meal. Back in the goshiwon, increasingly vivid Murim nightmares destabilize him despite Sleep Mode and qi circulation. His injuries worsen during raids, so Choi orders him home. Taekyung lies to Jinho that Jin Wikyung is his Chinese girlfriend, then concludes that Murim may be another reality and the Ark - 2020 capsule a dimensional Gate.

A dream of the Mount Heng Sword Sect–Jin Family battle convinces Taekyung that Murim’s people are real and that he must return. Choi and Butler Kim investigate him, find no evidence that he is an illegal Awakener or deliberately infiltrated Choi’s orbit, and offer an exceptionally generous contract. Taekyung refuses because he cannot abandon Murim, promises to return the next day, enters the capsule, and accepts the prompt to connect to Murim.

## Continuity

- Taekyung clears the Lizardman Gate without injury, then kills the Level 52 Lizardman Great Chieftain and the summoned horde with One Flash.
- He spends all 100 Remaining Points: 30 Strength, 30 Stamina, and 40 Agility. His equipment remains the First Rate Lizardman Hunter’s Leather Set and Lizardman Slayer’s Harpoon.
- Taekyung completes three C-rank Gates in one day and receives 300 million won, including a 270-million-won bonus. His seven-day provisional Peace Guild contract requires weekends off.
- Choi Minwoo suspects Taekyung may be stronger than him; Choi’s exact current rank remains unknown. Choi continues observing Taekyung and wants to recruit him.
- Sopung Guild expels Kim Sangshik after confirming his misconduct; Kim Sangho also leaves. Sopung’s recruitment of Taekyung remains unresolved.
- Taekyung now holds a C-rank Hunter license. His family knows only the edited explanation that he reawakened and earned money; Murim, the System, and the capsule remain concealed from them and from Seong Jinho.
- Hayeon is nineteen and still a high-school senior. Taekyung’s mother and Hayeon secretly give him additional cash and side dishes.
- Taekyung suffers recurring Murim nightmares and increasing injuries during raids. Sleep Mode repairs his body but does not resolve the mental disturbance.
- The Mount Heng–Jin Family battle is underway. The Head Elder’s third force is waiting for both sides to weaken; the traitor’s identity, betrayal, and the battle’s outcome remain unresolved.
- Taekyung has reconnected to Murim through the Ark - 2020 capsule. Whether the capsule can transport him safely and reliably, its ultimate purpose, and the consequences of his return remain unresolved.
- Choi’s offered contract includes a 500-million-won signing bonus, 50-million-won monthly salary, seventy-percent settlement split, officetel, sedan, and social insurance. Taekyung rejects it while intending to return from Murim.

## Translation Decisions

- Use **Lizardman Great Chieftain** for 대족장 and **One Flash** for 일섬.
- Preserve **swamp Lizardmen**, **Lizardman Hunter’s Leather Set**, **Lizardman Slayer’s Harpoon**, and the female-Lizardman pheromone lure.
- Keep **C-rank Hunter** distinct from System **Grade** terminology.
- Preserve **Sleep Mode**, **Remaining Points**, **Internal Energy**, **System**, and the exact prompt: **“Would you like to connect to Murim?”**
- Use **logged in** only for Taekyung’s action after accepting the prompt.
- Keep **Peace Guild**, **Sopung Guild**, **Hunter license**, **goshiwon**, and **officetel**.
- Preserve the distinction between Hayeon’s gender-neutral question about Jin Wikyung and Taekyung’s false claim that Wikyung is his girlfriend.
- Retain the dry, self-mocking narration; affectionate, profane family banter; Choi’s measured testing and recruitment; and the Guild Master’s “raise hell” callback.
- Keep *Bulgeum* as “Burning Friday,” with a concise Korean-slang footnote, and retain concise first-use footnotes for *gukbap* and *goshiwon*.

### Prior accepted reading-copy tails

#### Chapter 57 tail (accepted)

…
in two. *We were able to come this far because of his help.* Jin Wikyung thought the opposite. *We were able to come this far because this was what the Head Elder wanted.* A span too short even to call an instant. When Jin Wikyung finished the thought, he opened his mouth. “Wipeng.” “Your orders.” “Cut down the First Elder.” “What?” The stooped, emaciated old man—the First Elder—opened his eyes wide. The senior members standing nearby were just as shocked. “L-Lesser Family Head!” “What in the world…!” But Wipeng did not hesitate. Before anyone knew it, his sword was flying toward the First Elder’s chest. Clang-clang-clang! Two swords cut in out of nowhere and knocked Wipeng’s blade aside. Two fat, exceptionally tall old men. They were the Second and Third Elders, who, together with the First Elder, styled themselves the Head Elder’s hands and feet. Wipeng’s brow twitched when he saw the faint Sword Energy gathered on their blades. “You’ve been hiding your martial arts.” The First Elder answered with a single punch. Boom! With internal energy as deep as the years he had lived, he sent Wipeng flying, then straightened his back. The field froze at the appearance of yet another Peak master who had spent his entire life hidden in the Head Elder’s shadow. “First Elder, what… what is this?” “Then could it be…!” *Betrayal.* The word stamped itself clearly into everyone’s minds. “That’s impossible!” The one who shouted was the White Tiger Hall Leader. If the Elders were the Head Elder’s hands and feet, he had thoroughly served as the First Elder’s. “Elder, Lesser Family Head. It seems there has been some misunderstanding…” But he could not finish. At a jerk of the First Elder’s chin, the Second Elder moved with blinding speed and cut the White Tiger Hall Leader’s throat. Shhk. Thud. Jin Wikyung’s gaze met the First Elder’s in the air between them. “You recruited the White Tiger Hall Leader too?” “He was a noisy man. That was all. The others were the same.” Jin Wikyung’s guess had been half right and half wrong. The Elders had betrayed them, but the senior members who belonged to the Elders’ faction had not. “Then why… Ah!” “Sharp. I’ll give you that.” The First Elder pulled a dark, grimy bamboo tube from inside his robes. Only a little of the fuse was left, and it was already burning down. “Could we tell important secrets to men like that? Even just throwing the inside into chaos had already served its purpose. Things were easier if they didn’t know what was happening outside.” Jin Wikyung shouted like a scream. “Stop him!” “You’re too late.” The First Elder was right. The instant the fuse burned to its end, something burst, and a red flame shot high into the sky. Fwish—boom! It was a signal. The martial artists of the small and mid-sized sects known as the Five Gates of Shanxi—the Three Paths Sect, a union of three sects; the Tao-centered Byeokdo Sect; and Gunggwimun, which had been pouring arrows from the cliffs without pause—turned in an instant. “Kill everyone in your path!” “No exceptions! Sweep them all away!” They were no longer the clumsy third-rate martial artists they had seemed to be. Killing intent flowed from their eyes, and their sword paths were sharp. *This wasn’t something they prepared overnight.* Jin Wikyung’s face hardened. * * * Boom! The Head Elder looked up at the sky. Before the red flame had even faded, a massive roar erupted from every direction. *Too fast. Far too fast.* The signal was supposed to go up only after the Mount Heng Sword Sect had been annihilated. The Five Gates of Shanxi were a blade prepared over decades. It had to be swung once, and finish everything like a bolt of lightning. *Everything has its flow.* The plan, which had been running without a hitch, had begun to go off course. As the Head Elder smiled bitterly, a voice slipped into his ear. “So… it was you.” Lee Cheonbaek. His voice was faint, but his eyes burned more fiercely than ever. “You still have the strength to talk?” “I’ll tear you to pieces alive and kill you.” But no sooner had he finished speaking than blood poured from his mouth. The Head Elder pressed one of his acupoints and murmured, “That would be inconvenient just yet. You still have something to do.” Lee Cheonbaek despaired. They had taken heavy losses, but hundreds of Mount Heng Sword Sect martial artists still remained. At this point, with even the leadership annihilated, if their Sect Leader were taken prisoner… *Kill me instead!* The anguished cry never left his mouth. The Head Elder pressed the Mute Acupoint, taking his voice. Then his hand brushed the Paralysis Acupoint, and Lee Cheonbaek’s body went rigid. He had become a living corpse with his eyes still open. “You bastard! Get your hands off him!” At the same time, the air split with a shriek. Fwoooosh! The Head Elder did not panic. He swept his sword up from below. Beyond the spear splitting in two along the Sword Energy, Jin Taekyung was charging at terrifying speed. “Aaaaaah!” “Squad Leader! Please slow down a little!” Together with a dozen or so riffraff who had appeared from who knew where. [^1]: Red Hare is the legendary warhorse of Lü Bu in *Romance of the Three Kingdoms*.

#### Chapter 58 tail (accepted)

…
been waiting for rang out. Ding. > **System** > > - The effect of the Title **Gambler** is applied. > - **Strength** temporarily increases. > - **Agility** temporarily increases. > - **Stamina** temporarily… The effect of the Gambler Title, which raised combat-related stats by ten percent in a one-on-one duel, seeped through my whole body. And on top of that— Whoosh! The boost to my stats accelerated the attack as well. In an instant, the spearhead dropped like a bolt of light, aimed at the crown of the Head Elder’s head. *This is going in.* That was certainty. The certainty that even a monster like Jopil wouldn’t have been able to dodge it. But the man I was facing wasn’t Jopil. He was the Head Elder. Boom! The spear shaft shuddered with a thunderous crash. The Head Elder, having blocked the spear at a speed too fast to see properly, smiled faintly. “Not bad. Better than I expected.” Without even time to answer, I wrung out every last ounce of strength. The spear, loaded with tremendous force that even a decent master would have struggled to endure, crushed down on his sword. Grrrkk. With an ugly grinding sound, his sword began to lift… No. Wait. *It should be going down. Why is it coming up?* I’d put that much force into it, and I was the one being pushed back. At my dumbfounded expression, the Head Elder’s smile deepened. “You tried, but did you think that would be enough?” The next instant, every hair on my body stood on end. Tsssss. A blue haze bloomed along the blade. Sword Energy. Before I could even react, the spearhead that had been slowly getting pushed back was sliced off like tofu. Shing. Now it wasn’t a spear but a staff. A long staff. Sword Energy flashed again toward me as I backed away. Shing. The long staff became a short staff. Shing. “…” Fuck. Even nunchaku would be longer than this. I threw the iron rod—no longer a spear or a staff—at the Head Elder. Shing. “Do you intend to run?” Run? That’s a hurtful thing to say. I’d already thrown myself sideways at the same moment I threw it. I grabbed the collar of the man lying facedown as if he were dead. *Got him!* My only goal from the beginning had been to rescue Jin Wikyung. Now that I’d done it, there was no reason to fight that monstrous old man. I scooped Jin Wikyung into my arms and hurled myself away with all my strength. Whoosh—boom! The Sword Energy that arrived a beat later split the ground. Hyuk Mujin and the reconnaissance squad surrounded us as we slipped out of the Head Elder’s range by a hair. “Protect the Squad Leader!” “Are you all right?” I said nothing. I forgot we had to run from the Head Elder right now. I even forgot this was a battlefield. My head was full of a single question. *Who is this man?* I had definitely rescued Jin Wikyung. I was supposed to have rescued him… Then who was this macho middle-aged man in my arms? His face was covered in sword scars, and his eyes were bloodshot. In a trembling voice, I asked, “Excuse me, but who are you…?” At that moment, a single cry burst from Hyuk Mujin’s mouth. “Gah! Lee Cheonbaek!” Lee Cheonbaek? The name rang a bell. “You know him?” “Of course I do!” “Are you close?” “What kind of bullshit is that? That’s Blood Wolf Sword Lee Cheonbaek!” “Blood Wolf Sword?” “Yes! That Blood Wolf Sword…!” “Cool alias. Sounds like a master.” Hyuk tore at his hair and shouted, “He’s the Sect Leader of the Mount Heng Sword Sect! Blood Wolf Sword Lee Cheonbaek!” “…” I scrambled backward. This man was Lee Cheonbaek? Cold sweat rolled down me. *He’s Lee Seogeun’s father.* He was the man who’d started a war because he thought I’d poisoned his son. He was also a cold-blooded killer who’d slaughtered adults and children alike in revenge. *Rescuing the wrong guy was unfair enough, and I nearly got stabbed too.* But Lee Cheonbaek no longer seemed to have the strength left for that. His whole body was covered in blood, and he couldn’t so much as twitch a hand. It looked like severe internal injuries, or like his acupoints had been sealed. *Still, at least it isn’t Jin Wikyung.* As if he’d read my mind, Hyuk asked, “Then where is the Lesser Family Head?” “I don’t know. And…” I yanked him back by the nape of his neck. A sword came flying in and buried itself where Hyuk’s foot had been a moment before. *I’m really well and truly screwed.* I let out a long sigh, then went on, “You think that old man is going to let us go?” The Head Elder burst into a hearty laugh. “Ha ha ha! Have you ever seen such an insolent brat!” “If I behave politely, will you let us go?” “Don’t you think you’ve come too far for that?” Tsssss. Sword Energy surged up. No more words were needed. I pulled a spear stuck among the corpses. Then, with everyone’s eyes on me, I spoke. “Encircling formation. Spread out.” One of the oldest Hunter sayings was this: *There are strong monsters, but no monster that can’t be taken down.* What made that possible was a raid.

## Korean source

```text
＃59화



쉬쉬쉬쉭!

진위경과 위팽. 그리고 세 장로의 싸움은 폭풍 같았다.

평범한 무인은 눈으로 볼 수 없을 만큼 빠르고 강맹한 검격이 사방에서 부딪쳤다.

카가각.

‘막혔다.’

위팽은 판단과 동시에 몸을 뒤집었다. 이장로가 내뻗은 검이 머리카락을 아슬아슬하게 스치고 지나갔다.

이장로와 삼장로가 한 몸처럼 그를 압박해 갔다.

“이놈들!”

노호성과 함께 달려든 진위경은 일장로에 의해 가로막혔다.

“어딜 그리 급하게 가는가?”

순간 쭉 솟구친 검기가 진위경의 정수리를 향해 떨어졌다.

일도양단의 위기. 진위경은 황급히 검을 들어 막았다. 그의 검신에도 희끄무레한 검기가 서려 있었다.

쾅!

굉음과 함께 피어오른 먼지구름 속, 한 인영이 비틀거리며 물러났다. 안색이 창백해진 진위경이 피가래를 퉤 뱉었다.

‘무슨 놈의 공력이…….’

어릴 적부터 뛰어난 무공과 영약을 섭취해 온 그였지만 상대가 좋지 않았다. 일장로는 일 갑자를 넘게 살아오며 흑심을 감춰 왔던 비열한 노괴(老怪)다.

대장로와 더불어 정마대전을 온몸으로 헤쳐 지나온 산 증인인 것이다.

“염병할 늙은이 같으니라고.”

일장로가 허허 웃으며 대꾸했다.

“소가주, 체통을 지키시게.”

그러나 일장로의 속마음도 생각만큼 편치는 않았다.

파르르 떨리는 검신과 욱신거리는 손목이 그 증거였다.

‘이 정도일 줄이야.’

저잣거리 왈패들 싸움도 머릿수가 중요한데 고수들은 오죽할까. 그러나 진위경과 위팽의 실력은 생각 이상이었다.

아니, 어쩌면 늙은이의 자존심이 스스로를 과대평가했는지도 모를 일이다.

‘야속하구나. 참으로 야속해.’

일 갑자의 세월. 그는 심후한 공력을 얻었지만 육신의 노화까지는 어찌할 수 없었다.

‘십 년만 젊었다면.’

씁쓸히 자조한 일장로가 진위경에게로 걸음을 옮겼다.

그의 의제(義弟)인 이, 삼장로의 검도 더더욱 매서워졌다.

쉬쉬쉭!

“큭!”

진위경과 위팽은 서서히 밀리기 시작했다. 앞서 항산검문의 절정 고수들을 상대한 직후인지라 더더욱 그랬다.

점차 눈앞이 어지러워졌고, 몸에 잔 상처들이 늘어났다. 손발 또한 마음처럼 움직여 주지 않았다.

‘이대로는 어렵다.’

진위경의 안색이 어두워진 그때였다.

쐐애애액!

거침없이 쇄도하던 일장로의 검기가 불현듯 방향을 틀었다. 다음 순간, 번개 같은 일격이 목표를 갈라냈다.

서걱.

촤아아악.

피보라와 함께 한 사람이 비틀거렸다. 일장로의 옆구리를 겨누던 검은 산산이 부서져 형체조차 알아볼 수 없었고, 가슴에서는 피가 폭포처럼 흘러내렸다.

그의 얼굴을 확인한 일장로가 혀를 찼다.

“집법당주, 이 미련한 친구야. 그리도 죽고 싶었나?”

“일, 장로.”

집법당주의 목소리는 금방이라도 끊어질 듯했다. 그러나 그는 쓰러지지도, 말을 멈추지도 않았다.

“당신들은, 문내 법규를, 어겼소.”

“허허, 그래서?”

“대태원진가의, 집법당주로서, 명한다. 죄인들은 스스로 무공을 전폐하고, 참회동에…….”

서걱.

일장로는 검으로 대답을 대신했다. 대쪽 같은 성정에 비해 무공이 높지 않던 집법당주는 볼 수도, 피할 수도 없었던 일 검이 그의 목을 꿰뚫었다.

진위경의 눈에서 화염이 쏟아졌다.

“이노옴!”

이 순간, 분노한 것은 진위경뿐만이 아니었다. 집법당주의 죽음은 태원진가 중진들의 가슴에 불을 질렀다.

“집법당주!”

무인이기 전에 사람이다.

적지 않은 세월을 살아온 만큼 이뤄 온 것도, 지켜야 할 것도 많았다. 그래서 절정 고수의 무위가, 개죽음이 두려웠다.

그러나 집법당주의 당당한 최후는 잠시 잊고 있던 감정을 끓어오르게 만들었다.

바로 부끄러움과 분노였다.

“저 역도들을 쳐라!”

“태원진가의 기개를 보여라!”

스스로를 부끄럽게 여긴 자들이 제일 먼저 앞장서 달려들었다. 소위 장로원 계파에 속하던 중진들이었다.

그들은 배신자를 도운 자신을, 그리고 자신과 가문을 배신한 장로들을 용서할 수 없었다.

“멍청한 것들.”

서걱. 서걱. 서걱.

세 장로의 검이 한 번 번뜩일 때마다 한 명의 목숨이 스러졌다.

명백한 힘의 우위. 하지만 장로들의 주름진 얼굴은 딱딱하게 굳었다.

‘이놈들이……!’

동귀어진을 각오한 수십 명의 일류 고수가 죽음을 두려워하지 않고 사방에서 몰려들었다.

장로들은 그들의 무공이 아니라 기세에 당황했다. 그리고 그사이, 빈틈을 놓치지 않는 두 사람이 있었다.

서걱.

“크악!”

삼장로의 입에서 비명이 터져 나왔다. 부지불식간에 솟구친 위팽의 검기가 그의 옆구리를 베어 낸 것이다.

“아우야!”

수십 년을 함께한 의형제의 비명에 이장로가 흔들렸다. 아주 찰나, 그의 신경이 다른 곳으로 향했다.

그러나 그 결과는 뼈아팠다. 일시에 내뻗어진 세 개의 검이 그의 전신을 스쳤고, 황급히 물러나는 이장로를 향해 벼락 한 줄기가 쏘아졌다.

쐐애애액!

서늘한 무언가가 등을 파고든다고 느낀 순간, 이장로는 모든 것이 끝났음을 직감했다.

푹!

살을 가르고, 뼈를 잘라 낸다. 검기(劍氣)는 살아 있는 생물처럼 날뛰며 혈맥을 찢고 태웠다.

얼마 만에 느껴 보는 고통인가. 이장로는 눈앞이 새하얗게 물들었다. 그리고 이내 아무런 고통도 느낄 수 없게 되었다.

“나, 태원진가의 소가주 진위경이 이장로를 베었다!”

이장로의 가슴에서 검을 뽑아낸 진위경이 포효할 때, 멀지 않은 곳에서는 삼장로의 목이 떨어지고 있었다. 피를 뒤집어쓴 위팽이 그의 목을 들어 올렸다.

“삼장로의 목이 여기 있다!”

살아남은 이들이 잇따라 외쳤다.

“역도의 무리를 쓸어 버려라!”

“태원진가는 항산검문의 적이 아니다! 검을 거둬라!”

곳곳에서 울려 퍼지는 외침에 태원진가의 무인들이 힘을 얻었다.

수뇌부가 괴멸하다시피 한 항산검문 측은 아직 갈피를 잡지 못했으나, 이내 흑의인들을 향해 병장기를 돌렸다.

“자네 뭐 하고 있나! 태원진가 놈들이 코앞에 있는데…….”

“멍청한 소리 작작 하게. 덤비는 놈이라고는 저 시커먼 놈들밖에 없잖나!”

누군가의 말대로였다. 태원진가의 무인들은 수뇌부의 지시에 충실히 따랐고, 덕분에 항산검문의 무인들은 적이 하나 줄었음을 깨달았다.

이제 난데없이 나타난 흑의인들이야말로 공동의 적이었다.

“항산검문의 힘을 보여 줘라!”

“어디서 튀어나온 놈들인지 몰라도, 다 쓸어 버려!”

양 세력이 힘을 합치자 이제 밀리는 것은 흑의인들이었다.

그들은 혹독한 수련을 거친 정예였지만 두 장로의 죽음에는 사기가 흔들릴 수밖에 없었다. 틈을 놓치지 않고 사방에서 짓쳐 드는 칼날에 흑의인들은 하나둘씩 목숨을 잃었다.

“으아악!”

“물러서지 마라! 물러서는 놈은 죽음뿐이다!”

그 혼란 속에서도, 일장로는 묵묵히 검을 휘둘렀다.

눈에 닿고, 손이 향하는 곳 모두가 그의 적이었다.

서걱.

스물? 서른? 모르겠다. 일장로는 홀린 것처럼 가로막는 모든 것을 베어 냈다. 그중에는 한때 그를 어르신이라 부르던 이도 있었고, 약관이나 됐을 법한 어린 청년도 있었다.

‘죽고 사는 것에 나이가 무슨 상관이랴. 칼끝에 선 것이 무림인이거늘.’

수십 명의 피를 뒤집어쓴 일장로를 막아선 것은 곰 같은 덩치의 사내였다. 그의 눈빛은 모든 걸 태워 버릴 것 같았다.

“왜 그랬나?”

“부귀영화. 태원진가를 장악하고 산서 땅을 집어삼키기 위해서였지.”

한 치의 망설임도 없는 대답에 모든 이가 분노로 몸을 떨었다. 그러나 한 사람. 진위경만큼은 고개를 저었다.

“내가 원한 대답이 아니다.”

“그럼 소가주가 대답해 보시게. 내가, 내 형제들과 주공이 왜 이런 일을 벌였겠는가?”

“복수.”

진위경의 나직한 목소리가 이어졌다.

“당신이 말한 대계는 부귀영화나 일성의 패자가 되기 위한 것이 아니야. 그러기에는 이미 많은 기회가 지나갔고, 당신들은 늙었지. 그리고…….”

“그만.”

“대장로에게는 자손이 없다. 이장로, 삼장로, 그리고 당신도 마찬가지지.”

그 순간, 잔잔하던 일장로의 눈에서 시퍼런 불똥이 튀었다.

그건 오랜 세월 참아 온 분노였고, 아주 잠깐 떠올랐다 가라앉은 찌꺼기였다.

“왜 그랬나?”

일장로는 대답 대신 검을 들어 진위경을 겨눴다. 아니, 검 끝이 가리키는 건 진위경의 어깨 너머, 어딘가에 있을 한 사람이었다.

“그분께 직접 듣게.”

결국 마지막 열쇠는 대장로가 쥐고 있다.

진위경은 일장로를 향해 성큼 걸음을 내딛었다.

“그러지. 일장로, 당신을 베고 난 후에.”

“글쎄, 이렇게 여유를 부려도 되는 건가?”

“그게 무슨…….”

눈살을 찌푸리던 진위경의 얼굴이 딱딱하게 굳었다.

‘태경이!’

눈에 넣어도 아프지 않을 막냇동생이 대장로를 막고 있다.

잠시 잊고 있던 그 사실을 떠올린 순간, 전신의 피가 차갑게 식는 것 같았다.

‘더 이상 지체했다가는 돌이킬 수 없는 일이 벌어진다.’

모든 사태를 파악한 진위경의 입에서 서릿발 같은 음성이 터져 나왔다.

“위팽. 일장로를 맡아라.”

“받들겠습니다.”

“남은 분들도 힘을 보태 주시오.”

“소가주의 명을 받듭니다.”

위팽과 살아남은 중진 십여 명이 일장로를 넓게 포위했다.

“다른 이들은 나를 따라 길을 뚫어라! 대장로를 치러 간다!”

수십의 호위 병력과 함께 이동하려던 진위경은 문득 일장로를 바라보았다. 그는 최후가 다가왔음에도 어떤 동요도 보이지 않았다. 오히려 후련해 보이기까지 했다.

“일장로.”

“할 말이 남았나?”

진위경은 한마디를 툭 던졌다.

“태원진가 소가주의 권한으로 당신을 파문한다.”

“허허, 허허허!”

일장로의 웃음소리를 뒤로하고 진위경은 전장을 향해 질주했다.

수십의 흑의인들이 그를 저지하려 했으나 전세는 이미 기운 지 오래. 그들은 사방에서 몰려든 무인들에 의해 난자당해 죽었다.

“길을 뚫어라!”

“소가주님이시다! 막아서는 놈들은 모조리 죽여라!”

촌각에 불과한 시간. 그러나 진위경에게는 억겁과도 같은 시간이 흘렀다.

‘태경아, 부디, 부디…….’

차마 죽음이라는 단어는 생각조차 할 수 없었다.

두방망이질 치는 가슴을 끌어안고 얼마나 달렸을까, 이내 목적지에 도착한 그의 눈이 부릅떠졌다.

‘이게 무슨…….’

그만큼 눈앞에 벌어진 광경은 충격 그 자체였다.



* * *



레이드(Raid).

불과 수십 년 전까지만 해도 게임에서나 통용되던 단어다.

그러나 마왕의 등장과 대격변이 시작되자 레이드는 헌터들의 상징으로 자리매김했다.

그렇게 되기까지의 과정엔 수많은 실전과 희생이 있었고, 그걸 기반 삼아 마침내 오늘날의 레이드 방식이 정립되었다.

‘탱커, 딜러, 힐러.’

탱커는 막고, 딜러는 때리고, 힐러는 치료한다.

간단해 보이지만 정식 헌터가 되기 위해서는 엄청난 분량의 레이드 교본을 학습하고 실전 경험을 통해 검증받아야 한다.

‘헌터 훈련소…… 정말 지옥 같은 시간이었지.’

하지만 그 시간들을 견딘 덕분에 나는 헌터로 거듭났고, 7년 차 베테랑이 된 지금은 어떤 상황에서도 그에 맞는 포지션과 대응책을 떠올릴 수 있다.

그리고 지금.

“야, 흙 뿌려! 계속 뿌려!”

그동안 배운 모든 것들이 쥐뿔도 쓸모없다는 사실을 깨달았다.

탱커? 힐러?

씨바…….

근접 딜러 열 명으로 레이드를 생각한 내가 병신이다.
```

## Current accepted English baseline

```markdown
# Chapter 59

Shh-shh-shhk!

The fight between Jin Wikyung, Wipeng, and the three Elders was like a storm.

Sword strikes crashed together from every direction, too fast and fierce for an ordinary martial artist to follow.

Krshhk.

*Blocked.*

The instant he judged it, Wipeng flipped his body. The Second Elder’s thrusting sword grazed past his hair.

The Second and Third Elders pressed him as if they were a single body.

“You bastards!”

Jin Wikyung charged with a roar, only to have the First Elder cut him off.

“Where are you rushing off to?”

Sword Energy surged straight up, then dropped toward the crown of Jin Wikyung’s head.

A single stroke could split him in two. Jin Wikyung hastily raised his sword to block. A pale Sword Energy wreathed his blade as well.

Boom!

In the dust cloud that rose with the thunderous impact, a figure staggered back. Jin Wikyung’s face had gone pale. He spat a wad of bloody phlegm.

*What the hell kind of internal energy…*

He had trained in exceptional martial arts and taken elixirs since he was a child, but this was a bad matchup. The First Elder was a vile old monster who had lived more than sixty years with his black heart hidden.

Together with the Head Elder, he was a living witness who had fought his way through the Great Faction War.

“You damn old bastard.”

The First Elder answered with a hearty laugh.

“Lesser Family Head, mind your dignity.”

But the First Elder was not nearly as comfortable as he looked.

His trembling blade and throbbing wrist were proof enough.

*To think they were this strong.*

Even a street brawl came down to numbers. With masters, it mattered all the more. Yet Jin Wikyung and Wipeng were better than he had expected.

Or perhaps an old man’s pride had made him overrate himself.

*How cruel. Truly cruel.*

Sixty years. He had accumulated profound internal energy, but even that could not stop his body from aging.

*If only I were ten years younger.*

After a bitter jab at himself, the First Elder stepped toward Jin Wikyung.

The swords of his sworn younger brothers, the Second and Third Elders, grew even fiercer.

Shh-shh-shhk!

“Urgh!”

Jin Wikyung and Wipeng began to be pushed back. They had just fought the Peak masters of the Mount Heng Sword Sect, and that made it worse.

Their vision swam. Small wounds multiplied across their bodies. Their hands and feet no longer moved as they wanted.

*We can’t keep this up.*

Jin Wikyung’s face darkened.

Fwoooosh!

The First Elder’s Sword Energy had been driving in without pause when it suddenly changed course. In the next instant, a strike like lightning split its target.

Shhk.

Fwaaah!

A man staggered in a spray of blood. The sword that had been aimed at the First Elder’s side had shattered beyond recognition, and blood poured from his chest like a waterfall.

The First Elder confirmed his face and clicked his tongue.

“Discipline Hall Master, you foolish friend. Did you want to die that badly?”

“F-First Elder…”

The Discipline Hall Master’s voice sounded ready to break. He neither fell nor stopped talking.

“You have… violated the family’s laws.”

“Heh heh. And?”

“As the Discipline Hall Master of the Jin Family of Taiyuan, I command you. The guilty shall abolish their own martial arts and enter the Cave of Repentance…”

Shhk.

The First Elder answered with his sword. The Discipline Hall Master’s nature was straight as a bamboo stalk, but his martial arts were not high. He could neither see nor dodge the stroke that pierced his throat.

Fire poured from Jin Wikyung’s eyes.

“You bastard!”

Jin Wikyung was not the only one enraged. The Discipline Hall Master’s death set fire to the hearts of the Jin Family of Taiyuan’s senior members.

“Discipline Hall Master!”

Before they were martial artists, they were human.

They had lived long enough to have much they had built, and much they had to protect. That was why they had feared it: a Peak master’s prowess, thrown away on a dog’s death.

But the Discipline Hall Master’s dignified end brought the feelings they had set aside boiling back.

Shame, and anger.

“Strike down those rebels!”

“Show them the spirit of the Jin Family of Taiyuan!”

The ones who felt ashamed of themselves were the first to charge. They were senior members of the so-called Elders’ faction.

They could not forgive themselves for aiding the traitors. Nor could they forgive the Elders who had betrayed them and the family.

“Fools.”

Shhk. Shhk. Shhk.

Every time the three Elders’ swords flashed, another life went out.

The gap in strength was obvious. Even so, the Elders’ wrinkled faces had gone stiff.

*These bastards…!*

Dozens of First Rate masters, resolved to take their enemies with them, came on from every side without fear of death.

What rattled the Elders was not their opponents’ martial arts, but their momentum.

And in that gap, two men did not miss the opening.

Shhk.

“Gah!”

A scream tore from the Third Elder’s mouth. Before he knew it, Wipeng’s Sword Energy had surged up and cut across his side.

“Little brother!”

The Second Elder wavered at the cry of the sworn brother he had spent decades with. For the briefest instant, his attention went elsewhere.

It cost him dearly.

Three swords thrust out at once and skimmed his whole body. As the Second Elder scrambled back, a bolt of lightning shot toward him.

Fwoooosh!

The instant he felt something cold drive into his back, the Second Elder knew it was over.

Thuk!

It split flesh and severed bone. The Sword Energy ran wild like a living thing, tearing through his blood vessels and burning them.

How long had it been since he had felt pain like this?

The Second Elder’s vision went white. Soon he could not feel any pain at all.

“I, Jin Wikyung, Lesser Family Head of the Jin Family of Taiyuan, have cut down the Second Elder!”

As Jin Wikyung ripped his sword from the Second Elder’s chest and roared, the Third Elder’s head was falling not far away. Wipeng, soaked in blood, lifted it high.

“The Third Elder’s head is here!”

The survivors shouted one after another.

“Wipe out the rebels!”

“The Jin Family of Taiyuan is not the enemy of the Mount Heng Sword Sect! Lower your swords!”

The cries ringing from every direction put strength into the Jin Family’s martial artists.

Mount Heng’s command had been all but wiped out, and they still had not found their bearings. Before long, though, they turned their weapons on the black-clad men.

“What are you doing? Those Jin Family bastards are right in front of us—”

“Cut the stupid talk. The only ones coming at us are those black bastards!”

He was right. The Jin Family’s martial artists were following their command’s orders to the letter, and Mount Heng’s people realized one of their enemies had dropped away.

The black-clad men who had appeared out of nowhere were now the common enemy.

“Show them the strength of the Mount Heng Sword Sect!”

“I don’t know where you crawled out of, but we’ll wipe every last one of you out!”

Once the two forces joined up, it was the black-clad men who started to give ground.

They were elites hardened by brutal training, but the deaths of the two Elders were bound to shake their morale. Blades crashed in from every direction, wasting no opening, and the black-clad men began to die one after another.

“Aaargh!”

“Don’t fall back! Anyone who falls back dies!”

Even in that chaos, the First Elder swung his sword without a word.

Everything his eyes fell on, everything his hands reached toward, was an enemy.

Shhk.

Twenty? Thirty? He didn’t know. Like a man possessed, the First Elder cut down everything in his way. Among them were people who had once called him Elder, and young men who looked barely twenty.

*What does age matter to living and dying? Anyone who stands at the point of a sword is a person of Murim.*

What blocked the First Elder, drenched in the blood of dozens, was a man built like a bear. His eyes looked ready to burn everything to ash.

“Why did you do it?”

“Wealth and glory. To take the Jin Family of Taiyuan and swallow Shanxi whole.”

The answer came without a hint of hesitation, and everyone trembled with rage.

Everyone except one. Jin Wikyung shook his head.

“That isn’t the answer I wanted.”

“Then you answer, Lesser Family Head. Why would I, my brothers, and our lord do a thing like this?”

“Revenge.”

Jin Wikyung’s quiet voice went on.

“The grand plan you talked about wasn’t for wealth and glory, or to become the ruler of a single province. Too many chances for that have already passed, and you’re all old. And…”

“Enough.”

“The Head Elder has no descendants. Neither do the Second Elder, the Third Elder, or you.”

In that instant, a livid spark leapt from the First Elder’s still eyes.

It was anger he had held down for a very long time—dregs that rose for the briefest moment, then sank again.

“Why did you do it?”

Instead of answering, the First Elder raised his sword and pointed it at Jin Wikyung.

No—the tip pointed past Jin Wikyung’s shoulder, toward someone who would be standing somewhere beyond him.

“Hear it from him yourself.”

In the end, the last key was in the Head Elder’s hands.

Jin Wikyung took a long stride toward the First Elder.

“I will. After I cut you down.”

“Well? Can you really afford to take it this easy?”

“What do you—”

Jin Wikyung’s frown went rigid.

*Taekyung!*

His youngest brother, the apple of his eye, was standing in the Head Elder’s way.

The instant he remembered what he had let slip, it felt as if every drop of blood in him ran cold.

*If I delay any longer, something irreversible will happen.*

Once he grasped the whole situation, a voice like frost burst from Jin Wikyung’s mouth.

“Wipeng. Take the First Elder.”

“I obey.”

“The rest of you, lend him your strength.”

“We follow the Lesser Family Head’s command.”

Wipeng and some ten surviving senior members spread into a wide ring around the First Elder.

“Everyone else, follow me and break through! We’re going after the Head Elder!”

Jin Wikyung was about to move with several dozen guards when he glanced at the First Elder. Even with his end closing in, the man showed no agitation. If anything, he looked unburdened.

“First Elder.”

“Do you have something left to say?”

Jin Wikyung tossed out a single line.

“By the authority of the Lesser Family Head of the Jin Family of Taiyuan, I expel you from the family.”

“Heh heh. Heh heh heh!”

Leaving the First Elder’s laughter behind him, Jin Wikyung sprinted for the battlefield.

Dozens of black-clad men tried to stop him, but the fight had long since turned. Martial artists poured in from every side and hacked them apart.

“Open a path!”

“It’s the Lesser Family Head! Kill anyone who gets in his way!”

It was only a moment. For Jin Wikyung, an eternity passed.

*Taekyung. Please, please…*

He could not even let himself think the word *death*.

How long had he run with his pounding chest clutched in his arms? When he finally reached his destination, his eyes flew wide.

*What is this…*

The scene in front of him was shock itself.

* * *

Raid.

Until a few decades ago, it was a word that only meant anything in games.

But after the Demon King appeared and the Great Cataclysm began, raids became the symbol of Hunters.

Getting there had taken countless real battles and countless sacrifices. On that foundation, the raid methods used today had finally been set down.

*Tank, damage dealer, healer.*

The tank blocks. The damage dealer hits. The healer heals.

It sounded simple, but to become a proper Hunter you had to study a mountain of raid manuals and prove yourself in actual combat.

*Hunter training camp… that was a living hell.*

But because I endured it, I came out a Hunter. Now, as a seven-year veteran, I can pull the right position and the right response for any situation.

And right now—

“Hey, throw dirt! Keep throwing it!”

I realized that everything I’d learned wasn’t worth shit.

Tank? Healer?

Fuck…

I was a fucking moron for thinking ten melee damage dealers counted as a raid.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 59`.
