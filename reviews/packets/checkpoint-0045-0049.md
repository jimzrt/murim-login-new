# Checkpoint Review — 45–49

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

# Chapters 45–49

## Plot

Taekyung kills the Level 45 Hobgoblin Great Warrior after Character Synchronization restores his System in reality. His Status Window shows Level 33, First Rate Martial Artist, powerful renewed stats, fifteen years of Internal Energy, and the incomplete Traitor Chain Quest. Officials investigate how two C-rank Rare Monsters appeared in an E-rank Gate, while Taekyung asks Team Leader Choi to conceal his strength.

Choi offers Taekyung a 100 million won Peace Guild position, but Taekyung refuses a long-term contract because he fears the System may disappear. After recovering the Ark - 2020 capsule from Seong Jinho, Taekyung confirms that its manual binds it permanently to its user and that the System cannot read either the capsule or manual. He visits the Hunter Association for reassessment, where his former boss Kim Sangshik confronts him. Taekyung effortlessly crushes Kim’s wrist when Kim grabs him, but the reassessment device malfunctions while scanning his Internal Energy.

The Association recognizes Taekyung as C-rank-level, prompting Guild recruitment offers. Taekyung rejects Kim’s apology and says he will consider Sopung Guild only if it removes someone he hates—clearly Kim. He tells Jinho a false account of his reawakening and the Gate, then becomes afflicted with Dead Drunk and dreams of indistinct Murim voices telling the youngest to survive. After detoxifying a Hangover through qi circulation, Taekyung signs a seven-day provisional contract with Peace Guild.

Choi takes Taekyung into a D-rank Gate alone after giving him expensive equipment. Taekyung equips a First Rate Lizardman Hunter’s Leather Set and Lizardman Slayer’s Harpoon. Choi reveals that he was already C-rank before a later reawakening, leading Taekyung to infer that Choi is at least B-rank. They enter the Gate together.

## Continuity

- The Hobgoblin Priest and Level 45 Hobgoblin Great Warrior are dead. Im Hyeokjun and the other veteran Hunters survived but require hospitalization.
- Taekyung’s restored System shows Level 33, First Rate Martial Artist, 120 Strength, 125 Stamina, 121 Agility, 20 Intelligence, 20 Charm, fifteen years of Internal Energy, and 30 Remaining Points.
- Fame is 0; Taekyung’s active Titles are Novice Trainee and Gambler. The Traitor Chain Quest remains incomplete and carries a death penalty for failure.
- Taekyung is recognized as C-rank-level but is not yet formally registered as a C-rank Hunter; the official reassessment takes several days.
- Taekyung has signed a seven-day provisional Peace Guild contract, not the offered one-year contract. He enters a D-rank Gate with Choi alone.
- Taekyung’s equipment includes the First Rate Lizardman Hunter’s Leather Set, whose Scale Armor effect activates when complete, and the Lizardman Slayer’s Harpoon, which can cause Bleeding.
- Choi was C-rank before reawakening. Taekyung infers that Choi is at least B-rank, but Choi’s exact current rank remains unknown.
- Kim Sangshik helped arrange Taekyung’s dismissal from Sopung Guild and is now threatened with expulsion if Sopung wants Taekyung’s consideration. Choi Min-su remains a C-rank Hunter with A-rank mana control whom Sopung is trying to recruit.
- Taekyung continues hiding Murim, the capsule’s true nature, and the System from Seong Jinho. The capsule remains permanently bound to Taekyung until death, and its purpose and route back to Murim are unresolved.
- Reality’s qi is weak and polluted. Murim’s death and resurrection limits, the Head Elder’s accomplice, the officials’ investigation, Taekyung’s formal registration, and the outcome of the D-rank raid remain unresolved.

## Translation Decisions

- Preserve **Character Synchronization**, **Synchronization complete**, and **All systems are inherited** exactly.
- Keep **First Rate Martial Artist**, **Internal Energy**, **Fame**, **Titles**, **Remaining Points**, **Dead Drunk**, and **Hangover** as established System terminology.
- Distinguish Hunter **rank** from System item **Grade**.
- Use **C-rank-level** for the Association’s provisional recognition until formal registration.
- Preserve **Peace Guild**, **Sopung Guild**, **Hunter Association**, **D-rank Gate**, **Lizardman Hunter’s Leather Set**, and **Lizardman Slayer’s Harpoon**.
- Retain Taekyung’s dry, self-mocking voice, Kim’s petty obsequiousness, Jinho’s emotional support and finder’s-fee jokes, and Choi’s measured dialogue.
- Preserve the exact unreadable-item notification **“This Item cannot be read.”** and the capsule’s permanent user-binding rule.
- Keep **young master**, **Black Ivory**, and the concise Pocheongcheon footnote.

## Durable state

{
  "version": 1,
  "safe_through": 49,
  "continuity_sources": [48, 49],
  "active_continuity": [
    "Jin Taekyung is back in reality after logging out of Murim. He remains formally an F-rank Hunter pending registration of his C-rank-level reassessment, has signed a seven-day provisional contract with Peace Guild, and is entering a D-rank Gate with Team Leader Choi.",
    "Taekyung is the disgraced third son of the Jin Family of Taiyuan and narrates with dry, self-mocking, occasionally profane humor.",
    "The Ark - 2020 capsule's purpose and route back to Murim remain unresolved; its manual says users are bound until death, time runs at an adjustable slow ratio, and Character Synchronization exists.",
    "Murim's death and resurrection limits remain unresolved.",
    "The identity of the Head Elder's Sound Transmission accomplice and the full purpose of their plan remain unresolved.",
    "Im Kkeokjeong is Taekyung's old acquaintance, now E-rank Hunter Im Hyeokjun. He is a veteran Peace Guild member, calls Taekyung his little brother, and serves as a main tank with a tower shield and mace.",
    "Peace Guild is new and has only three people including its Guild Master. Taekyung's original E-rank Gate party consisted of Team Leader Choi, Im, three other veteran E-rank Hunters, and Taekyung as porter.",
    "Team Leader Choi was first measured as a C-rank Hunter and later reawakened. He uses expensive equipment, a sword, and wind-based Haste magic; Taekyung infers that Choi is at least B-rank, but his exact current rank is unknown.",
    "Taekyung can butcher Hobgoblin corpses at professional speed and has done this as paid raid work for years.",
    "The Boss Zone contained an old Hobgoblin Priest and a Level 45 Hobgoblin Great Warrior summoned from nearly a hundred dead Hobgoblins; both Rare Monsters are now dead.",
    "Character Synchronization completed in reality and all systems were inherited. Taekyung's Status Window now shows Level 33, First Rate Martial Artist, 120 Strength, 125 Stamina, 121 Agility, 20 Intelligence, 20 Charm, fifteen years of Internal Energy, and 30 Remaining Points.",
    "Fame is 0 and the active Titles are Novice Trainee and Gambler. The Traitor Chain Quest is active but incomplete: Taekyung must punish the traitor and lead the battle to victory; failure means death.",
    "Team Leader Choi killed the Hobgoblin Priest and witnessed Taekyung kill the Great Warrior. Officials are investigating how two C-rank Rare Monsters appeared in an E-rank Gate.",
    "Im Kkeokjeong and the other veteran E-rank Hunters survived the Boss Zone fight but were sent to the hospital for about a week.",
    "Taekyung accepts that Murim was real and wonders whether he can return; Choi's response to Taekyung's request for secrecy about his strength remains unclear.",
    "Choi's background check found that Taekyung was the sole survivor of the Sangdong Station Mutated Gate, returned to Gate work for a year and a half, and was fired three days ago; Choi suspects he is at least C-rank or recently reawakened.",
    "Seong Jinho took Taekyung's discarded Ark - 2020 capsule and returned it to his room after bargaining over a finder's fee. The manual confirms that the capsule is permanently bound to its registered user until death.",
    "The System reads ordinary objects but cannot read the capsule or its manual. Taekyung is awaiting formal Hunter registration after the Bucheon Branch reassessment.",
    "Taekyung encounters former boss Kim Sangshik at the Hunter Association and confronts him over arranging his dismissal. Kim is a Level 24 D-rank Hunter and one of Sopung Guild's team leaders; Taekyung's synchronized strength overwhelms him when he grabs Taekyung. The reassessment device malfunctions while scanning Taekyung's internal energy, but the Association recognizes Taekyung as C-rank-level. Choi Min-su of Sangdong Guild measures as C-rank with A-rank mana control, and Sopung's Guild Master orders Kim to recruit him.",
    "Guild scouts immediately compete to recruit Taekyung after the reassessment. Kim apologizes for his past conduct and offers Sopung Guild's recruitment package, but Taekyung tells him to say he will consider it only if Sopung gets rid of one man he cannot stand—the obvious target being Kim.",
    "Taekyung wakes from the System's Sleep Mode with a Hangover, detoxifies it through qi circulation, and finds reality's qi weak and polluted. He declines Choi's one-year contract, signs a seven-day provisional contract, chooses the First Rate Lizardman Hunter's Leather Set and Lizardman Slayer's Harpoon, and enters a D-rank Gate with Choi alone.",
    "The Lizardman Hunter's Leather Set activates its Scale Armor effect when fully equipped, and the Lizardman Slayer's Harpoon has a high probability of causing Bleeding. A deferential middle-aged man restricts access to the Gate and addresses Choi as 'young master,' indicating Choi's wealthy background."
  ],
  "open_questions": [
    "The capsule's purpose and route back to Murim remain unresolved; the System cannot read the capsule or its manual.",
    "The limits of Murim's death and resurrection rules remain unresolved.",
    "The identity of the Head Elder's Sound Transmission accomplice and the full purpose of their plan remain unresolved.",
    "Whether Choi keeps Taekyung's strength secret, whether the officials' investigation exposes Taekyung, how the System's restoration relates to Murim and a possible return, whether Taekyung's formal C-rank registration completes, Choi's exact current rank, whether Taekyung and Choi survive the D-rank Gate, and whether Sopung Guild can recruit Choi Min-su remain unresolved."
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
    "Use Lizardman Hunter’s Leather Set and Lizardman Slayer’s Harpoon for the First Rate System items, and retain the Pocheongcheon reference with a concise footnote."
  ]
}

## Reading copies

## Chapter artifact 45

# Chapter 45

Slash.

The red eyes blinked, almost tame. So even a C-rank Rare Monster—the terrifying Hobgoblin Great Warrior—could make a face like that.

*Why didn’t I realize it until now?*

With that passing thought, I shook the blood off the spearhead. At the same time—

Thud.

Something heavy hit the ground. The Great Warrior saw what it was and, without meaning to, shuffled backward.

Well, fair enough. Its right arm had been snipped clean off below the elbow.

*I thought you’d be a little different.*

Jin Family’s Manoeuvre Technique. Yeah—I’d used that exact technique to drive in against its chest. The Great Warrior reflexively swung its right arm, but that space was already empty.

“Forgot already?”

I set the spearhead against the Great Warrior’s side and drove it upward in the same motion. Charged with internal energy, the blade split hard skin and muscle.

Slash—

Its left arm came off in a spray of green blood.

Both arms gone in an instant, the Hobgoblin Great Warrior bellowed, the sound smeared with rage and pain.

—Kuwaaaaaargh!

But I still couldn’t let my guard down. Even without arms, it was more than dangerous enough bare-handed.

“Yeah. Come on in.”

Before I’d even finished, that massive frame charged.

Clang! Clang! Clang!

As expected, this thing’s body was a weapon all by itself. True to being a monster, it had primitive senses and strength beyond any human.

Swish. Slash.

Hooked claws grazed my forearm. A handful of flesh tore away, and blood poured out. Without flinching, I blocked the heel stomping down at the crown of my head.

Thud. Crunch.

The ground under my feet started to sink.

Incredible strength. At this rate, I might get buried standing up.

*If I didn’t have internal energy, that is.*

I drew up every last bit of internal energy in my dantian. The force flooded into every limb. As the spear shaft slowly rose, the Great Warrior’s eyes wavered.

*Too late.*

If it had been whole from the start, maybe. After losing both arms, the Hobgoblin Great Warrior was no longer my match.

—Grrr.

In the end, it was the one that backed off first. And from that point, the fight was as good as decided.

I didn’t stop. I thrust the spear out.

*Jin Family’s Spear Technique. First form.*

The movements engraved in my body and head unfurled in a rush.

Thrust. Cut. Block and strike with the shaft. Simple on their own, but the order and the angles made countless combinations.

That was martial arts, as I defined it.

Clang! Clang!

Swish. Swish-swish-swish!

Second form. Third form. Fourth…

Those hooked claws, hard as steel, were cut away. Every step it gave, a new wound opened and more blood spilled.

Then the Hobgoblin Great Warrior’s back hit the wall.

“Grrrk…”

A C-rank Rare Monster. This thing had seemed impossible to face, but those red eyes had already lost their will to fight a long time ago.

“Go. Now.”

Shunk.

Ghk. With a death rattle, the hulking green body slid down the wall.

And then—

Ding.

> **System**
>
> You have defeated Lv. 45 Hobgoblin Great Warrior!
>
> Level Up!

The System notification rang. I’d thought I’d never hear it or see it again…

*A System, out of nowhere?*

I wasn’t the only one confused.

“…Mr. Jin Taekyung?”

Team Leader Choi had already taken care of the Priest. His pupils trembled like they’d been hit by an earthquake as he looked from me to the Great Warrior’s corpse and back.

“What… are you?”

Yeah. I’d like to know that myself.

Heh heh. Heh heh heh.

* * *

“A Rare Monster?”

The cigarette in the government official’s mouth dropped.

He looked born to be a civil servant, and this was anything but good news for him. Sure enough, the way he looked us over was nothing but unease.

“W-what rank?”

Team Leader Choi gave the Priest’s staff a weary shake.

Clank.

“C-rank Rare. Hobgoblin Priest.”

“C-rank?! For fuck’s—”

Hey, save the swearing. There’s one more.

I kicked the Hobgoblin Great Warrior’s greatsword I’d been using like a walking stick. At the dull sound, the official turned.

“And that?”

“Buy one, get one more. C-rank Rare. Hobgoblin Great Warrior.”

“Two mid-grade Rare Monsters? In an E-rank Gate?”

I got the reaction. This had to at least make some kind of sense.

The official looked back and forth between us and the gear for a while, then finally nodded with a sad face.

“I’ll contact my superiors first.”

“Hey, mister. Hold on.”

Im Kkeokjeong had come to at some point. I was holding him up. He’d taken serious injuries—at least five broken bones.

“Call a healer. A pretty unnie.”

The E-rank trio dropped onto the ground as well.

“And potions! Potions! The good stuff!”

“Ah, for fuck’s sake, how did you people even manage this Gate?!”

“Our gear’s all smashed too, huh? What are you going to do about this?!”

Do about it? The government would cover everything.

There was an actual law for this: every item used in the Gate, plus medical costs and compensation.

So it was a show. Squeeze out a little extra.

*Tsk. Even so. People are watching.*

That was when I felt a stinging look from beside me.

“…Mr. Taekyung.”

Team Leader Choi.

“What are you doing?”

He was looking at me, confused. More precisely, at the hand holding my dagger.

Grrrk.

The dagger, charged with internal energy, raked long lines through seven-year leather armor until it was too wrecked to use.

“...”

“...”

“Team Leader Choi.”

I sighed hard enough to cave in the ground.

“The Hobgoblin Great Warrior. It was really strong. I made it out alive, but every piece of gear I had is ruined.”

“...”

“The armor that protected me for seven years. And now even the spear.”

“The spear looks perfectly—”

Right then, I pressed down steadily on the middle of the spear with one foot.

Under the majesty of a three-digit Strength stat, the iron spear bent like a stick of taffy.

“Looks perfectly fine? This?”

“...”

Team Leader Choi shut his mouth.

* * *

Team Leader Choi was called away by the officials dispatched to take charge, and the other four were moved to an ambulance for treatment.

Instead of the musty break room, I was left alone in a wide, comfortable office. Now that the moment had actually come, my heart started pounding.

*St-Status Window?*

At that half-doubtful call, the System answered.

Ding.

> **System**
>
> **Status Window**
>
> **Lv. 33 Jin Taekyung**
>
> **Job:** First Rate Martial Artist
>
> **Fame:** 0
>
> **Titles:** 2 (Title effects active)
>
> - Novice Trainee (Training speed +10%)
> - Gambler (Combat-related stats +10% in one-on-one matches)
>
> **Strength:** 120  **Stamina:** 125
>
> **Agility:** 121  **Intelligence:** 20
>
> **Charm:** 20  **Internal Energy:** 15 years
>
> **Remaining Points:** 30
>
> Synchronization has been completed. Changes have occurred to Titles and Fame.

“Fuck. It really came up.”

I stared at the Status Window, blank, then noticed something off.

*The Status Window… changed?*

The first things that jumped out were Fame reset to zero and two missing Titles. The last line gave me a rough idea why.

*Because this isn’t Murim?*

All five hundred Fame I’d stacked had been earned as a martial artist in Murim. The Title that had vanished, *Scion of a Prestigious Family*, made sense the same way.

*Well, I’m not some prestigious family’s son here. And I’m sure as hell no Sleeping Dragon.*

If I were getting a Title here, it’d obviously be something like *Scion of the Common Folk*, or *Earthworm* instead of Sleeping Dragon.

“How much else changed?”

For about ten minutes I turned every System function on and off and tested them. The only thing that had changed was the Status Window.

No. There was one more. The Quest Window.

Ding.

> **System**
>
> **Quest**
>
> **Traitor**
>
> You have discovered the traitor’s identity. Rejoin the main force, inform them that there is a traitor, and lead the battle to victory!
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Punish the traitor (Incomplete)
>
> Battle victory (Incomplete)
>
> **Reward:** Vast EXP and Fame
>
> Valuable iron chest
>
> **Failure:** Death

The Chain Quest I’d gotten after taking down Gwak Jun and the assassins. My thoughts tangled.

*Go back? To Murim?*

I knew it now. The Murim I’d been through wasn’t an illusion, and it wasn’t a game. A wildly unrealistic story, sure, but Murim was probably…

Creak.

I turned at the sudden sound. Team Leader Choi was standing in the doorway.

“Let’s go, Mr. Taekyung.”

Looked like the talk had wrapped up. I folded the thought away and stood.

“The others…?”

“They should be on their way to the hospital by now. They said about a week of admission. You don’t need to worry.”

I wasn’t particularly worried. Combat-type Hunter bodies, plus potions and healing magic—they’d be up soon enough.

And…

“How did it go?”

“They’ll contact us again in a few days. An investigator will probably come see you, too.”

An investigator.

Not a type I wanted to run into again. But that wasn’t the answer I’d wanted, so I asked again.

“And the rest?”

“Hmm.”

Team Leader Choi looked at me with an odd expression. Like he was studying some strange animal.

*Did he tell them the truth?*

I didn’t want my strength out in the open. Even less now, when I still barely knew why the System was showing up in reality, or what it had to do with Murim.

An F-rank Hunter killing a C-rank Rare Monster alone was unheard of. An awl in a bag pokes through. I’d lived the opposite kind of life, nothing sticking out, so I had to be careful.

So I asked him.

“Could you keep what concerns me a secret?”

From Team Leader Choi’s side, it had to be a hard ask. I was telling him to lie in his statement for someone he’d only just met.

“Mr. Jin Taekyung.”

“Yes.”

His heavy voice made my chest sink with it—and then:

“Let’s get some food.”

“What?”

“Look.”

Team Leader Choi held out his wrist. A glittering Magic Gem electronic watch pointed to two in the afternoon.

“It’s an N Company piece carved from a whole C-rank Magic Gem. It’s got enhancement magic, so in an emergency you can even use it as a shield—”

*So that’s where he was going.*

“…Let’s go.”

Impossible man to read.

“Let’s get some meat. You like Hanwoo?[^1]”

“Hanwoo?”

“Yes. Highest grade.”

And rich, too.

“I never get to eat it.”

Not just any beef. Hanwoo. Top-grade Hanwoo at that.

System or whatever—first I had to fill a hungry stomach.

[^1]: Hanwoo is beef from Korean native cattle, prized as premium meat.
## Chapter artifact 46

# Chapter 46

Sizzle.

The meat hit the grill. Thick, red, and marbled with white streaks like snowflakes—it was the finest Hanwoo beef.

The shape, the sound, the smell. All of it was intoxicating. The only thing I didn’t like was the price…

“Will this be enough? Let’s order more after we eat. Some special cuts, too.”

A rich C-rank Hunter was paying, so whatever.

*How long had it been since I’d last had Hanwoo?*

Food in Murim was spicy, salty, and bland. And even then, more days than not, I couldn’t eat properly. For thirty days, my stomach had been abused with beef jerky, bigu pills,[^1] and rice balls.

Chomp. Chomp-chomp.

The best thing about beef was how quickly you could eat it. The moment it looked more or less done, it went straight into my mouth.

Every chew felt like walking on clouds. This piece, that piece, that one too—every last one tasted like heaven.

“Hnnngh.”

Team Leader Choi watched me with that peculiar look of his.

“Would you like some more?”

“No. I should hold back on overeating.”

“We’re at twenty-five servings…”

“Twelve servings each isn’t all that much.”

“I’ve only eaten three servings.”

“Oh, can we order some yukhoe?[^2]”

“…Yes.”

“Rice, too.”

“…”

And so that storm of a meal came to an end. At last, Team Leader Choi opened his mouth.

“I said I was the one who killed them. The Priest and the Great Warrior, both.”

“Oh. Thank you.”

“Don’t mention it. Let’s call it a fair deal. If anything, there’s something I should thank you for, too.”

A fair deal.

He wasn’t wrong. I’d bought myself time to think, and he would gain a reputation. After all, he had led five low-rank Hunters and killed two mid-grade Rare Monsters.

The fact that nobody had died in the process would be a huge help for Guild publicity, too.

*What if I hadn’t found my strength through Synchronization?*

Who knew? Someone probably would have died. Maybe nobody would have made it out alive.

“You were already thinking along those lines.”

He wasn’t just some eccentric. Not with instincts that sharp.

I smiled awkwardly.

“It’s good for both of us.”

“Good for both of us. Both of us…”

Team Leader Choi muttered to himself, then asked out of nowhere,

“Would you like to join the Guild?”

“Pffft.”

Team Leader Choi lifted the tablecloth and blocked the water, then smoothly produced a business card with practiced elegance.

> **Peace Guild, Team 1 Leader Choi Minwoo**

What the hell was this? For a second I was completely thrown.

“Y-you’re making me a recruitment offer? Right now?”

“That’s right. We always need talent.”

I took the card, and for some reason I felt deeply moved.

It seemed like only yesterday that I’d been going to interviews with my back bent like a shrimp…

*Live long enough and you really do see everything.*

An actual recruitment offer, treating me like talent. F-rank Hunter Jin Taekyung, you’d come a long way.

“Our Guild is still new, and we don’t have many people, but we’re excellent where it counts. For example…”

Team Leader Choi elegantly swirled his wineglass. When had he even ordered that?

“Our finances are extremely solid.”

“Oh, finances!”

“And because of that, our employee benefits are excellent.”

“Oh, benefits based on solid finances!”

“Our Guild Master is a B-rank Hunter.”

“Oh, a high-ranking Hunter—the source of those solid finances!”

“There’s no need to worry about restructuring.”

“Oh, a stable workplace!”

Team Leader Choi asked with an affluent smile,

“Will you come?”

I scratched my head.

“No. That’s a little…”

“…Pardon?”

“I have some circumstances that make it difficult right now. I need time.”

If I followed my heart, I wanted to sign the contract right away—signature, stamp, thumbprint, even a kiss mark.

*But what if the System vanished tomorrow?*

I’d be dead broke.

Overnight, I’d go from being called talent to being called a human disaster.[^3]

“Is it a money problem?”

There was always a money problem.

But this was more important than that. I couldn’t get dazzled by the wad of cash right in front of me and snatch at it.

“It’s difficult to explain. I’m sorry, but this isn’t something I can decide right now…”

“100 million won.”

“100 million?”

“Just the signing bonus. The rest will match the minimum terms for a C-rank Hunter.”

That was dangerous. This time it was really dangerous.

But I held out with superhuman patience. Hadn’t I already learned that life wasn’t that easy?

It could be money I’d end up choking on.

“I’m sorry.”

Team Leader Choi looked at me quietly, then nodded.

“I’ll wait for your call.”

* * *

One person left, and one person stayed.

Team Leader Choi—no, Choi Minwoo—looked in silence at the seat Jin Taekyung had left, then took out his phone.

Beep. Beep. Click.

“—You bastard, you’re a ghost. I was just about to call you.”

“How did that thing I asked about turn out?”

“—I looked into it because you asked, but… is there something about this Jin Taekyung guy?”

“That’s why I called you. So? What did you find?”

“—It’s a dime-a-dozen case. Seven years ago he Awakened at twenty and was assessed as F-rank. There’s a record he finished first at the Hunter training center…”

Jin Taekyung’s past seven years spilled from the other end of the phone. Then, at one point, Choi Minwoo’s eyebrows twitched.

“What? The Sangdong Station Mutated Gate?”

“—Yeah. You know about that incident, right?”

How could he not? It had happened only two years ago, so Choi Minwoo remembered it clearly.

“—He was the only survivor. I checked that part myself, and it surprised me, too.”

Choi Minwoo tipped his glass of water. Thinking he’d grabbed a lead on how an F-rank Hunter had killed a mid-grade Rare Monster alone made his throat burn.

“And?”

“—He took six months off. The Hunter Administration kept sending investigators, and I guess he spent the time trying to get himself back together. You know how serious the incident was.”

“And then?”

“—That’s it. He went back to his Guild, ran Gates his ass off for a year and a half, then got fired. That was exactly three days ago.”

“Why was he fired?”

“—It was technically restructuring, but a booger-sized little Guild, restructuring? Please. The incident probably had a lot to do with it. They kept glancing nervously at the Administration, then pushed him out. From their perspective, he’d have been awkward to keep around.”

“That’s all?”

“—As far as I can tell. Want me to send you the file separately?”

“Send it now. I’m hanging up.”

“—Hey, hey!”

Click.

Choi Minwoo tapped the table with his long fingers.

Jin Taekyung. F-rank Hunter. The sole survivor of the Sangdong Station Mutated Gate.

And…

*At least a C-rank Hunter.*

That was the absolute minimum. The image of Taekyung driving a C-rank Rare Monster into a corner alone, with overwhelming strength and skill, kept flickering before his eyes.

*And yet he’s F-rank.*

There were only two possibilities. He had been hiding his strength, or he had recently reawakened.

Choi Minwoo suspected the latter, but that was still far beyond common sense.

It wasn’t as if only one or two Hunters retired without ever ranking up even once.

Reawakening from F-rank to C-rank was, without question, extraordinarily rare.

*This isn’t some kind of game. What the hell is he?*

Choi Minwoo shook his head. He felt as if a ghost had possessed him.

*I’ll have to look into this further.*

As he rose from his seat, the restaurant owner approached and held out the bill.

“1,937,000 won.”

“…”

He really did feel as if a ghost had possessed him.

* * *

“Shit. I’m fucked.”

I dropped heavily onto the ground. The recycling area was a mess. The thing that should have been there was nowhere to be seen.

“It’s gone. It’s gone. My capsule is gone.”

I’d been anxious ever since leaving Team Leader Choi. But I hadn’t expected someone to take it in less than half a day. I shouted into the empty air.

“Who the fuck was it?!”

And I got an answer.

“Me, you son of a bitch.”

On the roof of the goshiwon building,[^4] Jinho hyung was smoking in the same spot where I’d seen him that morning. He exhaled a plume of smoke with a wistful look, then went on.

“I spent ten years crying, regretting it, and making vows…”

“You want me to make you really cry and regret it?”

“You’re no fun. You haven’t seen this movie, have you?”

“Quit joking around. This is serious.”

“What, you come up empty today?”

“No.”

My voice drained of strength as I went on.

“The capsule.”

“…Huh?”

“Some bastard took my capsule.”

“Cough, cough-cough!”

Maybe he’d inhaled the cigarette smoke wrong. Jinho hyung coughed like a maniac before he finally managed to speak.

“D-didn’t you throw it away because you didn’t need it?”

“I did.”

Until the System came back.

I hadn’t expected the situation to change this much in just a few hours.

*I should’ve kept it for one more day.*

Where was I even supposed to start looking? I sighed heavily.

“Hyung, you didn’t happen to see who took it, did you?”

“Uh… well.”

Jinho hyung scratched his head.

“If I saw it, then I saw it. If I didn’t, then I didn’t.”

Was that even an answer, or just crap?

When I glared at him, he smiled sheepishly.

“Look, it’s not that I want a finder’s fee or anything…”

It definitely sounded like he wanted a finder’s fee.

Anyway, that wasn’t the point. I shot to my feet and asked,

“You saw them? You’re sure?”

“If I have to pick, I saw them.”

“Who? Where did they go?”

“I’m not asking for a finder’s fee, but what’s the expected amount, roughly?”

“…100,000 won?”

“Oh, dear. Maybe I’m getting old. My memory’s a little hazy.”

“For fuck’s sake.”

“Right. It’s hot out, so good luck with that.”

“The finder’s fee is 180,000 won.”[^5]

Apparently satisfied with the amount, Jinho hyung broke into a bright smile.

“Your capsule. I picked it up.”

“…?”

It took me exactly three seconds to understand.

*Have you ever seen a daylight robber like this?*

I was so dumbfounded I couldn’t even breathe. He’d hit me in the back of the head like this?

“But there wasn’t anywhere suitable to put it. My room’s too small, you know.”

“So?”

“I put it back in your room. I did good, right?”

How was I supposed to hit this guy so cleanly that people would say I’d really done it right?

I clenched my fists until they shook.

* * *

“It really is here.”

Seeing the capsule taking up half the studio as if nothing had happened, all I could do was let out a hollow laugh.

*Should I call this lucky?*

Of all the people in the world, Jinho hyung had taken the capsule.

I opened the capsule lid. Then I picked up the user manual, which had been tossed onto the worn seat, and flipped to the last page.

> **Main Features**
>
> - A customized capsule for one person! Once a user is registered, the capsule becomes permanently bound to that user and remains so until their death.

…Come on. No way.

*It has to be a simple coincidence.*

But I couldn’t shake the unease. I stared at the capsule, the source of all these events.

*What even is this thing?*

The reason I’d thrown the capsule into the recycling area that morning was so I could forget everything. My life was already dry enough; I wanted to write it off as one nightmare and keep living my life as I was.

But the situation had changed now.

*Because the System is here.*

The System…

Then something occurred to me. I placed my hand on the surface of the capsule and murmured,

“Item check.”

Ding.

Just as I thought. The corners of my mouth had just begun to rise when—

> **System**
>
> This Item cannot be read.

“…It can’t be read?”

This had never happened before.

*Is it because I’m not in Murim?*

Flustered, I checked every object in the room at random. The television, a ballpoint pen, even the pillow. Every time, the System displayed accurate information.

But there was one exception.

The capsule couldn’t be read.

“Wow. This is driving me nuts.”

Just in case, I picked up the user manual. Same result.

Ding.

> **System**
>
> This Item cannot be read.

I flopped onto the bed. I stared blankly at the old, yellow-stained ceiling and thought.

*What’s going on?*

For now, these were things I couldn’t understand. But one thing was certain.

*I’ve become stronger. Incomparably stronger.*

Power had soaked into every fiber of my body. Internal energy writhed in my dantian.

Synchronization had given me strength. Strength far beyond that of an F-rank Hunter. Strength enough to defeat a C-rank Rare Monster alone.

*Would you like to join the Guild?*

It was the first recruitment offer I’d ever received. But I refused. When someone recognized me, fear had come before joy.

*Can’t blame me.*

I’d endured seven years under the name of F-rank Hunter. A caterpillar that had only ever crawled through the dirt had, one day, grown wings called the System.

Fear was a natural feeling.

*But what if I can keep using this power—keep using the System?*

My heart pounded at the mere thought.

At the same time, the past seven years flashed through my mind. The name F-rank, stamped on me like a brand despite all the insane effort I’d put in. Even the memories from two years ago, when I’d trembled at other people’s contempt, at the guilt and the helplessness.

“Fuck…”

I couldn’t take it anymore. I shot to my feet, burst out of the goshiwon, and flagged down a passing taxi.

“Where would you like to go?”

I already knew the destination.

“Take me to the Bucheon Branch of the Hunter Association.”

A Hunter rank reassessment.

An F-rank Hunter. I’d start by breaking this loathsome shackle that had tormented me for so long.

*Let’s give it a shot.*

As I clenched my fist, the taxi driver said,

“This is a Seoul taxi.”

“Oh.”

[^1]: Bigu pills are traditional fasting pills said to sustain the body without ordinary food.

[^2]: Yukhoe is seasoned Korean raw beef.

[^3]: The Korean words for “talent” and “human disaster” share the same pronunciation, though they use different characters.

[^4]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement.

[^5]: In Korean, *sip-pal* (“eighteen”) echoes the swear he just used, and he switches abruptly to stiff politeness.
## Chapter artifact 47

# Chapter 47

Hunter Association.

The name had appeared some thirty years ago, at the same time the Great Cataclysm ended.

The first-generation Hunters who survived that blood-soaked catastrophe raised their flag, and over the years the Hunter Association grew into an organization of tremendous stature.

Gulp.

I swallowed as I stared up at the Association building standing tall before me. Even in this dense forest of skyscrapers, its size and height stood out. Even on an ordinary weekday, people streamed in and out.

*How many years has it been?*

Every Awakened underwent rank measurement under the Association’s supervision.

I was no different. The thought of twenty-year-old Jin Taekyung walking in here all excited almost made me snort—like hell it did.

*Now that I’m actually here, I’m incredibly nervous.*

I went into the lobby on stiff legs. The place was the size of a sports field and packed with people. I followed the electronic signs posted throughout until I found what I wanted.

**Measurement Waiting Room**

On the clerk’s instructions, I filled out the paperwork and went inside. Dozens of people were waiting to be measured.

Thud.

The door shut, and everyone’s eyes shot into me like arrows.

*Suffocating. This is suffocating.*

Even the air was different here. A taut tension pressed down on the entire waiting room.

*One measurement decides your whole Hunter life.*

I was no different. I’d been so nervous I’d even farted in front of an examiner once. That pretty much said it all.

I was waiting my turn, thinking about this and that, when—

“Jin Taekyung?”

A familiar voice from behind me. I turned my head slowly.

There he was.

“I didn’t think it would be, but it is.”

A middle-aged man with a bulbous nose and a potbelly. A face I couldn’t forget no matter how hard I tried.

*…Team Leader Kim?*

Kim Sangshik. A founding member and team leader of Sopung Guild, where I’d spent years. He could be summed up in one word.

Former boss.

“Wow, I never expected to run into you somewhere like this. Good to see you.”

Team Leader Kim thrust out his hand with a hearty laugh. I hesitated a moment, then took it.

“Likewise. It’s been a while.”

“What do you mean, a while? It’s only been a few days.”

“Those few days felt pretty long to me.”

I’d said it thinking of Murim, but Team Leader Kim would hear something else. After all, he was the one who’d handed me my dismissal only a few days ago.

“It’s because it’s summer. My days have felt long lately too.”

“Really?”

Watching him slide past it like a sly old fox, I let out a hollow laugh.

He was a funny guy, no matter when you saw him.

In more ways than one.

“So what brings you here?”

“I had some business. What about you, Team Leader?”

“Came to scout. Heard there was a decent one this time.”

They’d fired me for staff cuts in a restructuring. And he was here to scout.

“I see.”

That was all I had to say. Everyone knew that tired story, and it was already over. I had no lingering attachment left.

“What about you? Why are you here? Don’t tell me you’re trying to get reassessed.”

“Yes.”

Team Leader Kim spoke with a smile.

“Nice try, but isn’t that a waste of money? A reassessment isn’t cheap. Must be a burden for an F-rank Hunter.”

“Still, I figured I’d try. Just in case.”

“You should save up while you’re young. What’s going to change if you keep clinging to something that isn’t going to work?”

“Who knows? I think this time might be different.”

“It’s not that easy—”

“Team Leader.”

“Huh? What?”

I smiled, gentle.

“That’s enough.”

A crack ran through Team Leader Kim’s smile.

“What?”

“I said that’s enough. I’ve left the Guild now, so stay out of my business.”

“What’s that supposed to mean?”

What did it mean?

“You know what I mean.”

“…”

“It couldn’t be helped. You’re lucky you survived. Forget it all and make a fresh start. You pecked away at me behind my back while pretending to console me.”

“You…”

“Weren’t you the one who first told the Guild Master to cut me? Did you think I wouldn’t know?”

Kim Sangshik was a half-baked, petty little man.

Short on humanity, short on ability.

Even in Gates, he was too busy saving his own skin. His reputation in the Guild was rock-bottom.

“Who did you put in my place after you fired me? How much did you take to slot someone in?”

“Hey. Jin Taekyung.”

Team Leader Kim clamped down on my shoulder and growled. He didn’t look it, but he was one of only three D-rank Hunters in Sopung Guild. With that kind of strength, he could have toyed with an F-rank Hunter like me with one hand.

But—

“Take your hand off.”

I didn’t even blink. It wasn’t only the System that had synchronized. My martial arts, my stats, and even my steel-like Sinews and Bones had come with it.

“I’ll count to three. Take your hand off.”

“You little bastard. I’ve been putting up with you, but—”

I didn’t hesitate.

“One. Two.”

Three.

The instant I grabbed Kim Sangshik’s wrist—

Clack.

“Would the next group please come in. Numbers twenty-one through thirty!”

An Association examiner walked in with a file, and we both let go before the other could. Getting marked by the Association wouldn’t do either of us any good.

“Consider yourself lucky.”

“Who. Me? Or you?”

Kim Sangshik’s flushed face looked downright ridiculous. Even the Level Window I’d picked up through Qi Sense.

> **System**
> Lv. 24 Kim Sangshik

“Meeting you was disgusting. Let’s never see each other again.”

I got up without a shred of regret. My waiting number was thirty. The steps I took toward the examiner weren’t stiff anymore.

* * *

“Number twenty-one. Please come forward.”

An Awakened with a tense face stood in front of the measuring device. Made from an A-rank Magic Gem, it scanned his whole body and converted the mana inside him into numbers.

Bzzzzzt—

The examiner checked the reading and spoke.

“Mana distribution in the body: F-rank.”

The Awakened’s face turned ashen. But it was too soon to despair. He had a second chance.

“Try moving your mana. Concentrate as hard as you can, and imagine firing it into the measuring device.”

They were checking his mana control. Realizing it wasn’t over yet, the Awakened gritted his teeth and drew up his strength.

Every last ounce of it—ngh!

Bwoooom.

“…”

“…”

The examiner spoke with a face that looked ready to vomit.

“Control ability: F-rank.”

“Just once! Let me try one more time!”

“No. Next.”

The line moved fast.

All E-rank or F-rank. One guy wasn’t even Awakened.

“This is a scam! A scam! That measuring device is made in China, isn’t it? Huh? You bastards!”

“Handle him.”

At the examiner’s word, the security Hunters waiting nearby dragged the fraud out. Even if that guy miraculously Awakened, he’d probably end up on the Association’s blacklist.

“Next. Number thirty.”

Here it came.

I took a deep breath and stepped forward. The examiner glanced at the file in his hand.

“This is a reassessment?”

“Yes.”

“Mr. Jin Taekyung, you received F-rank seven years ago… and you know there’s a separate fee for reassessments, right?”

From the way he said it, he might as well have been telling me not to waste my money and to go home while I still could. The usual look people gave an F-rank Hunter.

*Do they think I’m a beggar?*

Familiar was one thing. Still filthy was another. When I glared at him, the examiner gave a short puff of a laugh.

“I’m only mentioning it in case you weren’t aware, but the fee is two million won.”

“…The price went up?”

“It’s been a few years.”

*Fuck. I didn’t know that.*

How much was in my account right now…?

“Then we’ll begin the assessment.”

Nervous, I closed my eyes.

And the next moment—

Bzzzzzt.

A wave of mana rolled out of the measuring device and swept through my whole body.

Fifteen years of internal energy answered it and shuddered.

*What rank will it be?*

C-rank? No, I’d be happy with D-rank. But ten seconds or so passed, and the examiner still didn’t open his mouth.

“Uh… why is it doing this?”

“Why?”

He looked from the device to me, flustered, then cleared his throat.

“There seems to be some kind of error… We’ll move on to the next step for now.”

I had no idea what was going on, but strangely, it didn’t feel ominous.

*This feels good.*

Feeling my heart pound, I drew up my internal energy.

Ssshhh.

At the call of the Jin Family’s Cultivation Technique, fifteen years of internal energy surged up and shot toward the measuring device.

* * *

The lobby entrance.

“Well done.”

Kim Sangshik patted a young man on the shoulder. As of today, he was a promising young D-rank Awakened, officially recognized.

He would soon join Sopung Guild and be assigned to Kim Sangshik’s team. Thinking of that coming day, Kim Sangshik smiled, proud.

“Father and son on the same team. That’s my boy.”

“What are you talking about? I’m not even an official Hunter yet. I still have to go through the training center.”

“Don’t worry. Your father already took care of it.”

“Wait, really? Didn’t you say the Guild didn’t have a spot?”

“There’s always a way.”

He didn’t mention that, in the process, he’d cut the lowest-rank Hunter who’d been a thorn in his eye.

“Anyway, rest up this week, and starting next week we’ll commute together—”

Kim Sangshik’s face suddenly twisted.

“What’s wrong?”

“…Nothing. Go wait in the car.”

After his son left, he was alone. He rolled up his shirtsleeve.

His wrist had already swollen a dark blue-green. The sight made him grind his teeth.

“Jin Taekyung, you fucking bastard.”

He’d disliked that bastard from the start. An F-rank Hunter as deputy team leader, and the way he’d been like brothers with the old team leader, who was dead now.

*That bastard should’ve fucking died with him back then.*

The unfortunate accident two years ago had been a stroke of luck for Kim Sangshik.

After being sidelined by various sex scandals, he’d made a triumphant return as team leader. A few days ago, he’d even gotten Jin Taekyung thrown out.

*But was this bastard really a reawakening?*

Kim Sangshik stared down at his throbbing wrist.

It had only lasted an instant, but the strength he’d felt then had been tremendous. Taekyung might have reawakened as E-rank—or even D-rank.

“No. Reawakening isn’t child’s play.”

Maybe he’d gotten weaker from not exercising lately. Kim Sangshik was muttering, mixed up inside, when—

“We have breaking news from the measurement room.”

“Someone good?”

“They say a big fish surfaced. C-rank.”

“C-rank? Not bad, but that’s not enough to call a big fish, is it?”

“But they say his mana control is A-rank.”

“What? A-rank! Get a straw in him, now!”

“Yes. This is Choi Min-su from Sangdong Guild. The thing is—”

A stir spread through the scouts prowling the lobby entrance like hyenas.

Most of them had been sent by small and midsized Guilds, but a few from the major ones were already moving fast.

*C-rank alone is impressive, and he’s gifted with mana control on top of it?*

This was a jackpot.

Kim Sangshik’s mind snapped clear. He shoved every thought of Jin Taekyung far away and pulled out his phone.

—Hey, Team Leader Kim. Did that business go well?

The deep voice on the other end belonged to Sopung Guild’s Guild Master.

Kim Sangshik spoke in a rush.

“Guild Master, it’s chaos here. A C-rank just showed up. And they say his mana control is at the level of a high-ranking Hunter.”

—What? Where did a guy like that come from?

“Exactly. The major Guilds always snatch them up midway, but it looks like they were a step late this time.”

—Good. So that’s how it is…

Huff. Huff.

Rough breaths came through the phone, as if he was excited. Even the way he addressed Kim Sangshik changed.

—Sangshik. You hold on to this guy no matter what. Tell him we’ll meet whatever conditions he wants.

“How high can we go on the money?”

—Don’t worry about it. Pile plenty on top of whatever the others offer. The major Guilds will drop out if they decide it isn’t profitable enough. It’s not like they need him.

“Yes, yes.”

—I’m on my way. Keep hold of him until I get there. If we pull this off… you know what that means, right?

After hanging up, Kim Sangshik clenched his fist.

*We’ve got this!*

He’d been worn smooth by years in this business. Holding on to a newly Awakened rookie was nothing.

This was a world where money could put even ghosts to work.

*Twice what everyone else offers. I’ll quote double, no matter what.*

The commotion grew louder. The elevator that had stopped on the third floor, where the measurement room was, was coming down toward the lobby.

“He’s coming!”

“Hey, stop shoving.”

About twenty scouts clung to the entrance like a swarm of ants. Kim Sangshik had muscled his way into the lead and was ready to hand over his card.

Ding.

At last, the elevator doors opened.

Kim Sangshik bowed low and launched into the words he’d prepared.

“Hello. I’m Team Leader Kim Sangshik of Sopung Guild. We’re a prestigious Guild with a long tradition here in Bucheon—”

“This is the first time I’ve heard anyone call Sopung a prestigious Guild.”

“…What?”

The familiar voice made Kim Sangshik lift his head, gingerly.

Their eyes met.

At the same time, Kim Sangshik’s buttonhole-sized eyes went wide.

“You, you…”

Jin Taekyung grinned.

“We meet again, Mr. Kim Sangshik.”
## Chapter artifact 48

# Chapter 48

“Y-you? What are you doing there?”

“Good question. What am I doing here?”

“Then, could it be…?”

“What do you mean, ‘could it be’? It is.”

Kim Sangshik’s face went dark and sallow, like a man with shit poisoning.

Seeing him like that felt like ten years of constipation finally letting go. Ah. So this was a shitgasm.

“Anyway, let’s take a step back. We’re not the only ones here, you know.”

I took a step forward, and Kim Sangshik backed away weakly.

The other scouts surrounded me with business cards in hand.

“Sangdong Guild. We promise the best possible treatment.”

“Instead of doing this here, why don’t we move somewhere private and talk…”

Recruitment offers poured in from every direction. In no time at all, dozens of business cards were in my hands.

*So this is what it feels like.*

It was a novel, peculiar feeling. Things I hadn’t experienced even once in seven years were unfolding right in front of me.

In a mere half day, the world around me had changed.

No.

*I’m the one who changed.*

People said that in this business, C-rank was where you started being a real Hunter. Exceptional ability, a high salary, and society’s recognition as a mid-level Hunter.

At last, it sank in that I had stepped onto that path.

*And…*

This was only the beginning.

With the System’s power, I could keep growing.

That was how I would step onto a new path faster than any other Hunter.

“Sir, if you have any conditions you want, we’ll meet them no matter what.”

“Ah, yes. I’ll get in touch later.”

“You really will, right? We’ll be waiting!”

No. Don’t wait. I’m not going to call.

“All right, everyone, calm down.”

Association security guards stepped in and blocked the scouts who kept clinging to me.

They didn’t usually go that far for a C-rank Hunter. I was just such a rare case that I seemed to be drawing a lot of attention.

*Well, I did jump that far from a single reawakening.*

It wasn’t a bad feeling. No—it felt good.

I fought down a smile that kept trying to break out and left the Association. Even then, one person still followed me.

“Jin Taekyung! No, Mr. Taekyung!”

“Heh.”

I looked at Kim Sangshik and swallowed a hollow laugh.

Only thirty minutes ago, he’d been calling me a bastard. Now I was suddenly *Mr. Taekyung*.

“What do you want?”

“I’m sorry about earlier. Really. And I’m sorry about everything from before, too.”

Kim Sangshik rambled, spilling out every wrong he’d done to me in the past. When that untimely confession was over, he finally got to the point.

“So let’s forget all of it and treat this as business.”

“Business.”

I rolled the word around on my tongue.

It sounded good. The feeling was terrible. Even more so because the business partner was Kim Sangshik and Sopung Guild.

“You already know this, Mr. Taekyung. Unless it’s a major Guild, they’re all more or less the same.”

“I know. I also know that once you’re C-rank, even the major Guilds will reach out.”

“I’m telling you to think it through. They won’t be hurting for you. That’s the kind of place where a C-rank Hunter isn’t hard to find. The treatment will be exactly that level, too.”

Kim Sangshik kept going, spraying spit as he talked.

“No matter what they offer, we’ll add more on top. The Guild Master already signed off on that, so you can count on it.”

Sopung Guild had been in steady decline for several years.

Given the situation, the Guild Master seemed scared shitless.

*This guy’s no different.*

The Guild’s opinion of him was already at rock bottom, and now the F-rank Hunter he’d fired on a whim a few days ago had reawakened as C-rank.

I found myself smiling at the thought of what would happen when the Guild Master, notorious for his temper, found out.

“Just look at it positively. Actually, forget standing around here. Why don’t we go somewhere decent and talk it out honestly? The Guild Master is on his way here right—”

“Mr. Kim Sangshik.”

At my quiet voice, Sangshik shut his mouth.

“If you want to recruit me, tell the Guild Master this. Don’t leave out a single word.”

“Tell him what?”

“I’ll think about it if he gets rid of one man I can’t stand the sight of.”

It was obvious who I meant.

Leaving Kim Sangshik behind with his face twisted in fury, I got into a taxi.

*Yeah. This should do it.*

I sank back into the soft seat.

The rank reassessment. Running into old bad blood. An indescribable rush, and at the same time a sense of relief.

“Where would you like to go?”

“Huimang Goshiwon at Songnae Station.”[^1]

The taxi driver looked at me and chuckled.

“Oh, you’re that passenger from earlier.”

“Ah.”

*Goddamn Seoul taxis.*

* * *

“What’s gotten into you? You actually bought beef.”

We laid out a mat and a grill on the goshiwon roof. Jinho hyung gazed happily at the meat as it cooked.

“All right. Seeing your sincerity, I’ll forget about the finder’s fee.”

“I wasn’t planning to give you one.”

“Are you a punk?”

“Right back at you.”

We sat across from each other and tilted our soju glasses.

“But where did you get the money? You were whining that even this month was going to be tough.”

“Today’s pay.”

“How much could that be? Did you give up on life after getting fired from the Guild?”

“How much?”

I couldn’t help letting out a little laugh.

“Oh, you’re laughing?”

“I should laugh. You’re treating ten million won like pocket change.”

Jinho hyung froze.

“How much?”

“Ten million won.”

“You made ten million won in one day’s pay?”

“A little more came in, but that’s for now.”

“You didn’t…”

Jinho hyung swallowed hard. He caught on fast. I gave him a meaningful smile.

“That’s right. Today I—”

“Did you sell an organ?”

Should I kill him?

I let out a long sigh, then downed my drink.

“Tell me the truth. As the goshiwon manager, I have a duty to know.”

If you only heard that, you’d think he was the prime minister, not a goshiwon manager.[^2]

“I made it at a Gate.”

“Bring me proof. I only believe what I see with my own eyes.”

“Suit yourself. Here.”

I handed him my phone. It was the message I’d gotten on the way back from the Association after the reassessment.

The sender was…

“Luxury Nutjob? Who’s that?”

“The Team Leader I ran the raid with today.”

“He must be rich. I want to become sworn brothers with him.”

This guy and I really did think alike.

A moment later, Jinho hyung finished the message and his eyes went wide.

“10.3 million won? Am I reading this right?”

“Probably.”

According to the contract, the payment was supposed to be 300,000 won. Team Leader Choi had added another ten million.

*And there’s still a balance left.*

The Hobgoblin Priest and Great Warrior had been C-rank Rare Monsters. Team Leader Choi had added that he was looking for buyers for their equipment, leather, and Magic Gems.

> “We’ll make an additional payment as soon as they’re sold.”

When I came to, I found myself in a nearby supermarket, grabbing every piece of beef I could get my hands on.

“You…”

Jinho hyung stared blankly, looking from me to the phone in my hand.

“Where the hell have you been, and what did you do?”

“It’s a long story.”

Jinho hyung chuckled and gripped the scissors.

“And your lifespan is short?”

Where was I even supposed to start?

I had decided not to say anything more about the capsule.

I figured it was better if, for Jinho hyung, it just stayed an absurd lie.

“Two Rare Monsters showed up at the Gate today, and…”

At a life-or-death moment, the luck of a reawakening had come, and I’d been able to take them down. Then I told him about the Association.

It was a story hastily stitched together, but Jinho hyung bought it.

“So now you’re a C-rank Hunter?”

“The reassessment procedure will take a few days, so technically, not yet.”

“Same thing, you idiot.”

His face was dazed, his voice hoarse.

Jinho hyung stared at me for a long moment. Moisture gathered in his eyes.

*What’s gotten into this guy?*

“…Don’t tell me you’re crying?”

“The fuck I am. What kind of bullshit is that?”

He turned away with an unnecessary curse, but he couldn’t hide the single tear that slipped down. I watched him out of the corner of my eye as he roughly rubbed his face with his sleeve.

“Hyung?”

“Turn the meat over. It’s burning.”

“Changing the subject?”

“I said it’s burning!”

“Ah, all right.”

Sizzle.

As I turned the meat, I felt flustered, and yet a corner of my chest tickled.

*Come to think of it, I’ve known Jinho hyung for a long time.*

Six years? Seven? I didn’t know. I’d never counted. Whenever I came back to the goshiwon after a hard day, he had always been there.

Sometimes I wondered if this was what it would have felt like to have a real older brother. We had lived like brothers, like friends.

“Hey.”

Jinho hyung broke the awkward silence. I turned the meat over one more time for no reason.

“Yeah? What?”

“Good for you.”

“…Yeah.”

“And…”

His quiet voice followed.

“You worked hard.”

At just those words, something surged up from deep inside me. The emotions and memories that had stacked up over the past seven years all came rushing in at once.

“Congratulations on becoming a C-rank Hunter. I guess I can’t tease you anymore.”

“Hyung…”

“Taekyung…”

“Hyung!”

“Taekyung!”

We hugged each other tightly across the grill. Jinho hyung whispered in my ear, his voice shaking.

“Do you remember what I said earlier?”

“I know how you feel, hyung. Thank you.”

“That’s not what I meant. The finder’s fee.”

“…What?”

“You have to pay the finder’s fee. Hyung’s having a hard time these days.”

“…”

“You make a lot of money now.”

Should I really kill him?

* * *

I staggered back to my room and threw myself onto the bed.

I let out a little laugh, thinking of the one person who was probably cleaning up the roof while grumbling.

*You really can’t let your guard down around him.*

That was Jinho hyung. The way he congratulated me, and that last prank.

I knew all of it was just his way of showing it.

*You worked hard.*

Those words kept circling in my head. It was embarrassing to admit, but for a moment there, I had almost cried.

*Yeah. I really did work hard.*

After my father died, I had run nonstop. I graduated high school while working part-time jobs, and I had to hold on and keep holding on for my sick mother and little sister.

At some point, all of it had become a given.

And then.

Ding.

> **System**
>
> - You have been afflicted with a Status Effect: Dead Drunk.
> - It can be detoxified by circulating your qi.

*Something that wasn’t a given had entered my life.*

It had all started with that unidentified junk game capsule.

“A game capsule, huh?”

I didn’t even know what to call the thing anymore. It had made me a C-rank Hunter, so should I call it a gift from God?

No. Maybe it was a gift from the devil.

*Is this really okay?*

The reason I was thinking this even after the best day of my life was simple.

*Nothing comes for free.*

That was the world I knew. Everything had a price tag. Visible or not, sooner or later you had to pay.

*How expensive is the System?*

A hundred billion? A quadrillion? Maybe even more?

I laughed weakly and felt my eyelids growing heavy.

*Oh, right. I was dead drunk.*

Chirp. Chirp-chirp.

Outside the window, the grass insects were crying loudly. My vision darkened, and sleep poured over me.

That night, I dreamed.

I dreamed that somewhere deep in the mountains, someone was shaking me awake.

“Squad leader, squad leader!”

Weirdly, just hearing it made me want to punch whoever it belonged to. Part of me wanted to see who that familiar voice belonged to, but I was too sleepy to open my eyes.

“What do we do?”

“We have to tell the main force right away…”

“Why is the squad leader suddenly like this now of all times…”

It felt like listening to a broken radio. The voices had static in them, and they kept cutting out.

*I’m sleepy…*

As my consciousness drifted farther away, I heard a small but clear voice.

“Youngest, survive.”

But when I woke the next day, I couldn’t remember any of it.

[^1]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement.
[^2]: A pun: the Korean word for a goshiwon manager sounds like “prime minister.”
## Chapter artifact 49

# Chapter 49

Early morning.

I eased my eyes open.

Ding.

> **System**
>
> Exiting Sleep Mode.

The System notification came with a sigh of relief.

“Phew.”

Thank goodness. It hadn’t all been a dream.

It had only been one day, but yesterday was the day my life changed. If I’d opened my eyes as Jin Taekyung, F-rank Hunter, reality would have felt like a nightmare.

I rustled my way up—and that was when it hit.

> **System**
>
> Afflicted with the status ailment Hangover.

“Urgh.”

Last night’s aftermath was no joke. I clutched my spinning head and sat cross-legged on the mattress.

The System had told me circulating qi could detoxify, too.

> **System**
>
> Beginning Qi Circulation.

Following the formula of the Jin Family’s Cultivation Technique, I guided my internal energy. The moment I started circulating qi, the headache began to fade. After about ten minutes, the message I’d been waiting for appeared.

> **System**
>
> Hangover disappears.

But I didn’t stop. I knew that wrapping it up halfway through would tank the efficiency.

*Experience from Murim.*

I didn’t uncross my legs until a full hour had passed. My head was clear, and my body was bursting with energy.

The problem was…

*Why is so little energy coming in?*

Internal energy only increased if you took in qi from outside, stored it, and circulated it. But my first circulation in reality brought in strangely little.

*And it’s murky, too.*

It was like a tiny serving of bland food—and even that took forever to arrive. I frowned.

*Environmental pollution, maybe?*

Internal energy was based on pure natural qi, so it was possible. Compared to Murim, the natural environment of modern society was in pretty dire shape.

*Or maybe the location is the problem.*

A one-room in a goshiwon[^1] built decades ago was hardly a nature-friendly place. It stank, and the facilities were old.

Jinho hyung was always suspicious of what this place really was, and he was the goshiwon manager.

*Maybe it used to be a torture chamber. During the Great Cataclysm they probably dragged monsters in, tapped their balls with a knife, and asked where the Demon King was. The monsters would’ve given up his parents’ location, too.*

…You had to give him credit for his imagination.

*He should be sleeping by now, right?*

He treated getting up in the morning as a disgrace, so there was no need to check. I was wondering whether to go grab breakfast when—

Bzzzt.

A text arrived on my phone.

〈 Luxury Junkie

Luxury Junkie

Do you have some time?

The sender was Luxury Junkie—or rather, Team Leader Choi.

* * *

A glittering chandelier. Stylishly dressed people, and soft classical music in the background.

I couldn’t tell if the meeting place was a café or a high-end restaurant.

“May I take your order?”

*Shit. Even the waiter here looks like a celebrity.*

Model proportions, and a face like a handsome Greek god.

*Is this how everyone turns gay?*

While I was having an identity crisis, Team Leader Choi calmly started ordering.

“One Black Ivory, please. What about you, Mr. Taekyung?”

The Greek god turned toward me.

Something about the vibe said I shouldn’t order a caramel macchiato.

“I’ll have the same.”

The coffee that came out a little later was pretty decent.

“It’s good. This is Black… what was it?”

“Black Ivory.”

Even after hearing it, I still had no idea what that meant. I just went, well, okay then.

I muttered my honest take.

“It looks expensive. Do they use good beans?”

“It’s elephant dung.”

“Oh.”

I quietly set down my cup. Team Leader Choi chuckled, then spoke.

“Congratulations.”

It came out of nowhere, but I knew what he meant right away.

He was talking about yesterday’s rank reassessment.

“You’re fast. It’s personal information—the Association wouldn’t have opened all of it.”

“C-rank reawakened Hunters are rare. Besides, I saw what happened yesterday with my own eyes. There was no way I wouldn’t know.”

That was true.

As I granted him that, Team Leader Choi held something out. A single envelope, laid neatly on the table.

“What is this?”

“You’ll know when you look.”

*Don’t tell me—money?*

I checked the contents. Instead of a check, tiny printed letters packed the page.

“It’s a contract.”

“The best terms our Guild can offer. Give it a read.”

I was already reading it. From the first line to the last. Every clause was another shock.

“This doesn’t look like a C-rank contract.”

After about seven years knocking around this business, I’d seen plenty, and overheard plenty more.

Even I had never seen a contract this generous.

“They’re good terms even among B-rank contracts.”

“Then why are you offering this to me…?”

“Because they trust me.”

“What?”

“They trust my instincts, and they trust my eye for people. That’s why I want to hold on to Jin Taekyung.”

Team Leader Choi set down his empty cup.

“Will you sign?”

Honestly, I was wavering. A lot.

It wasn’t only the terms. Someone had recognized me and wanted me this badly. I wanted to nod right then.

That was why today’s hesitation ran longer than yesterday’s. By the time I finally decided, the coffee had gone cold.

“I’m sorry.”

The reason was the same as yesterday.

According to the contract, I would have to work as an affiliated Hunter for at least one year.

I was grateful for the offer, but… I couldn’t rush this.

“Have you already signed with someone else? Or are you planning to?”

“No. I just need more time.”

“Time.”

Team Leader Choi sighed.

“I suppose it can’t be helped.”

I was about to apologize again when he said,

“This is my second offer.”

“Pardon?”

Another envelope came out of Team Leader Choi’s jacket. Still dazed, I took it and checked the contents.

“A provisional contract?”

“You have a rough idea of what that is, right?”

I did. I knew it well.

If the Manpower Office was day labor, a provisional contract with a Guild was temp work. You’d be attached to the Guild for a short stretch, basically a mercenary.

“You won’t turn this one down too, will you?”

It was less generous than the formal contract he’d given me, but it was still more than generous enough. And the part that mattered most to me—the contract period—was a blank.

“Write down whatever period you want.”

“Oh. Right.”

I took the pen he held out, half in a daze.

After thinking it over, I wrote seven days. A week should be enough time to see whether the System would last.

Once I’d signed, Team Leader Choi held out his hand.

“I look forward to working with you.”

“That’s my line.”

When we shook hands firmly, it sank in that I’d taken my first step as a C-rank Hunter.

*Even if it’s only a provisional contract.*

My chest swelled.

“Should I come in tomorrow?”

“No.”

Team Leader Choi tapped his watch.

“Starting now.”

* * *

Vroom.

Team Leader Choi’s car was a large military vehicle. He looked like the type to collect expensive supercars, so this was unexpected. I only understood why after we arrived at the Gate.

“Pick something.”

“Pick what?”

“Equipment.”

Team Leader Choi pressed a small button, and a trunk large enough for five grown men to lie down in appeared.

“I had it modified for work. Leaving all this at home felt kind of off.”

I stared into the trunk with my mouth hanging open.

*Holy crap.*

Gear worth at least several million won was stacked and sorted. Armor and weapons were a given. Potions of every kind, even disposable magic scrolls people said were too expensive to actually use. He had everything.

“…Is all this yours, Team Leader?”

“For now. Some of it was gifts, and some I bought because it looked nice.”

Ah. So he buys gear because it looks nice.

*How rich do you have to be to think like that?*

C-rank Hunters made good money, but Team Leader Choi’s spending was already beyond that. He must have been rich enough that money was never a concern.

Gulp.

“It might be better to rent from a rental shop. If I borrow something and it gets wrecked, it’d be kind of…”

“They’re out of fashion, so it doesn’t matter.”

Ah. So he even cares whether gear is in fashion.

I gave up thinking about it around there and picked my equipment.

Having the System made it easy.

*Item check.*

Ding.

> **System**
>
> Item Window
>
> Lizardman Hunter’s Leather Set
>
> Type: Armor
>
> **Grade:** First Rate
>
> Restriction: None
>
> Description: Made by stripping off a lizardman’s hide in one piece.
>
> Scale Armor activates when the full set is equipped.

*This is pretty good.*

It was light, and the leather was tough and hard.

Once I had everything on, the set effect Scale Armor activated.

“Oh.”

Green scales rose from the leather and covered my whole body in a tight layer. Team Leader Choi nodded at the sight of me.

“You picked a good one. You’ve got a good eye.”

*It’s the System that’s good.*

I smiled awkwardly and rummaged through the weapons. Come to think of it, I’d only ever seen this guy use a sword, but the trunk alone had more than five kinds of weapons.

*And they’ve got wear on them, too.*

You could see the traces of him trying to find what suited him.

A little later, I had a spear in my hand.

> **System**
>
> Item Window
>
> Lizardman Slayer’s Harpoon
>
> Type: Weapon
>
> **Grade:** First Rate
>
> Restriction: None
>
> Description: Upon a successful attack, Bleeding activates with a high probability.

Anyone watching would think I had a lizardman fetish.

With the spear as the last piece, I was done choosing. Team Leader Choi chuckled.

“What’s so funny?”

“I was thinking things are going well.”

“Pardon?”

“You’ll find out soon enough.”

I had no idea what he meant, but I followed him to the front of the Gate. Instead of an Administration staffer, some man was standing there.

“You’ve arrived.”

A perfectly proper ninety-degree bow. Even more surprising was the way Team Leader Choi took it as natural.

“How’s the Gate?”

“Yes. I received your call yesterday and restricted access.”

“Thanks for your hard work.”

“Not at all, young master.”

*Young master?*

The term was an honorific for an unmarried younger brother-in-law, but there was no way that man was Team Leader Choi’s sister-in-law…

*Team Leader Choi. So he was a rich family’s young master.*

No wonder.

I should have known from the moment I saw him dripping in luxury gear from head to toe.

Add being a fashion person who even cared about equipment design, and you couldn’t pull that off unless you were one hell of a gold spoon.

*That guy has everything.*

The guy who had everything turned to me.

“All right. Let’s go in.”

“Right now?”

“The equipment’s taken care of. Is there a problem?”

His tone made it sound so obvious that I looked around.

Me, Team Leader Choi, and some middle-aged guy I didn’t know. That was everyone.

“What about the other team members?”

“They’re right here. The team members.”

“Oh, I see. He’s going in too, right?”

The middle-aged man cut in, his voice heavy.

“I’m not.”

“Then…?”

“It’s just the two of us. There’s no one else.”

Team Leader Choi’s words left me slack-jawed.

“No one else?”

“No.”

“Not even one person?”

“We’re not bringing so much as a dog.”

Look at how decisive he was. Who was he, Pocheongcheon?[^2]

“So the two of us are running the Gate alone?”

“Why couldn’t we? It’s only a D-rank Gate.”

“This is my first D-rank Gate.”

“I’ve been to plenty.”

No, fuck…

A D-rank Gate wasn’t some neighborhood discount mart.

“If it’s just the two of us, I’m backing out.”

A safe raid on a D-rank Gate needed a team of ten Hunters of the same rank. I could use the System, and I’d learned martial arts, but that didn’t make the danger go away.

“I know what you’re thinking, Mr. Jin Taekyung. But let me tell you one thing.”

Team Leader Choi went on in a relaxed voice.

“I’m a reawakened Hunter, too.”

“Reawakened? I thought you were C-rank, Team Leader…”

“C-rank was the rank I received when I was first measured. The reawakening happened afterward.”

Meaning he was at least B-rank in ability.

The odds were slim, but he could be even higher than that.

*A B-rank Hunter.*

If that was true, the situation changed. Just the two of us also meant a bigger cut for me.

“If you want to go back, I won’t stop you. I can go in alone. It wouldn’t be the first time, or the second.”

He walked in and out of D-rank Gates alone on the regular?

“Then be careful in there. From tomorrow, we’ll look at E-rank.”

That was the deciding blow.

I grabbed his shoulder as he turned away.

“Team Leader Choi.”

“Yes?”

“I want to… raid.”

Team Leader Choi smiled warmly.

“Let’s do our best.”

[^1]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement.
[^2]: Pocheongcheon is a famously incorruptible judge in Chinese legend and popular storytelling.
