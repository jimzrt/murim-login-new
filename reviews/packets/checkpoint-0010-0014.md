# Checkpoint Review — 10–14

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

- `compendium.md` is binding for established names, titles, ranks, techniques, organizations, system terms, items, and locations.
- Search only exact Korean terms already present in the current chapter; the compendium contains future-sensitive entries.
- Never re-romanize established names or invent grand names for uncertain terms.
- Use `qi` for Murim energy and `mana` for the modern Hunter system when the source distinguishes them.

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
- Translate exactly one requested chapter unless the user explicitly requests a batch. Never modify `original 1-1104.txt`.

## Checkpoint summary

# Chapters 10–14

## Plot

Taekyung enters a staged confinement in the training hall, secretly arranged by Jin Wikyung to protect him from the Elder Council. He acquires and trains the Jin Family’s Spear Technique, combines it with his Manoeuvre Technique, and creates a crater with the Sky-Piercing Strike. The Unity of Self and Object achievement grants him the Clear-Heart Pill, a ring that improves concentration and cultivation. During three days of intensive training, his Cultivation Technique reaches the Third Stage, his Spear and Manoeuvre Techniques reach the Fourth Stage, and he reaches Level 14. Training Mode lets him practise against adjustable versions of opponents, including Hyuk Mujin.

After confinement ends, Taekyung is taken to the main assembly hall rather than allowed home. Lee Seogeun, a Level 30 envoy of the Mount Heng Sword Sect, accuses him of attempting to rape the sect leader’s daughter and demands that the Jin Family withdraw from every commandery and county except Taiyuan. When Jin Wikyung refuses the demand and the duel, Taekyung accepts the System’s Duel Quest to prevent war and his designation as a public enemy. Lee initially overwhelms him with killing intent, but Taekyung blocks more than twenty strikes, kicks Lee’s exposed chest, and breaks through the Intimidation effect. The duel continues with Taekyung promising to defeat him.

## Continuity

- Taekyung is Lv. 14. His Cultivation Technique is Third Stage; his Spear and Manoeuvre Techniques are Fourth Stage.
- The Clear-Heart Pill is a ring that steadies Taekyung’s mind and improves concentration and cultivation.
- Training Mode can summon prior opponents and partially adjust their abilities; Hyuk Mujin is Lv. 20.
- Taekyung’s three-day protective confinement has ended. He is at the main training ground, still not returned to his residence.
- Jin Wikyung is Taekyung’s protective eldest brother and Lesser Family Head; Wipeng restrains him from entering the duel and supports the protective plan.
- The Mount Heng Sword Sect and the Jin Family are sworn enemies. Lee Seogeun is a Lv. 30 envoy acting on Mount Heng’s behalf.
- The Myeongwollu evidence remains suspicious: witnesses claim Taekyung entered the wrong room while drunk and that someone heard screaming, while Taekyung denies the alleged assault through his amnesia pretence.
- Taekyung accepted the Duel Quest. Its reward is the Gambler title, EXP, and Fame 50; refusal would cause the Sex Fiend title, injury, war with Mount Heng, and public-enemy status.
- Taekyung can read and block Lee’s attacks despite the Level gap, has kicked Lee’s chest, and has lost the Intimidation status effect.
- The capsule’s purpose, route home, and the limits of Murim’s death and resurrection rules remain unresolved.

## Translation Decisions

- Retain **Mount Heng Sword Sect**, **Taiyuan**, **Myeongwollu**, **Lesser Family Head**, **Sound Transmission**, and the Jin Family’s **Cultivation**, **Spear**, and **Manoeuvre Techniques**.
- Render the achievement as **Unity of Self and Object**, the reward as the **Clear-Heart Pill**, and the quest titles as **Gambler** and **Sex Fiend**.
- Render Mount Heng’s demand as withdrawal from every commandery and county except Taiyuan.
- Preserve the brisk dark action-comedy, Taekyung’s self-mocking profanity, and the distinction between the first weapon clash (“Kra-kra-kraang”) and later cannon-like impacts.
- Preserve the gold-spoon/**God-Spoon** wordplay with a brief footnote where needed.

## Durable state

{
  "version": 1,
  "safe_through": 14,
  "continuity_sources": [13, 14],
  "active_continuity": [
    "Jin Taekyung is trapped in Murim through an old game capsule; death is presented as permanent and he cannot log out at will.",
    "Taekyung is the disgraced third son of the Jin Family of Taiyuan and narrates with dry, self-mocking, occasionally profane humor.",
    "Logout is the Main Quest reward for reaching First Rate, Lv. 30, and 500 Fame.",
    "Taekyung is Lv. 14; after three days of training, Qi Sense detects targets through Lv. 30 within ten jang.",
    "Hyuk Mujin is Lv. 20; Training Mode can summon him and Taekyung can partially adjust a summoned opponent’s abilities.",
    "Jin Wikyung is Taekyung’s thirty-five-year-old eldest brother and the Lesser Family Head of the Jin Family of Taiyuan; Wipeng is his trusted guard.",
    "At the Medicine King Hall, Taekyung pretends to have amnesia, and Jin Wikyung believes him.",
    "Jin Mukyung is twenty-five, the Heaven Shaking Sword, and a cadet at Heaven's Gate Temple.",
    "Taekyung has three martial arts occupying slots; the System displays ten total martial-art slots, and he finds several hundred manuals in his residence.",
    "Taekyung completed the Jin Family’s Manoeuvre Technique and Spear Technique training, reaching the Fourth Stage in both after combining their forms.",
    "The Jin Family’s Cultivation Technique remains at the Third Stage after Taekyung opened the Unity of Self and Object achievement reward.",
    "The reward is a Clear-Heart Pill ring that steadies Taekyung’s mind and improves concentration and cultivation.",
    "Taekyung’s three-day staged confinement ends; Wipeng escorts him to the main assembly hall instead of letting him return to his residence.",
    "The Mount Heng Sword Sect and the Jin Family of Taiyuan are sworn enemies; a Mount Heng envoy and Jin Family senior members await Taekyung at the assembly hall.",
    "Taekyung learns that his former self allegedly tried to rape a Mount Heng Sword Sect daughter; he denies it while relying on his supposed amnesia.",
    "Lee Seogeun is Lv. 30 and confronts Taekyung with intense killing intent and witness statements about the alleged Myeongwollu incident.",
    "The witness statements only claim Taekyung entered the wrong room while drunk and that someone heard screaming; Taekyung finds the evidence contrived.",
    "Lee Seogeun is the Mount Heng envoy and demands that the Jin Family withdraw from every commandery and county except Taiyuan; Jin Wikyung refuses the demand and the duel.",
    "Taekyung accepts the System’s Duel Quest to prevent the Mount Heng Sword Sect from declaring war and naming him a public enemy.",
    "During the duel, Taekyung blocks more than twenty of Lee Seogeun’s attacks, kicks his unguarded chest, and loses the Intimidation status effect.",
    "Jin Wikyung tries to intervene through Sound Transmission, but Wipeng restrains him."
  ],
  "open_questions": [
    "The capsule's purpose and the route home remain unresolved.",
    "The limits of Murim's death and resurrection rules remain unresolved."
  ],
  "temporary_decisions": [
    "The source name 성진호 is Seong Jinho; do not substitute the compendium's separate 송진호 entry.",
    "Preserve brisk dark action-comedy and character hierarchy without archaic wuxia diction.",
    "Use the accepted terms Heaven's Gate Temple, Three-Turn Footwork, Sound Transmission, Jin Family's Cultivation/Spear/Manoeuvre Techniques, and pleasure house.",
    "Preserve the gold-spoon/God-Spoon wordplay and explain it briefly in a footnote.",
    "Preserve the System titles Gambler and Sex Fiend, and render the Mount Heng demand as commanderies and counties."
  ]
}

## Reading copies

## Chapter artifact 10

# Chapter 10

After walking for more than ten minutes, we arrived at a cliff blocking off the rear of the Jin Family of Taiyuan. A massive cavern gaped open in its face. One person stood in front of it.

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

My mouth fell open the moment I saw it. Filling the passageway without leaving a gap, it looked less like a door and more like a wall forbidding all entry and exit.

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

There was a broad bed covered with a furry blanket that lifted my spirits just by looking at it. Instead of a damp, uneven stone floor, a neat gray surface stretched out before me.

*Cement… Obviously not. Limestone?*

Aside from the chill in the air—or even taking that into account—the environment was far better than I had imagined.

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
> - Remaining successful attempts (2 / 100)

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
> - Remaining successful attempts (5 / 100)

“Ah, fuck.”

In the end, I tossed the *Training Wooden Spear* aside and pulled a *Sharp Spear* from my inventory. Its length and shaft thickness were roughly similar to the spear I had used in the real world.

But why hadn’t I taken it out from the beginning?

“It’s insanely heavy. Seriously.”

Since it had been made entirely of steel, its weight was no joke. By feel alone, it was a monster weighing nearly fifty kilograms.

My Stamina couldn’t withstand swinging something like this for hours.

My current realm was Second Rate. Even with the System’s help, swinging around more than half a sack of rice as if it were a pinwheel was impossible.

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

The formula of the Jin Family’s Cultivation Technique, imprinted in my mind by the System, rapidly replayed itself and guided my internal energy along its prescribed path.

A prickling sensation ran through me.

The response was immediate.

The ten years of internal energy coiled in my dantian spread throughout my body. I could feel that energy—something I could sense because this was a game and I was a martial artist—spreading through every part of my body.

*This is…*

Strength overflowed through my entire body. My vastly improved physical abilities and senses once again filled me with exhilaration after a lifetime as an F-rank Hunter.

*How can a person change this much?*

I gripped the spear and began practicing the *Jin Family’s Spear Technique*. The fifty-kilogram iron spear no longer felt heavy. It thrust and slashed through the air along the paths I wanted it to follow.

Before long—

Ding.

> **System**
>
> - Remaining successful attempts (6 / 100)

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
## Chapter artifact 11

# Chapter 11

Whoosh. Fwoom—

The spearhead pierced dozens of sparkling points in the air one after another.

Each time I completed a movement, the red tassel hanging beneath the spearhead whipped around. It wasn’t there just for show. Its purpose was to distract the enemy’s eyes.

Bang!

Once again, the sound of the wind being torn apart rang out. It was the seventh and final form of the Jin Family’s Spear Technique: the Sky-Piercing Strike.

And this Sky-Piercing Strike was more precise and powerful than the ninety-nine I had successfully performed before it.

*This is it.*

My fingertips tingled. Each of the seven forms in the Jin Family’s Spear Technique was destructive enough when performed separately, but its true effect emerged when they flowed together.

If I compared it to a car race, the first form was starting the engine. The final Sky-Piercing Strike was crossing the finish line.

“Whew.”

I exhaled a hot breath and raised the spear upright.

Ding.

> **System**
>
> - Remaining successful attempts: (100 / 100)
>
> - You have acquired **Jin Family’s Spear Technique**.
>
> - As a result of repeated training, related stats have increased!
>
> - Strength, Stamina, and Agility have each increased by 1.

“Oh. My stats went up.”

So this was another way to improve my stats. Intrigued, I opened my Status Window.

Ding.

> **System**
>
> **Status Window**
>
> **Lv. 11 Jin Taekyung**
>
> **Job:** Second Rate martial artist
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
> **Strength:** 41  
> **Stamina:** 51
>
> **Agility:** 51  
> **Intelligence:** 10
>
> **Charm:** 10  
> **Internal Energy:** 10 years
>
> **Remaining Points:** 0

This was…

“What a fine Second Rate nobody.”

Still, it was better than reality. I could keep climbing higher. I no longer felt the limitations I’d sensed every day since awakening as an F-rank, or the glass ceiling society had placed over me.

“So what? I can’t even log out whenever I want.”

I sighed and sank to the floor. After training for several hours without a break, my body felt as heavy as a waterlogged cotton blanket.

“Ow. I’m exhausted.”

Ding.

> **System**
>
> - You feel fatigued and hungry. Consume food to restore your physical condition.

Yeah. I figured that would happen.

“Fatigue and hunger…”

The only answer was rest. Eat well and sleep well. But I didn’t have time to lie around leisurely scratching my belly.

If only I had some kind of recovery item…

“Oh, right. Grain-repelling pills.”

I took one of the grain-repelling pills from my inventory. It gave off a strange smell, but a professional Hunter couldn’t afford to be picky between cold rice and hot rice.

I opened my mouth wide and took a huge bite.

Then I thought,

*Should I just spit it out?*

It wasn’t merely tasteless. It tasted bad enough that my tongue screamed for mercy and my stomach hung up a no-entry sign.

But humans were capable of displaying superhuman willpower from time to time. I squeezed my eyes shut, chewed the grain-repelling pill thoroughly, and swallowed every last bit.

Gulp.

“Uuugh. I ate it. I actually ate it.”

If the System notification hadn’t sounded the next moment, I probably would have kept rolling around on the floor for quite a while.

Ding.

> **System**
>
> - You have consumed an **Excellent Grain-Repelling Pill**.
>
> - You feel full.
>
> - Your fatigue has been restored.
>
> - All stats increase by 2 for one hour.

“What?”

I hurriedly opened my Status Window. Every stat except Internal Energy had increased by 2. On top of that, my fatigue had lifted and my hunger was gone.

Feeling energized and full, I muttered,

“This is completely broken.”

Who would have thought such a foul-tasting lump of grain could have such incredible effects? Wait a second.

“Do the effects stack?”

Just one had increased my stats by a total of 10 points. What if I ate two? Three? No, ten?

*I’d eat goblin shit if I had to.*

Goblin shit might actually taste better… but it was definitely worth a try.

*I can do this. I can do this. Jin Taekyung.*

With trembling hands, I picked up a second grain-repelling pill.

And a short while later—

> **System**
>
> - You have consumed an **Excellent Grain-Repelling Pill**.
>
> - The effects do not stack.
>
> - You feel excessively full.
>
> - Your movements will be slowed for one hour due to **Overeating**!

I dropped to my knees as the System notification sounded.

“Bleaaargh!”

* * *

I could only resume training after my bloated stomach finally went down. I had three days to stay in the training hall. I needed to grow as strong as possible before leaving.

“Hah!”

With a short battle cry, the spearhead traced a heavy arc.

*Keep my stance low, my feet heavy, and my spear fast.*

The Jin Family’s Spear Technique was aggressive. It advanced while constantly pressuring the enemy. Its spear movements were simple but lethal.

*Was it derived from the military?*

I didn’t know what the game’s setting was, but it didn’t seem like a martial art an ordinary foot soldier could learn.

It was a First Rate martial art, after all, and required considerable physical ability to perform. Perhaps it had been practiced by elite soldiers or commanders.

*Compared with what I learned at the Hunter training camp, it’s like heaven and earth.*

That was when my foot tangled—whether from exhaustion or distraction, I wasn’t sure. Once my foot got tangled, my hands lost their rhythm too. The spearhead, loaded with strength, lost its momentum and sliced through the air.

Whoosh—

The System sounded at the same time.

> **System**
>
> - Jin Family’s Spear Technique Mastery increased by 1. (6 / 100)

“Only 1?”

My Mastery increased each time I performed the martial art from beginning to end. The amount I gained depended on the System’s evaluation, and this time, all I got was 1 because my feet had tangled so often.

“Why am I getting worse the more I do it?”

The third time I performed the Jin Family’s Spear Technique after acquiring it, I was getting worse and worse. The first time, I gained 3 Mastery. The second time, 2. This third time, 1.

“Three, two, one. It’s not even a countdown. What is this?”

The fourth attempt looked ready to give me no Mastery at all. I sighed and took hold of the spear again. My breathing was becoming increasingly ragged, but I performed the Jin Family’s Spear Technique once more.

Around the fourth form, I lost my balance and fell.

Ding.

> **System**
>
> - You did not gain Mastery for Jin Family’s Spear Technique. (6 / 100)

“This is driving me insane.”

I lay there and stared at the training hall’s ceiling, where stalactites hung overhead.

My feet kept getting tangled. I was performing the technique exactly as I had learned it, so why was this happening? Nothing like this had happened when I acquired it.

“What’s the problem?”

There was something that kept snagging me. I had to figure out what it was.

I got back up like a roly-poly and performed the Jin Family’s Spear Technique again. This time, I fell after only the third form.

> **System**
>
> - You did not gain Mastery for Jin Family’s Spear Technique. (6 / 100)

When I focused on my feet instead of the spear, the problem started to come into focus.

Good. One more time.

> **System**
>
> - You did not gain Mastery for Jin Family’s Spear Technique. (6 / 100)

Now I understood. But…

“Why is the Jin Family’s Manoeuvre Technique showing up here?”

I had struggled when I first learned it. I’d spent half a day practicing nothing but footwork. But if you asked whether it was enough to make me unconsciously mix it into my spear technique, the answer was no.

*If that were the case, I’d have mixed in every movement I’ve learned over seven years.*

I had learned spear fighting before, too. It was one of the basics taught at the Hunter training camp. Since it was distributed to F-ranks who couldn’t use mana, we called it shitty spear fighting among ourselves.

Compared with that, the Jin Family’s Spear Technique was good enough for intermediate Hunters.

“Should I give it a try?”

No matter how hard I racked my brain, all I’d get was a bald spot. The only way to understand a technique was to try it with my whole body.

I began performing the Jin Family’s Spear Technique slowly. At the same time, I performed the Jin Family’s Manoeuvre Technique with my lower body.

*The movements don’t flow naturally.*

They kept falling out of sync. But it was different. Until now, it had felt as if tangled threads were being pulled in every direction. This time, it felt as if gears were slipping past each other by a hair.

How many times had I tried?

Whoosh—Bang!

It was a simple thrust. For a moment, I wondered if I had performed all the way through the seventh and final form without realizing it, but it was only one movement from the fifth form.

“What was that?”

A shiver ran down my spine. For one brief moment, the footwork and spear technique had meshed perfectly. The spear in my hand trembled.

> **System**
>
> - You did not gain Mastery for Jin Family’s Spear Technique. (6 / 100)

I shoved the System notification into a corner of my mind and tightened my grip on the spear. Recalling the sensation from a moment ago, I stepped forward.

And again.

Swish—Whoosh—

*This is it.*

I felt it the instant I thrust the spear. The footwork and the spear technique. The two gears meshed perfectly.

Overwhelmed by indescribable pleasure, I turned those two gears again and again. My steps were fast and precise. The spearhead that thrust, slashed, and swung was fast, precise, and powerful.

My dantian grew hot. My internal energy became a ball of fire and seeped into the spear.

I had to release it.

*Right now!*

“Hah!”

The Sky-Piercing Strike—the final blow of the Jin Family’s Spear Technique, said to pierce the heavens—shot forward.

A deep, muffled boom erupted through the cavern.

Bang!

Dust rose, and stones scattered in every direction. The spear embedded in the training hall’s wall trembled. A massive hole had formed around the spearhead, which had plunged so deeply that it was no longer visible.

A hole? No.

This was a crater.

The sight was breathtaking.

“Huff, huff…”

The exhilaration sent a shiver down my spine.

*Fuck, it was me. I did it!*

I had unleashed that insane strike—the kind that could take down a troll in one blow.

Me!

I staggered.

*Huh?*

I needed to shout my head off and take a proof photo. I needed to put Big Brother Jinho in his place—he used to call me a freeloader.

*Oh, right. This was a game.*

My vision blurred. The strength drained from my body. An unbearable wave of sleepiness washed over me.

*I’m sleepy.*

I stopped thinking and surrendered my body to instinct. A familiar sound gradually faded into the distance.

Ding. Ding. Ding.

.

.

.

> **System**
>
> - All internal energy has been depleted.
>
> - You feel extreme fatigue.
>
> - You have completed the achievement **Unity of Self and Object**. A reward will be granted!
>
> - You have realized the connection between martial arts on your own. As a reward, the realms of your martial arts will rise substantially.
>
> - The realm of **Jin Family’s Cultivation Technique**…
>
> - The realm of **Jin Family’s Manoeuvre Technique**…
>
> - The realm of **Jin Family’s Spear Technique**…
>
> - Level up!
>
> - Level up!

* * *

> **System**
>
> - Sleep mode has ended.

I opened my eyes. The cave ceiling, with stalactites hanging from it, came into view.

*The training hall.*

How long had I been unconscious? Half a day? Or a full day?

I didn’t know. What mattered was that I was still in the game and had gotten plenty of rest.

*I feel great, too.*

My physical condition was strangely excellent. Come to think of it, I seemed to have heard System notifications just before I passed out.

“Open Message Window.”

The next moment, unread messages covered my vision. By the time I finished reading them all and sorting through my thoughts, more than ten minutes had passed.

I muttered a brief reaction.

“I really hit the jackpot.”

The Jin Family’s Manoeuvre Technique and Spear Technique had risen all the way to the Third Stage—two whole stages. The Jin Family’s Cultivation Technique had reached the Second Stage.

And on top of that…

“I went up two Levels?”

I was happy, but also bewildered. I hadn’t seriously expected to Level up in the training hall.

“Don’t you usually Level up by completing Quests or killing monsters?”

Apparently, learning martial arts and gaining insight like I had could also lead to a Level Up. Was it because this was a martial-arts game? It was definitely impossible to predict.

“No wonder my body felt so light.”

The Level Up effect must have restored my condition. The bruises and slight pain that had remained before I leveled up had vanished completely.

“Open Status Window.”

The Status Window had changed too. Reaching Level 13 had given me twenty remaining points, and the effects of training had slightly increased my Strength, Stamina, and Agility.

“Level 13…”

The Quest completion requirements were reaching the First Rate realm, Level 30, and 500 Fame.

I wasn’t progressing quickly, but I was steadily leveling up through training alone. That meant I was cruising along.

*Once I leave the training hall, I can spread my sails and surge forward.*

I smiled contentedly and distributed my points.

Now, all that remained was to check the reward I’d received for completing the Unity of Self and Object achievement.

“Open Inventory.”

> **System**
>
> - You have 1 new Item. Would you like to check it?

Yeah. Give it here.
## Chapter artifact 12

# Chapter 12

Was it about ten years ago? Back when I was in high school, several dozen ordinary people entered a Gate with government approval.

*China, I think.*

Gates were places where even Hunters became corpses if they let their attention wander, and they were sending ordinary people inside? It really was the Miracle Continent.

On the day of the expedition ceremony when this insane stunt took place, their identities were revealed during an interview with the overseas press.

The Chinese Martial Arts Alliance.

In other words, they were modern-day Murim martial artists. Made up entirely of non-awakened people, they solemnly declared their intentions toward hundreds of cameras, their robes fluttering in the wind.

*Today, the thousand-year martial lineage of China will be reborn in all its glory.*

It certainly was glorious. Their faces had been plastered across the front pages of all kinds of news outlets in less than half a day.

> **Chinese Martial Arts Alliance: Twenty-Five Members Massacred in an F-Rank Gate. More Than Half Confirmed Dead from Goblin Poison Needles…**

I didn’t know how impressive a thousand-year martial lineage was supposed to be, but the incident brought immense disgrace upon China, and the Chinese Martial Arts Alliance was left with nothing but its signboard.

*It got completely wrecked.*

Some of the most renowned martial artists on the continent were killed by goblin poison needles, and a tai chi master was beaten senseless by a mixed martial arts fighter.

That was reality. I had thought the scenes from novels and movies were fiction dressed up in media spectacle and mystery.

*But…*

Now, I wasn’t so sure. The movements Hyuk Mujin had shown me were *real*.

As I learned martial arts myself, my doubts gradually turned into certainty. There was nothing weak or floppy about the martial arts here, unlike in reality.

The martial arts of this world were systematic and involved countless movements. They couldn’t even be compared with real-world martial arts or boxing.

*How is this possible? Is it simply because this is a game?*

Ssshh. Hooouu.

Along with my breathing, I sensed the energy outside my body. Then I drew it in.

Compared to the ten years of internal energy rotating through my acupoints, it was nothing but a speck of dust—small and weak. But I was in no position to complain about even that.

*One circuit. Two…*

I continued circulating my qi according to the formula of the Jin Family’s Cultivation Technique. It was a natural action, as if I had been practicing it since childhood.

*Gyeonjeong, Amun, Bongan, Ip-dong…*

Names of acupoints I had never heard or seen in my twenty-seven years rose and vanished in my mind. Hundreds of acupoints had been engraved into my memory like that. Just how far did the System’s functions go?

*Now that I think about it, it’s downright bizarre.*

The human brain wasn’t a computer. But the System had entered the information into my mind as if it had copied and pasted a file. The other martial arts were the same.

Was a phenomenon like this possible? Simply because this was a game?

*No. For now, focus on circulating qi.*

I steadied my breathing again and guided my internal energy. Only after circulating the ten years of internal energy through twelve complete circuits according to the formula of the Jin Family’s Cultivation Technique did I open my eyes.

Ding.

> **System**
>
> - You have completed **Circulating Qi**.
>
> - **Jin Family’s Cultivation Technique** Mastery has increased slightly.
>
> - A small amount of turbid qi has been expelled.

“Whew.”

The Third Stage of the Jin Family’s Cultivation Technique was within reach. I didn’t know whether it was because I had started from the very bottom, but it felt like a fairly fast pace.

*Or it could be thanks to the Item.*

I looked at the ring on my right middle finger.

It was the Item I had received as a Reward for completing the **Unity of Self and Object** achievement.

> **System**
>
> **Item Window**
>
> **Clear-Heart Pill**
>
> **Type:** Ring
>
> **Grade:** None
>
> **Restriction:** None
>
> **Description:** A very hard ring made of a material that cannot be identified. It calms the wearer’s mind and helps with concentration.

The Clear-Heart Pill. Its form was different from the one I knew, but its effects were similar. After putting it on, the time it took me to settle into circulating qi had definitely shortened, and the Mastery I gained had increased.

*It’s good, but…*

I still felt uneasy. Logout was, well, something I could chalk up to the technical territory of engineering nerds beyond my understanding. But the martial arts formulas and this ring, the Clear-Heart Pill, were unsettling in a way I couldn’t quite explain.

*Was I supposed to call it the feeling of something being forcibly injected into me?*

Even if it helped me survive, it clearly wasn’t a pleasant experience. This game was a piece of shit in so many ways.

“What the hell was this Seong Jinho guy doing? That so-called goshiwon manager.[^1]”

If he’d gotten up, he should have woken me so we could at least have a bowl of hangover soup. And yet, the fact that nothing had changed even now meant…

*No. That’s not it.*

At the very least, I was still alive in the real world. That was why I could still exist in this game as a player.

I was alive in reality and in the game. And I would get out alive, no matter what. My life was too precious, and my burdens were too heavy, to die a pointless death like this.

*I can’t die here.*

I clenched my teeth and sat cross-legged. Perhaps it was the effect of the Clear-Heart Pill. My mind gradually settled, and my breathing steadied.

As the internal energy in my dantian began to move, I started yet another session of circulating qi.

* * *

It was the second day since I entered the training hall.

I devoted myself to training without stopping. I threw myself into the Spear Technique and Manoeuvre Technique like a madman, and whenever my internal energy was completely depleted, I immediately began circulating qi.

Ding.

> **System**
>
> - The realm of **Jin Family’s Cultivation Technique** has risen to the Third Stage.
>
> - Your internal energy has become purer, allowing for more efficient circulation of qi.

The Third Stage of the Jin Family’s Cultivation Technique. It had progressed more slowly than the other two, but it wasn’t bad. No, I was trying to think of it that way.

*I had to think of it that way if I was going to hold on.*

At least martial arts training allowed me to shake off my dark thoughts. For that, I was grateful.

Swish. Ssshk.

I performed the forms of the Jin Family’s Spear Technique in order. Ever since realizing its connection with the Jin Family’s Manoeuvre Technique, my attacks had grown more precise and sharper, sweeping through the empty space ahead of me.

I was projecting someone into that empty space.

*Hyuk Mujin.*

The first genuine martial artist I had met in this game. A Level 20 powerhouse who had toyed with me like a child.

*Could I beat that bastard in my current condition?*

That was the moment the question entered my mind.

Ding.

> **System**
>
> - A new function, **Training Mode**, has been activated.
>
> - You can summon illusions of opponents you have fought so far. However, opponents whose Level differs from the user’s by ten or more cannot be summoned.
>
> - Currently summonable opponents: **Lv. 20 Hyuk Mujin**, **Lv. 10 Cheon Ryeokbu**

“Huh?”

Training Mode? I could summon illusions of opponents I had fought so far? After hesitating for a moment, I decided to test the new function.

“Summon Hyuk Mujin.”

> **System**
>
> - Summoning **Lv. 20 Hyuk Mujin**.

The moment the System notification appeared, a transparent figure abruptly sprang into existence. He wore the navy martial uniform of the Jin Family of Taiyuan and had Hyuk Mujin’s distinctive caterpillar eyebrows. The figure stood with his eyes closed, looking exactly like Hyuk Mujin.

“Holy shit, it’s real.”

I carefully approached and touched Hyuk Mujin’s body. But perhaps because it was an illusion, my hand passed uselessly through him.

*Good. That passes the safety test.*

> **System**
>
> - You can partially alter the summoned target’s abilities.

“For now, make him about half as strong as Hyuk Mujin.”

> **System**
>
> - Entering the data for **Lv. 20 Hyuk Mujin**. The illusion can use 50% of the original’s abilities.

At the same time, Hyuk Mujin’s illusion opened his eyes. Perhaps his personality had been copied along with his abilities, because he looked at me with the same insolent gaze.

> **System**
>
> - Would you like to begin training?

“Of course!”

Ding.

The System notification was the starting signal. I charged forward like lightning and thrust my spear. Even though I was fighting an illusion, I poured out my internal energy without holding anything back.

*First form.*

It began with a thrust as I advanced, followed by a twist of the spear shaft. If the enemy couldn’t evade the first attack, the fight was already over.

Ssshwip—

But Hyuk Mujin slipped away with the movement of a loach. The next movement became meaningless.

*Let’s see if you can dodge this, too.*

I continued unleashing the Spear Technique. The sound of wind splitting filled the air, but Hyuk Mujin dodged every attack.

For an instant, it seemed a sneer crossed his opaque face.

*How can you fight so stupidly? A martial artist ought to use martial arts.*

Those were the words he had used when he toyed with me last time. He was nothing more than an illusion I had created, but…

*God, that’s pissing me off.*

*If you’re so confident, stop dodging and come at me.*

Hyuk Mujin picked up on my thought and rushed at me in a smooth glide. But this was a fight between a spear and a fist. If I let him land that attack, it would mean I had spent the last seven years digging holes for nothing.

“Where do you think you’re going!”

Whoom—

I swung the spear shaft. If the illusion had been real, it would have made a solid *thwack*. Even if he had dodged it, he would have failed to close the distance.

*Let’s see how far you can dodge.*

This form began. Faced with the torrent of attacks, Hyuk Mujin didn’t even dare to approach. He retreated step after step.

Combat had a flow. I had caught that flow, and Hyuk Mujin had been swept along by it. Looking at Hyuk Mujin rolling across the ground with an exhausted expression, I thought,

*He’s weak.*

I could see his movements. The Hyuk Mujin projected here was a fist fighter. I could tell how he would move by watching his feet, and I could predict his next action. His fists couldn’t reach me.

Ssshk-swish-swish!

In a single instant, I thrust three times in succession. It was an attack F-rank Hunter Jin Taekyung couldn’t perform. But Jin Taekyung the Murim martial artist, drawing on internal energy, could.

- Kraaagh!

Hyuk Mujin seemed to scream as the spear pierced his chest.

Without hesitation, I shoved the spear deeper and twisted it. The spearhead crushed through his breastbone and split his heart. The fallen Hyuk Mujin slowly faded away.

“Ah. This is way too easy.”

The fight had already been decided in less than five seconds.

I had even held the upper hand throughout the entire battle, only for it to end anticlimactically.

*Was half just too weak?*

I fell into thought while recovering the internal energy I had depleted by circulating qi.

Hyuk Mujin was Level 20 and a martial artist who had trained in martial arts for at least several years. There was no way he could be this weak.

*All right. Again.*

I stood up with the spear in my hand and closed my eyes, imagining a new Hyuk Mujin.

A height of 180 centimeters. Lean muscles and insolent eyes. I infused him with the movements I had seen back then. When I opened my eyes, an illusion exactly as I had imagined stood before me.

But it still wasn’t over. Hyuk Mujin had to be stronger.

*Your physical abilities are superior to mine.*

After I fed in a few more conditions, Hyuk Mujin’s illusion smiled pleasantly. He had become much faster and gained stamina that would never run out.

“Yeah. Now this is worth fighting.”

Those words were the starting signal. I thrust my spear at Hyuk Mujin as he charged toward me like a ray of light.

Ssshk-swish!

* * *

Vroooom. Boom!

The spearhead tore through the air. The air burst with the sound of a swarm of bees, bringing a gust of wind with it. It was the final form of the Jin Family’s Spear Technique: Cheongwanil.

- Kheugh…

Hyuk Mujin’s illusion looked down at his gaping chest. His eyes held pure disbelief. Then his knees buckled, and the illusion scattered.

“This isn’t right.”

I scratched my head roughly as I heard the message that my Mastery of the Jin Family’s Spear Technique had increased.

*Why am I still winning?*

Had the System made a mistake, or…

*Did I simply become stronger?*

I brushed the thought away as soon as it came to me. That couldn’t be it. I wasn’t some peerless genius. I had only learned a couple of martial arts.

*At this rate, this isn’t very useful.*

This was supposed to be a simulation for testing what happened when I fought a powerful opponent. If I kept winning, what was the point?

If I at least knew which martial arts Hyuk Mujin had learned, I could draw out their power. But wait.

“There’s an easier way.”

The Jin Family’s Manoeuvre Technique and Spear Technique. What if I grafted those two onto the Level 20 Hyuk Mujin?

I might even be able to identify their strengths and weaknesses from a third-party perspective.

Yeah. That would be better.

“You think so too, right?”

Hyuk Mujin’s illusion had reappeared at some point. It grinned and nodded.

“Then let’s fight again.”

I raised the spear diagonally and took one step forward with my left foot. The illusion assumed the same stance as if it were looking in a mirror.

- You’ll regret this.

“Regret, my ass.”

I was even talking to an illusion now. Anyone who saw me would have no choice but to call me a certifiable lunatic.

- Crazy bastard.

…It was my imagination, but it still pissed me off.

“You’re dead.”

Without hesitation, I pointed the spear at him.

Same weapon. Same martial arts. It looked like it would be an interesting fight.

- Interesting? You really are a lunatic.

Yeah. I suppose so.

Finding this fun in a situation like this meant I was pretty damn crazy, too.

[^1]: A goshiwon is cheap boarding made up of tiny private rooms, often rented by exam students.
## Chapter artifact 13

# Chapter 13

The five horses ran hard. They passed mountains, fields, and rivers, finally reaching their destination around noon.

“Where are you coming from?”

At the tense question from the Jin Family of Taiyuan’s gate guard, the young man in the lead smiled. Hostility he could not hide seeped from his crooked, lifted lips.

“Mount Heng.”

Jin Wikyung summoned the family’s senior members fifteen minutes later.

* * *

Hyuk Mujin was endlessly changeable. All I had to do was picture him in my mind. Spear, sword, saber, bow… There were times I won and times I lost, but one thing was certain.

“I’ve got the hang of it now.”

The martial arts had become second nature. At first, I had focused on executing them from beginning to end, one form after another. But things were different now.

The forms changed depending on the situation. Martial arts didn’t have to consist of one form flowing into the next in a fixed order. I had reached the point where I could skip the prescribed sequence and link forms together.

*Like this.*

Whoooosh!

By the time I heard the sound of the wind, it was already too late. Hyuk Mujin, his abdomen pierced through, let out a rueful sigh.

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

After distributing my remaining points, the tip of my nose began to sting for some reason.

> **System**
>
> **Status Window**
>
> **Lv. 14 Jin Taekyung**
>
> **Job:** Second Rate martial artist
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

The F-rank Hunter Jin Taekyung, who didn’t know the first thing about martial arts, was dead. I was now a Murim martial artist who had learned a Peak cultivation technique and two First Rate martial arts.

*It starts today.*

Everything was ready. Once I left the training hall today, I would gather the things I had in mind and leave the Jin Family of Taiyuan.

*I might even be able to get Jin Wikyung’s help.*

I could reach my target quickly just by dealing with idiot bandits like Cheon Ryeokbu. Two days at most. After that, I could return to my warm family.

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

“...What?”

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

That was the Level I had read with Qi Sense the instant I detected his killing intent. It was more than twice my Level.

*This is insane.*

Even worse were the looks from everyone else.

Dozens of sinister gazes, young and old alike, were fixed on me. My knees began to tremble. In that atmosphere, Lee Seogeun opened his mouth.

“What a shame. If you had come a little earlier, we could have had a deeper conversation. We were discussing something interesting until just now.”

“...Were you?”

“Wouldn’t you like to know what we were discussing?”

“N-no, I’m fine.”

I only hoped it wasn’t a discussion about whether to cut off my head or my balls. And if that miserable guess was correct, I preferred them to cut off my balls instead of my head.

*I might be able to recover with a Level Up if they did that… Why am I even thinking about this?*

It was simply miserable. Lee Seogeun studied my expression before speaking again.

“I heard you returned to the family a few days ago. Where have you been?”

“Honghwaru.”

“Then where were you before you went to Honghwaru?”

*I was at a goshiwon, you bastard.[^1]*

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

[^1]: A goshiwon is a very small, inexpensive room-for-rent.
## Chapter artifact 14

# Chapter 14

“Come out with me, you bastard! I’ll make you pay for what you’ve done!”

The instant Lee Seogeun shouted those words, filled with fury—

Ding.

> **System**
>
> **Quest**
>
> **Duel**
>
> Your debauchery has finally caught up with you!
>
> A man must deal with his own mess. To protect the tiny scrap of honor you have left and to avoid the anger of the Mount Heng Sword Sect, only one option remains.
>
> **Type:** Sudden Quest  
> **Grade:** First Rate  
> **Restriction:** Jin Taekyung  
> **Mission:** Win the duel (Incomplete)
>
> **Reward:** Title: **Gambler**
>
> - A large amount of EXP
> - Fame 50
>
> **Failure:** Title: **Sex Fiend**
>
> - Injury
>
> Would you like to accept the **Duel** Quest?
>
> **Accept** / **Decline**

“……”

Seriously? I hadn’t even dated anyone since high school, and I had to be called a sex fiend?

I spent half my day on raids and collapsed asleep in my goshiwon every night. Now I had to clean up a mess I hadn’t even made in a game.

*At least give me a decent Quest.*

How was I supposed to fight a Level 30 like Lee Seogeun?

*This is insane. The Level gap is more than twice mine…*

This was a fight I absolutely could not take.

I declined the Quest. Or I was going to. But Lee Seogeun beat me to it.

“If you run away from this place… the Jin Family of Taiyuan will pay the appropriate price.”

Ding.

> **System**
>
> - Quest information has been updated.
>
> - If the Quest is declined, the **Mount Heng Sword Sect** will declare war on the **Jin Family of Taiyuan**. In addition, **Jin Taekyung** will be designated a public enemy of the sect.

*…I knew it.*

I had wondered why the System was giving me a choice for once.

As I let out a deep sigh, the assembly hall was boiling like a cauldron over charcoal.

“How dare you!”

“That young punk thinks he can say anything because he has his family’s backing!”

“Even if the Third Young Master did something lower than a dog, how dare he look down on our family!”

“……”

The first two were fine, but who the hell was that last guy?

As the atmosphere turned hostile, Jin Wikyung, the Lesser Family Head, stepped forward.

“Everyone, calm yourselves. And you, Young Hero, enough. Let us consider this a verbal slip and let it go this once.”

Seated in the place of honor, he issued the warning in a low voice. His presence was no joke. He really did have the bearing of the next Family Head of a prestigious house with deep roots.

Perhaps cowed by that aura, Lee Seogeun answered in a noticeably quieter voice.

“Understood. However…”

“However?”

“It was not a verbal slip. Do you think I came here as a private individual?”

At those words, Jin Wikyung’s expression hardened, along with everyone else’s.

Right. Lee Seogeun was an envoy officially sent by the Mount Heng Sword Sect.

“My father—no, the Sect Leader—has entrusted me with all authority.”

“……Then what is it you want?”

“As I already said, I want a duel with the Third Young Master.”

*No. I don’t want that.*

Judging by how things were unfolding, those bastards from the Mount Heng Sword Sect had come here looking for a fight.

They intended to get as much as possible out of this incident, and even if that failed, they were going to wreck me, at least. Being targeted so blatantly sent a chill down my spine.

“There must be another way. Tell me what you truly want.”

“Withdraw from every commandery and county except Taiyuan. That should be an appropriate price for ruining my sister’s chances of marriage.”

The instant he finished speaking, shouts erupted throughout the assembly hall.

From the bits and pieces I could make out, he was basically saying they intended to strip us of everything but our underwear. Jin Wikyung’s answer was obvious.

“Impossible.”

“Then accept the duel—”

“That too, I must refuse.”

Jin Wikyung was a complete pushover when it came to his youngest brother. There was no way he would push me into a duel that was obviously dangerous.

At Jin Wikyung’s answer, Lee Seogeun smiled triumphantly.

“Then there is only one path left.”

War.

I wasn’t the only one who thought of that word. The assembly hall fell silent beneath the weight of it.

Amid that silence, I looked up at the empty air.

> **System**
>
> Would you like to accept the Quest?
>
> **Accept** / **Decline**
>
> - If the Quest is declined, the **Mount Heng Sword Sect** will declare war on the **Jin Family of Taiyuan**. In addition, **Jin Taekyung** will be designated a public enemy of the sect.

I read the System message, looked at the floor, looked at the ceiling, and then read it again.

*Fuck…*

There was no choice. Only one way remained.

“I’ll do it.”

Everyone reacted the same way this time. Wide eyes. Open mouths. Lee Seogeun, who had proposed the duel. Jin Wikyung, who had refused it. Every person in the assembly hall looked as if they doubted their own ears.

“W-wait. Taekyung?”

I left Jin Wikyung’s frantic attempt to stop me behind me and spoke to Lee Seogeun.

“Come out. Let’s have a go.”

The corners of Lee Seogeun’s mouth rose cruelly.

* * *

The winter wind was cold. I took a deep breath while looking up at the cloudy sky.

“Whoo.”

The place where I stood facing Lee Seogeun was the Jin Family of Taiyuan’s main training ground. About fifty people sat some distance away, watching us.

The Jin Family people wore expressions that seemed to ask what the hell I had eaten, while the Mount Heng Sword Sect’s goons looked as if they had come out for a day of entertainment. The only thing missing was popcorn.

Ah. Someone was sending me Sound Transmission, too.

- Little brother. Deep breaths. Deep breaths. In. Out. In. Out…

*I’m doing it, man.*

Jin Wikyung had a solemn expression, but he kept shifting his hips like a puppy that needed to poop. If Wipeng hadn’t been holding him down by the shoulder, he looked ready to charge into the training ground at any moment.

- Don’t worry. If it looks dangerous, this eldest brother of yours will jump in. What? If that bastard so much as lays a hand on our youngest brother, I’ll—fuck! Got it? Don’t get worked up. Take it slow and stay safe. You can do it, Jin Taekyung!

*……I get it, so calm down.*

He had radiated such overwhelming force in the assembly hall, yet Jin Wikyung was once again living up to my expectations.

*Still, he’s a hundred times better than having no one.*

At least someone would save me before I became a half-crippled wreck.

With Jin Wikyung and Wipeng, I had two life insurance policies. Excellent.

But the moment I looked at Lee Seogeun with that slightly lighter feeling, I withdrew my thoughts.

*What’s so excellent about this? Fuck.*

Now I understood why the Mount Heng Sword Sect’s people had been so confident.

Lee Seogeun suddenly stripped off his upper garments, and my breath caught at the muscles writhing like some kind of mollusk.

> **System**
>
> **Lv. 30 Lee Seogeun**

My hands and feet began to tingle at the sight of the blood-red Level window.

A full sixteen-Level difference. It was overwhelming. As if to drive that fact home, the System rang.

Ding.

> **System**
>
> - You have been afflicted with the Status Effect **Intimidation**!

*I’ll die three times before anyone gets here to save me.*

Perhaps he noticed my reaction, because Lee Seogeun gave me a cruel smile.

“Do you understand the situation now? Your breath is caught, and your hands and feet are tingling, aren’t they?”

He could read minds now, too?

But momentum was half the fight.

I deliberately composed my expression before answering.

“Bullshit.”

“Your voice is trembling. Of course you’re afraid. Fine. If you answer my questions honestly, I’ll go easy on you.”

……To be honest, I almost wavered.

“Cut the bullshit.”

“Oh? Putting on the airs of a martial family’s son, are you?”

Lee Seogeun laughed as if I were ridiculous.

“Let me ask you one thing. What made you accept the duel? You, whose martial arts are pathetic and who is infamous for being a coward. I want to hear the reason.”

“The reason?”

No matter how much I thought about it, this was the only way.

If war broke out, I would become a public enemy of the Mount Heng Sword Sect.

Hunting? Leveling up? I could forget about it. The moment I left the fence of the Jin Family of Taiyuan, assassins who caught my scent would come running.

*As long as I stay alive, there will be another chance.*

I had magic. The recovery magic of leveling up.

My mind eased slightly.

“I thought someone like you might be manageable.”

“Pfft! You’re just a wet-behind-the-ears pup.”

It was a light provocation, but it didn’t work. He was confident in his own abilities, and it showed in his relaxed manner.

“Is it my turn to ask questions now?”

“I never said I’d answer them… but I’ll indulge you as if they were your last words.”

“This incident. You fabricated it, didn’t you?”

Perhaps the question was unexpected, because Lee Seogeun’s expression stiffened awkwardly.

That expression was answer enough.

*There it is.*

I had wondered if that was the case, but sure enough. No wonder the whole thing had smelled rotten from beginning to end.

“You petty bastards. You should have just declared war.”

“……I’ll tear that mouth apart.”

Lee Seogeun lifted a massive greatsword and muttered ominously.

I raised the Sharp Spear I had already drawn.

*All right. Let’s do this.*

I had learned martial arts. I also had instincts honed by seven years of real combat.

An F-rank Hunter and a Second Rate Murim martial artist. Don’t underestimate the skills I had honed working two jobs!

“Graaah!”

Lee Seogeun was more agile than I had imagined. He closed the distance in an instant, and I blocked the greatsword crashing down vertically with the shaft of my spear.

Kra-kra-kraang.

“Urgh.”

I had wondered if I would be split in two, but the Sharp Spear was sturdy as a solid piece of steel. However, the force behind the greatsword began driving both my feet into the ground.

“Die, you insect!”

“Hup!”

Up close, his aura was even more suffocating. Was this what a monster’s Fear felt like?

“Kneel and beg for forgiveness now! Then I’ll let you off with one arm!”

- Little brother!

Over Lee Seogeun’s shoulder, I saw Jin Wikyung spring to his feet. The Mount Heng Sword Sect’s people watched while snickering, and the Jin Family people turned their heads away as if they couldn’t bear to watch.

*I have to hold out.*

At least until Jin Wikyung got here!

“Graaah!”

Lee Seogeun’s greatsword struck from every direction in a blurring barrage. The weapons were clearly clashing iron against iron, but all I could hear was the sound of cannons.

Boom! Boom! Boom! I blocked them.

“Graaah!”

“Hup!”

Boom! Boom! I blocked them again.

“Graaah!”

“Haaah!”

Boom! I blocked another.

“Graaah…”

“Haaah…”

“……?”

“……?”

The next moment, Lee Seogeun and I met each other’s eyes.

The moment I saw the bewilderment and confusion in his gaze, I knew he was thinking exactly what I was.

*What the hell is this?*

Lee Seogeun was strong. He possessed the brute strength of a giant monster, moved with surprising agility for someone with that much muscle, and swung his massive greatsword like a matchstick.

And that wasn’t all. He was a Young Master of the Mount Heng Sword Sect—a sect that could actually throw its weight around. The martial arts he used had to be quite advanced.

And yet…

*This is… doable?*

Even now, I was blocking each and every strike of the continuously swinging greatsword. More than twenty attacks. And more than twenty blocks.

I could see them. That was why I could block them.

I slowly lifted one of my legs, which had been buried in the ground up to the ankle. It came free with ease.

*Could this be…*

No way. Surely not.

Ssshwip!

At that moment, I redirected the greatsword flying toward my waist along the shaft of my spear. Then, without thinking, I kicked Lee Seogeun in his unguarded chest.

Whack!

“Urgh!”

……Huh?

Lee Seogeun slid back five or six steps while clutching his abdomen. Then he casually rubbed the bridge of his nose as if nothing had happened.

“You’re not bad. You’ve got a trick or two, despite being trash.”

“……”

“Heh. I won’t hold back anymore.”

“……Hey.”

“With my next strike, I’ll smash your head—what?”

With a queasy look, I raised a hand and pointed at his mouth.

“You’re bleeding.”

A beat later, a thin line of blood ran down from the corner of Lee Seogeun’s mouth. He had probably bitten his tongue. That had to hurt.

“Ah! Eeng! Eek! Hup!”

Lee Seogeun wiped away the blood while letting out some ridiculous yelps.

“Don’t wipe it. Leave it.”

“……?”

“It’ll be easier to wipe it all off at once later.”

Because from now on, I was going to beat the absolute shit out of him.

> **System**
>
> - The Status Effect **Intimidation** has been removed!
