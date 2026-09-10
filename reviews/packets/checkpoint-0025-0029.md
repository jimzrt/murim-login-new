# Checkpoint Review — 25–29

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

# Chapters 25–29

## Plot

Gong Yacheong survives his fall and reunites with Socheon and Soyul. The **Survivors of the Sakju Branch** Quest completes, granting Taekyung EXP, Merit, Fame, and several level-ups before generating a Chain Quest. Gong identifies Jopil, One Question, One Kill, as the leader of the Sakju Branch massacre, and Socheon vows revenge. Taekyung promises to kill Jopil under the false name Hong Gil-dong, then tries to retreat after learning that Jopil is a Peak master. Hyuk Mujin exposes Taekyung’s identity to the survivors.

Jopil examines the massacre site, kills the Mount Heng overseers and guides, and deduces that an exceptionally skilled spearman killed Black Mountain Blade and the other pursuers. He tracks Taekyung’s group through the blizzard while Jin Wikyung sends Wipeng and more than twenty riders to find and protect Taekyung. The group struggles toward the main family as Gong’s poison worsens. Taekyung’s Main Quest still requires First Rate, Level 30, and Fame 500 for Logout; he has reached Level 24 with displayed progress of 24/30 and 250/500.

Gong asks Taekyung to return Socheon and Soyul alive, creating the no-reward **Gong Yacheong’s Last Request** Quest. Taekyung initially orders the squad to abandon Gong, but Han Yeop disobeys and carries him. Taekyung turns back after realizing that abandoning the seemingly fictional survivors is emotionally impossible. A secret Sound Transmission reveals that the Head Elder sent Jopil, expects Taekyung’s death to change Jin Wikyung’s mind, and intends to drive out the Lower District Sect afterward; the accomplice remains unidentified.

The System forces Taekyung to confront Jopil. Jopil admits he is employed for a mission, recognizes Taekyung as the Jin Family’s third Young Master and the Sleeping Dragon, and offers to release only Taekyung. Taekyung refuses to abandon Gong, Socheon, Soyul, or the reconnaissance squad. Jopil attacks, killing one unnamed squad member with a throwing knife and overwhelming Taekyung with Peak-level speed and strength. His Berserk effect magnifies his Strength and Agility but makes his attacks broad and imprecise. Taekyung’s cut triggers the effect, and he orders the squad to stay back to preserve his Gambler Title’s one-on-one bonus. Hyuk and Han Yeop ignore him and attack; Jopil shatters Hyuk’s sword, cuts the head from Han’s spear, and throws both into trees. Taekyung’s Sky-Piercing Strike fails, and Jopil repeatedly wounds him before preparing another killing blow.

## Continuity

- Gong Yacheong, Socheon, and Soyul are the three recognized survivors of the Sakju Branch massacre. Gong is poisoned by the pursuers’ weapon coating; fasting pills restore stamina but do not detoxify him.
- Taekyung accepted **Gong Yacheong’s Last Request**, promising to return Socheon and Soyul alive. The Quest has no reward.
- Taekyung used the alias Hong Gil-dong until Hyuk Mujin revealed that he is Jin Taekyung.
- Jopil, One Question, One Kill, is a Peak master employed to complete an unspecified mission. He leads roughly fifty wandering martial artists and tracks the group through the blizzard with the help of a subordinate who is Third Rate in martial arts but Peak-level in tracking.
- Jopil killed Black Mountain Blade, the other pursuers, and the Mount Heng overseers and guides. The identity of the highly skilled spearman Jopil inferred from the corpses remains unknown.
- Jin Wikyung sent Wipeng and more than twenty riders to locate and protect Taekyung.
- The reconnaissance squad is traveling toward the main family. One unnamed member is dead. Hyuk Mujin remains Taekyung’s injured deputy; Han Yeop remains the Level 13 spear user, though Jopil destroyed his spearhead.
- The Head Elder secretly sent Jopil and plans to exploit Taekyung’s death against Jin Wikyung before driving out the Lower District Sect. His Sound Transmission accomplice and their full plan remain unresolved.
- Taekyung’s forced System Quest against Jopil is limited to Taekyung, requires survival, and fails on death. Jopil’s Berserk effect has worn off by the end of the fight.
- Taekyung’s Gambler Title grants a 10% combat-stat increase only in a one-on-one fight. His Sky-Piercing Strike failed against Jopil’s defense.
- Taekyung, Hyuk Mujin, and Han Yeop are in immediate danger after Jopil’s final attack begins. The outcome remains unresolved.
- Logout still requires First Rate, Level 30, and Fame 500. Taekyung has not advanced to First Rate and still cannot move the unidentified energy in his dantian.
- Taekyung’s growing inability to abandon the survivors intensifies the unresolved conflict between his belief that NPCs are unreal and his experience that they feel real. The capsule’s purpose, route home, and Murim’s death and resurrection rules remain unresolved.

## Translation Decisions

- Preserve **Survivors of the Sakju Branch**, **Gong Yacheong’s Last Request**, and the forced Quest against Jopil as distinct System events.
- Keep Jopil’s epithet as **One Question, One Kill**, his Peak rank, and his recognition of Taekyung as the **Sleeping Dragon**.
- Preserve the Hong Gil-dong alias and briefly footnote the folk-hero and “Father”/“Brother” wordplay where needed.
- Retain **Sound Transmission**, **Gambler**, **Berserk**, **Sky-Piercing Strike**, **First Rate**, **Peak**, **Merit**, **Fame**, and **Logout** as established System or martial terminology.
- Preserve the contrast between wandering martial artists’ experience and ordinary martial artists, and keep Jopil’s tracking subordinate as Third Rate in martial arts but Peak-level in tracking.
- Keep the distinction between fasting pills that restore stamina and treatment that detoxifies poison.
- Preserve the dark action-comedy tone, including Taekyung’s Hong Gil-dong lie, his attempted retreat, the unnamed squad member’s death, and his conflicted attachment to NPCs.
- Footnote **Mount Beimang** as a burial mountain whose “hiking” idiom means dying, **goshiwon** as tiny inexpensive room-for-rent housing, and **junichi** as a fish-quality image if those references recur.

## Durable state

{
  "version": 1,
  "safe_through": 29,
  "continuity_sources": [28, 29],
  "active_continuity": [
    "Jin Taekyung is trapped in Murim through an old game capsule; death is presented as permanent and he cannot log out at will.",
    "Taekyung is the disgraced third son of the Jin Family of Taiyuan and narrates with dry, self-mocking, occasionally profane humor.",
    "Logout is the Main Quest reward for reaching First Rate, Lv. 30, and 500 Fame. Taekyung is Lv. 24 with progress 24/30 and 250/500; First Rate remains incomplete.",
    "Taekyung's Jin Family's Cultivation, Spear, and Manoeuvre Techniques are at the Fourth Stage; his Spear and Manoeuvre Techniques reached the Fifth Stage after training, and Third-Stage Qi Sense detects targets through Lv. 50.",
    "Taekyung has the Gambler Title, which increases combat stats by 10% in a one-on-one fight; it does not apply when allies join the fight.",
    "Taekyung's unidentified dantian energy is stronger than his ten years of internal energy, rejects contact, and remains immovable despite cultivation; training raised Sinews and Bones by 1 each while the Status Window still displayed ten years.",
    "Jin Wikyung is Taekyung's thirty-five-year-old eldest brother and the Lesser Family Head of the Jin Family of Taiyuan; Wipeng is his trusted guard. The Head Elder is Taekyung's great-uncle and the family's most senior elder.",
    "Jin Mukyung is twenty-five, the Heaven Shaking Sword, and a cadet at Heaven's Gate Temple.",
    "The Mount Heng Sword Sect and the Jin Family of Taiyuan are sworn enemies. Mount Heng has declared war, made Taekyung a public enemy, and triggered the Main Quest — War; fleeing incurs severe penalties. Wikyung sealed the family grounds against entry or exit without his seal.",
    "The Jin Family has roughly 200 martial artists, fewer than 20 First Rate masters outside the wider senior group, and three Peak masters; Mount Heng has at least 300 martial artists, more than 50 First Rate masters, and five Peak masters.",
    "The Lower District Sect's Shanxi branch, based at Honghwaru in Taiyuan, is led by Wolhwa, whose real identity is Eun Sowol, a Level 50 martial artist. Its wartime alliance with the Jin Family trades half of Mount Heng's shops and exclusive pleasure-district rights for exclusive Shanxi intelligence support.",
    "Yama Whip is a Peak whip master and Wolhwa's coachman. Taekyung encouraged the gate guards' mistaken belief that he helped Yama Whip defeat the Heavenly Axe, gaining 20 Fame as Poisoner rumors declined and Sleeping Dragon rumors gained credibility.",
    "Lee Cheonbaek, the Blood Wolf Sword and Sect Leader of Mount Heng, is Lee Seogeun's father. He expelled poison from his son's corpse, vowed revenge, and sent about two hundred armed martial artists toward the Jin Family.",
    "Lee Seogeun was Lv. 30 and was killed by an unidentified masked assassin using Sound Transmission, paralysis or toxin, and a blue-black needle; the killer remains unidentified.",
    "Taekyung leads White Tiger Hall's reconnaissance squad. Hyuk Mujin is its Level 22 deputy squad leader; Han Yeop is the Level 13 spear user. The group has nine sword users, one spear user, and no experienced shield user before Taekyung assigns three shields.",
    "Taekyung trained the squad with a two-hour travel and fifteen-minute rest cycle and drilled formation, dispersal, and all-out retreat. Hyuk mocked the retreat tactics and accused Taekyung of causing the war; Taekyung knocked him unconscious twice.",
    "A blizzard forced the squad into a hunter's shelter. Jopil's detachment massacred Jin Family survivors from the Sakju Branch near Jeongyang; fourteen-year-old Socheon and his younger sister Soyul escaped with Gong Yacheong, an old friend of their father.",
    "Taekyung defeated the Mount Heng pursuers and Level 32 Black Mountain Blade with Sky-Piercing Strike, completing the Survivors of the Sakju Branch Quest and triggering a Chain Quest. Socheon, Soyul, and Gong are the three recognized survivors.",
    "Gong Yacheong was poisoned by cheap toxin on the pursuers' weapons. Fasting pills restore stamina but do not detoxify him; he asked Taekyung to return Socheon and Soyul alive, creating the no-reward Gong Yacheong's Last Request Quest.",
    "Taekyung initially ordered the squad to leave Gong behind, but Han Yeop disobeyed and carried the unconscious man. Taekyung turned back after Soyul's reality made abandoning the NPCs unbearable.",
    "A secret Sound Transmission conversation revealed that the Head Elder sent Jopil and expects Taekyung's death to change Jin Wikyung's mind; the Head Elder also plans to drive out the Lower District Sect afterward. The accomplice and wider plan remain unknown.",
    "Jopil, One Question, One Kill, is a Peak master leading a special detachment of roughly fifty wandering martial artists. He killed Black Mountain Blade and the other pursuers, then tracked Taekyung's group through the blizzard; his subordinate has Third Rate martial arts and Peak-level tracking skill.",
    "Jopil admits he is employed to complete a mission. After truthful answers, he offered to release Taekyung alone and demanded that Gong, Socheon, Soyul, and the reconnaissance squad remain behind; Taekyung refused.",
    "Jopil's speed and strength decisively exceed Taekyung's and the earlier First Rate opponents. A forced System Quest against Jopil is limited to Taekyung and fails on death.",
    "Jopil's System Berserk effect increases Strength and Agility, making his attacks larger and less precise; it wore off during the fight in Chapter 29.",
    "One unnamed reconnaissance-squad member died from Jopil's throwing knives. Taekyung had trained him but could not remember his name, and the death made Taekyung angry enough to attack.",
    "Hyuk Mujin and Han Yeop attacked Jopil despite Taekyung's order to stay back. Jopil shattered Hyuk's sword, sliced the head from Han Yeop's spear, and blasted both into trees.",
    "Taekyung's Sky-Piercing Strike failed against Jopil's faster sword. Jopil cut Taekyung's chest, shoulder, knee, and side, then struck toward his chest again; the immediate outcome is unresolved.",
    "Mount Beimang is a burial mountain; going or hiking there is an idiom for dying. A goshiwon is a tiny, cheap room-for-rent housing arrangement.",
    "The capsule's purpose and route home remain unresolved.",
    "Murim death and resurrection limits remain unresolved."
  ],
  "open_questions": [
    "The capsule's purpose and the route home remain unresolved.",
    "The limits of Murim's death and resurrection rules remain unresolved.",
    "The identity of the Head Elder's Sound Transmission accomplice and the full purpose of their plan remain unresolved.",
    "The immediate outcome of Jopil's attack on Taekyung, Hyuk Mujin, and Han Yeop remains unresolved."
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
    "Use tone-marked pinyin for Chinese dialogue such as “Tài lěng le” and “Zhōngguó rén ma?”; keep “Shenme” unmarked in Chapter 2 because it supports Taekyung’s “Ms. Sunmi” mishearing joke."
  ]
}

## Reading copies

## Chapter artifact 25

# Chapter 25

“Is this the afterlife?”

That was the first thing the middle-aged man said when he woke up.

Before I could answer, something small sprang forward and threw itself into his arms.

The child, tears dangling from the corners of his eyes, shouted.

“Uncle Gong!”

“Socheon! You’re safe. But what in the world…?”

The confused middle-aged man listened as the child explained through sobs. When he heard that we had met on the hill and that all the enemies had died by my hand, his eyes widened.

“Are you from the main family?”

“Yes. That’s right.”

“Ah, Heaven has helped us!”

“…”

*I helped you, you old man.*

“I was sure I’d fallen to the bottom of the mountain… I thought that was the end of me.”

“You nearly did. You were lucky.”

I pointed below the ridge. Two corpses presumed to belong to the enemy lay with their heads buried in trees.

If the grass along the path where he had slipped had not been so thick, he would have ended up just like them.

*I didn’t realize it at first, either.*

I only became aware of the middle-aged man’s presence thanks to the Quest window.

Even after I defeated all the enemies, the **Survivors of the Sakju Branch** Quest had not been completed. That meant there were more survivors.

*The question was whether there were any survivors besides this man…*

The last trace of unease vanished the moment I helped the exhausted middle-aged man to his feet.

Ding.



> **System**
>
> - You completed the **Survivor** Quest!
> - A Chain Quest has been created!
> - You leveled up!
> - You leveled up!
> - Merit and Fame increase!



* * *

“Whew.”

The middle-aged man exhaled. Though he had only circulated his qi briefly, his complexion had improved noticeably.

He rose and respectfully clasped his hands in a salute.

“Benefactor, you saved everyone.”

“Not at all. I only did what anyone should have done.”

Every time I opened my mouth, lies came spilling out. It wasn’t entirely wrong, either. I had to clear the Quest somehow.

*If anything, I’m the one who should be bowing to them and thanking them.*

Still, Santa Claus—or rather, the survivors—seemed deeply moved by my attitude.

“Outstanding martial arts and a sense of chivalry, too. I, Gong Yacheong, sincerely admire you.”

“Socheon and Soyul owe Great Hero an enormous debt of gratitude.”

Thanks to that, I learned their names. The middle-aged man was Gong Yacheong, and the young siblings were Socheon and Soyul.

“If it isn’t too impertinent, may I ask our Benefactor’s name?”

“My name is…”

Then I had a thought.

*Wait. If I tell them my name, won’t they come running at me with swords?*

Whatever conspiracy had been involved, the person who had lit the fuse on this war was none other than me, Jin Taekyung. It was hard to believe that two people who had lost their home and family would look kindly on me.

*Yes. This is the moment for a well-intentioned lie.*

“Hong Gil-dong. My name is Hong Gil-dong.”[^1]

“Hong Gil-dong… I’ve never heard that name before. But I can feel the bearing of a hero.”

Socheon chimed in from the side.

“Here one moment, there the next. It sounds like the name of someone who appears and disappears like a ghost.”

*…How did that kid know?*

Before he could bring up the tale’s business about calling one’s father Father and one’s elder brother Brother,[^2] I hurriedly changed the subject.

“More importantly, what happened?”

Dark shadows fell across both their faces.

Gong Yacheong spoke first.

“It happened only a few days ago.”

By the time the carrier pigeon bearing word of war arrived, the Sakju Branch had already been surrounded so tightly that not even a drop of water could get through. The wandering martial artists hired by the Mount Heng Sword Sect had slaughtered people and burned down the buildings.

“There must have been a full hundred of them. Thanks to the Branch Leader and the martial artists under him buying us time, we were able to escape through a secret passage. Most of those who escaped were women and children who knew no martial arts.”

I didn’t need to ask what had happened to the others.

The System was absolute and factual. Those three were all the survivors of the Sakju Branch identified by the Quest Window.

“I want to know about the enemy.”

“They’re wandering martial artists.”

“Wandering martial artists?”

“As you know, they’re bastards who’ll do anything for money. The especially vile ones among them were hired by the Mount Heng Sword Sect to attack us.”

“They seemed pretty weak for such vile bastards.”

“Do good and evil determine who is strong and who is weak? The ones they hired this time were ordinary wandering martial artists, common as dirt. The leader was the problem.”

Gong Yacheong gritted his teeth.

“Jopil, One Question, One Kill. That was the man. The Branch Leader sensed defeat the moment he saw him and entrusted his family members to me.”

Socheon’s small fists trembled.

“I’ll tear him limb from limb and kill him with my own hands.”

That was an unusual choice of words for a child, but considering the grudge carved into his bones, it was understandable.

I gently patted Socheon on the head.

“That is exactly what will happen. I’ll help you.”

“Really?”

“A man’s word is worth a thousand pieces of gold. Do you think I’d say one thing and do another? I’ll definitely catch that bastard and level u—”

“Huh?”

“No, I mean I’ll kill him and avenge your grudge.”

“Ah… Thank you. Thank you so much, Great Hero Hong!”

“Thank you. Truly, thank you!”

The two of them repeatedly expressed their gratitude. I felt like a real scumbag, and a sharp stab tore through one corner of my chest.

*No. They’ll be happy when their enemy dies, and I’ll be happy when I level up. It’s mutually beneficial. Mutually beneficial.*

I forced myself to accept that justification and asked,

“How many of them are there?”

“While we were trying to determine the enemies’ position, I overheard them talking. They said there were about thirty, including Jopil.”

“Thirty? Thirty men?”

“That’s right. So we need to flee at once…”

Gong Yacheong’s voice began to fade. In its place, a faint sound from far away drew closer.

Ding. Ding. Ding.

I could hear it. The sound of leveling up. The sound of logging out!

Suppressing the corners of my mouth as they kept creeping upward, I said,

“Let’s wait here for the rest of them.”

“Wait? What do you mean?”

“Wipe them all out! We can’t let such vile bastards live!”

“No, Great Hero Hong, listen to me…”

“A master like you can do it! Thank you, Benefactor!”

Socheon came running into my arms with tears in his eyes. I opened both arms and pulled him into a hug.

“That’s right. Let’s kill them all!”

“Let’s kill them!”

“Jopil, you son of a bitch!”

“Son of a bitch!”

That was when Gong Yacheong spoke.

“Jopil is a Peak master.”

“Jopil is a fucking bast—huh?”

“Jopil, One Question, One Kill. He’s one of the few Peak masters in all of Shanxi. What do you think is the reason he has survived until now, despite being tangled up in all kinds of grudges and vendettas?”

“Don’t tell me…”

“Everyone who challenged him died. That’s the kind of man Jopil is. Cruel—and every bit as strong.”

“Ah.”

Sensing that something was wrong, Socheon looked up at me.

“Socheon.”

“Yes, Great Hero.”

“Now that I think about it, this probably isn’t the right time.”

“Huh?”

“I was being foolish. The priority should be getting you and your sister safely back to our family. Right?”

“…”

“I was injured during the fight earlier, too, and my men are exhausted. It looks like it would be a difficult battle.”

Socheon looked me up and down. My clothes were soaked in the enemies’ blood, but they were perfectly intact, without a single tear. There was no way I could have been injured.

“I have an internal injury.”

“…”

He turned to the reconnaissance squad. They had not even swung their swords once, and they were bursting with energy.

“What you see isn’t everything.”

“…Great Hero.”

I slipped Socheon off me and shouted,

“We’re returning to the main family. Everyone, prepare to leave!”

I hurried back toward the squad, but Socheon’s hand clutched my collar tightly and refused to let go. Tears glimmered in his round eyes.

“Great Hero.”

“Hey, why aren’t you moving? Move, move! Socheon, I’m a little busy right now, so let’s talk later. Okay?”

“Great Heeero.”

“Mister Gong Yacheong. No, Great Hero Gong, what are you doing? Every second counts.”

“…Socheon, come here.”

Gong Yacheong looked at me as if I were an idiot and pulled Socheon away. His hand came between me and Socheon like a guardian blocking a criminal.

Socheon almost wailed.

“Great Hero Hong Gil-dooong!”

And that was the starting gun.

With a thunderous boom, the cabin door was smashed apart, and someone burst in.



> **System**
>
> - **Level 22 Hyuk Mujin**



“Jin Taekyung, you fucking bastard!”

Hyuk Mujin huffed and puffed, his furious eyes locked on me. Gong Yacheong and Socheon stared at me with blank expressions.

“Great Hero Hong?”

“Great Hero Hong Gil-dong?”

“Ah. Well, you see…”

*…Fuck.*

[^1]: Hong Gil-dong is a legendary Korean outlaw and folk hero.

[^2]: In the Hong Gil-dong tale, he demands the right to address his father as “Father” and his elder brother as “Brother.”

* * *

“Hmm.”

Jopil stared down at the corpse. The face was twisted, its eyes wide open. Frozen beneath blood and snow, the man had been known by the nickname Black Mountain Blade.

“Tsk, tsk. How did you end up like this, friend?”

He had been loyal and clever. Jopil had never imagined he would die so pointlessly.

“See? Haven’t I always told you to walk around with both eyes wide open?”

Jopil grabbed Black Mountain Blade’s bulging eyes and pried them farther open.

A horrible sound escaped as the frozen flesh tore.

Rip. Riiip.

The others watched without even daring to breathe.

His expression and tone were no different from usual, but they could feel to their bones that Jopil was furious.

The killing intent radiating from a Peak master made it hard to breathe, and cold sweat trickled down their backs.

*It was understandable.*

More than twenty men had been wiped out. And all on a mission to deal with the remnants of the Sakju Branch.

Jopil, One Question, One Kill, was a bizarre man. Whenever he encountered an enemy he liked, he asked exactly one question before killing them.

The wandering martial artists thought it was fortunate that Black Mountain Blade was dead. If he had still been alive, they would have suffered something even more horrifying.

“That’s better.”

Jopil wiped the blood on his trousers and rose.

“Well, what does everyone think? Tell me without holding back.”

“We should obviously follow the order.”

One man stepped forward. The neatly dressed, dignified middle-aged man and the ten-odd martial artists standing at attention behind him were the overseers and guides the Mount Heng Sword Sect had sent to keep the wandering martial artists under control.

Jopil smiled faintly.

“Ah, yes. I’d forgotten our Mount Heng Sword Sect Hall Master was here. But what’s this about an order?”

“Wipe out the Sakju Branch and join the main force. Have you already forgotten the Young Sect Leader’s order?”

“An order? I remember accepting a commission.”

“Isn’t that the same thing?”

The middle-aged man glared at Jopil, displeased.

“Coming here in the first place was your own arbitrary decision. And what came of it? You lost more than twenty subordinates to the remnants of a single branch!”

“Then we should pursue them. We can finish them off in half a day.”

“Jeongyang might be another matter, but if you pursue them as far as Honju, we risk a counterattack. I won’t permit any more unilateral decisions.”

“Permission. Permission…”

After mulling it over, Jopil spoke.

“No. That won’t do. I don’t like it.”

“What do you mea—”

Crunch.

The middle-aged man’s neck shattered, and he died before he could finish speaking. Jopil had twisted it at blinding speed. He licked his lips.

“I like war. No matter who dies, people forget.”

“You bastard!”

The Mount Heng Sword Sect’s martial artists realized what had happened and drew their weapons, but Jopil had already plunged into their midst.

Crunch. Slash!

Warm blood poured onto the snowfield. Every time Jopil rampaged like a wild beast, someone’s neck, arm, or leg was torn free and sent flying.

“Gaaah…”

The groan of an unnamed martial artist was the last sound.

Standing atop the heap of corpses, Jopil spoke into the crushing silence.

“We’re pursuing them.”

This time, no one said a word. As his subordinates hurried to prepare as though fleeing for their lives, Jopil continued to stare at the bodies.

*What kind of man was it?*

Jopil was a Peak master. From the scars on the corpses and the footprints, he could picture what his opponent looked like.

*Only one man.*

A highly skilled spearman had been here. He was the one who had slaughtered the other twenty-plus men.

*If he killed Black Mountain Blade in one strike, he must be something else.*

The final strike that pierced through Black Mountain Blade’s chest had been particularly interesting.

*This should be a fun fight.*

Who was he? A master from the Jin Family of Taiyuan? Or someone unknown?

It didn’t matter. Jopil let out a pleased laugh.

“Let’s meet soon, friend.”

* * *

“What news have we received?”

“None, sir. All we can do is move as quickly as possible…”

“Damn it! Damn it!”

Wipeng was furious. But there was nothing he could do. As his subordinate had said, the only thing they could do was find the Third Young Master and protect him.

*Jopil, One Question, One Kill…*

Wipeng knew the man’s reputation well. If the Third Young Master fell into his hands, death would be the only possible outcome.

*If that happens, I won’t be able to face my lord.*

Jin Wikyung endured with superhuman patience.

He was currently at the head of the Jin Family of Taiyuan, its central pillar. He had placed his beloved younger brother and hundreds of family members on the scales, and after much deliberation, he had sent his most trusted subordinate, Wipeng, to his brother.

*But if I fail…*

*I won’t be able to face my lord.*

Wipeng’s grip tightened on the reins. He spurred his horse onward. More than twenty mounted riders followed in a long line behind him.
## Chapter artifact 26

# Chapter 26

“So…”

Gong Yacheong looked at me with a strange expression.

“So you are that Young Master Jin Taekyung.”

The moment had finally come. I let go of Hyuk Mujin’s collar—he’d passed out for the third time—and smiled awkwardly.

“Yes. I’m Jin Taekyung.”

The reconnaissance squad members preparing camp pricked up their ears. We were on our way back to the main family.

We had ridden for more than five hours without a break since leaving the cabin where the fight had taken place. Gong Yacheong had kept his mouth shut the entire way. Only now did he speak.

*If it weren’t for that bastard.*

I glared at Hyuk Mujin, who was being dragged along by one of the quicker-witted squad members. I should have hit him one more time before letting go.

As I was still regretting that, Gong Yacheong spoke.

“I’ve heard plenty about you, Young Master.”

“…I see.”

“Even a three-year-old knows who you are. You must be the main family’s biggest celebrity.”

At this point, it would have been faster to find someone who didn’t know me.

“You’re lazy by nature and arrogant beyond belief. You’re lost in wine and women and don’t even practice martial arts… But I see the rumors of the martial world aren’t worth believing after all. The martial prowess you displayed today was truly remarkable.”

“…”

If there were some kind of Martial World Daily that collected every rumor in the martial world, I’d subscribe immediately. It was surprisingly credible.

*More importantly…*

Did Gong Yacheong really not know?

Whatever bullshit the Mount Heng Sword Sect had pulled, I was at the center of this entire mess.

It was an undeniable fact that countless people had died along the way.

It wouldn’t have been strange if Gong Yacheong and Socheon held a grudge against me. That was why I had hidden my name.

*If he really doesn’t know, that’s a relief.*

We were being chased by a ruthless Peak master. I had no interest in stirring up extra trouble.

“How long until we reach the main family?”

Gong Yacheong’s question snapped me back.

“We should arrive in two or three days.”

“Of all times, it had to snow now…”

Gong Yacheong lamented. He glared resentfully at the sky, still dumping snow.

“Young Master, we should prepare for the worst.”

“The worst?”

The blizzard had us stuck, but it had our enemies stuck too. There was even a chance they had given up the chase.

Gong Yacheong shook his head.

“Don’t underestimate wandering martial artists. The purity of their internal energy and the martial arts they’ve learned may not amount to much, but their greatest weapon is something else.”

I gave him the answer.

“Experience.”

“Exactly. The experience gained from fighting a hundred battles. What’s chasing us isn’t martial artists. It’s wandering martial artists. Similar, but entirely different creatures.”

Similar, but different. I thought I understood what he meant.

In short, they were well-trained hunting dogs. And the man holding their leash was Jopil, One Question, One Kill.

“The reason Jopil is truly frightening isn’t simply because he’s a Peak master. It’s his persistence. His viciousness. He has never once failed a commission or allowed a target to escape.”

I answered with a sigh.

“It’ll be the same this time, then.”

“Probably.”

Gong Yacheong stared into the darkness ahead, as though something might leap out and swallow us whole.

“We’re being chased by a man like that.”

Whoosh. The snow-filled wind faded into the darkness.

* * *

We finished making camp. We had dug several small dugouts and blocked their mouths with branches, fallen leaves, and whatever else we could find. It was crude, but this was no time to be choosy.

“Have a comfortable night.”

Gong Yacheong had already vanished, carrying the sleeping siblings in his arms. I kept thinking of the exhausted smile at the corner of his mouth.

*He really is an adult.*

If he had wanted to live, he could have run away long ago. Gong Yacheong was a trained master, a seasoned man of the martial world.

But he hadn’t.

He had risked his life fighting for two children who didn’t share a drop of his blood.

That was why Gong Yacheong was a good adult.

*Could I have done the same?*

I shook the question off as soon as it came up. This was a game. It wasn’t good to think too deeply about an illusion that would soon disappear.

That was right. An illusion that would soon disappear.

*Open Quest Window.*

Ding.

> **System**
>
> **Logout**
>
> You must now make your way through this harsh Murim.
>
> Become stronger. Become famous.
>
> For the day that will come someday…
>
> **Grade:** Main Quest
>
> **Limit:** Jin Taekyung
>
> **Task:** Reach the First Rate realm — Incomplete  
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reach Lv. 30 — 24/30  
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reach Fame 500 — 250/500
>
> **Reward:** **Logout**

The EXP and Fame I had received for dealing with the enemies. The Quest reward on top of that.

I was starting to see the summit of this treacherous mountain.

I opened my Status Window and distributed all my remaining points. Vitality flowed back into my exhausted body.

*I’m almost there.*

I only had to get past this hurdle. If I could avoid that bastard Jopil, One Question, One Kill—the man whose face I didn’t even know—I could finally put an end to this miserable journey.

But there was another problem.

*Let’s say I can somehow fill up my Level and Fame. How am I supposed to raise this damn realm?*

Back when I first started clearing the tutorial Quests, I had raised my realm from Third Rate to Second Rate by distributing my stats. After that, radio silence.

*What the hell am I missing?*

I was an absurdity in Murim. I could learn martial arts and raise my stats faster than anyone else. I had grown stronger with the System’s help in all kinds of ways.

That was why I could literally wipe the floor with ordinary First Rate martial artists despite being a dime-a-dozen Second Rate.

And yet I wasn’t First Rate!

*I should’ve asked Jin Wikyung.*

At first, I thought I just needed to keep raising my stats or internal energy. Lately, though, I had started to feel I was barking up the wrong tree.

*Level? Stats? Internal energy?*

What was it? The last piece needed to finish this puzzle?

The answer came quickly.

*If I don’t know, I have to find out.*

Just like I had until now. If I kept walking, I would find an exit.

I sat cross-legged and regulated my breathing. The internal energy coiled in my dantian answered my call.

* * *

“We lost them.”

Jopil muttered. His black, viper-like eyes swept the surroundings.

They had lost the fugitives. But traces remained. Those faint traces would become new signposts.

“About twenty people. They left this place roughly two shichen ago.”[^1]

Jopil nodded at his subordinate’s report. The man’s martial arts were only Third Rate, but his tracking skills were Peak. Jopil had countless hunting dogs like that under his command.

*Two shichen.*

The gap was already down to two shichen. How long would it take to catch the fugitives?

Half a day at most.

*They should have run with everything they had. Without looking back. They should have thrown off every burden, abandoned any stragglers, and kept running for their lives.*

If they had done that, the distance would not have narrowed. But they had let their guard down. They must have thought the blizzard had them trapped.

That difference had created the current situation.

*But I’m a little different.*

The previous night had been long. Even among his pursuit-hardened subordinates, there had been stragglers.

In the mountains during a blizzard, falling behind was as good as dying.

The only difference from dying on a battlefield was that it took a little longer.

That was why Jopil had given the order.

*Kill them.*

They said that when a tiger died, it left its hide, and a person left a name.

But Jopil thought differently. What kind of name could a Third Rate nobody who’d spent his whole life drifting through back alleys leave behind?

They should at least leave a hide.

Leaving twenty stripped corpses behind, they continued onward. After the long night ended, they found the fugitives’ traces just before dawn.

*We’ll be meeting soon, friend.*

The corners of Jopil’s mouth lifted. A mysterious master—the first in a long while to catch his interest.

His long-stiff heart began to pound.

* * *

I shuddered.

“Ugh. What the hell?”

A chill had run through me. I lifted my arm and found it covered in goose bumps.

If this were a scene in a novel, the protagonist would have muttered, *Something feels off,* and gone on his way.

But I was different. I had a solid hunch, and I acted on it.

“Hey. Get over here, quick.”

I couldn’t see him, but I could feel it. Someone trudging behind me faltered.

“W-why?”

“I’m counting to three. One, two. Three.”

The instant I hit three, Hyuk Mujin hurried over and pressed himself against my side.

“It was you, wasn’t it?”

“What?”

“You were the one. Tell me the truth and I’ll let it slide.”

“What? I didn’t do anything!”

I silently stared at his face, swollen like a steamed bun.

“You were cursing me behind my back just now, weren’t you?”

“Hah.”

“You were cursing me, right?”

“I-I was…”

So it really had been this bastard. When I raised my hand, Hyuk Mujin squeezed his eyes shut.

After getting beaten about three times, he had lost all his fighting spirit. On top of that, he had learned a valuable life lesson:

Dodging only meant getting hit more.

“Fine. Since you told the truth, I’ll let it go this once.”

Hyuk Mujin jerked his head up.

“Really?”

I gave him a warm smile.

“Of course. But don’t even think about deceiving me from now on. I’ll be watching you with mind-reading.”

Hyuk Mujin glared at me like he wanted to kill me, then bolted back to his place. If I’d had enough time, I would have crushed his head with a mace.

Swallowing my regret, I kept walking.

“What’s mind-reading?”

The chatter tickled my ears. It belonged to Soyul, Socheon’s little sister. Was she five years old?

She was small enough to fit right inside my backpack.

“Is it martial arts?”

“Something like that.”

“Is mind-reading strong?”

“Very.”

“Wow! Soyul wants to learn mind-reading, too!”

“But you have to be one-eyed.”

“Gasp!”

I glanced over and saw Soyul staring at me, startled. Her eyes had gone huge. Ridiculously cute.

*Hayeon used to be like that, too.*

These days she was a creepy little sister, but when she was little she had been a baby angel. She had even gotten offers to be a child model…

Having her around felt exactly like piggybacking Hayeon at that age.

“Do you want me to teach you?”

“…Soyul doesn’t like martial arts. I want to become a proper young lady.”

“That’s fine, too.”

“Mm. Mister, do you like martial arts?”

“Me?”

“My brother says you’re really strong. Dad said only people who work hard can become strong.”

“Your dad said that?”

“Yes. My dad is really strong, too. Because…”

She chattered excitedly for a while, then stuck out her lower lip.

“Soyul wants to see Dad. But I guess Dad doesn’t want to see us. Oppa says he went out to play with Mom, leaving me and Oppa behind.”

My heart dropped with a thud.

An old memory filled my vision. In a funeral hall of black and white, little Hayeon had searched for our father, and I had no choice but to tell her an obvious lie.

Just as Socheon had done for Soyul.

It was the only thing I could say.

“…I see.”

What else could I say?

I looked at Socheon, following along in the middle of the formation. He was panting, soaked in sweat.

*He must be exhausted.*

His willpower was far beyond his years. The saying that pain made people mature was fucking bullshit, but it was true.

Socheon had never fallen behind even once, and the other reconnaissance squad members marveled at him for it.

*But the real problem is somewhere else.*

Gong Yacheong.

His face was deathly pale; he still hadn’t shaken off his injuries. If not for the remarkable effects of the fasting pills I had given him, and the qi he had circulated last night, he might have collapsed long ago.

*At this rate, we’ll be caught.*

Even after the sun rose, the packed snow wouldn’t melt. I was out front, clearing a path through it, but everyone was exhausted, and our pace had slowed.

On top of that, we had an injured man and children.

*Should I run away by myself?*

The thought came in an instant.

It was a game. So what?

Gong Yacheong, those two kids, the whole reconnaissance squad—every last one of them was created AI. Just NPCs.

But what about me?

I was alive. Among all of them, I was the only one who was real. The only one with a real body.

But…

*Fuck. It’s a simple problem… Why am I like this?*

An inexplicable aversion surged up. It was strong enough to startle me—strong enough to throw me off.

*Why?*

I didn’t know.

I didn’t find the answer for hours after that, and then night came.

[^1]: A shichen is a traditional time period of roughly two hours.
## Chapter artifact 27

# Chapter 27

“Fifteen-minute break.”

The reconnaissance squad members dropped to the ground with a sound like the air going out of them.

They looked exhausted, but I wasn’t particularly worried about those guys. As I’d observed, they had solid basic stamina, and during the battle they had done nothing but stand around and watch.

The other two were the problem…

“Are you all right?”

“Huff. I’m fine. I’m fine.”

Socheon answered while breathing heavily. He didn’t look like he was about to collapse just yet. But if he kept traveling like this, he would hit his limit before long.

*He’s a stubborn little brat.*

Earlier, I had offered to carry him and his sister. He had refused without hesitation.

“If you’re having trouble, tell me. I can handle carrying both of you.”

“Huff. I’m fine like this. It’s enough.”

*Doesn’t look like it.*

“I’m saying this for everyone’s sake. Don’t answer so quickly.”

“Understood.”

His eyes hardened as he answered. I placed the peacefully sleeping Soyul in his arms and turned around.

“Great Hero Gong.”

The pale-faced man raised his head.

“…Young Master Jin.”

His voice sounded like it might give out at any moment. His condition was worse than I’d expected. The question *Are you all right?* lingered on the tip of my tongue before fading away.

“How long can you hold out?”

“I don’t know.”

His answer was honest—and serious.

“What about the fasting pills?”

I had given him several of the fasting pills I had left. But Gong Yacheong shook his head.

“They’re not very effective. Some quack must have made them. They’ve done nothing but ruin my appetite. Hahaha.”

“…Are you telling me that to make me laugh?”

“Wasn’t it funny?”

“No. Not at all.”

“That’s a shame… Cough!”

A sudden cough.

Drops of blood fell onto the white snow.

*Damn it.*

Worried that someone might see, I hurriedly stepped in front of Gong Yacheong.

“What happened? You weren’t this bad before.”

His condition had deteriorated rapidly in half a day. Gong Yacheong no longer looked merely exhausted. He unmistakably looked like a sick man.

“It was inevitable.”

The calm look in his eyes made it even more ominous. I brushed aside the hand trying to stop me and pulled up the front of his robe.

“Ah.”

His body was covered in all kinds of wounds. But what shocked me were the blue veins spreading outward from his lower abdomen.

“What is this…? Don’t tell me…”

Gong Yacheong weakly fastened his robe again. He seemed worried that someone else—especially Socheon and Soyul—might see.

“Those wolf-like bastards coated their weapons with poison.”

Now I understood why Gong Yacheong hadn’t recovered even after taking the fasting pills. They could only stave off hunger and restore stamina. They had no detoxifying effect whatsoever.

“You should have told me sooner!”

“Those bastards must have been short on money. They used cheap poison. Its potency was weak, so I didn’t notice until last night. By then, it was too late.”

Gong Yacheong’s stamina had already been at rock bottom when he was poisoned. Then he had continued forcing himself through this weather…

“Isn’t there anything we can do?”

“There is.”

“Tell me.”

“But time won’t allow it. I can’t waste such precious time on one person.”

He was right.

But still…

“We have to try.”

“Young Master.”

“Everyone is exhausted. If we rest for one shichen[^1]—no, just half a shichen—and try the method, that should be enough.”

“Hahaha.”

“Please don’t laugh. I was planning to stop and rest around here anyway…”

I didn’t know what I was saying anymore. As Gong Yacheong watched me ramble, a faint smile appeared at the corner of his mouth.

“Go.”

“…”

“You know it too, don’t you? If we waste time here, we’ll be held back.”

I fell silent.

He was right. I had been considering this possibility since I saw his precarious complexion and the blood he coughed up. Perhaps I had been thinking about it since last night.

*So this is how it ends?*

I had to leave Gong Yacheong behind. If I took him with us, he might survive for now, but everyone’s pace would slow down.

What if I carried him myself?

Even with the System’s help, I was still human. I had spent two days walking at the front and clearing a path. Fatigue had piled up with it.

*Two fasting pills left.*

Even the thirty fasting pills I’d had were almost gone. Could I escape those bastards while carrying Gong Yacheong with only two pills remaining?

And if we still ended up running into them, would I be able to fight them while exhausted? Would I be able to face Jopil, One Question, One Kill, a Peak master?

The answer had been clear for a long time.

We both knew it.

“Please take care of the children.”

The moment Gong Yacheong spoke, the System notification rang.

Ding.

> **System**
>
> **Quest**
>
> **Gong Yacheong’s Last Request**
>
> He wants only one thing now. See that the surviving children make it back safely.
>
> **Grade:** None
>
> **Limit:** Jin Taekyung
>
> **Task:** Socheon and Soyul’s safe return (Incomplete)
>
> **Reward:** None
>
> - Would you like to accept the Quest?

There was no reward.

It was the most shameless Quest I had ever received.

*I’m busy trying to stay alive myself, old man.*

But I nodded.

If accepting it could ease even a little of the guilt sitting in the corner of my heart, I was willing to do it.

“Let’s do that.”

Gong Yacheong smiled with satisfaction.



* * *

“You’re saying we’re leaving Great Hero Gong behind?”

Han Yeop muttered with a shocked expression. Hyuk Mujin said nothing, as though he was lost in thought, while the other reconnaissance squad members were busy watching one another’s faces.

“Yes.”

“That makes no sense!”

“Lower your voice.”

There was nothing to gain from Socheon finding out. That was especially true because he would insist on staying behind with Gong Yacheong.

“B-but this…”

“It was Great Hero Gong’s decision. I agree with him.”

That was when Hyuk Mujin suddenly spoke.

“What’s the reason?”

*Has this bastard not been beaten enough?*

I glared at him, but Hyuk Mujin neither flinched nor backed down. My fist, which had tightened instinctively, slowly relaxed.

“His condition is serious. If we continue like this, he’ll put all of us in danger.”

“Is that all?”

“Yes.”

Han Yeop cut in, his face flushed.

“No.”

“It’s an order.”

“Then I’ll disobey.”

Everyone stared at Han Yeop in surprise.

I hadn’t expected the boy who had declared himself my ardent follower from the very first time we met to use the word *disobey*, either.

“Nothing will change just because you say that.”

“We can’t leave him like this.”

“If we can’t leave him behind, then what?”

Fatigue suddenly swept over me. I rubbed at the corners of my stiff eyes.

“I’ll carry him.”

“Yes. I’ll carry him.”

“And you’ll get tired soon.”

If Han Yeop got tired, someone else would step forward to help him. Then they would grow tired one by one, our pace would slow, and the enemy would catch up.

“Our opponents are a pack of battle-hardened wandering martial artists led by a Peak master. Do you think we can survive?”

Han Yeop lowered his head without answering. The other members of the reconnaissance squad avoided my gaze as well.

Only one person continued to meet my eyes.

“Number One. Do you still have something to say?”

Hyuk Mujin had been silent for a long time. He finally bowed his head.

“I’ll follow your orders, Squad Leader.”



* * *

We began moving again.

Just before we left, Gong Yacheong gently stroked Socheon and Soyul’s heads with a peaceful expression.

“I’ll see you soon.”

Socheon nodded bravely. Soyul, still half-asleep, whimpered and nestled into my arms.

Every time I heard her shallow, wheezing breaths, a pang of unease tightened in my chest.

*Has he left by now?*

Gong Yacheong hadn’t wanted the children to know he was gone. That was why he had told me he would quietly slip away along the way.

Socheon was in the middle of the formation, so the reconnaissance squad members would block his view. He wouldn’t be able to see Gong Yacheong leave.

*How long has it been since we left?*

A sikyeong? Half a shichen?

I didn’t know. In the dead of night, with darkness swallowing everything around us, I couldn’t even feel time passing.

With every step I took, one thought refused to leave my mind.

*He must have left by now.*

It was only natural. Gong Yacheong and I knew it, and everyone in the reconnaissance squad except Han Yeop had accepted it.

Most importantly…

I had a family waiting for me. The real world was waiting for me outside.

*Then why does this feel so damn awful?*

My feet felt heavy.

It wasn’t just because snow had piled up to my calves. It wasn’t because grass and branches blocked the path ahead.

It was because a mere NPC named Gong Yacheong kept weighing on my mind.

I thought about his final smile. I thought about the cheap Quest with no reward.

I thought about Han Yeop’s defiance. Hyuk Mujin’s calm gaze pricked my chest like a thorn.

*It’s only natural. So why?*

Because it was a game.

Because it was only a game.

*If I didn’t leave him behind, everyone would die. I’d die, too! You fucking bastards!*

“Fuuuck…”

The profanity that had been caught in my throat spilled out.

Soyul stirred from her light sleep and mumbled something as she wrapped her arms around my neck.

Her tiny hands were cold. They felt so real that goose bumps rose across my skin. Too real to believe this was a game.

Real enough that I felt guilty over abandoning a single NPC.

“…What a fucked-up game.”

I turned around.

“Where are you going?”

I strode back the way we had come. I couldn’t see Socheon’s face or the faces of the reconnaissance squad members.

That was why I didn’t notice the fleeting smile that crossed Hyuk Mujin’s face when he asked where I was going.

I also didn’t notice that Han Yeop, who should have been at the very rear, was no longer there.

“Huff. Huuuff.”

I sprinted across the snow like the wind.

And then I found him.

Below the hill, Han Yeop was gritting his teeth and forcing one foot in front of the other despite gasping for breath.

Gong Yacheong, unconscious, was on his back.

“You…”

I didn’t know what to say. With a sigh, I grabbed Han Yeop’s hand and pulled him up.

“Th-thank you.”

*Shit.*

*I don’t know anymore, either.*



* * *

This was a hidden retreat reserved for one person.

After becoming its owner thirty years ago, he had barred everyone else from entering. Over time, that had hardened into an unbreakable rule, and the others thought of it the same way.

“How are things going?”

As the air trembled faintly, the two shadows conversed through Sound Transmission.

“Smoothly. And you?”

“There’s no need to ask.”

“I wouldn’t expect otherwise.”

“The Blood Wolf Sword. He’s surprisingly fond of his family for someone with that epithet.”

“A wolf can still love its own blood. So?”

“The vanguard alone numbers two hundred. A madman named Jopil is running wild as he pleases, but… it should be fine.”

“Jopil, One Question, One Kill? The Blood Wolf Sword chose well.”

“The wastrel young master is being chased for his life. It wasn’t part of the plan, but it isn’t bad, either.”

“Hahahaha.”

“Could it be…?”

“That’s right. I sent him. When the Lesser Family Head sees the head of his beloved youngest brother, he’ll change his mind.”

“Whew. A heart as cold as poison, without blood or tears. Impressive.”

“Is that something you should be saying?”

“I only took one hopeless life.”

“And thanks to that, a bloody storm will sweep across Shanxi?”

“Isn’t that what you wanted?”

“I can’t deny it. Yes. I’ve waited too long.”

“The fruit will be all the sweeter.”

“I hope so.”

“Ah, yes. The Lower District Sect has gotten involved.”

“The Lower District Sect? How did they?”

“The new Branch Leader has a good nose. Once this matter is finished, I plan to drive them out.”

“Be careful. No matter how formidable Heaven may be, one must never let one’s guard down…”

At that moment, the wind stopped.

The air trembled.

“…I misspoke.”

It was a long while before another message came through Sound Transmission.

“It would be wise to watch your words and actions.”

The voice was soft as a cat’s paw.

But the listener could feel the razor-sharp blade hidden beneath it.

“Let me apologize once more.”

“Let’s end things here for today. If a problem arises, I’ll come see you again soon.”

The conversation ended there.

The other person vanished without a sound or trace.

*They were like ghosts.*

Sometimes, he wondered what their true identities were. How strong were they? Who were their members?

But he soon shook his head.

*That would only shorten my life.*

He had endured years of hardship to reap the fruit. He couldn’t let mere curiosity ruin his plans.

*It truly has been a long time.*

The shadow reached a hand toward the moon. Faint moonlight slipping between his fingers illuminated a silver beard.

*Soon… everything will fall into place.*

The Head Elder smiled with delight.

[^1]: A shichen is a traditional time period of roughly two hours; a sikyeong is a shorter traditional interval.
## Chapter artifact 28

# Chapter 28

*Hoo.*

I sat cross-legged and evened out my breathing. The breath I exhaled still carried qi I hadn’t managed to draw back in.

*What a waste.*

Circulating qi meant drawing in energy from outside, cycling it together with my internal energy, and accumulating it. But only a small amount stayed in my body.

Most of it returned to nature.

*In novels, you could shoot up just by doing a little of this.*

The greatest martial arts under heaven? An elixir of the ages?

Not here. The Jin Family’s Cultivation Technique was Peak-grade, but it was hopeless at accumulating internal energy. And elixirs? Bullshit. I hadn’t even gotten a look at one. All I’d done was suffer like hell.

*Is that my only hope?*

Another mass of internal energy crouched in a corner of my dantian. If I could make all of it mine, it would be a huge help in the fights ahead.

The problem was that no matter how many times I tried, it wouldn’t budge.

*Move. Move!*

As if the thing that had sat there like a boulder this whole time was going to start moving. I tried drawing up my internal energy, but it gave me nothing. I sighed and got to my feet.

“Are we departing?”

Hyuk Mujin had been watching our surroundings.

“Yeah.”

“Understood.”

Then he briskly got the reconnaissance squad ready and scooped Soyul into his arms. I was left staring.

*What the hell did this bastard eat?*

Why had he suddenly gotten so sharp?

This was the guy who used to move only when I shoved a fist in his face. Somehow he seemed like a different person.

*Not that I’m complaining.*

I shoved the stray thoughts aside and slung Gong Yacheong onto my back. As the poisoning worsened, his face had gone dark blue.

Hyuk Mujin asked, worried, “Will he be all right?”

“He has to be.”

I’d already done everything I could. All I could do was hope Gong Yacheong held on. I muttered toward the unconscious man.

“Not much farther. Just hold on a little longer.”

Sunlight squeezed through the dim dawn. I took a long stride toward it.

No—I started to.

- Awoooooo!

At first I thought it was the wind. But those were the cries of living beasts. Hyuk Mujin muttered,

“The wolves must be hungry.”

“Wolves?”

“Of course. It’s hardly strange for there to be wild animals in the mountains.”

This was a game set in ancient China. Wolves, tigers—nothing jumping out would be strange. I’d heard wild animals crying more than once over the past few days.

But…

*Something feels off.*

This wasn’t like the ones before. Just hearing those howls made my chest tight and my fingertips tingle.

The gut I’d honed over seven years seemed to whisper. Something was beyond that forest, where the sunlight hadn’t reached yet.

“Prepare for battle.”

“Then we’re leaving now… Huh?”

“Form a defensive formation.”

Hyuk Mujin snapped out of it and passed on the order. Three reconnaissance squad members with thin-iron-plated shields blocked the snow-covered path.

A narrow trail, high ground on a hill. Advantageous position.

- Awoooooo!

A second howl. Closer—and more ominous for it. Hyuk Mujin spoke carefully.

“They appear to be nothing more than a wolf pack…”

“Then that’s even better.”

“Won’t this delay us too long?”

I shook my head. We’d been running for two full days. If this brief pause was what got us caught, that was fate.

“Hold. We wait a little longer.”

The beasts seemed to take me at my word. For several minutes the howls never stopped, and they kept getting closer. In the snow-covered mountains at dawn, snapping branches and paws racing over snow made a racket.

“Doesn’t sound like one or two.”

Hyuk Mujin glanced at my face.

“From the sound, there must be dozens… Wolves are pack animals, but this is strange.”

No sooner had he finished than the pack showed itself. Maybe they hadn’t found prey in winter; most of them were nothing but ribs. But they were still predators. We couldn’t let our guard down.

*Hungry predators, at that. The kids could get hurt.*

And yet, oddly, I felt relieved. The place was crawling with martial artists, but it wasn’t as if the beasts had learned martial arts too.

Forget gut feelings—these were easy opponents.

*I skip a few raids and my touch is completely gone.*

I clicked my tongue and stepped forward. The dozens of wolves charging at us already looked like chunks of EXP.

“Let’s wrap this up. Yeah?”

I crooked a finger at the wolf running point in the distance. Judging by the size, that one was the leader.

- Grrrraaaah!

Since when did a wolf roar like a lion? Don’t tell me it was some kind of spirit beast? Was I seriously going to lose to an animal?

*Not happening.*

I swallowed and brought my spear up. I couldn’t afford to lose a clash of qi, so I glared hard and dropped my voice.

“Come.”

The effect was incredible!

- Grrrrr…

The charging wolf suddenly veered off and plunged into the forest. Its dozens of subordinate wolves poured after it.

No—that was a retreat. A cold wind swept over the countless pawprints stamped into the snow.

*What the hell.*

They came running like they were going to eat me alive. Why run?

Then a famous comic popped into my head. The one about a rubber man with hyperactivity disorder smashing the maritime authorities.

“D-don’t tell me it’s that?”

That ability that could scare enemies senseless—knock them out, even—with qi alone.

This game was insane enough that it was entirely possible. In which case the System ought to ping me right about now…

Ding.

There it was! I waited for the System voice, buzzing with anticipation.

I ignored the reconnaissance squad’s bizarre faces and muttered without stopping.

“Come on, come on, come on!”

It appeared.

The Quest Window.

> **System**
>
> A Quest has been created.
>
> **Quest**
>
> **Jopil, One Question, One Kill**
>
> The relentless chase has come to an end. You have come face-to-face with these cruel and tenacious pursuers, and you must confront Jopil, One Question, One Kill.
>
> May you rest in peace… No, fortune in battle.
>
> **Grade:** Peak
>
> **Limit:** Jin Taekyung
>
> **Task:** Survive — Incomplete
>
> **Reward:** ???
>
> **Failure:** Death
>
> - You do not have the authority to choose this Quest.
>
> - The Quest has been forcibly accepted!

“…Huh?”

What was this. Where was I, and who was I?

Countless questions rose and vanished. Then I heard someone’s voice.

“We finally meet.”

A man stood beside a gaunt tree, about twenty zhang away.[^1] Far if you called it far, close if you called it close. The problem was that nobody had known he was there.

Not even me.

*When the hell did he…?*

The higher my Level and martial realm, the sharper my five senses got. And I still hadn’t picked that man up. I hadn’t even heard footsteps.

If he hadn’t spoken first—if the Quest Window hadn’t appeared—I would have turned around without knowing a thing.

*The wolves.*

Those beasts had run. Not from me. From that man.

The unease that hadn’t left me since earlier took on a shape. I didn’t even need Qi Sense.

I already knew his name.

“Jopil?”

The man—Jopil, One Question, One Kill—smiled wide and nodded.

* * *

I had met three Peak masters so far.

Jin Wikyung, Wipeng, and the Head Elder. All three looked the part. Jopil, One Question, One Kill, did not.

*He looks ordinary.*

He wasn’t a giant like Jin Wikyung, didn’t have sharp eyes like Wipeng, and didn’t wear a silver beard like the Head Elder.

Jopil was average height, unremarkable face—and that made him look even more dangerous.

“Nice to meet you.”

The instant Jopil smiled brightly and stepped forward, I sprang back. No thought required.

“Nimble. Good reactions, too. I like you.”

My heart hammered. Maybe from the tension, a hoarse voice slipped out.

“Don’t come any closer.”

“Sorry about that. I got a little too happy to see you.”

I wasn’t happy at all.

“Don’t be so tense. I only want to talk.”

“Talk?”

“Yes. I’ve been wanting to meet you.”

From Jopil’s side, he probably had. He’d lost twenty men just a few days ago.

*Fuck. I’m fucked.*

The thought of a master like that chasing me day and night for two days, wanting to tear me apart, made my stomach turn.

“Don’t give me that bullshit, Jopil!”

When I shouted, I felt the air behind me freeze. Jopil smiled like he already knew.

“What difference does it make if you tell them who I am? Second Rate, Third Rate. All idiots and trash.”

He’d read the reconnaissance squad’s level exactly. I almost wondered if he was using the System too.

“Why not have a short conversation? There’s a lot I want to ask you.”

“A conversation? You’re not just buying time?”

“Buying time? What is that supposed to mean?”

“You know what it means. You’re waiting for your men.”

As if I’d hit the mark, the bridge of Jopil’s nose twitched. Right. I didn’t know why, but he was alone. If I was willing to take a few losses, it might be enough to…

“Waiting? Me? For those pathetic weaklings?”

“…What?”

“Didn’t I already say? They’re all idiots and trash. Hopeless lives. No effort, no talent.”

“…”

“Black Mountain Blade was decent enough, but he had no eye for people, so he deserved to die. I tore his eyes before I left. Punishment for failing to recognize a master.”

Correction. Jopil, One Question, One Kill, didn’t look dangerous.

He was a fucking dangerous bastard.

*This guy’s completely insane.*

I’d never seen anyone like Jopil, in real life or in a game. That unbothered tone and manner. He treated people like tools. A psychopath.

“Anyway, what you’re worried about won’t happen. They’re painfully slow. It’ll take them half a shichen to catch up.[^2] By then, everything will be over.”

One thing was certain. In the ending Jopil had in mind, his own death wasn’t part of it.

“Well?”

“And if I refuse?”

Jopil smiled softly.

“I’ll be disappointed in you. Very disappointed.”

I could more or less picture what happened if he got disappointed.

“Young friend, I have no grudge against you. No—if anything, I’m rather fond of you. Answer a few things truthfully, and I might even let you go.”

“Wait. Let me go?”

“Yes. I won’t lay a finger on you. I’ll send you back in one piece.”

“…Really?”

“I’ll stake my neck on it. Is that enough?”

The sincerity showed on Jopil’s face. Unpredictable psychopath or not, maybe everyone could walk out of this alive.

“All right.”

Even if the worst came, all I could do was fight. I’d buy a little time and try to read his openings.

“Good. A friend who can talk, haha.”

Jopil clapped and laughed. The sword case at his left hip swayed.

*Right-handed. Swordsman.*

I kept inputting the data in my head.

“First, I’d like to ask your age.”

“Twenty.”

Jopil’s eyes went round.

“My. That realm at twenty. Impressive.”

Seven years as a Hunter and I never got out of F-rank. In this game, they treated me like a martial arts genius. Strange feeling.

“Judging by your clothes, you seem to be from the Jin Family of Taiyuan.”

I nodded readily.

“Super First Rate at twenty. You wouldn’t be that famous Heaven Shaking Sword, so… your name?”

“Jin Taekyung.”

“Jin Taekyung. Jin Taekyung. I’ve heard that name somewhere. Ah!”

Jopil had been turning it over. Then he exclaimed.

“The wastrel third Young Master! That’s you?”

“Not a wastrel. These days they call me the Sleeping Dragon.”

“Puhahaha! I knew it. The Jin Family of Taiyuan, those rigid fools, poisoning someone? Please. I don’t know who set this board, but things are getting interesting.”

Jopil looked at me, satisfied.

“I’ve heard plenty of rumors about you. Was all of that a disguise?”

“…Something like that.”

“Good. A hidden blade, then. I like it. When did you start learning martial arts?”

“Seven years.”

Not entirely a lie. By Murim standards, Hunter combat methods were a kind of martial art too.

“Seven years. And your master?”

“Don’t have one.”

“No master?”

He studied me for a while, then said,

“Doesn’t seem like a lie.”

“You promised to spare me if I answered honestly. That was your promise, wasn’t it?”

“Yes, it was. An absurd, entertaining story. A direct descendant of the Jin Family of Taiyuan, no master, that realm at twenty… My, my.”

My mouth was bone-dry. I gripped the spear and scanned Jopil’s body. The openings on him right now were unbelievable. But was what I was seeing really all there was?

*He could be baiting me into attacking first.*

The thought didn’t go any further. Jopil suddenly burst out laughing.

“Hahaha! Good. I like it. I’ll keep my promise.”

He’d keep his promise?

The thing I’d thought was impossible was actually happening. I stared at him, blank.

“No need to look at me like that. Truth is, at first I really wanted to kill you… But now that we’ve met, I find I want to watch you a little longer.”

Jopil went on, his voice full of goodwill.

“It’d be a waste to kill talent like this. Especially in a situation like this.”

“A situation like this?”

“Ah. You might not know. You’ll find out when you return. Go on, then. I hope you’ll have grown a little by the next time we meet.”

I could go? He meant it?

I backed away without dropping my guard. Jopil just smiled at me.

He looked like a fisherman letting a minnow go.

*They say even if you walk into a tiger’s den, you live if you keep your head.*

Who’d have thought Jopil’s wild-card personality would turn into an exit.

Once I had a safe distance, the breath I’d been holding came out. But there was no time to catch it. I had to leave this place a second sooner, if I could.

“We’re moving. Hurry!”

Then—

“Hold on, young friend.”

Jopil looked at me, puzzled.

“What are you doing?”

“What do you mean? Going back, like you promised…”

“I only gave permission for you. Alone.”

“…What?”

“I may not look it, but I’m in someone’s employ. I have to finish the mission I took on.”

The mission. Don’t tell me.

“The three survivors of the Sakju Branch. And those pieces of trash you call your subordinates. Leave them. I should be paid for two days’ work, don’t you think?”

Eyes that had been clear as a child’s flashed. The next instant, they were a predator’s.

“I’ll say this now. If you refuse, I’ll be very disappointed.”

I stared blankly at Jopil, the reconnaissance squad, the young siblings, and the dying Gong Yacheong. Time was short, but after dozens of loops of doubt and conflict, one line came out.

“Then be disappointed, you fucking bastard.”

Jopil laughed savagely.

[^1]: A zhang is a traditional Chinese unit of distance, roughly 3.3 meters.
[^2]: A shichen is a traditional time period of roughly two hours.
## Chapter artifact 29

# Chapter 29

Some people don’t hesitate once they’ve made a decision. Jopil was one of them.

“Let’s see what you’ve got.”

Jopil tossed the line out and kicked off the ground. Ten-odd zhang of distance vanished in two steps.[^1] A flash burst from his waist.

*Whoosh!*

*What the…?*

My body moved before I could think. The moment my outstretched spear shaft met the flash—

*Boom!*

A thunderous impact threw me backward. I shot toward the reconnaissance squad like a cannonball. Forget the shields—the three or four men in front went down in a heap.

“Argh!”

“Squad Leader! Are you all right?”

…Would I be all right?

*Wow, shit.*

I clenched the spear shaft. It still hadn’t stopped shaking.

The flash was Jopil’s sword. And in all twenty-seven years of my life, it was the fastest, strongest attack I had ever taken.

*It hit that hard even though I blocked it?*

If my reaction had been even a moment slower, I would have been hiking up Mount Beimang by now.[^2] I calmed my pounding heart and got back on my feet.

Jopil was smiling.

“I’m disappointed. Is that all you’ve got?”

The only reason I had been able to block it was because it was merely “that much.” If I hadn’t leveled up after mowing down those twenty men, I might already have been dead.

*Fuck. Wrong opponent.*

My realm was Second Rate. Even so, I had easily beaten two First Rate masters so far—with the martial arts and stats I’d gained through the System, and with the combat experience I had built up.

But I could tell from that one attack.

*This guy is different.*

I felt outmatched in every way. Jopil was on a completely different level from Lee Seogeun or Black Mountain Blade.

Different enough that the word *death* came to mind.

“You’re afraid.”

Afraid? Me?

I looked at my hand. The spear had stopped vibrating, but the hand gripping it was shaking like an aspen leaf. My heartbeat was so loud it felt as though everyone could hear it.

“How will you survive in the martial world with a chicken heart like that?”

Jopil clicked his tongue.

“This won’t do. I’ll give you a little boost.”

“What?”

“Anger always beats fear.”

Before I could even understand what he meant, Jopil flicked his sleeve. Several streaks of light shot out at once.

*Danger!*

The instant a red alert went off in my head, I swung my spear. *Clang!* A few throwing knives bounced away with a sharp ring.

But I couldn’t stop every attack.

“Guh.”

One of the reconnaissance squad clutched his throat. Blood fountained between his fingers, and I saw a throwing knife buried there.

“Grrk. Squ… Squad Leader. Grrk.”

He dropped to his knees, gurgling on blood. His still-boyish face was twisted with the terror of dying.

“P-please, save me…”

*Whoosh. Thunk!*

No one survived throwing knives to the throat and between the eyes. He was no exception.

*Splat.*

He planted his face in the ground, which had only just begun to thaw.

He never got up again.

It had all happened in an instant.

“I picked him because he looked the youngest… Was he a subordinate you cherished?”

I shook my head at Jopil’s question.

“No.”

“That’s a shame.”

“I don’t even know his name.”

“You called him a subordinate.”

“He was an NPC. No need to know his name or his age.”

“What?”

I turned the corpse onto his back. After brushing the dirt and snow from his face, I closed his staring eyes.

Then I spilled it to Jopil, who still looked bewildered, like a confession.

“We’ve only known each other three days.”

“Is that so?”

“That’s right.”

“Then…”

Jopil smiled and went on.

“Why are you angry?”

He was right. Something was bubbling up from the pit of my stomach. My head and chest were burning, and I had to say something.

*What was that kid’s name again?*

He was the one they called Number Seven in the reconnaissance squad. I had forced a shield on him when he didn’t want one and trained him whenever I had the chance. He was young, so a few words of praise had him breaking into a goofy grin.

*What was his name?*

In the end, I couldn’t remember.

I didn’t even know all my goshiwon neighbors’ names.[^3] Why would I remember some NPC I had only known for a few days? There was no reason to, and no need.

*But…*

I was annoyed. I was angry. I had thought it would be different in a game, but even here I hadn’t protected my teammate.

The reason I had gone out of my way to train him, the work of the past few days—gone like foam. I opened my mouth and let out a hot breath.

“You son of a bitch. You’re dead.”

I chewed and swallowed the last fasting pill I had.

Together with the System message that my energy had recovered—

*Boom.*

I kicked off the ground and launched.

* * *

Jopil knocked away the spearhead that had surged up from his blind spot.

*Clang! Skrrratch.*

Fast, and strong. His fundamentals were solid, and his combat sense was quite good.

He was not someone a rootless wandering martial artist like that Mount Heng Sword Sect brat or Black Mountain Blade could handle.

*The Jin Family of Taiyuan… even rotten, still a junichi, is that it?*[^4]

Jopil slipped the spearhead aside at his leisure and thought.

The fall of the Jin Family of Taiyuan was nothing new. The prestige that had once covered Shanxi was already gone. All that remained was faded glory from the past, and talent that turned up once in a blue moon.

Someone like the Jin Taekyung in front of him.

*They’ve raised an interesting one.*

This much skill at twenty. He still couldn’t match the Heaven Shaking Sword, already called Shanxi’s greatest master, but he was an interesting kid.

Leave age out of it, and his internal energy and martial arts were both middling… but he knew how to fight. He knew exactly when to back off and when to press, and when a chance came, he charged like a fighting demon.

Just like now.

“Ha!”

*Whoosh—Boom!*

The spearhead flashed at his face and punched through empty air. With a bursting crack, Jopil’s hair flew.

*Well, look at this.*

The sequence of gripping the spear and thrusting was compact, flowing like water. And that movement—smoothly twisting his whole body before exploding the force—was silk-reeling force.[^5] He was still clumsy with it, but there was no mistaking it.

*Silk-reeling force at twenty?*

Innate sense, combat experience that called to mind an old martial-world veteran, and talent.

Frightening potential.

That was what Jopil was thinking when Jin Taekyung muttered with a stiff face,

“Fuck, what is this?”

“…”

Jopil’s feet tangled.

The instant he thought *ah, shit*, Jin Taekyung’s spear slid in like a snake. He hopped back and opened the distance, but the internal energy on that spear was no joke.

*Riiip!*

It was the first attack Jopil had allowed through. His upper robe split in a long gash, baring his chest.

“Ah, so close. I could’ve finished it.”

“…”

*So close? Finished it? Against me—Jopil, One Question, One Kill?*

Watching Jin Taekyung smack his lips, Jopil felt a violent surge of rage.

“Youuu bastard!”

His shout, loaded with internal energy, shook the forest. His eyes rolled back as he charged at Jin Taekyung.

* * *

The moment I cut a long gash through Jopil’s clothes, the System notification rang.

*Ding.*

> **System**
>
> **Lv.??? Jopil** enters **Berserk**!
>
> Strength and Agility increase for the duration!

*Damn it. Even more?*

“Graaaaah!”

*Boom! Boom!*

Blow after blow crashed down with a roar. The ground overturned, and trees were ripped out by the roots.

With his eyes rolled completely white, Jopil rampaged like a madman.

*The problem is, he’s no ordinary madman.*

A madman who happened to be a Peak master, no less. If I hadn’t had the **Gambler** Title, which increased my combat stats by 10% in a one-on-one, I wouldn’t have lasted this long.

*Boom!*

That wasn’t martial arts.

It was a bombardment.

But there was no precision in Jopil now. His movements were simple and fast, but the extra strength from **Berserk** had made them big and left him full of openings.

*I just need him to show me one opening…*

The problem was, I couldn’t see one.

He had completely lost it and was turning the area around us into a wasteland. All I could do was dodge. I didn’t even dare to block.

Step into range and I would be shredded. That much was obvious.

“Squad Leader!”

“We’ll go!”

I hurriedly waved off the reconnaissance squad members running toward me.

“Hey, don’t come! Don’t come! Fall back!”

Had they lost their minds? Coming *here*?

We had already lost one man for nothing. Wiping out the reconnaissance squad was not the result I wanted.

And besides—

*If those guys come over here, the Gambler Title’s effect disappears!*

**Gambler** only applied in a one-on-one.

I was barely hanging on as it was. If the Title’s effect vanished too, I had no idea how much longer I could last.

“Get back, you bastards!”

I shouted and flung myself sideways. Sure enough, Jopil’s sword smashed the ground to pieces.

*Crack!*

“Squad Leader!”

Hyuk Mujin’s shout came a beat late. For all I had tried to stop him, he was already charging. Behind him, I saw Han Yeop with a set, determined face.

“Hey, don’t—”

“Jopil, you vile bastard!”

“Get away from the Squad Leader!”

But it was a step too late. Hyuk Mujin and Han Yeop, who had come running with everything they had, drove their weapons at Jopil, who was preoccupied with me.

“Die!”

Sword and spear. Spear and sword.

Good timing, good attacks, like they had practiced it beforehand. There was just one problem.

They had the wrong opponent.

“How dare you, you rats!”

Jopil’s response was instant. He drove his sword into the ground where he stood and, in the same turn, smashed both weapons with his bare hands.

Going at a sword and a spear empty-handed was suicide.

But this was Murim.

More precisely, Jopil was different because he was a Peak master.

*Crack—Crunch!*

His palm had only brushed the side of the blade, and Hyuk Mujin’s sword still shattered into pieces before it reached him. Han Yeop stared in horror at his spear, the head sliced clean off.

That was Jopil’s straightened knife-hand.

“What is this?”

“That’s impossible…”

Before they could finish, Jopil’s hands slammed into both their chests.

They smashed into trees, spraying fountains of blood.

“I’ll kill you.”

On that chilling smile, the whites of his eyes were gone.

Berserk had worn off. He was back in his right mind.

“Fuck…”

From bad to worse. Mountains on mountains. Surrounded on all sides. Jopil, you son of a bitch.

The situation was sliding toward the worst possible outcome. If anyone was going to stop him, it had to be me.

“Jopil—!”

The internal energy I had pulled up at full strength raced through my whole body. I kicked off the ground and shot toward him.

Jopil grinned wide.

“Right. I’ll kill you first.”

But I had something to count on.

*He’s empty-handed right now.*

A mistake he had made while Berserk. And I was sure I could finish everything before he drew the sword from his back and swung it.

The next instant, I hauled up every bit of internal energy in my dantian. I focused all of it on a single point—the spear tip—and thrust.

“Die!”

The final form of the Jin Family’s Spear Technique, Sky-Piercing Strike.

If it could pierce the heavens, why couldn’t it pierce Jopil’s heart?

I was sure of it.

*This is it… the end.*

The world slowed, and I saw Jopil’s face.

He was smiling.

The moment I saw that smile, I knew.

Something was wrong.

*Skrrrng.*

Jopil’s sword was faster than my spear.

The blood-wet crimson blade shoved my spear shaft aside and drove inward. The instant my internal-energy-charged spearhead stabbed empty air—

*Slash.*

A chilling sound, and my chest felt cool. Then came the searing pain, and the blood bursting out.

Fortunately, I had jerked back at the last moment and avoided a fatal wound.

*Damn it.*

What the hell had just happened?

As I staggered back, Jopil charged.

*Whoosh-whoosh-whoosh!*

Crimson sword-light poured down. Every flash was so fast and strong I could barely see it.

I gritted my teeth and swung my spear, but Jopil had the edge in both momentum and martial arts.

*Slash. Thunk. Splurt.*

Lightning cut across my whole body. The blade stabbed my shoulder, slashed my knee, and punched through my side before coming back out with a spray of blood.

“Guh.”

“You didn’t drop your weapon. I’ll give you that.”

Jopil added,

“If you can take this, too.”

The next instant, his hand slammed into my chest.

[^1]: A zhang is a traditional Chinese unit of distance, roughly 3.3 meters.

[^2]: Mount Beimang is a burial mountain; hiking it means being dead.

[^3]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement.

[^4]: A junichi is a quality fish; even rotten, it is still a quality fish.

[^5]: Silk-reeling force is a method of twisting the entire body in a continuous, coiling motion to release power.
