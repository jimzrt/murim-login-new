# Checkpoint Review — 5–9

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

## Durable state

{
  "version": 1,
  "safe_through": 9,
  "continuity_sources": [8, 9],
  "active_continuity": [
    "Jin Taekyung is trapped in Murim through an old game capsule; death is presented as permanent and he cannot log out at will.",
    "Taekyung is the disgraced third son of the Jin Family of Taiyuan and narrates with dry, self-mocking, occasionally profane humor.",
    "Logout is the Main Quest reward for reaching First Rate, Lv. 30, and 500 Fame.",
    "Taekyung is Lv. 11 after assigning his ten new points to Stamina; Qi Sense detects targets through Lv. 30 within ten jang.",
    "Hyuk Mujin is Lv. 20; after their fight both he and Taekyung were taken to the Medicine King Hall.",
    "Jin Wikyung is Taekyung's thirty-five-year-old eldest brother and the Lesser Family Head of the Jin Family of Taiyuan; Wipeng is his trusted guard.",
    "At the Medicine King Hall, Taekyung pretends to have amnesia, and Jin Wikyung believes him.",
    "Jin Mukyung is twenty-five, the Heaven Shaking Sword, and a cadet at Heaven's Gate Temple.",
    "Taekyung has four martial arts learned; the System displays ten total martial-art slots, and he finds several hundred manuals in his residence.",
    "Taekyung is practicing the Jin Family's Manoeuvre Technique and earns the Novice Trainee title after completing its movement sequence one hundred times.",
    "Taekyung asks for a practice room; Jin Wikyung orders indefinite confinement in the training hall to shield him from the Elder Council. Wipeng promises release within seven days, and Taekyung negotiates three.",
    "Taekyung deliberately left a second mass of unassimilated internal energy untouched while circulating qi."
  ],
  "open_questions": [
    "The capsule's purpose and the route home remain unresolved.",
    "The limits of Murim's death and resurrection rules remain unresolved."
  ],
  "temporary_decisions": [
    "The source name 성진호 is Seong Jinho; do not substitute the compendium's separate 송진호 entry.",
    "Preserve brisk dark action-comedy and character hierarchy without archaic wuxia diction.",
    "Use the accepted terms Heaven's Gate Temple, Three-Turn Footwork, Sound Transmission, Jin Family's Cultivation/Spear/Manoeuvre Techniques, and pleasure house."
  ]
}

## Reading copies

## Chapter artifact 5

# Chapter 5

“One, be good. Two, live. Come on, one.”

“Be good!”

“Two.”

“Live!”

“Louder.”

“Be gooood!”

*Is this hell?*

That was the first thought the coachman had when he came to. His body felt as heavy as waterlogged cotton, and his head was spinning. All the while, a distant cry that sounded like a scream continued without pause.

“Liiive!”

“Louder!”

*…It has to be hell.* Whenever the merciless voice of a grim reaper rang out, the screams of the dead followed without fail.

“Be gooood!”

With his eyes closed, he shed tears of bitter regret. He had ended up in hell. If he’d known he would die such an untimely death, he would at least have donated more to a temple.

*Oh, Mother!*

The coachman began to sob. He was so absorbed in his grief that he failed to notice someone quietly looking down at him.

“Excuse me.”

For one brief instant, the coachman’s heart stopped. Then it began pounding again. Clutching his chest, he shouted in alarm.

“You nearly scared me to death!”

“……”

“…?”

Now that he’d said it, something seemed off. The coachman stared blankly down at his chest and placed a hand over it. It was beating. His heart was beating.

And that wasn’t all. There were horses. There was a carriage. The cold wind of early winter made his body shiver.

“I’m alive?”

He turned around, scarcely daring to believe it, and saw a man standing there with one eye swollen purple. His expression was strange, but there was no doubt about it. He was alive.

*I’m alive!*

“I survived! I’m alive!”

The man pushed the coachman away from his exuberant embrace and answered awkwardly.

“Congratulations.”

“Sniff. Sob. Thank you, truly. But who are you…?”

“Ah, that. We met briefly earlier.”

*Earlier? Who was he talking about?* The coachman knew everyone from Honghwaru by sight, and today’s first guest had been the wastrel of the Jin Family of Taiyuan.

*Where had he seen this traveler he was so grateful to before?* The coachman stared intently at his face, then suddenly sucked in a breath.

“That bandit from earlier!”

“Yes. That was me—”

“The one standing next to the big guy! Those five idiots who look like morons!”

“…That’s right.”

“The shortest one of them!”

“……”

“The ugliest one!”

“……”

“And the one with the smallest package!”

“No, I’m not!”

The bandit’s shout finally brought the coachman to his senses. *What did I just say?* Regret and despair soon surged over him like a rising tide.

*I’m really dead this time.*

He almost wished he had already died. At least then he wouldn’t have to suffer.

But then—

“Ha. Enough nonsense. Just follow me.”

The bandit, who had looked like a ferocious demon, calmed down in an instant and started walking ahead. The coachman followed him before he knew what he was doing, feeling a strange sense of déjà vu.

*This feels like I’m being shown around.*

Compared to before he passed out, the bandit’s attitude was not merely subdued—it was downright polite. Mustering all his courage, the coachman opened his mouth.

“Um, where are we going?”

“To the boss.”

The coachman’s face went white. He remembered what he had said to the Heavenly Axe. *I’ll gouge out your eyes, grind your limbs to powder in a mortar…*

*I need to run. Right now.*

But the next moment, his legs began to tremble, and cold sweat poured down him like rain. He couldn’t move even one step.

Dark red blood splattered in every direction. A leg that looked like it belonged to a corpse jutted out from the grass beside the road.

*These lunatics.*

He had feared as much, but they had actually killed someone in broad daylight—and not just anyone, but a young master of the Jin Family of Taiyuan. The coachman could feel death closing in.

Until someone emerged from the grass.

“Oh, you’re awake?”

Behind him, the bandits were panting with their arms slung over one another’s shoulders.

Each of them sported a matching bruise around one eye.

“What are you doing, punk? Can’t you see your comrades are working themselves to death? Get over here.”

“Yes, Boss.”

“You little bastard. How many times have I told you not to call me that?”

The coachman watched the scene in a daze and thought:

*At least I’m still alive.*


* * *


“So that’s what happened.”

The coachman’s eyes lit up like flashlights as he listened to the story.

*Ow. That glare. I can barely look him in the face.*

“Um, excuse me.”

*What now?*

“Are you really Young Master Jin Mukyung?”

“…Please, stop.”

*How many times do I have to tell him? I’m Jin Taekyung.*

He was an NPC who drove me insane in every possible way. I couldn’t decide whether to call it a triumph of artificial intelligence or a failure.

*If I’d known how to drive a carriage, I would have ditched him ages ago.*

“Are you all set?”

The coachman answered as he tied the final knot.

“Yes. Everything is ready.”

What knot, you ask? The rope binding the hands and feet of the five bandits. It had been tied so tightly that their mournful groans never stopped.

“Boss. Could you loosen it just a little?”

“Nope. Not happening. I’m not loosening them. Stay right there.”

“Please, Boss. Give your little brothers the chance to serve you—”

“Call me Boss one more time, and I’ll give you the chance to serve the King of the Underworld.”

Leaving their silence behind, I climbed into the carriage.

I had confiscated the bandits’ weapons long ago and placed them in my Inventory, and the level-up effect had restored me to perfect condition.

“We’re leaving.”

The coachman took up the reins, and the four-horse carriage began to move.

The mountain road was as well maintained as a local hiking trail. Cool air and the scent of the forest drifted in through the carriage window.

*It’s incredible, no matter how I look at it.*

I shook my head.

Science. Technology. Whatever you wanted to call it, it was beyond my comprehension.

Besides, worrying about that was a luxury in my current situation.

*Damn it. What kind of time ratio does this game have?*

Virtual-reality games had something called a time ratio. If the ratio between reality and virtual reality was one to three, three hours in virtual reality would mean only one hour had passed in the real world.

That was why I had forced myself to hold out at Honghwaru for three days.

*Someone will come get me by then.* That was the hope I’d been clinging to.

*What the hell is Seong Jinho doing?*

A deep sigh escaped me. At the same time, a sliver of unease began to surface.

*What if the time ratio is wildly different?*

*No way.*

It couldn’t be. Jinho had once told me that a capsule’s time ratio was proportional to its performance and price. A piece of junk like this had no chance of having an extreme ratio.

Though it was performing better than I’d expected.

*No. For a piece of junk, it’s performing unbelievably well.*

I hadn’t played a game in years, but I wasn’t so clueless that I couldn’t recognize that. *Murim* was clearly a high-spec game, yet this old capsule was running it without any trouble.

That alone was astonishing. Which meant—

*Stop giving me new things to be astonished by.*

Please. I muttered the words like a spell and opened my Skill Window.

> **System**
>
> Skill Window
>
> LV. 11 Jin Taekyung
>
> Cultivation Technique: Jin Family’s Cultivation Technique
>
> Martial Arts: Jin Family’s Spear Technique / Jin Family’s Manoeuvre Technique (Unavailable)
>
> Bones: 70
>
> Sinews: 50
>
> Remaining Points: 10
>
> - Distribute your remaining points.
>
> - You have forgotten the formulas because you have not trained in martial arts for a long time.
>
> - You can view information about your acquired skills.

It was astonishing even after seeing it a second time. I couldn’t use my martial arts because I hadn’t trained?

*How much had this guy slacked off?*

With a sigh, I moved on. The first thing was the remaining points.

It seemed I received ten points every time my Level increased by one. The Status Window probably worked the same way.

*If I combine the Skill Window and Status Window, do I get twenty points every time I level up?*

The number felt oddly ambiguous. I put off distributing my points and touched the final sentence.

> **System**
>
> Would you like to view information about your acquired skills?

*View all.*

Ding.

> **System**
>
> Skill Window
>
> Jin Family’s Spear Technique
>
> **Grade:** First Rate
>
> **Restriction:** Those who have learned Jin Family’s Cultivation Technique
>
> **Realm:** Unknown
>
> **Effects:** Unknown
>
> **Description:** The Jin Family of Taiyuan’s hereditary martial art. Can be learned through a martial arts manual. The formula has currently been forgotten, so it cannot be used.
>
> Skill Window
>
> Jin Family’s Manoeuvre Technique
>
> **Grade:** First Rate
>
> **Restriction:** Those who have learned Jin Family’s Cultivation Technique
>
> **Realm:** Unknown
>
> **Effects:** Unknown
>
> **Description:** The Jin Family of Taiyuan’s hereditary martial art. Can be learned through a martial arts manual. The formula has currently been forgotten, so it cannot be used.

>
> Skill Window
>
> Jin Family’s Cultivation Technique
>
> **Grade:** Peak
>
> **Restriction:** Direct descendants of the Jin Family of Taiyuan
>
> **Realm:** 2nd Mastery
>
> **Effect:** Allows you to circulate and accumulate internal energy through Circulate Qi.
>
> **Description:** Exceptionally stable, but slow to accumulate internal energy.

*Hmm.*

The first thing that caught my eye was the grade.

The Spear Technique and Manoeuvre Technique were First Rate. Only the Jin Family’s Cultivation Technique was Peak. It was also the only one with a clearly listed realm and effect.

*I haven’t even tried the Spear Technique or Manoeuvre Technique. And the Cultivation Technique…this is pretty good.*

Who cared how fast my internal energy accumulated? Exceptionally stable—that was all I needed. My motto in life was to keep my head down and live a long time.

That was when—

> **System**
>
> Quest
>
> Tutorial—Stage 4
>
> You can now use Circulate Qi to control internal energy.
>
> However, uncontrolled internal energy is a double-edged sword.
>
> Do not let your guard down until the very end!
>
> **Grade:** Tutorial (Final)
>
> **Restriction:** First-time player
>
> **Objective:** Circulate Qi (Incomplete)
>
> **Reward:** Item Chest
>
> Qi Sense acquired
>
> Main Quest unlocked
>
> **Failure:** Status Effect Qi Deviation or Death
>
> Would you like to accept the Quest?
>
> Accept / Decline

I answered without hesitation.

*Nope. I’m not doing it.*

A reward? I didn’t need some lousy reward. There had to be a limit to this kind of bullshit. Were they seriously trying to bargain with my life over some game items?

> **System**
>
> - Your response is being delayed.

*Look at it trying to pull a cheap trick.* I ignored the coachman’s stare and enunciated each word.

“De-cline.”

> **System**
>
> - Tutorial Quests cannot be declined.

“…?”

> **System**
>
> Would you like to accept the Quest?
>
> Accept / Accept

“I said decline! Why are both options Accept?”

> **System**
>
> - Quest forcibly accepted!

“Hey! You sons of bitches!”

The profanity I had been holding back finally exploded out of me.


* * *


> **System**
>
> - Starting Circulate Qi.
>
> - The effect of Jin Family’s Cultivation Technique greatly increases stability.

I had never missed my family as much as I did then. My beloved mother. My adorable little sister…or rather, my pain-in-the-ass little sister, Hayeon.

*When I get out, your big brother will buy you enough fried chicken to make your stomach burst.*

*If I ever get out.*

> **System**
>
> - The Circulate Qi Helper will run for the first time only.

This wasn’t a case of stabbing someone and then applying medicine to the wound…

> **System**
>
> Would you like to skip the Helper System?
>
> Accept / Decline

I fixed my trembling gaze on the message window.

“D-Decline.”

> **System**
>
> - Continuing execution.

*That was a coincidence, right? Yeah. It had to be.*

Before my uneasy feeling had even faded, my vision flipped upside down.

And when I came to, I was in an unfamiliar gray space.

“Over here.”

I whipped my head around in surprise and saw an old man beckoning me.

*If an old man like that called me over in a dream, I’d turn around and run for my life. But this was a game.*

*So he’s the helper.*

Even if I hadn’t reasoned it out, I would have followed him without much suspicion.

It was strange, even to me, but that was how I felt. An inexplicable sense of familiarity. And trust.

“Take the most comfortable position.”

*Huh? Isn’t circulating qi supposed to be done sitting cross-legged?*

As if he had read my thoughts, the old man answered.

“Weaklings fuss over things like that. Masters don’t need to.”

I could smell it in his calm voice. I could smell it.

*This was the scent of a master. The real deal had finally appeared!*

“Good grief. What a handful.”

His wrinkled hand seemed to reach toward me, then vanished in a blur. Huh?

Tap. Tap-tap.

The next thing I knew, I was frozen in place.

*Was this what a corpse felt like with its eyes still open?* I couldn’t move a muscle.

“It’s only a simple acupoint-sealing technique, so don’t be alarmed. Focus from this point on.”

As he spoke, the old man placed a hand on my back. Then he rapidly rattled off words in a low voice.

“Circulating qi is the most important training for a martial artist. It allows you to advance to a higher realm not only by accumulating internal energy, but also by honing essence, qi, and spirit. Therefore…”

I listened closely, but I couldn’t understand a word of what came after that. I only understood that circulating qi was extremely important.

“Clear your mind like a stream, maintain your focus, and draw out the flow. Now I will recite the formula of the Jin Family’s Cultivation Technique.”

Without giving me time to stop him, he began reciting the formula at a speed like beans popping in a pan…but I could hear it. It felt as though words in a foreign language were being translated automatically inside my head.

*What is this?*

It was a formula of exactly 318 characters. The moment I felt the formula of the Jin Family’s Cultivation Technique become perfectly etched into my mind, a change occurred.

“Descend.”

One word from the old man.

*Where to?*

Before the question had even faded, I was being sucked into somewhere deep. No—it felt as though I was.

My eyes were definitely closed, but I could see. I could feel.

The breeze that gently blew in before scattering. Sunlight. The coachman’s breathing and the horses’ snorts…

I pushed all of it away. There was only one place to focus on: my body.

> **System**
>
> - Beginning circulation of Jin Family’s Cultivation Technique. Follow the glowing acupoints.

By then, I could no longer sense the old man’s disappearance or the System voice ringing out.

The consciousness awakened in my head slid downward. I didn’t know that the points shining like stars were acupoints. Everything simply felt familiar, as if it had always been this way.

At last, I reached my dantian.

A small but pure energy. Ten years of internal energy.

*But what’s that?*

In one corner of my dantian was something else, as large and hard as a boulder.

I understood instinctively.

*More internal energy.*

It was energy that I—Jin Taekyung—had not yet assimilated and made my own. It was almost as vast as the internal energy I already possessed.

*What if I absorb it?*

There was no question that I would become stronger.

But for me, right now, it would be a reckless challenge. An adventure without a purpose.

*I can’t make a reckless move and die out here.*

I steadied my mind and stirred my internal energy. Following the path the System voice had shown me, I slowly guided it along.

At some point, I thought I faintly heard someone’s voice.

“Good judgment.”


* * *


> **System**
>
> - Circulate Qi complete.
>
> - Tutorial—Stage 4 complete. Rewards have been issued!
>
> - You have gained insight into the skill Qi Sense. You can now manipulate qi more freely and sense the energy of others.
>
> - A small amount of turbid qi has been expelled.
>
> .
>
> .
>
> .
>
> - You have completed all Tutorials.
>
> - Main Quest created.

With the System’s final voice, the coachman spoke.

“We’ve arrived. This is the Jin Family of Taiyuan.”

*Yeah. At last.*
## Chapter artifact 6

# Chapter 6

The Jin Family of Taiyuan looked like an entire village from the hill above it.

Dozens of buildings, large and small, spread across the broad grounds, while high stone walls wrapped around the family estate without leaving a single gap.

And that wasn’t all. The cliff rising behind the Jin Family of Taiyuan was a spectacle in itself.

Nature that had weathered the ages, and one family crouched beneath it.

The sight alone was deeply imposing.

“Wow.”

Even the coachman was impressed. Wait, hold on.

“Didn’t you say you’d been here often?”

“This is my second time.”

“……You’ve only been working for how long?”

“Not even half a month.”

This guy had more layers than an onion.

He looked and carried himself like a twenty-year veteran, but he was a new hire.

*Then again, if he really had that much experience, there was no way he wouldn’t recognize this face.*

Mine was a face that had practically worn down Honghwaru’s threshold from coming and going so often. If he was a new hire, it made sense that he might mistake me for Jin Mukyung.

*Good thing everything worked out.*

I had completed the final Tutorial Quest, and the Jin Family of Taiyuan was right in front of me. I could finally relax a little.

“Could you slow down a bit?”

“Ah, yes.”

As I felt the carriage slow, I opened my Skill Window.

> **System**
>
> Skill Window
>
> **Qi Sense**
>
> **Grade:** None
>
> **Restriction:** None
>
> **Realm:** 1st Mastery
>
> **Effect:** Can identify targets at or below Lv. 30.
>
> **Description:** Scans targets within a designated range. As the realm rises, the scan range and maximum target level increase.

When I finished reading the description, something suddenly occurred to me.

*That’s exactly what it is. A power-level scanner.*

In a famous manga, a mechanical device quantified an opponent’s battle power. I wondered what Qi Sense would be like.

Curious, I called to mind the command.

*Activate Qi Sense.*

Was that right? I hesitated for a moment, and then a blue circle appeared beneath my feet. At the same time, a notification chimed.

Ding.

> **System**
>
> - You used Qi Sense. Since your current realm is 1st Mastery, you can scan targets at or below Lv. 30 within 10 jang.

Ten jang—that was 30 meters.

Whoosh. A blue concentric wave stretched outward and caught one person in its radius. A System window sprang up over the coachman’s round head.

> **System**
>
> - You identified the target with Qi Sense.
>
> **Lv. 4 Jang Sam**

Aha. So that was how it worked.

*Easy, simple, and most of all……*

It was an essential skill for survival. Whether an enemy was strong, weak, or roughly on my level—I could find out at once by using Qi Sense.

*I got a pretty good one.*

I nodded and opened the Quest Window. The moment I checked the new Main Quest, my mouth fell open before I knew it.

“……Huh?”

It felt as if the world in front of me had suddenly lit up. If Qi Sense was a single ray of light reflected in a sewer, this was the sun. My heart pounded, and heat rushed to my head.

> **System**
>
> Quest
>
> **Logout**
>
> Now you must make your way through this harsh Murim.
>
> Grow stronger and become famous.
>
> For that day, when it finally comes……
>
> **Grade:** Main Quest
>
> **Restriction:** Jin Taekyung
>
> **Objective:** Reach the First Rate realm (Incomplete)
>
> Reach Lv. 30 (Incomplete)
>
> Reach 500 Fame (Incomplete)
>
> **Reward:** Logout

The one word I had been desperate to see.

*Logout!*

I was happy, but dazed too. I had been determined to survive by any means necessary, yet a sliver of anxiety had always remained in the back of my mind. *Can I get out? What if I can never leave?* Those ominous suspicions had been there all along.

*I can get out.*

But now things were different. I was certain I could log out. It felt as if my mind had awakened anew.

*Yeah, fuck it. At the end of the day, it’s just a game.*

A quest? How hard could it be?

For seven years, I had crossed the line between life and death almost every day. A Hunter’s ability to survive—and sheer willpower—were beyond comparison with an ordinary person’s.

*And then there’s this power.*

My hand closed into a fist on its own. All of this might be virtual, but the power overflowing through my body felt real enough.

That was how I knew.

I was stronger in the game than I was in reality.

The difference was tiny, but it was definite.

*It’s all thanks to the System.*

Leveling up, Quests, distributing stats, and skills. All of it was the power of the System—things that were possible because this was a game and I was a player.

With my experience as a Hunter and the System at my disposal, logging out was only a matter of time.

*Once I get out, they’re all fucking dead.*

I’d start by beating the shit out of the game’s developers. Fucking bastards. I was grinding my teeth when someone shouted in my ear.

“Stop!”

* * *

Uniforms. Disciplined postures. Clipped voices.

The moment I saw the martial artists guarding the main gate of the Jin Family of Taiyuan, the word *martial artist* flashed through my mind.

*So this is what a prestigious family is like.*

They were definitely different. The Heavenly Axe and the bandits I’d run into before had been a rabble. These people were more like a trained regular army.

One of the NPCs approached the coachman. He was a martial artist with a young face and thick caterpillar eyebrows.

“I’m Hyuk Mujin, Captain of the Gatekeepers of the great Jin Family of Taiyuan. State your identity and the purpose of your visit.”

Captain of the Gatekeepers. Come to think of it, he was the only one wearing a band resembling an armband. He looked young enough to be twenty, at most.

*Then again, if you’re talented enough, that’s all that matters.*

While I was thinking that, the coachman answered.

“We’re from Honghwaru.”

“Honghwaru? You mean the pleasure house?”

“Yes.”

Through the window, I saw the NPC’s face—or rather, Hyuk Mujin’s face—twist into a frown. His previously polite manner turned curt on the spot.

“What business could a pleasure house possibly have with our family?”

“Ah, well……”

No matter where you went, there were always people like this. The kind who worked for a conglomerate and thought that made them a chaebol. The actual chaebols were somewhere else entirely.

I quietly opened the window and coughed.

“Ahem. Hmm-hmm.”

It was a deliberately conspicuous cough. The famous *Don’t you know who I am?* cough, available only to people who had made it big in life.

“Hmm.”

Sure enough, Hyuk Mujin recognized me at a glance. I opened my mouth with a mild smile.

It was a magic line widely used among high-ranking politicians, soldiers, and businessmen.

“Hmm. Right. Good work.”

I was about to close the window when……

Clack. Rattle.

“Huh?”

It wouldn’t close. A hand had shot forward and caught the window.

The owner of that hand was, of course, Hyuk Mujin. Through the half-closed window, I saw his face, stiff as a board.

“Get down.”

“Me?”

“Who else? Did you think I was talking to the air?”

What the hell? Why was this guy reacting like that?

*He didn’t recognize me after all.*

I put on a generous smile.

“You might not know this, but I live in this house.”

“So do I.”

“No, what I mean is……”

“The Third Young Master of the Jin Family of Taiyuan. Is that what you’re trying to say?”

“……”

He had hit the nail on the head. Hyuk Mujin continued.

“I know perfectly well who you are, Young Master. Now get down from the carriage. We’ll follow procedure.”

What else could I do? He said it was protocol. But warning lights were flashing in my head as I climbed down from the carriage.

*Why does this feel so ominous?*

The other NPCs in the Jin Family of Taiyuan were giving me strangely chilly looks too. Just as my face began to sting under their gazes, Hyuk Mujin took out paper and a brush and spoke.

“Name.”

“……”

“I’ll ask again. Name.”

What was this, a criminal interrogation?

I was in a foul mood, but decided to wait and see what happened.

“……Jin Taekyung.”

“Affiliation.”

“Jin Family of Taiyuan.”

“Age and martial arts realm.”

“Twenty. Second Rate.”

Hyuk Mujin’s brush paused.

“Don’t let pointless pride get in the way. Answer honestly.”

Honestly?

*I raised my rank to Second Rate by assigning stats. Would that mean anything to you?*

When I simply stared at Hyuk Mujin’s face instead of answering, he shook his head.

“Well, if that’s how you want it, we’ll move on. Now, let’s see…… You’ve been away for several days. Where have you been?”

“Honghwaru.”

“Wow, you spent several days at expensive Honghwaru? Must have been nice. You must have blown a fortune. Or did you skim the family funds again?”

“Again?”

“Why pretend otherwise? Isn’t that something the Young Master has done now and then, time and time again, as a matter of course?”

The hostility in Hyuk Mujin’s eyes brought one fact back to me.

*Jin Taekyung.*

I had forgotten for a moment what the character Jin Taekyung was in this game—especially in the Jin Family of Taiyuan.

*The Shame of the Family.*

There was no way the Jin Family of Taiyuan’s NPCs would like someone saddled with a title like that. As if to prove it, their contempt was aimed entirely at me now.

In this game where nothing went the way I wanted.

*Ah, for fuck’s sake……*

Something surged up from deep in my chest. My head throbbed, and heat rose behind my eyes. Then I heard a low voice.

“Third Young Master, I may only be a low-ranking squad leader, but let me say one thing.”

He said it with a look that made it clear what he thought of me: *What a pathetic bastard.*

“Stop disgracing the family’s reputation. At least try to live like a human being. Understood?”

He tossed out that one remark and turned away. I stared blankly at the back of his head, then let out a hollow laugh.

“Live like a human being?”

I knew Hyuk Mujin was nothing more than an NPC who knew nothing.

I knew he was saying it to Jin Taekyung, not to me.

But……

*This is fucking bullshit.*

The fact that this was a game and Hyuk Mujin was an NPC didn’t matter. No—I decided not to think about it.

All the stress that had piled up over the past few days burst out, and even the last of my patience crumbled.

“Hey. You. Stop right there.”

Hyuk Mujin turned around with an annoyed look on his face. I’d wanted to punch that face since earlier.

I beamed like a child who had just seen Santa Claus.

“You’re…… fucking dead.”

I sent my clenched fist flying toward his jaw.

* * *

The air was heavy. A pile of documents rose high above the desk. And, as always, a cold-looking escort stood beside his master like a shadow.

Scratch. Scratch.

The Chief of the Gatekeeping Pavilion swallowed. From the moment he entered the office, his mouth had been bone-dry.

“Tell me.”

The calm voice drifting from beyond the pile of documents was an oasis.

The Chief of the Gatekeeping Pavilion finally managed to speak.

“There’s one promising man among my subordinates. He’s quite loyal to the main family, and he has considerable martial talent, but……”

“I’m listening.”

“Perhaps because he’s young, he’s arrogant and insolent. He doesn’t know how to think things through.”

“Get to the point.”

“I hear he got into a fight with the Third Young Master.”

“……I can imagine. What about the youngest?”

“We moved the youngest to Medicine King Hall immediately. He’s unconscious now, with some bruising……”

Silence fell.

“It was all my fault. Please punish me severely!”

The Chief of the Gatekeeping Pavilion bowed deeply, his vision going dark. A long while passed before the voice came again.

“That’s enough. You may leave.”

The Chief of the Gatekeeping Pavilion raised his head, feeling as if he had narrowly escaped death.

“Ah, one more thing.”

“Yes, Lesser Family Head.”

“Could I see that fellow? I’d like to speak with him for a moment.”

“Lesser Family Head, I’m sorry to say this, but his treatment isn’t finished yet.”

“Treatment?”

“Yes. He’s at Medicine King Hall too. I hear one of his bones was cracked.”

“……I see. Then never mind.”

The silence that continued after the Chief of the Gatekeeping Pavilion withdrew was broken when the precariously stacked tower of documents came crashing down.

“Wipeng.”

The thirty-five-year-old Lesser Family Head of the Jin Family of Taiyuan, Jin Wikyung, called to his trusted retainer, his expression stiff.

“Yes.”

“I’m going to step out for a while.”

*Here we go again.*

Wipeng, Jin Wikyung’s escort, let out an inscrutable sigh as he watched his master walk away.
## Chapter artifact 7

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

“……”

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

I was feeling an extreme amount of shame. I was being sexually harassed by an AI—and one that looked like a middle-aged man, at that.

*Mom…*

It took me a moment to realize that I had completely misunderstood.

His hands were moving quickly, but they were moving just like a physician examining a patient.

He lifted my eyelids, checked my pulse, and carefully examined the bruised areas. Every time his hands passed over me, the pain faded and my body felt refreshed, as if I were getting a massage.

“You little bastard! Keep acting like this and, huh? Huh! You’ll get what’s coming to you! Do you understand?”

“……”

At last, he stopped moving his hands and whispered in a small voice,

“It’s not as bad as I thought. Thank goodness. Why did you get into a fight, anyway? You never even train in martial arts.”

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
## Chapter artifact 8

# Chapter 8

“There are no abnormalities.”

That was the physician’s conclusion. I nodded inwardly at his confident tone. He was telling the truth.

*There’s nothing wrong with my brain.*

I was simply inhabiting this body.

But someone didn’t seem satisfied with the diagnosis.

“Then why can’t he remember?”

The dignified atmosphere. The commanding voice. I knew his name now.

*Jin Wikyung.*

Jin Taekyung’s eldest brother and the Lesser Family Head of the Jin Family of Taiyuan, Jin Wikyung. Right. He really wasn’t my father.

*That guy was practically tearing up earlier.*

Now he had put on a mask of stern solemnity and seriousness, acting as if nothing had happened.

The innocent physician fumbled for an answer.

“Well, that is certainly my assessment, but there may occasionally be exceptions…”

“That will do. You may leave.”

The physician left with a wounded expression, and Jin Wikyung immediately moved close to me as if he had been waiting for the chance. His voice overflowed with affection and concern.

“You truly don’t remember?”

“No.”

“Not a thing?”

I quietly nodded. I had already finished calculating how I was going to act.

*Let’s keep going like this.*

An amnesiac patient—the kind I had only ever seen in dramas. There was no better situation for me. I didn’t need to make an effort to fit into the game’s circumstances, and I didn’t even need to gather information.

All I had to do was lie still, blink at everyone with an expression that said *I don’t know anything*, and let the situation unfold on its own. Just like now.

“Do you remember what you said a moment ago?”

“What did I say?”

Thinking that I had lost my memory, Jin Wikyung told me a few basic facts. That was how I learned his identity.

“Tell me my name.”

“Jin Wikyung. The Lesser Family Head of the Jin Family of Taiyuan.”

“Age?”

“Thirty-five.”

Good grief. He was in his thirties with that face? And apparently, he was still an unmarried bachelor.

“What about our parents?”

“Our father is touring the Central Plains. Our mother died ten years ago.”

“Correct. And your second brother?”

“Jin Mukyung, the Heaven Shaking Sword. Twenty-five years old. Currently a cadet at Heaven’s Gate Temple.”

I had no idea where Heaven’s Gate Temple was located. I was simply parroting back everything I had heard.

Jin Wikyung mechanically repeated “Correct, correct” to each of my answers, then tilted his head.

“The Heaven Shaking Sword? Did I tell you his sobriquet too?”

No. The coachman had told me that.

The moment our eyes met, I grabbed my forehead.

“Ah, my head! My head hurts!”

“Oh, my youngest!”

This was practically a cheat code.

* * *

“It’s only a simple contusion. The swelling and bruises should be completely gone within three days at most.”

Leaving the physician’s final words behind, I walked out of Medicine King Hall. A servant with a plain, friendly face was waiting for me at the entrance.

“I’ll guide you to your quarters, Young Master.”

The servant walked ahead without hesitation. He already seemed to know that I had lost my memory, because whenever we passed a building or a person, he quietly explained what they were.

*A guide, an errand boy, and an encyclopedia.*

I could roughly guess why Jin Wikyung had sent him.

He was busy with his duties, so this was probably his way of looking after me.

“We’ve arrived.”

At last, we stopped in front of a two-story wooden building.

Weren’t buildings like this usually called pavilions in China? It had a rather impressive old-fashioned charm.

“Wow.”

It was unbelievably spacious, too. The moment the servant opened the door, my jaw dropped.

“The second floor contains your bedroom. Bells have been installed throughout the building, so please ring one if you need anything.”

After the servant left, I came to my senses and began exploring the pavilion. The first floor alone looked to be more than three hundred square meters.

To someone who had lived in a goshiwon room measuring barely seven square meters,[^1] this was no different from an Olympic stadium.

*This is the first time I’ve ever envied an NPC.*

There were six rooms on the first floor alone. A sudden wave of curiosity rose in me.

*What could be inside?*

Treasures? Martial arts manuals? Amazing items?

I didn’t care what it was. I opened the nearest door.

“Whoa.”

A gasp escaped me the moment I opened it. The room was bright on all sides despite having no fluorescent lights. Silk clothes filled the shelves lining the walls. There were an astonishing number of them, even at a glance.

Of course, it wasn’t what I was looking for.

*This bastard has a lot of clothes.*

A club rat—no, a pleasure-house regular. I clicked my tongue and closed the door. Then I went straight to the second room and threw that door open, too.

“More clothes?”

I had underestimated Jin Taekyung. At this point, wasn’t he practically the fashion icon of his era?

I forced myself to ignore the unease slowly crawling up my spine and moved to the third room.

The door flew open.

“…What kind of shopping-addicted bastard is this?”

Seriously, what kind of person was he? Seeing three rooms packed completely full of clothes made my throat close up, as if I had swallowed a sweet potato.

*Could this possibly mean…*

My unease gradually took shape and pressed down on my body. With heavy steps, I stood before the last room. Unlike the others, it clearly hadn’t been used in a long time. I grabbed the rusty handle and slowly pushed.

Creeeak.

The final room revealed itself with an irritating groan.

Sunlight filtered through a small window. Dust rose with every step. And beyond it stood several bookshelves.

“Found it.”

A smile spread across my face before I even realized it.

* * *

There were five bookshelves in total. I approached the nearest one and pulled out a book. When I shook off the thick layer of dust, the writing on its cover appeared.

This was why the System was so convenient. Thanks to Synchronization, I could read and pronounce even writing that looked like an alien language as naturally as my mother tongue.

“Three-Turn Footwork?”

Ding.

> **System**
>
> Item Window
>
> **Three-Turn Footwork**
>
> **Type:** Martial Arts Manual
>
> **Grade:** Third Rate
>
> **Restriction:** None
>
> **Description:** The most basic practical footwork technique. It can even be purchased on the open market.
>
> - Would you like to train in this martial art? (3 / 10)

Jackpot!

I read through the System window with a pounding heart.

Three-Turn Footwork. The most basic Third Rate footwork technique. This was the very martial arts manual I had only ever seen in novels.

My first plan was to learn martial arts.

*So the System applies to martial arts training too.*

The suspicion I had formed after completing the Quest to circulate my qi, just before coming to the Jin Family of Taiyuan, had now become certainty.

*Thank goodness.*

I had been worried that I might have to learn martial arts one step at a time, like the protagonists and NPCs in novels. Fortunately, that fear had been unfounded.

*Even a trash game is still a game.*

If the System applied to ordinary martial arts the same way it had to circulating qi, rapid growth would be a piece of cake.

I was about to shout, “I accept!”—but stopped.

> **System**
>
> - Would you like to train in this martial art? (3 / 10)

The number in parentheses bothered me immensely. I had learned exactly three martial arts so far: the Jin Family’s Cultivation Technique, the Jin Family’s Spear Technique, and the Jin Family’s Manoeuvre Technique.

*Could it be…*

*Is there a limit to how many martial arts I can learn?*

If that suspicion was true, now was not the time to learn a Third Rate martial art like Three-Turn Footwork. I needed to find a higher-grade martial art—one that could keep me alive until Logout and help me raise my Level and Fame quickly.

The good news was that this room contained several hundred martial arts manuals, give or take.

“Good. Good.”

That meant I could learn seven more martial arts. If I filled those slots with nothing but the best techniques, Logout would only be a matter of time.

With a satisfied smile, I pulled out the next book.

Ding.

> **System**
>
> Item Window
>
> **The Night King: Well-Endowed Man**
>
> **Type:** Erotic Novel
>
> **Grade:** None
>
> **Restriction:** None
>
> **Description:** Even better when read with illustrations.

“…”

* * *

Work had been another fierce battle today. I hadn’t been able to leave the office from morning until nearly midnight. It had already been two months of this grueling pace.

“You’ve worked hard.”

That was Wipeng’s signal that the day’s work was over.

Jin Wikyung rose, his body stiff, and left the office. The owner of this place was his father, who had vanished one day—not Jin Wikyung himself.

His residence was a pavilion in the inner compound at the center of the Jin Family estate, and it took about a quarter hour to walk there.

“It’s cold tonight.”

Wipeng, who had followed him like a shadow, draped a thick fur cloak over his shoulders. Jin Wikyung smiled tiredly.

“Thank you. If I didn’t have you, I might have collapsed long ago.”

“What else could I do? Someone has to play the lady of the house.”

“Forget it. The old men are already hounding me enough as it is.”

Jin Wikyung rubbed his stiff eyes. He was in his mid-thirties, but still unmarried. He had kept putting it off under the excuse of being young, and more than a decade had passed in those delays.

*I suppose I’ll have to do it eventually. For the family’s sake.*

If someone asked whether he had never experienced love, the answer would be no.

But Jin Wikyung was not an immature child. One day, he would become the Family Head and take responsibility for everyone in the household. If a political marriage could strengthen the family, it would be a small price to pay as far as he was concerned.

“The stars are bright. We almost wouldn’t need torches.”

Sensing the mood, Wipeng changed the subject. Jin Wikyung shook his head. His residence had come into view.

“Hmm?”

“What is it?”

Following Jin Wikyung’s gaze, Wipeng tilted his head. A faint light was leaking from a nearby pavilion.

“Isn’t that the Third Young Master’s residence?”

“It is. It’s late, but the lights are still on.”

As he spoke, Jin Wikyung strode forward. Wipeng had no choice but to follow.

“My lord, why don’t we come back another time? The memory loss is just an excuse. He’s obviously drinking.”

“Shh.”

The two men entered the pavilion. The light was coming from the old room on the far left. The constant creaking made it clear that someone was moving around inside.

“I underestimated the Third Young Master. It sounds like he even brought a woman with him. Listen to that. I’ll bet my salary for this month.”

Wipeng’s lips moved. He was using Sound Transmission, sending his voice through internal energy.

“Wipeng.”

“Yes?”

“Shut your mouth.”

Jin Wikyung sent the short, heavy response through Sound Transmission, then moved right up to the door. Through the narrow gap, he could see what was happening inside.

Wipeng cut in again with a wounded expression.

“I never took you for this sort of person, my lord, but your tastes are rather unusual…”

He gasped.

The next moment, Wipeng’s mouth fell open.

*What did I just see?*

*Was I seeing things because I’ve been feeling weak lately?*

He rubbed his eyes with his sleeve, but all five senses continued to take in the scene before him exactly as it was.

“Now, take two steps diagonally…”

It was a young man with a sturdy build. He muttered continuously while moving his body without pause. Countless footprints covered the dusty floor, and more were being added even now.

Swish. Stumble.

“Fuck, they made this martial art like shit—aaagh!”

It was the Third Young Master. That foul personality and that foul mouth. There was no doubt that he was Jin Taekyung.

He hadn’t trained in martial arts since the age of twelve, yet he was practicing past midnight, drenched in dust and sweat!

“Wipeng.”

Wipeng, who had been staring blankly, suddenly snapped back to reality.

“Yes, yes?”

Jin Wikyung gazed into the room with dazed eyes. Jin Taekyung had fallen over and was hurling vicious curses at the ceiling, but he soon got back up and resumed practicing his footwork.

“As promised, you won’t be getting paid this month.”

[^1]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement.
## Chapter artifact 9

# Chapter 9

Ding.

> **System**
>
> - You have acquired **Jin Family’s Manoeuvre Technique**.
>
> - You can obtain various effects upon mastering this martial art.
>
> - You have completed the achievement **Learn a Martial Art**.
>
> - As an achievement completion reward, you have acquired the title **Novice Trainee**.

“Good grief.”

The moment the System notification appeared, I slumped to the floor. Dust billowed into the air, but who cared? I already looked like a bum anyway.

*Why is this so damn hard?*

There were only two kinds of books in Jin Taekyung’s study.

Erotic novels. And books that weren’t erotic novels.

Of the more than four hundred books, only about a hundred remained after I took out the erotic novels.

*What an incredible bastard.*

If he’d been born in Korea, he would’ve been running an illegal adult website. If he’d been born in America, he’d be serving a prison sentence.

At any rate, once I finished sorting them, there were only about thirty martial arts manuals.

*If only he’d collected half as many manuals as erotic novels.*

It was a shame from my perspective, but I had still made a worthwhile discovery. I’d found the martial arts manuals I needed right now.

The Jin Family’s Spear Technique and the Jin Family’s Manoeuvre Technique. They were hereditary martial arts of the Jin Family of Taiyuan—arts I had forgotten after going far too long without practicing them.

*Let’s check the Jin Family’s Manoeuvre Technique.*

Ding.

> **Skill Window**
>
> **Jin Family’s Manoeuvre Technique**
>
> **Type:** Manoeuvre Technique
>
> **Grade:** First Rate
>
> **Restriction:** Direct descendants of the Jin Family of Taiyuan
>
> **Realm:** First Stage
>
> **Description:** A manoeuvre technique devised by the founder of the Jin Family of Taiyuan. It has few variations and is monotonous, but it is practical.

The description of the Jin Family’s Spear Technique wasn’t much different. Except…

*“Few variations and monotonous,” my ass.*

The hereditary martial art created by some fellow called the founder—or was it the ancestor bird?—was unbelievably complicated. Just thinking about last night made my teeth grind.

> **System**
>
> - You are beginning to acquire **Jin Family’s Manoeuvre Technique**.
>
> - You are memorizing the formula. The speed varies according to the martial art’s grade and your Intelligence stat.

Right. Everything was fine up to that point.

The problem started after that.

> **System**
>
> - The movement sequence for **Jin Family’s Manoeuvre Technique** is being displayed. (0 / 100)

I followed the footprints displayed by the System and practiced the manoeuvre technique. But the footprints were so fussy and razor-precise that stepping even slightly outside them meant failure. Taking too long to perform the next movement also meant failure.

I had to follow the entire sequence perfectly to complete it once.

*What a fucking garbage game.*

There was a major difference between my real-world physique and the character’s. My height was shorter by nearly half a handspan, and my reach was shorter too. I couldn’t make the fine adjustments I needed, so one mistake followed another.

*It’s a miracle I succeeded at all.*

After completing the sequence one hundred times, my hands and feet were trembling.

*Still, I gained something.*

After years of working as a Hunter, I was thoroughly familiar with combat—especially group battles. In fights where life and death were on the line, the most important thing was luck first and your feet second.

Moving forward. Retreating. Or stopping.

Even if your arm was cut off, you could survive as long as your legs still moved. But if your legs were cut off, it was over.

Your feet had to move before your arms. That was how all my battles had gone, and it was why I had chosen to learn a manoeuvre technique first.

*But…*

It was too slow. Even with the System’s help, half a day had passed in the blink of an eye. How much longer would it take if I also had to learn spear techniques?

*Today makes five days.*

I’d heard that time passed faster in virtual-reality games than in the real world. But even after accounting for the time multiplier, five days was a long time.

“Fuu…”

I forced away my distractions with a sigh.

Rescue? Logout?

This wasn’t the time to cling to possibilities. I had to keep moving forward, even if I had to do it alone.

*That’s enough for today.*

I gathered up the martial arts manuals and stood.

When I reached the bedroom on the second floor, I realized that one unusual book had been mixed in among the manuals.

**The Night King: Well-Endowed Man**

“Ahem.”

Oh dear. What a mistake.

* * *

“Are you up already?”

The servant stared at me with wide eyes. He was holding a tray with breakfast on it.

“I couldn’t sleep…”

My answer was the truth. That was because I’d been circulating my qi.

*This is ridiculously effective.*

Circulating my qi didn’t just clear my mind and sharpen my senses. It also relieved fatigue. Thinking back carefully, I didn’t think I’d felt tired even once since I started circulating my qi.

*The pain is almost gone too.*

“Your wounds could worsen, so please don’t push yourself too hard.”

A warm feeling spread through one corner of my chest at the servant’s words.

*Even this shitty game has an NPC who’s like a ray of light. I’ve finally met a normal person.*

*Why does this make me feel so emotional?*

Feeling strangely choked up, I began eating breakfast.

Every side dish was either too salty or too bland, but I demolished the entire meal, using my hunger as a side dish, then downed the bowl of herbal decoction in one gulp.

“Ugh.”

The taste made me frown instinctively. Once the servant had cleared away the table, he bowed his head.

“Then I shall take my leave.”

“Ah, wait a second.”

“Please speak less formally. Why are you using honorifics with me?”

Come to think of it, he had a point.

At first, the graphics and artificial intelligence had been so realistic that I had used polite speech with every NPC I met. But by now, I had grown somewhat accustomed to them.

The time had finally come to reclaim the dignity of a user.

I answered sternly.

“For now, I’ll speak however I’m comfortable.”

*Fuck, I can’t bring myself to drop the honorifics.*

I couldn’t exactly talk down to a man who clearly looked over forty and call him “you bastard” or “you punk.”

*Damn game. The graphics are so good I can’t even speak informally.*

*At this rate, I’ll end up becoming friends with an NPC.*

When I emphasized the fact that I had suffered a head injury, the servant reluctantly nodded.

“I suppose it can’t be helped. Is there something you require?”

“I was wondering if there was an empty room.”

The servant tilted his head.

“I can arrange one for you, but what might you need it for?”

“I want to practice martial arts.”

“Pardon?”

“All the rooms here are either dirty or stuffy… Why do you look like that?”

* * *

After leaving the pavilion, the servant went straight to the Family Head’s office.

Once his report was finished, Jin Wikyung’s solemn voice rang out from beyond a tower of documents.

“You’ve done well.”

The instant the servant left, Jin Wikyung sprang to his feet and scattered the documents into the air.

“It’s cause for celebration! I’m not working today!”

“Who said you could decide that?”

Wipeng caught every last one of the fluttering documents and sighed.

“If the others find out you’re acting like this, they’ll start talking again.”

“The Third Young Master says he’s going to take up martial arts in earnest. What could possibly be more important than that?”

“The fact that the Elder Council is waiting to pounce on you is more important.”

At the words *Elder Council*, Jin Wikyung’s expression darkened.

“Damn old men.”

“A family council meeting may be held soon. From their perspective, they’ve spotted an opening, so naturally they’ll sink their teeth into it.”

The agenda was obvious. It would begin with Jin Taekyung’s usual conduct and end with an attack on Jin Wikyung himself, the Young Sect Leader.

“Those bastards are persistent.”

“Is this something that started yesterday? Old pillars always end up crawling with bugs.”

“Isn’t there any way around it?”

“So you’re volunteering to serve as the Third Young Master’s shield again.”

Wipeng sighed.

“My lord, may I offer a word?”

“I refuse.”

“Then I refuse as well. This is the fifth time he’s embezzled the sect’s public funds. I’ve lost count of the other things. If we had enforced the family rules properly, it would be a miracle if the Third Young Master were still alive.”

“Now, now.”

“Since we’re on the subject, grab anyone in the family and ask them. From your perspective, he’s your beloved little brother. To everyone else…”

Wipeng shook his head.

“Honestly, I can’t even say it.”

“Do you have some complaint against our youngest? Why are you speaking like that?”

“I’m frustrated. That’s all. I’m frustrated. The Third Young Master causes trouble, you clean it up, and you accept the Elder Council’s demands to keep them from making things worse. They’re slowly taking away your control. Do you know what kind of rumor is going around these days?”

“What rumor?”

“Some people say the Third Young Master is part of the Elder faction. That he gets pocket money from the Elder Council and deliberately causes trouble.”

Jin Wikyung’s eyelids began to tremble.

“That’s an outrage!”

“I’d actually prefer that to be true. If the Elder Council slipped him even a few silver coins, he wouldn’t have to embezzle the family’s funds.”

“You…”

“I’ve said my piece. Fire me if you want.”

With a groan, Jin Wikyung let out a deep sigh.

“I’ve been thinking things can’t go on like this, either.”

“Thinking is good. The problem is that you never put it into action.”

“Even so, I should do my best this time.”

“Oh, my lord…”

“This will be the last time. I give you my word.”

Jin Wikyung spoke with a serious expression. Wipeng asked, sounding skeptical,

“Do you really mean it?”

“He’s still a child whose memory hasn’t fully returned. And besides… he changed into an entirely different person overnight. You’ve noticed it too.”

“That’s true, but…”

Wipeng let his voice trail off.

The Third Young Master had definitely changed. Whether the memory loss was a lie or the truth, the way he was behaving now was undeniably hopeful.

Jin Wikyung thought for a moment before speaking.

“Wipeng.”

“Yes.”

“Prepare an order in my name.”

“What sort of…?”

“Use a few appropriate charges and order him to undergo indefinite confinement in the training hall.”

“Ah.”

Wipeng slapped his forehead.

It was mostly for show, but under the circumstances, it was an excellent emergency measure. It would relieve the pressure Jin Wikyung was about to receive at the upcoming family council meeting while lowering the severity of the punishment imposed on Jin Taekyung.

And on top of that…

“It fulfills the Third Young Master’s request too. He was looking for somewhere to train.”

Wasn’t this three birds with one stone? Wipeng was genuinely impressed.

“As expected, you’re my lord.”

“That’s how my family is. Oh, did I ever tell you? Taekyung was a clever child when he was young, but one day…”

“…I’ll go write the order.”

* * *

“Therefore, for violating fourteen regulations and disrupting discipline within the family, the Third Young Master, Jin Taekyung, is hereby ordered to undergo indefinite confinement in the training hall.”

Was his name Wipeng? I listened silently to the sour-looking bastard, then raised my hand.

“I have a question.”

“Go ahead.”

“What does ‘indefinite’ mean?”

Wipeng answered reluctantly.

“It means there is no set deadline.”

“Oh.”

I’d thought the game’s language system had malfunctioned. Fortunately, it meant the same thing I knew it meant.

Ha ha.

“Ha ha ha.”

“Ho ho ho.”

Laughter was contagious by nature. The warriors who had come with Wipeng began laughing along with me.

In that warm atmosphere, Wipeng read the final line.

“The convict, Jin Taekyung, shall submit to the bonds.”

“No.”

“…”

“…”

“I said no. Fuck.”

The two men approaching with rope restraints looked at Wipeng as if to say, *This isn’t how it was supposed to go.*

I ignored them and said what I had to say.

“I asked you to find me a room so I could practice, not put me in prison. Are you people completely fucking insane?”

“Now, Third Young Master. Calm down and listen to me.”

“Listen to what, for fuck’s sake? You’re going to say the training hall has everything needed for practice and the living conditions aren’t bad. You’ll spout that kind of nonsense.”

Judging by Wipeng’s expression, I’d hit the nail on the head. I drove the point home.

“You people would tell someone to go happily serve in the army because military pay had gone up. Forget it. I’m not going in. I’ll practice by myself in my room or in the yard.”

Honestly, on the surface, the training hall didn’t sound so bad.

But the word *indefinite* stuck in my mind like a thorn. I needed to learn martial arts and Level up immediately. I couldn’t spend day after day in the training hall, craning my neck and waiting to be let out.

I flopped onto the floor.

“Go ahead and gut me!”

“Third Young Master, that’s enough. Please get up.”

Wipeng scowled at me.

“The Lesser Family Head made this decision entirely for your sake.”

“Jin Wikyung—I mean, my brother?”

That brother-obsessed idiot had given this order?

At that moment, Wipeng’s lips moved.

At the same time, a voice reached my ears. It felt strange, unlike an actual spoken voice.

> “This is Sound Transmission. Don’t be alarmed—just listen.”

Sound Transmission. I remembered seeing it in martial arts novels. A kind of telepathy that only masters could use.

> “You may not know this because you’ve lost your memory, but the Third Young Master is a person of concern. A harsher punishment may be handed down soon, so the Lesser Family Head is taking action beforehand.”

I had worked hard for twenty-seven years. What did I do to deserve an aggravated sentence?

As I lamented, Wipeng’s Sound Transmission continued in my ear.

> “It may be called indefinite confinement, but do you really think the Lesser Family Head intends to bury you in the training hall for the rest of your life?”

I shook my head.

*There’s no way he’d do that.*

Not unless he wanted the two of us locked up together in the training hall.

> “I’ll get you out within seven days and nights at the latest. How does that sound?”

There was fierce determination in Wipeng’s eyes. If I refused this too, he looked ready to beat me and drag me there if he had to.

*Fuck, are all the NPCs here thugs or what?*

*Hey, you bastard. Are you really that good at fighting?*

I raised my Qi Sense and checked Wipeng’s Level.

> **System**
>
> - **Lv. ???**

“…”

*He really is a thug.*

A Level thug, at least.

He was probably every bit the human butcher Jin Wikyung was.

Wipeng opened his eyes wide and asked,

> “What will you do?”

Even as I trembled with fear, I held up three fingers.

> “…You want me to get you out in three days?”

*What kind of bastard is this?*

Wipeng glared at me with that exact look, then finally sighed.

“Escort him.”

#TrainingHall #ClosedDoorTraining #Negotiation #Successful.
