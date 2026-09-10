# Checkpoint Review — 55–59

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

# Chapters 55–59

## Plot

Taekyung wakes in Murim after roughly two hours of deathlike sleep and learns that the reconnaissance squad has sent messengers to the Jin Family’s main force. He orders the exhausted squad to reach Eight Spring Gorge before the battle is lost. There, Mount Heng’s larger army is trapped in the Jin Family’s terrain-controlled gorge while hidden cliff archers fire on them. Lee Cheonbaek leads Mount Heng’s core forces in a desperate assault, but the Head Elder overwhelms him with Sword Energy and prepares to kill him.

Taekyung arrives, splits a spear aimed at the Head Elder, and publicly brands him a traitor. The Jin Family’s First, Second, and Third Elders reveal concealed Peak-level abilities and turn against their own side. A signal flare summons the Three Paths Sect, Byeokdo Sect, Gunggwimun, and other Five Gates of Shanxi forces, exposing a decades-old conspiracy. The Head Elder confirms that “they” killed Lee Seogeun but does not identify the accomplice or explain the complete plan.

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

## Durable state

{
  "version": 1,
  "safe_through": 59,
  "continuity_sources": [58, 59],
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
    "Character Synchronization completed in reality and all systems were inherited. Taekyung's current post-allocation state is Level 40, First Rate Martial Artist, 180 Strength, 185 Stamina, 191 Agility, 20 Intelligence, 20 Charm, fifteen years of Internal Energy, and 0 Remaining Points.",
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
    "Sopung Guild’s Guild Master discovers Kim Sangshik filed a false report about Taekyung and expelled him from the Guild, then expels Kim Sangshik and orders Kim Sangho's resignation. The Guild begins gossiping about Taekyung’s reawakening and whereabouts.",
    "Taekyung returns home after months with his C-rank Hunter license and 300 million won. He tells his mother and younger sister Hayeon an edited account of his reawakening and income, then spends freely on clothes and an expensive meal for them at Mirae Department Store.",
    "Hayeon is nineteen and still a high-school senior; she is awake early for the school founding anniversary and resumes her sharp, affectionate sibling banter with Taekyung.",
    "After returning to reality, Taekyung begins having increasingly vivid nightmares of Murim. Sleep Mode restores his physical condition but not his mental stability, and his mistakes and injuries increase during Gate raids. The dreams now show the Mount Heng–Jin Family battle, and he has decided to return.",
    "Taekyung kills a Level 50 Lizardman Chieftain but is injured three times in one day and five times by the fourth day. Team Leader Choi orders him home and asks what is wrong.",
    "Taekyung suspects that Murim is another reality and that the Ark - 2020 capsule may be a Gate to another dimension; he decides to return and successfully reconnects to Murim at the end of Chapter 54. In Chapter 55 he wakes during the Eight Spring Gorge battle and orders the reconnaissance squad to reach the main force; in Chapter 56 he reaches the battlefield and interrupts the Head Elder's attempt to kill Lee Cheonbaek by splitting a spear.",
    "Team Leader Choi privately plans to keep watching Taekyung and recruit him after Butler Kim clears him of being an illegal Awakener or deliberately approaching Choi. Taekyung rejects Choi's latest contract offer—500 million won signing bonus, 50 million won monthly salary, seventy-percent settlement split, officetel, sedan, and social insurance—because he intends to return to Murim, and schedules another meeting.",
    "The Mount Heng–Jin Family battle is underway at Eight Spring Gorge. The Jin Family has the terrain advantage, while Mount Heng's core forces, led by Lee Cheonbaek, launch the decisive assault. The Head Elder fights Lee Cheonbaek, overwhelms him, and prepares to kill him before Taekyung arrives.",
    "The Head Elder tells Jin Wikyung that he, Wikyung, and Wipeng must engage Mount Heng's command while arrows rain from the cliffs. He privately regards Wikyung as capable of raising the family, but his betrayal remains unresolved. In Chapter 56, he reveals through Sound Transmission that “they” killed Lee Seogeun, without explaining the full plan or the accomplice.",
    "Taekyung reaches the Eight Spring Gorge battlefield with the reconnaissance squad, throws a spear at the Head Elder to protect Jin Wikyung, and publicly calls the Head Elder a traitor.",
    "Jin Wikyung recognizes the accusation as the missing explanation around Lee Seogeun's death and orders Wipeng to cut down the First Elder. The First, Second, and Third Elders reveal concealed Peak-level martial arts and turn against the Jin Family command.",
    "The First Elder's signal causes the Three Paths Sect, Byeokdo Sect, Gunggwimun, and other Five Gates of Shanxi forces to attack their supposed allies, exposing a decades-old conspiracy.",
    "The Head Elder keeps Lee Cheonbaek alive but silences and paralyzes him; Taekyung charges the Head Elder with the reconnaissance squad while the battle remains unresolved.",
    "In Chapter 58, the Head Elder uses Sword Energy to overpower Taekyung's Gambler-boosted spear and slices it down to an iron rod. Taekyung mistakenly rescues Lee Cheonbaek instead of Jin Wikyung, retreats with Hyuk Mujin and the reconnaissance squad, and orders an encircling formation while the Head Elder attacks.",
    "In Chapter 59, the Discipline Hall Master's death rallies the Jin Family's senior members, and Mount Heng joins them against the black-clad forces. Wipeng wounds the Third Elder, Jin Wikyung and the surrounding fighters kill the Second Elder, and Wipeng takes the Third Elder's head. The First Elder admits wealth and glory as the stated motive but points Taekyung toward the Head Elder when Taekyung identifies revenge as the deeper motive. Jin Wikyung orders Wipeng and ten senior members to hold the First Elder, expels him from the family, and leads guards toward the Head Elder after realizing Taekyung is in danger. Taekyung and the reconnaissance squad remain engaged with the Head Elder, and the First Elder's fate is unresolved."
  ],
  "open_questions": [
    "The Ark - 2020 capsule's ultimate purpose and route remain unresolved; Taekyung has reconnected to Murim, but whether it can transport him safely and reliably and what will happen after the ongoing battle remain unknown.",
    "The limits of Murim's death and resurrection rules remain unresolved.",
    "The Head Elder's betrayal and the Five Gates conspiracy are exposed, but the identity of his Sound Transmission accomplice, the full purpose of their plan, and the meaning of the signal remain unresolved; the Second and Third Elders are dead, the First Elder has been expelled and left encircled with his fate unresolved, and the Eight Spring Gorge battle continues.",
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

## Chapter artifact 55

# Chapter 55

*This is driving me crazy.*

Hyuk Mujin felt the world go yellow before his eyes.

Assassins disguised as disciples from minor sects. The Head Elder’s betrayal. That alone was enough to make his head feel like it was about to explode, but…

*Why the hell did this guy collapse too?!*

Jin Taekyung had gone down out of nowhere. The reconnaissance squad had taken turns slapping his cheeks and shaking him by the collar, and he still showed no sign of waking.

*He’s definitely still breathing.*

It was enough to make a ghost weep. And with things as they were, Hyuk Mujin—the deputy squad leader—had ended up in charge of this enormous mess.

“You, and you.”

Hyuk picked out two of the reconnaissance squad members still standing there in a daze.

“Return to the main family at once and report this.”

The Head Elder.

He did not know why the family’s senior, a hero of the old Great Faction War, had devised such a dark scheme, or what he hoped to gain from it.

But they had to stop the worst from coming to pass.

“The rest of us move to the main force. Hurry!”

Hyuk hoisted the unconscious Jin Taekyung onto his back.

After running for roughly two hours, the world went yellow before his eyes again—this time for a different reason.

*I’m going to die.*

It had only been a few days since Jopil’s brutal palm strike had left him with internal injuries. He had loudly told Jin Taekyung he was almost fully recovered, but in truth he needed at least two weeks of rest, no arguments.

“Huff… huff.”

He was soaked through, and his legs were shaking.

He would have fallen behind even if he had only been trying to keep up. Carrying the solidly built Jin Taekyung on his back was literally killing him.

*Ah, Mother. Father.*

Now he was even hallucinating his parents—who were alive and well—waving him over. The woman standing beside them was a face he often saw at the temple hall.

*Guanyin Bodhisattva?*

“Child. You’ve suffered enough. You may rest now.”

Her benevolent smile slowly eased Hyuk’s heart.

*Yeah. I’ve done enough. The squad leader collapses at the critical moment, and these bastards won’t even offer to carry him for me, whether I drop dead or not.*

*Fuck it. Whatever.*

Hyuk was just about to let go when—

“Whew… haaah.”

Warm breath slipped into his ear. He knew who it was without turning around. Tears of relief stung Hyuk’s eyes.

“Squad Leader!”

Jin Taekyung grinned and whispered,

“Candy in your ear.”[^1]

* * *

Clang! Clang!

“Kill them! Kill them!”

“Graaah!”

Blood and screams burst out on every side. A blood-soaked martial artist crawled on all fours between the corpses.

His still-youthful face was stained with pain and terror.

“Hnnh… hhhk…”

He tried to hold it back, but the crying kept breaking free. He had spent ten years grinding through martial arts with grim determination, and it had all been useless on a battlefield spraying blood.

The senior he had counted on was dead. So was the comrade who had been like a brother. Weapons poured in from every direction, splitting open bellies and hacking limbs apart.

“Mother… Mother…”

He called for her without end, and then his face went stiff.

Shunk—!

A spearhead had already sprouted from his chest.

His eyes flew wide for an instant, then the light went out of them. A wandering martial artist with a bandit’s beard pulled his rusty spear free and grinned.

“What’s a brat doing here?”

But even a wandering martial artist who had survived countless brushes with death could not dodge the blade that came flying at him a moment later.

Slice—

A silver line flashed, and the wandering martial artist’s head shot into the air.

A wandering martial artist killed a martial artist. Another martial artist killed the wandering martial artist.

Nameless men killed and died on every side, over and over.

That was what a battlefield was.

*Yes. This was what it was like.*

The Head Elder looked out over the battlefield, his face steeped in memory.

Eight Spring Gorge. A battleground that had occupied a single line in the history of the Great Faction War, decades ago. How many had died in that narrow gorge?

*I was young then, too.*

His body had been strong, and his heart had burned hot. It had been a time when that embarrassing character—chivalry—had still felt enormous.

But the Great Faction War had changed the Head Elder. He had grown tired of the endless fighting, and afraid of death.

*What good is a chivalrous warrior? Die, and you’re nothing but a ghost.*

That had been a sliver of enlightenment. In the end he had survived and become a hero, and after a long stretch of endurance he had reached this place.

Now it was time to reap the fruit.

The Head Elder turned his cunning old eyes on the man standing beside him.

*What a waste. Such a waste.*

Jin Wikyung was a remarkable talent. He was young, his martial arts were considerable, and above all he had the dignity and judgment a leader needed. He sometimes let himself be bound by sentiment, but perhaps because of that, he was deeply respected within the family.

*He’s more than capable of raising the family.*

If Jin Wikyung became the Family Head, and if his two younger brothers—each already distinguishing himself—stood firmly behind him…

The Head Elder caught himself and let out a short laugh.

What a bizarre thing to be thinking, this far along. Jin Taekyung would already have died and become a lonely ghost, at that.

“I’ve grown old.”

Jin Wikyung reacted to the quiet mutter.

“Did you say something?”

“Nothing of importance. Old men talk to themselves more. More to the point, how does it look to you, Lesser Family Head?”

“The battle is going in our favor, but…”

Jin Wikyung’s expression darkened slightly. They held the advantage in troop quality and terrain, but the casualties kept mounting.

There was no way he could watch members of his family die and feel at ease.

“Lesser Family Head. I understand how you feel, but do not act rashly.”

The Head Elder’s warning was stern.

“A leader must know when to step forward. The longer the battle drags on, the more impatient they become. That is the moment we have to seize.”

“The Mount Heng Sword Sect will soon throw its full strength at us.”

“They’ll put their Peak masters at the front. Their Sect Leader, Lee Cheonbaek, may even come himself.”

“Then everything will be decided.”

The Head Elder nodded.

“If you, I, and Wipeng hold off the enemy command, and arrows rain down from the cliffs, their morale will hit rock bottom.”

“It’s a shame we can’t use a fire attack. I resent the heavens.”

The narrow terrain of Eight Spring Gorge was perfect for fire, but the heavy snowfall from several days ago had left snowdrifts everywhere.

Even if the heavens had taken Jin Wikyung’s side, though, what he was hoping for would never have happened.

The men drawing their bows on the cliffs would obey the Head Elder.

“I resent the heavens as well.”

The Head Elder meant it.

The years of waiting had been too long. He resented the destiny that had only now arrived.

* * *

“Candy in your ear.”

“Squad Leader!”

“Was it sweet as a dream?”

“…Are you insane?”

The sight of Hyuk Mujin’s ugly face sent a rush of relief through me. The other reconnaissance squad members crowding in at the news that I was awake were no different.

“Squad Leader’s awake!”

“What happened? Are you all right?”

“Wasn’t he dead?”

I’d have to deal with the bastard who had just said that later. I memorized his face and name, then grinned at everyone.

“Been a while. You guys been well?”

“Huh?”

“What’s that supposed to mean?”

“Did he hit his head?”

“His head—check his head!”

Exactly the reaction I’d expected.

But it was also a greeting I’d genuinely wanted to give them at least once.

…Not that they didn’t treat me like a lunatic afterward.

“Anyway, that’s enough greeting. How long was I out?”

Hyuk dropped onto the ground with a thud and answered.

“Definitely more than an hour, and a little under two.”

I’d spent two weeks in reality, so the timing roughly lined up. I nodded and moved on.

“Was I breathing?”

“Why are you asking that all of a sudden? Seriously.”

“No time. Answer.”

“You were breathing, that’s why you woke up. Otherwise you’d be dead.”

Fair enough.

Apparently, logging in or logging out put the other side into a deathlike sleep.

*If I’d logged out before dealing with the assassins, there wouldn’t have been a body to come back to.*

I’d think about that later.

There was a more urgent problem.

“The main force?”

“We were already heading that way. We split two men off and sent them back to the family.”

“Good. How much farther?”

“At least another two hours.”

“Two hours…”

“Uh, Squad Leader. I’m sorry to say this, but… I think we have to consider the worst case.”

Hyuk Mujin and every member of the reconnaissance squad clamped their mouths shut. Nobody had to ask what the worst case meant.

*I’ve thought about it too.*

From what Gwak Jun had said right before he died, this betrayal had been planned down to the last detail for a long time.

But the plan had exactly one error.

*Me.*

The Head Elder had underestimated me.

No—maybe, in another way, he’d overestimated me. He’d sent dozens of First Rate masters just to kill me.

Even that hadn’t been enough. I had survived.

*He made a mistake.*

On top of that, when Gwak Jun first showed his true colors, he’d said they had to start moving soon if they wanted to make it on time.

Which meant…

“It’s not too late.”

I met each squad member’s eyes and spoke firmly.

“Don’t think about the worst case. I’ll change that outcome, no matter what it takes.”

“Squad Leader…”

“So, Mujin.”

I gave Hyuk’s choked-up face a good-natured smile.

“Get up. Now.”

“I’m dying here.”

“Want to get beaten to death instead?”

“…”

“Run even one more step in the time we’ve got. Don’t you know marathon spirit?”

“I don’t.”

Ah. Right. This was Murim.

“Anyway, get up. Another hour will do it.”

Hyuk grabbed his shaking legs and pushed himself up, then cocked his head.

“An hour?”

“Yeah. An hour.”

“I already told you. Even at full speed, it’s two hours.”

“Exactly. An hour.”

“What are you even saying…”

“Mujin.”

“Yes?”

Hyuk blinked at me, as simple as an ox. I smiled even brighter.

“You ever heard of grit?”

Two hours or four, I didn’t care.

We were getting there in an hour. Period.

“Run like hell. That’ll do it.”

“Huk.”

Every face in the reconnaissance squad went deathly pale.

* * *

“We’ve been blocked.”

“Casualties are heavy. Sect Leader, please take action.”

Even as the reports kept coming, Blood Wolf Sword Lee Cheonbaek, Sect Leader of the Mount Heng Sword Sect, did not open his eyes.

*I was too hasty.*

The war had started in a rush, and the preparations had been just as thin. Provisions were burning down fast, morale was dropping, and deserters were popping up one after another.

*They read us completely.*

Rage at losing his son and impatience with the situation had clouded his judgment. He had ignored his subordinates’ advice and taken the fastest route he could find.

And that was how he had run into the Jin Family of Taiyuan in a narrow gorge whose very name was unfamiliar: Eight Spring Gorge.

“Sect Leader!”

At his subordinate’s shout, Lee Cheonbaek slowly opened his eyes.

The fearsome vision of a Peak master pierced the battlefield.

“Gaaah!”

“Wipe them out! They’re nothing but rabble!”

Well over a thousand of his own men were jammed at the narrow mouth and couldn’t advance. The wandering martial artists and mounted bandits he’d put at the front had numbers, but man for man they were worse than even the Jin Family’s rank-and-file.

*Sword fodder, at best.*

Just as he was clicking his tongue, several dozen wandering martial artists suddenly started peeling off the front line. The middle-aged wanderer at their head bellowed until his throat tore.

“This is a dog’s death! Brothers of the Blood Rain Group, fall back!”

Those became the middle-aged wandering martial artist’s last words.

Whoosh—

A light breeze. The wandering martial artist felt nothing else.

He did not know that Blood Wolf Sword Lee Cheonbaek had already brushed past him. He did not know that the wandering martial artists under him had frozen in terror.

He only thought, suddenly, that his neck was hot.

“Uh…”

His cleanly severed head dropped with a dull thunk. The headless body staggered a few more steps, then went down like a rotten old tree.

“Blood Rain Group, was it?”

Lee Cheonbaek pointed his sword at the frozen wanderers. Not a drop of blood stained the blade.

“Go back.”

A Peak master’s killing intent shot into them like a blade. The wandering martial artists charged toward the front even faster than they had come.

They had decided that fighting at the front beat throwing themselves at the Peak master in front of them.

“Rat bastards.”

Lee Cheonbaek went after them. His burning gaze was aimed somewhere ahead, where the Jin Family of Taiyuan’s command had to be.

“The Sect Leader is taking the lead!”

“Everyone, charge! Wipe out the Jin Family of Taiyuan!”

With Lee Cheonbaek stepping forward, the Mount Heng Sword Sect’s core forces followed.

Three Peak masters and dozens of First Rate masters crashed toward the front.

[^1]: A Korean joke-whisper: mock ASMR, promising something sweet right in your ear.
## Chapter artifact 56

# Chapter 56

The Head Elder was the first to notice Lee Cheonbaek’s arrival.

*The head himself has entered the fray.*

The fierce wave of qi blasting across the gorge, and the killing intent rolling with it, made that obvious even without seeing him.

Sure enough—

“You bastards!”

Lee Cheonbaek appeared with a thunderous roar. His half-gray hair whipped around like a mane, and his eyes burned red.

The Mount Heng Sword Sect’s core forces arrived on his heels. First Rate martial artists, and three Peak masters!

“Wipe out those Jin Family of Taiyuan bastards!”

“The Sect Leader is here! The Sect Leader has come!”

“Waaaah!”

The cheers rekindled the fighting spirit that had begun to fade. Lee Cheonbaek surged forward along the path that had opened in an instant.

“Kill those treacherous Jin Family of Taiyuan bastards!”

Jin Wikyung was not the kind of man to stand by and watch.

“The time has come.”

The Head Elder answered.

“I agree.”

In truth, he had not welcomed Lee Cheonbaek’s arrival. A certain amount of attrition would have made the cleanup easier.

But the losses on both sides—the Jin Family of Taiyuan and the Mount Heng Sword Sect—were still nothing to speak of.

*It doesn’t matter. They’ll be making their move anyway.*

The two great powers claimed to be the rulers of Shanxi, but compared to *them*, they were insignificant.

Even in its former heyday, the Jin Family of Taiyuan had been treated as nothing more than a martial family from the frontier. How could it possibly stand against them?

*A mere martial family…*

The Head Elder swallowed a bitter smile and drew his sword.

Shing.

For many years he had carried two swords. One at his chest, the other at his waist.

There was no need for more words.

“I’ll handle Lee Cheonbaek.”

“Please do.”

Who was Blood Wolf Sword Lee Cheonbaek? The man who had founded the Mount Heng Sword Sect with nothing but a single sword, and who now meant to become the ruler of an entire city. Enemy or not, there was no denying he was a Peak martial artist of the highest caliber.

*I want to fight him.*

But Jin Wikyung forced down the heat in his blood.

This was a battle with the family’s fate at stake. Competitive spirit had no place here.

“Wipeng.”

“Yes.”

Wipeng had already drawn his sharp, narrow blade and taken his place at Jin Wikyung’s side.

“You and I will handle the rest.”

“As you command.”

There was not a trace of hesitation in the answer. Jin Wikyung smiled faintly and drew his own sword—the family’s treasured blade, passed down through generations of the Jin Family of Taiyuan.

It was the only thing left behind by the father who had vanished one day without a trace.

*I’m going to travel around the Central Plains for a while.*

*Use this in the meantime.*

Remembering the letter that had been stuffed carelessly into the scabbard, Jin Wikyung felt his blood boil all over again.

*Travel around the Central Plains, my ass. You spent your whole life having fun.*

He didn’t even know where that so-called Family Head was, or what he was doing. And his second brother, thousands of li away, had probably only just received the letter.

*I have to protect them.*

Martial artists, maids, servants, children.

Jin Wikyung was the Family Head of the Jin Family of Taiyuan now. No one else.

Their deaths and their survival were his to carry, and his alone.

*We will win.*

Jin Wikyung’s eyes flared wide. Sword raised, an Azure Dragon’s Roar burst from his mouth.

“Don’t let a single one of them live!”

Whoosh, whoosh, whoosh!

The Jin Family’s masters kicked off the ground and leaped into the air. Taking that as the signal, a single fire arrow rose high behind them.

That was when dozens of figures stood up along the cliffs.

“Fire!”

Beneath arrows pouring down like a sudden rain, the fight between the masters who would decide the course of the battle began.

* * *

Blood Wolf Sword Lee Cheonbaek was a born martial artist.

With innate talent for martial arts and beastlike instincts, he had cut down his enemies and realized his ambitions one after another.

He had founded the Mount Heng Sword Sect and grown its strength by absorbing the surrounding factions one by one. His aim was to lay the foundation for a prestigious house that would one day be recognized even in the Central Plains.

*Sect Leader! The Young Master…*

Then, one day, his second son came home a corpse.

It had not been a fair duel. Deadly poison had taken him, and he had died with blood pouring from all seven orifices.

Lee Cheonbaek swore an oath.

He would kill and burn everything connected to the Jin Family of Taiyuan.

And then Jin Wikyung appeared before his eyes.

Lee Cheonbaek’s eyes blazed.

“You bastard—!”

He charged like a beast. The blade, holding sixty years of internal energy, shone milky white.

With this much power, it could cut through any armor, any divine weapon.

*That bastard dies here!*

Just as Lee Cheonbaek, sure of it, was about to swing—

“Oho. Sword Energy?”

A low voice, from behind him.

Lee Cheonbaek’s heart sank.

*How?*

To give up his back so cheaply. His reaction was lightning-fast. He drove the sword backward in a reverse grip.

Whoosh.

The blade stabbed empty air, and that bought him time. Only then could he see his opponent’s face.

A beard hanging down to his chest. A relaxed smile at the corners of his mouth.

A white-haired old man.

Lee Cheonbaek knew him at once.

“Blade of Flowers?”

The Head Elder nodded.

“I haven’t heard that name in a long time. Then you must be Lee Cheonbaek.”

“That’s right.”

Even as he answered, a chill ran down Lee Cheonbaek’s spine.

He didn’t dare look for Jin Wikyung, or check how the battle was going. Take his eyes off the old man, and he felt his head would come off on the spot.

*Coincidence? No.*

It was true that seeing Jin Wikyung had agitated him past reason. It was true that he had been impatient.

But Lee Cheonbaek was a Peak master.

A Peak master who had reached the realm of Sword Energy Frost Blade.

The answer was already clear.

*A master!*

Whether in one form or half a form, the old man in front of him was a master a league above Lee Cheonbaek.

Lee Cheonbaek tightened his grip on his beloved sword.

“I’ve heard much of your reputation.”

“Reputation? I’m nothing more than an old man in the back room.”

“Then why leave the back room?”

“You’re still a young fellow, so there’s a lot you don’t know. The older you get, the more you have to get moving now and then.”

Lee Cheonbaek ground his teeth at the Head Elder’s sly manner.

*Damn old man.*

He had been watching the Jin Family of Taiyuan for a long time.

He knew there was a faction centered on the Head Elder that opposed the Family Head. He had even privately hoped the family would split from within.

But things had gone the opposite of what he had expected.

*So when an outside enemy invades, they unite as one?*

Lee Cheonbaek stared at the Head Elder with heavy eyes, then opened his mouth.

“How strong are you?”

“As strong as you believe me to be.”

“Word games.”

“When I was called Blade of Flowers, I was thirty.”

At thirty, the Head Elder had already been a Peak martial artist.

Now he was a man of seventy. How had his martial arts changed since then?

After a moment’s thought, Lee Cheonbaek let out a wry laugh.

*I’m getting old, too.*

Blood Wolf Sword.

In his youth, Lee Cheonbaek had been unstoppable. Without an exceptional martial art or a respectable master, he had carved his way through everything on his own.

Even against an opponent a level above him, he never backed down. He charged like a wolf and tore out their throats.

*I lived half my life that way…*

At some point, people had started calling him Sect Leader instead of Blood Wolf Sword.

Blood relatives, subordinates, wealth.

The things he had to protect had piled up like a mountain.

Time spent training shrank; time spent on affairs grew. When it was time to act, he started thinking instead.

Just as he was now.

“Why are you laughing?”

Lee Cheonbaek answered the Head Elder’s question.

“I’m laughing because I find myself pathetic.”

“You’re afraid of me.”

Lee Cheonbaek nodded in silence.

“Were you afraid of death?”

“For a very brief moment.”

“And now?”

“I’m going to kill you.”

“Someone of your level won’t manage it.”

“You have to measure them to know which is longer, don’t you?”

“That’s what the short ones always say. They never realize that even after you measure, the result doesn’t change.”

“Your tongue is sharp.”

“Is it only my tongue?”

The Head Elder lowered his sword.

It looked like an ordinary blue-steel sword, but the moment it entered his hand, it began to give off a vicious killing edge.

“Come at me first.”

Lee Cheonbaek did not refuse.

The blade, having drawn in sixty years of internal energy, raised a shimmering haze of light.

The realm of Sword Energy Frost Blade—a realm countless martial artists dreamed of reaching.

Tssss.

The moment the Sword Energy rose three inches—about ten centimeters—Lee Cheonbaek’s body shot forward.

A unique martial art, perfected through countless real battles, unfolded from his fingertips.

Whoosh! Whoosh-whoosh-whoosh!

Boom!

Sword Energy hacked wildly in every direction. Screams burst from between the mounds of earth that erupted in an instant.

“Graaagh!”

They were the cries of martial artists caught in the gap.

Every voice was a young man’s.

A red warning light went on in Lee Cheonbaek’s mind.

*Behind!*

He spun and swung at the same time.

He saw the white beard fluttering in the wind.

And the sword in the old man’s hand.

Boom!

*Kh.*

Lee Cheonbaek fell back in a daze amid the thunderous crash. He was not even given time to feel the pain in his wrist.

Boom! Boom! Boom!

Every time the two swords met, thunder and lightning rolled.

Sword Energy poured out in a continuous stream, smashing the ground and tearing the wind.

Whoosh!

“What in the world is that…?”

The martial artists of both sides forgot they were fighting. They could only stare, slack-faced, at this staggering life-and-death duel.

In that moment, every one of them was thinking the same thing.

*Are those two really human beings like us?*

The ceaseless thunder. A feast of Sword Energy so dazzling it left them spellbound just to watch.

The movements of the two men at its center were faster and stronger than anyone they had ever seen.

Someone muttered, almost a groan.

“So this is a Peak master…”

To their eyes, it was a fight where either outcome would have made sense.

But the superiority in strength was obvious.

After some three hundred exchanges, the Head Elder’s sword changed.

Whoosh—slice!

“Ghk.”

Lee Cheonbaek bit down on his lip.

Blood streamed from the forearm the Head Elder’s sword had raked.

The strength drained from the hand on his sword.

*Of all things.*

He shifted the sword to his other hand at once, but he was a right-handed swordsman by nature.

Even at full power he would have been hard-pressed. Now that the arm he used to wield a sword was injured, the outcome was all but decided.

Boom!

Crack.

A single blow snapped his wrist.

His Sword Energy, weakened by the severe drain on his internal energy, could no longer stand against the Head Elder.

But Lee Cheonbaek did not give up.

*Not yet. It isn’t over yet.*

He had taken worse injuries than this, plenty of times.

Using the strength in his arm, his waist, his legs, Lee Cheonbaek swung his sword.

No—he tried to.

Slash!

This time, it was the knee.

The tendons had been cut, and the knee buckled slowly, with no regard for Lee Cheonbaek’s will.

His sword carved uselessly through empty air.

Shhk. Shhk-shhk-shhk.

His side. His shoulder. His chest.

Lightning stabbed and sliced through his whole body. The fierce Sword Energy did more than cut flesh and bone—it churned his insides.

“Bleeegh!”

Lee Cheonbaek vomited blood mixed with pieces of organ and looked up at the Head Elder through clouded eyes.

The old man’s face was impassive.

No joy at having put his opponent down. No delight that the war was ending.

To him, all of this was simply the natural result.

“Cough… So Shanxi’s Number One was standing right in front of me.”

“If you’re not Number One Under Heaven, you’re nothing more than a martial brute from the frontier. Neither you nor I have that kind of capacity.”

“Tell me what you want. I’ll give you my neck. I’ll make my men surrender, and I’ll seal the sect for ten years—or a hundred. So…”

“Impossible. What I want is annihilation. Complete annihilation, without a single blade of grass left standing.”

“Why…!”

“Don’t ask me that. If you had won, it would have been this family facing annihilation.”

Lee Cheonbaek glared at the Head Elder with bloodshot eyes.

He wanted to snap that wrinkled neck then and there.

But in his condition, all a man with wounds like his could do was wring out a voice.

“Jin Family of Taiyuan. You started this, didn’t you? You killed that boy—my son!”

“Ah, Lee Seogeun. That’s right. That child was where it began.”

The Head Elder wore a sardonic smile.

Even the master of the Mount Heng Sword Sect, one of the two powers splitting Shanxi between them, had failed to notice *their* intervention.

Not even with death at his doorstep.

—When you meet King Yama, ask him. Ask who killed Lee Seogeun.

The Sound Transmission burrowing into his ear made Lee Cheonbaek’s eyes flare wide.

“What does that mean…?”

It had been a thoroughly impulsive act.

Perhaps pity for Lee Cheonbaek, who was about to die knowing nothing.

Or perhaps nothing more than an old man’s whim.

—Fare for the road to the afterlife. Think it over on the long journey.

The Head Elder raised his sword.

The sunset beyond the winter ridge shattered into fragments along the blade.

*With this…*

With the death of the giant called Lee Cheonbaek, the Mount Heng Sword Sect would collapse.

Those who resisted would die. Those who surrendered would be taken.

One war would end like that…

And a new war would begin, at the very moment everyone was drunk on victory.

*It’s over.*

At last, the Head Elder’s sword moved.

Screeeech—!

A sharp sound tore the air.

Sensing the end, Lee Cheonbaek closed his eyes.

The blade, wrapped in blue Sword Energy, traced a beautiful line.

Slice.

But the tearing sound that had come first, and the direction of the sword, were both beyond Lee Cheonbaek’s expectations.

The Head Elder split a spear that came flying at his back out of nowhere, cutting it apart with Sword Energy.

An enraged roar burst from his mouth.

“Who the hell are you!”

The answer came the next instant.

“It’s me, you fucking bastard!”

The Head Elder saw the face of a young man standing tall on a low hill, and groaned.

“Jin Taekyung?”
## Chapter artifact 57

# Chapter 57

“Faster! Faster!”

“Huff… huff!”

We ran like mad. Hyuk Mujin was panting like he was about to drop dead, but he didn’t. Whenever his steps started to slow, I put the spearhead to his back, and he might as well have been Red Hare.[^1]

Then, at some point, the sounds started to reach us.

Someone’s screams. Steel ringing on steel…

Good. The battle wasn’t over yet.

Relief hit me, and my heart hammered at the same time. The fighting was still going on, but I still hadn’t confirmed whether Jin Wikyung was alive or dead.

What if he died because we were a minute—or even a second—too late?

*If that happens…*

Crack.

I tightened my grip on the spear without realizing it. I drew internal energy up from my dantian and sent it flowing through both legs.

“S-Squad Leader!”

I kept running, leaving the reconnaissance squad’s voices fading behind me. The countless tracks the main force had left, and the growing noise of the battlefield, were my landmarks.

*Stay alive. Stay alive. Please, stay—*

Ah. I could see it at last.

Below a low hill, not even two hundred meters away, countless martial artists were locked in a bloodbath, killing and being killed.

“Die!”

“Gaaah!”

Corpses and blood—and more corpses, more blood!

The sight in front of me was so brutal I was momentarily speechless.

If I hadn’t built up a tolerance from my life as a Hunter, I probably wouldn’t have been able to pull myself out of the shock for a long time.

*Jin Wikyung! Where is Jin Wikyung?*

But someone else caught my eye first.

White hair you could pick out at a glance even from far away.

*The Head Elder!*

He stood in front of someone, sword in hand.

Hidden behind the Head Elder’s back, the kneeling man was hard to see, but he was huge, and he had a sword in his hand.

*A big guy with a sword?*

Only one person came to mind.

Jin Wikyung. If I wanted to save him, I had to move now.

*Open Inventory.*

The Inventory I used in Murim was packed with all kinds of things.

This spear was one of them. Its shaft was wood, its head steel.

*Equip Weapon.*

I took the spear and stepped back a few paces.

Two hundred meters. Impossibly far. Even more so if I was trying to hit someone with a thrown spear.

But I had to do it.

*It’s not like I can’t.*

Strength, Stamina, Agility.

I pushed the stats I’d built up going back and forth between Murim and reality as far as they would go.

With internal energy in my arm, I could send the spear farther and harder.

“Hup.”

I held my breath and stepped in. The first step was slow. The last was heavy. I whipped my arm, and the spear shot from my fingertips.

Fwoooosh!

The throw was faster and more accurate than I’d expected. It looked like it would punch straight through the Head Elder’s back.

But then…

Shhk.

*What the hell was that?*

A flash of blue light, and the spear split in two. From the spearhead at the very top all the way to the end, a clean cut.

For a moment I couldn’t tell whether I’d thrown a spear or a birthday cake.

“Who the hell are you?”

The old man had quite a set of lungs.

“It’s me, you son of a bitch!”

It was probably a curse the Head Elder had never heard in his life.

On top of that, he and I were members of the same family in Murim. If you went by the genealogy, the generation gap between us was about an archaeopteryx and a chick.

That alone was plenty of reason to be stunned. But I still had one finishing blow left.

“The Head Elder is—!”

My voice, loaded with internal energy, thundered across the battlefield. Even I was surprised by how loud it was. I could only imagine what it sounded like to everyone else.

I stared at his frozen, cold face in the distance and shouted with everything I had.

“A traitor!”

* * *

Jin Wikyung heard the voice right after bringing down all three Peak masters of the Mount Heng Sword Sect.

No—not only him. Everyone on the battlefield heard that shout.

“Who the hell are you?”

“It’s me, you son of a bitch!”

Cursing?

That was common enough on a battlefield. But if the target of the abuse was the Head Elder, and the young man who had appeared out of nowhere to dump a double helping of it was Jin Taekyung, then it was a completely different matter.

“Isn’t that… isn’t that the Third Young Master?”

“What? That’s Jin Taekyung? But why?”

“What’s going on?”

Jin Wikyung was thinking the same thing.

*What in the world is happening?*

His youngest brother, who was supposed to be in the rear, had appeared on the battlefield. That alone was shocking enough, and on top of it he had hurled language unfit to repeat at one of the family’s elders.

Wipeng, standing beside him, muttered,

“He’s completely lost it.”

Jin Wikyung was just about to nod without realizing it when—

“The Head Elder is—!”

An even bigger bomb dropped.

“A traitor!”

The battlefield sank into an icy silence. Even the occasional clash of weapons cut off cold.

Everyone stared blankly at Jin Taekyung.

*What kind of bullshit is this?*

*Betrayal? The Head Elder?*

*Is he drunk? The Third Young Master’s old habits must be coming back.*

Needless to say, the martial artists of the Jin Family of Taiyuan thought so. The martial artists of the Mount Heng Sword Sect were much the same.

Even the senior members who had recently begun to look favorably on Jin Taekyung stood there with their mouths hanging open.

“What a madman.”

“Does he even know who the old master is?”

If they had to name the person who had contributed most to this war, it was, without question, the Head Elder.

He had helped Jin Wikyung gather the family’s strength, and in today’s battle he had defeated Lee Cheonbaek.

Even setting aside his merits in this war, Jin Taekyung’s words could only sound like nonsense.

Who was the Head Elder?

He was a master of the previous generation, famous even in the Central Plains as the Blade of Flowers, a symbol of righteousness who had struck down countless demonic masters during the Great Faction War.

Every martial artist in Shanxi held him in some degree of respect.

“That man? A son of a bitch? A traitor?”

“Good heavens. That boy is smearing shit on three hundred years of the Jin Family of Taiyuan’s history.”

The Jin Family of Taiyuan, the Mount Heng Sword Sect—everyone here seemed to share the same thought. But there was at least one exception.

*The Head Elder. Betrayal.*

The instant he heard his youngest brother’s words, Jin Wikyung felt the blood in his entire body run cold. It was a sense of wrongness, finally showing its true shape.

*Lee Seogeun’s death was where it began.*

He had died poisoned by a lethal toxin. The Mount Heng Sword Sect had named the Jin Family of Taiyuan as the culprit, and that had been the spark that started the war.

But the most important question had been left unanswered.

*Who was the murderer?*

Even now, with the war nearing its end, the killer hiding behind it all had never been identified. No—because the war was nearing its end, no one cared about the murderer’s identity anymore.

Survival of the fittest. The strong would live and take everything.

*This war… was wrong from the very beginning.*

Lee Seogeun’s death.

The unnaturally rapid spread of the rumors.

The Mount Heng Sword Sect had declared war, and the Jin Family of Taiyuan had answered. That was how the real fighting had begun.

*And the Head Elder had been there.*

The Head Elder, who had never left seclusion, had appeared immediately after news of Lee Seogeun’s poisoning reached the family. His role within the family had been enormous.

A respected martial artist. One of the family’s senior elders.

If the Head Elder had not cooperated so actively, the Jin Family of Taiyuan might have split in two.

*We were able to come this far because of his help.*

Jin Wikyung thought the opposite.

*We were able to come this far because this was what the Head Elder wanted.*

A span too short even to call an instant. When Jin Wikyung finished the thought, he opened his mouth.

“Wipeng.”

“Your orders.”

“Cut down the First Elder.”

“What?”

The stooped, emaciated old man—the First Elder—opened his eyes wide.

The senior members standing nearby were just as shocked.

“L-Lesser Family Head!”

“What in the world…!”

But Wipeng did not hesitate. Before anyone knew it, his sword was flying toward the First Elder’s chest.

Clang-clang-clang!

Two swords cut in out of nowhere and knocked Wipeng’s blade aside.

Two fat, exceptionally tall old men.

They were the Second and Third Elders, who, together with the First Elder, styled themselves the Head Elder’s hands and feet.

Wipeng’s brow twitched when he saw the faint Sword Energy gathered on their blades.

“You’ve been hiding your martial arts.”

The First Elder answered with a single punch.

Boom!

With internal energy as deep as the years he had lived, he sent Wipeng flying, then straightened his back.

The field froze at the appearance of yet another Peak master who had spent his entire life hidden in the Head Elder’s shadow.

“First Elder, what… what is this?”

“Then could it be…!”

*Betrayal.* The word stamped itself clearly into everyone’s minds.

“That’s impossible!”

The one who shouted was the White Tiger Hall Leader. If the Elders were the Head Elder’s hands and feet, he had thoroughly served as the First Elder’s.

“Elder, Lesser Family Head. It seems there has been some misunderstanding…”

But he could not finish. At a jerk of the First Elder’s chin, the Second Elder moved with blinding speed and cut the White Tiger Hall Leader’s throat.

Shhk. Thud.

Jin Wikyung’s gaze met the First Elder’s in the air between them.

“You recruited the White Tiger Hall Leader too?”

“He was a noisy man. That was all. The others were the same.”

Jin Wikyung’s guess had been half right and half wrong.

The Elders had betrayed them, but the senior members who belonged to the Elders’ faction had not.

“Then why… Ah!”

“Sharp. I’ll give you that.”

The First Elder pulled a dark, grimy bamboo tube from inside his robes. Only a little of the fuse was left, and it was already burning down.

“Could we tell important secrets to men like that? Even just throwing the inside into chaos had already served its purpose. Things were easier if they didn’t know what was happening outside.”

Jin Wikyung shouted like a scream.

“Stop him!”

“You’re too late.”

The First Elder was right. The instant the fuse burned to its end, something burst, and a red flame shot high into the sky.

Fwish—boom!

It was a signal.

The martial artists of the small and mid-sized sects known as the Five Gates of Shanxi—the Three Paths Sect, a union of three sects; the Tao-centered Byeokdo Sect; and Gunggwimun, which had been pouring arrows from the cliffs without pause—turned in an instant.

“Kill everyone in your path!”

“No exceptions! Sweep them all away!”

They were no longer the clumsy third-rate martial artists they had seemed to be. Killing intent flowed from their eyes, and their sword paths were sharp.

*This wasn’t something they prepared overnight.*

Jin Wikyung’s face hardened.

* * *

Boom!

The Head Elder looked up at the sky. Before the red flame had even faded, a massive roar erupted from every direction.

*Too fast. Far too fast.*

The signal was supposed to go up only after the Mount Heng Sword Sect had been annihilated. The Five Gates of Shanxi were a blade prepared over decades. It had to be swung once, and finish everything like a bolt of lightning.

*Everything has its flow.*

The plan, which had been running without a hitch, had begun to go off course. As the Head Elder smiled bitterly, a voice slipped into his ear.

“So… it was you.”

Lee Cheonbaek. His voice was faint, but his eyes burned more fiercely than ever.

“You still have the strength to talk?”

“I’ll tear you to pieces alive and kill you.”

But no sooner had he finished speaking than blood poured from his mouth. The Head Elder pressed one of his acupoints and murmured,

“That would be inconvenient just yet. You still have something to do.”

Lee Cheonbaek despaired.

They had taken heavy losses, but hundreds of Mount Heng Sword Sect martial artists still remained. At this point, with even the leadership annihilated, if their Sect Leader were taken prisoner…

*Kill me instead!*

The anguished cry never left his mouth. The Head Elder pressed the Mute Acupoint, taking his voice. Then his hand brushed the Paralysis Acupoint, and Lee Cheonbaek’s body went rigid.

He had become a living corpse with his eyes still open.

“You bastard! Get your hands off him!”

At the same time, the air split with a shriek.

Fwoooosh!

The Head Elder did not panic. He swept his sword up from below. Beyond the spear splitting in two along the Sword Energy, Jin Taekyung was charging at terrifying speed.

“Aaaaaah!”

“Squad Leader! Please slow down a little!”

Together with a dozen or so riffraff who had appeared from who knew where.

[^1]: Red Hare is the legendary warhorse of Lü Bu in *Romance of the Three Kingdoms*.
## Chapter artifact 58

# Chapter 58

The battlefield descended into chaos. At the signal, two hundred martial artists suddenly turned and swarmed in every direction like a pack of wolves.

“Kill them all!”

“Aaaaargh!”

They weren’t quite on the level of Gwak Jun and the assassins we’d fought earlier, but a honed-blade aura still poured off them.

The Jin Family of Taiyuan and the Mount Heng Sword Sect. If both factions’ martial artists joined forces, we’d have a real shot—but right now, that looked difficult.

*This is bad.*

At worst, I might have to pull Jin Wikyung out and run.

I was thinking that when the reconnaissance squad arrived behind me, breathing hard.

“Squad Leader, maybe we can—huff!”

The moment they saw what was happening in front of them, their eyes all popped wide. Hyuk Mujin, who came crawling up behind them, gaped as well.

“Bweeegh!”

“…So that was it.”

It must have been rough. After a fast, heavy burst of vomiting, Hyuk looked half-dead as he spoke.

“I think this is as far as I go.”

Anyone looking at him might have taken him for a wounded soldier who’d been stabbed while fighting bravely.

I gripped his shoulder hard.

“Mujin. You can do this.”

“No. I’m finished. I’ll only be a burden if I go.”

“A burden? You’re an excellent meat shie—”

“Excuse me?”

“Shield! You’re the Jin Family of Taiyuan’s shield!”

“I could have sworn you said meat shield.”

Ignoring Hyuk’s suspicious muttering, I hauled him to his feet. Right now, even a meat shield—no, a single extra hand—was precious.

Besides, apart from me, Hyuk was the strongest meat shield in the reconnaissance squad. Ah, it kept slipping out.

I deliberately lowered my voice.

“Our family is in danger, and you’re saying you want to run?”

If it had been me, I would have run.

“No, sir!”

A twenty-first-century office worker would have spat in your face and walked away, even if you’d offered to file it as a workplace injury. But the reconnaissance squad was more loyal than I’d expected. Hyuk drew his sword with a pale face.

“Very well. If a martial artist has to die, he should die fighting.”

“That’s a fine resolve, but don’t die.”

“You just called me a meat shield.”

“You don’t trust me?”

“Yes.”

Hyuk’s answer was as sharp as a blade, and a light laugh spread through the reconnaissance squad. They’d been frozen stiff by the first large-scale battle of their lives, but they seemed to loosen up a little.

I grinned and gripped my spear.

“Eyes wide, ears open. Follow my orders, and you’ll make it back alive.”

That was a vow I was making to myself. I would get these guys out alive somehow.

*Please don’t die.*

I didn’t know how this war would end, or who would live and who would die.

All I could do was give it everything I had.

“Let’s go.”

At that, we charged forward like a gale. We were an arrow with me at the tip, and the target we had to hit was already set.

*The Head Elder.*

Clear in the distance, I could see a white-haired old man. At his feet lay a fallen man, and a pool of blood.

A hot lump of fire surged up from my gut.

“That’s my brother…”

I pulled a spear from where it had been driven into someone’s corpse like a gravestone. Then, in the next instant—

“Get your hands off him, you bastard!”

The spear shot in a straight line, compressing dozens of yards of distance.

Someone in the reconnaissance squad let out a muffled cry.

“We got him!”

That was when the Head Elder’s sword moved.

Shuk.

A streak of light. The spear split in half and bounced away to either side.

Same result as before. But this time we’d closed the distance considerably, so I could see it clearly.

The blue flash that had surged along the blade for an instant.

*Aura?*

No. Why was that showing up here?

* * *

Aura.

A crystallization of mana that only an A-rank Hunter or higher could draw out.

Mana and internal energy were different only in name. In terms of qi, they were the same. And this was Murim, so put another way, it was Sword Energy.

Sword Energy.

Heh heh heh.

*Fuck. Are you kidding me?*

I’d known for a long time that the Head Elder was a master. I’d even been ready to fight him if it came to that. The problem was that a Head Elder *using Sword Energy* hadn’t been part of the plan.

*This is a bit much.*

I glanced aside and saw ten-odd pairs of shaking eyes.

Hyuk Mujin’s were practically seismic.

“S-Squad Leader.”

“Y-Yeah?”

“That just now… that looked like Sword Energy.”

“Yeah…”

“Can you use Sword Energy too?”

“If I could, I would have used it already. Even Jopil wasn’t at that level.”

“Right?”

“Right. But aren’t you exhausted?”

“I feel like I’m going to throw up.”

As if we’d agreed on it, we slowed down. The event had switched from a hundred-meter dash to race walking, but it still felt like walking into a lion’s jaws.

“Uh, Squad Leader.”

Hyuk opened his mouth with a face drained of all color. As far as his skin went, he could have passed for a white man.

“Are you sure the Head Elder betrayed us?”

“I’m sure.”

“Could it possibly be a misunderstanding—”

Before he could finish, three or four black-clad men charged at us with a shout.

“Protect our lord!”

“For the Head Elder!”

Get a load of those lines. They’d work as a toast at a Jin Family of Taiyuan year-end party.

I cut down every last black-clad man charging us, then looked at Hyuk.

“Uh, what were you about to say?”

“…Nothing.”

Having failed to win the argument in his head, Hyuk hung his head, looking grim.

But only for a moment. Step by step. The closer we got to the Head Elder, the more desperately he started hunting for a way out.

“Why do people have to fight?”

*Is this bastard aiming for the Nobel Peace Prize?*

“You said earlier you’d fight and die. Like a martial artist.”

“That was the worst case. Wouldn’t it be better to settle this with talk?”

“Talk’s good. But they sent assassins after us first.”

“Oh.”

“And I threw a spear.”

“Ah.”

“And I cursed while throwing it.”

“Ah—ahhh.”

When we closed to within about a hundred feet of the Head Elder, Hyuk’s face looked like death. The other reconnaissance squad members didn’t say anything, but I could see them shaking.

Of course, I wasn’t much different. Just thinking about Sword Energy made my chest hammer.

*I’m well and truly screwed.*

But I had no intention of running. If I had, I never would have come back in the first place. I would have been content with reality and just lived that way.

I’d already come too far. There was only one path left.

“Stop.”

Everyone halted as if they’d been waiting for it. Hyuk’s face said he was hoping for a dramatic peace treaty, but I gripped my spear and stepped forward.

“W-Where are you going?”

“To fight. You wait here.”

“Are you insane? We’d be better off waiting for the Lesser Family Head and attacking together—”

“See the person lying over there?”

“Y-Yes.”

“That’s my brother.”

Hyuk looked at me like the sky had fallen, then let out a long sigh.

“Then I’m coming with you.”

“What?”

“Even a meat shield like me should bump our odds up by a hair, shouldn’t it?”

This guy actually came up with some admirable thoughts.

I snorted a laugh and turned away.

“You going there to die? I’m just going to test the waters and come back. Wait here.”

The distance to the Head Elder was now barely thirty feet.

A distance either of us could close in an instant.

A heavy silence crushed the space between us. In that brief interval, my palms went damp.

*Phew.*

But I wasn’t an easy mark either. At Level 30, when I was only Second Rate, I’d already beaten Jopil, a Peak master. And I’d kept improving after I went back to reality.

At Level 40, I could proudly call myself a master who held his own in both reality and Murim.

No. I was a master.

*If I fight while keeping as much distance as I can…*

In a fight where a few centimeters could decide life or death, a spear’s reach was a massive advantage.

I looked at the Head Elder’s face and steadied my breathing.

*This is doable.*

I drew up my internal energy in a single burst and charged. Ten feet—the range where my spearhead could reach the Head Elder, and his sword couldn’t reach me.

*Now!*

I brought the spearhead down toward the crown of his head.

At the same time, the System notification I’d been waiting for rang out.

Ding.

> **System**
>
> - The effect of the Title **Gambler** is applied.
> - **Strength** temporarily increases.
> - **Agility** temporarily increases.
> - **Stamina** temporarily…

The effect of the Gambler Title, which raised combat-related stats by ten percent in a one-on-one duel, seeped through my whole body.

And on top of that—

Whoosh!

The boost to my stats accelerated the attack as well. In an instant, the spearhead dropped like a bolt of light, aimed at the crown of the Head Elder’s head.

*This is going in.*

That was certainty.

The certainty that even a monster like Jopil wouldn’t have been able to dodge it. But the man I was facing wasn’t Jopil.

He was the Head Elder.

Boom!

The spear shaft shuddered with a thunderous crash. The Head Elder, having blocked the spear at a speed too fast to see properly, smiled faintly.

“Not bad. Better than I expected.”

Without even time to answer, I wrung out every last ounce of strength. The spear, loaded with tremendous force that even a decent master would have struggled to endure, crushed down on his sword.

Grrrkk.

With an ugly grinding sound, his sword began to lift…

No. Wait.

*It should be going down. Why is it coming up?*

I’d put that much force into it, and I was the one being pushed back. At my dumbfounded expression, the Head Elder’s smile deepened.

“You tried, but did you think that would be enough?”

The next instant, every hair on my body stood on end.

Tsssss.

A blue haze bloomed along the blade.

Sword Energy.

Before I could even react, the spearhead that had been slowly getting pushed back was sliced off like tofu.

Shing.

Now it wasn’t a spear but a staff. A long staff.

Sword Energy flashed again toward me as I backed away.

Shing.

The long staff became a short staff.

Shing.

“…”

Fuck. Even nunchaku would be longer than this.

I threw the iron rod—no longer a spear or a staff—at the Head Elder.

Shing.

“Do you intend to run?”

Run? That’s a hurtful thing to say.

I’d already thrown myself sideways at the same moment I threw it. I grabbed the collar of the man lying facedown as if he were dead.

*Got him!*

My only goal from the beginning had been to rescue Jin Wikyung.

Now that I’d done it, there was no reason to fight that monstrous old man. I scooped Jin Wikyung into my arms and hurled myself away with all my strength.

Whoosh—boom!

The Sword Energy that arrived a beat later split the ground.

Hyuk Mujin and the reconnaissance squad surrounded us as we slipped out of the Head Elder’s range by a hair.

“Protect the Squad Leader!”

“Are you all right?”

I said nothing. I forgot we had to run from the Head Elder right now. I even forgot this was a battlefield.

My head was full of a single question.

*Who is this man?*

I had definitely rescued Jin Wikyung. I was supposed to have rescued him…

Then who was this macho middle-aged man in my arms?

His face was covered in sword scars, and his eyes were bloodshot. In a trembling voice, I asked,

“Excuse me, but who are you…?”

At that moment, a single cry burst from Hyuk Mujin’s mouth.

“Gah! Lee Cheonbaek!”

Lee Cheonbaek? The name rang a bell.

“You know him?”

“Of course I do!”

“Are you close?”

“What kind of bullshit is that? That’s Blood Wolf Sword Lee Cheonbaek!”

“Blood Wolf Sword?”

“Yes! That Blood Wolf Sword…!”

“Cool alias. Sounds like a master.”

Hyuk tore at his hair and shouted,

“He’s the Sect Leader of the Mount Heng Sword Sect! Blood Wolf Sword Lee Cheonbaek!”

“…”

I scrambled backward.

This man was Lee Cheonbaek?

Cold sweat rolled down me.

*He’s Lee Seogeun’s father.*

He was the man who’d started a war because he thought I’d poisoned his son. He was also a cold-blooded killer who’d slaughtered adults and children alike in revenge.

*Rescuing the wrong guy was unfair enough, and I nearly got stabbed too.*

But Lee Cheonbaek no longer seemed to have the strength left for that.

His whole body was covered in blood, and he couldn’t so much as twitch a hand. It looked like severe internal injuries, or like his acupoints had been sealed.

*Still, at least it isn’t Jin Wikyung.*

As if he’d read my mind, Hyuk asked,

“Then where is the Lesser Family Head?”

“I don’t know. And…”

I yanked him back by the nape of his neck. A sword came flying in and buried itself where Hyuk’s foot had been a moment before.

*I’m really well and truly screwed.*

I let out a long sigh, then went on,

“You think that old man is going to let us go?”

The Head Elder burst into a hearty laugh.

“Ha ha ha! Have you ever seen such an insolent brat!”

“If I behave politely, will you let us go?”

“Don’t you think you’ve come too far for that?”

Tsssss.

Sword Energy surged up.

No more words were needed.

I pulled a spear stuck among the corpses. Then, with everyone’s eyes on me, I spoke.

“Encircling formation. Spread out.”

One of the oldest Hunter sayings was this:

*There are strong monsters, but no monster that can’t be taken down.*

What made that possible was a raid.
## Chapter artifact 59

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

Sixty years. He had won profound internal energy, but even that could not stop his body from aging.

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

But the Discipline Hall Master’s dignified end brought boiling back feelings they had set aside.

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

Once he had the whole situation, a voice like frost burst from Jin Wikyung’s mouth.

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
