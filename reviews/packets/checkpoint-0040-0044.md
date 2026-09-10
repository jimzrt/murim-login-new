# Checkpoint Review — 40–44

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

# Chapters 40–44

## Plot

Taekyung wakes in reality after dreaming of the Jin Family’s battle. Seong Jinho cannot see the Ark - 2020 manual’s text, confirming that its contents are visible only to Taekyung. Taekyung tests a popular virtual-reality game, but its artificial NPCs and sensations cannot compare with Murim. After speaking with his sister Hayeon and thinking of his mother, he accepts that he has returned home and decides to live with his family. He discards the capsule and leaves for work; Jinho, still skeptical but curious, begins investigating H Soft.

Taekyung returns to Hunter work after Sopung Guild fires him. His old acquaintance Im Kkeokjeong, now the E-rank Hunter Im Hyeokjun, recommends him to Team Leader Choi of the newly formed Peace Guild. Taekyung joins an E-rank Gate as a porter. Inside, Choi and the veteran Hunters defeat a Hobgoblin group, while Taekyung efficiently processes the corpses.

In the Boss Zone, an old Hobgoblin Priest uses nearly one hundred corpses to restore a stone gate, trap the party, and summon a C-rank Hobgoblin Great Warrior. The Great Warrior overwhelms Im and the other veterans, leaving them unconscious. Taekyung lures it away, then returns to protect them and blocks its greatsword. This triggers Character Synchronization in reality: “Synchronization complete” and “All systems are inherited.” The System identifies the monster as Level 45. Taekyung reverses the fight with his spear. Choi kills the Hobgoblin Priest, then watches in disbelief as the supposedly F-rank porter severely maims the Great Warrior.

## Continuity

- Taekyung is back in reality, officially an F-rank Hunter and working as a porter for Peace Guild.
- Character Synchronization has restored all of Taekyung’s systems in reality, though the consequences and limits of this restoration are unknown.
- Im Kkeokjeong/Im Hyeokjun and the other veteran E-rank Hunters are unconscious but alive in the Boss Zone.
- Team Leader Choi is a C-rank Hunter, Peace Guild’s leader for this raid, and an equipment-focused fighter who uses a sword and wind-based Haste magic.
- Peace Guild is newly formed and has only three members, including its Guild Master.
- The Hobgoblin Priest is dead. The Level 45 Hobgoblin Great Warrior has been severely wounded, but its final fate and whether Taekyung can defeat it remain unresolved.
- The party remains inside the Boss Zone; the stone gate and route out have not been resolved.
- The Ark - 2020 capsule’s purpose, H Soft’s connection to it, Character Synchronization’s full scope, and any route back to Murim remain unexplained. The manual’s permanent user binding and adjustable time ratio remain binding facts.
- Murim’s death and resurrection limits remain unknown.
- The Head Elder’s Sound Transmission accomplice and the wider plan against the Jin Family remain unresolved.

## Translation Decisions

- Preserve **Ark - 2020**, **H Soft**, **Character Synchronization**, **Synchronization complete**, and **All systems are inherited** exactly.
- Use **Hunter Manpower Office**, **Peace Guild**, **E-rank**, **F-rank**, **porter**, **Gate**, **Boss Zone**, **Hobgoblin Priest**, and **Hobgoblin Great Warrior** consistently.
- Keep **Level 45** for the System level and **rank** for Hunter classifications.
- Use **Im Kkeokjeong/Im Hyeokjun** consistently; retain **hyung** for his informal address.
- Preserve Taekyung’s dry, self-mocking modern voice, blunt sibling banter, and brisk dark action-comedy.
- Render **gukbap** with a first-use footnote as Korean soup served with rice.

## Durable state

{
  "version": 1,
  "safe_through": 44,
  "continuity_sources": [43, 44],
  "active_continuity": [
    "Jin Taekyung is back in reality after logging out of Murim. He is an F-rank Hunter and works as a porter for an E-rank Gate.",
    "Taekyung is the disgraced third son of the Jin Family of Taiyuan and narrates with dry, self-mocking, occasionally profane humor.",
    "The Ark - 2020 capsule's purpose and route to Murim remain unresolved; its manual says users are bound until death, time runs at an adjustable slow ratio, and Character Synchronization exists.",
    "Murim's death and resurrection limits remain unresolved.",
    "The identity of the Head Elder's Sound Transmission accomplice and the full purpose of their plan remain unresolved.",
    "Im Kkeokjeong is Taekyung's old acquaintance, now E-rank Hunter Im Hyeokjun. He is a veteran Peace Guild member, calls Taekyung his little brother, and serves as a main tank with a tower shield and mace.",
    "Peace Guild is new and has only three people including its Guild Master. Taekyung's E-rank Gate party consists of Team Leader Choi, Im, two other veteran E-rank Hunters, and Taekyung as porter.",
    "Team Leader Choi is a C-rank Hunter who leads the Gate party, uses expensive equipment, and fights with a sword and wind-based Haste magic.",
    "Taekyung can butcher Hobgoblin corpses at professional speed and has done this as paid raid work for years.",
    "The Boss Zone contains an old Hobgoblin Priest and a Level 45 Hobgoblin Great Warrior summoned from nearly a hundred dead Hobgoblins.",
    "The Hobgoblin Great Warrior knocks Im Kkeokjeong and the other veteran Hunters unconscious; Taekyung lures it away and blocks its greatsword.",
    "Character Synchronization completes in reality, all systems are inherited, and Taekyung can fight the Great Warrior with his spear despite his official F-rank status.",
    "Team Leader Choi kills the Hobgoblin Priest and witnesses Taekyung severely wound the Great Warrior.",
    "The Great Warrior's final fate and the consequences of Taekyung's restored systems remain unresolved."
  ],
  "open_questions": [
    "The capsule's purpose and route home remain unresolved.",
    "The limits of Murim's death and resurrection rules remain unresolved.",
    "The identity of the Head Elder's Sound Transmission accomplice and the full purpose of their plan remain unresolved.",
    "Whether Taekyung can defeat the Hobgoblin Great Warrior and what happens to the trapped party remains unresolved."
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
    "Preserve the exact System notifications “Synchronization complete” and “All systems are inherited.”"
  ]
}

## Reading copies

## Chapter artifact 40

# Chapter 40

I was flying through the sky. Enormous wings spread, I cut through the wind.

Far below, a high, steep gorge came into view. Shaped like a bottle gourd, it held people—hundreds of them, at a rough count.

A man standing at the center shouted at the top of his lungs.

“Don’t fight for the Jin Family of Taiyuan!”

Then the ground shook. Trees trembled, and mountain birds took flight.

I glanced over my shoulder. A huge cloud of dust was sweeping through the gorge toward us.

“Fight for yourselves! Fight for the flesh and blood and loved ones who will be trampled by the enemy!”

He drew his sword and roared.

“Stand and face them like martial artists! I will do the same!”

Hundreds of weapons were drawn in unison. The man strode forward and took the lead. The cloud of dust crossing the gorge scattered, revealing countless people.

— Waaaaah!

— Wipe out those Jin Family bastards!

The man suddenly looked up. When he spotted me, he grinned.

“I’ve got a good feeling about this.”

The moment I saw his face, the strength drained from my wings. I plunged into the depths of consciousness.

* * *

“Pwah, pwah-pwah!”

I flailed desperately with my wings—or rather, my arms—before it hit me.

*It was a dream.*

Thank god. I thought I was a goner. Only after catching my breath did the situation in the room come into focus.

— This is a breaking news report. A new Gate has appeared at Exit 3 of Hapjeong Station. Mana measurements have confirmed it as a C-rank Gate, and…

A small TV sat on the desk, showing an announcer. And then there was—

“What the hell was that?”

Jinho hyung. He held a pot lid in one hand and chopsticks in the other, staring at me like I was out of my mind.

“Some kind of performance art?”

“Shut up. I was dreaming.”

“About swimming?”

“About falling.”

“Good for you. You’ll grow taller.”

He tossed out the line with zero soul and slurped up his noodles, looking completely at home. For a moment I wondered if this was even my room.

“This is my room, right?”

“Probably.”

“Then why are you here?”

“What, has it only been a day or two?”

That actually sounded plausible. I almost bought it.

“Turn the TV off or something. People are sleeping.”

“Some inconsiderate bastard even hits people in the uvula while they’re sleeping.”

“…”

Anyway, that bastard had one hell of a mouth on him.

“If you’ve got nothing to say, eat some ramen. I boiled five packs because I thought you might wake up.”

Talk about foresight. I took the chopsticks from him, a wave of feeling hitting me.

Was this ordinary ramen? This was ramen I was eating for the first time in a month.

The smell that pulled at my appetite. Noodles cooked just right. Broth boiled spicy with separately sliced Cheongyang peppers.

*Insane. This is insane.*

Slurp.

By the time I came to, it was all over. Jinho hyung stared blankly at me as I licked the pot clean.

“I thought you were filming a commercial. Have you never eaten ramen in your life?”

“It’s my first ramen since I came back.”

“Are you still on that?”

“Try eating nothing but Chinese food for a month, then have some ramen. Michelin’s got nothing on this.”

“Stop. It’s not funny anymore.”

He looked thoroughly fed up. But this time, I had something to back me up.

“Look this over, then we’ll talk again.”

“What is this?”

“What do you think? A product user manual.”

“…”

“Don’t tell me…”

“Yeah. It was inside that capsule. Read it.”

“You stuck this in a piece of junk more than twenty years old before throwing it away?”

Jinho hyung tilted his head, then started reading. A few seconds later, he looked up.

“This is a misprint. The date of manufacture is January 1, 2020.”

I’d thought the same thing at first. At first.

“That might not be a printing error.”

“Huh?”

“No, never mind—that’s still just a guess. What about the rest? The model name and manufacturer listed there. Have you heard of them?”

Jinho hyung was crazy about electronics, especially capsules.

On the related sites, he was a named user people recognized on sight. He’d even run an IT blog.

But the answer that came out immediately sent my expectations crashing down.

“No.”

Well, that was only natural. Even an internet search hadn’t turned anything up. Still, I couldn’t help feeling a little disappointed.

“You really don’t know? You know this field inside out.”

“Yeah. But I don’t know this.”

Jinho hyung scratched his head.

“An illegally modded capsule? Or a custom job? Honestly, I’ve never seen a design like that.”

The more he talked, the bleaker it got.

“Fine, I’ll grant you the design. But I know every model from the earliest ones to the latest. Everything that’s ever been released in Korea.”

“And?”

“The model name written here. The manufacturer. Complete strangers.”

“Couldn’t it be an overseas manufacturer?”

“Oh, you hopeless idiot. You dumbass. You moron.”

Jinho hyung thrust the manual at me, looking thoroughly exasperated.

“Read the first line.”

“Product User Manual?”

“Exactly. It’s in Korean. Korean!”

“Oh.”

“Whether H Soft is a domestic manufacturer or an overseas one, if they went as far as making the user manual in Korean, there’s no way I wouldn’t know them. It’s not like there are hundreds or thousands of capsule manufacturers in this business.”

I felt like a complete idiot. Not that I knew anything about capsules. That was when Jinho hyung spoke up.

“Wait a second.”

He pulled out his smartphone and started tapping the screen. Searching, from the looks of it. But the result was obvious.

“Fuck. All that comes up is porn sites.”

*Yeah, that one was pretty good.*

“It’s not even a ghost company. Why isn’t anything coming up?”

“Read the rest of it, too.”

By the time he reached the last page, he’d really feel like he’d been haunted. Jinho hyung turned the pages with a serious expression.

Once.

Then once more.

“Isn’t it incredible?”

“Yeah. Incredible.”

His voice was hollow.

“You told me to look at blank pages. That’s incredible.”

“Huh?”

“No wonder I thought this manual was so slapdash. No explanation of the capsule’s parts, no operating instructions, and even the model name, manufacturer, and date of manufacture are a mess.”

“Blank pages? What are you talking about?”

“Well, well. Look at this humanities-major bastard, acting all innocent.”

I snatched the manual and read it in a hurry. The contents I’d seen before falling asleep were still there. Precautions on the second page. Key features on the last.

“You can’t see this?”

“Cut it out. This is starting to get scary.”

That look. That tone. He meant it. The writing I could see was invisible to Jinho hyung.

Or maybe…

*Only I can see this.*

I stayed frozen like that for a long while.

* * *

Pshhh—

I climbed out of the capsule on shaky legs. Glossy exterior, shaped like a giant egg—this was the latest model, released only last month.

“Oh, you’re out already. Did you try the game I recommended?”

Still half out of my mind, I answered the capsule café owner at the counter.

“Yes.”

The virtual-reality game he’d recommended was a megahit with ten million concurrent users. Incredible graphics, outstanding freedom, over seventy percent of the market, he’d said.

“The graphics are insane, right?”

I logged in. I looked at the graphics and thought:

*Am I the one who’s insane?*

*This is the most popular virtual-reality game there is?*

The graphics were good. I could give it that. But that was as far as it went.

The NPCs’ faces and movements, their dialogue patterns, the five senses I felt through my character—all of it was unnatural. It was a *game*, but it never felt like *reality*.

“Do you have any games set in wuxia?”

“Ah, so you’re into wuxia? There are quite a few. What’s the title you’re looking for?”

“Murim.”

“Murim Online?”

“No. It’s an open-world game. One you play alone.”

“Are there games like that in the wuxia genre?”

Figures. There was nothing more to hear. I staggered out the door, and the owner called after me.

“Come again!”

I wouldn’t.

Not ever again.

* * *

Hope Goshiwon.

I sat beneath the old, rusted sign and pulled out my smartphone. The other end picked up almost before it could ring.

Click.

— Yeah. Why?

My one and only nemesis—no, my younger sister, Hayeon. The moment I heard that uniquely bratty voice of hers, my throat closed up.

— Hello?

“…Yeah.”

— Why’d you call?

“Just. I wanted to hear your voice.”

A deathly silence followed.

— I’m hanging up.

“No, wait. Wait!”

— Three seconds. What’s your business.

*That damn girl…*

Right. This was Jin Hayeon. Thanks to her, the tear ducts that had gotten a little moist dried out like sand around the pyramids.

“What’s Mom doing?”

— She went out. Said she had an errand. Call her if you’re curious.

I didn’t. On purpose. Even this brat’s voice was enough to choke me up. If I heard Mom’s, I’d bawl like a little kid.

I quickly changed the subject.

“What about you?”

— What’s a high-school senior with a hundred and twenty days left until the college entrance exam supposed to do? Study.

Her tone was sharper than usual. Exam stress must have been hitting her hard.

“How’s studying going?”

— I bombed the July mock exam. I didn’t manage my condition right and missed even the easy questions. God, the more I think about it, the more annoyed I get.

“It’s fine. Just do well on the real thing. How many did you miss?”

— Two.

“That’s still Grade 1.[^1] What about the other subjects?”

— Two across all subjects.

“Huh?”

— One in Korean history and one in math.

“…Two in total, across every subject? Are you serious?”

— Obviously that’s what I meant.

*Smart little brat…*

I knew she was good at studying, but I hadn’t realized she was this good. Thinking back on my own school grades, it really seemed like there was such a thing as dumping all the genes into one kid.

“You study pretty well, huh?”

— From an older brother’s standpoint, isn’t it amazing?

“W-what kind of nonsense is that? I studied pretty well too, you know? You just don’t remember because you were in elementary school…”

— Last week during a deep clean, I found your report card. There were so many Grade 7s I thought it was a slot machine that had hit the jackpot.

“You need some allowance, right? How much do cosmetics cost these days?”

— That’s pathetic. Seriously.

*Cruel girl…*

The call lasted more than ten minutes. I did most of the listening. Hayeon rattled on about studying, school, and a boy she was interested in, and her voice was much brighter than it had been at first.

I found myself getting oddly sentimental.

*I really did come back.*

Had I been dreaming? Or lost in a delusion?

Only a day had passed in reality, yet utterly incomprehensible, inexplicable things had happened.

But I decided not to try to understand them anymore.

*I’m back in reality now.*

And I had to live in reality.

My family was here. I was here. That was enough. I had simply dreamed a strange dream for a little while. The kind of dream that would fade on its own with time.

— So I…

“Yeah.”

Listening to my little sister chatter, I stood up. It was time to leave the old, rusted sign behind and go back to my room.

* * *

Bzzzt. Bzzzt.

Seong Jinho cracked his bleary eyes open. The smartphone by his pillow was ringing.

Six in the morning. The signal that started the day.

“Oh, I’m dying.”

It had been five years since he left home. The moldy smell that crept into his nose every morning had gotten pretty familiar. Eyes half shut, Seong Jinho shoved his cigarettes and lighter into his pocket and left the room.

*Nothing wakes you up like a cigarette.*

He shuffled up to the rooftop in his slippers. He’d just put a cigarette between his lips when—

Thud.

“Huh?”

What was that? Wondering, he leaned over the railing, and a hunk of metal sitting in the recycling area right in front of him caught his eye.

So did the well-built young man gazing at it.

“Hey! Jin Taekyung!”

At Seong Jinho’s shout, Jin Taekyung looked up.

“What?”

“You throwing that away?”

The hunk of metal was the junk capsule Taekyung had picked up the day before. After pulling some failed prank with it, he seemed to be taking it back out to throw away.

*He’d been awfully serious for a prank like that… Ah, whatever. It was nonsense.*

Seong Jinho gave a short laugh.

“Why throw it away? Not going back to Murim?”

“You believed that?”

Jin Taekyung smiled back. But to Seong Jinho, who had watched him for a long time, the smile looked somehow awkward.

*What’s with him?*

Something felt off. As Seong Jinho stood there uneasily, Jin Taekyung waved and started down the hill.

“Where are you going, you punk? Aren’t we eating breakfast together later?”

“I have to work!”

Jin Taekyung left without looking back. Seong Jinho took a drag from his half-burned cigarette.

“That bastard’s really working hard…”

Soon, Jin Taekyung disappeared from sight. Seong Jinho stubbed out his cigarette in a flowerpot and was about to leave when the junk capsule caught his eye.

*He said the manufacturer was H Soft, right?*

It was probably just some half-assed prank, but there was no harm in looking into it.

[^1]: Korean mock exams use a 1–9 scale; Grade 1 is the highest.
## Chapter artifact 41

# Chapter 41

The Hunter Manpower Office.

They called it an office, but it was a building. This six-story building sat on prime real estate right by the station, and hundreds of Hunters came through it every day.

*It’s been a while.*

Even at dawn, the lobby was packed.

After working through the long line, I reached the counter. The woman there asked in a businesslike tone,

“Is this your first time at the manpower office?”

“No. I’m already registered.”

“Your name?”

“Jin Taekyung.”

Back when I was a rookie, I’d graduated from the Hunter Training Center with excellent scores. But almost nowhere needed an F-rank Hunter like me, and the contracts a few small and midsize Guilds offered like they were doing me a favor were highway robbery.

So I’d found this place. The region had been different, though.

“There’s a record at the Ilsan branch. I’ve put you on the list, so please wait in the hall on the first floor.”

“Yes.”

This six-story building was a pyramid all by itself. The first floor took E- and F-ranks. You needed at least D-rank to set foot on the second.

Some people got angry, asking if this wasn’t just open discrimination.

It was.

*Not like this was the first or second time.*

I’d lasted seven years in this business and taken every kind of dirty treatment there was. I’d long since passed the point of being picky.

I started walking with that thought when—

“Hey, look who it is!”

I turned at the gravelly voice. Some hairy guy was grinning at me.

“Taekyung. You’re Jin Taekyung, right?”

“Uncle Kkeokjeong?”

*This guy’s still alive?*

* * *

His surname was Im. I’d forgotten his given name. I was pretty sure I’d heard it once, when he introduced himself seven years ago, but I couldn’t remember it.

He just looked so much like a bandit that everyone called him Im Kkeokjeong[^1].

“How’ve you been all this time?”

“Life as an F-rank Hunter is always the same. How about you?”

“Don’t call me uncle.”

Im Kkeokjeong gave me an easy smile.

“Call me hyung. We’re not even that far apart in age.”

How many years apart were we again? It was hazy.

“Hyung, how old are you?”

“Forty-five.”

“…”

*What’s with that confidence?*

But the people skills I’d honed over the years paid off. I somehow managed to force a smile.

“Right. I’ll just call you hyung.”

“That’s it, little brother. Hahahaha!”

His hearty laugh rolled through the hall. Nearly a hundred people looked over, then looked away.

*I should’ve just pretended I didn’t hear him and kept walking.*

In a way, it was a shallow connection. We’d run into each other every day for about half a year at the Ilsan office, and sometimes worked together. That was about it.

*He’s a good guy, but…*

Sometimes having him next to me was embarrassing.

Like now.

“The yulmu tea here is incredible. And the chairs in the hall are nice and soft.”

Im Kkeokjeong knocked back a mouthful of yulmu tea[^2] and tipped his chair as far as it would go.

From the way he did it, this clearly wasn’t his first or second visit.

“You come here often?”

“Not every day. I drop by now and then. Once I got married and had kids, I started watching myself. Heh heh.”

It seemed he’d started a family while we were out of touch. When I congratulated him, Im Kkeokjeong scratched his head.

“What’s so great about that.”

He was being modest, but a big deal was a big deal. He’d worked as a Hunter—an F-rank Hunter—for more than twenty years and still managed to build a family.

I wondered if the Im Kkeokjeong in front of me might be my future self.

*Assuming I lived to that age first.*

Being a Hunter wasn’t a career you could keep up for long. Plenty of people retired the moment they finished the ten years that qualified them for a pension.

“Anyway, you’re starting to look the part. When I first saw you, you were completely frozen. Could barely even talk.”

“Of course. I’ve got seven years in.”

“So you’ve just been bouncing around offices ever since? Didn’t you sign with a small or midsize Guild on fairly decent terms? So, So… what was the name again?”

“Sopung Guild. They fired me the day before yesterday.”

Im Kkeokjeong forced a laugh.

“Hahaha! Good for you. The Guild’s name was lousy, too. What the hell is Sopung? It’s not like you’re going on a picnic to a Gate.”

“No, not that sopung. It’s a place name. They’re near Bucheon Sopung Terminal, so Sopung Guild.”

“Oh…”

The conversation that followed was pretty useful. Im Kkeokjeong was a regular at the manpower office, after all, and a veteran Hunter with decent information and his own hard-earned know-how.

“The office takes a ten percent commission. That’s standard. But the batting average here is pretty good.”

*Batting average* was slang in this business for the odds of getting hired. For someone whose immediate goal was a day’s pay, that was good news.

“Even for F-rank Hunters like us?”

“Huh? Yeah. That’s right.”

*What’s with that awkward look?*

Before I could ask anything else, a voice came through the speakers in the hall.

—E-rank Hunter Im Hyeokjun. Im Hyeokjun, please come to the lobby.

Six thirty in the morning.

At last, the first batter was up. And it would only be my turn after all the E-rank Hunters had left.

“E-ranks first, as expected… Hyung, where are you going?”

“I’ll go ahead.”

Im Kkeokjeong—or rather, Im Hyeokjun—slung a large bag of armor and weapons over his shoulder and gave a sheepish laugh.

*No wonder his expression looked off.*

The man had clearly worked himself to the bone while I wasn’t looking.

It was only one step, but ranking up on an F-rank’s potential was no easy feat.

“See you again.”

“Yes. See you.”

Him walking out of the hall was the start. The speakers began pouring out names like they meant it.

E-rank this person, E-rank that person, E-rank…

*Goddamn it, am I the only F-rank here?*

Just as I was starting to get anxious—

—F-rank Hunter Jin Taekyung. Jin Taekyung, please come to the lobby.

*There it is!*

* * *

“Mr. Jin Taekyung?”

A man in a white linen shirt was waiting in the lobby. Without preamble, he held out a contract with a blank face.

“I’m from the Peace Guild. Read it and sign.”

*This guy’s way of talking is seriously irritating.*

I glared from the contract to the man’s face and back.

“The settlement split is eight to two.”

“After the raid, we divide the proceeds fairly by contribution. Then we take twenty percent of the amount you receive.”

“And the base pay?”

“Thirty.”

“Thir…ty?”

*Did this guy’s tongue get cut in half?*

“Gate rank.”

“E-rank.”

“Rejected.”

“The positions are full. You’ll be a porter.”

The corner of my eye twitched.

*What the hell did this guy just say?*

“Por-ter?”

“Is there a problem?”

“Obviously.”

The shirt guy glared at me, looking down his nose.

“What is it?”

“I don’t have a pen.”

“…”

After a brief silence, I took the pen he handed me and scrawled my signature. The base pay was 300,000 won, and the settlement split was generous too.

I’d flinched at E-rank Gate, but I was only going as a porter, so it didn’t matter. Skin a few monsters, haul a pack for a while, and part ways in a good mood.

*Peace Guild. I like the name already.*

I’d been itching to sign so badly my fingers had almost cramped.

“All signed.”

“…”

“So where are we going now? We taking a van?”

“There’s a van waiting outside.”

“Oh, that one? Looks nice. Bet the AC’s blasting too.”

“…”

“Guess I was last? There are already a few people here… Huh? Kkeokjeong hyung!”

“Huh? Taekyung!”

Im Kkeokjeong was waiting to load his bags into the bus’s trunk. He grinned wide.

“You’re coming too. Great!”

“Right? I must really have a connection with you, hyung.”

“Hahahaha!”

“Ahahaha!”

“…Let’s get going.”

Maybe it was the heat, but the shirt guy’s face looked years older.

* * *

The bus pulled out. From the passenger seat, the shirt guy said we’d arrive within twenty minutes, then closed his eyes.

Im Kkeokjeong introduced me to the others who’d been hired with us.

“All right, everyone, say hello. This is a younger brother I know.”

Now that I looked, they all knew each other. I dipped my head.

“Hello. I’m Jin Taekyung.”

“Oh, nice to meet you.”

“Tall young fellow. Looks like he can fight.”

There were three new people in all, men in their late thirties or early forties. In that warm atmosphere, Im Kkeokjeong explained.

“These guys are all E-rank. I’ve known them a long time. Over ten years now.”

“Yeah, about that long. Time sure flies.”

Meaning they all had at least ten years in. I had enough experience that nobody was going to call me a rookie wherever I went, but these guys were on another level entirely.

*Old-timer party.*

People like them pulled their weight wherever they went. In a pinch, they were much better than a middling D-rank.

“So what’s the young guy’s rank?”

Here it came. The rank check.

I answered carefully.

“F-rank.”

“Ah. That so? How many years?”

“Seven.”

“Hmm. That so?”

The mood went lukewarm. If my first raid started like this, that would be a problem.

I ran my mouth before it could settle.

“I won’t be in combat at all. I’m joining as a porter, so you don’t have to worry…”

The three men stared at me blankly.

“Why the extra explanation? We gonna eat you?”

“Drop it. If he’s been knocking around for seven years, he knows enough.”

“If Kkeokjeong hyung recommended him, that’s enough. Team Leader Choi must’ve thought he was all right too, or he wouldn’t have said yes.”

*Recommended? Team Leader Choi?*

I didn’t know the exact details, but I could more or less see how this had gone.

Im Kkeokjeong had recommended me. To the shirt guy—Team Leader Choi.

“W-what are you talking about?”

Im Kkeokjeong waved his hands, his face bright red.

The three men snickered.

“It’s written all over him. How did that hyung ever get married?”

“Good deeds are supposed to come to light. Why live hiding them?”

“Right. You think so too, don’t you?”

I nodded at once.

“Of course. Thank you for looking out for me.”

“Ahem. I just put in a word. Team Leader Choi made the decision.”

Well, then…

I’d thought of Im Kkeokjeong as one of the many people I’d crossed paths with for a moment and moved on from. Meeting him again, he was more simple and warmhearted than I’d expected.

*So that’s why the terms were so generous.*

The way they kept saying Team Leader Choi, Team Leader Choi, I figured their friendship had played a part in my contract too.

“I’ll work hard.”

“I told you, Team Leader Choi made the decision!”

The man in question answered Im Kkeokjeong’s awkward excuse.

“Then let’s say I made the decision.”

The shirt guy had opened his eyes at some point. No—Team Leader Choi. He spoke to us.

“We’ve arrived.”

I looked over. A four-meter-high Gate was drawing closer. At its center, a vortex of mana churned, ready to suck us in.

*An E-rank Gate.*

My first raid since coming back.

[^1]: Famous Joseon-era folk-hero bandit; the nickname comes from his looks.
[^2]: Yulmu tea is a sweet Korean grain drink, commonly served hot or cold.
## Chapter artifact 42

# Chapter 42

A Gate.

The greatest scar left behind by the Great Cataclysm.

More than thirty years ago, Demon King Asmodeus had used them as an invasion route. These days, they had long since been reduced to a livelihood for Hunters and excavation sites for a higher-dimensional energy resource called Magic Gems.

“Are you with the Peace Guild?”

A middle-aged man in work clothes came over from the entrance.

He was a civil servant from the Gate Management Office, posted at every Gate.

“Yes.”

At Team Leader Choi’s curt reply, the civil servant nodded.

“You’re right on time. When will you be entering?”

“We’ll gear up and go in right away.”

“There’s a waiting room on the second floor. Come down when you’re ready. Right, then.”

We followed Team Leader Choi. The two-story building where the Management Office civil servant was stationed was as run-down as a building could get, and the waiting room wasn’t much better.

*Damn. Get a load of that smell.*

The moment we opened the door, the stench of sweat hit me. Rusty cabinets and an overflowing trash can jumped out at me too.

“This place is pretty bad. Don’t they even air it out?”

“That’s how Gate officials are. It’s not called a cushy post for nothing.”

I left the grumbling behind and started changing into my raid gear. Leather armor and lightweight combat boots. Last, I drew a spear from its long case and gripped it.

*It’s been a while.*

That snug fit in my hand felt familiar and strange at the same time.

It was definitely different from the weapon I’d used over the past month… Ah, no. I shouldn’t think about that anymore.

*I have to forget all of it now.*

I was tightening the perfectly fine laces on my combat boots for no reason when Im Kkeokjeong came over.

He looked every bit the main tank, in full-body armor with a massive tower shield.

“Are you ready?”

“Yes. Pretty much.”

Im Kkeokjeong looked me up and down, then clicked his tongue.

“Look at this guy. How old is that equipment, even?”

“Who knows? I bought it when I first started, so at least seven years?”

Back when I was a rookie, I’d splurged on it at an underground shop in Dongdaemun.[^1] I still remembered the exact price.

1.98 million won.

*I couldn’t sleep properly for days after buying it.*

Hunting was a job where the expenses ran about as high as the pay. Most of that spending went to equipment. All because of how Gates worked.

*Gear that isn’t imbued with mana—or magic power—falls apart in no time.*

So the most common method was to craft equipment from Magic Gems taken from Gate monsters.

The higher the Grade of Magic Gem used, the more the price shot through the roof.

“Seven years? Good grief. No matter how much you like money, you have to spend it when you need to. You going to pinch pennies with your life on the line?”

“Hmm. I had my reasons.”

Reasons I didn’t particularly want to talk about. Im Kkeokjeong’s voice was worried.

“You’ll be in a noncombat position today, so you should be fine… but be careful.”

“Yes.”

Even as I answered, I felt strange. Someone who’d had “be careful” on their lips constantly until just recently came to mind.

But the sentimentality didn’t last.

“Is everyone ready?”

When Team Leader Choi appeared, my jaw dropped.

*No way.*

“Is that a Red Drake leather set?”

“Hmm.”

Team Leader Choi’s face hardened. I’d only ever seen gear like that in luxury-store catalogs, so the words slipped out before I could stop them.

“Ah, sorry…”

“It’s nothing. It’s only made with five types of magic and B-grade Magic Gems.”

“…”

“I’m not emphasizing it, but the materials are five types of magic and B-grade Magic Gems.”

“Ah. Right.”

“Red Drake leather is popular because of its distinctive sheen, but that’s all for show. It isn’t actually that useful.”

Team Leader Choi moved, his face still stiff. A faint red glow flashed across him.

“But it is very beautiful.”

“…”

“Let’s head downstairs.”

Team Leader Choi left the waiting room first. Im Kkeokjeong came over.

“That guy really loves it when people recognize his equipment.”

“I mean, I get it, but… why is he like that?”

“No idea. He’s an equipment nut. There’s even a rumor he blew his entire fortune on that set and sleeps in it every night.”

*So this guy’s a nutjob too.*

I sighed inwardly and hoped today’s raid would end in one piece.

* * *

“This isn’t the number of people you registered.”

The civil servant looked uncomfortable. Fair enough. We were supposed to enter soon, and the party still wasn’t all there.

*How long are we going to have to wait?*

Six people had gathered in front of the Gate. Barring me, the porter, there were only five combatants.

It was an E-rank Gate, so you needed at least five more Hunters of the same rank… and with those Peace Guild bastards nowhere in sight, of course the civil servant was pissed.

“If additional personnel have been added, you need to inform us in advance.”

*Huh? What did he just say?*

Additional personnel?

“I’m sorry.”

At Team Leader Choi’s curt apology, the civil servant picked up his pen and struck several lines through the paperwork.

“We can just amend it, so it’s not a major problem… but please be careful next time.”

“Yes.”

*Not a major problem, my ass. There aren’t any people!*

I poked Im Kkeokjeong in the ribs.

“Hyung. When are the others getting here?”

“What others?”

“The Peace Guild.”

“Team Leader Choi is here.”

“What?”

“Oh, did I not tell you? The Peace Guild is new, so it’s short on people. There are only three of us, including the Guild Master. Hahaha.”

…You’re laughing?

“Come on, hyung.”

“I know, punk. But you don’t have to worry.”

Im Kkeokjeong patted my shoulder and pointed at Team Leader Choi, who was signing the paperwork.

“That man’s a C-rank Hunter.”

“Oh. C-rank…”

I shut my mouth.

If Team Leader Choi was a C-rank Hunter, there was no problem. No—he was far better than ten E-rank Hunters. He was a mid-rank Hunter, in a completely different league from a low-rank Hunter like me.

*I should’ve realized the moment I saw him in that luxury gear.*

This was a man walking around with a high-end apartment wrapped around his body. A price most low-rank Hunters couldn’t afford even if they drained their entire fortunes ten times over.

A faint halo seemed to shine from Team Leader Choi’s back.

“Please verify the signature.”

Even the way he handed the pen back to the civil servant was elegant.

Even his smallest movements seemed to drip with class.

*So this is the dignity of a C-rank Hunter.*

*That’s fucking cool.*

I wanted to become sworn brothers with him. To swear a gay oath beneath the Gate—no, a Gate oath.

“All right, then. Let’s go in… What is it?”

Team Leader Choi looked at me, startled.

“No. I just thought you looked cool.”

“Excuse me?”

“The equipment. I said it looks cool.”

At that moment, the corner of Team Leader Choi’s mouth twitched.

“It’s nothing. It’s only made with five types of magic and B-grade Magic Gems…”

*A nutjob I wanted to get along with.*

* * *

I took a step toward the Gate.

Whoosh—

A familiar sensation wrapped around me. The cool, sticky energy unique to magic power. Then the scenery flipped.

“It’s a cave.”

As Team Leader Choi said, this raid’s location was a cave. The walls were damp with moisture, and faint darkness lay over everything around us.

“Mr. Taekyung. Take out a flashlight.”

“Yes.”

I quickly set down my backpack. It was a porter’s bag Team Leader Choi had handed me just before we entered the Gate. It looked ordinary on the outside, but it was an expensive item enchanted with both space expansion and weight-reduction magic.

“Here. A flashlight.”

I handed it over since he’d asked, but in my experience it wasn’t the best method. Convenient, sure, but if the light vanished, you couldn’t adapt to the sudden dark.

It was much better to wait a little and let your eyes get used to the darkness…

Click.

“Let there be light. Light.”

Whoosh. A ball of light the size of a soccer ball shot out of the flashlight and slapped itself against the cave ceiling.

“…Magic?”

“It’s built-in magic that activates as soon as you chant the spell. It lasts quite a long time, so three or four hours shouldn’t be a problem. It’s a limited edition I bought from Company M, but…”

Im Kkeokjeong, who had been watching, boiled it down to one line.

“It’s crazy expensive.”

Was Team Leader Choi’s face darkening a little just my imagination, or was it the shadows? Either way, the raid had gotten a lot easier thanks to it.

*Money really is the best.*

The world was ruled by capital, and Gates were no different. People with money fought easy with magic equipment; people without it had to carry torches.

“Take your positions.”

At Team Leader Choi’s command, everyone moved at once. Im Kkeokjeong and another E-rank Hunter took the lead as tanks, with Team Leader Choi behind them. I, the porter, and the two ranged dealers stood at the very back.

“Move.”

We started advancing slowly.

The bright magic light lit the path ahead.

“…”

*I want one.*

* * *

“Kiiiieet!”

The creatures that had been crouched in the darkness showed themselves with shrill cries. Green skin. Short torsos. Limbs that looked grotesque.

They were Hobgoblins, a higher species of ordinary goblin.

*About thirty of them.*

With only five people, this would be a hard fight.

*But a C-rank Hunter changes the story.*

On top of that, the other four were veteran E-rank Hunters with at least ten-odd years of experience each.

I hung back and watched the fight.

“Ranged!”

The moment Team Leader Choi gave the order, arrows flew. One shot, one kill. The arrows punched into vital points, and the unshielded Hobgoblins dropped in heaps.

“Kiit!”

“Oof, shield-bearers. What should we do?”

“Hold.”

Team Leader Choi went on.

“Tanks, advance.”

The tanks in thick full-body armor moved forward with their tower shields. Im Kkeokjeong and the other man were both huge, over 190 centimeters, so the intimidation factor was no joke.

“Kiiiieet!”

But monsters were monsters for a reason. Trusting in their numbers, the Hobgoblins charged like a swarm of bees.

But then—

“Well now.”

Bam!

They turned to bloody pulp against those big, beautiful tower shields and went flying. Riding that momentum, Im Kkeokjeong swung his mace like a flyswatter, wrecking limbs and smashing heads.

“You punk! You punk!”

…What was this, whack-a-mole?

*Old-timers, as expected.*

All four of them kept to their roles without overdoing it, steadily cutting the enemy numbers down.

Knowing when to fall back and when to push in was combat intelligence born of plenty of experience.

“Everyone, hold your positions.”

And then one man.

The man who had been directing the flow of battle until now moved.

“I’ll handle the rest.”

At the same time, a red line flashing along his armor plunged through the twenty Hobgoblins.

Slash—

A head sprang into the air along a clean arc. The monsters couldn’t react in time to something that happened so fast.

“Kiiie?”

Slash. Slash. Slash.

The blade did not stop. Merciless and efficient, it pierced and cut through vital points. This was no longer a battle.

It was a massacre. A massacre of some twenty monsters by a single human.

*This is a C-rank Hunter.*

I could see his speed, his strength. All of it. And I felt it.

*He really is strong.*

As a mere F-rank, I couldn’t even dream of matching him. He was a mid-rank Hunter three full stages above me. A wide river and a high wall that effort alone could never bridge.

But at the same time, a question surfaced.

*What if this were Murim?*

Team Leader Choi was definitely strong. He had the ability befitting a C-rank Hunter, and plenty of experience.

But if this were Murim… if he were a man of Murim…

*I’d be stronger.*

His movements were fast and powerful, but that was all. He hadn’t learned martial arts, and he didn’t use mana efficiently either.

At best, he was first-rate. In Murim, that was exactly where he would stand.

*But this is reality.*

I bit my lip without realizing it.

A mid-rank Hunter and the lowest-rank Hunter.

While the mid-rank Hunter wore expensive equipment and slaughtered monsters, the lowest-rank Hunter could only stare blankly.

In the role of a porter.

“Kiiieet…”

The last Hobgoblin fell. Team Leader Choi pulled his sword from its chest, and our eyes met.

“Mr. Taekyung. Please handle the byproducts.”

“…”

“Mr. Taekyung?”

I wanted to tell him I was stronger than he was.

But in the end I couldn’t. This was my reality.

“…Thank you for your hard work.”

I *used to be* stronger than you.

[^1]: Dongdaemun is Seoul’s major wholesale-market district.
## Chapter artifact 43

# Chapter 43

Swish.

A sharpened dagger dug into a Hobgoblin corpse.

Fluids splattered, and a foul stench filled the air, but I didn’t stop. I discarded the heads, neatly cut away the hides from their backs and bellies, and stacked them in a pile.

“You’re quite skilled.”

“…Thank you.”

It was Team Leader Choi. His kindly voice made me feel guilty. Getting jealous of someone like him—how childish was that?

Especially after dragging up an illusion I’d already decided to forget.

*It’s not like I’m going through puberty.*

I finished the job with my face burning red.

A little over ten minutes, so about twenty seconds per corpse? Even Im Kkeokjeong sidled over, drawn by the speed, and his mouth fell open.

“Damn, have you been doing nothing but this?”

“Plenty of people can do this much.”

“Plenty, my ass. You’re a total professional.”

Hmm. That made me a little proud.

I’d played modest a second ago, but Im Kkeokjeong was right. There weren’t many Hunters who could butcher this cleanly at this speed.

“I’m just fast with my hands.”

I’d done factory part-time jobs in school. I’d even stuck eyes on dolls. In a way, I’d started this before I ever worked as a Hunter.

“I kept doing it during raids, too.”

“You switched over to this completely?”

“No. I just did both. A side job.”

“A side job?”

Team Leader Choi, who’d been listening quietly, cut in.

“Oh, yes.”

“Exactly what kind?”

“I just split the rest time after combat to do the work.”

“Do you receive additional pay?”

“Of course. It’s work, too.”

“How long have you been doing it?”

“I’ve kept at it. From the beginning until now.”

Im Kkeokjeong was floored.

“You hardcore bastard. I couldn’t do that.”

“You get used to it. It helps build stamina, too.”

“Your life’s on the line, and you’re building stamina? Hahaha. Team Leader Choi, didn’t I tell you? There’s nobody who works as relentlessly as this kid.”

*Did you say that?*

“Hm.”

Instead of answering, Team Leader Choi studied me for a moment, then turned away.

“The work’s done, so shall we get moving again?”

What was that reaction supposed to mean? While I stood there bewildered, Im Kkeokjeong gave me an unreadable smile.

“Keep working hard.”

*No, what?*

* * *

The raid went smoothly. The E-rank Hunters had been in sync so long they moved as one. Once they cut the monsters’ numbers down, Team Leader Choi took over.

Slash—

Every swing of his sword sent up a fountain of blood.

I took in every second of the fight unfolding right in front of me.

*He really can fight.*

Of course, I couldn’t help thinking about Murim.

I’d seen real martial arts with my own eyes—and even learned them. Not the dance-like moves I practiced in the city park at dawn.

*…Huh?*

*No way. Still, maybe?*

It was ridiculous. There was no way it would work, but I was going to try once.

*It won’t work. It won’t… But it’d be nice if it did.*

That was the moment I was about to take a careful step.

“Mr. Taekyung. Please handle the cleanup.”

Team Leader Choi’s voice snapped me straight back.

*I’ve completely lost it.* Getting distracted in the middle of a raid.

*Get a grip.*

Whatever I wanted to do later, the raid came first.

That was courtesy to my teammates—and the conviction that would keep me alive.

“Yes. I’m coming!”

I ran over like the wind and started taking the corpses apart.

Team Leader Choi and Im Kkeokjeong loitered nearby the whole rest period, like they weren’t tired at all.

*It’s seriously getting on my nerves.*

* * *

Im Kkeokjeong came over again at the next break, without fail.

“Taekyung. How long have you been using a spear?”

“Seven years.”

“Wow. At that point, you’re pretty much a master. A real master.”

“…?”

The break after that, too.

“Taekyung. You said you were top of your training class, right?”

“Yes. But I was only first among the F-ranks, so it doesn’t mean much.”

“You punk. That’s what makes it impressive. I finished dead last.”

“You’re impressive too, hyung. But I have some work to do.”

“Oh, right.”

And then the next break. And the one after that. And the one after that.

“Taekyung. Taekyung. Taekyung.”

“Hyung. I think my cochlea’s been torn open.”

“You said you worked at your previous Guild for several years, right?”

“Ah.”

I wanted to switch to a mage right then and there, just so I could put a silence spell on that man’s mouth.

*This is driving me crazy.*

There was only one way out. Finish the work before blood really started pouring from my ears. I clenched my teeth and kept my hands moving.

Slice. Slice. Slice.

“Taekyung.”

*Save me.*

I sent a distress signal to Team Leader Choi, who was sitting nearby, but he answered by quietly slipping away.

* * *

“The work’s done.”

I stood up with the bag on my back, heavier than before. Hobgoblins were generous monsters. Poison-resistant hides, a few usable weapons—and they even dropped two E-rank Magic Gems.

*The hides are in good condition, and there are two Magic Gems. This could be worth a decent amount.*

Team Leader Choi had contributed the most, so he’d probably take about half. But with so few people, it was still a profitable deal for the other team members.

Not me, of course. According to the contract, the 300,000-won base pay was all I would get.

*If he’s in a good mood, maybe he’ll throw me a little extra.*

Team Leader Choi was a fairly generous employer. He was a C-rank Hunter way out of my league, yet he always treated me with respect. His personality was a little unusual, but in this line of work, that made him a decent human being.

*And a skilled Hunter I can trust.*

Thanks to him, we’d made it this far at a steady, rapid pace.

All that remained was the last stretch of the Gate.

The Boss Zone.

If we opened the stone gate in front of us, the Gate’s boss monster and the mana field that would send us outside should be waiting beyond it.

“Man, all that moving around made me hungry.”

“Let’s finish this quick and go out for some gukbap.[^1] Taekyung, you’re coming too, right? And you too, Team Leader Choi.”

“I’m fine. I’ll order sushi separately.”

“…”

Talking about food with the Boss Zone right in front of us. And on top of that, there was a guy planning to order sushi by himself.

*Is it really okay to be this relaxed?*

Of course, I had no right to say that. Just portering and butchering in between had already earned me a day’s pay.

Until I landed a job at a new Guild, if Team Leader Choi kept calling me, I wouldn’t have anything left to wish for. A sweet gig like this? I could do it a hundred times over.

“Well, shall we head in?”

“Yes.”

At Team Leader Choi’s answer, Im Kkeokjeong slammed his tower shield into the stone gate.

Boom!

The gate blew apart, and stone dust and dirt poured down. I followed the others into the Boss Zone.

And there…

—Keuruk.

It was there.

*A shaman?*

That was the first word that came to mind when I saw it.

An old Hobgoblin in robes marked with unreadable patterns. A withered staff in one hand, a sharp dagger in the other.

—Karruk. Chwi. Akto.

Despite the loud crash when the stone gate broke, it went on muttering, unfazed. Each time a syllable ended, black energy rose from the corpses scattered around it.

*Wait. Corpses?*

I’d seen it right. Nearly a hundred Hobgoblins lay dead on the altar. Looking closer, they were the ones we were supposed to fight in the Boss Zone.

*What the hell is this?*

While all of us froze at a situation none of us had ever seen, Team Leader Choi shouted like a thunderclap.

“Get outside. Now!”

That was when the unknown old Hobgoblin turned its head.

Clink.

Its staff shook lightly.

—Mita. Allo.

The air shuddered.

Magic was taking form.

“Behind the shields!”

The tanks hurriedly raised their tower shields. But that was the wrong call. What it had used wasn’t an attack spell.

Boom. Boom. Boom!

“It’s behind us! The passage is being blocked!”

“Run! Hurry!”

*Damn it. Too late.*

As if the clock had been turned back, the shattered stone gate stood intact again.

And the changes didn’t stop there.

The rubble on the floor had stacked into double and triple walls, and vines from the cave walls bound them tight.

“Everyone, out of the way!”

It was Im Kkeokjeong. His muscles had swollen like they were about to burst—probably a Strength Enhancement Skill. Tower shield in hand, he charged the stone gate.

“Haaah!”

Bang! Crack!

“…Goddamn it.”

Im Kkeokjeong dropped the tower shield, his face blank with disbelief. An E-rank Hunter had even used a Skill, and he hadn’t broken through. He’d only wrecked his shield.

*Enhancement magic?*

Whatever it was, one thing was certain.

That old Hobgoblin, using magic like this, was a monster at least one or two stages above us.

And…

Swish!

There was someone among us who could face it.

*When did he—?*

Team Leader Choi was already charging the thing, as if he’d been sure the passage wouldn’t break.

“The wind takes hold. Haste.”

His body slid forward. More than a hundred meters vanished in an instant. With five paces left, the sword came free from Team Leader Choi’s waist.

Whoosh!

A C-rank Hunter’s full-power attack.

The old Hobgoblin only smirked.

—Karruk. Chwi. Akto.

The change happened in an instant.

Whoosh—

The hundred-odd corpses scattered across the altar shriveled, then dispersed like sand. The black energy, fully pulled out of them, gathered into one mass and smashed into Team Leader Choi’s side.

Thud!

“Ghk.”

Team Leader Choi bounced back fast. With a twisted face, he said,

“We have to stop it. Right now.”

“…That?”

It was already too late.

Only a few seconds ago, it had been nothing more than energy given form. Now it was rapidly taking shape.

A hulking frame nearly three meters tall. A monster with muscles ready to burst, holding a greatsword of terrifying size.

“What the hell is that…?”

Someone muttered in a dazed voice. Just like me, this had to be the first time they were seeing anything like it.

Only Team Leader Choi knew what they were.

“Hobgoblin Great Warrior. A C-rank Rare Monster.”

The fact that something that size was a Hobgoblin was shocking enough. Next to what came after, it was nothing.

*C-rank Rare Monster?*

*Fuck, why is that thing showing up here?*

Rare Monsters were rare monsters that appeared in a given Gate only at a low rate. And that Great Warrior was C-rank—something the rest of us would never have run into in our lives.

…Of course, not anymore.

“You want us to fight that thing?”

“Those things.”

Team Leader Choi pointed at the old Hobgoblin.

“Hobgoblin Priest. Also a C-rank Rare Monster.”

“Ah, fuck…”

The curse slipped out before I could stop it. Im Kkeokjeong asked with a stiff face,

“What are our chances? Give it to me straight.”

“If we take out the Priest first, there’s hope. In exchange…”

Boom. Boom.

Team Leader Choi’s words cut off.

The Great Warrior was coming toward us.

One step. Then another.

The cave floor shook.

“We need to hold that thing down for a little while.”

*Who?*

“Us?”

“No. All of you.”

“Kuwooooh!”

The Great Warrior’s roar sent a stalactite dropping from the cave ceiling.

Team Leader Choi turned with a resolute look I’d never seen on him before.

“The wind takes hold. Haste.”

*Hey, you bastard.*

[^1]: Gukbap is a Korean dish of soup served with rice.
## Chapter artifact 44

# Chapter 44

“Just hold out for five minutes.”

With that, Team Leader Choi shot off like the wind. For better or worse, the Hobgoblin Great Warrior didn’t give him so much as a glance.

“He’s coming this way.”

At my words, everyone nodded blankly.

“He is.”

Boom, boom, boom!

“He’s running this way.”

“Defensive formation—!”

The team snapped into formation. I gripped my spear and moved as ordered. Between the tank and the ranged dealers. Dead center—that was my spot.

*No, for fuck’s sake. I’m a porter…*

Even if my life was going to go sideways, did it have to go this sideways?

They say an unlucky bastard can fall over backward and still break his nose. For 300,000 won, I’d run into two mid-grade Rare Monsters. This wasn’t just a broken nose. This was a broken nose and a cracked skull.

—Kuwaaaaah!

The Hobgoblin Great Warrior charged with a roar. Nearly three meters of muscle and green hide—overwhelming all by itself.

*Why is that greatsword so damn huge?*

The thought of that thing swinging at me made me swallow hard.

“Can we stop it?”

“We’ll have to try.”

Im Kkeokjeong planted his tower shield in the ground and shouted,

“Archers! Don’t hold back on mana! Pour it on!”

Swish, swish, swish!

Mana-charged arrows flew in a straight line. They had enough force to punch through most shields, but…

Thunk, thunk.

The Hobgoblin Great Warrior flicked its greatsword and chopped every one of them in half. Even if they’d hit, I doubted they could have pierced that hide.

“Aim for the vitals! Keep shooting and slow it down!”

Then the Great Warrior’s eyes burned red. Once it drew up its mana, its strength and speed were on a whole different level.

“Kuwooooooh!”

With a booming roar, the green giant launched into the air.

Im Kkeokjeong screamed,

“Scatter!”

Before anyone had time to think, they threw themselves aside.

Boom!

The greatsword smashed the ground to pieces. A blast of air sent dust whipping around us like a tornado.

“Ghh.”

“Cough, cough.”

Groans and coughing broke out beyond the curtain of dust. I crouched as low as I could and thought,

*What kind of monster is that?*

It couldn’t compare to *that guy* from two years ago, but a chill still ran down my spine. In a fight like this, an F-rank Hunter like me was nothing but baggage.

*I have to get as far away as I can while I have the chance.*

Everything was a wash of haze. Nobody could tell friend from foe. This was my opening.

I stayed low and moved slowly. Spear in one hand, the other feeling through empty air.

Then—

Tap.

My fingertips hit something solid. Very hard, and wet.

It had to be the cave wall.

*Already?*

I’d thought I was farther out, but I must have been closer than I expected.

Fine by me. If I followed the wall, I could—

Squish.

“…?”

What was this now? I carefully probed the unpleasantly squishy thing.

*There’s fur, too. A person?*

Maybe it was the head of someone who’d passed out. I held my breath and whispered,

“Kkeokjeong hyung?”

No answer.

“Who is it?”

This time, I got a reply.

Right above me.

“Grrr.”

A gust of wind swept through from somewhere and cleared the dust. I slowly looked up and saw a pair of gleaming red eyes.

“Grrk.”

“…”

I looked back down. Between thighs as thick as pillars and hard as stone, my dainty little hand was clamped around something.

I groaned under my breath.

“Ah, fuck…”

That was a male’s instinct. Unbearable nausea. Disgust at myself. The next moment, my grip went slack on its own.

Slide.

My hand dropped, limp—and the greatsword rose with force.

“Grrk.”

“I let go! I let go, so why are you doing this?!”

“Kuwooooooh!”

Goddammit.

I wrung out every last bit of strength I had and ran.

* * *

Boom! Boom! Boom!

The Hobgoblin Great Warrior had completely lost it. It chased me like a lunatic, hacking in every direction with its greatsword.

Whoosh—

“Aaaaah!”

That one was actually close. I ducked at the last second; the greatsword skimmed over my head and wrecked the cave wall.

“Taekyung!”

“Shoot!”

The team poured on arrows and throwing weapons, but…

“Kuwaaaaargh!”

It wasn’t enough to pull the Great Warrior’s attention. Its eyes had already rolled back.

I rolled, then rolled again, and cursed my luck.

*I should’ve just popped it.*

Instinct had beaten reason. A man’s need to get his hand off *that* even one second sooner.

Whoosh!

The greatsword barely missed. Crisis after crisis, and I still hadn’t let the C-rank Rare Monster land a single clean hit.

*Maybe it’s because I’ve seen so much hell in Murim.*

It sounded insane, but it was true. I could see the attacks. Moving half a beat ahead was what was keeping me alive.

Boom!

Of course, one hit from that thing and I’d be a goner.

“Taekyung, this way!”

I cut toward the voice. The team was waiting there in a defensive formation again.

“Fall back!”

Im Kkeokjeong Charged the Great Warrior chasing me. Blue mana sheathed the tower shield, packed with enough force to smash most low-grade monsters to pieces.

“Hah!”

With a short shout, Im Kkeokjeong brushed past me. And then—

Crunch. Thud.

Something broke, and he shot backward at a vicious speed.

He flew a good ten meters, slammed into the wall, and vomited a gush of blood.

“Gweeehk.”

“…”

Was this for real?

I was stunned. The rest of the team, on the other hand, looked grimly determined.

“No! Kkeokjeong hyung!”

“We’ll buy time! Take hyung and get out!”

Then the greatsword sent another tank flying, tower shield and all.

Boom!

“Agh!”

“Jongmin!”

“We’ll buy time! Take Jongmin and hyung and get out!”

Thud!

“Aaargh!”

“Seokho!”

“…”

Smack!

That was the sound of the team wiping. The last member had charged in with a dagger, taken a knuckle to the skull, and gone flying. He twitched, then passed out.

At least they were all still breathing. Small mercies.

—Grrr…

Scratch that.

I kept my eyes on the monster and shouted,

“Team Leader!”

A brutal fight was still going on at the altar in the distance.

A tired voice came through the explosions.

“What?!”

“Are you still not done? It feels like it’s been more than five minutes!”

Boom! Boom! Fwoosh!

Lightning struck, and flames surged. Team Leader Choi screamed,

“Three more minutes!”

Anyone who didn’t know better might have taken him for a soccer referee. His bold call for extra time left me speechless.

—Karruk, karruk.

The Hobgoblin Great Warrior came on slowly. A cruel smile hung on its wide-slit mouth. I eased back in time with its steps.

“That’s right. Come on. Come on.”

No choice. Same as before: run like hell and stall.

—Grrk.

But the Great Warrior didn’t play along.

“Huh?”

Its bulging eyes rolled toward the teammates sprawled unconscious on the ground. I had a very bad feeling about this.

“Don’t tell me…”

That was exactly it.

My heart dropped as I watched its back heading for Im Kkeokjeong.

“Hey! Hey, you!”

All I got was being ignored completely.

Now I was the one in a panic.

*If I leave it like this, they’re all dead.*

I had to pull its eyes somehow. I grabbed a rock off the ground and threw it at the monster’s head.

Thwack!

Direct hit.

The Hobgoblin Great Warrior turned and glared at me.

“Yeah. Come here.”

—Grrr.

Its narrowed eyes flicked between me and Im Kkeokjeong. Then it started running at Im Kkeokjeong.

Boom, boom, boom!

“You crazy bastard!”

At this rate, Im Kkeokjeong and the rest of the team would all be wiped out. I was the only one who could stop it.

*Stop that thing? Me?*

A one-on-one against a C-rank Rare Monster.

A fight I could never win. But…

*Ah, fuck.*

I was already charging at it. Sometimes you have to fight even when there’s no chance.

This was one of those times.

“You son of a bitch!”

Whoosh—!

The instant I thrust my spear at its broad back—

—Kururuk.

The green giant turned like it had been waiting. A smug smile sat on its mouth. The greatsword swept in horizontally, a streak of light shooting for my side.

*That’s what you were after.*

My mind went white. Could I even block that? Had I made the wrong call out of some cheap guilt and heroics?

But the die was already cast.

*I have to hold.*

There are times you fight with your life on the line. This was one of them.

*Please!*

I clenched my teeth and turned the iron spear into its path. At the same time, the greatsword smashed into it.

Rrrrk—

A roar of impact. Then enormous pressure. The greatsword, iron spear and all, split straight through my waist—

“…Huh?”

The iron spear was fine. So was my waist. All that had happened was my feet had been pushed back a little. A very, very little.

“…?”

What was this?

—G-Grrk?

The Hobgoblin Great Warrior’s face flushed bright red. It pulled the greatsword back and smashed it down on the iron spear again. Even through the confusion, I tightened my grip and blocked.

Boom!

My body slid back.

Maybe thirty centimeters?

“…Uhh.”

—…Grrk.

The Hobgoblin Great Warrior’s eyes met mine in the air between us. I’d been through this somewhere before.

*That’s right. The duel with Lee Seogeun. It was exactly like this.*

I’d freaked out at his Level and thought I was dead, only to find out he was a total pushover. How was I supposed to forget a moment that absurd?

*But I had the System backing me there.*

This was reality. I was an F-rank Hunter with nothing. No System, not a damn thing.

*How is this even…*

Ding.

“Huh?”

I froze. For that instant, I couldn’t see or hear a thing.

*This can’t be. This is actually insane.*

Ding.

> **System**
>
> Synchronization complete.
>
> All systems are inherited.

And yet, it actually happened.

“Ha… hahaha.”

A laugh slipped out of me like I’d lost my mind. The Hobgoblin Great Warrior stared at me like I was the crazy one.

> **System**
>
> Lv. 45 Hobgoblin Great Warrior

Right. So that was how it was.

“I don’t know what the hell just happened…”

I grinned at the monster.

“But you’re fucking dead.”

* * *

Gurgle.

A wrinkled hand clutched at a throat. But the old goblin had neither the strength to stop the blood pouring out like a waterfall nor the time to spit out the spell still sitting on the tip of its tongue.

“What a nuisance.”

With that from Team Leader Choi, the light went out of the Hobgoblin Priest’s eyes.

*I’m tired.*

But he turned around at once. He still had work to do. A C-rank Rare Monster was going to be a brutal fight, so—

Slash—

“Kwaaaaargh!”

Team Leader Choi thought he was seeing things. That same Hobgoblin Great Warrior was screaming. One arm gone, it was staggering back.

*Who did that?*

He watched the fight, even forgetting he was supposed to help. Ghostlike movement. A spear-point pouring like water, carving the green giant to pieces.

Wait. A spear?

Of everyone here today, only one person used a spear.

*The porter—no, Jin Taekyung?*

That was him.

The F-rank Hunter who’d been hauling a backpack and skinning hides!

“What on earth…”

Team Leader Choi’s mouth slowly fell open.

“What’s going on?”
