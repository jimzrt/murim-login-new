# Master Edit Task — Chapter 10

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
| 위팽     | **Wipeng**         |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 삼류     | **Third Rate**    |
| 이류     | **Second Rate**   |
| 일류     | **First Rate**    |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 창법     | **spear technique**                              |                                                       |
| 구결     | **formula**                                      | Mnemonic/oral formula for a martial art               |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 영약     | **elixir**                                       |                                                       |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 낭인     | **wandering martial artist**                     |                                                       |
| 기루     | **pleasure house**                               |                                                       |
| 기녀     | **courtesan**                                    |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 큰형     | **eldest brother**                           |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 진가보법   | **Jin Family's Manoeuvre Technique**   |
| 진가창법   | **Jin Family's Spear Technique**       |
| 시스템              | **System**                     |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 아이템              | **Item**                       |
| 습득               | **Acquired**                   |
| 체력               | **Stamina**                    |
| 지능               | **Intelligence**               |
| 헌터      | **Hunter**            |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 공자      | **Young Master**                                                |
| 대사      | **Master** for a senior Buddhist monk                           |

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

#### Chapter 8 tail (verified mastered)

…
I was about to shout, “I accept!”—but stopped. > **System** > > - Would you like to train in this martial art? (3 / 10) The number in parentheses bothered me immensely. I had learned exactly three martial arts so far: the Jin Family’s Cultivation Technique, the Jin Family’s Spear Technique, and the Jin Family’s Manoeuvre Technique. *Could it be…* *Is there a limit to how many martial arts I can learn?* If that suspicion was true, now was not the time to learn a third-rate martial art like Three-Turn Footwork. I needed to find a higher-grade martial art—one that could keep me alive until Logout and help me raise my Level and Fame quickly. The good news was that this room contained several hundred martial arts manuals, give or take. “Good. Good.” That meant I could learn seven more martial arts. If I filled those slots with nothing but the best techniques, Logout would only be a matter of time. With a satisfied smile, I pulled out the next book. Ding. > **System** > > Item Window > > **The Night King: Well-Endowed Man** > > **Type:** Erotic Novel > > **Grade:** None > > **Restriction:** None > > **Description:** Even better when read with illustrations. “…” * * * Today’s battle against work had been fierce. Jin Wikyung had not left the office once between morning and the present hour, which was approaching midnight. This grueling pace had already continued for two months. “You’ve worked hard.” Wipeng’s words signaled the end of the day’s work. Jin Wikyung rose, stretching his stiff body, and left the office. After all, the owner of that room was not Jin Wikyung, but his father, who had vanished without warning one day. His residence was a pavilion in the inner compound at the center of the Jin Family estate, and it took about a quarter hour to walk there. “It’s cold tonight.” Wipeng, who had followed him like a shadow, draped a thick fur cloak over his shoulders. Jin Wikyung smiled tiredly. “Thank you. Without you, I might have collapsed long ago.” “What else can I do? Someone has to play the lady of the house.” “Forget it. The old men are already hounding me enough as it is.” Jin Wikyung rubbed his dry eyes. Though he was in his mid-thirties, he remained unmarried. He had kept putting marriage off on the grounds that he was still young, and those delays had added up to more than a decade. *I suppose I’ll have to do it eventually. For the family’s sake.* Had he ever been in love? Yes. But Jin Wikyung was no immature child. One day, he would become the Family Head and bear responsibility for everyone in the household. If a political marriage could strengthen the family, he considered it a small price to pay. “The stars are bright. We almost wouldn’t need torches.” Sensing the mood, Wipeng changed the subject. Jin Wikyung shook his head. His residence had come into view. “Hmm?” “What is it?” Following Jin Wikyung’s gaze, Wipeng tilted his head. A faint light was leaking from a nearby pavilion. “Isn’t that the Third Young Master’s residence?” “It is. It’s late, but the lights are still on.” As he spoke, Jin Wikyung strode forward. Wipeng had no choice but to follow. “My lord, why don’t we come back another time? The memory loss is just an excuse. He’s obviously drinking.” “Shh.” The two men entered the pavilion. The light came from the old room on the far left. Constant creaking sounded from within, as if someone were moving around without pause. “I underestimated the Third Young Master. It sounds like he even brought a woman in. Listen to that. I’ll bet this month’s salary on it.” Wipeng’s lips moved. He was using Sound Transmission, sending his voice through internal energy. “Wipeng.” “Yes?” “Shut your mouth.” Jin Wikyung sent the short, heavy reply through Sound Transmission, then moved right up to the door. Through the open crack, he could see what was happening inside. Then Wipeng cut in with a wounded expression. “I never took you for this sort of person, my lord, but your tastes are rather unusual…” He gasped. The next moment, Wipeng’s mouth fell open. *What did I just see?* *Am I seeing things because I’ve been feeling weak lately?* He rubbed his eyes with his sleeve, but all five senses continued to take in the scene before him exactly as it was. “Now, take two steps diagonally…” A sturdy young man muttered continuously as he moved without pause. Countless footprints covered the dusty floor, and more were appearing even now. Swish. Stumble. “Fuck, they made this martial art like shit—aaagh!” It was the Third Young Master. That foul personality and that foul mouth. There was no doubt that he was Jin Taekyung. He had not trained in martial arts since he was twelve, yet here he was, practicing past midnight until he was drenched in dust and sweat. “Wipeng.” Wipeng, who had been staring blankly, snapped back to his senses. “Yes, yes?” Jin Wikyung gazed into the room with dazed eyes. Jin Taekyung had fallen over and was hurling vicious curses at the ceiling, but he soon got back up and resumed practicing his footwork. “As promised, you won’t be getting paid this month.” [^1]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement.

#### Chapter 9 tail (verified mastered)

…
memory hasn’t fully returned. And besides… he changed into an entirely different person overnight. You’ve noticed it too.” “That’s true, but…” Wipeng let his voice trail off. The Third Young Master had certainly changed. Whether his memory loss was real or a lie, his current behavior was undeniably encouraging. After a moment’s thought, Jin Wikyung spoke. “Wipeng.” “Yes.” “Prepare an order in my name.” “What sort of…?” “Use a few suitable charges and have him forcibly confined in the training hall as punishment.” “Ah.” Wipeng slapped his forehead. It was mostly for show, but under the circumstances, it was an excellent emergency measure. It would relieve the pressure Jin Wikyung was about to receive at the upcoming family council meeting while lowering the severity of the punishment imposed on Jin Taekyung. And on top of that… “It fulfills the Third Young Master’s request too. He was looking for somewhere to train.” Wasn’t this three birds with one stone? Wipeng was genuinely impressed. “As expected of you, my lord.” “That’s how the people in my family are. Oh, did I ever tell you? Taekyung was such a clever child when he was young. One day…” “…I’ll go write the order.” * * * “Therefore, for violating fourteen regulations and disrupting discipline within the family, the Third Young Master, Jin Taekyung, is hereby ordered to undergo indefinite confinement in the training hall.” His name was… Wipeng, wasn’t it? I listened silently to the sour-looking bastard, then raised my hand. “I have a question.” “Go ahead.” “What does ‘indefinite’ mean?” Wipeng answered reluctantly. “It means there is no set deadline.” “Oh.” I’d thought the game’s language system had malfunctioned. Fortunately, it meant exactly what I thought it meant. Ha ha. “Ha ha ha.” “Ho ho ho.” Laughter was contagious. The warriors who had accompanied Wipeng began laughing along with me. In that warm atmosphere, Wipeng read the final line. “The convict, Jin Taekyung, shall submit to the bonds.” “No.” “…” “…” “I said no. Fuck.” The two men approaching with rope restraints looked at Wipeng as if to say, *This isn’t how it was supposed to go.* I ignored them and said what I had to say. “I asked you to find me a room to practice in, not throw me in prison.” “Are you people all completely fucking insane?” “Now, Third Young Master. Calm down and listen to me.” “Listen to what, for fuck’s sake? You’re going to tell me the training hall has everything I need for practice and the living conditions aren’t bad. That kind of bullshit.” Judging by Wipeng’s expression, I’d hit the nail on the head. I drove the point home. “You people are the type to tell someone to enjoy military service because soldiers got a pay raise. Forget it. I’m not going in. I’ll practice by myself in my room or out in the yard.” Honestly, on the surface, the training hall didn’t sound so bad. But the word *indefinite* stuck in my mind like a thorn. I urgently needed to learn martial arts and Level up. I couldn’t spend every day in the training hall craning my neck and waiting for someone to let me out. I flopped onto the floor. “Go ahead and gut me!” “Third Young Master, that’s enough. Please get up.” Wipeng scowled at me. “The Lesser Family Head made this decision entirely for your sake.” “Jin Wikyung—I mean, my brother?” That brother-obsessed idiot had given this order? At that moment, Wipeng’s lips moved. At the same time, a voice reached my ears. It felt strange, unlike an actual spoken voice. > “This is Sound Transmission. Don’t be alarmed—just listen.” Sound Transmission. I remembered seeing it in martial arts novels. A kind of telepathy that only masters could use. > “You may not know this because you’ve lost your memory, but the Third Young Master is a person of concern. A harsher punishment may be handed down soon, so the Lesser Family Head is taking action beforehand.” I had worked hard for twenty-seven years. What did I do to deserve an aggravated sentence? As I lamented, Wipeng’s Sound Transmission continued in my ear. > “It may be called indefinite confinement, but do you really think the Lesser Family Head intends to bury you in the training hall for the rest of your life?” I shook my head. *There’s no way he’d do that.* Not unless he wanted the two of us locked up together in the training hall. > “I’ll get you out within seven days and nights at the latest. How does that sound?” There was fierce determination in Wipeng’s eyes. If I refused this too, he looked ready to beat me and drag me there if he had to. *Fuck, are all the NPCs here thugs or what?* *Hey, you bastard. Are you really that good at fighting?* I raised my Qi Sense and checked Wipeng’s Level. > **System** > > **Lv. ???** “…” *He really is a thug.* A Level thug. He was probably every bit the human butcher Jin Wikyung was. Wipeng opened his eyes wide and asked, > “What will you do?” Even as I trembled with fear, I held up three fingers. > “…You want me to get you out in three days?” *What kind of bastard is this?* Wipeng glared at me with that exact look, then finally sighed. “Escort him.” #TrainingHall #ClosedDoorTraining #Negotiation #Successful.

## Korean source

```text
＃10화



십여 분을 걸어 도착한 곳은 태원진가의 후방을 가로막은 절벽이었다. 커다랗게 아가리를 벌린 동공(洞空). 그 앞에 한 사람이 있었다.

“음. 왔느냐?”

불곰 같은 덩치에 근엄한 말투. 진위경이다. 나는 엉거주춤하게 고개를 숙여 보였다.

“안녕하십니까, 형……님.”

진위경은 껄끄러운 존재다. 졸지에 NPC 가족이 생긴 것도 모자라 나한테 엄청 관심이 많기 때문이다.

저 봐라, 남들 보는 눈이 있다고 티 내지 않으려고 무지 애쓰는 거. 하지만 자세히 보면 눈동자가 촉촉하게 젖어 있다.

‘감수성 실화냐.’

외관상으로는 삼합회 두목도 한 수 접고 들어갈 것 같은데, 이 게임 캐릭터들은 어째 다 요지경인지 모르겠다.

“네 행실을 더 이상 묵과할 수 없어 소가주이자 가주 대행의 직분으로 폐관을 명했다. 하고 싶은 말이 있느냐?”

‘당연히 있지.’

그러나 짜고 치는 고스톱이다. 수련동으로 오는 길에 위팽에게 돌아가는 사정을 들었다. 태원진가 내에서 권력층 간의 힘 싸움이 있고, 진위경이 내 방패 역할을 해 주고 있다는 것.

이번 강제 폐관 행은 그러니까, 쇼인 거다.



‘어차피 공자도 수련 공간이 필요하다고 하지 않았습니까? 사흘만 참으십시오.’



나는 위팽의 마지막 말을 떠올리며 반성하는 척 고개를 숙였다.

“죗값을 달게 받겠습니다.”

이 연극의 장점은 대사가 짧다는 것이다. 진위경은 애잔한 눈빛으로 마지막 대사를 읊었다.

“죄인을 수련동에 가둬라. 출관 날짜는 차후 통보하겠다.”

말이 끝나기가 무섭게 수련동 입구를 지키던 무사 두 명이 다가와 내 양팔을 붙들었다. 연극이 끝났으니 퇴장할 차례.

나는 수련동 입구에 섰다.

- 필요한 것은 가져다 놨다. 막내야, 무리하지 말거라.

진위경의 전음과 함께 첫발을 내디뎠다.



* * *



수련동은 한마디로 동굴이었다. 그것도 절벽을 파서 만든 인공 동굴. 높고, 넓었다. 그리고 축축했다.

철벅철벅.

수련동 소속 무사를 따라 얼마나 걸었을까. 내가 신은 것이 가죽신인지 물걸레인지 헷갈릴 때쯤 거대한 철문이 나타났다.

‘와…….’

보는 순간 입이 벌어졌다. 통로를 빈틈없이 채운 그것은 문이라기보다 모든 출입을 금지하는 벽처럼 보였다.

안내해 준 무사가 횃불을 들고 외쳤다.

“개문!”

그그긍-

거대한 철문이 천천히 아가리를 벌렸다. 무슨 열려라 참깨 같은 마법 주문은 아니고, 미리 대기하고 있던 NPC 한 명이 삐죽 튀어나와 있는 개폐 장치를 잡아당긴 것뿐이었지만 압도적인 광경이었다.

그리고 내부가 눈에 들어온 순간.

“우와.”

이번만큼은 나도 새어 나오는 탄성을 숨기지 못했다.

처음 수련동에 들어올 때만 해도 축축한 지하 동굴을 생각했는데…….

“이게 다 뭐야.”

넓은 침상에 보기만 해도 기분이 좋아지는 털 이불. 축축하고 울퉁불퉁한 돌바닥 대신 깔끔한 회색 지면이 펼쳐져 있다.

‘시멘트……는 당연히 아니겠고 석회석인가?’

냉기가 감도는 것만 빼면, 아니, 그걸 감안해도 상상 이상으로 괜찮은 환경이다.

‘이게 처벌이라고?’

얼떨떨하게 주위를 바라보는데 등 뒤에서 헛기침 소리가 들렸다. 돌아보니 안내역을 한 수련동 무사다.

“필요한 것들은 모두 갖춰 놓았습니다. 그럼 저는 이만.”

그그긍. 천천히 닫히는 철문을 바라보다가 문득 수련동 입구에서 들었던 전음이 생각났다.



‘필요한 것은 가져다 놨다. 막내야, 무리하지 말거라.’



아아, 그것은 동생을 생각하는 NPC의 마음.

이 못난 유저는 목 놓아 웁니다.



* * *



현실에서도 숱하게 일어나는 일이다. 비리를 저지른 고위층들이 휠체어를 타고 검찰을 드나들고, 수사를 피하기 위해 병원 특실에 입원하는 것.

조금 다르긴 해도 내가 지금 그 모양새다. 나는 감동한 얼굴로 수련동 특실을 바라봤다.

“이런 게 금수저의 삶이구나.”

그래픽, 인공지능만 현실적인 게 아니다. 아무리 날고 기어도 금수저가 최고라는 사회적 메시지를 담고 있다.

세상에, 이 캐릭터 아니면 어쩔 뻔했어. 아빠가 가주, 큰형이 소가주에 둘째 형은 무공의 천재다. 마음 놓고 기루 죽돌이 짓 할 만하다.

‘진태경 이 새끼…….’

알고 보니 어린 나이에 세상 돌아가는 이치를 깨달은 대현자가 아닌가.

나는 현실적인 갓-수저 시스템에 전율하며 백여 평에 달하는 수련동을 돌아다녔다. 그리고 수련동 무사가 말한 ‘필수품들’을 찾을 수 있었다.

‘우선 식량.’

식량은 항아리 두 개에 나뉘어 보관되어 있었다. 속을 들여다보니 약재 냄새가 진하게 풍기는 주먹밥이다.



아이템창



[뛰어난 벽곡단]

종류 : 단환

등급 : 일류

제한 : 없음

설명 : 온갖 좋은 약재를 무식하게 때려 박아 만든 벽곡단. 섭취 시 원기를 회복하며, 장복할 경우 추가적인 효과를 얻는다.





“아, 이게 바로 그 벽곡단?”

무협 소설에서 많이 봤다. 가볍고 부피가 작아서 휴대하기 편한 데다 영양 보충까지 된단다. 나머지 항아리에도 벽곡단이 그득했다.

‘일단 인벤토리에 넣어 둬야지.’

양손으로 항아리를 잡고 중얼거렸다.

“아이템 습득.”

다른 사람이 이 모습을 봤다면 놀라 자빠졌을 거다. 멀쩡하게 놓여 있던 항아리 두 개가 증발한 듯이 사라졌으니까.

나는 인벤토리에 수납된 항아리를 흐뭇하게 바라봤다.

‘이걸로 식량 문제는 해결됐고.’

그다음으로 발견한 두 번째 필수품은 물이다. 수련동 내부는 엄연히 동굴이라, 한쪽 구석에 차가운 지하 샘물이 있어 식수 문제를 해결해 주었다.

그리고 마지막 세 번째.

“흠.”

여러 개의 병기가 나란히 걸려 있는 무기 거치대. 당연하게도 가장 먼저 손에 쥔 것은 단단해 보이는 목창(木槍)이다.

‘아이템 감정.’

띠링.



아이템창



[수련용 목창]

종류 : 병장기

등급 : 삼류

제한 : 없음

설명 : 초보자용으로 제작되었다.





“오.”

초보자를 대상으로 만들어진 수련용 목창. 지금의 내게 딱 맞는 물건이다. 여기에 하나만 더 있으면 완벽하지.

“인벤토리 오픈.”

나는 씩 웃으며 인벤토리에서 [진가창법]이 적힌 비급을 꺼냈다.

띠링.



- [진가창법]을 습득하시겠습니까? (3 / 10)



“당연히 예스지.”

나는 시스템이 참 좋다. 가끔은 사랑스럽다.



* * *



어제 진가보법을 익히며 처음 알게 됐다. 시스템 알림은 띠링, 하나만이 아니라는 사실을.

그리고 저 소리가 얼마나 듣기 싫은 소리인지를.

삑!



- 동작이 실패했습니다.

- 남은 성공 횟수 (2 / 100)



실패 메시지. 일명 삑사리가 나면 어김없이 뜨는 시스템창이다. 도대체 몇 번째 보는 메시지인지 모르겠다.

나는 손에 쥔 [수련용 목창]을 바라봤다.

‘잘못 생각했네.’

목창이라 그런가, 가볍다. 찌르면 찌르는 대로, 휘두르면 휘두르는 대로 빠르게 움직인다. 그래서 문제다.

‘너무 가벼워서 조절하기가 힘들어.’

미세한 조정이 어렵다 보니 자꾸만 삐끗한다. 더럽게 깐깐한 시스템이 그런 사소한 실수를 눈감아 줄 리가 없다.

삑.



- 동작이 실패했습니다.

- 남은 성공 횟수 (5 / 100)



“아오. 시발.”

결국 [수련용 목창]을 내던지고 [예리한 창]을 인벤토리에서 꺼냈다. 길이나 창대의 굵기가 내가 현실에서 쓰던 창과 얼추 맞아떨어진다.

그런데 왜 처음부터 꺼내지 않았냐고?

“더럽게 무겁네. 진짜.”

통짜 강철로 만들었다 보니 무게가 장난이 아니다. 체감상 느껴지는 무게만 얼추 50kg에 육박하는 괴물인 것이다.

이런 걸 몇 시간이고 휘둘렀다가는 내 체력이 못 버틴다.

현재 내 경지는 이류, 시스템의 힘을 빌렸다지만 쌀 반 가마니가 넘는 무게를 팔랑개비처럼 휘두르는 건 무리다.

‘어디서 호랑이 기운이 솟아나는 것도 아니고.’

그런 생각을 했을 때였다.

“……어?”

내가 방금 뭐라고 했지? 호랑이 힘?

“있네?”

이곳은 게임이다. 시스템이 있고 능력치가 있다. 그리고 공력이 있다. 심법을 통해 이끌어 낼 수 있는 10년의 공력이!

잠깐이나마 잊고 있었다는 게 쪽팔릴 정도다.

“내가 그런 걸 써 봤어야지…….”

고기도 먹어 본 놈이 안다고 했다. F급 헌터가 괜히 F급이겠나. 마나라고는 쥐뿔도 없이 맨몸으로 때우니까 헌터들 사이에서도 반푼이 취급받는 거다.

‘그래도 문제 하나는 해결했네.’

허허, 나는 어이없게 웃으며 창을 집어 들었다. 그리고 천천히, 신중하게 공력을 끌어 올렸다.

머릿속에서는 시스템이 각인시킨 진가심법의 구결이 빠르게 되감기며 공력을 정해진 길로 이끈다.

찌릿.

반응은 즉각적이었다.

단전에 웅크리고 있던 10년 공력이 전신으로 퍼져 나간다. 게임이라서, 무림인이라서 느낄 수 있는 그 기운이 사지백해로 뻗어 나가는 것이 느껴졌다.

‘이건…….’

온몸에 힘이 넘쳐흐른다. 월등히 상향된 신체 능력과 감각은 F급 헌터로 살아온 내게 다시 한번 황홀함을 선사해 주었다.

‘이렇게 달라질 수 있다니.’

나는 창을 잡고 [진가창법]을 펼쳤다. 더 이상 무겁게 느껴지지 않는 50kg의 철창은 내가 원하는 길을 따라 허공을 찌르고 베었다.

이윽고.

띠링.



- 남은 성공 횟수 (6 / 100)



기다리던 알림이 울리기 시작했다.



* * *



진위경이 근심 섞인 얼굴로 입을 열었다.

“잘하고 있겠지?”

“잘하고 있겠지요. 염치가 있으면.”

“아직 몸도 성치 않은데…… 괜찮겠지?”

“모르는 사람이 보면 삼공자가 오늘내일하는 줄 알겠습니다. 저 정도면 침 발라도 나아요.”

“아니야. 막내가 어릴 때부터 얼마나 허약했는지 자네가 몰라서 하는 말이야.”

위팽이 기가 찬 얼굴로 대답했다.

“삼공자 입으로 들어간 영약과 보양제만 해도 방 하나를 채울 겁니다. 그리고 벌써 잊으셨습니까? 작년에 있었던 백년설삼 절도 사건!”

“어허. 그건…….”

“그때 약왕당주가 대노해서 삼공자 배를 갈라 보겠다고 날뛰는데, 솔직히 말리면서도 그런 생각이 들더군요. 갈라도 정당방위라고.”

진위경은 슬쩍 시선을 회피했다. 결국 진위경의 개인 사재를 털어 보상하는 것으로 마무리됐지만 당시 약왕당주의 분노는 대단했다.

“그 정도 영약을 꿀꺽했으니 모르긴 몰라도 죽을 때까지 잔병치레는 안 할 겁니다.”

“그래도 부족해. 자네는 딱 보면 모르나? 나는 막내 볼 때마다 안쓰러워. 애가 뼈다귀에 살점 몇 개 붙어 있는 꼴이잖나. 아침마다 비리비리해서 힘도 없고.”

“힘이 없다고요?”

위팽은 순간 과거에 들었던 소문을 떠올렸다. 태원 홍등가 기녀들 사이에서 진태경이 야왕(焲王)이라는 별명으로 불린다는 소문이었다.

‘도대체 어느 정도길래.’

약발 하나는 제대로 받은 모양이군. 위팽은 자신도 모르게 팔뚝을 들어 크기를 상상해 보았다.

“자네 뭐 하나?”

“아, 아닙니다.”

진위경은 산더미처럼 쌓인 서류 더미를 보며 한숨을 내쉬었다.

“막내도 그렇고, 가문 안팎으로 신경 쓸 일 천지야. 특히…… ‘그들’이 접선해 온 것도 꺼림칙하고.”

“항산검문 말씀이시군요.”

항산검문. 그 이름이 갖는 무게는 결코 가볍지 않았다.

수십 년 전, 어느 불패(不敗)의 낭인이 현판을 내건 이래 무서운 속도로 성장해 왔고, 작금에 이르러서는 태원진가의 입지를 위협할 정도가 되었다.

“무슨 의도일까?”

“수하들을 풀어 알아보고 있습니다.”

진위경은 항산검문에서 온 서신을 만지작거렸다.

왜? 어떤 목적으로 그들이 오는가? 꼬리에 꼬리를 무는 의문 끝에 내린 결론은 하나였다.

“산서성 각 지부에 알리게. 항산검문의 목적이 무엇이든 간에 만반의 준비를 갖추라고.”

이곳은 무림이다.

준비된 자만이 살아남아 내일을 맞이할 수 있으리라.
```

## Current accepted English baseline

```markdown
# Chapter 10

After walking for more than ten minutes, we arrived at a cliff that blocked off the rear of the Jin Family of Taiyuan. A massive cavern gaped open in its face. One person stood in front of it.

“Hmm. You came?”

He had the build of a brown bear and spoke in a solemn tone.

Jin Wikyung.

I gave an awkward bow.

“Hello, big… brother.”

Jin Wikyung was an awkward presence. As if suddenly gaining an NPC family wasn’t enough, he also paid an absurd amount of attention to me.

Just look at him. He was trying so hard not to show it in front of everyone else. But if you looked closely, his eyes were moist.

*Is this guy seriously that sentimental?*

With his appearance, he looked like the kind of man who could make even a triad boss back down. Yet somehow, every character in this game was completely bizarre.

“I can no longer overlook your conduct. As the Lesser Family Head and acting Family Head, I have ordered you to undergo closed-door training. Do you have anything to say?”

*Of course I do.*

But this was all a staged performance. On the way to the training hall, Wipeng had explained what was really going on. There was a power struggle among the upper ranks of the Jin Family of Taiyuan, and Jin Wikyung was acting as my shield.

This forced confinement was, in other words, a show.

*The Young Master needed a place to train anyway, didn’t he? Just endure it for three days.*

Remembering Wipeng’s final words, I bowed my head as if repenting.

“I will gladly accept my punishment.”

The advantage of this play was that the lines were short.

Jin Wikyung delivered his final line with a sorrowful look in his eyes.

“Confine the criminal to the training hall. The release date will be announced later.”

The moment he finished speaking, two warriors guarding the entrance to the training hall approached and grabbed me by both arms.

The play was over. Time for me to exit the stage.

I stood at the entrance to the training hall.

*I’ve had everything you need brought there. Little brother, don’t overdo it.*

Along with Jin Wikyung’s Sound Transmission, I took my first step inside.

* * *

The training hall was, in a word, a cave. An artificial cave dug into a cliff, at that. It was tall, spacious, and damp.

Splash. Splash.

How long had I been walking behind the warrior assigned to the training hall? By the time I could no longer tell whether I was wearing leather shoes or wet mops, a massive iron gate appeared.

*Wow…*

My mouth fell open the moment I saw it. Filling the passageway without leaving a gap, it looked less like a door and more like a wall blocking all entry and exit.

The warrior leading me raised his torch and shouted,

“Open the gate!”

Grrrnnng—

The massive iron gate slowly opened its jaws. It wasn’t some magical command like “Open, Sesame.” One NPC who had been waiting nearby simply grabbed and pulled the protruding gate mechanism.

Even so, it was an overwhelming sight.

And the moment I saw what lay beyond it—

“Whoa.”

This time, I couldn’t hide the exclamation that escaped me.

When I had first entered the training hall, I had imagined a damp underground cave.

“What is all this?”

A broad bed covered in a furry blanket lifted my spirits just by looking at it. Instead of a damp, uneven stone floor, a neat gray surface stretched out before me.

*Cement… Obviously not. Limestone?*

Even with the chill in the air, the environment was far better than I had imagined.

*This is supposed to be a punishment?*

I looked around in a daze, then heard someone clear his throat behind me. It was the warrior who had guided me here.

“We’ve prepared everything you need. I’ll be going now.”

I watched the iron gate slowly close with another grinding sound, then suddenly remembered the Sound Transmission I had heard at the entrance to the training hall.

*I’ve had everything you need brought there. Little brother, don’t overdo it.*

Ah. The heart of an NPC who cared about his little brother.

This pathetic user was bawling his eyes out.

* * *

It was something that happened all the time in the real world, too. High-ranking officials who had committed corruption showing up at the prosecutors’ office in wheelchairs, or checking themselves into private hospital rooms to avoid investigation.

My situation was a little different, but I looked much the same. I gazed at the private suite of the training hall with a deeply moved expression.

“So this is the life of a gold spoon.”[^1]

It wasn’t only the graphics and artificial intelligence that were realistic. The game also carried the social message that, no matter how high you flew or how low you crawled, gold spoons had it best.

What would I have done without this character? His father was the Family Head, his eldest brother was the Lesser Family Head, and his second brother was a martial arts prodigy. He could spend his days loafing around pleasure houses without a care.

*Jin Taekyung, you bastard…*

Now that I thought about it, wasn’t he actually some great sage who had grasped the ways of the world at a young age?

Shuddering at the realistic God-Spoon System, I walked around the training hall, which covered well over three thousand square feet. Before long, I found the “necessities” the warrior had mentioned.

*Food first.*

The food was stored in two jars. When I looked inside, I found rice balls that gave off a strong medicinal scent.

> **System**
>
> **Item Window**
>
> **Excellent Grain-Repelling Pill**
>
> **Type:** Pill
>
> **Grade:** First Rate
>
> **Restriction:** None
>
> **Description:** A grain-repelling pill made by crudely cramming in all kinds of beneficial medicinal ingredients. Restores vitality when consumed and grants additional effects when taken over a long period.

“Oh, so this is the famous grain-repelling pill?”

I had seen them plenty of times in martial arts novels. They were light, compact, easy to carry, and apparently provided nutritional supplementation, too.

The other jar was packed full of grain-repelling pills as well.

*I should put these in my inventory for now.*

I gripped the jars with both hands and muttered,

“Item acquisition.”

If someone else had seen me, they would have fallen over in shock. The two perfectly ordinary jars had vanished as if they had evaporated.

I gazed fondly at the jars stored in my inventory.

*That takes care of food.*

The second necessity I found was water. Since the training hall was, after all, a cave, a cold underground spring in one corner took care of my drinking water.

And then there was the third and final necessity.

“Hmm.”

A weapons rack held several weapons in a neat row. Naturally, the first thing I picked up was a sturdy-looking wooden spear.

*Item appraisal.*

Ding.

> **System**
>
> **Item Window**
>
> **Training Wooden Spear**
>
> **Type:** Weapon
>
> **Grade:** Third Rate
>
> **Restriction:** None
>
> **Description:** Made for beginners.

“Oh.”

A training wooden spear made for beginners. It was exactly what I needed right now.

If I had just one more thing, everything would be perfect.

“Open inventory.”

Grinning, I took a martial arts manual titled *Jin Family’s Spear Technique* out of my inventory.

Ding.

> **System**
>
> - Would you like to learn the Jin Family’s Spear Technique? (3 / 10)

“Obviously.”

The System was great.

Sometimes, it was even adorable.

* * *

I had learned something for the first time yesterday while practicing the Jin Family’s Manoeuvre Technique.

The System’s notification sound wasn’t always ding.

I had also learned just how much I hated the other sound.

Beep!

> **System**
>
> - The movement failed.
>
> - Successful attempts (2 / 100)

It was the failure message. The System window that appeared without fail whenever I botched a movement.

I had no idea how many times I had seen it by now.

I stared at the *Training Wooden Spear* in my hand.

*I was thinking about this all wrong.*

Maybe it was because it was made of wood, but the spear was light. Whether I thrust or swung it, it moved as quickly as I wanted.

That was the problem.

*It’s too light to control.*

Because it was so difficult to make minute adjustments, I kept making mistakes. There was no chance that such a filthy, ridiculously picky System would overlook minor errors.

Beep.

> **System**
>
> - The movement failed.
>
> - Successful attempts (5 / 100)

“Ah, fuck.”

In the end, I tossed the *Training Wooden Spear* aside and pulled a *Sharp Spear* from my inventory. Its length and shaft thickness were roughly similar to the spear I had used in the real world.

But why hadn’t I taken it out from the beginning?

“It’s insanely heavy. Seriously.”

Since it had been made entirely of steel, its weight was no joke. By feel alone, it was a monster weighing nearly fifty kilograms.

My Stamina couldn’t withstand swinging something like this for hours.

My current realm was second-rate. Even with the System’s help, swinging around more than half a sack of rice as if it were a pinwheel was impossible.

*It’s not like I suddenly have tiger power or something.*

That was when it hit me.

“…Huh?”

What had I just said?

Tiger power?

“It’s here?”

This was a game. There was a System and stats. And there was internal energy.

Ten years of internal energy that could be drawn out through a cultivation technique!

It was embarrassing that I had forgotten about it even for a moment.

“I should’ve tried using that…”

They say you only know what something is like once you’ve experienced it. Was it any wonder an F-rank Hunter was F-rank? With barely any mana to speak of, I made do with my bare body. Even among Hunters, I was treated like a half-baked amateur.

*At least that solves one problem.*

I let out a dumbfounded laugh, then picked up the spear. Slowly and carefully, I began drawing out my internal energy.

The formula of the Jin Family’s Cultivation Technique, imprinted in my mind by the System, played rapidly through my thoughts, guiding my internal energy along its prescribed path.

A prickling sensation ran through me.

The response was immediate.

The ten years of internal energy coiled in my dantian spread throughout my body. Because this was a game and I was a martial artist, I could feel it spreading through every part of me.

*This is…*

Strength overflowed through my entire body. My vastly improved physical abilities and senses once again filled me with exhilaration after a lifetime as an F-rank Hunter.

*How can a person change this much?*

I gripped the spear and began practicing the *Jin Family’s Spear Technique*. The fifty-kilogram iron spear no longer felt heavy. It thrust and slashed through the air along the paths I wanted it to follow.

Before long—

Ding.

> **System**
>
> - Successful attempts (6 / 100)

The notification I had been waiting for began to ring.

* * *

Jin Wikyung spoke with a worried expression.

“He’s doing well, right?”

“He should be, if he has any sense of shame.”

“He’s still not fully recovered… He’ll be all right, won’t he?”

“Anyone who didn’t know better would think the Third Young Master was on death’s door. At that point, even spit would cure him.”

“No. You don’t know how weak the youngest was when he was little.”

Wipeng answered with an incredulous look.

“The elixirs and tonics that have gone into the Third Young Master alone would be enough to fill an entire room. And have you already forgotten about the hundred-year snow ginseng theft last year?”

“Ahem. That was…”

“At the time, the Medicine King Hall Master was so furious that he ran around shouting that he was going to cut open the Third Young Master’s stomach. To be honest, even while I was stopping him, I found myself thinking that it would qualify as self-defense.”

Jin Wikyung subtly averted his gaze.

In the end, the matter had been settled by paying compensation out of Jin Wikyung’s personal fortune, but the Medicine King Hall Master’s rage had been extraordinary.

“He swallowed that much elixir. Whatever else may be true, he probably won’t suffer from minor ailments until the day he dies.”

“It still isn’t enough. Can’t you tell just by looking at him? Every time I see the youngest, I feel sorry for him. He looks like a skeleton with a few scraps of flesh stuck to it. He’s so feeble and weak every morning.”

“Weak?”

Wipeng suddenly remembered a rumor he had heard in the past.

Among the courtesans of Taiyuan’s red-light district, Jin Taekyung was supposedly known by the nickname Night King.

*Just how impressive is he?*

The medicine must have worked properly, after all. Without realizing it, Wipeng raised his forearm and began imagining the size.

“What are you doing?”

“Ah, nothing.”

Jin Wikyung sighed as he looked at the mountain of documents piled before him.

“There’s so much to worry about, both inside and outside the family. Especially… I don’t like the fact that ‘they’ have made contact.”

“You mean the Mount Heng Sword Sect.”

Mount Heng Sword Sect. The weight of that name was anything but light.

Since an undefeated wandering martial artist first hung its signboard decades ago, it had grown at a frightening pace. By now, it had become strong enough to threaten the position of the Jin Family of Taiyuan.

“What could their intentions be?”

“I’ve sent my subordinates out to find out.”

Jin Wikyung fidgeted with the letter from the Mount Heng Sword Sect.

Why were they coming? For what purpose?

After one question led to another, he reached a single conclusion.

“Notify every branch in Shanxi. Whatever the Mount Heng Sword Sect’s purpose may be, tell them to make every possible preparation.”

This was Murim.

Only those who prepared themselves would survive and live to see tomorrow.

[^1]: In Korean, “gold spoon” is shorthand for someone born into wealth; “God-Spoon” is a pun that escalates the expression.
```

## Final instruction

Edit the complete baseline against the Korean source. Return only the complete mastered English Markdown chapter beginning exactly with `# Chapter 10`.
