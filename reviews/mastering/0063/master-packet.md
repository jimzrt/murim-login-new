# Master Edit Task — Chapter 63

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
| 혁무진    | **Hyuk Mujin**     |
| 이천백    | **Lee Cheonbaek**  |
| 이소군    | **Lee Seogeun**    |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 이류     | **Second Rate**   |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 내공     | **internal energy**                              |                                                       |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 중원     | **Central Plains**                               |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 수문조장   | **Captain of the Gatekeepers**               |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 시스템              | **System**                     |
| 상태창              | **Status Window**              |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 명성               | **Fame**                       |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 로그아웃             | **Logout**                     |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 매력               | **Charm**                      |
| 헌터      | **Hunter**            |
| 팀장      | **Team Leader**       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 염라편 | **Yama Whip** |
| 녹림십팔채 | **Eighteen Strongholds of Green Forest** | |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |

## Chapter-safe character profiles

(No chapter-safe profiles available. This is expected for early retrospective chapters.)

## Chapter-safe bounded continuity

### Latest prior summary

# Chapters 55–59

## Plot

Taekyung wakes in Murim after roughly two hours of deathlike sleep and learns that the reconnaissance squad has sent messengers to the Jin Family’s main force. He orders the exhausted squad to reach Eight Spring Gorge before the battle is lost. There, Mount Heng’s larger army is trapped in the Jin Family’s terrain-controlled gorge while hidden cliff archers fire on them. Lee Cheonbaek leads Mount Heng’s core forces in a desperate assault, but the Head Elder overwhelms him with Sword Energy and prepares to kill him.

Taekyung arrives, splits a spear aimed at the Head Elder, and publicly brands him a traitor. The Jin Family’s First, Second, and Third Elders reveal concealed Peak-level abilities and turn against their own side. A signal flare prompts the embedded Three Paths Sect, Byeokdo Sect, Gunggwimun, and other Five Gates of Shanxi forces to attack their supposed allies, exposing a decades-old conspiracy. The Head Elder confirms that “they” killed Lee Seogeun but does not identify the accomplice or explain the complete plan.

The Discipline Hall Master dies defending the Jin Family’s laws, rallying the Jin and Mount Heng fighters against the black-clad conspirators. The Second and Third Elders are killed, while the First Elder admits greed and glory as his stated motives and points Taekyung toward the Head Elder when Taekyung identifies revenge as the deeper cause. Jin Wikyung expels the First Elder and leaves him surrounded by Wipeng and ten senior members before leading guards toward Taekyung.

Taekyung attacks the Head Elder with the Gambler Title active but is decisively overpowered. The elder cuts his spear down to an iron rod. While trying to rescue Jin Wikyung, Taekyung grabs the wrong person and escapes with the gravely wounded, silenced, and paralyzed Lee Cheonbaek. With Hyuk Mujin and the reconnaissance squad, he forms an encirclement against the Head Elder, belatedly realizing that his raid-party tactics are useless without a tank, healer, or ranged damage dealer. The battle remains unresolved.

## Continuity

- The Eight Spring Gorge battle continues. The Head Elder remains the dominant combatant and can overpower Taekyung’s Gambler-boosted attacks with Sword Energy.
- The Head Elder’s betrayal and the Five Gates conspiracy are exposed, but the accomplice who killed Lee Seogeun, the meaning of the signal, the revenge motive, and the full conspiracy remain unresolved.
- The Second and Third Elders are dead. The First Elder is alive, expelled from the Jin Family, and surrounded by Wipeng and ten senior members; his fate is unresolved.
- Jin Wikyung is alive and leading guards toward the Head Elder. Taekyung mistakenly rescued Lee Cheonbaek instead of Wikyung.
- Lee Cheonbaek remains alive but unable to speak or move. Taekyung, Hyuk Mujin, and the reconnaissance squad are confronting the Head Elder.
- Taekyung knows that logging in or logging out leaves the other side in a deathlike sleep. The Ark - 2020 capsule’s safe operation, ultimate purpose, and route between realities remain unresolved.
- Taekyung’s Traitor Chain Quest remains active and requires punishing the traitor and leading the battle to victory; failure means death.

## Translation Decisions

- Preserve **Head Elder**, **First/Second/Third Elder**, **Discipline Hall Master**, **Peak master**, **Sword Energy**, **Blood Wolf Sword**, and **Blood Rain Group**.
- Use **Eight Spring Gorge**, **Three Paths Sect**, **Byeokdo Sect**, and **Gunggwimun** consistently.
- Retain the raid framing—**tank**, **healer**, and **damage dealer**—and Taekyung’s dry, profane self-mockery.
- Preserve the Head Elder’s unresolved Sound Transmission reveal that “they” killed Lee Seogeun.
- Keep **Gambler** as the System Title and **logged in** only for Taekyung’s connection to Murim.

### Prior accepted reading-copy tails

#### Chapter 61 tail (accepted)

…
to take revenge.” If holding out ten years made you a gentleman, did holding out forty make the Head Elder Jesus? It was nothing more than a crazy old man’s self-justification. “You run your mouth just because you’ve got one.” “I did. What are you going to do about it?” “Do you think you know everything?” “Do I have to? After it’s gone this far?” The question was so obvious I snorted a laugh and pointed at the battlefield. A mountain of corpses, a sea of blood. Utter pandemonium. The scene in front of us was exactly that. “That…” The chill in the Head Elder’s eyes wavered. But only for an instant. “I see. What more is there to say?” He muttered it like a jab at himself, then raised his sword. “Head Elder.” Jin Wikyung’s lips moved, and that was all. A fight that ended only when one side died. They had come too far to turn back. “Come.” I wasn’t about to decline. “Attack!” It was time to hunt the wounded beast. * * * I remembered the first day I saw the Head Elder. A bearing and dignity that made his age meaningless. His white beard called an immortal to mind. Fwoosh! Of course, there were no immortals who mercilessly cut people in half. *Even rotten, a prized fish is still a prized fish.* Drenched in blood, he swung his sword without pause. Looks mixed with awe and fear poured toward him. “Monster…” He had lost an arm, but the Head Elder was still strong. He just clearly wasn’t as strong as before. *This is doable.* Peak master or not, the martial artists here were the Jin Family of Taiyuan’s elite. Men who had fought across the battlefield under Jin Wikyung, skilled enough to have survived the earlier clash with the Head Elder. Clang-clang-clang! The Head Elder knocked aside blades driving in from every direction, his face darkening. In the old days, he would have cut down everything in his path with Sword Energy. Proof that the internal energy that had once seemed like a spring that never ran dry had finally hit bottom. On top of that, his aged body had reached its limit. Shraaaak! Sword wounds began to multiply across the Head Elder’s body. Unlike before, most of the blood was his. *Now!* I wasn’t about to miss that opening. The spear I drove with everything I had tore a handful of flesh from his side. “Hk!” Even through the pain, the Head Elder cut down a martial artist and charged me. He meant it this time; a faint Sword Energy gathered along the swinging blade. But… Shhk. The Sword Energy scattered in a rising spray of blood. Jin Wikyung appeared behind the staggering Head Elder. “I’d forgotten you were there.” The Head Elder turned with a twisted face. “Did my elder brother teach you to put a knife in someone’s back?” “My family members are dying. Is a sneak attack really that important?” “Aren’t you ashamed, as a martial artist?” “I am the Lesser Family Head before I am a martial artist.” “The Lesser Family Head, is it? Heh heh.” Jin Wikyung looked at the Head Elder with a complicated expression. “The tide has already turned.” “So? Are you going to ask me to surrender?” “Please stop this meaningless fight.” The flow of the battlefield had been ours for a long time. But the black-clad men kept resisting stubbornly, and the screams and corpses still showed no sign of thinning out. “You’re right. It may be a meaningless fight. But…” The staggering Head Elder straightened his back. A sharp gleam was already flashing in his eyes, and a blade-like aura began to rise. “We’ve come too far to stop.” A last desperate struggle? No. More than that. Someone suddenly came to mind. Jopil. The last sight of him as he was dying overlapped with the Head Elder now. *Innate qi. He’s drawing up his innate qi.* If internal energy was acquired power, piled up by circulating qi and taking elixirs, innate qi was the opposite. It was the root of the human body—life force itself, for all intents. The Head Elder was staking his life to use it. “Cough.” He spat blood and raised his sword. His life was going out fast, but his sword shone more brilliantly than it ever had. The moment I saw that overwhelming sight, a single word slipped out of me. “Sword Force…” It was instinct. My heart pounded just from looking at it. I could feel a terrifying power that far outstripped Sword Energy. And then— “Yes. You were here.” His red eyes, the capillaries bursting one after another, locked on me. Jin Wikyung lunged to stop the Head Elder. “No!” But the Head Elder was already gone from that spot. In a single step he compressed fifty feet and brought his sword down on me. Whoooong. *So this is how I die.* An attack I couldn’t dodge or block. I was dead. I was going to die. But… *I can’t die like this.* I wrung every muscle in my body. The last scant handful of internal energy raced for the spearhead. It was a final struggle, and a show of respect for the life I had lived so fiercely until now. “One Flash.” Shiiiiiiing! The last strike, carrying every bit of strength I had left, shot forward.

#### Chapter 62 tail (accepted)

…
this road. Scatter as widely as you can and get out of Shanxi. If you do, you may at least save your lives.” The martial artist nodded resolutely. “I will follow you until I die.” “I… will remain here.” “What?” The confusion lasted only a moment before the martial artist's voice began to tremble with feeling. “Is it because of us?” “Not at all.” Jin Chung answered firmly, but his thoughts were different. *If I followed them, the Jin Family of Taiyuan would hunt them relentlessly.* The Five Gates of Shanxi were many, yet one. One, yet many. They had been created for the same purpose, but each sect had raised its martial artists in a different way. Jin Chung had not raised them as weapons. He had taken them in as disciples. “Sect Leader!” “Please lead us!” Every one of them had been an orphan with nowhere to go. For at least ten years—twenty or more in some cases—he had fed them, sheltered them, and taught them martial arts. If the grand scheme had succeeded, they would have become the backbone of Shanxi's Murim. Now that it had failed, they were nothing more than traitors. “Do you not understand how this is going?” “Even if we die, we will die with you, Sect Leader.” “You brat!” “Please allow us.” The martial artist who had stepped forward first slammed his forehead against the stone floor. Then, one by one, his disciples began to kneel. Jin Chung looked up at the sky and lamented. “If only the grand scheme had not been delayed. If only they had stepped forward!” Talk of *them* was a secret known only to the eight at the top. To speak those words aloud was no different from deciding to share his final moments with his disciples. *This too must be heaven's will.* Jin Chung turned his gaze from the dark night sky and helped the prostrate martial artist to his feet. He felt endlessly sorry—and deeply moved—by the loyalty the man had shown. “That's enough. Get up.” At the warmth in his voice, the martial artist lifted his head. He flicked his tongue over the trickle of blood running down his forehead, then gave a crooked grin. “Yes.” Thuck! Jin Chung stared at the martial artist with a blank look. The shock was so great he could not even feel pain. *What in the world…?* Shwaaak! The martial artist pulled his hand from Jin Chung's chest. A glow brighter than moonlight clung to it—a blood-red Force that inspired dread just to look at. “You…” “You already know, so why ask? Oh, and about what you just said—I'll give you a simple answer.” The martial artist's smile deepened. “Why would we step forward? Your role ends right here.” Jin Chung's eyes flew wide. *Them.* The unknown beings who had never revealed themselves until the very end. Dark Heaven! “You bastards!” “Don't look at me like you've been used. Forgotten who got you out of that hell alive?” Jin Chung remembered the nightmare from forty years ago. The corpses of allies covering the ground around him. The endless army of the Demonic Cult surging in. They had gathered around the Head Elder and prepared themselves to die. That was before Dark Heaven appeared. “We saved your lives and gave you a chance at revenge. What more did you want?” He was right. Dark Heaven had annihilated the Demonic Cult's army, then proposed a deal. They had accepted. They had to have a gu planted in their heads, but they would have done anything for revenge.[^2] But… “Wasn't your real aim to use us to rule Shanxi?” “Well, maybe that was the plan at first.” “Then what was it all for?” The martial artist grinned. “A bigger picture.” At the same time, his bloodstained hand pressed against Jin Chung's chest. Boom. A small explosion went off inside Jin Chung's body. The energy burst his eardrums, severed his blood vessels strand by strand, and reached his heart. *Just like this…* The thought went no further. Jin Chung's body, already dead, flew like a bird and plunged off the cliff. Shiiiiik! Crash! The martial artist glanced down and grimaced. “Ouch. That must've hurt.” When he turned around, screams and blood were waiting for him. Ten black-clad men who had appeared out of nowhere were massacring Gunggwimun's disciples. “Let's finish this quickly and go.” “As you command.” Shreeeeek! Thud! The martial artist turned his gaze toward the bottom of the cliff. Screams erupted all around him, but below the cliff the air was filled with cheers and shouts. “The Sleeping Dragon of Shanxi!” “Jin Taekyung! Jin Taekyung!” “The Sleeping Dragon of Shanxi…” The plan had succeeded. But Jin Taekyung's appearance had been a variable even he had not anticipated. He did not like that. *Take him out, or let him be?* If he set his mind to it, he could rip him out by the roots. His deepening gaze turned toward Jin Taekyung, ringed by cheers. “Our youngest! My little brother!” “Let go! Let go, you bastard!” A snort of laughter escaped him. *I'll let you live. For today.* The martial artist turned away. Some fifty corpses lay like a carpet in his wake. [^1]: 弓鬼門, lit. Bow Ghost Gate. [^2]: A *gu* is a traditional poison associated with venomous creatures; in Murim fiction, it may be implanted in a person's body.

## Korean source

```text
＃63화



끼이이익.

사내가 객잔에 들어온 것은 미시(未時) 무렵이었다.

낡은 나무문이 삐걱댔지만 객잔 안의 사람들은 아무도 돌아보지 않았다. 심지어 잽싸게 손님을 맞이해야 할 주인과 점소이마저 그랬다.

“그래서, 그래서 어떻게 됐소?”

“거, 자꾸 애타게 하지 말고 말을 좀 해 보쇼!”

사람들의 열광적인 반응에 노인이 빈 대접을 톡톡 두드렸다.

결국 주인이 죽엽청을 넘치도록 따른 후에야 노인, 매담자(賣談者)의 이야기가 이어졌다.

“치열한 격전이 벌어졌지. 혈랑검 이천백이 끌고 온 자들만 물경 삼만. 그에 비해 태원진가는 삼백의 정예가 전부였어.”

“삼만!”

“세상에, 삼만이라니!”

“그게 말이 되오? 항산검문이 무슨 구파일방도 아니고…….”

매담자가 죽엽청을 마시다 말고 도로 뱉었다.

“에이, 시발. 술맛도 더럽게 없네. 나 갈 테니까 저 구파일방 운운하는 놈한테 나머지 얘기 들으쇼.”

“어허. 왜 이러시오.”

“방금 말한 놈 누구야!”

흉흉해진 분위기에 한 청년이 엉거주춤 밀려났다.

그제야 매담자가 반쯤 뗐던 궁둥이를 다시 내려놨다. 하지만 비위가 상한 만큼 배포도 두둑해진 상태였다.

톡톡.

빈 대접을 두드리는 매담자의 모습에 모두가 인상을 썼다. 이제는 술이 아니라 돈을 줘야 한다. 사람들이 보이지 않는 눈치 싸움을 하고 있던 그 순간이었다.

팅.

“어?”

게슴츠레하던 매담자의 눈이 동그랗게 뜨였다. 번쩍거리는 은자 한 냥이 어디선가 날아온 것이다.

“허, 누군지 통도 크네.”

“누구야?”

“왜 날 봐? 마누라한테 맞아 죽을 일 있어?”

그때 사람들의 등 뒤에서 한 사람이 입을 열었다.

“이야기를 더 듣고 싶은데.”

나직하지만 울림이 있는 목소리. 앞서 객잔에 들어온 사내였다. 죽립을 푹 눌러쓴 탓에 얼굴은 제대로 보이지 않았고, 전신을 감싼 피풍의는 먼지투성이였다.

‘무림인.’

누가 말을 보태지 않아도 사람들은 모두 사내의 정체를 그렇게 생각했다.

매담자가 은자와 사내를 번갈아 보며 침을 삼켰다.

“감사합니다, 대협. 혹시 듣고 싶은 이야기가 있으신지……?”

그의 경험상 무뢰배와 무림인은 한 끗 차이다. 매담자는 살 만큼 산 노인이었으나 고작 이런 곳에서 칼 맞아 죽고 싶진 않았다.

다행히도 죽립 사내는 후자에 해당했다.

“간단하게. 사실만.”

목소리를 들어 보면 어린노무 새끼가 분명한데, 무공을 배운 어린노무 새끼다. 함부로 대할 순 없었다. 매담자는 손바닥을 비볐다.

“제가 아는 선에서 싹 다 말씀드리겠습니다요.”

“노인장이 말한 그 전투, 며칠 전 이야기요?”

“닷새 전입니다.”

“누가 이겼소?”

“태원진가가 시원하게 발라 버렸습죠. 산서잠룡이 큰 활약을 했다고 들었습니다.”

“그럼 항산검문은…… 지금 뭐라고 했소?”

“예?”

“산서, 뭐?”

“아, 산서잠룡 말입니까요?”

“맞소. 처음 듣는 별호인데.”

“외지에서 오셨다면 그럴 수도 있지요. 진 공자가 두각을 드러낸 것이 얼마 되지 않았으니.”

“소가주인 진위경 공자 말이오?”

“예에? 천만에요. 소가주님도 대단하지만, 이번에 가장 활약이 컸던 것은 아무래도 진 공자죠.”

“그러니까 그 진 공자가…… 잠깐, 지금 말하는 산서잠룡이 설마 삼공자 진태경과 연관이 있소?”

“동일 인물입죠.”

한동안 침묵을 지키던 사내가 손가락을 튕겼다. 두 번째 은자가 매담자의 대접에 정확히 안착했다.

“간단하게. 사실만 말해 달라고 했던 것 같은데.”

“제 불알을 걸겠습니다.”

매담자의 결연한 대답에 사내가 한숨을 내쉬었다.

“그렇다 칩시다. 항산검문은 어찌 되었소?”

“거의 봉문 직전입니다. 이공자 이소군은 진즉 죽었고, 문주인 혈랑검 이천백은 전사. 이틀 후에 후계자인 대공자도 마적 떼에 맞서다가 죽었답니다.”

“마적?”

“이 간 큰 놈들이 글쎄, 혈랑검이 죽었다는 소식에 항산검문으로 쳐들어왔답니다. 처음부터 그걸 노리고 인근을 배회하고 있었다는군요.”

“개판이군.”

“말판이죠. 마적 떼들 아닙니까.”

장내가 쥐 죽은 듯이 조용해졌다. 사람들은 저 통 큰 무림인 사내가 세 번째 은자를 매담자의 이마에 박아 넣는 모습을 기대했지만, 그는 군말 없이 자리에서 일어났다.

“이야기 잘 들었소.”

사내가 떠난 후에도 매담자의 이야기는 이어졌다. 그들은 쉴 새 없이 술을 들이켰고, 안주는 끊이지 않았다.

무림인들 간의 패권 다툼. 승리와 패배. 샛별처럼 떠오른 젊은 영웅의 이야기에 대해 입을 모아 떠들었다.

“태원진가가 산서를 넘어 중원에 우뚝 설 날이 얼마 남지 않았군. 문무겸전의 소가주에, 이번에 두각을 드러낸 산서잠룡. 그리고…… 그리고 또 누구더라.”

“진천검?”

“아, 그래. 이공자 진무경!”

“그 젊은이도 대단하지. 백 년에 한 번 나올까 말까 한 무학의 천재라며?”

“근데 지금은 어디서 뭐 하고 있대?”

“몰러. 이 시간이면 자고 있겄지.”

객잔의 술자리가 이어지는 그 순간에도 사내는 묵묵히 말을 몰았다. 굳게 다문 입과는 달리 그의 귀는 활짝 열려 있었다.

“자네 그 얘기 들었나?”

“또 산서잠룡인가? 귀에서 피 나니까 작작 하게.”

“그렇긴 한데…… 이건 일급 정보야. 태원진가 수문각 무사한테 들은 거거든.”

“뭔데 그렇게 호들갑이야?”

“천력부라고 아나?”

“녹림십팔채의 그 천력부? 산적 주제에 절정 고수라는 그놈?”

“그래. 바로 그 천력부도 산서잠룡이 해치웠다는군!”

“헛소문 아니야? 천력부쯤 되는 작자가 굳이 왜 산서성까지 와서 산적질을 해?”

“난들 아나. 더 놀라운 건 그 자리에 염라편(閻羅鞭)도 있었다는 거지.”

“헉. 염라편까지!”

“홍화루에서 마부로 위장하고 있다는데. 혹시 갈 일 있으면 주의하게나.”

사람들의 끊이지 않는 대화 속에서 가장 많이 들리는 단어는 두 가지였다. 산서잠룡. 그리고 진태경.

목적지에 가까워질수록 소문은 눈덩이처럼 불어나 크기를 키웠다.

‘고금 제일의 미남에. 하늘이 내린 천무지체. 불의를 보면 참지 못하는 협객.’

죽립 사내는 말에 박차를 가했다. 산서잠룡의 산 자만 들어도 내상을 입은 것처럼 속이 울렁거리고 머리가 아파 왔다.

마침내 그가 목적지에 도착한 것은 다음 날 아침이었다.

‘오랜만이군.’

수년 만에 돌아온 그곳은 여전했다.

굳이 변화가 있다면.

“멈춰라! 이 몸은 산서성의 패자, 대태원진가의 수문조장이자 산서잠룡의 오른팔 혁무진이다. 순순히 신원과 목적을…….”

영 상태가 안 좋아 보이는 놈이 수문조장을 맡고 있다는 것.

죽립 사내, 진무경이 한숨을 내쉬었다.

“입 닥치고 문 열어.”



* * *



쏴아아.

물결이 흐른다. 잔잔하게, 그리고 거침없이.

단전에서 흘러나온 공력은 수백 개의 혈도를 질주하다가, 마침내 본래 있어야 할 자리로 돌아갔다.

띠링.



- [운기조식]을 성공적으로 마쳤습니다.

- [진가심법]의 경지가 팔 성으로 상승합니다.



시스템 알림을 들으며 눈을 떴다.

‘팔 성이라.’

분명 좋은 소식이지만 살짝 실망감이 드는 건 어쩔 수 없다.

내가 기다렸던 알림은 따로 있었으니까.

‘공력이나 좀 오르지.’

시스템을 사용할 수 있게 된 지 오늘로 두 달째. 이제는 습관처럼 하는 운기조식이지만 공력은 여전히 제자리걸음이다.

‘지금 속도라면 10년은 더 걸리겠네.’

내가 익힌 진가심법의 최대 장점은 매우 안정적이라는 것이다. 일반적인 내공 심법과는 달리 움직이면서도 심법 운용이 가능할 정도다.

문제는…….

‘공력 축적 속도가 더럽게 느리다는 거지.’

무림인에게 있어 공력의 부재는 치명적인 단점이다.

일류, 이류 정도야 손쉽게 상대할 수 있겠지만 절정 고수를 적으로 만나면 목숨이 두 개여도 모자라는 것이 현실이다.

이번에 대장로의 무위를 직접 겪으면서 확실히 느꼈다.

‘대단했지, 그 영감.’

닷새가 지난 지금에도 잊히지 않는다.

아니, 닷새가 아니라 50년 후에도 잊지 못할 광경이었다.

전장을 휩쓸던 검기와 검강. 그리고 95레벨이라는 말도 안 되는 숫자.

‘일대일이었으면 얼마나 버틸 수 있었을까?’

젖 먹던 힘까지 쥐어짜도 1분은 버텼을지 의문이다.

하지만 예상치 못한 변수들이 결과를 뒤집었고, 나는 그의 가슴에 창을 박아 넣을 수 있었다.

그리고 시스템은 보상을 잊지 않았다.

“상태창 오픈.”

띠링.



상태창



[Lv.50 진태경]

직업 : 일류 무인

명성 : 1180 (+150)

칭호 : 4개 (칭호 효과 적용 중)

- 산서잠룡 (모든 능력치 +10, 명성 +100)

- 명가의 자제 (모든 능력치 +5, 명성 +50)

- 초보 수련자 (수련 속도 +10%)

- 승부사 (일대일 전투 시 전투 관련 능력치 +10%)

근력 : 135 (+15)체력 : 142(+15)

민첩 : 130 (+15)지력 : 25(+15)

매력 : 25(+15)공력 : 15년

잔여 포인트 : 100

- 잔여 포인트를 분배하십시오.





“크으.”

지난 며칠간 수십 번은 확인한 상태창이지만 질리지가 않는다. 혈관에서 탄산이 톡톡 튀는 이 기분.

‘대장로와 싸운 보람이 있구만.’

목숨을 건 도박이었던 만큼 보상도 빵빵했다.

단숨에 13레벨을 껑충 뛰어올랐고, 명성은 세 자릿수에 접어들었으며 칭호에도 변화가 있었다.

“칭호 확인.”

띠링.



상태창



[산서잠룡]

등급 : 절정

효과 : 모든 능력치 +10, 명성 +100

설명 : 이제 당신의 명성은 산서성 곳곳에 퍼져 있습니다. 그러나 천하는 넓고 고수는 많은 법. 결코 자만하지 마십시오!





아직 전국구 급은 아니지만 산서성이라는 우리 지역구에서는 침 좀 뱉는다는 말인데…….

‘그래서 산서잠룡인가?’

고양시 꿀주먹. 인천 피바다. 뭐 그런 느낌.

어쨌든 내게는 잘된 일이다. 산서잠룡이라는 좋은 칭호에, 얼마 전까지만 해도 꼬리표처럼 붙어 있던 [가문의 수치]가 사라지니 앓던 이가 빠진 것처럼 시원했다.

‘이렇게 또 강해졌구나.’

문득 무림으로 돌아오기 전, 최 팀장과 했던 대화가 떠올랐다. 다음에 나를 볼 때는 계약서를 고쳐야 할 거라는 말.

그는 허풍으로 받아들였겠지만 나는 사실로 만들었다.

‘최대한 강해져서 돌아간다.’

내가 얻을 수 있는 힘을 최대한 얻어서 돌아갈 것이다.

공력, 무공, 능력치. 그게 뭐든 간에 모조리.

다음 로그아웃 때는 B급, 아니 A급 헌터 정도는 되어서 금의환향을…….

“어?”

아니, 잠깐만.

나 지금 뭔가 엄청 중요한 걸 잊고 있는 것 같은데.

‘뭐지?’

하고 있던 모든 걸 멈추고 기시감의 정체를 고민하던 그때였다.

“여기냐?”

“옙. 틀림없습니다요.”

문밖에서 두런두런 들리는 두 개의 목소리. 그중 하나가 혁무진이라는 사실을 알아차린 순간.

쾅!

굉음과 함께 문이 뜯겨 나갔다.



* * *



나는 기본 상식을 중요시하는 사람이다.

휴지는 휴지통에. 담배는 흡연 구역에서. 야동은 일본.

그리고 다른 사람 방에 들어갈 때는 노크를.

특히 남자 혼자 쓰는 방에 노크도 없이 벌컥 들어오는 놈들은 무기징역에 처해야 한다고 생각하는 사람이다.

“여기 있었군.”

그런 의미에서 눈앞의 이놈은 사형이다.

문을 박살 냈으니까 무기징역. 초면에 말을 놨으니 가중 처벌.

나는 점잖게 대꾸했다.

“어, 여기 있다.”

놈이 눈을 동그랗게 떴다. 아오지 탄광에서 20년쯤 일하다 왔는지 얼굴이 시커멓게 때가 껴 있었다.

젊은 나이에 초라한 행색. 대충 스토리가 나오는 듯했다.

‘떠돌이 무사1.’

산서잠룡의 명성을 듣고 무작정 찾아온 엑스트라.

나는 놈과 비슷한 표정을 짓고 있는 혁무진에게 물었다.

“얘 뭐냐?”

혁무진이 그대로 얼어붙었다. 귀신이라도 본 얼굴이다.

“모르세요?”

“내가 어떻게 알아, 인마. 소개를 해 줘야 알지.”

나는 투덜거리며 [기감]을 끌어 올렸다. 푸른 원이 두 사람을 향해 쭉 뻗어 나간다.



[Lv.??? 진무경]



진무경이라. 레벨 좀 되나 보네?

“응? 진무경?”

레벨창 한 번 보고. 얼굴 한 번 보고.

그 짓을 서너 번 반복하다가 떨리는 마음으로 그에게 다가갔다.

“저, 잠시만.”

“…….”

문질문질.

깨끗하던 내 옷소매가 까맣게 변한다. 이어 잘생긴 얼굴이 드러났다. 어디서 많이 본 얼굴이다 싶더니 매일 아침 세수하면서 마주하는 내 얼굴이다.

‘완전히 붕어빵이네.’

허허.

나는 어색하게 웃어 보였다. 떠돌이 무사1은 얼음장 같은 시선으로 나를 노려보고 있었다.

“오랜만이야, 형.”
```

## Current accepted English baseline

```markdown
# Chapter 63

Creeeak.

The man entered the inn around early afternoon.

The old wooden door creaked, but no one inside turned to look. Not even the owner and the waiter, who should have been rushing to greet a customer.

“So? So what happened?”

“Quit keeping us in suspense and tell us already!”

At the crowd’s eager urging, the old man tapped his empty bowl.

Only after the owner filled it to overflowing with bamboo-leaf wine did the old man—the storyteller—go on.

“A fierce battle broke out. Blood Wolf Sword Lee Cheonbaek brought no fewer than thirty thousand men. Compared to that, the Jin Family of Taiyuan had only three hundred elites.”

“Thirty thousand!”

“My word, thirty thousand!”

“Does that make any sense? Mount Heng Sword Sect isn’t one of the Nine Sects and One Gang…”

The storyteller stopped mid-sip and spat the wine back out.

“Fuck this. This booze tastes like shit. I’m leaving. Hear the rest from the guy who brought up the Nine Sects and One Gang.”

“Now, hold on. Why are you doing this?”

“Who just said that?”

The mood turned ugly, and a young man was shoved back, half-stumbling.

Only then did the storyteller set his half-raised ass back down. His stomach had turned, and his nerve had thickened to match.

Tap, tap.

Everyone frowned as the storyteller tapped his empty bowl. Now they had to give him money, not more wine. They were in the middle of an unspoken standoff when—

Ting.

“Huh?”

The storyteller’s narrowed eyes flew open. A gleaming silver tael had come flying from somewhere.

“Well. Whoever that is, they’re a big spender.”

“Who was it?”

“Why are you looking at me? You trying to get me beaten to death by my wife?”

That was when someone spoke from behind the crowd.

“I’d like to hear more.”

The voice was quiet but resonant. It belonged to the man who had entered the inn earlier. His face was hidden under a bamboo hat pulled low, and the cloak wrapped around him was caked with dust.

*A martial artist.*

Nobody needed to say it. Everyone in the inn came to the same conclusion.

The storyteller looked from the silver to the man and swallowed.

“Thank you, Great Hero. Is there something in particular you’d like to hear…?”

In his experience, ruffians and martial artists were only a hair apart. He was an old man who had lived his share of years, but he had no desire to get stabbed to death in a place like this.

Fortunately, the man in the bamboo hat was the latter.

“Keep it simple. Just the facts.”

Judging by the voice, he was clearly a young bastard—but a young bastard who had learned martial arts. The storyteller couldn’t treat him carelessly. He rubbed his palms together.

“I’ll tell you everything I know, sir. The whole lot.”

“That battle you mentioned. How many days ago was it?”

“Five days ago.”

“Who won?”

“The Jin Family of Taiyuan wiped the floor with them. I heard the Sleeping Dragon of Shanxi played a major role.”

“Then Mount Heng Sword Sect… What did you just say?”

“Excuse me?”

“Shanxi, what?”

“Ah, you mean the Sleeping Dragon of Shanxi?”

“That’s right. I’ve never heard that alias before.”

“If you’re from out of town, that would make sense. Young Master Jin only rose to prominence recently.”

“You mean Young Master Jin Wikyung, the Lesser Family Head?”

“What? Not at all. The Lesser Family Head is impressive too, but the one who played the biggest role this time was Young Master Jin.”

“So that Young Master Jin… Wait. Is the Sleeping Dragon of Shanxi somehow related to Third Young Master Jin Taekyung?”

“They’re the same person.”

The man, who had been silent until then, snapped his fingers. A second silver tael landed perfectly in the storyteller’s bowl.

“I believe I asked you to keep it simple and stick to the facts.”

“I’ll stake my balls on it.”

At the storyteller’s resolute answer, the man sighed.

“Let’s say that’s true. What happened to Mount Heng Sword Sect?”

“They’re on the verge of closing their gates. Second Young Master Lee Seogeun had already died, and their Sect Leader, Blood Wolf Sword Lee Cheonbaek, fell in battle. Two days later, even their successor—the First Young Master—was killed fighting a band of mounted bandits.”

“Mounted bandits?”

“These gutsy bastards heard the Blood Wolf Sword was dead and stormed Mount Heng Sword Sect. Word is they’d been circling nearby from the start, waiting for their chance.”

“What a dog’s mess.”

“A horse’s mess, more like. They’re mounted bandits, aren’t they?”

The inn went dead quiet. Everyone expected the big-spending martial artist to drive a third silver tael into the storyteller’s forehead.

Instead, the man rose from his seat without a word.

“I heard you.”

Even after the man left, the storyteller’s tale went on. They drank without pause, and the snacks never ran out.

They all talked about the struggle for supremacy among martial artists. Victory and defeat. The young hero who had risen like a morning star.

“It won’t be long before the Jin Family of Taiyuan steps beyond Shanxi and stands tall in the Central Plains. The Lesser Family Head, who excels in both civil and martial arts, the Sleeping Dragon of Shanxi, who rose to prominence this time, and… and who else was it?”

“The Heaven Shaking Sword?”

“Ah, right. Second Young Master Jin Mukyung!”

“That young man is incredible too. They say he’s a martial arts genius who appears once in a hundred years, if that.”

“But where is he now? What’s he doing?”

“Dunno. At this hour, he’s probably asleep.”

Even as the drinking went on inside the inn, the man rode in silence. His mouth was shut tight, but his ears were wide open.

“Did you hear?”

“The Sleeping Dragon again? My ears are bleeding. Give it a rest.”

“Yeah, but this is grade-one intel. I heard it from a gate guard of the Jin Family of Taiyuan.”

“What’s the fuss?”

“You know the Heavenly Axe?”

“The Heavenly Axe of the Eighteen Strongholds of Green Forest? That mountain bandit who’s a Peak master anyway?”

“That’s the one. Word is the Sleeping Dragon of Shanxi took him out too!”

“Isn’t that just a rumor? Why would someone like the Heavenly Axe come all the way to Shanxi to play bandit?”

“How would I know? The wilder part is that Yama Whip was there too.”

“Yama Whip too?!”

“They say he’s disguised as a coachman at Honghwaru. If you ever have reason to go there, watch yourself.”

Of all the talk that never stopped, two words came up most often.

The Sleeping Dragon of Shanxi.

And Jin Taekyung.

The closer the man came to his destination, the more the rumors swelled like a snowball, growing larger and larger.

*The most handsome man of all time. A heaven-bestowed martial physique. A chivalrous hero who cannot stand injustice.*

The man in the bamboo hat spurred his horse. Even the Shan in Sleeping Dragon of Shanxi was enough to make his stomach churn and his head ache, as if he had taken an internal injury.

He finally reached his destination the next morning.

*Been a while.*

The place he had returned to after several years was unchanged.

If there was any difference worth mentioning—

“Stop right there! I am the hegemon of Shanxi, Captain of the Gatekeepers of the Great Jin Family of Taiyuan, and the right-hand man of the Sleeping Dragon of Shanxi—Hyuk Mujin! State your identity and purpose, and—”

—it was that a guy who looked like hell was serving as Captain of the Gatekeepers.

The man in the bamboo hat, Jin Mukyung, sighed.

“Shut up and open the gate.”

* * *

Whoooosh.

The water flowed. Calm, and unimpeded.

The internal energy that had left my dantian raced through hundreds of acupoints, then finally returned to where it belonged.

Ding!

> **System**
>
> - You have successfully completed **Qi Circulation**.
>
> - The realm of the **Jin Family’s Cultivation Technique** has risen to the Eighth Stage.

I opened my eyes as I listened to the System notification.

*The Eighth Stage.*

It was clearly good news, but I couldn’t help feeling a little disappointed.

The notification I had been waiting for was a different one.

*Could’ve at least bumped my internal energy.*

Today marked two months since I had been able to use the System. Circulating my qi had become a habit, but my internal energy was still going nowhere.

*At this rate, it’ll take another ten years.*

The greatest strength of the Jin Family’s Cultivation Technique I had learned was its stability. Unlike ordinary internal cultivation techniques, I could even run it while moving.

The problem was…

*The accumulation speed is fucking terrible.*

For a martial artist, a lack of internal energy was a fatal weakness.

I could handle First Rate and Second Rate opponents easily enough, but if I ran into a Peak master as an enemy, even two lives wouldn’t be enough.

I had felt that clearly after tasting the Head Elder’s martial might firsthand.

*That old man was something else.*

Even after five days, I still couldn’t forget it.

No. Not five days.

Even fifty years from now, I would never forget that sight.

The Sword Energy and Sword Force that had swept the battlefield. And that absurd number—Level 95.

*How long could I have lasted against him one-on-one?*

Even if I had wrung out every last ounce of strength, I doubted I could have held on for a minute.

But unexpected variables had overturned the result, and I had been able to drive my spear through his chest.

And the System had not forgotten my reward.

“Open Status Window.”

Ding!

> **System**
>
> **Status Window**
>
> **Lv. 50 Jin Taekyung**
>
> **Class:** First Rate Martial Artist  
> **Fame:** 1,180 (+150)  
> **Titles:** 4 (Title effects active)
>
> - **Sleeping Dragon of Shanxi** — All Stats +10, Fame +100
> - **Scion of a Prestigious Family** — All Stats +5, Fame +50
> - **Novice Trainee** — Training Speed +10%
> - **Gambler** — Combat-related Stats +10% in one-on-one combat
>
> **Strength:** 135 (+15)  
> **Stamina:** 142 (+15)  
> **Agility:** 130 (+15)  
> **Intelligence:** 25 (+15)  
> **Charm:** 25 (+15)  
> **Internal Energy:** 15 years
>
> **Remaining Points:** 100
>
> - Distribute your Remaining Points.

“Ohhh, yeah.”

I had checked that Status Window dozens of times over the past few days, and I still wasn’t sick of it. It felt like carbonation popping in my veins.

*Fighting the Head Elder was worth it.*

It had been a gamble with my life on the line, so the reward was stacked.

I had jumped thirteen levels in one stroke, my Fame had entered the triple digits, and my Titles had changed.

“Check Titles.”

Ding!

> **System**
>
> **Status Window**
>
> **Sleeping Dragon of Shanxi**
>
> **Grade:** Peak  
> **Effect:** All Stats +10, Fame +100  
> **Description:** Your fame has now spread throughout Shanxi. But the world is vast and masters are many. Never become complacent!

I wasn’t a nationwide name yet, but in Shanxi—my local district—I apparently had some real clout…

*So that’s why it’s called the Sleeping Dragon of Shanxi?*

Goyang’s Honey Fist. Incheon’s Sea of Blood. That kind of thing.

Either way, it was good for me. I had a solid new Title, and Family Shame, the tag that had clung to me until recently, was gone. It felt as good as having an aching tooth pulled.

*I’ve gotten stronger again.*

I suddenly remembered what I had told Team Leader Choi before coming back to Murim.

“Next time you see me, you’ll have to revise the contract.”

He had probably taken it as a bluff. I had made it a fact.

*I’ll get as strong as I can, then go back.*

I would take every scrap of power I could get before I returned.

Internal energy, martial arts, stats. Whatever it was, all of it.

On my next Logout, I’d be a B-rank Hunter—no, an A-rank Hunter—and return home in glory…

“Huh?”

Wait.

I was forgetting something incredibly important.

*What is it?*

I stopped everything I was doing and tried to pin down that sense of déjà vu.

That was when—

“Is it here?”

“Yessir. No mistake.”

Two voices murmured outside the door. The moment I realized one of them belonged to Hyuk Mujin—

Boom!

The door tore off its hinges with a thunderous crash.

* * *

I take basic common sense seriously.

Tissues go in the trash. Cigarettes belong in the smoking area. Porn comes from Japan.

And when you enter someone else’s room, you knock.

I especially believe that anyone who barges into a room a man uses alone, without knocking, deserves life in prison.

By that standard, the bastard in front of me got the death penalty.

He had smashed the door, so that was life. He had spoken down to me on first meeting, so that was an extra charge.

I answered him politely.

“Yeah. I’m here.”

The bastard’s eyes went round. His face was black with grime, as if he had spent twenty years in the Aoji Coal Mine.[^1]

Young, in shabby clothes. The story practically wrote itself.

*Wandering Martial Artist #1.*

An extra who had come running after hearing about the Sleeping Dragon of Shanxi.

I turned to Hyuk Mujin, who was wearing a similar expression.

“What’s with this guy?”

Hyuk Mujin froze solid. He looked like he had seen a ghost.

“You don’t know him?”

“How would I know, idiot? You have to introduce people.”

Grumbling, I raised my Qi Sense. A blue circle stretched toward the two of them.

> **System**
>
> **Lv. ??? Jin Mukyung**

*Jin Mukyung. Guess he’s pretty high-level.*

“Huh? Jin Mukyung?”

I looked at the Level window once.

Then at his face.

I did that three or four times, then walked up to him with my heart pounding.

“Uh. Just a second.”

“…”

Rub, rub.

My clean sleeve turned black. Then a handsome face emerged. I thought I had seen it somewhere before, and then I realized it was the face I met every morning when I washed up.

*Carbon copies.*

I gave an awkward laugh. Wandering Martial Artist #1 was glaring at me, his eyes like ice.

“Long time no see, hyung.”

[^1]: Aoji Coal Mine was a notorious coal mine in North Korea, associated with harsh working conditions.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 63`.
