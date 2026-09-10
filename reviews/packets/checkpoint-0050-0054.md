# Checkpoint Review — 50–54

Review only this bounded packet. Check the English reading copies, summaries,
and active state for voice drift, terminology drift, dropped hooks, formatting
differences, internal contradiction, and accidental spoilers. Do not redo the
source-fidelity reviews and do not rewrite files. Return exactly one JSON object
using the chapter-review schema: summary plus a findings array. Use stable IDs
`C01`, `C02`, and so on; source identifies the chapter/location, current quotes
the exact English, correction gives the action, and confidence is 0 through 1.
Use an empty findings array when nothing is actionable.

Return this exact shape with no Markdown fence:

{
  "summary": "brief assessment",
  "findings": [
    {
      "id": "C01",
      "severity": "critical|major|minor",
      "source": "chapter and location",
      "current": "exact current English",
      "defect": "specific defect",
      "correction": "recommended action",
      "rationale": "specific reason",
      "confidence": 0.0
    }
  ]
}

## Binding rules

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

## Checkpoint summary

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

## Durable state

{
  "version": 1,
  "safe_through": 54,
  "continuity_sources": [53, 54],
  "active_continuity": [
    "Taekyung has reconnected to Murim after returning to reality, visiting his family, and being ordered home by Team Leader Choi; he has a C-rank Hunter license and had completed the recent Lizardman Gate work.",
    "Taekyung is the disgraced third son of the Jin Family of Taiyuan and narrates with dry, self-mocking, occasionally profane humor.",
    "The Ark - 2020 capsule's purpose and route back to Murim remain unresolved; its manual says users are bound until death, time runs at an adjustable slow ratio, and Character Synchronization exists.",
    "Murim's death and resurrection limits remain unresolved.",
    "The identity of the Head Elder's Sound Transmission accomplice and the full purpose of their plan remain unresolved.",
    "Im Kkeokjeong is Taekyung's old acquaintance, now E-rank Hunter Im Hyeokjun. He is a veteran Peace Guild member, calls Taekyung his little brother, and serves as a main tank with a tower shield and mace.",
    "Peace Guild is new and has only three people including its Guild Master. Taekyung's original E-rank Gate party consisted of Team Leader Choi, Im, three other veteran E-rank Hunters, and Taekyung as porter.",
    "Team Leader Choi was first measured as a C-rank Hunter and later reawakened. He uses expensive equipment, a sword, and wind-based Haste magic; Taekyung infers that Choi is at least B-rank, but his exact current rank is unknown. Choi killed the Hobgoblin Priest, witnessed Taekyung kill the Great Warrior, and later claimed he killed both monsters when questioned by officials, concealing Taekyung's role.",
    "Taekyung can butcher Hobgoblin corpses at professional speed and has done this as paid raid work for years.",
    "The Boss Zone contained an old Hobgoblin Priest and a Level 45 Hobgoblin Great Warrior summoned from nearly a hundred dead Hobgoblins; both Rare Monsters are now dead.",
    "Character Synchronization completed in reality and all systems were inherited. Taekyung's Status Window now shows Level 33, First Rate Martial Artist, 120 Strength, 125 Stamina, 121 Agility, 20 Intelligence, 20 Charm, fifteen years of Internal Energy, and 30 Remaining Points.",
    "Fame is 0 and the active Titles are Novice Trainee and Gambler. The Traitor Chain Quest is active but incomplete: Taekyung must punish the traitor and lead the battle to victory; failure means death.",
    "Team Leader Choi killed the Hobgoblin Priest and witnessed Taekyung kill the Great Warrior. Officials are investigating how two C-rank Rare Monsters appeared in an E-rank Gate.",
    "Im Kkeokjeong and the other veteran E-rank Hunters survived the Boss Zone fight but were sent to the hospital for about a week.",
    "Taekyung accepts that Murim was real and has now successfully logged back in through the Ark - 2020 capsule, but the capsule's ultimate purpose, safe operation, and long-term route remain unresolved.",
    "Choi's background check found that Taekyung was the sole survivor of the Sangdong Station Mutated Gate, returned to Gate work for a year and a half, and was fired three days ago; Choi suspects he is at least C-rank or recently reawakened. Butler Kim's further investigation finds Taekyung clean, not an illegal Awakener and not someone who deliberately approached Choi.",
    "Seong Jinho took Taekyung's discarded Ark - 2020 capsule and returned it to his room after bargaining over a finder's fee. The manual confirms that the capsule is permanently bound to its registered user until death.",
    "The System reads ordinary objects but cannot read the capsule or its manual. Taekyung is awaiting formal Hunter registration after the Bucheon Branch reassessment.",
    "Taekyung encounters former boss Kim Sangshik at the Hunter Association and confronts him over arranging his dismissal. Kim is a Level 24 D-rank Hunter and one of Sopung Guild's team leaders; Taekyung's synchronized strength overwhelms him when he grabs Taekyung. The reassessment device malfunctions while scanning Taekyung's internal energy, but the Association recognizes Taekyung as C-rank-level. Choi Min-su of Sangdong Guild measures as C-rank with A-rank mana control, and Sopung's Guild Master orders Kim to recruit him.",
    "Guild scouts immediately compete to recruit Taekyung after the reassessment. Kim apologizes for his past conduct and offers Sopung Guild's recruitment package, but Taekyung tells him to say he will consider it only if Sopung gets rid of one man he cannot stand—the obvious target being Kim.",
    "Taekyung wakes from the System's Sleep Mode with a Hangover, detoxifies it through qi circulation, and finds reality's qi weak and polluted. He declines Choi's one-year contract, signs a seven-day provisional contract, chooses the First Rate Lizardman Hunter's Leather Set and Lizardman Slayer's Harpoon, and enters a D-rank Gate with Choi alone.",
    "The Lizardman Hunter's Leather Set activates its Scale Armor effect when fully equipped, and the Lizardman Slayer's Harpoon has a high probability of causing Bleeding. A deferential middle-aged man restricts access to the Gate and addresses Choi as 'young master,' indicating Choi's wealthy background.",
    "Taekyung clears a nearby colony of about twenty Level 40 swamp Lizardmen alone with the Lizardman Hunter’s Leather Set and Lizardman Slayer’s Harpoon, levels up twice without injury, and survives Choi’s pheromone test. When the resulting horde arrives, Taekyung assigns all 100 Remaining Points (30 Strength, 30 Stamina, 40 Agility) and uses One Flash to kill the Level 52 Lizardman Great Chieftain and dozens of monsters.",
    "After the fight, Choi (Choi Minwoo) privately recognizes that Taekyung may be stronger than him. Taekyung completes three C-rank Gates in one day, receives a weekly payment of 300 million won including a 270 million won bonus, and is ordered to take weekends off under the provisional contract.",
    "Sopung Guild’s Guild Master discovers Kim Sangshik filed a false report about Taekyung and expelled him from the Guild, then expels Kim and his son Kim Sangho. The Guild begins gossiping about Taekyung’s reawakening and whereabouts.",
    "Taekyung returns home after months with his C-rank Hunter license and 300 million won. He tells his mother and younger sister Hayeon an edited account of his reawakening and income, then spends freely on clothes and an expensive meal for them at Mirae Department Store.",
    "Hayeon is nineteen and still a high-school senior; she is awake early for the school founding anniversary and resumes her sharp, affectionate sibling banter with Taekyung.",
    "After returning to reality, Taekyung begins having increasingly vivid nightmares of Murim. Sleep Mode restores his physical condition but not his mental stability, and his mistakes and injuries increase during Gate raids. The dreams now show the Mount Heng–Jin Family battle, and he has decided to return.",
    "Taekyung kills a Level 50 Lizardman Chieftain but is injured three times in one day and five times by the fourth day. Team Leader Choi orders him home and asks what is wrong.",
    "Taekyung suspects that Murim is another reality and that the Ark - 2020 capsule may be a Gate to another dimension; he decides to return and successfully reconnects to Murim at the end of Chapter 54, while the capsule's ultimate purpose and route remain unresolved.",
    "Team Leader Choi privately plans to keep watching Taekyung and recruit him after Butler Kim clears him of being an illegal Awakener or deliberately approaching Choi. Taekyung rejects Choi's latest contract offer—500 million won signing bonus, 50 million won monthly salary, seventy-percent settlement split, officetel, sedan, and social insurance—because he intends to return to Murim, and schedules another meeting."
  ],
  "open_questions": [
    "The Ark - 2020 capsule's ultimate purpose and route remain unresolved; Taekyung has reconnected to Murim, but whether it can transport him safely and reliably and what will happen after the ongoing battle remain unknown.",
    "The limits of Murim's death and resurrection rules remain unresolved.",
    "The identity of the Head Elder's Sound Transmission accomplice, the betrayal's outcome, and the full purpose of their plan remain unresolved.",
    "The cause of Taekyung's recurring nightmares and Jin Wikyung's appearance in them remains unresolved.",
    "Whether the officials' investigation exposes Taekyung, whether the System's restoration relates to Murim, Choi's exact current rank, whether Peace Guild can recruit Taekyung after his refusal, and whether Sopung Guild can recruit Choi Min-su remain unresolved."
  ],
  "temporary_decisions": [
    "The source name 성진호 is Seong Jinho; do not substitute the compendium's separate 송진호 entry.",
    "Use Heavenly Axe for 천력부, Jang Sam's epithet; never romanize this established title.",
    "Use Sky-Piercing Strike for 천관일, the final form of the Jin Family's Spear Technique.",
    "Use Grade for the System/UI field 등급; reserve rank for Hunter classifications and ordinary prose.",
    "Preserve brisk dark action-comedy and character hierarchy without archaic wuxia diction.",
    "Use the accepted terms Heaven's Gate Temple, Three-Turn Footwork, Sound Transmission, Jin Family's Cultivation/Spear/Manoeuvre Techniques, and pleasure house.",
    "Preserve the gold-spoon/God-Spoon wordplay and explain it briefly in a footnote.",
    "Preserve the System titles Gambler and Sex Fiend, and render the Mount Heng demand as commanderies and counties.",
    "Preserve the alliance terms, the approximate count “about two hundred,” the rank “Super First Rate,” and the guards’ crude insult.",
    "Keep Taekyung’s staged title delivery as “Yama. Whip. Great Hero!” rather than treating Yama Whip as a personal name.",
    "Keep the fixed Tutorial wording “Check and Distribute Skill Window Points” in both the objective and completion notice; use “Redistribute” only when previously assigned points are actually reallocated.",
    "Use tone-marked pinyin for Chinese dialogue such as “Tài lěng le” and “Zhōngguó rén ma?”; keep “Shenme” unmarked in Chapter 2 because it supports Taekyung’s “Ms. Sunmi” mishearing joke.",
    "Use Three Paths Sect for 三道問, retaining the Chapter 34 note that the given final character is 問 rather than the usual 門.",
    "Use gukbap with a first-use footnote identifying it as soup served with rice.",
    "Use Hobgoblin Priest and Hobgoblin Great Warrior for the two C-rank Rare Monsters in the Boss Zone.",
    "Preserve the exact System notifications “Synchronization complete” and “All systems are inherited.”",
    "Preserve the *sip-pal* (“eighteen”) finder’s-fee pun and explain the abrupt formal delivery in a footnote.",
    "Keep the exact unreadable-item notification “This Item cannot be read.” and the capsule manual’s permanent user-binding rule.",
    "Use Kim Sangshik for 김상식, and preserve the distinct Hunter rank and mana-control grades in the Choi Min-su recruitment scene.",
    "Use Lizardman Hunter’s Leather Set and Lizardman Slayer’s Harpoon for the First Rate System items, and retain the Pocheongcheon reference with a concise footnote.",
    "Use swamp Lizardmen for 늪 리자드맨 and preserve the female-Lizardman pheromone lure and its resolution in Chapter 51.",
    "Use Lizardman Great Chieftain for 대족장, One Flash for 일섬, and footnote *Bulgeum* as Korean slang for Friday night.",
    "Use goshiwon for 고시원, with a concise first-use footnote explaining the tiny rented-room arrangement and approximate size.",
    "Render the System prompt [무림]에 접속하시겠습니까? as “Would you like to connect to Murim?”; reserve “logged in” for 로그인했다."
  ]
}

## Reading copies

## Chapter artifact 50

# Chapter 50

My mouth fell open at the sight in front of me.

In the hot, humid heat, wetlands stretched on without end along a dense forest.

“This is a D-rank Gate…”

I knew higher-ranked Gates had more space. I just hadn’t thought the difference would be this big.

“Pretty big, right?”

I forgot to be angry and answered.

“Yeah. Big enough to feel lost.”

“This is fairly average. From B-rank Gates on, you even have to hire a separate guide.”

“…Feels like we need one now.”

“We’ll be fine today.”

Team Leader Choi pulled out a laminated sheet and showed it to me.

“What’s that?”

“A map. They gave it to me along with the transfer of rights.”

A map. Then we wouldn’t get lost—

“Wait. What did you say?”

“I said it was a map.”

“No, not that. You said something after that.”

“You mean the transfer of rights?”

Yeah, you. That.

“What does that mean?”

“Exactly what it sounds like.”

Team Leader Choi spoke as if it were nothing.

“This Gate is mine.”

“What?”

“More precisely, I have the exclusive rights to it.”

Maybe it was the wetlands. Sweat beaded on my palms, and my throat went bone-dry.

I swallowed a dry gulp.

*Exclusive rights to a Gate?*

In South Korea, Gates were national property.

Since the Great Cataclysm, Magic Gems had become a core energy source, and Gates were no different from diamond mines that never ran dry. And this guy had exclusive rights to one of those Gates.

*What the hell is he?*

I knew he was a rich family’s young master, but I hadn’t thought it went this far.

“Let’s get moving.”

Team Leader Choi strode ahead. The sight of his back was dazzling.

Ah, that golden radiance. The scent of wealth I could never touch.

*I’ll bury my bones in your Guild.*

I swore it then and there.

* * *

The wetlands were a maze.

Without a capable guide like Team Leader Choi, I would have wandered for a long time. How long had we been walking when—

- Keeiik.

The cry grew even clearer as I drew up my internal energy.

A monster had appeared.

*At least twenty.*

According to Team Leader Choi’s explanation on the way here, the monsters in this Gate were swamp Lizardmen.

They lived in several colonies under a single tribe, and this seemed to be one of them.

“This is the small colony closest to the entrance. About twenty of them, so let’s take them out fast and move on.”

Team Leader Choi hacked through the vines as he advanced. He was usually a pretty-faced young master, but once real combat started, he was no joke. The back driving forward like an eight-ton truck with a broken steering wheel reeked of machismo.

*He’s fucking cool.*

Even if it weren’t thirty Lizardmen but a hundred, I felt like we could sweep them all as long as Team Leader Choi was with me.

Now I understood why people let high-level players carry them in online games.

“Keiik!”

Maybe that was why my first face-to-face with Lizardmen didn’t come with much tension.

All I had was the novelty of seeing monsters I’d only ever seen in photos and videos.

“Oh, they’re big.”

Even the smallest of the twenty was a head taller than me.

They were at least two meters tall, with sleek muscle and thick tails that made them look even bigger.

*Of course, still not as big as the Hobgoblin Great Warrior I fought yesterday.*

These hideous basketball prospects didn’t seem too happy to see us.

- Keiik!

- Keet, keet!

Dozens of harpoons flashed in their hands. Watching them close in from the front in an encircling formation, I spoke.

“No archers.”

“Swamp Lizardmen mostly use harpoons. Watch out for thrown spears, just in case.”

“Yep.”

As expected of a lizard expert. He even had his arms folded, nice and easy.

“Keiik!”

They’d come within twenty meters. I grinned at Team Leader Choi.

“These guys have no fear.”

“That’s a Lizardman trait. They’re reckless, and they prefer a head-on fight.”

“Aha.”

Meanwhile the distance closed to ten meters. Team Leader Choi’s folded arms were starting to get on my nerves.

“I think we should start fighting soon.”

“Guess we should.”

“…Ah. Right. We should.”

Whoosh!

Then three or four harpoons tore through the air. If I’d still been an F-rank Hunter, my life would have flashed before my eyes. Now I just swung my spear and batted them aside.

Clang, clang, clang!

It was only after that that I sensed something off.

- Kieeeik!

- Keet! Keiik!

*What’s wrong with them?*

Their eyes rolled back white as they shrieked. This had gone past hostility. It was practically hatred.

As I stood there bewildered, Team Leader Choi tossed out a line.

“It’s because of your equipment.”

Equipment? Why would equipment—

Ah.

*Lizardman Hunter’s Leather Set. Lizardman Slayer’s Harpoon.*

*Shit. Look at those names.*

If I were a Lizardman, I’d throw harpoons too.

*Come to think of it, they only threw them at me.*

With the enemy of their kind standing right in front of them, Team Leader Choi might as well have been invisible.

At this rate I was going to get attacked nonstop—

No, wait.

“Did you plan this?”

“Plan what?”

“You put this on me to pull aggro so you could mop them up. That’s the strategy, isn’t it!”

“I swear it isn’t.”

Team Leader Choi’s face turned serious as he added,

“Because I’m going to stay put.”

“What?”

“You’ll pull the aggro, and you’ll do the raid too. Don’t get the wrong idea.”

*What the hell is this bullshit.*

“So… I have to fight them alone?”

“Yes.”

“And you’ll stand there with your arms folded and watch?”

“I’ll uncross my arms.”

“No, for fuck’s sake…”

“Harpoons incoming.”

Whoosh!

As the spears were thrown, green scales flashed from every direction and they charged.

Team Leader Choi sprang back and shouted with heroic gravity,

“You got this!”

Was this guy completely insane?

I wanted to run over and grab him by the collar, but harpoons were already flying in from all sides.

Clang!

- Keiik!

“You bastards.”

Grinding my teeth, I drew up my Qi Sense. Soon, twenty spears sprang up over their heads.

> **System**
>
> **Lv. 40 Lizardman Tribesman**

Level 40, huh?

I tightened my grip on my spear.

“You’re all dead.”

Ding.

> **System**
>
> - Damage dealt to this monster increases by 10% due to the effect of **Lizardman Hunter’s Leather Set**.
>
> - Damage dealt to this monster increases by 20% due to the effect of **Lizardman Slayer’s Harpoon**.
>
> - All **Lizardmen** in this Gate are hostile toward you. They will never stop until they repay this grudge!

At the same time, the Lizardman Slayer’s Harpoon traced a heavy arc. The forms of the Jin Family’s Spear Technique, having reached Seven Stars, poured toward them.

Crunch!

* * *

- Keiik…

The yellow reptilian eyes slowly closed.

The green wetlands were soaked with the corpses and blood of the ones already dead. Not a single Lizardman was left standing.

Ding.

> **System**
>
> - Level Up!
>
> - Level Up!

Leaving the cheerful System notifications behind me, I turned around.

Team Leader Choi was leaning against a tree. He’d said he wouldn’t fold his arms, and there he was with them folded. That made me twice as pissed.

“What do you think you’re doing?”

Team Leader Choi looked at me in silence, then tossed something over.

A small drink bottle of red liquid. A potion that restored depleted Stamina.

“So you give me the disease and then the medicine?”

“You look pretty healthy for a sick man. Not a scratch on you.”

…That actually sounded plausible. I nearly bought it.

While I hesitated, Team Leader Choi spoke.

“I’m sorry.”

He didn’t stop there. He even bowed at the waist.

It was such a formal apology I had nothing to say. My anger eased a little, but I still needed the reason.

“Why did you do that?”

“I had to see your skill.”

“Just for that?”

“It’s important to me. I need to know how you move, how much you can take on, and how far we can go together.”

“So you just slipped out alone while it was crawling with monsters?”

“If I hadn’t trusted you, I wouldn’t have.”

When a capable guy hyped me up like that, I had to admit it felt good.

*More importantly, I didn’t even get hurt, and I leveled up twice.*

I asked, quietly hopeful.

“And the results?”

“Hmm.”

Team Leader Choi studied me with that peculiar look of his. At last he opened his mouth.

“I still don’t know.”

“What?”

“Which is why.”

Team Leader Choi pulled something out and tossed it to me.

A long, opaque cylinder. When I shook it, liquid sloshed inside.

“What is this, a potion?”

“There’s a button on the bottom, right? Press it.”

*Does it open when I press it?*

I tilted my head and pressed the button.

Click.

The front of the cylinder sprang wide open.

The problem was—

Fwoooosh—

Boom!

Whatever had been inside shot up like a firework and burst in midair. The pink liquid that exploded there spread out over a wide area.

“Huh?”

*What is that?*

As I stared blankly at the sight, Team Leader Choi’s voice dug into my ear.

“It’s pheromones.”

“Pheromones? Perfume?”

“Something like that.”

“…?”

“It was collected from female Lizardmen.”

The instant he finished speaking, I felt a tremor from somewhere.

The ground. The ground was rumbling.

Team Leader Choi kindly added,

“The effect is extremely powerful.”

*You bastard…*

* * *

“Team Leader Three.”

That was the first thing the middle-aged man with half-gray hair had said in an hour. Kim Sangshik, who had been waiting endlessly while the Guild Master chain-smoked, answered.

“Yes, Guild Master.”

“Curious, aren’t you? Figured I called you in first thing this morning to raise hell?”

“Ah, no, sir.”

The Sopung Guild Master smiled good-naturedly.

“That’s right.”

“What?”

“I called you to raise hell.”

“…”

“Do you know where I went today?”

The Guild Master exhaled a plume of cigarette smoke.

“The Guild Alliance breakfast meeting.”

Small and midsize Guilds were corporations too. In each region, Guild Masters held meetings to form alliances and socialize. That was where he’d been today.

“I was on an empty stomach, just about to take a bite, when that Sangdong Guild Master bastard told me something interesting. He said the C-rank who awakened recently had been one of our Guild people until a few days ago.”

“…Guild Master, that…”

The Guild Master raised a hand and stopped Kim Sangshik from continuing.

“I wondered what kind of bullshit that was. But rude as the Sangdong Guild Master is, he isn’t the type to make up a story. Not at an alliance meeting, either.”

“I’ll look into it again myself!”

“Team Leader Three? No. No need.”

The Guild Master threw a crumpled bundle of papers across the room.

“I already looked into it myself.”

Kim Sangshik recognized the crumpled papers for what they were: someone’s personal file.

And the name on it, too.

“Jin Taekyung. Team Leader Three knows that name too, right?”

*Fuck.*

Kim Sangshik squeezed his eyes shut. The Guild Master tapped the ash from his cigarette.

“I know how you feel, Team Leader Three. You’re a founding member of the Guild, after all. You’re allowed to fire one bottom-tier Hunter you don’t like. Stick your beloved son in the vacancy. Right?”

“Yes, yes.”

“But the F-rank loach you treated like dirt and kicked out turned into a dragon and came back, huh? I even made a point of telling you to recruit him, but if you told the truth I’d obviously raise hell. You’d get a reputation for having dog eyes that can’t even recognize someone. So you filed a false report, right?”

Sizzle.

The Guild Master crushed out his cigarette. As the embers scattered, the last of his patience went with them.

“Team Leader Three. No, Sangshik. Have we been together about twenty years?”

Kim Sangshik answered in an uneasy voice.

“Twenty-one years, Guild Master.”

“That’s not what I meant.”

“…Yes, hyung.”

“Good. That sounds nice. Keep calling me that from now on.”

“What?”

“Twenty-one years of dragging you along is enough. You’ve done your part. I’ll talk to the Team Three kids separately, so as of today, you’re out.”

“H-hyung!”

“Shut your mouth, leave quietly, and I won’t block your path. Once you’re out, do whatever you want.”

The Guild Master’s voice was packed with tightly suppressed fury.

Kim Sangshik realized he had no choices left.

*Leave? Leave the Guild?*

This was the workplace he’d spent more than twenty years in. And now he was being told to leave over something like this. Thrown out without a second thought.

*Fuck…*

He clenched his teeth and walked out of the office.

One last blow came after him.

“Hey, HR. Process two resignations today. Kim Sangshik and Kim Sangho.”

For the next few days, Sopung Guild was in an uproar over the rare event of a father and son resigning at the same time.

Along with that, the hottest topic in the Guild became the recent whereabouts of the bottom-tier Hunter who had quit not long before.

“They say he’s C-rank. A reawakening.”

“Oh my, Mr. Taekyung? The Taekyung I know?”

“That’s what I’m saying. He hit the lottery. Apparently Kim Sangshik went to recruit him without even knowing who he was and got shut down hard.”

“He found every excuse he could to fire him, and now he’s reaped what he sowed. I heard Team Leader Kim’s been going around calling it wrongful dismissal and badmouthing the Guild Master.”

“He still hasn’t come to his senses. Still, I’m jealous. When do I ever get to live a life like that?”

“Honestly, Taekyung deserves it. He worked so hard, so luck found him.”

“Deserves it, my ass. Then are the rest of us all just living it up? It’s luck. All luck.”

Half envy, half jealousy, the conversations always ended with the same question.

“Where is Mr. Taekyung now, and what’s he doing?”
## Chapter artifact 51

# Chapter 51

Swish, swish, swish!

Swords, axes, maces.

Dozens of weapons poured down like rain. But I could see every one of them clearly—where each attack was headed, and how.

I slipped through the gaps.

Slice—

It started with me taking the head off a C-rank monster, a Lizardman Warrior. The instant the spearhead drew a semicircle, blood spurted in every direction.

Ding. Ding. Ding.

> **System**
>
> - You defeated **Lv. 40 Lizardman Warrior**!
>
> - You defeated **Lv. 41 Swamp Lizardman**!
>
> - You defeated **Lv. 40 Swamp Lizardman**…

- Keeee…

The survivors hesitated and backed away. The same creatures that had been pouring out killing intent at the enemy of their kin were now trembling with fear.

But that lasted only a moment.

- Gwoooaar!

> **System**
>
> - Boss Monster, **Lv. 52 Lizardman Great Chieftain**, has appeared!
>
> - Uses Skill **Battle Cry**!

A frame at least twice as large as the others. The roar of the Lizardman Chieftain, gigantic mace in hand, exploded through the air. The Lizardmen that had been backing away came to their senses at their leader’s appearance and formed ranks.

*I was wondering why this was wrapping up so easily.*

Team Leader Choi’s unhurried voice came from behind me.

“Can you handle it?”

“Is that something someone who hasn’t lifted a finger for days should be asking?”

“This is a different story. It’s a C-rank Gate.”

“Then help, why don’t you.”

Team Leader Choi thought it over before answering.

“I don’t think I can. I wore a limited edition today. It’d break my heart if blood splattered on it.”

“……Should I make it hurt for real?”

The longer we talked, the more my gut burned and the back of my head throbbed, like I’d taken internal injuries. Fighting monsters would have been better.

As I took a long stride forward, Team Leader Choi tossed out a single line.

“Retreat is another option.”

The man standing behind me with his arms folded so blood wouldn’t splatter on his limited-edition Equipment had said something pretty sensible.

A punchable kind of sensible.

And then…

“Why bother, when there’s a better way?”

Ahead of us, the monsters were surging forward like a wave, led by the Lizardman Great Chieftain. C- and D-rank monsters mixed together—a force an ordinary C-rank Hunter wouldn’t even dream of facing.

An ordinary C-rank Hunter, that is.

*Status Window, open.*

Ding.

The System answered at once.

A week had passed since I’d started Hunter work again. On the Status Window, the number 40 and the line written at the very bottom were shining bright.

> **System**
>
> - Remaining Points: 100

Since returning to reality, I hadn’t spent a single Remaining Point. Purely out of curiosity.

*How far can I go as I am now?*

But hoarding them any further would be reckless.

*Assign 30 each to Strength and Stamina. Assign 40 to Agility.*

The next moment, my Remaining Points hit zero.

In exchange, new power surged up from deep inside me. A different me from the Jin Taekyung of only a few seconds ago was standing here now.

*Yeah. This is it.*

My body was still shivering with exhilaration when—

- Gwaaaar!

The Lizardman Great Chieftain charged with a roar. I thrust my spear toward the gigantic mace that cast a shadow over me.

“One Flash.”

At the spearhead, a path through the wind opened.

* * *

“Hah.”

Team Leader Choi—Choi Minwoo—let out a hollow laugh.

A dense fog of blood wrapped the wetlands, and beneath it the monsters’ corpses lay sprawled.

*What the hell…*

Dozens of monsters, the boss included, had been slaughtered in an instant. All of it had come from the spear-tip of a C-rank Hunter who had reawakened only a few days ago.

*Is something like this even possible?*

It was a question he had carried since the day he first met Jin Taekyung.

That day, they had gone to an E-rank Gate without much thought. There, Taekyung had overwhelmingly overpowered a Rare Monster that normally took a couple of C-rank Hunters to bring down.

And on top of that, the strength he had shown over the past few days was…

*Calling him a C-rank Hunter is a joke.*

The reason Choi had started raiding with Taekyung alone was simple.

To see this fascinating man’s limits.

And to keep anyone else from finding out.

But another thought suddenly occurred to him.

*Could he be stronger than me…?*

No. No.

That was impossible.

Choi Minwoo forced the thought aside. That was when Jin Taekyung entered his vision.

He was clutching the boss monster’s corpse—its upper body gone—and wailing in grief.

“No! My hide! This was expensive!”

……There was no way a guy like that could be.

No. He *mustn’t* be.

Choi Minwoo suddenly felt cheated.

* * *

Burning Friday. *Bulgeum*, for short.[^1]

People in their twenties would be drinking in packs and drifting in and out of clubs. I was running Gates with Team Leader Choi.

Once in the morning. Twice in the afternoon.

By the time we finished three C-rank Gates and came back out, it was already dark.

“Good work, young master.”

That face was familiar now. Team Leader Choi called this broad-featured man in his forties that.

“You worked hard too, Mr. Kim.”

Kim the Butler. Not secretary—*butler*.[^2]

The word was so absurdly unrealistic I thought I’d misheard it at first.

*I’ve only ever met church deacons.*

Back when I was a snot-nosed kid getting a thousand won a week in allowance, he had been the bastard who forced me to put in a hundred won as a tithe.

Of course, he hadn’t called me young master. When I dug in and refused to pay, he’d even muttered that I was the child of Satan.

And I had been seven—the kind of kid who always asked when he was curious.

*Mom. Are you Satan?*

*Huh? Satan?*

*Yeah. The church deacon said I was Satan’s child. I’m your kid, so that makes you Satan, right? Right?*

That turned my mother into Satan.

I never got to eat the church tteokbokki again,[^3] and the church deacon nearly went to be with the Lord.

Thinking about it again, my life really was one hell of a variety show.

“Did you have something to say…?”

Butler Kim’s voice pulled me back.

“Nothing. I was just thinking about something else.”

“Let’s call it a day.”

Team Leader Choi had already changed into street clothes. In a thin tailored suit, he looked just like a celebrity.

*Life is so damn unfair.*

I grumbled inwardly as I started taking off my Equipment. Carefully, of course. I’d looked up the price on the first day, and it was…

Never mind. Let’s not go there.

While Butler Kim took the Equipment and loaded it into the car, I asked Team Leader Choi,

“What time should I come in tomorrow?”

“Tomorrow?”

Team Leader Choi asked back, sounding puzzled.

“Today is Friday.”

“Yes.”

“And tomorrow is Saturday.”

“I know Saturday comes after Friday.”

*Does he take me for a fucking idiot?*

“No, I mean…”

Team Leader Choi furrowed his brow.

“Don’t tell me you’re planning to work on the weekend too?”

“……Isn’t that obvious?”

“……”

“……”

Team Leader Choi asked with a shocked look,

“If you don’t take weekends off, when do you rest?”

“Um. When I can’t find work?”

“How often is that?”

“I don’t know. If I take a lot of time off, maybe once a month?”

“You used to belong to a Guild. You worked weekends then too?”

“I did, if there was work.”

“Isn’t that a violation of the Hunter Labor Law?”

Even Team Leader Choi, who seemed perfect, didn’t know one thing.

How the world actually worked.

I chuckled.

“What small or midsize Guild follows that to the letter? They all throw on extra pay and send you out on raids. Worked out for me, anyway.”

“Excuse me? You *liked* it?”

“I go to the Manpower Office on weekends. Getting extra pay from the Guild beats going there. They paid cash on the spot so there wouldn’t be a record.”

“……”

“That’s just how it is.”

Team Leader Choi shook his head in disbelief.

“Our Guild follows the Labor Law. Provisional contracts are no different.”

*That’s a shame. Looks like I’ll have to go to the Manpower Office this weekend.*

Team Leader Choi looked at me with that peculiar expression of his as I smacked my lips over the missed chance.

“Why do you go that far?”

“Why?”

“You’re a C-rank Hunter now. You could take it a little easier.”

“That’s…”

*Because I don’t know when the System might disappear.*

I caught the words before they jumped out of my throat. That was my secret—something I couldn’t tell anyone.

“No particular reason. You have to row when the tide comes in.”

“If you keep working like that, you’ll snap the oars. Think about the people in the boat with you.”

“The people in the boat with me? You, Team Leader?”

“Well, for example…”

Team Leader Choi paused, then went on.

“Your family, perhaps.”

Family.

It was only one word, but warmth seeped into every corner of my body. We talked on the phone now and then, but I hadn’t seen them in more than two months. Counting the time in Murim, it had been three.

*Has it already been that long?*

Ever since my father died, my life had been a car running uphill.

So I’d had no choice but to keep my foot on the gas. Take it off, and it felt like I’d roll backward. Like the engine might die at any second.

“Anyway, weekends are off. Don’t even think about going to the Manpower Office. Rest. That would be a contract violation.”

“Ah. Right.”

*Forcing me to rest this hard… Maybe this guy Choi isn’t such a bad person after all…*

No.

I couldn’t let myself get taken in by a little emotional appeal. Not after all the hell I’d gone through on my own.

*Team Leader Choi is an exploitative employer. An exploitative employer.*

It was obvious he only wanted me resting on the weekend so he could work me to the bone starting next week. The mindset of a slave plantation owner who didn’t want stamina wasted in the wrong places.

What a vicious man.

“Preparations are finished, young master.”

Butler Kim was back from loading the Equipment.

*That man’s suffering under an exploitative employer too. It’s almost ten at night, and he still hasn’t gotten off work.*

“Ah. What about the thing I mentioned?”

“I brought it.”

“Give it to him.”

At the exploitative employer’s word, Butler Kim held out the small box in his hands.

“Please take this, Hunter.”

To me.

“Huh? Me?”

It looked like a box of tonic drinks. I just blinked at it, then a thought flashed through my head and I asked carefully,

“Don’t tell me this is money?”

“We contracted for weekly pay. Did you forget?”

I had. I’d naturally assumed I’d get it on Sunday.

I took the box with a dazed look. It was heavy.

“Is it usually paid in cash?”

“Of course not.”

“Then…”

“You said you liked cash, Mr. Jin Taekyung. Especially crisp new bills.”

I’d mentioned it in passing yesterday—or the day before. I hadn’t expected it to come back like this.

My opinion of the exploitative employer rose a little.

*Of course, the important part’s still left.*

Four days of pay, Tuesday through Friday. My first weekly paycheck as a C-rank Hunter.

Of course I couldn’t help looking forward to the amount.

I swallowed and opened my mouth.

“Then how much is all of this…”

“We put in a little more than the contract. The settlement details are inside, so check them. We’ll be going.”

“Until next time, Hunter.”

Team Leader Choi and Butler Kim took off in a flash.

It really did happen in an instant.

I stared after the receding car lights, bewildered, then opened the drink box. In the faint moonlight, thick bundles of bills caught my eye.

*One, two, three…*

The count stopped at six.

Six bundles of a hundred bills.

In other words, six million won.

“What is this?”

*Scam.*

The word flashed through my mind, and just as my legs were about to give out—

“Huh?”

Had I seen it wrong? Why were the bills yellowish?

“Wait. Wait a second!”

I focused internal energy into my eyes, and the world in front of me brightened.

Then I saw her.

A kindly smiling woman in a hanbok, right there on the bill.

“Shin Saimdang! Wise mother and virtuous wife! Her son is Yulgok Yi I! Her husband is Yi Wonsu!”

Dialect burst out of me before I knew it.

This was insane. Completely insane.

One bundle was a hundred Shin Saimdang bills. Six of those, so…

“Th-three hundred million!”

This time I couldn’t catch my legs as they gave out. I dropped to my knees hard enough to thud and stared blankly into the drink box.

Under the bundles, a white sheet of paper lined the bottom.

*Right. The settlement sheet!*

I unfolded the paper in a panic.

It had a complete record of the past four days’ earnings.

Down to the final amount being paid to me.

*The settlement says thirty million won?*

What? Had I imagined it?

I was confused. Completely confused.

My shaking gaze froze on the last line.

**Bonus: 270,000,000**

And then Team Leader Choi’s last words as he left.

*We put in a little more than the contract.*

Thunder and lightning tore through my head.

I stood on trembling legs. Far off, the car’s lights were already fading.

They looked like a single ray of light.

“Ahh. Aaaah…”

Team Leader Choi.

No—he was the Light.

[^1]: Korean slang for Friday night, from “burning Friday.”
[^2]: In Korean, the same word, *jipsa*, means both butler and church deacon.
[^3]: Tteokbokki is a Korean dish of chewy rice cakes in a spicy sauce. Korean churches often sell it as a snack.
## Chapter artifact 52

# Chapter 52

Six in the morning.

Taxi driver Mr. Kim picked up his first fare of the day.

And regretted it ten minutes later.

*I’ve been jinxed.*

The young man looked perfectly normal at first glance. Sturdy, muscular build, clean-cut face—even being generous, he only looked mid-to-late twenties.

But then…

“Sniff, sniff.”

Something was off. Very off.

“Huuugh.”

He was hugging a drink box like treasure, cracking it open every thirty seconds to smell it, then shuddering like he was possessed.

*What in the world is he doing?*

A chill crawled up the back of Mr. Kim’s neck. He had been driving a taxi for more than ten years, but he had never had a problem customer quite like this.

He kept stealing glances at the young man in the passenger seat, and in that moment—

“Mister.”

“Yes, yes?!”

He nearly had a heart attack.

The young man’s eyes, hollow only a moment ago, were gleaming like a beast’s.

“There’s a truck behind us.”

“A-a truck? A blue one?”

“Yes. Doesn’t it look like it’s been following us since that intersection?”

“Huh? Well, I suppose it does.”

“It might be tailing us.”

What fresh bullshit was this?

Mr. Kim’s eyes darted around, and in the end he gave the answer the young man seemed to want.

“I-I’ll peel off to the side.”

The young man hugged the drink box tight until the blue truck disappeared from view. As if someone might snatch it away.

“Sniff. Sniff.”

Of course, he didn’t skip smelling it whenever he got the chance.

*This guy’s completely insane.*

The AC was blasting inside the car, but Mr. Kim’s back was soaked with cold sweat.

And this was the first fare of the day.

A thoroughly jinxed day.

* * *

Vroom.

The moment I handed over the fare and shut the door, the taxi shot off like a bullet.

Anyone watching would’ve thought a monster was chasing it. What if he got in an accident?

I clicked my tongue and headed into the apartment complex.

I still had yesterday’s drink box hugged carefully to my chest.

*Three hundred million won.*

About as much as I’d saved over three full years as an F-rank Hunter. Of course, I didn’t have a single won of that left now.

*I spent it all paying off debts.*

There had been a time when I was drowning in debt, but I’d gritted my teeth and kept at it until things gradually got better. I’d even moved my family to a safe-zone apartment near Ilsan.

Lately, though, my life had been like a roller coaster.

A roller coaster that dropped whenever the System disappeared…

No. I was coming home for the first time in months. I should drop thoughts like that.

*Which building and unit was it again?*

I only came here once every couple of months, so it was always like this.

I glared at the apartment buildings packed in tight, then pulled out my phone and called. The ringtone went on for a long time before the line finally connected.

Click.

“Hello?”

I’d figured Hayeon would still be asleep this early, but her voice was clear.

“You were already up?”

“I have to be. Do you know what time it is?”

“It’s not even seven.”

“I study better when I get up early.”

My little sister never failed to impress me. Jinho hyung, who treated getting up in the morning like one of the seven deadly sins, should’ve heard that.

“Why’d you call?”

“I’m out front.”

“Huh? Out front?”

“Yeah. But I forgot which place is ours.”

“……Again? You really do the damnedest things. Wait there.”

I stood there holding the dead phone. After a few minutes, a girl appeared at the entrance of one of the buildings, dragging her slippers.

Even from a distance, she radiated total bum energy. That face said the whole world was too much trouble, and I couldn’t help smiling.

“Jin Hayeon!”

“Don’t yell. You’ll wake people up.”

……Yeah. That was my little sister.

“What brings you here? You didn’t even tell us you were coming.”

“Do I have to announce it every time I come to my own house?”

“You come so rarely. The residents’ association president probably visits more than you do.”

“That bad?”

“That bad.”

The elevator stopped. Hayeon punched in the password at the front door and turned the handle.

And there—

“Son!”

Someone stood there beaming.

Wrinkled hands. A perm half fallen out. She looked as happy as a kid getting a surprise gift.

My throat tightened. I scratched my chin, then burst out laughing.

“I’m home, Mom.”

I had finally come back.

To the place where my family was waiting.

Home.

* * *

Sizzle, sizzle.

Mom was busy with breakfast in the kitchen. A good smell hung in the air.

“Mrs. Kim is really excited now that her son’s home after so long.”

Hayeon scratched her stomach and plopped down beside me.

The old sofa sagged.

What a pig.

“Is she making a lot?”

“Yeah. A whole feast. Looks like we’re eating well today.”

She answered, but her eyes stayed glued to her phone.

“You haven’t seen your brother in ages. Aren’t you happy to see me?”

“Huh?”

“I mean, you could at least massage my shoulders after all the work I did.”

Hayeon let out a long sigh.

“What’s gotten into you, Mr. Taekyung? We’re not that kind of siblings.”

“……Listen to that attitude.”

It wasn’t like we’d only started bickering yesterday, but I still felt a pang.

I mean, I’d barely made it back after brushing past death!

“That got to you just now, didn’t it?”

Her radar was scary.

“Go get ready for school, you little cafeteria parasite.”

“Mm. Today’s the school founding anniversary.”

My fist trembled.

I wanted to smack the back of that irritating head right then and there, but doing it would mean I’d really lost.

“You want to hit me, don’t you? Your fist is shaking.”

“You’re lucky you’re a girl. If you had balls, I would’ve—”

“Mom! My brother’s sexually harassing me!”

“Hey, hey!”

“He said my b—mmph!”

I clamped a hand over Hayeon’s mouth. She thrashed, hitting and pinching, but she was still just a nineteen-year-old girl. It didn’t hurt.

Then, by pure coincidence, the foot she flung out slammed into the drink box I’d set so carefully in the corner of the sofa.

Thump.

Flutter.

The box flew wide open.

Yellow bundles of bills spilled across the living-room floor.

Hayeon froze.

“Come on, stop fighting and eat your breakf—”

Mom had come out of the kitchen too.

Everything in the living room stopped as if someone had hit pause. Only the quiet sound of stew simmering filled the space.

Sizzle, sizzle.

I smiled awkwardly and opened my mouth.

“Can’t we talk about this after breakfast?”

“……Son?”

“Mmph, mmph, mmph.”

Breakfast was probably going to be delayed for quite a while.

* * *

I told my family a suitably edited version of everything that had happened so far.

My reawakening as a C-rank Hunter, and where the money had come from.

“So that’s how it happened.”

Their reactions split in two.

“I see.”

Mom nodded blankly.

And then—

“Proof.”

“……”

Yeah. I hadn’t expected anything else from you.

I sighed and tossed her my wallet.

“What’s this?”

“Check it.”

Hayeon looked at me with suspicion, then started digging through the wallet. There was barely anything in it, so it didn’t take her long to find *it*.

“Whoa.”

A single card in her hand.

The C-rank Hunter license the Association had issued me two days ago.

“This isn’t fake, is it?”

“Want to get hit?”

“Guess it’s real.”

“Forging one is a serious crime, you idiot.”

“What about that money? Did that Team Leader Choi or whoever really give it to you, like you said?”

“How many times do I have to tell you before you believe me?”

“About three hundred and fifty?”

Despite her words, she seemed to believe me now.

The C-rank Hunter license gleaming silver. Neatly stacked bundles of three hundred million won.

Every bit of it looked completely out of place in this old, cramped living room.

Mom sat there staring blankly and muttered, almost a groan.

“What on earth is all this……?”

Hayeon let out a hollow laugh like an old woman who had seen everything life had to offer.

“I know. You live long enough, you see it all.”

“You’re not even twenty yet.”

“It’s just an expression. But, Mom.”

“Y-Yes?”

“I smell burning.”

“Oh, right! The stew!”

Mom’s half-lidded eyes flew open. I got up in a hurry, but the kitchen was already a wreck.

Mom followed me in, stomping her feet.

“Oh no, what do we do!”

The broth had boiled down to almost nothing, and the fish had turned to lumps of charcoal. I’d been looking forward to a home-cooked meal after so long, but……

Well, this kind of development wasn’t so bad either.

“Let’s go eat out. It’s been a while.”

On any other day, Mom would’ve launched into a whole speech about how ridiculous restaurant prices were, and Hayeon would’ve asked us to order chicken. This time, both of them stayed quiet.

“Little sister.”

“Yes, dear brother.”

“Grab the money.”

“Yessir.”

Hayeon swept up the bundles like she’d been waiting for the order.

* * *

“I’m sorry, but our restaurant has a dress code…….”

The manager of the upscale restaurant—where a course meal ran to several hundred thousand won a person—gave us an awkward smile.

“A dress code?”

“Yes. As you can see, the other guests are the same.”

He was right. Men and women alike, all in suits and dresses. Some were even in evening gowns.

*Shit. Anyone watching would think they’d come here to dance at a ball.*

What was this, eighteenth-century France?

For someone like me, who’d only ever gone to gukbap[^1] places, it was a massive culture shock.

“Let’s just go somewhere else.”

“Yeah. Hayeon knows a lot of good restaurants around here.”

The family looked even more embarrassed than I did, so I just walked out.

The three of us were reflected in the restaurant glass. We’d clearly dressed up for our first meal out in a long time, but every piece we owned was cheap market-brand stuff that already looked well-worn.

*Had they been that short on money?*

I’d sent most of what I earned home, cutting back on food and clothes for myself.

Even as an F-rank Hunter, I’d worked twice as hard as other people. It shouldn’t have been a small amount.

“Son, should we go get pork belly? Maybe greasy food is a bit much this early in the morning.”

“Pork belly’s good. Mom knows what’s what. A friend went to the meat place at the intersection up ahead and said it was amazing.”

Just pork belly.

I had a C-rank Hunter license in my wallet and a bag stuffed with cash. It wasn’t like they didn’t know that. They could splurge without worrying.

*That’s why I work.*

Someone once said you can’t buy happiness with money. That happiness doesn’t have a price tag.

Personally, I had one thing to say to people who talked like that.

*Fuck off.*

Money’s what you can’t spend because you don’t have it.

And after thinking all night about how to use this money, I’d finally made up my mind.

At least for today, I would spend it freely on my family.

Right now, that decision had swollen even bigger.

“Let’s eat a little later.”

Without waiting for an answer, I flagged down a passing taxi.

“Where can I take you?”

“Mirae Department Store.”

It was supposed to be the biggest, most expensive department store in the area. In the rearview mirror, Mom’s eyes went round.

“The department store?”

Meanwhile, the corners of Hayeon’s mouth curled up slyly.

“Nice. My rich oppa can buy me clothes too.”

Sharp as ever. I only had to say the word and she got it.

I snorted.

“Buy whatever you want.”

“Really?”

“Pick out Mom’s things first.”

“Okay.”

“You’ve got yourself a devoted son, ma’am. Ha ha.”

Only then did Mom smile at the driver’s banter.

* * *

“You’re really buying everything?”

“Everything.”

Once I confirmed it for the last time, Hayeon tore through the department store like a colt off its reins. The way she scanned clothes was viciously sharp, and she moved so fast I started to wonder if she was an Awakened.

At first, Mom looked at the price tags more than the clothes. Before long, she started moving with enthusiasm too.

“Mom, what do you think of this?”

“Isn’t it too short?”

“This one!”

“That’s nice.”

“This too!”

“That’s pretty. Excuse me, miss—do you have this in one size larger?”

Two hours passed, and I felt a change in my body.

*I’m dying.*

Crushing shortness of breath and pain in my legs, for no reason I could name.

Helplessness wrapped around my whole body at about the same level as when I’d faced Jopil in Murim.

“Oppa, how do I look?”

“You’re ugly. Get lost.”

“Son, try this on.”

“I don’t think I need to try it. I’ll take that.”

I don’t know how many clothes we bought that day, or how much we spent.

All I know is, by the time we finished shopping and headed out, someone high up at the department store had come to see us off.

“Welcome.”

The manager of the restaurant that had been so strict about its dress code didn’t even recognize us.

“Wow, I’ve never eaten anything like this before.”

“I know. How do they make the food look this pretty?”

Mom and Hayeon spoke in hushed voices, their cheeks flushed.

We’d spent dozens of times more than the several-hundred-thousand-won course meal just to eat it, but it was a day when not a single won felt wasted.

“But I want rice. This is too rich.”

“Why are the portions so small?”

……I pretended it didn’t.

[^1]: A cheap Korean rice-and-soup meal, typically eaten at modest diners.
## Chapter artifact 53

# Chapter 53

Ding.

> **System**
>
> - Sleep Mode has ended.

“…O-oppa!”

I gasped and opened my eyes.

The first thing I saw wasn’t the ceiling of my goshiwon[^1] but Hayeon’s face.

*Oh, right. I came home yesterday.*

“Did you have a nightmare?”

“Huh?”

“You’d been screaming. And you were sweating like crazy.”

*I was?*

Before I could even ask, I understood. My whole body was soaked in sweat, and my throat stung as if I’d swallowed sand.

*Why do I feel like this?*

The System I had didn’t only work while I was awake. Sleep Mode let me sleep deeply and pulled my condition up to its peak at the same time.

Nothing like this had happened in Murim, or after Synchronization. And a nightmare, on top of that?

*What did I even dream?*

My head just throbbed. I couldn’t remember the dream at all.

Hayeon asked, worried,

“Has something bad happened lately?”

“No. Nothing like that.”

“If there is, tell me. Don’t suffer by yourself.”

“Yes, nuna.”

“I’m not joking.”

Her little fist thumped my chest. Hayeon’s serious face left me with nothing to say. I scratched my chin.

“Really? No worries? Nothing hard going on?”

“I told you, there’s nothing.”

It was a lie. There had been things seven years ago, and there would be things seven years from now. There’d been days I locked myself in my room and cried, and days I drank myself senseless with Jinho hyung just to forget.

*That’s enough.*

There were things I couldn’t tell my mother, who’d worked until the cartilage in her knees wore down raising two young kids, or my little sister, a high-school senior now preparing for her college entrance exam.

Enduring and getting through things alone. I was used to it by now.

I flashed a grin, like nothing was wrong.

“My life’s finally about to take off. What would I have to worry about? Ah, there is one thing. How I’m supposed to spend all this money. Something like that.”

“Show-off.”

The mood lightened a little. I made a face on purpose.

“Show-off? Don’t you remember yesterday? Want me to show you the bundles of cash again?”

“I’ll give you that. You’re obnoxious, but I can’t argue.”

“I’ve hit the peak of my twenty-seven-year life graph. Nothing’s going on, so you just study hard.”

“My grades are in the top 0.1 percent nationwide, okay? I’m doing more than well enough, so don’t worry.”

Hayeon pouted and started to leave, then stopped and turned back.

“Oppa. But…”

“Yeah?”

“Who’s Jin Wikyung?”

“…What?”

A name I never expected, at a moment like that.

My body went rigid.

* * *

Crunch.

I bit into a piece of freshly made young-radish kimchi. It was Mom’s cooking, the food I’d wanted so badly, but I could barely taste it.

Because of the conversation I’d just had with Hayeon.

“Where did you hear that name?”

“From you. You kept calling it in your sleep.”

And then her last question.

“Someone you know? If they show up in your dreams, you must be close.”

I couldn’t answer. I hadn’t found that answer in Murim or in reality.

No. I no longer had any reason to look for it. I had come back to reality, and Jin Wikyung was in Murim.

*Then why did Jin Wikyung suddenly show up in my dream…?*

My head was a mess. An aftereffect of Murim? The word PTSD surfaced—post-traumatic stress disorder.

*This is driving me crazy.*

I must have looked grim without realizing it. Mom asked carefully,

“Have you lost your appetite? I made all your favorites.”

“Oh, no. When did you make the kimchi? And this doenjang-jjigae is perfect.”

I scrambled for an excuse and picked up my spoon. For the first time in ages, the three of us were together at one table. I couldn’t ruin this.

*It’s nothing. It has to be nothing.*

Slurp.

Even so, the savory doenjang-jjigae tasted faintly bitter.

* * *

That uneasy corner of my mind soon went back to normal.

I laughed and talked with my family all day. I even took a long nap, and then it was evening.

Time to go back.

“Stay a few more days. I was going to make boiled pork tomorrow.”

“Our Mrs. Kim is starting again. I know how to eat boiled pork too, you know?”

Hayeon grumbled at the reluctance dripping from Mom’s words.

“She packed you a ton of side dishes already, so why are you so worried? At this rate she could open a side-dish shop.”

“…That’s true.”

The shopping bags Mom had ready by the front door were packed with side dishes. This, too, was the compromise I’d only gotten after talking her down.

*There’s nowhere to put them.*

If I put a fridge in my three-pyeong goshiwon room, there really wouldn’t be anywhere to stand. No—there wasn’t even room to put a fridge.

I already had a capsule the size of one.

*Should I start looking at moving?*

I was thinking that as I slung the backpack I’d packed last night over my shoulder.

“…?”

Why was it so heavy? All I’d put in were a few outfits I’d bought yesterday.

When I set the backpack down, my family was the ones who suddenly got frantic.

“Son, you’ll be busy starting tomorrow, right? Hurry back, wash up, and get a good night’s sleep.”

“…A minute ago you told me to stay a few more days.”

“Oppa, you’re going to miss your bus.”

“I’m taking a taxi, though?”

“Night surcharge. There’s a night surcharge.”

At that point, I had a pretty good idea.

“When did you put it in?”

“P-put what in?”

“The money.”

Their faces answered for them. I sighed.

“I told you to keep it and use it when you needed it.”

“….”

“I make plenty of money. And I will from now on, too.”

I mixed fact and fiction fifty-fifty.

The average annual salary of a C-rank Hunter was five hundred million won. I’d met a generous employer in Team Leader Choi and gotten a bonus I never imagined, but if the System disappeared, all of it would go up in smoke.

That was why I’d wanted to give even more to my family, but…

“That’s money you risked your life to earn. Spend it on yourself. All right?”

“Mom.”

“Son.”

The next moment, the quiet words that came from Mom left me speechless.

“Don’t push yourself. Don’t get hurt, either. That’s enough for Mom.”

What else was I supposed to say?

A little later, I stepped out into the humid air of a summer night.

With shopping bags full of side dishes and a backpack stuffed with bundles of cash.

Vroom.

The whole taxi ride back to the goshiwon, I thought of Mom’s last words, and the warmth in them.

And of a voice in a memory that was growing fainter and fainter.

“Survive. I’m telling you to run without looking back. That’s your mission.”

* * *

Shaaah—

Blood spurted. Not the green blood of a monster, but red human blood. Feeling the burning pain in my thigh, I rammed my spear into the Lizardman Chieftain’s chest.

“Keee…”

Ding.

> **System**
>
> - You defeated **Lv. 50 Lizardman Chieftain**!
>
> - You gained EXP!

Gate cleared. A mana field leading outside formed over the Lizardman Chieftain’s lifeless body.

That was when Team Leader Choi pushed away from the tree.

“Three.”

“Pardon?”

“The number of times you’ve been injured today, Mr. Jin Taekyung.”

His long, sturdy fingers pointed to spot after spot on my body.

The nape of my neck and my arm, already treated with potions, and my thigh, still bleeding.

“I’m fine. It only grazed me. A low-grade potion is more than enough…”

“You’re not fine.”

He cut me off, his tone firm. Team Leader Choi’s expression was always unreadable, but this time was different.

One thing was certain. The emotion in that look wasn’t simple concern.

“You weren’t injured even once last week. Same Gate, same monsters. If this is happening, there’s only one reason.”

His clear eyes turned on me.

“Mr. Jin Taekyung. Is something wrong?”

* * *

One day. Two days. Three days.

Time passed, but things didn’t improve. In the end, on the fourth day, I took injuries in five places.

“Not in your current condition. Go home.”

Leaving Team Leader Choi’s words behind, I headed for the goshiwon, my head a mess.

*What’s the problem?*

Everything had been going well. The System hadn’t disappeared, and my account had some three hundred million won sitting in the bank. All that was left was to keep riding high as a C-rank Hunter, but…

*Damn dreams.*

That was when it started. After the first night at my family’s house, I began having nightmares.

The scenes in them grew clearer and clearer, and when a dream ended I woke up soaked in sweat. Even if I circulated my qi and pulled my condition up, my mind was unstable, so the mistakes only multiplied.

*This is going to be a problem.*

My body was in reality, but my mind was still trapped in Murim. I was wondering whether I should see a psychiatrist when I reached my goshiwon room.

Click.

“Oh, you’re back?”

The greeting was so natural I almost wondered if I’d walked into the wrong room.

I asked, incredulous,

“What are you doing?”

Jinho hyung answered,

“Disassembly and assembly.”

He was sitting in front of the capsule with a screwdriver. For a second my vision went yellow.

*This bastard isn’t actually—*

“Are you crazy? Move!”

“Hey, hey. You have to hear Korean all the way through.”

Jinho hyung hurriedly waved his hands.

“I haven’t even started yet.”

“What?”

“I just got here too. Seriously.”

He didn’t look like he was lying. Only after I checked that the capsule was still intact did a sigh of relief slip out.

“Phew.”

Jinho hyung looked thrown by my reaction.

“Why are you making such a fuss over one junk capsule that doesn’t even work? What happened to tossing it out like a piece of luggage?”

“That was then.”

There was no way Jinho hyung could know about Synchronization. Or what that unidentified thing—just a junk capsule to him—meant to me.

“Anyway, don’t touch it. Got it?”

“You look ready to beat me to death.”

“I’ll tear you apart.”

“….”

I ignored Jinho hyung’s baffled face and flopped onto the bed.

After that little episode, it felt like all the energy had drained out of me.

“Something going on?”

“Going on, my ass.”

“Complaints about you have been no joke lately. Today I barely calmed the guy next door down and sent him off.”

I could guess why.

Jinho hyung scooped up the tools he’d spread on the floor and went on.

“He says he’s going crazy because you keep groaning all night. Oh, and he asked who Jin Wikyung is.”

That name again.

I buried my face in the pillow.

“Just tell him she’s my girlfriend.”

I saw his hand quiver around the monkey wrench.

“You got a girlfriend? You traitorous bastard.”

“….”

“She pretty? How old? Show me a picture.”

This guy was thirty. I couldn’t help but despair.

“The name’s a bit exotic, though. Is she an ethnic Korean from China? Or Chinese?”

“…Chinese.”

Not exactly wrong.

“This bastard hits C-rank and he’s already gone global. Anyway, introduce me to a girl. I like China. Nǐ hǎo ma? Wǒ ài nǐ. What else was there?”

“You fucking bastard.”

“Idiot. You got the tones and the pronunciation all wrong. With that, you think you’ll last a hundred days? Repeat after me. Nǐ chī fàn le ma?”[^2]

“You fucking bastard.”

“Again. Nǐ chī fàn le ma?”

“You fucking bastard.”

“…What the hell is this bastard doing?”

I ignored Jinho hyung, who was getting angry at this sudden realization, and pointed at the door.

“Get out.”

*Please. Just let me have some time to myself.*

* * *

Once the room was quiet, I sat up on the bed and went over to the capsule. I tapped its old, grime-caked surface and muttered,

“What the hell are you?”

As expected, no answer came back.

I’d been hoping, privately. Shame.

*The System’s already synchronized with reality. Why couldn’t a machine talk too?*

Honestly, I wasn’t even sure it was a real machine. Reality had been fantasy for a long time now, but wasn’t this a whole new genre?

If I wrote my current situation as a novel, what genre would I even pick? Fantasy? A game novel? Or—

*Dimensional travel?*

Pffhh. A deflating sound slipped out. Dimensional travel? I really was losing it. There was no way something like that was possible.

There was no way it could be…

It was like ice water over my head. My mind snapped clear.

*…It is possible.*

Dimensional travel had happened in the past, and it still existed now.

The invasion of the Demon King Asmodeus, and the Gates, were the proof.

We only used Gates to come and go from reality, but decades ago a monster army had crossed through one from another dimension to Earth.

*The Demon World.*

A land of evil. The home of monsters. The Demon King’s domain.

An unknown dimension no human had ever set foot in, or even glimpsed. That was how humanity defined it.

But what if this capsule in front of me was a kind of Gate to another dimension? What if Murim was another unknown dimension?

*Murim is another reality.*

Everything I had seen and been through there.

Water. Earth. Wind. And people, too.

*They weren’t NPCs.*

I stared at my vacant face reflected on the capsule’s faded surface.

For a long while after that.

[^1]: A *goshiwon* is a tiny, inexpensive room-for-rent housing arrangement; three pyeong is roughly ten square meters.

[^2]: *Nǐ chī fàn le ma?* means “Have you eaten?” In Korean, its pronunciation resembles a profanity, which is why Taekyung keeps answering with “You fucking bastard.”
## Chapter artifact 54

# Chapter 54

It felt like watching an old TV.

Scenes and voices stuttered across a faded screen, cutting in and out. Even so, the heat of the battlefield came through vivid.

“Kill!”

“Destroy the Jin Family of Taiyuan!”

The people packed into the narrow gorge charged forward with a roar. Behind them, a flag marked *Mount Heng* whipped in the air.

At the tips of those steel-blue weapons was another flag.

Jin (振).

And hundreds of martial artists sealing off the gorge.

“They’re bastards with neither martial honor nor chivalry. The Mount Heng Sword Sect disappears today!”

“Attack!”

Static crackled.

The view zoomed in through the noise, locking onto two people who stood out beneath the flag of the Jin Family of Taiyuan.

An old man with a long white beard spoke.

“This is going to be a long fight.”

A massive man answered.

“And the last one.”

The old man smiled wide.

“It will be. Without fail.”

And then.

People crashed into people, swords into spears. Countless martial artists collided, and a thick blood-mist settled over the gorge.

Somewhere, a drumbeat announcing the start of battle rolled out.

Boom. Boom. Boom.

* * *

“Hah.”

I sat up, soaked in sweat. Another Murim dream.

Unlike at first, I could remember it clearly even after waking.

*The battle has begun.*

Even after I came back to reality, time kept moving in Murim.

The scenes I had seen might be happening there right now. A great battle with the fate of two massive forces on the line.

*No. There’s one more.*

A third force led by the Head Elder.

Once the fighting hit its climax and both sides had taken heavy losses, that was when they would finally move.

*What about Hyuk Mujin? What happened to the reconnaissance squad?*

If they arrived in time and exposed the betrayal, the worst could still be avoided. Or the opposite had already happened, and everything was already over.

*The Head Elder…….*

An old man who had given me the creeps from the first impression. Who would have thought that so-called elder of the Jin Family of Taiyuan would be plotting something like this?

If the Head Elder became the final victor, it would all be over.

The end of a rebellion always brought a bloody purge.

*Jin Wikyung, Wipeng, Hyuk Mujin, and the reconnaissance squad.*

Plus Han Yeop, too badly injured in his fight with Jopil to march out, and Gong Yacheong and the siblings Socheon and Soyul, still recovering.

Familiar faces appeared and vanished in my mind again and again.

*What were they to me?*

One month in Murim.

To them, I had been a Benefactor, a trusted superior, and a comrade they could turn their backs to. And to someone…

“I’m proud of you.”
“Are you hurt anywhere?”
“Survive, youngest.”

I had been a blood brother, too.

But what had they been to me? NPCs loaded with advanced AI? Or people?

*What were they?*

Another dimension only I could come and go from, and the people left behind there. What was I supposed to do about that?

My eyes drifted to the capsule on their own.

*If I went back…….*

The thought startled me. I was out of my mind.

Go back and do what? It was a great battle with some two thousand martial artists mixed together. Among them were monsters as strong as Jopil, One Question, One Kill—or even stronger.

And I was thinking of going back there?

“You lunatic. You crazy bastard. You’ve completely lost it.”

I was muttering it like a sigh when my phone rang.

Bzzz.

Luxury Freak.

It was Team Leader Choi.

* * *

A large café in the heart of a downtown forest of high-rises.

“Here are the materials you requested.”

Butler Kim held out a thick binder. Even at a glance, it looked like a massive file of more than a hundred pages.

“That’s a lot.”

“I investigated just as thoroughly.”

Choi Minwoo nodded and started flipping through the pages. What he was reading was one person’s life.

Jin Taekyung’s twenty-seven years were packed into those hundred-plus pages.

Birthplace, background, how he had grown up—even account inquiry records provided by the bank. Nothing was missing.

Unusual or suspicious parts had been highlighted in bold, so Choi Minwoo finished the entire file in under thirty minutes.

“What do you think, Butler Kim?”

“He’s clean.”

Butler Kim answered in a definitive tone.

“He isn’t an illegal Awakener, and he didn’t approach you as part of some plan.”

Choi Minwoo nodded. If Butler Kim said so, that was how it was.

He was the one who had spent the past two weeks using every means available to look into everything about Jin Taekyung. Likewise, every page of the hundred-odd-page file on the table would have passed through his hands.

“So this was all a coincidence?”

“For now, yes.”

“Butler Kim.”

“Yes. Please go ahead.”

“Do you know the odds of reawakening?”

“I understand they’re around one percent.”

One in a hundred.

From an ordinary person’s perspective, that might not seem impossibly rare. But those hundred people were not ordinary people. They were Hunters who had already been born through similar odds.

And among them, only the chosen enjoyed the luck of reawakening.

“Then what are the odds that an F-rank Hunter reawakens in one jump as a C-rank Hunter?”

Choi Minwoo did not wait for an answer.

“What about the odds that a C-rank Hunter could clear a Gate of the same rank alone?”

“Alone, it would be impossible. He’d have to be at least B-rank……”

“And yet there’s someone who can.”

“Could it be…?”

“Ten C-rank Gates. Ten D-rank Gates. Across twenty raids in total, all I did was sit with my arms crossed and watch. I never even needed to step in.”

His long fingers tapped the thick binder.

Everything about Jin Taekyung was written inside it, and in another sense, nothing was.

After a moment of silence, Butler Kim spoke.

“I’ll investigate him again.”

“No.”

Choi Minwoo shook his head.

“Keep scratching and you’ll only raise a sore. I intend to keep him close and watch.”

“Do you intend to recruit him into the Guild after all?”

“I should. If something smells fishy, I’ll dig into his background. If it doesn’t……”

Choi Minwoo’s eyes gleamed.

“I’ll make him one of my people. Even if I have to pay him three personal visits.[^1]”

And in the next moment—

Jingle.

As someone came into the café with the doorbell, Choi Minwoo gave a quiet laugh.

Zhuge Liang—or rather, Jin Taekyung.

* * *

A signing bonus of 500 million won.

A fixed monthly salary of 50 million won and a seventy-percent settlement split.

A roughly 132-square-meter officetel[^2] and a sedan came as extras, and the four major social insurances were a given. After reading the contract through, I had exactly one thought.

*This is insane.*

What kind of outrageous terms were these?

They were giving me a home, a car, and more money than I knew what to do with.

The average annual salary of a C-rank Hunter was 200 million won, including fixed pay and raid pay.

And me?

*The signing bonus alone is 500 million.*

This was the kind of contract a B-rank Hunter could get, at minimum.

It also meant my skill was valued that highly. And it was proof I had found an employer with the insight not to judge a Hunter by rank alone.

*And he has the money, too.*

I stared across the table at Team Leader Choi. As always, his expression gave nothing away, and his eyes were deep.

Team Leader Choi spoke without warning.

“This is the third time.”

He had made two offers before. I had turned both down. This was a roundabout way of telling me not to refuse him again.

“I’m sorry about that. There was a minor issue.”

“Have you resolved it?”

“Yes. For now, it seems that way.”

“Then there shouldn’t be any problem now.”

“……Of course.”

Even as I answered, I still had doubts. Was there really no problem now? Was it okay to leave it like this?

*What the hell am I thinking?*

I had to knock this out before my mind wandered.

“I’ll sign.”

I started signing with the fountain pen Team Leader Choi had handed me.

One page, two pages, three……

The contract was five pages long. All I had to do was write the three characters of my name on the last page, and it would be done.

At that moment, the question came back.

*Is this really okay?*

The fountain pen that had been moving without hesitation slowed. One thought caught on the next.

*What if it isn’t? Isn’t this what I wanted?*

It was. This was exactly what I had dreamed of so desperately for seven years.

A massive salary and high social standing.

Becoming a son and older brother they could be proud of, and treating my family to an easy life.

Becoming someone to envy and admire instead of someone to ignore and look down on.

*I can have it all now.*

I could live enjoying every bit of it. Goodbye to my grimy life. Goodbye to that shitty Murim.

Crack.

And goodbye to the fountain pen, too.

I let the strength out of my grip. Ink spilled from the shattered pen and soaked the contract.

“Mr. Jin Taekyung. Let me ask you again.”

Team Leader Choi pulled out a white handkerchief and wiped the ink that had splashed onto his chin.

For all the sudden mess, he looked calm.

“That problem from last time. Have you really resolved it?”

“No.”

Once I said it, I felt a weight lift.

“If it’s something I can help you with……”

“I appreciate it, but I have to handle this myself.”

Team Leader Choi studied me with an odd look, then gave a small laugh.

“I didn’t know a contract could be this hard. I didn’t expect to get turned down three times, either.”

He sounded amused by the situation rather than angry.

“When would be a good time to make the fourth offer?”

He had probably meant it half as a joke, but my answer was serious.

“Tomorrow, at this time, in this place.”

“Tomorrow?”

“Yes. Tomorrow.”

Only one day.

But for me, it would be a month, or maybe several.

Team Leader Choi had no way of knowing that, and he furrowed his brow.

“I don’t much like jokes like that.”

“Neither do I. Not jokes like this.”

He didn’t know what my words meant.

“I’ll be sure to see you.”

That was a vow to myself.

A vow that I would come back alive.

And……

“Tomorrow, you’ll have to raise the contract terms even further.”

I left the café, leaving Team Leader Choi behind with his eyes wide.

* * *

“Phew.”

I drew a deep breath and opened the capsule.

The sunken seat and VR headset made my heart hammer. Even after coming this far, temptation kept lifting its head and whispering.

*Don’t go back.*

*Just forget everything and live content with your reality.*

*Everyone you met in Murim is an NPC, and Murim is nothing more than a game.*

Right. There had been a time I thought that way.

But after thinking it through, I realized I was going back, one way or another.

*I’d already reached my conclusion a long time ago.*

On the night of the blizzard, I had gone back for Gong Yacheong.

I had brought along two young siblings who were nothing but baggage, and instead of using the reconnaissance squad as a shield, I had fought Jopil and barely made it through.

*It probably started then.*

That was when the three letters NPC, lodged in my head, began to fade.

That was when I saw the two-character word for family in Jin Wikyung’s back as he told me to survive and turned away.[^3]

“Fuck, life really is a variety show.”

With a hollow, complaining laugh, I climbed into the capsule. The moment I put on the VR headset, a single line of text appeared in front of me.

Ding.

> **System**
>
> Would you like to connect to Murim?
>
> **Accept** / **Decline**

“Yes.”

My consciousness faded. My vision darkened.

I logged in.

[^1]: “Paying three personal visits” alludes to Liu Bei’s repeated visits to Zhuge Liang in *Romance of the Three Kingdoms* to recruit him as an adviser.
[^2]: An officetel is a Korean mixed-use unit designed for both office and residential use.
[^3]: In Korean writing, each syllable is written as a single character block; the word for “family” consists of two such blocks, contrasting with the three Roman letters in “NPC.”
