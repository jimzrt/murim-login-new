# Checkpoint Review — 30–34

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

# Chapters 30–34

## Plot

Taekyung survives Jopil’s Flame Divine Palm and uses Inventory daggers to sever Jopil’s Achilles tendons and pierce his dantian, causing qi deviation. When Jopil burns his life for one final attack, Taekyung awakens the hardened third energy in his dantian, channels it through the broken Sharp Spear, and uses **Thrust with All My Might** to kill him. The skill’s destructive power exceeds Taekyung’s body’s limits, leaving him critically injured.

Taekyung remains unconscious for five days and confronts, in a nightmare, the guilt surrounding a disastrous modern-world Gate raid where his team died after he insisted on entering the boss zone. Wipeng reports that the reconnaissance squad and the Sakju Branch survivors returned safely. The squad member killed by Jopil was an orphan who dreamed of becoming Number One of All Time; Wipeng urges Taekyung to remember him and live his share as well.

The Jin Family wins a major battle at Honju, where one hundred elites defeat two hundred Mount Heng vanguard troops. Wipeng and Jin Wikyung each kill one of the Mount Heng Twin Devils, while the Mount Heng Lesser Family Head escapes. Jin Wikyung publicly celebrates Taekyung as the Sleeping Dragon of Shanxi, though the family’s rumor greatly exaggerates his victory.

Taekyung recovers rapidly after consuming a hundred-year snow ginseng. He reaches Level 30, has fifteen years of internal energy, and remains Second Rate until Wikyung explains that martial arts begin with belief. Realizing he has trusted the System’s label instead of his own achievements, Taekyung reaches First Rate. His martial arts advance by one stage, his body and meridians improve, his dantian expands, and he gains two levels. **Thrust with All My Might** evolves into the Peak, Second-Stage Skill **One Flash**, whose cost can be adjusted but whose overuse can leave him helpless.

Mount Heng gathers roughly five hundred fighters and plans to march on Taiyuan. The Jin Family will march north in two days, aided by the Five Gates of Shanxi, and strike before Mount Heng’s reinforcements join its main force. Taekyung accepts the **Rear Guard Defense** Quest, deliberately cultivates public awe to gain Fame, and goes to Medicine King Hall while still short of the Fame required for Logout.

## Continuity

- Jopil, One Question, One Kill, is dead. He was the nineteenth-generation successor of the Fire Gate Clan.
- Taekyung survived the fight but suffered severe damage to his qi and blood channels. The awakened hardened third dantian energy remains a major but dangerous power source.
- **Thrust with All My Might** evolved into **One Flash**, a Peak, Second-Stage Skill with adjustable stamina and internal-energy costs.
- Taekyung is now First Rate, has reached Level 30 and gained two additional level-ups, and possesses fifteen years of internal energy. His Fame remains below 500, so Logout is still unavailable.
- The reconnaissance squad and Gong Yacheong, Socheon, and Soyul returned safely. Hyuk Mujin and Han Yeop survived with serious but nonfatal injuries.
- The unnamed squad member killed by Jopil was an orphan; his body was recovered and buried, and his dream was to become Number One of All Time. Wipeng’s dream is Number One Under Heaven.
- Taekyung’s modern-world team died during a Gate raid after he insisted on entering the boss zone; he alone survived.
- The Jin Family defeated Mount Heng’s vanguard at Honju. Fewer than thirty Mount Heng fighters escaped, Jin Family casualties were similar in number, and Mount Heng lost three Peak masters. The Lesser Family Head escaped.
- Wipeng and Jin Wikyung killed the Mount Heng Twin Devils, both Peak masters.
- Mount Heng now has about five hundred assembled fighters, including hired wandering martial artists, black-market fighters, and mounted bandits. Lee Cheonbaek intends to march on Taiyuan and suppress rumors of Taekyung’s victory over Jopil.
- The Jin Family will march north in two days. The Five Gates of Shanxi has pledged support, including the Three Paths Sect. The enemy force could reach about one thousand after reinforcements join the Blood Wolf Sword’s main force.
- Taekyung accepted the **Rear Guard Defense** short-term Quest and is expected to command the rear guard.
- The capsule’s purpose, route home, and the limits of Murim’s death and resurrection rules remain unresolved.
- The Head Elder’s Sound Transmission accomplice and the full purpose of their plan remain unidentified.
- Medicine King Hall entry is restricted to authorized personnel; Taekyung has gone there seeking additional Fame.

## Translation Decisions

- Preserve **Flame Divine Palm**, **Fire Gate Clan**, **qi deviation**, **Inventory**, **Sharp Spear**, **Thrust with All My Might**, and **One Flash**.
- Keep **First Rate**, **Second Rate**, **Peak**, **Grade**, **Level**, **Fame**, and **Logout** distinct according to established System terminology.
- Preserve Wipeng’s “live his share as well” counsel and the contrast between Taekyung’s guilt, dark humor, and growing responsibility toward Murim’s people.
- Retain **Sleeping Dragon of Shanxi**, **Mount Heng Twin Devils**, **Five Gates of Shanxi**, and **Three Paths Sect**.
- Preserve the exaggerated public rumor, Wikyung’s destructive affection, and Taekyung’s deliberate Fame-seeking as dark action-comedy.
- Keep the modern Hunter terms **Gate**, **Demon Realm**, **Magic Gems**, **boss zone**, and Hunter grades distinct from Murim terminology.
- Preserve the goshiwon footnote and the established gold-spoon/God-Spoon wordplay where relevant.

## Durable state

{
  "version": 1,
  "safe_through": 34,
  "continuity_sources": [33, 34],
  "active_continuity": [
    "Jin Taekyung is trapped in Murim through an old game capsule; death is presented as permanent and he cannot log out at will.",
    "Taekyung is the disgraced third son of the Jin Family of Taiyuan and narrates with dry, self-mocking, occasionally profane humor.",
    "Logout is the Main Quest reward for reaching First Rate, Lv. 30, and 500 Fame. Taekyung is Lv. 30 with Fame 410 and fifteen years of internal energy; Lv. 30 is complete, while First Rate and Fame 500 remain incomplete.",
    "Taekyung's Jin Family's Cultivation Technique remains at the Fourth Stage; his Spear and Manoeuvre Techniques are at the Fifth Stage, and Third-Stage Qi Sense detects targets through Lv. 50.",
    "Taekyung has the Gambler Title, which increases combat stats by 10% in a one-on-one fight; it does not apply when allies join the fight.",
    "Taekyung's unidentified dantian energy is stronger than his ten years of internal energy, rejects contact during ordinary cultivation, and remained immovable until the mortal danger in Chapter 30 awakened it; training raised Sinews and Bones by 1 each while the Status Window still displayed ten years.",
    "Jin Wikyung is Taekyung's thirty-five-year-old eldest brother and the Lesser Family Head of the Jin Family of Taiyuan; Wipeng is his trusted guard. The Head Elder is Taekyung's great-uncle and the family's most senior elder.",
    "Jin Mukyung is twenty-five, the Heaven Shaking Sword, and a cadet at Heaven's Gate Temple.",
    "The Mount Heng Sword Sect and the Jin Family of Taiyuan are sworn enemies. Mount Heng has declared war, made Taekyung a public enemy, and triggered the Main Quest — War; fleeing incurs severe penalties. Wikyung sealed the family grounds against entry or exit without his seal.",
    "Before the Honju battle, the Jin Family had roughly 200 martial artists, fewer than 20 First Rate masters outside the wider senior group, and three Peak masters; Mount Heng had at least 300 martial artists, more than 50 First Rate masters, and five Peak masters. Mount Heng now has about 500 men assembled after the Honju losses.",
    "The Lower District Sect's Shanxi branch, based at Honghwaru in Taiyuan, is led by Wolhwa, whose real identity is Eun Sowol, a Level 50 martial artist. Its wartime alliance with the Jin Family trades half of Mount Heng's shops and exclusive pleasure-district rights for exclusive Shanxi intelligence support.",
    "Yama Whip is a Peak whip master and Wolhwa's coachman. Taekyung encouraged the gate guards' mistaken belief that he helped Yama Whip defeat the Heavenly Axe, gaining 20 Fame as Poisoner rumors declined and Sleeping Dragon rumors gained credibility.",
    "Lee Cheonbaek, the Blood Wolf Sword and Sect Leader of Mount Heng, is Lee Seogeun's father. He expelled poison from his son's corpse, vowed revenge, and sent about two hundred armed martial artists toward the Jin Family; after the Honju defeat, he orders Lee Seogwang back to the sect and prepares to march on Taiyuan.",
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
    "Taekyung survives Jopil's Flame Divine Palm and remembers his first use of the Hunter skill Thrust with All My Might, whose destructive power exceeds his body's limits and normally incapacitates him.",
    "Taekyung uses daggers from his Inventory to stab Jopil's foot, sever both Achilles tendons, and drive a dagger into Jopil's dantian as his internal energy peaks, causing qi deviation.",
    "Jopil is the nineteenth-generation successor of the Fire Gate Clan. He burns his life for a final attack, but Taekyung awakens the hardened third internal energy, channels it through his ruined qi and blood channels, and kills Jopil with Thrust with All My Might through the broken Sharp Spear.",
    "Hyuk Mujin and Han Yeop survived Jopil's final attack; both suffered serious injuries, but their lives are not in danger.",
    "Mount Beimang is a burial mountain; going or hiking there is an idiom for dying. A goshiwon is a tiny, cheap room-for-rent housing arrangement.",
    "Taekyung was unconscious for five days after killing Jopil; the Medicine King Hall Leader had expected him to die within a day.",
    "The reconnaissance squad and the Sakju Branch survivors returned safely. Two people suffered serious injuries, but no lives are in danger.",
    "The unnamed squad member killed by Jopil was an orphan. His body was recovered and buried, and Taekyung learned the young man’s chosen name and dream of becoming Number One of All Time.",
    "Wipeng urged Taekyung to remember the dead and live their share as well; Wipeng’s own dream is to become Number One Under Heaven.",
    "Taekyung’s modern-world backstory includes a disastrous Gate raid two years earlier: after he insisted on entering the boss zone, every teammate died except him.",
    "Two days before Taekyung wakes, one hundred Jin Family elites defeat two hundred Mount Heng vanguard troops at Honju; fewer than thirty Mount Heng fighters escape, and Jin Family casualties are similar in number.",
    "The Mount Heng Sword Sect's Lesser Family Head escapes the Honju battle. The Mount Heng Twin Devils are Peak masters; Wipeng and Jin Wikyung each kill one, and their deaths are a major gain because fewer than twenty Peak masters exist across Shanxi.",
    "Wipeng sincerely acknowledges Taekyung's defeat of Jopil but says Taekyung was not stronger than Jopil and won through a surprise attack.",
    "Jin Wikyung hears the account of Taekyung's victory, wrecks part of Taekyung's bedroom in an emotional outburst, then carries Taekyung's bandaged body before a crowd.",
    "The family rumor exaggerates Taekyung's actions into leading a death squad, defeating Jopil and one hundred wandering martial artists, and rescuing the Sakju Branch's household; Wikyung publicly celebrates him as the Sleeping Dragon of Shanxi.",
    "Taekyung checks the System after recovering: he is Lv. 30, has Fame 410 and fifteen years of internal energy, and remains Second Rate. Thrust with All My Might has become the Peak, Second-Stage Skill One Flash, whose stamina and internal-energy cost can be adjusted but which can leave him helpless.",
    "Lee Seogwang is Lee Cheonbaek's son and the Young Sect Leader of Mount Heng. He returns from Honju with twenty-three survivors, including himself, after more than two hundred Mount Heng troops and three Peak masters are lost.",
    "Lee Cheonbaek has five hundred men assembled, plans to march on Taiyuan in three days, and is willing to hire wandering martial artists, black-market fighters, and mounted bandits while suppressing rumors that Taekyung killed Jopil.",
    "Taekyung recovers from Jopil's attack in two days. The hundred-year snow ginseng granted twenty years of internal energy, but most of it was consumed by his final Skill use.",
    "Taekyung recognizes that he enjoys living as a martial artist in Murim but still wants to return to his family and true self in the real world. Jin Wikyung is the person he intends to ask about reaching First Rate.",
    "Jin Wikyung learns from the Lower District Sect that Mount Heng is gathering troops. The Jin Family will march north with all its forces in two days and strike before the reinforcements join the Blood Wolf Sword's main force, which could then number about one thousand.",
    "The Five Gates of Shanxi is an alliance of five small- and medium-sized sects that has agreed to aid the Jin Family. A representative of its Three Paths Sect introduces himself to Taekyung and pledges support.",
    "Taekyung accepts the Rear Guard Defense short-term Quest after Jin Wikyung asks him to command the rear guard; the System rewards Fame for acceptance and penalizes refusal.",
    "Jin Wikyung tells Taekyung that martial arts begin with belief. Taekyung realizes he has trusted the System's Second Rate label instead of his own achievements and recognizes that he is already First Rate.",
    "Reaching First Rate raises every martial art by one stage, greatly improves Taekyung's Sinews and Bones and Meridians, expands his dantian, and grants two level-ups.",
    "Taekyung gains Fame from the accepted Quest and public awe and rumors, but remains roughly fifty short of the Logout target. He goes to Medicine King Hall, where entry is restricted to authorized personnel."
  ],
  "open_questions": [
    "The capsule's purpose and the route home remain unresolved.",
    "The limits of Murim's death and resurrection rules remain unresolved.",
    "The identity of the Head Elder's Sound Transmission accomplice and the full purpose of their plan remain unresolved."
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
    "Use Three Paths Sect for 三道問, retaining the Chapter 34 note that the given final character is 問 rather than the usual 門."
  ]
}

## Reading copies

## Chapter artifact 30

# Chapter 30

*Whoosh.*

The instant Jopil’s red-hot palm struck my chest, energy as hot as lava swept through me. My breath caught, and my internal energy surged backward.

*What is this?*

The question came with me as I was sent flying. I slammed and rolled some ten zhang before I could stop.

“Cough.”

Blood trickled down my chin. The unidentified chunks mixed in with it now and then were… fuck. Pieces of organ.

*He got me good.*

Through my blurry vision, Jopil walked toward me. His unhurried stride had a victor’s ease.

*I have to get up.*

I groped beside me and found a cool spear shaft. Using the spear as a cane, I barely made it to my feet—and saw Jopil’s scowling eyes.

“You can still stand after taking a seventh-stage Flame Divine Palm… What a high-maintenance junior.”

*Wham!*

His palm detonated into me again.

The Flame Divine Palm was every bit as powerful as its name. My shirt burned away, and my flesh melted and sloughed off. The heat that sank inside me severed my blood channels strand by strand.

“Guh.”

Horrible pain crashed in. Instead of writhing in it, I drove the spear at Jopil’s vital point.

*Thunk.*

“You’re like a fighting dog.”

Jopil snatched the spear shaft and clicked his tongue.

“Someone at your level can’t do anything to me.”

“Go… fuck yourself!”

The next moment, I let go of the seized spear and threw myself into his chest.

Last chance. Focus every bit of internal energy on a single point. If I struck his vital point, I could turn the tide.

But…

“Gasp.”

The result was disastrous.

I had forced my internal energy up without accounting for my internal injuries. I collapsed on the spot and shook like I’d been struck by lightning.

I could feel drool running from the corner of my mouth.

“Pfft. Puhahaha! Have you ever seen such a stupid bastard!”

Jopil burst into mad laughter and snapped the spearhead.

“Well? What now? Huh? Youngest Young Master of the Jin Family of Taiyuan?”

I had no weapon left. Despair blacked out my vision.

*Am I going to die like this?*

In the last seven years, I had never felt death this close. Me—who had fought more than a thousand times and lived. Die here, of all places?

This pointlessly?

*No. I can’t die like this…*

I reached out, but that was as far as I got.

—Squad Leader!

A shout crackling with static was the last thing I heard before all the light went out.

* * *

When I opened my eyes again, it was neither heaven nor hell. I was drenched in sweat and panting. My whole body felt heavy, like waterlogged cotton.

*A dream? Or my life flashing before my eyes?*

Either way, one thing was certain. This was the past—a memory from seven years ago. The familiar face of the training instructor was proof enough.

“You—you, this…”

The instructor couldn’t finish. His eyes were on a steel dummy built for training. Modeled after a monster, it was little more than scrap metal now.

Bent and split scrap, head to toe.

“Was that a skill just now?”

My younger self answered in an exhausted voice.

“Thrust with All My Might.”

“Thrust with All My Might?”

“Yes. I just thrust as hard as I could.”

“You don’t really know how to use it, but after Awakening you just started using it naturally?”

“Uh, yes. That’s right.”

“That’s a skill, you idiot.”

Looking incredulous, the instructor turned to the file in his hand.

“Jin Taekyung. Twenty years old. Lives in Goyang, Gyeonggi Province. F-rank Awakened. Is this you?”

“Yes. So? My full-power thrust—no, my skill. It’s good, right?”

“You’re asking if it’s good?”

The instructor let out a hollow laugh.

“I’ve been at this training center for fifteen years, and I’ve never seen anything like this. Destructive power like that should be at least D-rank.”

“Fuck, I knew it. Uh, Instructor. I’m leaving.”

“What?”

“I’m going to get reevaluated. Honestly, with power like that, I should at least be E-rank.”

“No. They seem to have judged you correctly over there.”

“What?”

“The skill really is incredible. It’s a level that could never come out of an F-rank. But…”

The instructor scratched the back of his head.

“You can’t use it.”

“Why? Why not?”

“Your body can’t keep up. That skill is beyond what F-rank mana and physical ability can handle. That’s why you collapse after using it once.”

“But I’m fine.”

“Are you?”

Before I could even nod, the instructor’s hand shot out like lightning and tapped my chest.

Literally a tap. But I’d used up all my strength, so I flopped onto my back.

My whole body throbbed. I could barely twitch a finger.

“You’re already putting out more power than your limits can handle. Later on, it won’t end with a little soreness.”

“…Is there another way?”

“Solid fundamentals and excellent technique. And your own combat sense. If you want to live a long time, don’t use that skill. Ah. Except in special circumstances.”

“Special circumstances?”

The instructor grinned and added,

“When your life is in danger. That skill might save you once.”

The next moment, I opened my eyes on the cold snowfield.

* * *

“Squad Leader!”

The shout I’d heard at the end came through clearly. So did my wrecked body, and the sharp pain.

*I’m still alive.*

The flash of my life had lasted only an instant. Jopil was looking behind him, close enough to reach if I stretched out a hand.

“Not bad loyalty. Their skill’s pathetic, though.”

The reconnaissance squad was charging toward us in a cluster, right where he was looking.

“I’m thinking of tearing those guys apart and killing them. What do you say?”

“…dly. Fought.”

“What?”

“Stupid… fought.”

I mumbled it again. Jopil bent down, irritated.

“Can’t you even talk straight?”

“I said I’ve been fighting stupidly this whole time.”

*Ptoo!*

The moment I’d been waiting for.

I spat the blood I’d gathered at his face. Half a beat faster, my hand was already slamming down toward his foot.

*Inventory Open.*

Jopil didn’t know. I was a Hunter, a man of Murim, and a player who could use the System!

*Equip Dagger.*

A solid weight filled my empty grip. Jopil, his face covered in blood, tried to jerk back, but the dagger’s tip had already punched through the top of his foot.

*Shunk!*

“Guh.”

Even a Peak master was still human.

When his body jerked to a halt from the sudden pain, I dropped the dagger and reached for his ankle.

*Equip Dagger.*

My Inventory was piled with weapons from enemies I’d taken down since the Tutorial. Swords, spears, axes, daggers… more than twenty of them.

Jopil’s men had been a walking armory.

*Slice.*

“Gaaah!”

The Achilles tendon. The moment I cut the tendon at his ankle, a scream burst out of him. As his stance collapsed, I rolled aside, slashing and stabbing. His remaining left leg was soaked in blood too.

*Slice. Thrust. Thrust. Stab-stab-stab!*

Jopil’s mouth fell open with rage and pain.

“Gaaaaah! You son of a bitch!”

He couldn’t use either leg, but Jopil was a Peak master. He spun like lightning, slipped the dagger, caught my wrist, and twisted.

*Crack.*

“Gah!”

The attack didn’t end there.

A red-hot palm.

The Flame Divine Palm.

*Boom.*

My chest caved in. My vision went white. Powerful fire qi tore through my body.

*Boom.*

The strength drained out of me.

From the neck in Jopil’s grip came the sound of bone slipping out of place. A chilling voice slid into my ear.

“You understand now, don’t you. Who you picked a fight with.”

“…Cough.”

“If King Yama asks, tell him I sent you.”

To me, hanging limp as a corpse, Jopil declared it with a face full of rapture.

“Die.”

The final Flame Divine Palm shot toward my chest. Lava that would swallow my life whole was imbued in that blazing palm.

And at last…

*Tap.*

The world stopped.

No lava. No heat of any kind. Only a scarred, callused palm resting against my chest.

A ripple ran through Jopil’s eyes.

“You…”

The grip on my throat slipped away. As Jopil staggered backward, I saw the dagger driven in below his navel—buried in his dantian.

“This… what the hell is this?”

The next moment, blood ran down Jopil’s chin.

That was only the beginning.

Blood started pouring from his eyes, his nose, and his ears as well. A waterfall of blood streamed from his seven orifices.

The reconnaissance squad stopped in their tracks at the horrifying sight. Someone muttered, almost a groan.

“Qi deviation…”

Internal energy was a double-edged sword.

I had waited for the moment Jopil drew his internal energy to its peak, then driven a dagger summoned from my Inventory into his dantian.

The result was a reversal of internal energy. Qi deviation.

“You were definitely empty-handed.”

I answered in a tired voice.

“You live long enough, all sorts of things happen.”

“I can’t die like this. This makes no sense.”

Jopil muttered like a man whose soul had left him and took one step after another.

Wherever he passed, pools of blood collected.

“I am Jopil. Jopil, One Question, One Kill. The nineteenth-generation successor of the Fire Gate Clan. I’m not someone who should die at the hands of a nobody like you!”

A chilling, ghostly aura came off him as he screamed, covered in blood. Even the reconnaissance squad members who had charged in ready to die were shaking with fear.

“Then why? Why, at the likes of you, would I—!”

That was when the ember I’d thought extinguished burst into flame.

The change started in Jopil’s body. The flowing blood stopped, and the veins all over him stood out blue. He looked like a man who couldn’t feel the pain of both tendons being cut—or even the qi deviation.

A terrible heat poured from his breath.

*What is this?*

A literal resurrection?

No. This was Jopil’s last desperate struggle.

Everyone screamed, seized by terror, but I could see it clearly. His hair was turning white by the second. His skin was shriveling.

Right now, that man was…

*Burning his life.*

*He’ll kill me, at least, before he goes.*

Power gained by throwing away the most precious thing he had. Every bit of it was aimed at me. I knew on instinct that I couldn’t dodge.

*Can I do this? Me?*

I picked up the fallen spear.

The *Sharp Spear* I’d used from the Tutorial until now.

Its spearhead was broken. Nothing left but a pointed iron rod.

*I’ll end up looking like this soon enough.*

I had only one option left.

Even if I succeeded, I couldn’t guarantee I’d live. But there was no luxury of hesitation.

“Jin Taekyung!”

“Yeah. Let’s finish this.”

Me and Jopil.

Jopil and me.

We shot toward each other. The heat pouring off him melted the piled snow and dried my lips. I drew a long breath.

*Sss. Hoo.*

The noise around me receded. My heartbeat and breathing sounded like thunder.

*Thump. Thump-thump. Thump-thump-thump.*

My heartbeat hit its peak. My breathing locked in, precise as a machine.

I was certain.

*Now.*

At the same time, I woke the internal energy in my dantian. Inside me, where my qi and blood channels were twisted and wrecked, the only thing left was the third internal energy, hardened like rock.

My only option—and the last piece that would fill my Skill.

*Run wild as you please.*

The awakened energy went berserk. It forced its way through my ruined qi and blood channels and spread through my whole body. A dizzying pain hit me.

But it was soon forgotten in the new strength the energy gave me.

*Go!*

Every muscle in my body pulled taut. From my calves and thighs, through my waist and along my thrusting arm, every bit of strength and internal energy in me surged forward.

Condensed air burst from the broken spear tip.

Matching it, Jopil thrust out his Flame Divine Palm.

“Dieeeee!”

*Whoooosh.*

A mound of snow erupted with the wind. Through the flakes drifting gently back down, Jopil came into view.

From the right arm that had unleashed the Flame Divine Palm, through his shoulder and his side—half of his upper body had evaporated.

“What kind of martial art…?”

I dropped the spear and answered.

“Thrust with All My Might.”

The next moment, heaven and earth flipped.

Beyond my blurring vision, Jopil’s already lifeless head shot high into the sky.

Socheon was crying out loud, holding a sword as tall as he was.
## Chapter artifact 31

# Chapter 31

“Well, look at this. This bastard’s got it made.”

I slowly opened my eyes to a familiar face.

“Did you come here for a picnic? Sleeping in a Gate?”

I must have dozed off. I answered, shameless.

“I wasn’t sleeping. Who says I was?”

“Wipe the drool off your mouth before you start lying.”

“Tsk.”

“Oh, you little—”

He shook a fist at me, but a smile sat at the corners of his mouth. I rubbed my stiff neck.

“Ugh, I’m tired.”

“Did you meet a woman yesterday? Why are you nodding off like a sick chicken even in the middle of a raid?”

“When would I have time to meet a woman? You know my situation.”

“True enough.”

We’d been through thick and thin for five years, from our first battle until now. He knew me as well as I knew him.

“Then what’s wrong?”

“What do you think? Money.”

“Money? Don’t tell me you’re moonlighting.”

His voice dropped low. I looked past his shoulder at the team members resting nearby and nodded.

“Well, well. This bastard gets a little time under his belt and now he’s stuffing his back pocket. And he’s the vice team leader, no less.”

“Raids have been scarce lately, and I’m strapped. Really strapped. You’ve done it yourself, hyung, so don’t give me that.”

Hunters with professional licenses were legally barred from second jobs. Even a D-rank probably wouldn’t have to live like this, but F-ranks like us had no choice. That was why the Guild looked the other way even when they knew.

“True, but… be careful. If someone files a complaint with the Management Agency, it’ll become a real headache.”

“It’s a trustworthy place. They pay cash the same day, so there’s no problem. You think I’d do this for nothing?”

“Really?”

Judging by his face, he was tempted.

“Do you need money too, hyung?”

“I’ve got three kids. I’d need an oil well to blow in the yard.”

He poured it out with a miserable look. I’d already heard this routine dozens of times. After venting about the misery of raising kids, the rising price of formula, and the shamelessness of merchants, he patted my shoulder.

“Don’t get married.”

“I won’t.”

More precisely, I couldn’t.

I had no woman and no money. My life’s goal was to buy a house in a safe zone within five years, so deep down I envied him.

A spouse I loved, and kids. A happy family. I had no idea when I’d ever get something like that.

“Marriage is a swamp.”

For all that talk, he had a reputation as a devoted husband and a good father. I knew how he sometimes took out his family photos and smiled fondly at them.

“Your whole life gets sucked in. You come to your senses and you’re buried up to your chest, barely breathing.”

“…”

Maybe I’d had the wrong idea about him.

“So don’t just work. Take breaks. Dating, hobbies—stuff like that’s good for you.”

“I don’t know. I still need the money.”

I scratched my head as I answered. He looked at me with pity.

“I saw you sleeping earlier, sweating cold the whole time. Keep that up and you’ll drop dead from overwork.”

“Was I?”

Now that he mentioned it, my back was damp with cold sweat. Must have been a bad dream…

*Can’t remember.*

Probably just some stupid dream anyway.

* * *

A Gate.

These days it was how Hunters like me made a living, but its true nature was an invasion route for the Demon Realm’s army.

When Demon King Asmodeus fell, his mighty army was routed with him. Decades later, the Gates were still there.

“Defensive formation!”

At his command, three Hunters bearing huge tower shields blocked the front. In a narrow cave, that alone was enough to soak most attacks.

*Clang! Clang-clang!*

“Giiiiik!”

About twenty goblins hurled poison needles, axes, and spears, but every one of them bounced off those big, beautiful tower shields.

“Archers!”

Up front, the tanks blocked every attack. From the rear, the archers poured arrows. We pushed forward and dropped about half of them, and the goblins let out panicked cries.

“Gyaaaah!”

“Kieek!”

He timed the next order perfectly.

“Attack formation!”

The tanks dropped their tower shields and burst forward at the same time. I was faster.

“Hah!”

I swung the iron spear in a wide arc. Green blood burst, and the front rank broke. I dove into the gap, stabbing and cutting at everything I could reach, and the line came crashing down.

“Charge!”

The damage dealers and tanks piled in, and in an instant the goblin pack was a pile of corpses.

“Pretty easy today, huh?”

“Honestly, the vice team leader did half of it. He was flying around. When did he get that good…? Shh. The Team Leader’s pissed.”

The people chatting shut their mouths the moment he appeared.

“Hey, Jin Taekyung!”

That made me jump.

I’d been staring off, lost in thought, and I startled as I answered.

“What?”

“Who told you to go solo? Are you a tank? Forget the attack order? And you still call yourself vice team leader?”

“That’s not—”

“If you’re going to act like this, transfer teams. You’re putting the rest of them in danger too.”

I looked at his grim face and sighed.

“I’m sorry. I don’t know why I did that. They just… suddenly didn’t seem like a big deal. I must have lost it for a second.”

The feeling was strange. The moment I saw the goblin pack, I’d thought I could wipe them out by myself.

No. That hadn’t been a thought.

It had been certainty.

“You…”

He swallowed the rest. We’d had each other’s backs for five years now, and this was the first time I’d ever pulled something like this.

“Don’t do it again. If you’re having a hard time, tell me.”

I watched him walk away after patting my shoulder. For some reason, a spot in my chest throbbed.

*Should I see a doctor?*

But before long I wasn’t even thinking about the pain.

* * *

“Magic Gems!”

“Got some!”

“Another!”

“Jackpot! Jackpot! Jackpot!”

“Mom! Hayeon!”

Ah, that last shout was mine. His face was flushed too as he muttered.

“Hey, what is all this…?”

Twenty Magic Gems, large and small, lay neatly on the floor.

Magic Gems. They looked like red pebbles, but they were called the flower of the Gate. These lumps of mana that monsters carried were high-dimensional energy, and the most valuable byproduct a monster had.

“At this rate, each one’s got to be worth over a million won.”

That from the Team Leader, an E-rank Hunter who’d lasted ten years in this business. People’s eyes went slack at the intoxicating sight.

“Is it normally like this?”

At the new recruit’s question, everyone shook their heads hard.

“Absolutely not.”

In an F-rank Gate the average was one or two, and even with incredible luck you wouldn’t hit five.

I was busy doing the math.

*Twenty million from the Magic Gems alone, another five million for the byproducts and Equipment. Add all the various allowances and…*

*Fuck. How much is this?*

The biggest jackpot I’d hit since becoming a Hunter.

And the raid wasn’t even over yet.

“How far have we come?”

“Almost there. Turn right and it’s the boss zone.”

The words *boss zone* made everyone’s eyes light up.

It went without saying, but a boss zone had a boss. A boss monster was the strongest monster in that Gate—and the one with the most expensive byproducts, Equipment, and Magic Gems.

*If we take down the boss monster too?*

A literal jackpot. A once-in-a-lifetime chance for an F-rank Hunter.

Everyone was smiling bright at the thought when he spoke.

“Wait. Let me think.”

What the hell was he talking about?

“What do you mean?”

“Think about it. Every monster we’ve run into has been an ordinary goblin. This many Magic Gems? Something’s off.”

He sighed. Excitement still hadn’t left his flushed face, but there was conflict on it too.

“I know how you feel. I do… but we’ve already grabbed a fortune. Let’s be satisfied with this much and go back.”

Satisfied?

Here? After coming this far, turn back?

I looked at the other team members. Some had been in sync for two or three years; some were new. They all had the same look I did.

“I’m against—”

My breath caught.

*Damn it. The chest pain again.*

I tried to keep talking, but no voice came out. Now there was ringing in my ears too.

*What is this?*

The pain and the ringing got worse and worse. I dropped to my knees, gasping.

*Someone. Please, help me.*

I grabbed someone’s pant leg and hung on.

It was him. The man who’d looked after me like a brother, like a father, for the past five years.

*Hyung. Please save me.*

He looked down at me, indifferent.

“Me? You, who ran and left everyone behind?”

What?

“I wanted to live too.”

I forgot the pain and stared at him. Clothes and skin melted away, and bone showed through. Everyone except me had become skeletons, sprawled across the ground.

*Ah. That’s right.*

They were all dead.

That day two years ago. In the boss zone I had insisted we enter, they had all died.

*I was the only one who survived.*

I floundered, buried in the memories. I remembered the ominous darkness that had settled over the boss zone, the foul smell, the damp floor, and that thing’s enormous wings.

Bodies ripped to shreds in midair. Screams of terror. People running.

*You fucking bastard!*

But even the Skill I had poured everything into hadn’t been enough to kill it. As I waited to die, he pulled me to my feet.

*Taekyung!*

*Hyung, I’m sorry. It was all my fault.*

If it hadn’t been for me. If I hadn’t gotten greedy, everyone could have lived. They could have gone home to their families.

I wailed like a child, and he forced a smile.

*How is that your fault? Look at this kid, now you’re even playing Team Leader.*

The massive body drifted through the cave. Stalactites rained down, and the last member of the team let out a death cry. In the darkness, its red eyes turned toward us.

*That arrogant bastard. Taekyung, you go first.*

*Hyung. Cheonsu hyung!*

My chest hurt. Pain rolled in hard enough to blank my vision. It felt like I had swallowed lava, like everything inside me was burning away. The ringing in my ears turned into a monster’s roar.

*Kyaaaaau!*

* * *

“Hyung—!”

I woke with the scream.

But it wasn’t a Gate. There were no monsters, and no team members.

Someone stood up at the window, where sunlight poured in.

“Did you dream about my lord? He’ll be pleased if I tell him.”

Coldness dripped from his face.

Wipeng, Jin Wikyung’s right-hand man.

Seeing him made it real that I was still inside the game.

“Are you all right?”

“No. It was a nightmare.”

“Then I’ll leave that part out of the report.”

“Suit yourself.”

I was soaked in sweat. Through the gaps in the bandages wound tight around my whole body, I could see flesh raised with blood scabs.

“How long was I out?”

“You were unconscious for five days. Your condition was so critical that the Medicine King Hall Leader concluded you wouldn’t last the day.”

“Really?”

“Yes. When my lord heard that, he went berserk. If I hadn’t stopped him, he would have beaten the Medicine King Hall Leader to death.”

“Ah.”

I remembered the old man from the meeting a few days ago, the one who had threatened to shove a giant needle into the White Tiger Hall Leader’s anus.

*So he really had been chanting for me to die.*

“Did anything else happen?”

“A great deal happened. Among it, there’s good news and even better news. Which would you like to hear first?”

“The good news.”

“First, the reconnaissance squad and the survivors of the Sakju Branch returned safely. Two of them suffered fairly serious injuries, but their lives are not in danger.”

*Survivors.*

The word made my heart drop.

*Number Seven.*

I remembered his face as he gasped out his last breath, a dagger in his throat and another between his brows. Twenty at most. Far too young to lose his life.

“Are you thinking of the dead?”

“The body—did they recover the body?”

“We recovered it properly and buried him. He was an orphan with no one in the world, so there were no surviving relatives.”

“…”

“May I say something?”

Wipeng didn’t wait for an answer. He took a step toward me and went on.

“Third Young Master, do not turn your subordinate’s death into a dog’s death.”

“What does that…”

“Martial artists are not beings meant to be protected. They are people who fight their enemies and prove themselves. He died facing an enemy too strong to do anything about, but that was not mere death—it was death in battle.”

The idea that dying on a battlefield made it an honorable death was the biggest load of bullshit ever.

There was no such thing as an honorable death. Even now, the screams of my comrades who died two years ago and Number Seven’s wide-open eyes as his breath left him were still vivid.

“The fact that he died hasn’t changed.”

“There are people who cling to facts that will never change. I won’t say who.”

“…”

“Do you regret it?”

“Of course.”

“Then live his share as well.”

Wipeng continued in a gentler voice than I had ever heard from him.

“I’m not telling you to forget the dead. Bury them in your heart and carve them into your mind. Use that regret as a foothold and soar to the place they dreamed of reaching. That is the path you must take, Young Master.”

*The path I must take…*

Just hearing those words made something in my chest lurch. I turned them over for a while, then let out a sudden laugh.

“Damn. I’ll break a leg before I get there.”

“It will take a lifetime.”

“If I give it my whole life, can I make it there?”

“I don’t know. I don’t even know how far my own path goes, so how could I know yours?”

“What’s at the end of the road Great Hero Wipeng is walking?”

“Number One Under Heaven.”

A joke?

No. Wipeng was more serious and resolute than ever.

“That’s a hard one.”

“Because it’s a dream.”

He was right. Dreams were always hard to reach.

Even more so if you were carrying the dreams of those you had lost.

“Great Hero Wipeng. May I ask you one thing?”

“Anything.”

“That guy. What was his name?”

“His name was…”

The moment Wipeng opened his lips, a cold winter wind shook the window.

*Whoooosh.*

Beyond the chill of the wind, I heard Number Seven’s name.

“That’s a cool name.”

“I heard he chose it himself. His dream was just as big.”

“What was it?”

“Number One of All Time.”

“…”

“You’re going to have a hard time.”

“Yeah. That’s unbelievable.”

A laugh slipped out. Only then did I feel the weight in my heart lift.

It was all thanks to Wipeng.

“You’re finally back to your old self.”

“Thank you.”

“Don’t mention it.”

Wipeng tipped his head and spoke.

“Now, there’s still the even better news.”

Ah. Right.

Good news and even better news.

I waited, as expectant as I could get, for what he would say next.
## Chapter artifact 32

# Chapter 32

“There was a major battle two days ago. One hundred elite fighters from our family clashed with two hundred vanguard troops from the Mount Heng Sword Sect in Honju.”

“There was a battle?”

And a major one, no less—hundreds of people thrown in. My heart lurched for a moment, but then I remembered what Wipeng had said earlier.

Good news and even better news. I’d already heard the outcome.

“We won.”

“It was a great victory. Fewer than thirty of them escaped alive. That’s about the same as our family’s casualties.”

Judging by the scar running from Wipeng’s forehead to his chin, it must have been a fierce fight.

*Well, of course. They outnumbered us two to one.*

Still, it was a relief we’d won. From the Jin Family of Taiyuan’s perspective, we’d poured in nearly half our strength. If we’d lost, the damage would have been enormous.

“It’s unfortunate we let the Mount Heng Sword Sect’s Lesser Family Head escape, but taking the Mount Heng Twin Devils was a major haul.”

“The Mount Heng Twin D-Devils?”

“The Mount Heng Twin Devils. Peak masters under the Mount Heng Sword Sect, and their loyalty was something else… They kept throwing themselves at us without any regard for their lives, so we had no choice but to kill them.”

Wipeng tapped the fresh scar.

“If we’d captured them, we could have extracted some important information.”

“Did you—I mean, did Great Hero Wipeng kill them?”

“My lord and I took one each. They were pretty good.”

“…”

I was left speechless as Wipeng slurped his tea.

*For fuck’s sake… Are Peak masters a joke to him?*

It had been the fiercest fight of my twenty-seven years. All kinds of internal injuries, and I’d been sliced up like a steak. I’d been out for five days after that, so I’d practically taken a half-bath in the River Jordan.[^1]

And after taking down Peak masters of that caliber. What, *pretty good*?

*He’s a complete monster.*

I learned something for certain this time: even Peak masters came in different levels. It was a huge relief that people of that caliber were on my side.

“That aside…”

*Clink.*

Wipeng set down his teacup and looked at me with a peculiar expression.

“You were remarkable.”

“Pardon?”

“I’m talking about Jopil, One Question, One Kill. Defeating him isn’t something the word remarkable can even cover.”

“…”

*You people seem more remarkable to me.*

It felt like getting praised by an A-rank Hunter for being good at killing goblins.

“Ah. Yes. Thank you, I suppose.”

I wanted to wrap up the Jopil talk there. My body and my mood were both in bad shape, and I wanted to check the System Rewards still waiting for me.

*Let’s rest now. I’m still a patient, damn it.*

I put that meaning into a wink. Wipeng frowned.

“Does your eye hurt? Shall I call a physician?”

“…No. I’m fine.”

“Your eye just spasmed.”

“That wasn’t a spasm.”

“It was a spasm. I saw it clearly.”

“No, just now, that was…”

Then Wipeng rolled his eyes back until only the whites showed and started to tremble.

The table shook, and tea spilled over the rim of the cup. I cried out in alarm.

“My God, Great Hero Wipeng!”

*This guy’s epileptic. No—how does a Peak master even get epilepsy?*

Just as I hurriedly tried to stand, the trembling stopped. Back to normal, Wipeng spoke with a perfectly calm face.

“You did this.”

“Are you all ri—wait, what?”

“That’s what you did just now, Third Young Master. Your eye spasmed.”

“So you were imitating me?”

“Yes.”

*What kind of lunatic is this…*

I tried to explain the difference between a wink and an epileptic fit, but the words stuck. Wipeng was glaring at me like a pissed-off dictator.

“…Shall we just finish talking about Jopil?”

“By all means.”

Wipeng nodded, satisfied.

*You crazy bastard.*

In the end, I had to tell him everything about the fight with Jopil, from beginning to end.

How Jopil had moved, what martial arts he’d used. Wipeng’s sharp questions had me tensing up more than once.

“You severed the tendons in Jopil’s legs with daggers?”

“Yes. I had them hidden in advance.”

“There’s no way Jopil failed to notice them… Continue.”

When the long story finally ended, Wipeng let out the breath he’d been holding. The mixed feelings in the way he looked at me came through loud and clear.

“Third Young Master. You have accomplished a truly great deed.”

“Ah, thank you…”

“I hate to admit it, but I mean it.”

“…Ah. Yes.”

“When I think of all the trouble you’ve caused until now, my blood boils, but I was genuinely impressed. I mean that.”

“…”

“Who could have imagined that the Third Young Master who stole family funds day after day and poured them into pleasure houses, then paraded through the streets dead drunk and smeared shit all over the family’s reputation, would become such a great man? I, Wipeng, am genuinely in awe.”

*Just curse me out, you bastard…*

I barely held back the stream of swearing trying to burst out and said,

“I got lucky. Jopil let his guard down too.”

Wipeng shook his head.

“No. It was all skill. Who let their guard down and who hid a dagger beforehand are not excuses. If that had been enough to kill Jopil, he would not have been Jopil, One Question, One Kill. Murim is a place where only the strong survive.”

“Only the strong survive.”

I quietly rolled the words over my tongue. They tasted bitter and sweet at the same time.

Murim—this game—had been that kind of place from the beginning. I had survived there, and I had gotten stronger.

“Jopil used every martial art he possessed to its fullest. In the end, he even pulled up his innate qi. A Peak master threw away his own life trying to kill you. But what was the result?”

“I won.”

“Yes. Exactly.”

“Then I was stronger than Jopil.”

Wipeng, who’d been looking sour this whole time, turned serious.

“What are you talking about? Jopil was stronger. Do Peak masters look like a joke to you?”

“…”

“You were only strong enough to kill Jopil in a surprise attack.”

*Enough already. Seriously.*

While I was debating whether to pull a weapon from my Inventory, Wipeng let out a short chuckle. It was the first time I had ever seen him laugh.

“Well done.”

I looked at Wipeng suspiciously.

“What are you going to tack on this time?”

His smile deepened.

“I mean it. It’s true I disliked you quite a lot, but… this time, I have no choice but to acknowledge you.”

When he put it like that, I had nothing to say. I got embarrassed for some reason and cleared my throat.

“Ahem. Well, I almost died, but all I did was take down Jopil and a few wandering martial artists. Ahem.”

“How many Peak masters do you think there are in a single city? Across all of Shanxi, where our family is located, there are fewer than twenty.”

Twenty. Far fewer than I’d expected.

“The Mount Heng Sword Sect must have taken serious losses. They lost three Peak masters like that.”

“But the greatest blow is something else.”

“What is it?”

“That is…”

The instant Wipeng opened his mouth, a trembling voice came from the doorway.

“The pretext. The pretext for starting this war is gone. The Third Young Master of the Jin Family of Taiyuan is strong enough without using poison. Indeed, that’s exactly right.”

The enormous Jin Wikyung stood there, teary-eyed, both arms spread wide.

“My baby brother!”

“…”

*Please, just leave me alone.*

* * *

In the end, I had to replay the chase of the past several days and my fight with Jopil all over again.

“The wandering martial artists who chased the survivors…”

“Those bastards! I’ll tear them apart!”

*Boom!*

“Jopil’s Flame Divine Palm caused internal injuries…”

“I’ll kill him! How dare that vicious wandering martial artist bastard! Even if I ripped out his guts and chewed them to a pulp, it wouldn’t be enough!”

*Boom! Boom! Boom!*

“…”

I stared blankly at the wreckage of my bedroom. Jin Wikyung had gotten way too into the story.

Wipeng had already backed far away and was mouthing something.

—It would be best not to bring that story up again.

For the first time, the two of us were in complete agreement.

Jin Wikyung huffed and puffed for a long while before he finally calmed dow—

“If that bastard had still been alive, he wouldn’t have died peacefully.”

*Crunch.*

I watched with sad eyes as the corner of the bed crumbled into powder. Wipeng shook his head.

“My lord. Please calm down. The Young Master seems anxious.”

That one actually worked. Seeing me sitting there sadly, wrapped in bandages from head to toe, Jin Wikyung’s eyes reddened.

“Just look at my baby brother. How much has this child suffered, to be sitting there so out of it?”

*Grab!*

A hand the size of a cauldron lid seized my shoulder and yanked me in. I was a fairly big guy myself, but this man was practically a small ogre. Crushed against his broad chest, I trembled in fear.

“There, little brother. It’s all right now. It’s all right.”

After a heartfelt hug that only he found moving, Jin Wikyung sniffed.

“I thought you’d be a child forever… but you’ve grown up now. Wipeng, did you know?”

Wipeng answered without even taking a breath.

“Yes. You don’t need to tell me.”

Of course, Jin Wikyung pretended not to hear him.

“Rumors have spread throughout our family and even through the streets. The tale of the hero who led a death squad in a raid on the enemy camp, defeated Jopil, One Question, One Kill, and one hundred wandering martial artists, and rescued the Sakju Branch’s household.”

“Wow. That’s amaz—wait, what?”

I blinked.

*Hold on. That was my story?*

“Um, I think there’s been some misunderstanding.”

“That’s right, my lord. There seems to have been some misunder—”

Jin Wikyung smiled, pleased.

“Our little brother is modest, too. Wipeng, you shut your mouth.”

“No, it isn’t modesty. I think the rumor has been distorted a little.”

“That’s right. I know you care for the Young Master, my lord, but this is going too far. If the rumor gets too far-fetched, people won’t beli—”

“Rumor? Far-fetched?”

*BOOM!*

Wipeng’s voice vanished under the thunderous crash. I stared with my mouth hanging open at the hole blown through my bedroom wall.

*What the hell are you doing, you lunatic?*

Jin Wikyung threw another punch. With a sound like compressed air bursting, what was left of the wall came down.

Wood and bricks rained from the two-story pavilion, and the people outside started shouting.

“It’s the Third Young Master! The Third Young Mas—his residence is collapsing!”

“Get people over here! Hurry!”

While everyone was still stuck in shock, Jin Wikyung hoisted me into the air.

*Put me down. Put me down, you crazy bastard!*

I struggled with all my strength, but there was no fighting him off. One step. One step. Every step toward the gaping wall sent terror through me.

*He’s going to drop me!*

More than fifty people had gathered below. It was two stories in name, but the pavilion was so huge the drop was a good ten meters. The wind coming through made me dizzy.

*If I fall, that’s a fracture at the very least.*

Even with a chill running down my spine, people kept packing in. More than fifty of them had their heads cranked back, looking up at us.

“Who is that? Wasn’t there an accident?”

“That’s the Lesser Family Head, isn’t it? Who’s he holding?”

“The Third Young Master. It’s the Third Young Master!”

Someone’s shout sent a stir through the crowd.

“The Third Young Master—no, the Third Young Master, sir?”

“The Third Young Master who defeated Jopil, One Question, One Kill, has awakened!”

*What is this situation?*

While my eyes and ears were still whipping around, a solemn voice rang out clearly.

“Can you see?”

“Ah, yes, I can see. Could you put me down—”

“Can you hear?”

“I can hear too, but first, could you—”

“What do you feel?”

“Embarrassment. And shame.”

“They believe in you. They’re calling your name!”

“No, you fucking bastard.”

That last curse vanished, swallowed by the crowd’s shouts.

“Third Young Master! Third Young Master!”

Dozens more had shown up in that brief interval. Countless eyes came flying at me and stuck.

*No, what is this?*

Then, with a solemn face, Jin Wikyung shoved his hands into my armpits and lifted me high.

Right on cue, a thunderous cheer erupted.

“Woooooo!”

“Third Young Master! Jin Taekyung!”

“Sleeping Dragon of Shanxi! Sleeping Dragon of Shanxi!”

And then…

*Fuck. What is this, a baby lion?*

An old cartoon’s BGM rang in my ears.

[^1]: In Korean, “crossing the River Jordan” is a euphemism for dying; Taekyung twists it into taking a half-bath.
## Chapter artifact 33

# Chapter 33

“Please kill me.”

A young man with disheveled hair, covered in blood and dust, dropped to his knees. His name was Lee Seogwang—the elder brother of the late Lee Seogeun and the Young Sect Leader of the Mount Heng Sword Sect.

“Report. From your own mouth.”

The cold voice froze everyone inside the tent. Every last one of them was a senior of the Mount Heng Sword Sect, a master who had spent long years roaming the martial world.

Yet even they had to bow their heads before one man.

“Father…”

“That isn’t the answer I want.”

The Blood Wolf Sword, Lee Cheonbaek, did not even turn around. Lee Seogwang forced the words out in a trembling voice.

“The only survivors are twenty-three of us, including me. We have no idea whether the rest are alive or dead.”

A heavy silence settled over those present.

Some two hundred troops had been killed or captured, and they had lost three Peak masters. That alone would have made it hard to avoid punishment, but there was a bigger problem still.

“What orders were you given?”

“…To wipe out the Jin Family of Taiyuan’s branches and advance as far as Jeongyang.”

“And after that?”

“To blockade the road and wait for the main force to join us.”

“Why did you push as far as Honju?”

“Intelligence—I obtained intelligence.”

“Intelligence?”

“Yes. They said Jopil, One Question, One Kill, had chased Jin Taekyung all the way to Honju and captured him. But…”

“He must have said the Jin Family of Taiyuan’s pursuit party was on his heels and asked you to help him.”

Lee Seogwang lowered his head, and Lee Cheonbaek let out a hollow laugh.

“Who delivered that information?”

“A wandering martial artist under Jopil.”

“Do you still think that?”

“…No.”

Smack!

Lee Seogwang’s head snapped to the side. Lee Cheonbaek’s gaze poured down on him like fire.

“Be grateful you were born my son.”

In the end, Lee Seogwang was ordered back to the Mount Heng Sword Sect, and with his withdrawal, the matter was settled for now. It was time to look at reality with a cool head.

“What is the situation?”

“We lost two hundred men, but more than half of them were wandering martial artists we scraped together in a hurry. The damage isn’t as bad as it sounds. The problem is…”

“We lost three Peak masters.”

It left a bitter taste in Lee Cheonbaek’s mouth. The Mount Heng Twin Devils, who had stood with him for twenty years. And Jopil, whom he had paid a fortune to hire, was dead as well.

A Peak master was someone who could change the course of a battle. Somehow, they had to fill the void.

“Gather more. Buy wandering martial artists from the black market, hire mounted bandits—use whatever means necessary.”

“The expense is already too high. By now, word of what happened in Honju will have spread, so they’ll try to drive their prices up.”

“They aren’t trustworthy men, either. Especially the mounted bandits. Aren’t they human butchers? If we hire people like that, our sect’s reputation will suffer afterward…”

Lee Cheonbaek did not even blink.

“All the better. Hire them all.”

“Sect Leader!”

“There are no fewer than five hundred men gathered here. We have more than twice their numbers, and we aren’t behind in Peak masters either.”

“My son thought the same thing. Then he got utterly wrecked in Honju.”

“That was…”

“Don’t worry about whether they’re human butchers or anything else. Throw everything we have into this. If we lose this war, it won’t be our reputation we lose—it’ll be our lives!”

At Lee Cheonbaek’s thunderous command, the seniors realized persuasion was pointless. That did not mean the discussion was over.

“The martial artists’ morale is in shambles.”

“The defeat at Honju is one thing, but they’re shaken by the news that Jin Taekyung killed Jopil, One Question, One Kill.”

Jin Taekyung.

Hearing the name of his enemy made Lee Cheonbaek’s stomach churn.

*Are there really people stupid enough to believe a rumor that dumb?*

As if it weren’t enough that that pathetic fool Jin Taekyung had poisoned his son, now he had supposedly killed a Peak master too. The scheme was obvious. Lee Cheonbaek’s teeth clenched at the Jin Family of Taiyuan’s despicable tactics.

“Find everyone spreading that kind of nonsense. Don’t miss a single one!”

If he took a few heads as examples, morale might drop, but he could keep the army from collapsing. Now was the time to clamp down and push forward.

“Three days. In three days, we march on Taiyuan!”

That was how the debts and grudges of Murim worked. The chain of debts and grudges would not break until one of the two sides fell.

*I’ll take everything from you. Just as you did.*

* * *

“What an incredible recovery.”

The physician was astounded. It was my second day since I’d come to. Overnight, the scabs had fallen away, and pale new skin had grown in.

“In ten years as a physician, this is the first time I’ve seen anything like this.”

Even to me, the speed of it was astonishing. The flesh melted by the heat of Flame Divine Palm, the fractured bones, the deep sword wounds—there was no trace of them left.

Oh, and the internal injuries too.

*Must be the effect of leveling up.*

There was only one method in the real world that produced a similar result.

Healing magic used by the tiny handful of Hunters known as healers.

*Is complete healing too much to ask?*

I was a little disappointed, but it was just as well. If a single level-up had healed every wound on my body, it would have been hard to dodge suspicion.

Even now, the physician kept stealing glances at me like I was a monster.

“Heavens. How bizarre. It’s far too much to pin on the effects of hundred-year snow ginseng…”

“Hundred-year snow ginseng?”

I remembered seeing something like it in martial arts novels. Ginseng that had grown for a hundred years, or whatever.

*Why is that suddenly coming up?*

Seeing how lost I looked, the physician explained. He was one of the few NPCs who knew I had lost my memory.

“Around this time last year, the Medicine King Hall’s storeroom was robbed.”

Ah. The moment he said it, I understood.

The stolen medicinals must have included hundred-year snow ginseng, and the culprit was obviously…

“The Medicine King Hall Leader was absolutely furious.”

The physician gave me an awkward smile.

“It isn’t something you can get just because you have money, after all. You stole an elixir that can grant twenty years of internal energy in a single dose and consumed it.”

“Twenty years of internal energy?”

Something clicked. The third internal energy that had refused to obey me.

*So that was it.*

At the same time, I felt a pang of regret. At the last moment, when I used the Skill, most of the twenty years of internal energy from the hundred-year snow ginseng had vanished.

It had been a complete disaster, because the energy had run wild instead of following my control.

*I used it as a one-time item.*

The physician misread the look on my face and hurriedly added,

“Of course, Young Master, you must have made that decision for some grand purpose.”

*Grand purpose, my ass. I probably ate it as a tonic.*

The snow ginseng’s internal energy had kept me alive, but it was still a waste.

A waste so bad it was killing me.

“You’ve almost completely recovered, so you shouldn’t have any trouble moving around. Then I’ll be on my way.”

The moment the physician hurried out, I opened the System window.

*Open Status Window.*

Ding.

> **System**
>
> **Status Window**
>
> **Lv. 30 Jin Taekyung**
>
> **Class:** Second Rate Martial Artist
>
> **Fame:** 410
>
> **Titles:** 4 (Title effects active)
>
> — **Scion of a Prestigious Family** (All stats +5, Fame +50)
>
> — **Family Shame** (All stats −5, Fame −50)
>
> — **Novice Trainee** (Training speed +10%)
>
> — **Gambler** (Combat-related stats increased by 10% in a one-on-one fight)
>
> **Strength:** 115 **Stamina:** 120
>
> **Agility:** 116 **Intelligence:** 15
>
> **Charm:** 15 **Internal Energy:** 15 years
>
> **Remaining Points:** 0

The moment I saw it, pride welled up.

*I’ve grown a lot.*

It felt like only yesterday I’d been shaking in front of some two-bit bandits. Now I was a master in my own right. My Level had jumped after I took down Jopil, and I’d gained a massive amount of Fame.

That wasn’t all. I’d absorbed some of the hundred-year snow ginseng’s leftover energy and gained another four years of internal energy. On top of that…

> **System**
>
> **Skill Window**
>
> **One Flash**
>
> **Grade:** Peak
>
> **Realm:** Second Stage
>
> **Restriction:** Jin Taekyung
>
> **Effect:** Consumes Stamina and internal energy to deliver a powerful strike. Depending on the amount used, the user enters a helpless state for a certain period of time.

I had a new martial art—or rather, a new Skill.

But it was very different from my Skills in the real world.

*I can adjust how much it consumes, and how much power it puts out.*

Thrust with All My Might. This Skill, now named One Flash, couldn’t be spammed. It could put out destructive power several stages above my usual level for an instant, but that single blow burned through all my strength.

*No. Maybe it was always a Skill you could adjust.*

In the real world, I was an F-rank Hunter. My physical abilities and the mana in my body were pathetic. But this game—Murim—was different.

Here I was a martial artist with fifteen years of internal energy and a body better than NPCs with a twenty- or thirty-Level gap. Change the vessel that holds the power, and the Skill’s original range of use comes out.

*I’ve gotten stronger again.*

It felt like only yesterday Hyuk Mujin had been wiping the floor with me while I learned martial arts. Now I’d taken down a Peak master.

Outside the window, they chanted my name several times a day.

Sleeping Dragon of Shanxi, hero of the family, that sort of thing.

*A hero.*

I never thought I’d hear a word like that in my life. For a two-bit F-rank Hunter whose motto was safety first, it was a word that had never had anything to do with me.

I lay still and fidgeted with my hands. Palms that had once been a young master’s—white and soft—were now packed tight with calluses.

*With these hands, I took down Jopil.*

All told, the people I’d taken down numbered more than a few dozen. Bandits, wandering martial artists, even people rated as First Rate—and I had survived. I’d even taken down a Peak master I thought I could never beat: Jopil, One Question, One Kill.

I suddenly remembered something Wipeng had said.

*The one who survives is strong.*

If he was right, I was definitely strong. I’d survived every enemy I’d faced so far, and they were calling me a hero.

Yes. If I’m being honest…

*It doesn’t feel bad.*

The real-world me was pitiful.

I ate and slept in a one-room goshiwon barely ten square meters across,[^1] the breadwinner who had to support my family. I couldn’t become a hero, and I didn’t want to.

I was just Jin Taekyung, a bottom-rung Hunter who fought every day praying he’d survive.

That was me.

*But in this game, I’m different.*

I’d done a lot of things F-rank Hunter Jin Taekyung could never do. At the very least… I could protect the people who trusted and followed me from the enemy. People acknowledged me. They called me a hero.

Even if everything here was nothing but virtual, even if the people in front of me were NPCs, that fact didn’t change.

Thinking that, I suddenly laughed.

*This is why games are scary.*

Was this game addiction?

Without realizing it, I’d found that I was enjoying living as Jin Taekyung, a martial artist of Murim. Because this was a game. Because it could turn every impossibility into a possibility.

But now it was time to leave.

Back to that place packed with impossibilities—the real world. My family was there. The real me was there.

*Check Quest Window.*

Ding.

> **System**
>
> **Quest**
>
> **Logout**
>
> Now you must make your way through this harsh Murim.
>
> Become stronger and more famous.
>
> For the day that will eventually come…
>
> **Grade:** Main Quest
>
> **Restriction:** Jin Taekyung
>
> **Objective:** Achieve the **First Rate** realm (Incomplete)  
>        Achieve **Lv. 30** (Complete)  
>        Achieve **Fame 500** (410/500)
>
> **Reward:** **Logout**

Logout.

The moment I saw those four glittering characters, my breath caught.

Only two conditions left before I could log out. Time could take care of Fame. The more rumors about me spread, the more it would keep climbing.

The problem was something else.

“First Rate.”

What did I even need to become First Rate?

If it wasn’t Level, stats, or Fame, then…

*Internal energy? Or do I need to raise the realm of my martial arts further?*

Just then, a polite voice came from outside the door.

“Young Master. The Lesser Family Head is looking for you.”

“Ah.”

Right. When you don’t know something, the best thing to do is ask.

And for that, Peak master Jin Wikyung was the best private tutor I could get.

[^1]: A goshiwon is a tiny, inexpensive room-for-rent housing arrangement.
## Chapter artifact 34

# Chapter 34

Once, while Jinho hyung and I were watching TV, we had a conversation like this.

“That’s him, right? Han Seongjin.”

“You know Han Seongjin?”

“Wouldn’t it be weird if I didn’t? Turn on the TV and his face is right there. I’ve seen him so much he feels like family now.”

“Watch your mouth. That’s defamation.”

“Son of a bitch.”

On the screen, a handsome man with a lanky build was smiling brightly. Dozens of cameras and a huge crowd reacted to his every move. Flashes and screams kept going off without a pause.

“He’s got it all. An A-rank Hunter is basically a walking mid-size company, isn’t he? Model proportions and a celebrity face on top of that? That’s just cheating. How old did you say he was?”

“I think he’s the same age as me.”

“…Hang in there.”

No matter the job, there were people who made good money and people who didn’t. And no profession had a wider gap than Hunters.

“Don’t worry, man. If you wait a little longer, your day will come.”

“How long do I have to wait?”

“Try waiting another hundred years. It’ll be possible in your next life.”

I wanted to show Jinho hyung—the one who’d snickered while he teased me back then—what I looked like now.

*I wonder what kind of face he’d make if he saw this.*

With every step I took, dozens of people swarmed after me. NPCs from the Jin Family of Taiyuan, men and women of all ages, were looking at me with shining eyes.

*Is this how famous people always feel?*

People’s attention. Those admiring looks were burdensome, and yet a little enjoyable.

It was the moment I finally understood that common game-promo line: *Awaiting a new hero!*

*Yeah. It’s almost over. Might as well enjoy it.*

I waved with a smile, and a roar went up. Trailing a crowd that only kept growing, I arrived at the main hall they used for meetings.

“They’re waiting for you.”

The martial artist’s face looked familiar. He was the same man who had looked at me with contempt when Lee Seogeun came to see me last time.

*Has it been about fifteen days?*

Just as I was different from the person I had been then, so was he. He made an extremely respectful fist-and-palm salute and threw the door open.

* * *

The main hall looked exactly as I remembered it. The large table in the center and the scattered chairs on either side showed that a meeting had just ended.

“You’ve come?”

Jin Wikyung, seated at the head of the table, gave me a tired smile. He was the only person in the spacious hall.

“Where’s Wipeng?”

“He’ll be back shortly.”

Once I sat down, Jin Wikyung got straight to the point.

“The Lower District Sect has contacted us. It seems the Mount Heng Sword Sect is rounding up troops however they can.”

*They must be shitting bricks over there.*

I didn’t know war, but I knew combat. And war was what you got when battles piled up. Having already lost so many martial artists and so much morale in one crushing defeat, the enemy would throw everything they had into the next battle.

“It’ll be a difficult fight.”

“They’ve poured the entire wealth of their sect into this. If the reinforcements join the main force led by the Blood Wolf Sword, they’ll number around a thousand.”

“A thousand…”

That was an insane number. I’d never been in a battle on that scale, and I had no desire to.

Jin Wikyung continued with a grim expression.

“We’ll march north with every force we have. The plan is to strike the enemy’s main force before it joins the reinforcements.”

“When is that?”

“In two days.”

*Goddammit. That’s filthy fast.*

The race against time wasn’t happening only between the Jin Family of Taiyuan and the Mount Heng Sword Sect. It was happening to me, too.

*Can I log out by then?*

If I became First Rate within two days, I could log out. But what if I didn’t? I’d have to fight my head off all over again.

*Then I’d be completely screwed.*

Jin Wikyung spoke again.

“I’d like you to take charge of the rear guard.”

*Can’t. Won’t.*

I barely swallowed the words that tried to leap out on reflex.

Jin Wikyung’s face was more serious than I’d ever seen it.

“This is a fight our family is staking everything on. Your presence alone will raise morale a great deal.”

“…”

I was still debating whether to accept when he continued.

“Fortunately, the Five Gates of Shanxi have agreed to help us. Move with some of them in the rear guard.”

“The Five Gates of Shanxi?”

“An alliance of five small and mid-sized sects. We’ve always been on good terms with them.”

“…I see.”

“Then will you take charge of the rear guard?”

Ding.

> **System**
>
> **Quest**
>
> **Rear Guard Defense**
>
> Jin Wikyung has proposed that you take charge of the rear guard.
>
> If you accept this mission, the martial artists will praise your will and courage.
>
> **Type:** Short-Term Quest
>
> **Grade:** Second Rate
>
> **Restriction:** Jin Taekyung
>
> **Objective:** Accept the proposal (Incomplete)
>
> **Reward:** Fame +10
>
> **Failure:** Fame −10

I answered without giving it any more thought.

“I will.”

A message appeared saying the Quest had succeeded and my Fame had increased.

*Fame drops if I refuse?*

The Quest Window had made me an offer I couldn’t refuse. It was ridiculous, but a strange relief spread through me all the same.

*Relief? Have I actually lost my mind?*

While I was berating myself for being a game addict, Jin Wikyung smiled broadly.

“It’s a relief to have you here.”

He was smiling, but an invisible shadow hung over his face.

Being buried under stacks of paperwork all day hadn’t been enough. Now there was a war, too. Commanding the enormous Jin Family of Taiyuan had to be a heavy burden even for him.

*He said two days.*

Two powers that split a region between them were about to collide. The Jin Family of Taiyuan was short on martial artists, so even if we threw everything we had into it, we’d still be at a disadvantage.

*Can we win?*

I forced the thought aside.

*Live or die, what do I care?*

The march was in two days, and it would take several more days before the battle actually began. Whoever won, I wouldn’t be here by the time the victor was decided.

Now it was time to hear what I needed to know.

“Um, there’s something I’m curious about.”

“Ask.”

“I’m still stuck at the Second Rate realm…”

After hearing me out, Jin Wikyung tilted his head.

“You’re Second Rate?”

His tone made it clear that he couldn’t understand it at all. I had literally wiped the floor with Lee Seogeun and even brought down Jopil. Jin Wikyung had taken me for First Rate for a long time, and so had Jopil.

“Yes. My realm just won’t rise, so I wanted to ask your advice.”

“Advice…”

Jin Wikyung thought for a moment before speaking.

“You’re already First Rate.”

“But I’m Second Rate.”

“I’m telling you, you’re First Rate. Not just that—you’re a Super First Rate martial artist who’s run into the wall of Peak.”

“No, I really am Second Rate…”

“Who told you that?”

*Ugh, this is driving me crazy.*

I wanted to show him the System Window. It plainly said Second Rate, but I was the only one who knew that, and the frustration was killing me.

I answered with a sigh.

“No one told me I was Second Rate.”

“Then?”

“It’s just… I’m just Second Rate, so it’s a little hard to explain.”

“Do you believe you’re Second Rate?”

“Yes.”

“Then it’s simple.”

“Wh-what is?”

*Is he finally going to reveal the secret to advancing realms?*

I looked at Jin Wikyung, eyes full of anticipation, but he didn’t open his mouth. Instead, he dipped a finger into the tea that had gone cold and brought it to the table.

Ssssk.

A single character appeared.

信

*信? The character for ‘believe’?*

After checking my face, Jin Wikyung let out a short laugh.

“You look like you’ve just been slapped.”

“…You must be mistaken.”

*More like I look like I want to slap you.*

“What is this?”

“Exactly what it says. Believe in yourself.”

“What does that have to do with advancing realms?”

“Because martial arts begin with belief.”

*They begin with belief.*

It sounded like pie in the sky. But from the moment I heard those words, my heart was pounding.

*They begin with belief…*

Strangely, that one sentence kept circling through my mind, spinning round and round until I was dizzy.

*What had I been believing in all this time?*

The first word that came to mind—and the only one—was the System.

The thing that had helped me most in this game, and had always told me nothing but absolute fact.

I had thought of myself as Second Rate because the System had told me I was Second Rate.

*Because I believed in the System.*

I had already overwhelmed Lee Seogeun, a First Rate master. I had taken down more than twenty wandering martial artists by myself, and I had even brought down Jopil, a Peak master.

Everyone praised me as a First Rate master and a hero, but I was still Second Rate.

Because I had believed in the System instead of myself.

But now I understood.

*I’m already First Rate.*

Already. Maybe I had been for a long time.

I was First Rate.

“You look like you’ve just been slapped.”

This time, Jin Wikyung was right. I slumped against the back of my chair, looking completely out of it.

*What a dumbass.*

If I couldn’t even believe in myself, I was Second Rate. No. I *had been* Second Rate.

Ding.

> **System**
>
> — You have reached the **First Rate** realm!
>
> — The realm of all martial arts increases by one stage!
>
> — Your Sinews and Bones and your Meridians improve greatly!
>
> — The size of your dantian expands!
>
> — Level Up!
>
> — Level Up!

From Third Rate to Second Rate. Then from Second Rate to First Rate.

I felt power surge from deep within my body, and Jin Wikyung burst out laughing.

“What happened?”

Wipeng showed up late and asked, looking bewildered.

* * *

It felt like a blocked nose had blown clear. Reaching First Rate had brought a tremendous leap in every way—senses, martial arts, everything.

I left the main hall and started walking. The wind felt refreshing.

“It’s the Third Young Master.”

“Has he fully recovered?”

Sure enough, people’s eyes gathered. I changed direction toward a place with even more people.

*Anyone watching would take me for an attention hog.*

But everything happens for a reason.

Ding.

> **System**
>
> — Someone gazes at you with awe.
>
> — Fame increases by 1.
>
> — Someone is impressed after hearing your rumors.
>
> — Fame increases by 1.

As I walked, the crowd gathered like clouds. Plenty of NPCs in unfamiliar clothing were mixed in among them.

*Who are they?*

My eyes met one of them. The young man looked a little over twenty. He flinched in surprise, then quickly approached and made a fist-and-palm salute.

“Guo of the Three Paths Sect presents his respects.”[^1]

“Ah, yes.”

The fist-and-palm salute now came out on reflex and looked fairly convincing. But where was the Three Paths Sect?

*Oh. Could it be…?*

“Are you with the Five Gates of Shanxi?”

Guo Whatsisname nodded hard.

“That is correct. Our Three Paths Sect has agreed to lend its strength to the Jin Family of Taiyuan. I, Guo, could not be more delighted to offer even the smallest assistance.”

In a situation like this, he was reinforcements worth their weight in gold. I grabbed Guo Whatsisname’s hand, hoping he would fight hard enough for my share as well.

“Thank you for coming.”

“Don’t mention it. It is merely an honor to be included in the Young Master’s tales of martial prowess.”

> **System**
>
> — Someone is impressed after hearing your rumors.
>
> — Fame increases by 1.

A complete stranger had come all this way to fight for us, and he was even helping my Fame climb. I offered my warm thanks to the freely giving Guo Whatsisname.

“God bless you.”

“Pardon?”

“It means I hope the Jade Emperor’s blessing will be with you.”

“Ahh. Thank you. Gapburaesuyu.”

“Ah. Yes.”

I put on a fake smile and kept walking. Maybe because everyone who needed to know already did, the Jin Family of Taiyuan’s people no longer raised my Fame.

*Still, I’d piled up quite a bit.*

I opened the Status Window and saw that I was about fifty short of the target. If I grinded hard for just two more days, maybe I could log out.

“Um, Young Hero Jin.”

I turned around. It was the fellow from the Three Paths Sect. He looked ready to follow me to the ends of the earth.

“If you aren’t busy, perhaps we could have some tea together…”

“I’m sorry. I have somewhere to be.”

It sounded like a lie, but it was the truth. My destination had been decided from the start.

I pointed out a building to him as he looked disappointed. A faded signboard hung there, and the smell of medicinal decoctions rolled out thick.

Medicine King Hall.

And beneath it hung a small wooden plaque.

**No Entry Except for Authorized Personnel.**

The people surrounding me let out pitying sighs.

[^1]: The given characters are 三道問, with 問 (“question”), not the usual 門 (“gate”/“sect”).
