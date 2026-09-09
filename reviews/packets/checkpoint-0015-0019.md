# Checkpoint Review — 15–19

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

# Chapters 15–19

## Plot

Taekyung defeats Lee Seogeun in the duel, completing the Duel Quest and gaining three levels, the Gambler title, Fame, Fourth-Stage Cultivation, and Third-Stage Qi Sense. Lee is later killed in the departing Jin Family carriage by an unidentified masked assassin using Sound Transmission, paralysis or toxin, and a blue-black needle; “going to Mount Beimang” foreshadows his death.

The Jin Family’s belief that Taekyung is the Sleeping Dragon of Shanxi earns him additional Fame. While cultivating, he discovers a powerful unidentified energy in his dantian that rejects his contact and nearly consumes the internal energy he sends toward it. His cultivation raises his Sinews and Bones, but his Status Window still shows ten years of internal energy.

The Elder Council interrogates Taekyung over Lee’s poisoning and blames him for provoking Mount Heng. Jin Wikyung rejects the proposal to hand him over and calls for war. The Head Elder unexpectedly supports Wikyung and condemns the faction that framed Taekyung, though his political motives remain unclear. Mount Heng declares war, creating a System War relationship, designating Taekyung a public enemy, and triggering the Main Quest — War. Wikyung seals the family grounds and assumes operational control.

The Jin Family is badly outmatched: roughly 200 martial artists and three Peak masters against Mount Heng’s 300 or more martial artists and five Peak masters. With Shanxi sects refusing to answer the family’s requests for aid, Wikyung accepts assistance from Wolhwa, revealed to be Eun Sowol, the Level 50 Branch Leader of the Lower District Sect’s Shanxi branch. In exchange, she demands half of Mount Heng’s shops and assets.

## Continuity

- Taekyung is Lv. 17. His Cultivation, Spear, and Manoeuvre Techniques are Fourth Stage; Qi Sense is Third Stage and detects targets through Lv. 50.
- The Main Quest still requires First Rate, Lv. 30, and Fame 500 for the reward of Logout. Taekyung has 17/30 levels and approximately 70/500 Fame.
- Taekyung’s ten years of internal energy remain insufficient for advancement despite his strong physical stats. An unidentified, much stronger energy occupies his dantian and resists control.
- The Sleeping Dragon of Shanxi rumor is spreading through the Jin Family. Taekyung deliberately confirms it, gaining 10 Fame, with later belief producing periodic Fame increases.
- Lee Seogeun is dead. His masked killer remains unidentified; the assassin used Sound Transmission, paralysis or poison, and a large blue-black needle.
- Jin Wikyung is Taekyung’s protective eldest brother and acting Family Head during the war. Wipeng remains his trusted Peak-level ally.
- The Head Elder is Taekyung’s great-uncle and the Jin Family’s highest-ranking elder. He supports Wikyung publicly, but his true plan is unresolved.
- Mount Heng Sword Sect and the Jin Family of Taiyuan are at war. Taekyung is a public enemy, and fleeing incurs severe System penalties. The family grounds are sealed without Wikyung’s authorization.
- Wolhwa is Eun Sowol, a Level 50 martial artist and Lower District Sect Branch Leader. Honghwaru is that sect’s Shanxi branch. Wikyung accepted her demand for half of Mount Heng’s shops and assets.
- The capsule’s purpose, the route home, and the limits of Murim’s death and resurrection rules remain unresolved.

## Translation Decisions

- Preserve **Mount Heng Sword Sect**, **Mount Beimang**, **Sleeping Dragon of Shanxi**, **Lower District Sect**, **Branch Leader**, **War relationship**, **Main Quest — War**, **First Rate**, **Peak**, **Fame**, and **Logout**.
- Keep **Sound Transmission**, **Elder Council**, **Head Elder**, **acting Family Head**, and the Jin Family’s **Cultivation**, **Spear**, and **Manoeuvre Techniques** consistent.
- Render the System’s war clause as: “Those who survive are strong, and only the strong will survive.”
- Preserve the brisk dark action-comedy and Taekyung’s dry, self-mocking profanity.
- Retain the gold-spoon/**God-Spoon** wordplay with a brief footnote where needed.
- Keep the assassination cues explicit: burning throat pain or loss of voice where applicable, paralysis or toxin effects, the Mount Beimang death idiom, and the masked assassin’s blue-black needle.

## Durable state

{
  "version": 1,
  "safe_through": 19,
  "continuity_sources": [18, 19],
  "active_continuity": [
    "Jin Taekyung is trapped in Murim through an old game capsule; death is presented as permanent and he cannot log out at will.",
    "Taekyung is the disgraced third son of the Jin Family of Taiyuan and narrates with dry, self-mocking, occasionally profane humor.",
    "Logout is the Main Quest reward for reaching First Rate, Lv. 30, and 500 Fame.",
    "Taekyung is Lv. 17; his Jin Family’s Cultivation, Spear, and Manoeuvre Techniques are at the Fourth Stage, and Third-Stage Qi Sense detects targets through Lv. 50.",
    "Hyuk Mujin is Lv. 20; Training Mode can summon him and Taekyung can partially adjust a summoned opponent’s abilities.",
    "Jin Wikyung is Taekyung’s thirty-five-year-old eldest brother and the Lesser Family Head of the Jin Family of Taiyuan; Wipeng is his trusted guard.",
    "At the Medicine King Hall, Taekyung pretends to have amnesia, and Jin Wikyung believes him.",
    "Jin Mukyung is twenty-five, the Heaven Shaking Sword, and a cadet at Heaven's Gate Temple.",
    "Taekyung has three martial arts occupying slots; the System displays ten total martial-art slots, and he finds several hundred manuals in his residence.",
    "Taekyung completed the Jin Family’s Manoeuvre Technique and Spear Technique training, reaching the Fourth Stage in both after combining their forms.",
    "The Clear-Heart Pill reward is a ring that steadies Taekyung’s mind and improves concentration and cultivation.",
    "Taekyung’s three-day staged confinement ends after he wins the duel; the family seniors accept Jin Wikyung’s coercive decision to release him.",
    "The Mount Heng Sword Sect and the Jin Family of Taiyuan are sworn enemies; the sect leaves with injured warriors after Lee Seogeun loses.",
    "Taekyung accepted and completed the System’s Duel Quest, gaining the Gambler title, EXP, Fame, three levels, Fourth-Stage Cultivation, and Third-Stage Qi Sense.",
    "Lee Seogeun was Lv. 30; Taekyung defeated him with the Jin Family techniques, unarmed grappling, and concentrated internal-energy strikes.",
    "Lee Seogeun is killed in the departing Jin Family carriage by an unidentified masked assassin using Sound Transmission, paralysis or toxin, and a large blue-black needle.",
    "Mount Beimang is a burial mountain; “going to Beimang” is an idiom for dying.",
    "After the duel, Jin Wikyung draws heroic pictures of Taekyung, receives an urgent messenger hawk, and summons a secret late-night family-council meeting.",
    "Han Yeop tells Taekyung that the Jin Family believes he is the Sleeping Dragon of Shanxi; Taekyung confirms the rumor, gaining 10 Fame, with later belief producing periodic 3-Fame increases.",
    "Taekyung concludes that his ten years of internal energy are insufficient for martial-realm advancement despite strong stats; Lee Seogeun likely had twenty years.",
    "The Main Quest requires First Rate, Level 30 (17/30), and Fame 500 (70/500), rewarding Logout; two days remain in Taekyung's protective confinement.",
    "The Head Elder is Taekyung’s great-uncle and the most senior elder in the Jin Family; he sits beside Wikyung at the family council and observes the interrogation.",
    "An unidentified energy occupies Taekyung’s dantian. It is more powerful than his ten years of internal energy, rejects contact, and nearly consumes the energy he sends toward it.",
    "Cultivation training raises Taekyung’s internal energy slightly and increases Sinews and Bones by 1 each, but his Status Window still displays ten years of internal energy.",
    "Jin Wikyung guides Taekyung through the Lee Seogeun poisoning interrogation with Sound Transmission and remains on his side during the Elder Council’s factional pressure.",
    "The Elder Council’s senior faction blames Taekyung for disorderly conduct, disgracing the family, and provoking the Mount Heng Sword Sect’s prized treasure; Taekyung confirms through the System that he has no poison-related martial arts, abilities, or Items.",
    "At the council, Jin Wikyung rejects handing Taekyung over and calls for war; the Head Elder backs him, condemns the faction’s framing, and publicly rallies the family around Wikyung, though his motives remain unclear.",
    "The Jin Family has roughly 200 martial artists, fewer than 20 First Rate masters outside the wider senior group, and three Peak masters; Mount Heng has at least 300 martial artists, more than 50 First Rate masters, and five Peak masters.",
    "Mount Heng has declared war on the Jin Family. The System establishes a War relationship, designates Taekyung a public enemy, creates the Main Quest — War, and warns that fleeing will incur severe penalties; Wikyung seals the family grounds against entry or exit without his seal.",
    "Wolhwa is Eun Sowol, a Level 50 martial artist and Branch Leader of the Lower District Sect’s Shanxi branch; Honghwaru in Taiyuan serves as that branch’s establishment.",
    "The Lower District Sect offers aid against Mount Heng in exchange for half of Mount Heng’s shops and assets, which Wikyung accepts as acting Family Head."
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

## Chapter artifact 15

# Chapter 15

Wipeng thought,

*What am I looking at right now?*

Something unbelievable was happening right before his eyes. The Third Young Master—of all people, that very Third Young Master—was holding his own against Lee Seogeun.

*Am I hallucinating?*

Who was Lee Seogeun?

He was a blood relative who had inherited the Sect Leader’s martial arts, as well as a First Rate swordsman.

When the Third Young Master first accepted Lee Seogeun’s challenge to a duel, Wipeng had inwardly sighed. *What nerve did a guy who had barely escaped Third Rate think he had?*

And then what? *Come out? Let’s have a go?*

*Crazy bastard. He’s talking shit.*

Something did seem to have changed lately. Hadn’t he suddenly started using polite speech without fail? Hadn’t he started practicing martial arts until late at night?

Oh, and there was also that bullshit about losing his memory.

At the time, Wipeng had wondered if the man had gone insane. But when he heard today that the Third Young Master had laid a hand on the Mount Heng Sword Sect’s cherished jewel, it dawned on him. He had nearly ascended to heaven on the spot.

*Of course. A human being can’t change overnight.*

Wipeng had served in the Jin Family of Taiyuan for more than ten years. In his eyes, Jin Taekyung was past a bad seed with yellow sprouts—he was practically gold.[^1]

But what could he do? Taekyung was his lord’s beloved youngest brother and a direct-line member of the Jin Family. Wipeng had been planning to rescue him before Lee Seogeun turned him into a half-cripple.

And yet…

Whack! Whack! Whack!

Now Taekyung was beating Lee Seogeun without mercy.

Jin Taekyung.

The martial arts he was using were ones Wipeng knew well. The Jin Family’s Manoeuvre Technique and Spear Technique.

He was fairly skilled at linking the two techniques together, and there was even a seasoned air to his movements—the hard-won experience of a wandering martial artist who had spent around ten years roughing it in back alleys.

*What in the world…?*

Martial arts could not be mastered through one or two days of effort.

That was the natural order Wipeng believed in, and he knew exactly one person who defied it.

*The Second Young Master.*

Jin Mukyung, the Second Young Master of the Jin Family of Taiyuan. A genius who had reached the Peak realm before the age of twenty—a true prodigy who had gone against the natural order.

*Could the Third Young Master possibly…?*

Wipeng’s thoughts went no further. A commotion had broken out around them.

“This duel is invalid!”

“Stop the duel immediately!”

“The Jin Family of Taiyuan used underhanded tricks!”

“That’s right! Otherwise, how could our Young Master possibly lose to trash like that—”

The Mount Heng Sword Sect warriors who had been snickering moments ago now had their hands on their sword hilts.

*What a bunch of lunatics.*

It was true that the Mount Heng Sword Sect had been riding high lately, but for these underlings to cause such a scene—

Just as Wipeng, unable to tolerate it any longer, was about to step forward—

Whoosh—smack!

The wind blew, and some ten teeth went flying through the air.

A Mount Heng Sword Sect warrior, blood pouring from the corner of his mouth, stared blankly up at the enormous shadow looming over him.

“What trash?”

Buh. Buh-buh.

Jin Wikyung looked down calmly at the warrior, who could no longer get the words out. Then he struck the man across the mouth with a palm as large as a cauldron lid.

Smack! Clatter.

The warrior spat out every tooth he had left, then lost consciousness and collapsed.

Leaving the frozen Mount Heng Sword Sect behind, Jin Wikyung returned to his seat and resumed watching the duel.

Wipeng sighed.

“There could be a problem…”

“Wipeng.”

“Yes?”

“Don’t say anything.”

Jin Wikyung looked at his youngest brother with shining eyes and added,

“This is the best moment of my life.”

* * *

This was my first time using martial arts in a real fight. After learning martial arts, I hadn’t had any reason to fight anyone—and I hadn’t wanted to fight anyone, either.

*But…*

I had always thought about it. If I ever encountered an enemy, if the moment came when I had to use my martial arts in an actual battle, how would I respond?

In that respect, my time in the training hall had meant a great deal.

Whack!

“Guh!”

Lee Seogeun’s back bent like a shrimp when the shaft of my spear struck him directly in the abdomen.

He had dropped the greatsword in his hands a long time ago. I kept advancing and swinging the shaft, and every time I did, Lee Seogeun’s screams rang out.

Whack! Whack! Whack!

“Gaaaah!”

At first, I had been bewildered. *My kick worked? Lee Seogeun was Level 30, and I was only Level 14.*

But after exchanging more than fifty blows, I realized the truth.

*I’m stronger.*

Lee Seogeun was definitely strong. If I compared him to Hunters, he was at least equivalent to a C-rank Hunter.

But I was stronger. The difference was slight, but it was undeniable. Strength, Stamina, Agility.

*And experience.*

“Graaah!”

Lee Seogeun charged at me with a roar. He was fast. And destructive. Every step he took left the training-ground floor dented and cracked.

*But he has no finesse.*

Lee Seogeun was young. And because he was young, he lacked experience. Against a weaker opponent, he could make up for that lack with sheer strength. But I was different.

I was stronger, and I had more experience.

*I’m going to win. Without a doubt.*

It wasn’t a resolve. It was a certainty.

That was why I threw away my spear without hesitation. A clash between two unarmed bodies.

The moment Lee Seogeun saw me discard my weapon, fire poured from his eyes.

“You looked down on me? You dare—how dare you!”

Anger stiffened the body and simplified its movements. I tripped Lee Seogeun’s leg as he charged like a bull and sent him tumbling.

Then I climbed onto his chest as he tried to get up.

“What is this…?”

Looking down at his bewildered eyes, I asked,

“Have you ever heard of full mount?”

I didn’t wait for an answer. I drove my fist straight down.

Lee Seogeun desperately shook his head from side to side, but it did him no good.

Bam-bam-bam-bam!

Chin, cheek, forehead, nose… I rained blows down on every part of his face without discrimination. Lee Seogeun twisted his body endlessly and screamed until, at some point, he went limp.

*This should be enough.*

My original purpose in accepting the duel was to avoid war with the Mount Heng Sword Sect.

It would be a problem if Lee Seogeun suffered serious injuries. I had to stop at a reasonable point.

With a little concern, I shook Lee Seogeun by the shoulder.

“Hey, are you oka—”

Smack!

The world flashed before my eyes.

A little dizziness. Drops of bright-red blood dripped from my stinging chin.

The result of Lee Seogeun’s fist grazing me.

*Ah. I let my guard down.*

If I hadn’t instinctively jerked my head back, I would have been in serious trouble. That blow had been imbued with internal energy.

“You dodged that?”

Lee Seogeun quickly broke free of the mount and scrambled away, his face filled with extreme bewilderment.

Of course. He probably hadn’t imagined that a guy like me—no, a guy like Jin Taekyung—would humiliate him like this.

Especially after his decisive strike had been rendered useless.

“This can’t be… This can’t be happening.”

I answered Lee Seogeun, who muttered as if he were bewitched.

“Life’s full of surprises.”

“Why! How! How could this possibly happen? I’m Lee Seogeun. I’m Lee Seogeun of the Mount Heng Sword Sect!”

Lee Seogeun shouted with bloodshot eyes.

“I honed my skills for ten years. So why! Why do I lose to trash like you? To someone as debauched and lazy as you!”

Although he was only a game character, for that moment I could sympathize with Lee Seogeun’s feelings. The sensation of having all his efforts betray him. The futility and emptiness.

*I felt that way, too.*

I had felt it for seven years. It had dulled with time, but the sense of deprivation had never disappeared. In the end, I had accepted it.

Reality was cruel.

I spoke to Lee Seogeun.

“Give up now. You’re weaker than me.”

Those words made Lee Seogeun’s eyes go wild with rage.

“Shut your mouth!”

The air around us crackled.

Lee Seogeun gathered every last bit of strength he had left, then shot forward like an arrow.

“I told you clearly. You made your choice.”

“Stop spouting bullshit!”

Whoosh.

With the sound of air splitting apart, his fist grazed my face by a hair. That alone sliced my skin and drew blood.

It was faster and stronger than any attack I had seen from him so far.

*But the same goes for me.*

I channeled internal energy into my right foot and brought it down on the top of Lee Seogeun’s foot.

Crack!

With the sound of breaking bone, his foot slammed into the training-ground floor and sank into it.

“Graaah!”

I drove my knuckles into his screaming face. His nose broke, and teeth scattered through the air. With his leg buried up to the calf, he couldn’t even pull himself free.

One more.

More.

More.

Whack. Whack. Whack.

Chest. Side. Stomach.

And finally—

*The solar plexus.*

Thump!

It landed cleanly. And it wasn’t merely a punch. It was a single blow with a tremendous concentration of internal energy behind it.

Lee Seogeun’s eyes widened.

“Guh!”

His pupils lost focus. His strength left him, his back bent backward, and he collapsed. I watched the motion as if it were happening in slow motion.

Even my right foot shooting toward his abdomen.

Pop!

With a sound like a balloon bursting, Lee Seogeun’s body went flying through the air.

Everyone watched it happen. Jin Wikyung, Wipeng, the people of the Jin Family of Taiyuan, and the warriors of the Mount Heng Sword Sect.

And me, too.

Thud.

Lee Seogeun flew more than ten meters before landing. Whether he had passed out or not, he did not move.

I let out the breath I had been holding and stood tall beneath the dozens of gazes that had shifted from Lee Seogeun to me.

“Whoo. Whoo.”

Ding.

> **System**
>
> - The **Duel** Quest has been successfully completed!
>
> - Quest rewards will be distributed!
>
> - You have acquired the Title **Gambler**!
>
> - You have gained EXP and Fame!
>
> - An additional reward has been granted for your overwhelming performance!
>
> - **Jin Family’s Cultivation Technique** has risen to the Fourth Stage!
>
> - **Qi Sense** has risen to the Third Stage. You can now detect targets up to Level 50.
>
> - Level up!
>
> - Level up!
>
> - Level up!

The System notifications sounded like celebratory fireworks.

* * *

The Mount Heng Sword Sect left.

Since they had all arrived on horseback, the Jin Family of Taiyuan even had to lend them a carriage to transport the injured.

But Lee Seogeun was one thing. Who was the other guy?

All his teeth were gone, and the cloth stuffed into his mouth was soaked with blood. Good Lord. What kind of bastard had—

Jin Wikyung patted me on the shoulder with a solemn expression.

“Well done. You performed better than I expected.”

“Ah, yes. Thank you—”

“Why are you looking at me like that?”

*Because there’s blood splattered on your cheek.*

I had no idea why, but somehow he had turned a person into a cripple in that brief span of time.

“So, what do you think?”

“Pardon? What do you mean?”

“About ending your confinement. It is true that your usual conduct has been disgraceful, but after the remarkable performance you showed today, this is a great blessing for our family.”

Jin Wikyung looked around as he continued.

“What do the rest of you think?”

The senior members looked displeased, but none seemed particularly inclined to object. Compared to the looks they had given me in the meeting hall earlier, I almost felt that they were favorable.

*Is it because they’re Murim people?*

In the novels, Murim was a place where justice mattered, but strength came first. Maybe defeating Lee Seogeun had influenced them.

“You should answer him. Hahaha.”

…Or maybe it was because of Jin Wikyung.

His mouth was smiling, but his eyes were not. With the blood on his cheek, he looked like something out of a horror movie.

“I wholeheartedly agree.”

Once Wipeng’s manipulation of public opinion was added to the mix, one by one, the others voiced their agreement.

Jin Wikyung watched the coerced vote, produced by a show of force, and smiled in satisfaction.

* * *

*Damn it. Damn it. Damn it!*

Lee Seogeun bit down hard on his lip. Jin Taekyung’s face refused to leave his mind.

*I lost? To trash like him?*

The Jin Family of Taiyuan incident had given him more than enough justification.

If the Mount Heng Sword Sect gained something from the matter, that would be enough. And if the Jin Family refused, escalating into a full-scale war would also have been a success.

If he turned Jin Taekyung into a half-cripple, word would have spread throughout Shanxi. The Jin Family of Taiyuan had suffered humiliation at the hands of the Mount Heng Sword Sect.

But he had failed.

*How could this have happened?*

He had taken up a sword as a child. He wasn’t a genius, but he wasn’t ordinary, either.

The second son of the Mount Heng Sword Sect. A promising young martial artist. A First Rate swordsman. He had always been the object of admiration…

*Damn it!*

Everything he had possessed had been smashed to pieces today. For the first time, he had been forced to kneel before Jin Taekyung’s merciless violence—and he had lost consciousness.

When he opened his eyes, he was already inside a carriage.

Even this carriage belonged to the Jin Family of Taiyuan.

Fire poured from Lee Seogeun’s eyes.

*I’ll kill you. I’ll kill you with my own hands, Jin Taekyung!*

Unable to contain his rising fury, he slammed his fist into the carriage wall.

The carriage stopped moving.

Lee Seogeun shouted roughly,

“What are you doing? Don’t dawdle. Get moving again!”

At that moment, his brow prickled.

- We should get moving, yes. But going to the Mount Heng Sword Sect would be a little troublesome.

*Sound Transmission?*

“Who is it!” Lee Seogeun shouted, but no sound escaped his throat.

His chest felt tight, and his throat hurt as if it were on fire. The carriage began moving again.

- Let’s do this. Mount Beimang first. We can go to the Mount Heng Sword Sect after.[^2]

*What does that mean—*

It took only the time it would have taken to blink a few times.

His limbs went numb, and pain flared violently through his body. Lee Seogeun turned his trembling head.

Someone wearing a mask was staring at him.

“Grrk… grrrk.”

*Who are you?*

Instead of a voice, dark, discolored blood poured from his mouth.

His vision blurred. The sounds around him grew distant.

*Sa… save me…*

That was his final thought.

The next moment, he plunged headfirst into darkness.

“Farewell, Young Hero.”

The masked man smiled brightly as he retrieved the large blue-black needle from the dead man’s brow.

[^1]: *Ssaksumyeon norata*—“the sprouts are yellow”—means a hopeless case. The line pushes yellow all the way to gold to make that worse, not to call him born rich.

[^2]: Mount Beimang is a traditional burial ground; “going to Beimang” means dying.
## Chapter artifact 16

# Chapter 16

“Whew. Finally done.”

Jin Wikyung set down his brush as he spoke. Wipeng, who was sitting in a chair beside the door as always, raised his head.

“You’re getting faster at handling your work. You must be exhausted toda—”

Wipeng let his words trail off. He had just noticed the mountain of documents still piled on the table.

Come to think of it, it was only around noon. There was no way anyone could finish that much work in so little time.

*Did I hear him wrong?*

“Good. This should be enough…”

This time, it wasn’t a hallucination. The proof was Jin Wikyung’s face, which suddenly rose above the pile of documents.

“Wipeng, come here. This is very important.”

His voice was so serious that Wipeng grew slightly concerned.

*Did something major happen?*

Perhaps they had discovered some serious embezzlement in the documents. Or maybe the Elder Council, which had been constantly watching for an opportunity, had caused some kind of incident.

*This is bad. We haven’t even finished dealing with the Mount Heng Sword Sect yet.*

A moment later, Wipeng accepted the document in question from Jin Wikyung. His expression twisted into something bizarre.

“…What is this?”

“You can’t tell? It’s a drawing.”

Just as Jin Wikyung said, the problematic document Wipeng had expected was nowhere to be found. What he had been handed was a single sheet of rice paper covered in drawings.

“No, that’s not what I meant. Why are you suddenly—”

Jin Wikyung cut him off with a secretive smile.

“Look closely. It isn’t an ordinary drawing.”

*It isn’t an ordinary drawing?*

Wipeng’s eyes lit up.

All kinds of legends circulating through Murim flashed through his mind.

A Daoist who achieved ascension after looking at a single painting. An absolute master who attained enlightenment after seeing a mural in an ancient cave!

Wipeng’s gaze roamed over the rice paper for a long while. Then, at some point, it began to tremble as if struck by lightning.

“T-this is, perhaps…!”

“You noticed. That’s right.”

Jin Wikyung continued with a chuckle.

“I tried drawing yesterday’s duel.”

“……”

“Lee Seogeun lying defeated, and Taekyung standing proudly! The sky spread above the head of the young hero who would one day become the greatest under heaven!”

“……”

“I deliberately chose a composition looking up from below. What do you think? It’s good, right? Isn’t it?”

Wipeng’s hands trembled around the rice paper. If he had been acting on impulse, he would have crumpled it, torn it apart, covered it with a week’s worth of piss and shit, dried it thoroughly, and burned it.

But—

“…It’s very well drawn.”

Wipeng was a rational man. He summoned the magnificent mental fortitude of a martial artist at the Peak realm.

Of course, he also had enough courage to reprimand a lord whose sanity was in serious doubt.

“How can you say that when there’s so much work piled up? Are you telling me that you spent the entire morning drawing this one picture?”

“Of course not.”

“Then you know how ridiculous this is—”

“Did you think I spent three hours focusing on only one thing?”

“What?”

“Of course I drew another one. I was going to show it to you later, but you really are quick to catch on.”

Wipeng accepted the next sheet of rice paper from Jin Wikyung with trembling hands. Grinning from ear to ear, Jin Wikyung began explaining the drawing.

“I tried to depict the scene immediately after the duel. The young hero declares that he won’t rest on his laurels and will return to the training hall! And the people gazing up at him in admiration!”

“I agree with a considerable part of that. The Third Young Master really has changed a great deal.”

“Right? I was surprised myself.”

After defeating Lee Seogeun in the duel, Jin Taekyung had defied everyone’s expectations and returned to the training hall. Jin Wikyung’s eyes grew hazy as he recalled the events of the previous day.

“I always knew a day like this would come. The youngest is a heavenly eagle. Wipeng, can’t you hear it? The powerful sound of Taekyung’s wings beating…”

“I don’t know about wings, but I can hear you spouting nonsense.”

Wipeng lowered the rice paper with a sigh that sounded as if he had given up on everything.

Flap.

“Gasp.”

“See? You can hear it!”

Wipeng hurriedly turned toward the window. A hawk that had just landed was preening its feathers. A small container hung from its ankle.

“It’s a messenger hawk.”

These hawks were trained intensively from the time they were fledglings before being put to use as messengers.

The Jin Family of Taiyuan had only two messenger hawks, and they were sent out only for matters of extreme urgency.

“We have a problem.”

Jin Wikyung muttered in a subdued voice.

And that problem soon made itself known.

* * *

“My name is Han Yeop.”

“Pardon?”

“It’s an honor to meet you.”

It was a sudden introduction. Of course, I knew his face.

He was the person I had seen most often since entering the training hall.

*Should I call him the training hall’s guard?*

Guard. Guarding martial artist. Whatever the proper term was, the NPC in front of me was a martial artist of the Jin Family of Taiyuan in charge of the training hall. Bringing me meals and herbal decoctions was one of his duties, too.

*But why is he introducing himself all of a sudden?*

This was an NPC I had never exchanged a single word with. He didn’t seem to bear me any ill will, but he wasn’t especially friendly, either.

“Ah, yes. Nice to meet you, too.”

Despite my lukewarm response, the guard—or Han Yeop’s—face brightened.

*What the hell? Why is he suddenly acting like this?*

“I was there yesterday, too.”

“There? Oh.”

He meant the duel. So many people had gathered that it wasn’t surprising for Han Yeop to have been among them.

“I watched from beginning to end. I saw the heroic way you fought against that vicious Lee Seogeun of the Mount Heng Sword Sect!”

*Vicious? Heroic?*

*That’s how it looked?*

Honestly, from a modern man’s perspective, one was as bad as the other.

No, I almost wanted to take Lee Seogeun’s side. As an older brother myself, even if my little sister’s personality were fucking awful, I’d lose my mind if she said she was dating a guy like Jin Taekyung.

Of course, the Mount Heng Sword Sect’s attitude and proposal had been absurd. That was why I had no choice but to fight.

“My heart trembled the entire time I watched. I’m sure everyone there felt the same way.”

Han Yeop continued with an excited expression. He seemed to be under a serious misunderstanding, and I had no idea when I was supposed to stop him.

“I used to misunderstand you, too, Young Master. But now everyone in the family knows the truth.”

This time, I couldn’t help asking.

“The truth? What truth?”

“That is…”

Han Yeop whispered in a voice so hushed that it was practically a secret. Leaving aside the hot breath against my ear, the content itself gave me goose bumps.

In other words—

“I’m the Jin Family of Taiyuan’s secret weapon?”

“Yes, yes!”

Han Yeop nodded furiously.

“Your behavior until now was all an act, and ever since you were young, you’ve undergone bone-shattering training, becoming a man accomplished in both civil and martial arts, with virtue and righteousness, a sl—sl—”

I couldn’t bring myself to say that word. Han Yeop came to my rescue before my hands and feet could curl up from embarrassment.

“The Sleeping Dragon of Shanxi! There isn’t a single person in the family who doesn’t know now! The truth that you are Shanxi’s Sleeping Dragon, still hiding in the water instead of ascending to the heavens!”

*Oh, please. Somebody save me. And don’t shout it out loud.*

The Sleeping Dragon? There wasn’t a single person in the family who didn’t know?

*If I die, the cause of death will be death by embarrassment.*

As I writhed in agony, Han Yeop asked with shining eyes,

“It’s true, isn’t it? I know it’s rude, but just between us…?”

This wouldn’t do. I decided to suppress this ridiculous, cringe-inducing rumor whose origin I couldn’t even guess, then opened my mouth.

“I have no idea who started such an absurd rumor, but…”

That was when it happened.

Ding.

> **System**
>
> A rumor about the **Sleeping Dragon of Shanxi** is spreading throughout the **Jin Family of Taiyuan**.
>
> Fame has risen by 10 due to the influence of the rumor.
>
> The more people believe the rumor, the more Fame will rise.

I continued with a solemn expression.

“Every word of it is true.”

“I knew it! I believed it with all my heart!”

I watched Han Yeop walk away with a face full of rapture and shed a single tear.

*Fuck…*

*Ah, I miss my mom.*

* * *

I realized several things through my duel with Lee Seogeun.

First.

*I’m strong.*

Early in the game, I had knocked down Cheonryeokbu, who had appeared as the tutorial NPC, in a single hit. What had only been a suspicion back then had now become a certainty.

I was strong. Strong enough to defeat a Level 30 like Lee Seogeun without much trouble. The difference in combat experience had certainly played a part, but my basic stats were overwhelmingly superior.

*Strength, Stamina, Agility. They were all similar, or I had a slight edge.*

Stats. In other words, the difference in abilities. In this game, I was a player, and I had continued growing by using the System.

I had raised my stats rapidly by learning martial arts, training, and completing various Quests. The result had shown itself in the duel.

And second.

*I don’t have enough internal energy.*

Lee Seogeun had surpassed me in internal energy. No, he had been overwhelmingly ahead.

What had he been eating growing up? Even after I smashed him dozens of times with the spear shaft, and even when I beat him one-sidedly from a mount, he endured it. He even counterattacked and drew on more internal energy at the final moment.

*I currently have ten years of internal energy.*

Lee Seogeun probably had twenty years—twice as much as I did. That led me to a third realization.

*The difference in internal energy determines the stage of one’s martial arts.*

I had defeated Lee Seogeun, who was First Rate. But the realm displayed by the System still said I was Second Rate.

I thought the reason lay in internal energy. Once I raised the one ability I lacked, wouldn’t my realm finally rise as well?

After organizing my thoughts that far, another idea suddenly occurred to me.

*This is basically just Hunter rank classification.*

A newly awakened Hunter had to be tested at a designated center for their abilities, suitable profession, and mana capacity. No matter how high their physical abilities were, if their mana capacity was lacking, they received a cold reception during the rank evaluation.

That was also why mages started at D-rank at the lowest. Because of their profession, mages had plenty of basic mana from the start.

*Still, the game is better than reality.*

At least you could grow here. Reality had no such thing. Even I had only managed to get mixed in with the E-ranks by working my ass off for seven years. I was still an F-rank Hunter.

Anyway, I had now drawn a rough outline.

*My stats are sufficient. I’ll keep cycling the Jin Family’s Cultivation Technique whenever I have time, and focus on taking Quests that reward EXP.*

It had been over a week since I was trapped in this godforsaken game. I didn’t know what kind of nonsense was happening in the real world, but I could forget about being rescued.

I needed to prepare properly and finish this.

“Open Quest window.”

Ding.

> **System**
>
> **Quest**
>
> **Logout**
>
> You must now make your way through this harsh Murim.
>
> Become stronger and more famous.
>
> For the day that will come someday…
>
> **Grade:** Main Quest  
> **Restriction:** Jin Taekyung  
> **Mission:** Achieve the **First Rate** realm (Incomplete)
>
> &nbsp;&nbsp;&nbsp;&nbsp;Reach Level 30 (17 / 30)
>
> &nbsp;&nbsp;&nbsp;&nbsp;Reach Fame 500 (70 / 500)
>
> **Reward:** **Logout**

“Ugh. This is brutal.”

I sat cross-legged. Two days remained before my seclusion ended. I intended to gather as much internal energy as possible.

> **System**
>
> Fame has risen by 3 due to the influence of the Sleeping Dragon of Shanxi rumor.

The Fame-increase messages that chimed from time to time were a small source of comfort.

* * *

Late at night, the lights came on in the main assembly hall. At the request of the Lesser Family Head, a secret meeting of the family council was taking place.

It was very late, and the summons had been so sudden that several of the senior members wore sour expressions.

“A sudden summons? What is this about?”

“Exactly. They didn’t even tell us why they were calling us here at this hour.”

“That’s what happens when the Lesser Family Head is still young. He doesn’t know procedure or etiquette.”

“He must have grown rather full of himself after yesterday’s events. Though I suppose his only weakness has disappeared. No one expected the Third Young Master to be that capable.”

“The Elder Council must have been deflated. They were probably preparing to make a major move over the Third Young Master.”

“Hmph. Even now, the Head Elder should step forward and set the family straight.”

“Careful. Watch your tongue…”

At that moment, every sound abruptly stopped. The doors to the meeting room opened from both sides, and Jin Wikyung entered.

The senior members had varying opinions of their Lesser Family Head, but the silence that settled over the room the instant he appeared proved that he possessed the qualities of a leader.

“Thank you all for answering my summons at this late hour.”

Jin Wikyung took the seat of honor and spoke his opening words, but he found it difficult to continue.

*What should he say? Where should he begin, and how?*

His head throbbed. But this was something he had to tell them.

“The reason I called everyone here today is…”

That was when a strange voice interrupted him.

“It must be because of the Mount Heng Sword Sect.”

The voice was bizarre. At first, it sounded like an old man’s. And yet it was young as well—rough one moment, smooth the next. There was also an inexplicable resonance to it.

*Could it be…?*

Jin Wikyung’s face twisted.

The doors to the meeting room, which had seemed as if they would never open again, began to part.

Step. Step. Step.

Five old men walked in as if they were gliding across the floor. The instant everyone recognized the old man at the front, they hurriedly stood and bowed their heads.

“We pay our respects, Head Elder!”

The Head Elder. He had appeared after keeping himself shut away from the world for years.
## Chapter artifact 17

# Chapter 17

Circulating qi.

It was a method of regulating one’s energy by evening one’s breathing. The act of taking qi from outside the body, circulating it within, and accumulating it.

Right now, I was circulating qi using the Jin Family’s Cultivation Technique.

*This still feels incredible every time.*

I had never realized there were so many acupoints in my body.

I had once heard that the human body contained more than three hundred and sixty acupoints, but based on what I could feel while circulating qi through the cultivation technique, there were even more than that.

*Is it because I’m a virtual game character?*

*Whatever.*

The ten years of internal energy I drew up from my dantian circulated through my body. If internal energy was a car, then the meridians were a highway. All I had to do was sit behind the wheel and press the accelerator.

The internal energy raced along the straight and curving meridians throughout my body before returning to my dantian.

*And this is where the real problem starts.*

I took a long, deep breath. Then I felt it.

Another internal energy, occupying my dantian like an enormous boulder that would not budge no matter how hard I willed it.

*What the hell are you?*

It had been a mystery ever since I first circulated qi. An unidentified energy that had taken root like it owned the place.

I didn’t know where it had come from, how it had been formed, or why I couldn’t use it, but one thing was certain. This unidentified energy contained more power than the ten years of internal energy I possessed.

*Until now, I hadn’t even dared touch it.*

To be more precise, I hadn’t intended to. Until a few days ago, I had been waiting for rescue while doing just enough to stay alive.

But things were different now.

*I need more internal energy.*

The situation had changed. If I wanted to escape on my own, I had to fulfill the Logout Quest’s condition: reaching the **First Rate** realm.

I also knew that I needed internal energy on the level of Lee Seogeun’s to become First Rate.

*I’ll make it mine.*

I cautiously began moving my internal energy.

The moment I sent it toward the unidentified energy, half anxious and half expectant, I realized something.

*Not even close.*

Internal energy was, strictly speaking, qi itself—something without a physical form. And yet the instant the two energies touched, I felt powerful rejection and resistance.

No. It was even pulling me in. At this rate, it was going to eat me alive.

*Hey, hey, hey! Wait a second!*

I hurriedly withdrew my internal energy and shook off the unidentified energy, which clung to me until the very end. At the same time, a System notification rang out.

Ding.

> **System**
>
> - You have trained the **Jin Family’s Cultivation Technique**. Internal energy has risen slightly.
>
> - As a result of repeated training, **Sinews** and **Bones** have each increased by 1.

“What the hell was that?”

I calmed my pounding heart and opened my Status Window.

> **Status Window**
>
> **Lv. 17 Jin Taekyung**
>
> **Class:** Second Rate martial artist  
> **Fame:** 70  
> **Titles:** 4 (Title effects active)
>
> - **Scion of a Prestigious Family** — All stats +5, Fame +50
> - **Family’s Shame** — All stats –5, Fame –50
> - **Novice Trainee** — Training speed +10%
> - **Gambler** — Combat-related stats +10% in one-on-one matches
>
> **Strength:** 65  **Stamina:** 65  
> **Agility:** 75  **Intelligence:** 10  
> **Charm:** 10  **Internal Energy:** 10 years
>
> **Remaining Points:** 0

The numbers in my Status Window were fairly impressive by now.

I had gained three levels all at once through the Duel Quest, then distributed the thirty points equally among Strength, Stamina, and Agility.

But looking at the Status Window still left a bitter taste in my mouth.

*My internal energy is the only thing that hasn’t changed.*

This damn System kept saying that my internal energy had risen, but the amount displayed in the Status Window remained exactly the same.

*Do I need to take a spirit pill, an elixir, something like that?*

I thought of Jin Wikyung. If I screwed up my courage and said, *Big brother, just give me one spirit pill,* I didn’t think he would refuse me outright.

I’d ask him the next time I saw him. I would also ask about the unidentified energy inside my dantian.

Krrrummble.

At that moment, the entrance to the training hall opened, and two people stepped inside.

“Um, Young Master Jin?”

It was Han Yeop. Behind him stood a martial artist I had never seen before. The man spoke in a blunt tone that matched his appearance.

“The Lesser Family Head commands you to attend the family council.”

“The Lesser Family Head?”

That worked out perfectly. There was something I wanted to ask him about.

* * *

“It is beyond doubt. A few bones were broken, and there was some minor internal damage, but that level of injury could never—”

“Are you sure? You swear that on the name of the Medicine King Hall Leader?”

“I said it’s true! I examined him myself!”

“Then why are you talking down to me? I treated you with respect because you’re another Hall Leader, and now you think I’m a joke!”

“You were the one who started talking down to me, White Tiger Hall Leader!”

I stared blankly at the ceiling of the meeting room. The shouts and curses flying from every direction made my ears ring.

*What the hell is this?*

This wasn’t what I had imagined a family council would be like. I had pictured a quiet, orderly atmosphere where everyone exchanged opinions and searched for common ground…

“You think every Hall Leader is your equal? You’re nothing but some quack doctor!”

“Listen to this young bastard. I ought to shove a large needle straight into his perineal acupoint!”

Two men in their forties or fifties, both developing M-shaped hairlines, were grabbing each other by the collars and shaking one another. Just watching them made my head hurt.

The problem was that scenes like this were unfolding all over the room.

Maybe that was why most of the people there didn’t seem to notice me opening the door and taking my seat.

—You came?

The voice sounded as if it had entered through my head rather than my ears. Sound Transmission.

I turned my head and met Jin Wikyung’s gaze from the seat of honor. He gave me a tired smile.

—It’s a madhouse, isn’t it?

*You said it. Why did you call me to this madhouse, you old man?*

When I shot him a reproachful look, Jin Wikyung sent another message through Sound Transmission, his expression turning sheepish.

—I couldn’t help it. The Elder Council demanded your attendance. In any case… you are involved in this matter.

*The Elder Council? I’m involved in this matter?*

*What matter am I involved in…? Oh. The Mount Heng Sword Sect?*

I quickly pieced things together amid the shouting and cursing.

If there was one recent incident connected to me, it was the Mount Heng Sword Sect. And because of that incident, this place called the Elder Council had summoned me.

That had to be it.

*Come to think of it, there are some old men here I’ve never seen before.*

There were four of them. Every one had a face covered in age spots and hair that had gone completely white.

They watched the men with the M-shaped hairlines grab each other by the collars with cold eyes. Anyone could see it was a nursing home—or rather, the Elder Council.

—And… the Head Elder is here.

I turned toward Jin Wikyung without thinking, then flinched.

*What the hell? Where did that old man come from?*

I had only just noticed that there were two seats of honor today. An old man was sitting to Jin Wikyung’s right, staring at me. His gaze made my face prickle.

*Is that old man the Head Elder?*

White hair, a white beard, and white eyebrows. He looked like an immortal who had stepped out of an old painting. His back was straight, his shoulders broad, and his skin taut enough to make his age seem meaningless.

*But why is he staring at me so intently?*

I gathered strength in my eyes and tried to glare back at the Head Elder…

Then I quietly looked away.

Not because I thought I would lose if we locked eyes. It was respect for my elders. Respect for my elders. Really.

*I’ll just keep my head down.*

Jin Wikyung’s Sound Transmission continued in the meantime.

—You may not know this because you lost your memory, but the Head Elder is your great-uncle and the most senior elder in the family. Be especially careful with your words and actions.

I hadn’t even seen my father’s face, and now I had a great-uncle.

*Maybe this place has relatives by marriage, distant cousins, and every kind of obscure uncle, too.*

I gave Jin Wikyung a small nod.

—And… you must not be flustered by what happens from this point onward. Calmly tell them only the truth. Do you understand?

I didn’t know exactly what was going on, but one thing was certain: Jin Wikyung was on my side.

I nodded again, and Jin Wikyung rose with a faint smile.

“Silence, everyone.”

His voice, infused with internal energy, swept across the meeting hall.

“This is a family council of the Jin Family of Taiyuan, and we have gathered to discuss a grave matter. Since our witness has arrived, I intend to begin the interrogation.”

The meeting hall had gone quiet without me noticing. With everyone’s attention focused on him, Jin Wikyung spoke.

“By the authority of the Lesser Family Head and current acting Family Head, I begin this interrogation. Third Young Master Jin Taekyung, step forward.”

I felt everyone’s eyes on me as I walked forward. I had expected this much. They hadn’t summoned me for no reason.

But…

“I ask you this. Did you poison Lee Seogeun of the Mount Heng Sword Sect?”

That was something I hadn’t expected.

* * *

“No.”

I barely managed to force the word out. My thoughts were a mess from the sudden question.

*Lee Seogeun was dead? Poisoned, at that?*

“Tell us the truth. If it turns out to be a lie…”

“I have nothing to do with Lee Seogeun’s poisoning.”

My answer was as sharp as a blade. Jin Wikyung let out a sigh of relief.

—Keep doing exactly this.

The interrogation proceeded quickly. They asked questions, and I answered them.

Starting with Jin Wikyung, one question after another came flying at me.

About half of the questions concerned whether I had been involved in poisoning Lee Seogeun, and I continued to deny it.

*Because it was true.*

Just in case, I secretly opened my System Window to check. It was certain. None of my martial arts or abilities had anything to do with poison. I didn’t have any such Items, either.

That was why I could answer without hesitation.

“No.”

The problem was that, at some point, the atmosphere in the meeting hall began to grow strange.

“Do you have any evidence to prove it?”

“Evidence?”

White Tiger Hall Leader, was it? The man, whose name I didn’t even know, stared at me with obvious displeasure.

“That is correct. Evidence. I mean evidence that would prove the Third Young Master’s innocence.”

*What the hell is this bastard talking about?*

“Why do I have to prove it?”

“What?”

“Don’t talk down to me.”

“Listen here, Third Young Master!”

“You’re free to suspect me, but shouldn’t you be the ones looking for evidence? Am I wrong?”

I’d been letting it slide, and these bastards thought they could wrap me up like a cloth?[^1]

Fuming, I glared at the White Tiger Hall Leader as he sat down, then noticed something strange.

*Well, well. Look at this.*

The White Tiger Hall Leader kept stealing glances at the old men of the Elder Council.

The strange thing was that everyone who had been pressing and interrogating me was doing something similar.

Nearly half the people in attendance were acting this way. It was getting difficult to pretend I hadn’t noticed.

*So this is a factional struggle.*

The Elder Council and Jin Wikyung.

Even now, a power struggle was taking place between the senior members of the family and the Lesser Family Head who was young enough to be their grandson.

*What a family.*

Only a few people remained to question me. The problem was who those people were.

Faces covered in age spots. Canny, experienced eyes.

The old men of the Elder Council.

The oldest and fattest of them opened his mouth.

“Enough of this empty questioning. There is only one thing this old man wishes to ask. Where did this matter begin?”

The senior members allied with the Elder Council answered as if they had been waiting for the question.

“The Third Young Master.”

“Who was it that dragged our family’s reputation through the mud with disorderly words and conduct?”

“The Third Young Master.”

The same answer came from several places around the room.

“Then who was it that provoked the Mount Heng Sword Sect’s prized treasure and brought us to this crisis?”

“…”

*Just kill me already, you bastards.*

[^1]: In Korean, the line puns on *boja* (“let’s see / wait and see”) and *bojagi*, a wrapping cloth.
## Chapter artifact 18

# Chapter 18

The atmosphere grew worse by the second.

“The important fact is that the duel was fair!”

“Fair? Since when is using poison considered fair? Is this the Sichuan Tang Clan or something?”

“The man himself said he didn’t do it! And as the Medicine King Hall Leader said earlier, Lee Seogeun was perfectly fine—”

“Of course the Third Young Master would say he didn’t. And how can you believe that quack?”

“A quack? You little bastard!”

Then one particularly agitated voice pierced my ears.

“If necessary, we should stop the war even if it means offering up the Third Young Master’s head!”

…What?

“What kind of outrageous nonsense is that?”

“Am I wrong? Let’s just admit it. The Mount Heng Sword Sect is stronger than our family. If war begins, hundreds will die or be injured, and in the worst case, our family could be destroyed. If we hand over the Third Young Master, who caused all this, won’t everything be over?”

Was that talk or a fart? It had been a while since I’d heard such spectacular bullshit. The back of my neck tightened, and my chest grew tight.

But someone else stepped forward before I could.

“What did you just say?”

His voice was quiet, but it carried power. In fact, its quietness made it sound even clearer.

It was Jin Wikyung. He looked around the room with an expressionless face.

“Whose. Head. Did you say we’d offer?”

Each syllable fell separately, frost coating his voice. The atmosphere was so chilling that even I shivered.

The White Tiger Hall Leader spoke up at once.

“Obviously, the Third Young Master, the main culprit behind this—ah.”

That bastard was bald, and he couldn’t read the room either. The White Tiger Hall Leader let his words trail off, but it was already too late.

“So you intend to hand the Third Young Master’s head over to the Mount Heng Sword Sect over an unconfirmed matter? Is that something a hall leader of this family should be saying?”

“No, that’s not what I meant…”

The White Tiger Hall Leader was overwhelmed by Jin Wikyung’s aura and avoided his eyes. Jin Wikyung silently glared at him.

He wasn’t normally like this, which made him even scarier now that he was angry.

Looking at the White Tiger Hall Leader’s pale face made me feel as if ten years of indigestion had finally been cured. Jin Wikyung rose from his seat and looked down at everyone with a cold expression.

“You all already know.”

He looked around the room and spoke firmly.

“That the duel was fair, and Lee Seogeun’s poisoning was a conspiracy. Knowing that, are you suggesting we submit to them out of fear?”

The members of the Elder Council faction avoided his gaze. Jin Wikyung’s sneer grew deeper.

“I don’t know who placed it in their hands, but the Mount Heng Sword Sect holds the hilt of a sword called justification. Whether it happens today or tomorrow—or whether the sword has already been drawn—we are already too late to reverse it. There is only one way forward. We fight.”

“……”

“Do you want to live? Do you want to protect the family? If you truly do, prepare the martial artists and prepare for war. Or cut off my head and my younger brother’s, then offer them to the Mount Heng Sword Sect. If all you want is wealth and glory, I suppose that isn’t a bad option, either.”

A suffocating silence took over the main assembly hall.

If one person hadn’t opened his mouth the next moment, we might have been crushed beneath that silence for hours.

“Excellent.”

It was the man who had watched the situation without saying a word until now.

The Head Elder.

* * *

The Head Elder.

A person to watch out for. The family’s highest-ranking elder and the head of the Elder Council.

I remembered the Sound Transmission Jin Wikyung had sent me earlier.

*He told me to be careful.*

Jin Wikyung was the greatest ally and adviser I had among the NPCs.

I hadn’t taken his warning lightly. Whenever I had the chance, I kept an eye on the Head Elder.

And I reached one conclusion.

*Fuck, I can’t figure him out at all.*

If someone asked me to count the number of NPCs I had encountered even once since starting this godforsaken game, the number would easily be over a hundred.

Each of them had their own expressions and personalities. The servant I met at the pleasure house wore a business smile worn down by life. The coachman who brought me here had a goofy side. The senior members I met in the family were surprisingly simple-minded and aggressive.

But the Head Elder…

*I can’t read his expression.*

He merely watched everything with that strange smile of his.

When the interrogation began. When the senior members of each faction shouted at one another. And even now.

Clap. Clap. Clap.

The Head Elder’s vigorous applause rang through the hall.

“I thought of you as merely young, but before I knew it, the Lesser Family Head had become such a dignified martial artist. Excellent. That is how the Lesser Family Head of our family should be.”

“I can only apologize for showing you such an unseemly side.”

“Excessive humility can look like arrogance. You have nothing to apologize for.”

Despite the Head Elder’s praise, Jin Wikyung’s face remained stiff.

“May this old man add a word? What do you think, Lesser Family Head?”

“I will take it to heart.”

The Head Elder slowly rose from his seat, and dozens of pairs of eyes locked onto him.

He was the family’s highest-ranking elder. In terms of authority and standing within the family, he might even surpass Jin Wikyung.

The biggest problem was that he was the head of the opposing faction—the Elder Council.

*Fuck, I’m screwed.*

Preparing for the worst, I started edging toward the door when the Head Elder’s first words reached my ears.

“You’re rotten to the core.”

Huh?

I whipped my head around. The Head Elder still wore that same strange smile.

*Did I hear him wrong?*

But I hadn’t.

“Even beasts join forces and fight when an enemy enters their den. And yet men who are supposedly senior members of this family offer up the head of a direct-line member as a solution to stop a war. Heh. So men like this sit in our family council.”

“N-no, Head Elder. You’ve misunderstood. It was merely…”

“White Tiger Hall Leader.”

At the Head Elder’s chilly call, the White Tiger Hall Leader stiffened.

“Have I been away for too long? Or is it because the Family Head is absent?”

“N-no, Head Elder.”

Going by the Head Elder’s expression, he looked like a muscular old man at a gym asking whether you’d eaten. But the content of his words was vicious beyond belief.

*What is this?*

What was going on? Why was he taking our side?

I looked around frantically, but everyone else was just as confused as I was. Both factions were visibly flustered.

“What do you think, Lesser Family Head?”

“I’m not sure what you mean.”

“If war has become inevitable, then our first priority should be to discipline those within our ranks. Wouldn’t it be best to cut off the heads of those men, who are little different from rebels?”

In the frozen air, Jin Wikyung stared at the Head Elder for a long moment before answering in something like a sigh.

“That cannot be done.”

Whew. The White Tiger Hall Leader let out a relieved sigh.

Considering how he had just been talking about offering up my head, I was a little disappointed.

*Should I suggest that we kill just him?*

“Those men not only framed a direct-line member of the family, but even argued we should hand him over to the enemy. Don’t you think that is too lenient a response?”

“They have served our family loyally for many years. I will consider it an ill-considered remark made in the heat of the moment.”

The Head Elder laughed heartily.

“An ill-considered remark. An ill-considered remark, indeed. Yes. The Lesser Family Head’s capacity is greater than I expected. Truly worthy of being the Lesser Family Head. In that case, I will not hold them responsible. I offer my thanks to the Lesser Family Head for magnanimously forgiving the thoughtless words of old men.”

When the Head Elder bowed, the others hurriedly waved their hands and bent at the waist in return.

“Oh, Head Elder, no. Our thoughts were shallow.”

“Please, don’t do this.”

“You’re only making us more ashamed. Please…”

“Head Elder!”

Jin Wikyung was the one who had spared them, yet they were making a huge scene.

Go on, put on a show. A real show.

I was watching the spectacle with a private click of my tongue when—

*Wait. A show?*

An indescribable sense of wrongness spread through my entire body. I hurriedly examined the people gathered around the Head Elder.

And then I noticed it.

The smiles flickering around the lips of the Elder Council members who had pressured me earlier.

*No way…*

Was this all planned? Every bit of it?

Why? For what purpose? Countless questions rose and vanished. My thoughts were a complete mess.

*Does Jin Wikyung know something?*

I didn’t even need to turn around to look for him. The Head Elder was already holding Jin Wikyung’s hand high in the air and shouting.

“With the Family Head absent, the Lesser Family Head is effectively the Family Head. I support the Lesser Family Head in this matter. If we unite around him, then no matter how formidable they are, they will not dare challenge the Jin Family!”

The heated atmosphere. The people’s cheers and shouts.

*Where had I seen this before?*

It felt strangely familiar.

And then—

“Thank you.”

The moment I saw the corners of Jin Wikyung’s mouth quiver and the Head Elder’s strange smile, I realized where that familiar feeling came from.

*An election campaign.*

The Head Elder’s figure overlapped with the politicians I had seen on television.

* * *

It was deeply unsettling, but once the Head Elder raised Jin Wikyung’s hand, the meeting proceeded swiftly.

The discussion about the duel, which the Elder Council faction had stubbornly kept dragging out, disappeared entirely. Instead, the meeting focused on preparing for war.

“How many men are currently available?”

“If we call back the martial artists stationed outside, roughly two hundred.”

As many as two hundred?

I was astonished by the unexpectedly large number, but the next question made me shut my mouth.

“If we select only elites of First Rate or higher?”

“Fewer than twenty. Of course, that number would be different if we included everyone present.”

Including the senior members, there were around thirty or forty First Rate masters.

I didn’t know much about the circumstances here, but that seemed like a decent number.

As expected of a prestigious family with deep roots. Two hundred years of accumulated strength didn’t simply vanish.

“What about the Mount Heng Sword Sect?”

“At least three hundred martial artists have been confirmed so far.”

Three hundred. And that was the minimum, meaning there was a difference of more than a hundred men.

But it was fine. Fights came down to numbers anyway—

“And they have more than fifty First Rate martial artists.”

This war was going to be difficult.

Still, with masters like Jin Wikyung and Wipeng, it was a fight worth attempting. They were high-level NPCs beyond what my Qi Sense could read. The Head Elder probably belonged to that category, too.

“Our family has three Peak masters in total: the Lesser Family Head, the Head Elder, and Sir Wipeng. The Mount Heng Sword Sect has five.”

…This was so damn hopeless I couldn’t even deal with it.

*What? A prestigious family with deep roots? Two hundred years of history?*

What the hell had these bastards been doing for two hundred years? I heard the Mount Heng Sword Sect had existed for less than thirty, but in terms of military strength, we weren’t merely outmatched.

We were being steamrolled. Steamrolled.

*Did the Black Death sweep through last year or something?*

Whether there had been a plague or not, I felt like I was going insane. I was staring at the meeting-hall ceiling, which had yellowed before I knew it, when I suddenly made a decision.

*I need to run.*

Around four in the morning should do. Once everyone was asleep, I’d sneak over the wall and run as far away as possible.

At my current level, I could easily take down five or six martial artists around Cheonryeokbu’s level.

I could scour every mountain I came across and rack up EXP and Fame—

“Mount Heng—A messenger pigeon has arrived from the Mount Heng Sword Sect!”

A martial artist had rushed into the hall and shouted.

Someone accepted the tightly rolled sheet of paper and unrolled it. Red words, as if written in blood, appeared before my eyes.

Even without a System translation, I could understand them.

> **Enemies Who Cannot Live Beneath the Same Sky**

*Enemies who cannot coexist beneath heaven.*

Jin Wikyung spoke with a grim expression.

“From this moment onward, our family enters a state of war. Without my seal, no one may enter or leave the family grounds, regardless of rank. Maintain a strict state of vigilance. Do not let a single ant through. Understood?”

“Yes!”

“……”

With my mind half gone, I heard a System notification ring in my ears.

Ding.

> **System**
>
> - The **Mount Heng Sword Sect** has declared war on the **Jin Family of Taiyuan**.
>
> - A **War** relationship has been established between both factions.
>
> - The **Mount Heng Sword Sect** has designated you as a public enemy of the sect.
>
> - You will incur severe penalties if you flee.
>
> - The **Main Quest — War** has been created.

…Heh. Heh heh heh.
## Chapter artifact 19

# Chapter 19

> **System**
>
> **Quest**
>
> **War**
>
> A war that will decide the fate of two families has begun.
>
> In Murim, the only way to prove yourself is through strength! Those who survive are strong, and only the strong will survive.
>
> May fortune favor you in battle.
>
> **Rank:** Main Quest  
> **Restriction:** Jin Taekyung  
> **Mission:** Surrender or destruction of the Mount Heng Sword Sect (Incomplete)  
> **Reward:** ???  
> **Failure:** ???

Jin Wikyung spoke to me as I stared fixedly at the Quest Window.

“You look very tired.”

Tired? I was amazed that my current state of mind could be summed up in such a simple word.

Instead of answering, I looked at the steaming teacup.

*The water’s already been spilled.*

I had done my best, but I couldn’t stop the war. The family council had turned into a war council, and with the Head Elder’s full support, Jin Wikyung had taken up command without hesitation.

> Martial artists of the Jin Family of Taiyuan, assemble at the main family residence immediately!

At dawn, dozens of messenger pigeons took to the sky, while messengers rode hard on horseback. A thorough security network spread out like a net.

When the family council finally broke up in that tense atmosphere, Jin Wikyung, Wipeng, and I moved to the Lesser Family Head’s office.

“It was bound to happen someday. This isn’t your fault, Taekyung.”

I felt like crying at Jin Wikyung’s warm words. Not because I was moved, but because it felt so unfair.

*Of course it wasn’t my fault!*

And since we were on the subject, why the hell did that “bound to happen someday” have to happen now?

While I was fuming inwardly, Wipeng suddenly spoke.

“My lord.”

“Why?”

“The Head Elder… I simply cannot figure out what he’s thinking.”

The Head Elder. The moment I heard that name, I abandoned all other thoughts. He was the most unsettling person among the NPCs I had encountered in this game.

He seemed genuinely devoted to the family, yet he also gave off the unmistakable air of a politician maneuvering for his own benefit.

I cautiously opened my mouth.

“What kind of person is the Head Elder?”

“He is a martial artist of a high realm, and his schemes run deep. You could call him one of the most dangerous types of people in Murim.”

“That dangerous?”

Jin Wikyung nodded heavily.

“Even the other Elders are little more than the Head Elder’s hands and feet. He rarely reveals himself, yet he has used the Elder Council to win over influential members and bring them under his command. He has been doing so for decades.”

“Then his supporting us at the family council…”

“We cannot know the exact truth, but he must have an ulterior motive. Of that, I am certain.”

“We should have killed them all.”

Wipeng cut in abruptly, his voice cold.

“They are disloyal rebels. When the Head Elder proposed killing them, I honestly hoped you would accept.”

I had felt the same way. But that had merely been the Head Elder’s clever way of speaking—a suggestion that perhaps we should back down at this point.

If Jin Wikyung had pretended to be insane and accepted that proposal, the result would have been obvious.

“A bloodbath would have broken out.”

“I know. That’s why I held back.”

The Jin Family of Taiyuan’s leadership would have split in two and continued fighting until they killed one another. If we lost, we would die. Even if we won, we would suffer tremendous damage.

*Maybe that was exactly what the Head Elder wanted.*

The Head Elder. An invisible hand.

A chill ran down my spine at the thought. It fit the image I had formed of him perfectly.

A politician like a hyena, stepping back and waiting for his moment.

Jin Wikyung tilted his teacup.

“But that is only a guess. We do not know what the Head Elder truly intends. He is still one of the family’s elders, and a powerful ally. Be wary of him, but do not make an enemy of him. For now, we need to overcome the situation rather than distrust everyone around us.”

He was telling me to look at the forest, not the trees.

The problem was that the forest itself wasn’t exactly in good shape, either.

As if he had read my thoughts, Wipeng brought up the subject.

“The situation is not good, either. According to our outside sources, rumors that Lee Seogeun was poisoned have begun spreading, and the main family’s reputation is falling.”

“In only half a day?”

“Yes. All of Shanxi is in an uproar over it.”

Concern clouded Jin Wikyung’s face.

“That is fast. Far too fast. Someone is definitely behind this.”

There was no internet here, and yet rumors had already spread across this vast land. It was certainly strange.

*An invisible enemy.*

Who could it be? A third faction? A staged act by the Mount Heng Sword Sect?

I hoped it was the latter if possible. Nothing was more dangerous than an enemy who remained unseen.

“The people are still taking the rumors with a grain of salt, but the other sects…”

“Still no replies?”

Wipeng lowered his head instead of answering.

Immediately after obtaining the information about Lee Seogeun’s poisoning, Jin Wikyung had sent requests for support to the other small and mid-sized sects in Shanxi. But it seemed every one of them had failed.

*This keeps getting worse.*

*Do I really need to run?*

I was looking out the window, thinking that, when—

Flap, flap.

A pigeon landed on the windowsill with the sound of beating wings.

“…It looks like a reply has arrived?”

* * *

The Jin Family of Taiyuan.

As the carriage approached the grand signboard written in magnificent calligraphy and the martial artists standing guard at the main gate with a stern aura, the coachman loosened the reins.

“Stop. State your identity and purpose!”

The gate guard called out loudly and blocked the carriage. Given the circumstances, there was tension in his voice.

More than that—

*This isn’t ordinary.*

The coachman holding the reins gave off the unmistakable air of a trained martial artist, while the four-horse carriage had both luxury and dignity.

*But why does he look familiar?*

The coachman, too. The carriage, too. Where had he seen them?

The question that had briefly arisen vanished the moment he saw the coachman’s sharp eyes. That aura, that gaze. This was certainly no ordinary visitor.

The gate guard swallowed and spoke again.

“Please state your identity and purpose.”

The carriage door opened, and a red silk slipper stepped lightly onto the ground.

Then a voice as gentle as a spring breeze drifted into the guard’s ear.

“I’m from Honghwaru. My name is a secret.”

Her face appeared along with her voice.

The gate guard’s eyes grew dazed. He wasn’t the only one. Everyone who saw the woman reacted the same way.

A vacant voice escaped the gate guard’s mouth.

“Ah, a secret… Then what brings you here?”

The woman, Wolhwa, answered with a charming smile.

“Hmm. I’m here to collect an unpaid tab?”

* * *

“How have you been? Didn’t you miss me?”

I froze halfway to standing.

A face I could never forget. And a face that had no business being here.

“Wolhwa?”

The first NPC I had met in this game. A courtesan at Honghwaru—and my, Jin Taekyung’s, little finger. That thing.

*Why is noona coming out of there…?*

“You remember me after all. Our Young Master Jin.”

Wolhwa giggled. She was beautiful, had a beautiful laugh, and when a beautiful woman laughed, she became even more beautiful…

*No, this is not the time for that.*

I whispered in a tightly restrained voice.

“What brings you here? No, never mind. Leave. Get out.”

I nudged Wolhwa with my elbow.

*This is driving me insane.*

Of all times, she had to show up in this atmosphere.

The entire family was under an emergency state of alert. If word got out that I had called for a courtesan, I couldn’t even imagine what would happen to my reputation. Just thinking about it made my vision swim.

“Don’t poke me. That tickles.”

“I know, so get out quickly. There are other people here. What are you trying to do by suddenly coming here? We’re expecting an important guest, too.”

The timing was damn awful, too. I was waiting for a guest from a sect called the Lower District Sect in the Lesser Family Head’s office.

Naturally, Jin Wikyung and Wipeng were there with me.

“Taekyung.”

Jin Wikyung called my name. Without even turning around, I hurriedly waved my hands.

“Ah, it’s not what you think. I didn’t call her. She’s leaving now, too. Right?”

Wolhwa’s laughter rose in pitch.

“Our Young Master Jin is still so adorable. But you guessed wrong. I came here because I have business to attend to.”

“Don’t call me ‘our Young Master Jin.’ I’m going to live chastely from today onward. I don’t have any business with you anymore, so get out quickly.”

“Hmm. No.”

Then there was no helping it. I would have to move her by force.

In desperation, I grabbed Wolhwa around the waist and hoisted her up—

“Huh?”

What the hell? Why won’t she lift?

Wolhwa looked slender, but was she so big-boned that she weighed a lot?

*That’s bullshit.*

What was my Strength stat again? With pure physical strength alone, I could grind a rock into powder. And yet I couldn’t lift one female NPC, which meant—

“Taekyung?”

I ignored Jin Wikyung’s second call and furtively let go. Then I heightened my Qi Sense.

“Ahahahahaha! This is driving me insane!”

As Wolhwa laughed herself to death, a Level Window appeared above her head. At the same time, I heard Jin Wikyung call my name for the third time.

> **System**
>
> **Lv. 50 Eun Sowol**

“Taekyung, greet her. She is the Branch Leader of the Lower District Sect’s Shanxi branch…”

Ah. Ahhh.

*I want to die.*

* * *

“Greetings. I am Wolhwa, Branch Leader of the Lower District Sect’s Shanxi branch.”

Eun Sowol.

No, for now, let’s just call her Wolhwa.

She was different from how she had acted until now. Every movement carried the grace and elegance of a noblewoman.

“I am Jin Wikyung of the Jin Family of Taiyuan.”

“I’m Wipeng.”

I kept my mouth shut like mute Samryong,[^1] and Wolhwa flashed me a grin.

It was an ominous grin.

*Don’t. Don’t smile.*

*Don’t talk to me. Please don’t.*

“It seems I haven’t been introduced to one person.”

Her gaze stung. Someone stepped on my foot beneath the table.

I opened my mouth with a feeling like I was coughing up blood.

“…I’m Jin Taekyung.”

“Yes. I hope we get along too, Young Master Jin.”

“Ahem.”

With a cough, Jin Wikyung glanced at me.

“I didn’t realize you were acquainted with my younger brother.”

“He is a regular at our establishment—the Honghwaru in Taiyuan. It also serves as this sect’s Shanxi branch.”

“Ah. A regular…”

I avoided everyone’s gaze. Wolhwa let out a burst of laughter, then brought up the real subject.

“Shall we talk business now?”

I had felt it several times before, but she really was a refreshingly direct woman. Jin Wikyung and Wipeng also turned their attention away from me and joined the conversation.

“First, allow me to offer my sincere thanks for the Lower District Sect’s assistance.”

“Think nothing of it.”

“But may I ask why you wish to help our family?”

Wolhwa smiled sweetly at Jin Wikyung’s question.

“The reason… I will tell you if necessary. First, we are doing this for our sect’s benefit.”

“Benefit. What specific compensation do you want?”

“Half of the shops and assets owned by the Mount Heng Sword Sect.”

“Good.”

“My lord!”

Wipeng hurriedly stepped forward, but Jin Wikyung paid him no heed.

Wolhwa also looked slightly surprised.

“You decide quickly.”

“Because I have staked everything the family has.”

“Has this already been agreed upon?”

“I am the Lesser Family Head, and with Father absent, I possess the authority of the acting Family Head.”

“I hear the internal opposition is quite fierce. The Elder Council, for example?”

“As expected of the Lower District Sect. Your information is fast.”

“It cannot be helped. Information is essential for survival in this bleak Murim. We need skills like these to make a living, don’t we?”

Watching Wolhwa smile, I suddenly had a thought.

*That information. Did I—or rather, did Jin Taekyung—let it slip?*

I had wondered where I had heard the name Lower District Sect before. It was an information-gathering sect that appeared regularly in martial-arts novels. In other words, Wolhwa, its Branch Leader, was a veteran information merchant.

On top of that, she was an outstanding martial artist at Level 50. A woman like that had disguised herself as a courtesan to meet a guy like Jin Taekyung?

*Even a dog would laugh at that.*

I stared at Wolhwa.

Her beauty was dazzling enough to make me wonder if a goddess had descended. Whenever she smiled, roses came to mind. Only now could I see the sharp thorns hidden beneath all that splendor.

Jin Wikyung spoke with a stiff expression.

“Then tell us the second reason.”

Wolhwa answered with her usual radiant smile.

“Because I like Young Master Jin.”

“Excuse me?”

“He’s young, handsome, well-built, and has such a cute personality.”

“…”

“…”

*How much of that was sincere, and how much was a joke?*

[^1]: Samryong is the mute protagonist of a well-known Korean short story; his name literally means “Three Dragons.”
