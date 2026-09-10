# Checkpoint Review — 35–39

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

# Chapters 35–39

## Plot

Taekyung visits Hyuk Mujin, Han Yeop, Gong Yacheong, Socheon, Soyul, and the injured reconnaissance squad before the Jin Family’s march. Hyuk and Han, both alive but seriously injured, vow to surpass Jopil and catch up to Taekyung. Gong returns Jopil’s possessions: the Supreme Peak **Flame Divine Palm** manual, the dangerous **Fire Divine Elixir**, and a mysterious **Nameless Sword** forged from ten-thousand-year cold iron.

Taekyung’s Fame reaches 475/500, then stalls. He commands the rear guard as the Jin Family and its allies march north. Jin Wikyung predicts victory within three days but privately tells Taekyung to survive and flee if the family loses, so Taekyung and Jin Mukyung can preserve its future. The exhausted Mount Heng reinforcements cross Mount Otae, and Wikyung plans to force the enemy through narrow Eight Spring Gorge, where the Jin Family has hidden roughly one hundred horn bows.

At Honju, Gwak Jun, the supposedly allied Level 40 leader of the Three Paths Sect, reveals that he and twenty black-clad fighters are First Rate assassins. A herd of water deer disrupts their ambush, triggering Taekyung’s solo **Slay the Assassins** Quest. Taekyung and the reconnaissance squad defeat the assassins through formation tactics and Taekyung’s use of Inventory weapons and **One Flash**. Gwak is captured but dies after severing his own heart meridian. He reveals that the Three Paths Sect was founded thirty years earlier according to an unidentified person’s will.

The System grants Taekyung 50 Fame and a level-up, raising him to 547/500 Fame and starting the three-second Logout countdown. He loses consciousness but successfully logs out. Thirty days in Murim correspond to only three hours in reality. Taekyung wakes in the unplugged Ark - 2020 capsule with Seong Jinho, who dismisses his account as insanity. The manual identifies H Soft as the manufacturer and states that the registered user is permanently bound until death, that reality and game time can pass at an adjustable slow ratio, and that **Character Synchronization** is a key feature. The capsule’s origin and connection to Murim remain unexplained.

## Continuity

- Taekyung is First Rate, Lv. 33 after the assassin Quest, with 547 Fame; Logout has succeeded, but the System is unavailable in reality.
- Taekyung possesses Jopil’s **Flame Divine Palm** manual, **Fire Divine Elixir**, and **Nameless Sword** in his Inventory. The manual requires Scorching Yang Qi; the elixir contains dangerous fire qi and grants thirty years of internal energy; the sword’s special power is unknown.
- Hyuk Mujin and Han Yeop survived Jopil’s attack. Han remains hospitalized with unhealed internal injuries; Hyuk’s internal injuries heal, but he joins the march despite serious external injuries.
- Taekyung commands the Jin Family rear guard. The broader war is expected to involve roughly fifteen hundred martial artists, with the Jin Family and allies moving to Eight Spring Gorge and Mount Heng’s forces approaching Jeongyang.
- Gwak Jun and the twenty infiltrators were assassins impersonating the Three Paths Sect. The real sect was established thirty years ago according to an unidentified conspirator’s will. More than one hundred suspected allied fighters came from the Three Paths Sect and Gunggwimun.
- Taekyung suspects the Head Elder has betrayed the Jin Family and assembled its strength to seize Shanxi. The Head Elder’s Sound Transmission accomplice, the infiltrators’ full chain of command, and the wider plan remain unresolved.
- Taekyung remembers Murim and its inhabitants as real. The capsule’s purpose, Character Synchronization, permanent user binding, route back to Murim, and the limits of death and resurrection remain unresolved.
- Seong Jinho currently believes Taekyung is mentally ill. The capsule was unplugged when Taekyung returned, despite the completed Murim experience.
- The manual’s observed time ratio is thirty days in Murim to three hours in reality; it describes the ratio only as adjustable and reversible.

## Translation Decisions

- Preserve **Flame Divine Palm**, **Fire Divine Elixir**, **Nameless Sword**, **One Flash**, **Slay the Assassins**, **Fame**, **Logout**, **Inventory**, **First Rate**, **Peak**, and **Character Synchronization** as established terminology.
- Keep **Three Paths Sect**, **Gunggwimun**, **Eight Spring Gorge**, **Mount Otae**, **Honju**, **Sound Transmission**, and **rear guard** consistent with prior chapters.
- Preserve the abrupt water-deer interruption, the reconnaissance squad’s drilled teamwork, Taekyung’s violent dark comedy, and the cliffhanger transition between Murim and reality.
- Render the capsule’s displayed forms exactly as **Ark - 2020** and **H Soft**.
- Retain Taekyung’s dry, self-mocking first-person voice and the blunt informal exchange with Seong Jinho.

## Durable state

{
  "version": 1,
  "safe_through": 39,
  "continuity_sources": [38, 39],
  "active_continuity": [
    "Jin Taekyung is trapped in Murim through an old game capsule; death is presented as permanent and he cannot log out at will.",
    "Taekyung is the disgraced third son of the Jin Family of Taiyuan and narrates with dry, self-mocking, occasionally profane humor.",
    "Logout is the Main Quest reward for reaching First Rate, Lv. 30, and 500 Fame. Taekyung is Lv. 32, has fifteen years of internal energy, and is First Rate; only the Fame 500 requirement remains incomplete, with his total at 497/500.",
    "Taekyung's Jin Family's Cultivation Technique is at the Fifth Stage; his Spear and Manoeuvre Techniques are at the Sixth Stage, and his Fourth-Stage Qi Sense detects targets through Lv. 50.",
    "Taekyung has the Gambler Title, which increases combat stats by 10% in a one-on-one fight; it does not apply when allies join the fight.",
    "The hardened third internal energy came from the hundred-year snow ginseng. It awakened during the mortal danger in Chapter 30, and most of the ginseng-granted energy was consumed by Taekyung's final Skill use; his current internal-energy total is fifteen years.",
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
    "Taekyung was unconscious for five days after killing Jopil; the Medicine King Hall Leader had expected him to die within a day.",
    "The reconnaissance squad and the Sakju Branch survivors returned safely. Two people suffered serious injuries, but no lives are in danger.",
    "Wipeng urged Taekyung to remember the dead and live their share as well; Wipeng’s own dream is to become Number One Under Heaven.",
    "Two days before Taekyung wakes, one hundred Jin Family elites defeat two hundred Mount Heng vanguard troops at Honju; fewer than thirty Mount Heng fighters escape, and Jin Family casualties are similar in number.",
    "Taekyung checks the System after recovering: he is Lv. 30, has Fame 410 and fifteen years of internal energy, and remains Second Rate. Thrust with All My Might has become the Peak, Second-Stage Skill One Flash, whose stamina and internal-energy cost can be adjusted but which can leave him helpless.",
    "Lee Seogwang is Lee Cheonbaek's son and the Young Sect Leader of Mount Heng. He returns from Honju with twenty-three survivors, including himself, after more than two hundred Mount Heng troops and three Peak masters are lost.",
    "Lee Cheonbaek has five hundred men assembled, plans to march on Taiyuan in three days, and is willing to hire wandering martial artists, black-market fighters, and mounted bandits while suppressing rumors that Taekyung killed Jopil.",
    "Taekyung recovers from Jopil's attack in two days. The hundred-year snow ginseng granted twenty years of internal energy, but most of it was consumed by his final Skill use.",
    "Taekyung recognizes that he enjoys living as a martial artist in Murim but still wants to return to his family and true self in the real world. Jin Wikyung is the person he intends to ask about reaching First Rate.",
    "Jin Wikyung learns from the Lower District Sect that Mount Heng is gathering troops. The Jin Family will march north with all its forces in two days and strike before the reinforcements join the Blood Wolf Sword's main force, which could then number about one thousand.",
    "The Five Gates of Shanxi is an alliance of five small- and medium-sized sects that has agreed to aid the Jin Family. A representative of its Three Paths Sect introduces himself to Taekyung and pledges support.",
    "Taekyung accepts the Rear Guard Defense short-term Quest after Jin Wikyung asks him to command the rear guard; the System rewards Fame for acceptance and penalizes refusal.",
    "Jin Wikyung tells Taekyung that martial arts begin with belief. Taekyung realizes he has trusted the System's Second Rate label instead of his own achievements and recognizes that he is already First Rate.",
    "Reaching First Rate raises every martial art by one stage, greatly improves Taekyung's Sinews and Bones and Meridians, expands his dantian, and grants two level-ups. He gains Fame from the accepted Quest and public awe and rumors, then goes to Medicine King Hall, where entry is restricted to authorized personnel.",
    "Hyuk Mujin and Han Yeop recover in Medicine King Hall from serious but nonfatal injuries and resolve to become stronger than Jopil and catch up to Taekyung. Han's internal injuries remain unhealed in Chapter 36; Hyuk's internal injuries have healed, but he sneaks out despite serious external injuries to join the march.",
    "Taekyung visits the injured squad members, Gong Yacheong, Socheon, and Soyul before the Jin Family's march; the System shows Fame 475/500, and ordinary family-wide Fame gains have stalled.",
    "Gong Yacheong returns Jopil's Flame Divine Palm manual, Fire Divine Elixir, and Nameless Sword to Taekyung. The manual is Supreme Peak and restricted to a holder of Scorching Yang Qi; the Peak elixir grants thirty years of internal energy but contains dangerous fire qi; the ten-thousand-year cold-iron sword's special power is unknown.",
    "Taekyung stores Jopil's recovered items in his Inventory and gains another point of Fame.",
    "The Head Elder meets an unidentified ally in the garden through Sound Transmission. Their preparations, including troop deployments, are complete; the Head Elder is willing to do anything to become Family Head and Shanxi's sole hegemon.",
    "At the departure ceremony, more than five hundred Jin Family and allied martial artists assemble. The force is divided into vanguard, center, and rear guard; Taekyung commands the rear guard, which contains only a few dozen martial artists.",
    "Jin Wikyung rallies the departing force by predicting victory within three days. The war is expected to pit about fifteen hundred martial artists against one another once both sides commit their forces.",
    "Taekyung asks Jin Wikyung for a reconnaissance mission to gain the remaining Fame, but Wikyung refuses and tells him his mission is to survive; if the family loses, Taekyung should flee so he and Jin Mukyung can become the family's roots.",
    "At Honju, Level 40 Gwak Jun of the Three Paths Sect joins the rear guard; he is fearless, intensely confident, and leads the sect’s martial artists in black robes.",
    "Mount Heng’s exhausted reinforcements have crossed Mount Otae and are low on food. Jin Wikyung plans to seize Jeongyang’s high ground and draw the enemy through narrow Eight Spring Gorge, where about one hundred horn bows are hidden on the cliffs with help from the Lower District Sect.",
    "Taekyung’s Fame is 497/500 for Logout. He stays awake counting the remaining three points, reflects on his month in Murim, and recognizes that the reconnaissance squad’s loyalty feels real.",
    "Taekyung tells the anxious rear guard that he trusts Jin Wikyung, and the squad affirms its trust in Taekyung.",
    "At Honju, Gwak Jun and twenty supposed Three Paths Sect martial artists reveal themselves as First Rate assassins; a herd of water deer breaks their ambush. Taekyung and the reconnaissance squad kill the infiltrators, and Gwak dies after severing his own heart meridian.",
    "Gwak says the Three Paths Sect was established thirty years earlier according to an unidentified conspirator's will. Taekyung suspects the Head Elder united the Jin Family's strength to seize Shanxi; the accomplice and full plan remain unresolved.",
    "The Slay the Assassins Quest completes after Gwak's death, granting 50 Fame and a level-up; Taekyung reaches 547/500 Fame and Logout begins, but he loses consciousness before its result is shown.",
    "Taekyung logs out after exactly thirty days in Murim; only three hours pass in reality. The System is unavailable after logout, and Seong Jinho does not believe Taekyung's account.",
    "The unplugged Ark - 2020 capsule's manual names H Soft as manufacturer and January 1, 2020 as its manufacture date. It says the registered user is permanently bound until death, reality/game time passes at an adjustable slow ratio, and Character Synchronization is a key feature; the capsule's purpose, synchronization, and route home remain unresolved."

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

## Chapter artifact 35

# Chapter 35

A hospital room in Medicine King Hall.

Hyuk Mujin, wound tight in bandages from head to toe, let out a groan.

“I’m dying.”

Han Yeop, lying beside him in much the same shape, answered,

“It’s a miracle we didn’t die.”

“Right?”

“It is.”

A brief silence followed. Both of them were remembering that day.

Jopil’s palm strike. An attack you couldn’t block even if you knew it was coming. The moment he closed his eyes, that bastard’s red-hot palm came back to him. It might become a nightmare that followed him for the rest of his life.

“That monster. How is something like that even possible?”

“He’s a Peak master.”

Unlike the dejected Hyuk Mujin, Han Yeop’s voice was calm.

“Hey, punk. Doesn’t it bother you at all?”

“What?”

“That…”

Hyuk Mujin found himself at a loss for words. Right. Maybe it didn’t have to bother him.

“No, that’s not what I meant…”

“I know.”

“Huh?”

“I know what the deputy squad leader is thinking. I know what you want to say.”

“…”

“When I first came to, a lot of things went through my mind. The relief of being alive. The helplessness I felt that day. The despair over my own martial arts.”

Hyuk Mujin shut his mouth. Han Yeop had it right. Jopil’s Flame Divine Palm had broken bones and torn heart meridians, but the wound he’d taken was somewhere else.

One question had been circling through his head ever since that day.

*Can I reach that realm?*

“Overwhelming” wasn’t enough. All his effort, all his pride in his own martial arts, had been ripped up by the roots.

“You’ve shaken all that off?”

Han Yeop shook his head.

“Then?”

“I admitted that I’m weak. It wasn’t even that hard. I’ve always known. But…”

“…”

“I’ll get stronger. As strong as Jopil. No—far stronger than Jopil.”

Han Yeop went on, his voice firm.

“Thinking about that made me happy. If I become a Peak master, I can get that strong too. Something like that.”

“A Peak master…”

The Peak realm was a domain granted to only a rare few. Coming from Han Yeop, who was barely second- or third-rate, the declaration was almost laughable.

But Hyuk Mujin didn’t sneer.

*You’ve changed. You too.*

So much had changed. The situation. The people.

Even the timid second-rate martial artist had, before anyone noticed, stepped into that current. Hyuk Mujin felt his heart lurch. The next words burst out before he could stop them.

“I’ll get even stronger.”

Han Yeop’s eyes went round, then he flashed a grin.

“You will. First, though, we have to catch up to one person.”

They thought of the same person at the same time. Jin Taekyung. He was already running far ahead of them. What was he doing now?

Behind the two men, lost in thought, the door that had been slightly ajar slid shut.

* * *

I closed the door and turned away, and a shudder ran through me.

“Ugh, shit.”

These idiots were filming a teen coming-of-age drama in a hospital room. I’d stood there quietly listening to hear what they were talking about, and it was quite a spectacle. A real spectacle.

If I’d gone in, I might’ve ended up swearing brotherhood with them.

*Still, I have to admit it’s kind of admirable.*

Hadn’t we shared life and death together, in our own way? Besides, those two had risked their lives to help me. Saying I didn’t feel so much as a shred of affection for them would have been a lie.

*Could this be the last time?*

In two days I would set out in charge of the main force’s rear guard, while those two and the rest of the reconnaissance squad would stay behind at the family as wounded men. And probably…

*By then, I’ll have logged out.*

I was close to the last condition of the Logout Quest: 500 Fame. Today’s visit to Medicine King Hall was a farewell of sorts.

You could call it the nostalgia filter of a sergeant in his last stretch before discharge.

*Well, no need to announce anything. Seeing their faces is enough.*

I’d already given the other reconnaissance-squad members a once-over. I’d seen Han Yeop and Hyuk Mujin too, so if I stopped by just one more place…

Huh?

“Oh!”

A rag doll in one hand. Snacks in the other.

A little girl with her hair tied in a cute ribbon shouted, her eyes round.

“It’s the mind-reading uncle!”

“…”

Couldn’t you call me Big Brother? I gave Soyul a sad little wave.

* * *

“Young Master Jin.”

“Benefactor!”

The moment I entered the room, the reactions came at once. Gong Yacheong, still pale, tried to rise, and I stopped him. Then I pulled Socheon, who had dropped into a full bow, back to his feet.

“Stay lying down. You too, punk. Get up. Do I look old enough to take a bow from you?”

“I’ve received a kindness a hundred bows couldn’t repay.”

Tears were already welling in both their eyes. Soyul, who didn’t understand any of it, hugged her rag doll tight and scampered over to cling to her brother.

“Big brother, did you put on the Benefactor’s kindness? Show me too. Is it pretty?”

*Uh. That’s clothes, isn’t it?*

Leaving the chattering Soyul behind, I spoke to Gong Yacheong.

“How are you feeling?”

“Couldn’t be better. I’ll need to recuperate for a while, though.”

A faint smile spread across Gong Yacheong’s lips.

“It’s all thanks to you, Young Master.”

“I didn’t do it to hear you flatter me. I even left you behind once.”

“That was my choice. And you came back.”

I remembered that night Jopil had been chasing us. Gong Yacheong had been badly poisoned and had wanted to stay behind. Just as he had, I’d had to make a choice.

After a great deal of inner conflict, the decision I reached was to go back for him.

*I regretted it like crazy.*

It had been insane. Gambling my life for a mere NPC in a game. But now I thought I understood why I’d made that choice.

What had I seen in those young siblings who’d lost their parents? Who had Gong Yacheong and the reconnaissance squad reminded me of…?

“Young Master Jin?”

Gong Yacheong’s voice pulled me back.

“It’s nothing. I just—just had something on my mind.”

“Ah, I heard the news as well. Is that what this is about?”

“What news?”

“They say there will be a major battle soon.”

*Wasn’t that military intelligence?*

If Gong Yacheong, who never left his hospital room, knew about it, then anyone in the Jin Family of Taiyuan with eyes and ears already knew.

If there was even one spy among us, we wouldn’t need a loudspeaker aimed at North Korea.

*Is this war really going to be all right like this?*

I waved the thought away. What did it matter to me? Soon enough, it wouldn’t have anything to do with me anyway.

The System alerts ringing even now were proof.

Ding.

> **System**
>
> — Rumors about you continue to spread.
>
> — Fame increases by 1.

They said a rumor traveled a thousand li without feet. After I’d taken Jopil down, my name seemed to have started spreading in earnest.

I cracked the Quest Window open for a look. About fifty Fame left to go.

Logout was as good as decided.

“It will be a battle with our family’s fate at stake.”

Of course they had no way of knowing my situation. I listened quietly to Gong Yacheong and Socheon, then rose from my seat.

“I think I should be going.”

“Benefactor.”

Gong Yacheong was the one who stopped Socheon when the boy looked disappointed.

“Let him go.”

“But…”

“That’s enough.”

Socheon lowered his head glumly. Soyul, who had been playing with the doll by herself, looked up at me with huge eyes.

“You’re leaving already, mister?”

“I said Big Brother.”

“Okay. Mister.”

I gave her chubby cheek a light pinch and was about to turn away when Gong Yacheong called out to me.

“Young Master Jin. You may be leaving, but shouldn’t you take the thing you left behind?”

“The thing I left behind?”

I thought about it for a moment, but there was no way I’d left anything. Thanks to the cheat known as Inventory, my hands were always empty.

“There’s nothing like tha—what is this?”

Gong Yacheong was holding a long bundle.

“You were in no state to collect it. Now that its owner has come, returning it is only right.”

*What is it?*

Still bewildered, I took the bundle. It was fairly heavy. Just as I was about to check what was inside, Gong Yacheong spoke.

“Unwrap it in your quarters. Don’t let anyone else see.”

*Did he put a golden calf in here?*

* * *

I unwrapped the bundle the moment I reached my quarters. Then I understood what Gong Yacheong’s last words had meant.

*These really are the kind of things people would covet if they saw them.*

An old booklet. A small box. And a familiar sword.

To someone in Murim, these were beyond comparison to any golden calf. And I had the ability to judge that value more accurately than anyone.

*Check Item.*

Ding.

> **System**
>
> **Item Window**
>
> **Flame Divine Palm**
>
> **Type:** Martial Arts Manual
>
> **Grade:** Supreme Peak
>
> **Restriction:** Holder of Scorching Yang Qi
>
> **Description:** One of the Fire Gate Clan’s secret techniques. A martial art based on powerful fire qi.
>
> **Effect:** Acquired Flame Divine Palm

> **System**
>
> **Item Window**
>
> **Fire Divine Elixir**
>
> **Type:** Spiritual Elixir
>
> **Grade:** Peak
>
> **Restriction:** None
>
> **Description:** A spiritual elixir made according to the Fire Gate Clan’s secret formula.
>
> **Effect:** Grants thirty years of internal energy when consumed. However, if the user cannot control the powerful fire qi contained within the elixir, they may meet a horrific end.

> **System**
>
> **Item Window**
>
> **Nameless Sword**
>
> **Type:** Sword
>
> **Grade:** None
>
> **Restriction:** None
>
> **Description:** Made of ten-thousand-year cold iron, this sword is exceptionally sharp and durable. After drinking countless amounts of blood over a long time, it changed on its own. Special conditions are required to draw out the sword’s power.
>
> **Effect:** Unknown

“This is insane.”

It really was insane. A Supreme Peak martial arts manual. A spiritual elixir that granted thirty years of internal energy. And a sword I didn’t fully understand, but that looked ridiculously good.

They said a tiger left its pelt behind when it died, but Jopil had left three things like these.

*Shit. It always hands over the good stuff after everything’s over.*

Damn shitty game. If it was going to give me something, it should have done it sooner. Playing catch-up after everything was finished just spiked my blood pressure.

*Still, these items are seriously good.*

Reading the descriptions, I caught myself getting tempted. What if I absorbed the elixir and learned Flame Divine Palm? Fire shooting from my hands like Jopil…

*That would be fucking cool.*

But the thought lasted only a moment. They said that in your last stretch before discharge, you had to watch out even for falling leaves. I didn’t want to swallow the elixir wrong and hold a self-immolation ceremony.

*Remember this. Safety first. Safety first.*

Talking about safety at this point was pretty funny, but I wasn’t stupid enough to just gulp it down.

*It’s almost over.*

One slip and I’d be gone. I stuffed all the items into my Inventory. Somewhere in the dead of night, someone must have been talking about me over drinks, because a System alert rang out.

Ding.

> **System**
>
> — Fame has increased by 1.

* * *

At that hour, the Head Elder was walking through the garden. The date and the place had been agreed upon. In the darkness, the man never failed to keep the time.

“The moon is very bright.”

“So it is.”

As he had said, tonight’s full moon was exceptionally bright.

“When I was young, I really loved the moon… but the older I got, the more I found myself thinking.”

“Thinking what?”

“That I’d rather there were no moon. Something like that.”

“A world without charm.”

“What’s wrong with a little less charm? I make my living at night, so I’d be delighted if the moon disappeared.”

*Night life, huh.*

He ran his mouth in a flippant, cheerful tone like a kept man, but the Head Elder knew the truth. He possessed formidable martial arts, and he was a superb assassin.

The wind seemed to carry the smell of blood.

“Ah, right. How is the work progressing?”

“Smoothly. Even the troop deployments are finished.”

“Don’t overdo it. If the clever Lesser Family Head catches a whiff of it, everything will go wrong.”

“Don’t worry. I didn’t even need to make a move.”

“Heaven is helping us.”

“And your side?”

“You’re asking the obvious.”

The light reproach in his words made the Head Elder fall silent.

*As if it would be otherwise.*

They were like sea fog. Their identities lay hidden under the mist, and even if you reached out and stirred it with your hand, there was no substance to grasp. All that remained was a damp palm and an unpleasant feeling.

*But they have power.*

The power to make him Family Head of the Jin Family of Taiyuan, the sole hegemon of Shanxi. An ambition he had held for half his life. The Head Elder was prepared to do anything.

“All preparations are complete.”

“Mine as well.”

The day the two great sects that divided Shanxi clashed…

Everything would end, and everything would begin anew.
## Chapter artifact 36

# Chapter 36

> **System**
>
> **Quest**
>
> **Logout**
>
> You must now make your way through this harsh Murim.
>
> Become even stronger, and become famous.
>
> For the day that will one day come…
>
> **Grade:** Main Quest
>
> **Restriction:** Jin Taekyung
>
> **Objective:** Reach the **First Rate** realm (Complete)
>
> Reach Lv. 30 (Complete)
>
> Reach Fame 500 (475/500)
>
> **Reward:** Logout

I closed the Quest Window. It was midwinter, and I still felt like I was about to break into a cold sweat.

*If this keeps up, I’m completely screwed.*

The Fame that had been climbing little by little had suddenly stopped dead. That had been half a day ago. I’d bolted from my quarters and shaken hands like a presidential candidate until I was worn to the bone, but the notification I’d been waiting for never came.

*No, I did get a notification.*

> **System**
>
> — There is no one in the Jin Family of Taiyuan who does not know your Fame.

It was the System’s way of telling me I’d already milked Fame to the limit and should knock it off. Even the System seemed to find me pitiful.

And so the day slipped away, and there was nothing I could do about it. Today was the long-awaited departure ceremony.

“Fuck…”

As I muttered the curse under my breath, Jin Wikyung was climbing onto the platform.

Hundreds of pairs of eyes followed him. Martial artists of the Jin Family of Taiyuan, and martial artists from the small and mid-sized sects that had newly joined us. More than five hundred martial artists stood in formation across the main training ground.

Boom. Boom. Boom.

At some point, a tremendous rumble spread through the air. Some stamped their feet; others struck their weapons. When five hundred martial artists with internal energy moved as one, the earth shook and a roar filled heaven and earth.

*What is this…?*

I had never seen anything like it. They had gone from individuals to a single military force, and now they were waiting for one man’s command.

At last, Jin Wikyung spoke.

“I will not deny it. The enemy is ahead of us in troop numbers and in the number of Peak masters.”

Silence dropped over them in an instant. But Jin Wikyung wasn’t foolish enough to kill morale from the opening. The presence pouring off his entire body was proof of that.

“However.”

His usual good-natured smile was gone without a trace. The Jin Wikyung standing before us was both a Peak martial artist and the head of the Jin Family of Taiyuan.

“They are nothing but jackals with numbers on their side. That man’s rabble—wandering martial artists blinded by gold, and a pack of mounted bandits who have plundered the common people!”

The air crackled under a shout that spat fire. Even I felt my blood boil, if only for that moment.

“They have neither cause nor justice.”

Cause. Justice.

The Mount Heng Sword Sect had lost the two most important things in a war.

That was also why the small and mid-sized sects of Shanxi Province, which had only been watching which way the wind blew in the war between two powers, had sent reinforcements.

“This war will be over within three days.”

Fifteen hundred martial artists would clash at the same hour on the same day.

It would be a hellish fight in which they killed and were killed.

“No one here can guarantee whether they will live or die. However…”

Jin Wikyung’s flashing eyes took them all in.

“We will surely win.”

The next moment.

A roar burst out, loud enough to leave my ears ringing. With the mood at its height, Jin Wikyung stood towering like a giant.

“Survival of the fittest! Fight with your lives on the line, and survive!”

The cheering went on for a long time afterward.

* * *

The five hundred troops were divided into vanguard, center, and rear guard. Most of the core fighting strength had been placed in the vanguard and the center, so the rear I’d been given had only a few dozen martial artists.

Some of the faces were fairly familiar.

“Squad Leader!”

They were members of the reconnaissance squad. Half pleased and half puzzled, I asked,

“Why are you guys here? Weren’t you at Medicine King Hall?”

“This is a battle with the fate of our family at stake. We can’t sit it out just because we’re a little injured.”

Last time I’d snuck over to visit, some of them had still had cracked bones in their arms and legs. Murim people really were tough as hell.

“When we asked to be placed under your command, the higher-ups readily approved it. We’ve been walking around with our chests puffed out ever since that day, haha.”

“Well, look at you.”

I let out a short laugh.

I’d spent several days with them on the reconnaissance mission, but I didn’t even know some of their names. Even so, I felt close to them—we’d been through life and death together.

*They say three raids are enough to make sworn brothers.*

Remembering the old Hunter saying, I smiled at the eight reconnaissance-squad members. Then a thought suddenly struck me.

*No, wait.*

Eight? Had I counted wrong?

I started counting again from the end, one person at a time. Not counting me, there were nine. Hyuk Mujin and Han Yeop had serious injuries, so they obviously couldn’t have come—meaning it should have been seven, but…

“…What are you doing here?”

Even looking at him, I wasn’t sure it was the same guy. His face was puffed up like a steamed bun, and the skin showing past his clothes was red and blotchy.

“Can’t you tell by looking?”

He was right. There was only one rude bastard on the reconnaissance squad.

“Hyuk Mujin?”

“Yes. Why? What?”

“Are you really Hyuk Mujin?”

“Can’t you recognize my face anymore?”

*Looking like that, even your parents wouldn’t recognize you…*

No. Before that—why was this bastard here?

“Did you volunteer too?”

“I did.”

He added,

“They didn’t take me, though.”

“Huh?”

“I told the physician, and he got angry and asked if I’d gone insane, wanting to die. So I just snuck out.”

I spoke seriously.

“Have you gone insane, wanting to die?”

“I want to live.”

Hyuk Mujin answered with a look like something had gone sour.

“Then why did you come here?”

“I know my own condition. I can fight well enough.”

“Your face looks like it’s about to burst.”

“The swelling is going down. My internal injuries have all healed, so there’s no problem.”

“What about the external injuries?”

“They’ll heal on the way.”

“…”

“A few bones are cracked, but I can handle i—kh!”

Hyuk Mujin suddenly bent forward at the waist. Startled, I shouted,

“Hey! What’s wrong?”

“Sometimes my chest hurts whenever I breathe… Ah, it’s fine now.”

“…”

Was this guy completely insane?

As I stood there speechless, Hyuk Mujin said,

“Ah, Han Yeop couldn’t come. His internal injuries haven’t healed, so he’d only be a burden. Squad Leader? Squad Leader, you are listening to me, right?”

There was only one thought in my head.

*Logout. Logout is urgent.*

* * *

Winter night came early. After the sun went down, we walked for who knew how long, and only after we entered a wide basin did the order come to prepare camp.

“Ugh, every bone in my body hurts.”

Hyuk Mujin groaned. Since he clearly wasn’t fully recovered, the march seemed to be too much for him.

“It’s not too late. Want to turn back even now?”

“Are you saying that again?”

“I’m saying it because you look like you’re struggling.”

“You’re mistaken. Does Hyuk Mujin the man look like someone who’d get tired from walking a mere half day?”

I nodded without the slightest hesitation.

“Yep.”

“Absolutely not!”

“Hmm. You’re really not tired? You’re fine?”

“Yes.”

“Then go help the others prepare camp.”

At that moment, Hyuk Mujin the man snapped his eyes wide and sank to the ground.

“Ugh, the internal injuries I took from Jopil…”

“…”

*You said your internal injuries had healed, you bastard.*

I was wondering whether I ought to hit him when a voice cut in.

“Is he injured?”

A massive shadow stretched under the moonlight. Hyuk Mujin cautiously lifted his head to see who it was, then his eyes flew open.

“Gasp, Lesser Family Head!”

If Jin Wikyung was a division commander, Hyuk Mujin was a private.

The next moment, Hyuk Mujin sprang to his feet like lightning and stood at attention. Jin Wikyung burst out laughing.

“You still don’t look fully recovered. Lie back down. Ah, the internal injuries do seem fully healed. I’ll vouch for that.”

“Ah, I, that isn’t…”

Jin Wikyung gave the flustered Hyuk Mujin’s shoulder a light pat, then turned to me.

“Shall we walk for a bit?”

I followed Jin Wikyung to a secluded corner. He spoke first.

“How’s your condition?”

“It’s good.”

I’d gotten full use out of the level-up. My body had recovered at a terrifying speed, and distributing my points had made it even stronger.

The problem was something else.

*My Fame isn’t going up.*

No, it was going up. Really, by about a rat dropping. Little by little. Very, very little.

At this rate, I couldn’t guarantee I’d be able to log out before the fighting started.

*If it stayed like this, I mean.*

Jin Wikyung showing up now was convenient. I brought up what I’d been thinking for a while.

“I want to take on a mission.”

His eyes went round at how bluntly I’d come out with it.

“Hm? A mission?”

“Now that I’ve recovered, I want to distinguish myself for our family.”

I was proud of myself. To think I could deliver a line like that—a lie like that—with a straight face.

“I-is that truly what you think?”

“Yes.”

The corners of Jin Wikyung’s eyes trembled. He looked like a wave of emotion was running through his whole body.

*This is actually making me feel kind of guilty.*

The reason I was putting on this unconvincing act was Fame. If I went out on even a reconnaissance mission and distinguished myself, Fame would come in.

It would be even better if I ran into a reconnaissance unit from the Mount Heng Sword Sect. Not only would that be excellent EXP, I’d be able to fill all the Fame I had left.

*Once the real battle starts, it’s over.*

I had to log out, and fast, before then. I spoke in a voice full of resolve.

“Just leave it to me.”

“How could you have thought of something so admirable? Thank you, my youngest brother.”

Jin Wikyung wiped the damp corners of his eyes with his sleeve and went on.

“But no.”

“Then a reconnaissance mission for me, please?”

“I’ll take the sentiment. You guard the rear as you are now.”

*What is he talking about?*

I barely held down the urge to grab him by the collar and shake him.

“I-I really want to distinguish myself.”

“You’ve already done more than enough.”

“No, that’s not what I mean.”

“The merits you’ve earned so far have already been a great help to our family. So don’t trouble yourself over it.”

“I’d like you to give me even one reconnaissance mission. There could be enemies lying in ambush ahead…”

Jin Wikyung laughed softly.

“This is a battle with our family’s fate at stake. Do you think I wouldn’t have accounted for something like that?”

“Might there not be a one-in-ten-thousand chance we missed something?”

“That is, quite literally, one in ten thousand.”

*Damn it.*

Nothing was going my way. If I really failed to fill my Fame at this rate? Then I’d have to fight a large-scale battle with fifteen hundred people committed.

*I’m fucked.*

Something large and warm settled on my dejected shoulder. Jin Wikyung’s hand.

“Youngest.”

His voice was heavy and lonely. At the sudden change in mood, I kept quiet and listened.

“Your mission is graver than anyone else’s among us.”

“What’s my mission?”

After letting it hang for a long time, he forced out a single word.

“Survive.”

“Huh?”

“Survive however you can. If our family loses, run without looking back.”

“…”

“If the roots live, the tree will grow again. Second Brother and you could become better roots than I.”

I was speechless. For a long while, I could only stare at his face.

Survive. Become roots.

His voice and eyes hit home with more seriousness than ever before.

“That is your mission.”

The palm resting on my shoulder slid slowly down. I stared after Jin Wikyung’s departing back, unable to look away.
## Chapter artifact 37

# Chapter 37

The march went smoothly. The heavy snow that had fallen during our last reconnaissance mission had melted away long ago, and command moved us while conserving as much of the troops’ strength as possible.

“At this rate, we’ll arrive in Jeongyang by tomorrow at the latest.”

I blinked at the oddly familiar man’s words.

“Who are you?”

Judging by his clothes, he wasn’t from the Jin Family of Taiyuan. Aside from the reconnaissance squad, most of the people in the rear guard were martial artists from the newly allied small and mid-sized sects, so that made sense.

“I’m Gwak Jun of the Three Paths Sect. We met once before… We even shook hands.”

Gwak Jun of the Three Paths Sect? It was on the tip of my tongue.

*It wasn’t as if I’d shaken only one or two hands trying to raise my Fame.*

He was probably one of them.

“Sorry. My memory isn’t very good.”

“I wasn’t expecting you to remember, honestly. Haha.”

Gwak Jun gave me a friendly smile and went on.

“To be honest, I was disappointed at first when I found out we’d been assigned to the rear guard.”

“Why?”

“Because there’d be fewer chances to distinguish ourselves. Isn’t this the chance for an unknown grunt like me to make a name for himself?”

“Ah. Right.”

There were two possibilities in cases like this. Either he’d been through so many battles that he’d grown nerves of steel, or he was simply fearless.

I raised my **Qi Sense**.

Ding.

> **System**
>
> **Lv.40 Gwak Jun**

*Oh. He’s got some skill.*

At Level 40, he was at least First Rate. He couldn’t exactly go around bragging he was a master, but it was more than enough to feel wronged about being stuck in the rear.

“Half of the enemy troops were recruited in a hurry. They’ve dragged in every kind of deadweight, and they must have force-marched to join the main force. They won’t stand a chance against the elites of the Jin Family of Taiyuan and the Three Paths Sect.”

His words sounded plausible enough.

*If you leave out the part about the Three Paths Sect being elite.*

I nodded half-heartedly.

“I see.”

“And we have Peak masters superior to the enemy’s as well. There’s the Lesser Family Head and Great Hero Wipeng, of course, but the reputation of the Blade of Flowers has spread throughout the Central Plains, hasn’t it?”

The Blade of Flowers. It was the first time I’d heard the title, but I could guess who he meant.

The Jin Family of Taiyuan had three Peak masters. Exclude Jin Wikyung and Wipeng, and only one person was left.

*The Head Elder.*

*Was that old man really that strong?*

Gwak Jun’s next words were nothing but praise. Title after title, name after name of masters the Head Elder had cut down in his youth, decades ago, came spilling out.

“He was a hero born of the Great Faction War.”

A war hero from the past. Listening to Gwak Jun, he sounded like a chivalrous hero among chivalrous heroes—a man who loved justice and couldn’t stand to see injustice go unpunished…

*Then why do I feel so uneasy every time I see him?*

Maybe it was the first impression, but I disliked the Head Elder.

That peculiar air of his. The strange gaze that bored straight through people. The fact that he had formed a political faction against Jin Wikyung.

And yet after that, the Head Elder had thrown his full support behind Jin Wikyung, and the Jin Family of Taiyuan had been able to pull tight together, inside and out.

*Well, when an outside enemy invades, even family feuds have to stop.*

The Head Elder was currently leading the vanguard alongside Jin Wikyung. If he really was as skilled as the rumors claimed, tomorrow’s battle would be that much easier.

“Just thinking of Great Hero Blade of Flowers sweeping the battlefield tomorrow already has my heart racing.”

Gwak Jun shuddered like a man taking a piss after three days.

*Does this bastard not know what tension is?*

And where was he getting the confidence that we were going to win?

“You’re certain of victory.”

“If we lose, we’re in big trouble.”

“Excuse me?”

*Not big trouble. We’d be finished.*

Judging by everything the Mount Heng Sword Sect had done so far, they would turn not only the Jin Family of Taiyuan but the small and mid-sized sects allied with us into a wasteland.

“What do you mean by—”

“I’m joking.”

*This bastard’s a lunatic too.*

As I stared at him, speechless, Gwak Jun flashed me a grin.

“We’ll win. We will.”

One sentence, packed with conviction.

When Gwak Jun left it at that and moved away, Hyuk Mujin came up and asked,

“Who was that?”

“Level 40.”

“What?”

“There’s this guy. Overflowing with confidence.”

I didn’t like him, in more ways than one.

*Well, it wasn’t as though I’d have to talk to him again.*

* * *

Time passed quickly. On the second night after we began the march, we reached Honju, and Jin Wikyung gathered the command staff for a meeting. He was holding a small slip of paper.

“A letter from the Lower District Sect. The enemy reinforcements crossed Mount Otae two days ago.”

“Then…”

“They’re likely to join the main force around now, or sometime tomorrow.”

*What?*

I couldn’t understand it. If we had attacked the main force before the reinforcements joined them, the fight would have been much easier.

*He must have something in mind.*

Sure enough, Jin Wikyung went on.

“The enemy reinforcements that just joined them are exhausted, and their food is running out. If we take Jeongyang’s high ground first tomorrow, the Mount Heng Sword Sect Leader will have a choice to make. Fall back, or clash.”

The next moment, Jin Wikyung’s gaze shifted to me.

“What choice do you think he’ll make?”

I was caught off guard, but the answer was already there. If he were the kind of man to fall back at this point, he would have done so long ago.

“I think he’ll clash.”

Twice our numbers, and they weren’t behind us in Peak masters either. From the enemy’s side, they would want to end this fight as fast as possible.

“Exactly.”

Jin Wikyung smiled, pleased, and traced a finger across the topographic map on the table.

“There are four routes the enemy can take into Jeongyang. But with their food situation as it is, they’ll choose the fastest one.”

His finger stopped on a place labeled Eight Spring Gorge. The Head Elder, who had been sitting quietly until then, spoke for the first time.

“Eight Spring Gorge. Jar-shaped, with a narrow, steep mouth. The mounted bandits will have to abandon their prized horses.”

“They’ll have to abandon their lives too.”

“The enemy will fight with their lives on the line as well. This much won’t be enough.”

“I’ve hidden some hundred horn bows on the cliffs above the gorge.”

“Hoh.”

A stir ran through the tent. I stared at Jin Wikyung with my mouth open.

*When the hell did he hide those?*

“Right after our victory at Honju. Thanks to a resourceful ally.”

Jin Wikyung looked straight at me as he said it.

*The Lower District Sect. Wolhwa.*

She had been helping us constantly from places we couldn’t see. Of course, Jin Wikyung was impressive too, for drawing a picture this big.

*That’s fucking cool.*

A build like a human meat grinder, and a sharp mind to go with it. Suddenly I wanted to call him big brother.

“Oh!”

“The Lesser Family Head…!”

The tent went hot under the burning gazes of those dark, burly men.

Jin Wikyung swept a heavy look over everyone assembled.

“Let’s settle this.”

No one objected. The Head Elder was the first to rise, then gave Jin Wikyung a fist-in-palm salute.

“By your command.”

That was the end of the meeting. As I left the tent, a familiar voice bored into my ear.

—Don’t forget what I told you yesterday.

I stiffened for a moment. Then I gave a small nod.

And at dawn that day, three hundred martial artists from the Jin Family of Taiyuan and one hundred fifty reinforcements from the small and mid-sized sects—four hundred fifty in all—set out for the gorge.

*Still, this was the end, and I hadn’t even said a proper goodbye.*

I climbed a hill and stared endlessly at the winding line of torches.

* * *

The next morning, Hyuk Mujin flinched when he saw me and stepped back.

“You startled me. What’s going on?”

“What?”

“What do you mean, what? You look like a living corpse. Did you not sleep?”

“Nah. I slept a little.”

That was a lie. I hadn’t slept a wink. I had planted myself on a rock and stared at the System Window all night.

Counting down to the moment that had finally come right up to my nose.

> **System**
>
> Achieve Fame 500 (497/500)

I never thought the number 1 could feel this precious.

In a voice that had aged all of a sudden, I muttered,

“I’m going, I’m going, going home now…”

“Now you’re even talking to yourself. Have you lost your mind?”

Hyuk Mujin clicked his tongue, then his eyes went round.

“What’s that? I’ve never seen those before.”

“This?”

I pointed in turn at the old book and the small case sitting on the rock.

“One’s a martial arts manual. The other’s an elixir.”

“Hah. Really?”

I explained it weakly to the guy whose eyes were halfway out of his head.

“The manual’s a Supreme Peak martial art, and if you absorb the elixir right, it’s thirty years.”

“What?”

“But they say if you take the elixir wrong, you’ll burn to death. You want it?”

“Ah. Sure…”

Judging by that unimpressed face and the snout sticking out a good few feet, he didn’t believe a damn word I was saying.

*Well, if someone suddenly came at me with a Supreme Peak martial art and a thirty-year Fireball elixir, I’d figure it was a joke too.*

“You really won’t eat it? It’s good stuff.”

“Oh, I’m fine. Learn plenty of that Supreme Peak martial art, and be sure to chew your elixir thoroughly.”

“I don’t need this kind of thing anymore.”

“Of course. You’re the Sleeping Dragon.”

Normally I would have smacked him in the back of the head. Right now I didn’t feel much of anything.

*Is this how a short-timer sergeant feels?[^1]*

At the same time, I felt strange. Was it the aftereffect of everything I’d been through? It had only been a little over a month, but it felt distant, as if I’d been here a year.

I started tracing back through old memories.

*I first opened my eyes at Honghwaru.*

That was where I met Wolhwa for the first time and realized I was trapped in this game. Even now, thinking about that moment gave me goose bumps.

*I really thought I was going to lose my mind.*

It had taken me three days just to decide to go to the Jin Family of Taiyuan. And the guy I met there was this one—Hyuk Mujin.

Smack!

“Argh! Why did you hit me?”

“Hmm. Just thought of the old days.”

“What old days?”

“Nope. Not telling. Get back already.”

“What am I, some back-alley punk? Just because your martial arts are a bit strong, you think you can oppress people like this?”

As Hyuk Mujin threw a fit, everyone’s eyes turned toward us. Even the reconnaissance-squad members who had been watching like it was none of their business jumped in.

“What are you two talking about?”

“Dunno. The deputy squad leader must have done something wrong.”

“Hey, I didn’t do anything!”

“This is Murim. Being weak is a crime.”

“But should we even be doing this?”

At someone’s words, silence fell for a moment.

“True. Waiting here is our mission, but…”

The tension and fear they had been holding down with forced smiles hung in the air. Even I, who would soon be going back to the real world, felt uneasy with Jin Wikyung’s face flickering through my mind. How much worse must it be for these guys?

There was only one thing I could say.

“I trust my big brother.”

*Big brother.* This time, I put my heart into the word.

Jin Wikyung had been the greatest source of strength I’d had in this place. Maybe I simply wanted to shake off that unease, even if only like this.

The faces that had stiffened for a moment eased.

“We feel the same.”

Hyuk Mujin slipped in as well.

“I trust the squad leader more.”

“Wow. Deputy squad leader, that side-switching of yours is really something.”

“You little bastards. Is there anyone here who doesn’t owe the squad leader their life?”

“Well, when you put it that way, what can we say?”

“I trust the squad leader too. Honestly, I knew all along, even when you were playing the thug. I thought, *Ah, that man is the Sleeping Dragon.* I could tell right away.”

I felt strange.

*They say even dried squid gives water if you squeeze it. Who knew I’d feel something like this toward NPCs in a game?*

*Well, honestly… it doesn’t feel bad.*

Suddenly I wondered about Jin Wikyung, somewhere beyond those mountains. Had the battle started? If it had, which side was winning?

And I wasn’t the only one thinking that.

“By now, the battle must have started.”

It was Gwak Jun of the Three Paths Sect. Unlike before, he was wearing black martial robes.

*Was that what this guy originally wore?*

At my look, Gwak Jun shrugged.

“I like this sort of thing. Easy to move in, and even if a little blood splatters, it doesn’t show. You all feel the same, right?”

That last question wasn’t aimed at us. It was for the martial artists of the Three Paths Sect whom he led. Every last one of them had changed into black, and they nodded without a word.

“Apparently so.”

Gwak Jun smiled, satisfied, then turned to me.

“Well, shall we set out too?”

*What the fuck is this bastard talking about right now?*

[^1]: A conscript sergeant in the last stretch of mandatory service, coasting toward discharge.
## Chapter artifact 38

# Chapter 38

The first thing I felt was puzzlement.

“Set out?”

Gwak Jun answered.

“Yes. Our side needs to get moving too, or we won’t make it in time.”

At those inscrutable words, Hyuk Mujin stepped forward.

“You there, Three Paths Sect man. You seem to have the wrong idea. Our mission is to wait here in the rear with the Young Master.”

“Oh, is that so?”

Gwak Jun’s eyes went round. At that reaction, the reconnaissance-squad members nodded with looks that said, *That figures.*

“Looks like I had it wrong.”

“It happens. Sure it does.”

But I thought differently.

*What do you mean, it happens?*

There were twenty Three Paths Sect martial artists left in the rear. The one who amounted to their leader was Gwak Jun.

*Would a guy like that mix up his orders?*

He was unpleasant, no question, but he didn’t look that stupid.

A creeping dread rose and wound around my whole body.

“That’s a problem. The mission I received is a little different.”

“How is it different?”

As I spoke, I pressed down firmly on Hyuk Mujin’s foot. He horsed around dozens of times a day, but he wasn’t an idiot. His eyes widened as he caught my signal.

“Squad Leader, please move your foot. It hurts.”

“…”

*For fuck’s sake.*

Gwak Jun’s mouth curled as he watched me stare in disbelief.

“You catch on fast. Or are your subordinates just idiots? Well, anyway. I’ll tell you exactly what that person said.”

The next moment, the smile vanished from Gwak Jun’s face. A killer with cold, vacant eyes went on.

“Eliminate everyone and join the main force.”

Clang-clang-clang!

The instant the words left his mouth, dozens of sword flashes shot into the air. Killing intent and tension hung between the twenty martial artists Gwak Jun led and the reconnaissance-squad members, who drew their swords half a beat later.

“Have you bastards lost your minds…?”

Hyuk Mujin ground his teeth and glared at them.

“You dare betray our family? Are you itching to die?”

“Betray? Die? You’re badly mistaken.”

A sneer tugged at Gwak Jun’s mouth.

“There has been no betrayal, and we aren’t going to die. Least of all to trash like you.”

“You son of a—!”

Hyuk Mujin’s eyes went wild as he threw himself at Gwak Jun.

Or tried to.

“Don’t move.”

“Squad Leader?”

Hyuk Mujin’s eyes flew wide.

“They’re the Three Paths Sect! They’re nothing but Second Rate sect husks! Let us smash them right now and—”

“No.”

“What?”

“They’re not husks.”

Their sharp aura and murderous eyes were nothing like the ordinary martial artists of a small or mid-sized sect I had seen until now. The System turned that suspicion into certainty.

> **System**
>
> **Lv.30**

That was the average Level I read through my **Qi Sense**.

Every last one of them was a First Rate martial artist. Damn it. I’d spent three days with these people and hadn’t noticed a thing.

*I’d been too fixated on Logout.*

That was what I got for letting my guard down. I bit my lip and looked at them—or, more precisely, at the thick grass behind them.

The movement had been extremely faint, but it couldn’t get past my eyes.

*Someone’s hiding.*

They were outside the range of my **Qi Sense**, so I couldn’t confirm it. My instincts were certain, though. Spies, and an ambush on top of it. Thorough bastards.

“You lot. What are you really?”

“What is that supposed to mean?”

“Where is the real Three Paths Sect?”

The Three Paths Sect was only a small or mid-sized sect. As Hyuk Mujin had said, they were Second Rate husks. People like these couldn’t have been whipped up overnight.

*Don’t tell me.*

“Did you come from the Mount Heng Sword Sect?”

Gwak Jun gave a short laugh.

“The Mount Heng Sword Sect? Well, you could think that.”

*Damn it. A third faction.*

Logout was right in front of me, and this had to happen now…

*Shit. My luck is rotten.*

I was scared shitless. The more I shrank back, the more triumphant Gwak Jun looked.

“It’s too late for regret now. The grand plan began long ago.”

“Kh.”

Gwak Jun declared it in a voice brimming with delight.

“Today… Shanxi Murim will welcome a new master.”

Ding.

> **System**
>
> — A Quest has been created.
>
> **Quest**
>
> **Slay the Assassins**
>
> Someone who has waited a long time for the right moment has made their move. First, defeat the assassins sent by the traitor!
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung
>
> **Objective:** Slay the Assassins (0/20)
>
> **Reward:** EXP and Fame
>
> **Chain Quest**
>
> **Failure:** Death

I blinked. Had I misread the Quest Window?

*Twenty?*

Why twenty? There were enemies lying in ambush back there too.

Just as the question formed, the grass shook. The ambushers charged us with a battle cry.

“Kweeeek!”

Strange, for a battle cry. No, wait. Wasn’t that an animal?

As I stood there blankly, an alert rang in my ears that **Qi Sense** had activated.

> **System**
>
> **Lv.1 Water Deer**

What the hell?

“A water deer?”

A herd of water deer brushed past us and vanished beyond the hill. A sudden appearance. A quick exit.

Gwak Jun drew his sword with an oddly deflated look on his face.

“Attack!”

The twenty enemies came on slowly. Still wearing the shock of the water deer, I called to Hyuk Mujin.

“Hey.”

“What.”

“They’re all First Rate, you know?”

“What? Really?”

Hyuk Mujin jumped.

“Yeah. You know Lee Seogeun, the second son of the Mount Heng Sword Sect? Imagine there are twenty of him.”

“Twenty Lee Seogeuns?”

This reaction was odd. Hyuk Mujin thought it over for a moment, then tossed out a single remark.

“They’re all going to die, aren’t they?”

* * *

Gwak Jun thought,

*This isn’t how it was supposed to go.*

His gaze was locked on one man. Jin Taekyung, the third Young Master of the Jin Family of Taiyuan, known as a Super First Rate.

Every time that spear moved, blood spurted and Gwak’s men went down.

Even if they weathered one blow, the second or third always finished them. Every one of them was a First Rate martial artist trained for at least ten years.

*How is there a man like that?*

He was clearly a spearman, but he didn’t care whether the gap closed or not. Whenever it looked like there wasn’t even room to swing the spear, daggers and axes popped out from somewhere and stabbed and jabbed at anything in reach.

It put an acrobat troupe’s stunts to shame.

*Where the hell are all those weapons coming from?*

He hadn’t even seen them appear. He had no idea what kind of technique it was. This wasn’t a matter of martial arts or internal energy. Jin Taekyung himself just looked strong.

*The information was wrong.*

Twenty men weren’t nearly enough. They should have brought twice that. According to what he had been told, Jin Taekyung was nothing more or less than a lucky greenhorn.

*And what the hell are those people?*

The nine said to be Jin Taekyung’s subordinates advanced slowly with their backs together, whether their leader was doing anything up ahead or not. Individually, their skill was far from enough, but once they bunched up, they were an iron wall.

Thud. Crack!

“Gaaah!”

“Stab them! Stab them!”

“Come in! Come in!”

Gwak Jun’s lips trembled.

They had no honor as martial artists. In the middle of this melee they piled on three or four at a time and hacked away, and even his First Rate subordinates couldn’t avoid ending up as meat on a skewer.

“You bastards…!”

Anger shoved aside the fear of Jin Taekyung. Just as Gwak Jun, livid, was about to hurl himself into the fight—

Whoooosh—

A violent gale whipped up at the center of the battle.

Jin Taekyung’s spear tore through the wind and shattered the swords. Hundreds of sword fragments rode the gale and swept forward, toward the owners of those swords and the men who hadn’t reacted in time.

Pupupupupup!

“…Urk.”

Thud.

A martial artist with sword fragments buried all over his body crumpled forward. Of the ten or so subordinates caught in One Flash, he was the only one who even left a sound.

“…!”

Someone swallowed hard. Their throat bobbed.

For that moment, friend and foe alike kept silent. No one even dared think of raising a sword to fight.

Of course, one person was the exception.

“One Flash. This thing is awesome.”

The instant Gwak Jun heard that mutter, he gave up on everything.

*It’s all over.*

Even if the grand plan succeeded, he had failed. All that remained was the meaningless choice of dying to Jin Taekyung or dying to that person.

*I have to run. Far away, somewhere no one can find me.*

But Gwak Jun couldn’t leave to find a second life. Just as he was turning, a savage voice cut in.

“Stop right there. If you don’t want to die very painfully.”

Jin Taekyung added, his voice a little milder,

“If you answer well, I’ll kill you gently.”

Gwak Jun’s face went white.

* * *

Crunch!

“Ghk.”

I knew that feeling.

Two or three ribs had to have broken, and the wind would have been knocked clean out of him.

He held up pretty well for a Level 40, but that was as far as he could go.

“I told you not to run.”

“If I were him, I would’ve run too.”

Hyuk Mujin, covered in blood and dust, stared at me like I was some kind of beast.

“If you’re going to kill him gently, you might as well say you’ll coat your spearhead with Golden Sore Medicine[^1] and stab him.”

“Want me to stab you?”

“Now that I think about it, that’s true. A blade hurts less if it hits you gently, doesn’t it? You could die gently. Heh heh, heh heh heh.”

I smacked him once on the back of the head, then hauled Gwak Jun to his feet.

“Let’s try this again. Who are you?”

Ptooey.

I easily dodged the bloody phlegm. With a high Agility stat, you could even avoid spit flying at you from point-blank range.

That was a useful life hack.

Of course, I had a fitting life hack for Gwak Jun, too. For example:

“If you get hit in the solar plexus while your ribs are broken, it hurts a lot.”

Thump.

“Gaaaaah!”

“So? Your answer?”

“T-Three Paths Sect.”

As I raised my fist again, Gwak Jun shouted,

“The Three Paths Sect! It really is the Three Paths Sect! I’m telling you the truth!”

Hyuk Mujin frowned.

“He’s lying. The Three Paths Sect was founded thirty years ago. In truth, it’s closer to a martial arts school than a sect. They’re highly respected for taking in wandering orphans and teaching them.”

“So?”

“Couldn’t these bastards have killed all the Three Paths Sect’s disciples and impersonated them?”

“Impersonated? Pfft.”

A deflating sound escaped Gwak Jun’s mouth. He was laughing.

“You still don’t understand? The Three Paths Sect was established according to that person’s will. As if you could have guessed at a thirty-year grand plan. Heh heh.”

“Thirty years?”

It was an unimaginably long time. There were only a handful of people who could lie low for that many years and plot to seize Shanxi Province.

Only one person came to mind.

*The Head Elder?*

What possible reason could he have?

The Head Elder was the one who had pulled Jin Wikyung to his feet while he blamed himself in front of the children’s bodies. He was also the one who had halted every political maneuver and actively cooperated.

Thanks to that, the Jin Family of Taiyuan had united and made it this far…

*Wait.*

My head spun.

*Could it be?*

“Hyuk Mujin. How many martial artists from the newly joined small and mid-sized sects are there?”

“If you add the Three Paths Sect and Gunggwimun together, well over a hundred.”[^2]

“And under the Head Elder?”

“If you mean the Head Elder’s faction, probably close to half the main force… Ah!”

Hyuk Mujin and the reconnaissance-squad members opened their mouths as they grasped the situation.

If my guess was right and the Head Elder was a traitor, everything fit.

Helping Jin Wikyung had been nothing more than a setup for today.

*To take everything in a single battle.*

He had helped Jin Wikyung and united the family’s strength for this very day.

Suddenly I remembered what Gwak Jun had said before the fight.

That one line about Shanxi’s master changing. It no longer sounded like nonsense.

*The main force is in danger.*

I had to tell Jin Wikyung.

“We’re moving out. Right now!”

I shouted and was about to turn.

“Already too late.”

Gwak Jun grinned, baring bloodstained teeth.

“Too late for me, too late for you bastards, and too late for the Jin Family of Taiyuan and the Mount Heng Sword Sect. The grand plan has already begun.”

At the same time, blood gushed out. From his eyes, nose, and mouth—from every opening.

Gwak Jun’s head slowly drooped.

Hyuk Mujin spoke with a sickened look on his face.

“He severed his own heart meridian.”

Gwak Jun’s death meant one thing.

Ding. Ding. Ding.

> **System**
>
> — Defeated **Lv.40 Gwak Jun**!
>
> — **Slay the Assassins** (20/20)
>
> — Quest **Slay the Assassins** complete!
>
> — Level up!
>
> — Fame increases by 50!

Quest complete, a level-up, and a Fame increase.

After all those notifications, a single message appeared.

> **System**
>
> — All conditions for **Logout** have been met.
>
> — Logging out in 3 seconds. 3, 2…

Strength drained from my whole body. It felt as if I were floating.

Hyuk Mujin, startled, caught me.

“Squad Leader!”

His voice came through full of static. My vision blurred, and my body slipped out of my control.

*Not now. Not like this…*

*Of all times.*

And then—

> **System**
>
> — 1.

Darkness crashed in.

[^1]: Golden Sore Medicine is a salve for blade wounds.
[^2]: Gunggwimun is the name of another small sect newly allied with the Jin Family.
## Chapter artifact 39

# Chapter 39

“Ah.”

I blinked. It was hot and humid. When I exhaled, my vision went hazy. I felt around my head and found something hard.

*The VR helmet.*

I pulled it off, and the dusty interior of the capsule came into view.

Sitting in the old capsule chair with its collapsed cushions, I calmed my pounding heart.

*Reality? Really?*

Logout after exactly thirty days. Fear surged through me.

Was this really reality? When I pressed that button and the capsule opened, would too much have changed? I opened my mouth, my heart pounding.

“Open Status Window.”

Silence.

Neither the familiar notification nor the System Window answered.

Only then did it sink in. I had successfully logged out.

“Huuup.”

I drew a deep breath and pressed the button. With a click, the capsule door opened. Stale air greeted me.

“…Huh.”

A dark, cramped room. A small TV on the desk. A single bed. And one person asleep, reeking of alcohol.

“Khrrr. Khrrrrooo.”

Who would’ve thought those bizarre snores could sound so welcome?

*I’m back. Back to reality.*

Everything was just as I remembered it. The last thirty days felt like a dream.

After staring blankly around the room for a while, I walked over to Jinho hyung. Then I slammed the edge of my hand into his uvula.

Whack!

“Khrrr… gack!”

If it hadn’t been for this guy’s snoring, I never would have crawled into that capsule. I grabbed Jinho hyung as he thrashed around.

“Take one more. No, two.”

Whack! Whack!

“Gack! Grrrgh!”

* * *

“People who should know better, acting like this. And you’re supposed to be the goshiwon manager, no less.”

“…Sorry.”

“Let’s not make this something to be embarrassed about, all right?”

Bang.

Once the door closed, Jinho hyung turned around with a sigh.

“Are you insane?”

Before he could say anything worse, I beat him to the punch.

“For the record, it was self-defense.”

“What the fuck are you talking about? Have you lost your mind?”

“I’m perfectly normal.”

“Then why the hell did you hit a sleeping person in the neck and—!”

Thump, thump, thump.

The man next door pounded on the wall. Judging by the rhythm and force, the meaning was clear: *I want to kill you.*

Jinho hyung lowered his voice.

“Why the hell are you throwing a fit? In the middle of the night, too.”

“The middle of the night?”

“Yeah, you lunatic. It’s only three in the morning.”

With an incredulous look, Jinho hyung held out his phone.

July 25. 3:02 a.m.

I checked the date and time, and my mouth fell open.

*Only three hours have passed?*

I’d spent a whole month in Murim. Exactly thirty days. And in reality, only three hours had gone by.

“…Hyung.”

“Don’t talk to me. My throat hurts.”

“What’s the usual time ratio for a game capsule?”

“You’re like Hong Gil-dong, you bastard. Your conversation keeps flashing east, then west. All over the place.”

“How much is it?”

“Huh?”

When I asked with a stiff face, Jinho hyung looked briefly flustered, then answered.

“The latest capsule that came out last month? Five to one, I think.”

“What exactly does five to one mean?”

“What do you think? If five hours pass in the game, one hour passes in reality.”

This was driving me crazy.

“What about anything beyond that?”

“There isn’t any. With current technology, that’s the limit… Why are you asking about this?”

Because something impossible had happened.

*How am I supposed to make sense of this?*

Even looking at it again, the capsule was ancient. That piece of junk, made more than twenty years ago, had left current technology in the dust.

Thirty days in only three hours. What kind of time ratio was that? My head was too scrambled to calculate.

“Unbelievable.”

“What is?”

There was no way I could understand it on my own. Maybe Jinho hyung could come up with some kind of answer. After a moment’s hesitation, I spoke.

“A month ago—no, three hours ago—I went into that capsule…”

I’d been through so much that I had plenty to say. Even after hearing the whole story, Jinho hyung stayed silent for a long time.

Then he said one thing.

“Unbelievable.”

“Exactly. Does this make any sense? Isn’t that some illegally modified capsule or something?”

“No. Not the capsule. You.”

“Huh?”

Jinho hyung spoke with a serious face.

“Just apologize cleanly. Sorry. I hit you because your snoring was too loud. Be cool about it, you bastard.”

“…”

“What, you couldn’t log out and spent a month risking your life in a game? Go write a novel.”

*Right. I knew it was going too well.*

I sighed.

“I’m telling you, it’s true.”

“Come on, Taekyung. Let’s think about this rationally.”

Jinho hyung put on a solemn tone.

“Some guy smacks a sleeping person in the uvula to wake him up, then says he was trapped in a game for a month. But he checks the clock, and only three hours have passed? And the capsule is an antique that belongs in a museum?”

“I know it sounds insane. I get it. But…”

“Then try to get me, too. My head hurts from the hangover, my uvula hurts, and looking at you hurts.”

“Just listen to me!”

Thump, thump, thump, thump.

Before the man next door could smash through the wall, I lowered my voice.

“Then try it yourself.”

“What?”

“If you try it, you’ll believe me.”

Nothing was faster than experiencing it firsthand. If I pulled him out after about ten minutes, he’d have no choice but to believe me.

Jinho hyung stared through me, then spoke.

“Fine. Let’s try it, then.”

He climbed into the capsule and even put on the VR helmet. As he grumbled that it smelled sour inside the helmet, I said,

“I’ll pull you out soon. Stay holed up at Honghwaru.”

“Honghwaru, my ass. Just close the capsule door.”

I was curious what face he’d make when I saw him again. I closed the capsule door, took out my phone, and turned on the stopwatch.

The instant I pressed start, the numbers shot up.

*One second, two seconds… ten seconds.*

Ten seconds in reality had to mean minutes, maybe hours, in the game.

*By now he had to be losing his mind at Honghwaru trying to figure out what was going on…*

Clunk.

“Huh?”

The door opened.

*What? Why is he already out? No, how did he get out?*

Looking at me standing there flustered, Jinho hyung sighed.

“What are you doing?”

“Uh, uh?”

“The power isn’t even on. What game were you playing?”

What was that supposed to mean?

“The power isn’t on?”

“Move.”

While I was still stammering, Jinho hyung came out the door, bent down under the capsule, and picked something up.

“What does this look like to you?”

A cord. An unplugged power cord.

I scrubbed at my eyes furiously, but nothing changed.

*Was I seeing things?*

“Why is this…”

“Taekyung. Jin Taekyung. You poor, pathetic soul.”

Jinho hyung spoke with a distant look on his face.

“Go to a mental hospital as soon as it gets light. I’m going back to my room.”

He tossed the power cord aside and walked off. I stared blankly at his back.

The power cord hadn’t even been plugged in.

*Then what was the game I played?*

I felt like I’d been possessed by a ghost. Goose bumps rose all over my body.

* * *

I lay on the bed and thought.

*Am I crazy?*

I’d played a game for thirty days in a capsule that hadn’t even been plugged in.

I could understand Jinho hyung’s reaction. But everything that had happened there…

*It was all real.*

Jin Wikyung, Wolhwa, Hyuk Mujin, and the Head Elder. I remembered every NPC’s face, their way of speaking, their mannerisms. It hadn’t been a delusion I’d cooked up on my own.

*Then what was the problem?*

There was only one answer.

The problem was that game capsule made twenty-seven years ago—a piece of junk that should have retired from service long ago and been sitting in a museum.

The date of manufacture was suspicious, too.

January 1, 2020.

The day the Demon King Asmodeus fell at humanity’s hands.

*Where the hell were people making capsules back then?*

It was an era when hundreds of millions of people had died in the five-year Great War, and monsters had roamed downtown.

In my opinion, the bastards who heard the breaking news that the Demon King had fallen and fired up a factory going, *All right, let’s make game capsules now!* belonged in court.

*Back then, I thought it was a misprint.*

I froze.

*A misprint?*

*The product manual!*

How could I have forgotten something that important? What an idiot.

I shot to my feet and started turning the room upside down. At last, I found a familiar little booklet under the bed.

> **Product User Manual**
>
> **Product name:** Virtual Reality Access Device  
> **Model name:** Ark - 2020  
> **Manufacturer:** H Soft  
> **Date of manufacture:** January 1, 2020

And the next page.

> **Precautions**
>
> - The player cannot log out at will.
>
> - If the player dies during play, resurrection is impossible.

A month ago—no, three hours ago—I had thrown the booklet aside right there.

This time was different.

With trembling hands, I turned to the last page.

> **Key Features**
>
> - A custom capsule for one person only! Once a user is registered, the capsule is permanently bound, and this remains in effect until death.
>
> - Time-ratio adjustment for comfortable play! Upon login, time in reality passes very slowly. The reverse is also true.
>
> - Character Synchronization system! By synchronizing with their character, the user experiences a greater sense of unity.

“What the hell is this?”

I could read the words, but my brain refused to take them in. I started over from the beginning.

*First, permanent binding.*

It meant exactly what it said: it was mine until I died. Once I got some answers, I decided, I was going to smash that goddamn capsule to pieces.

*Next, the time ratio.*

That was the part I’d been most curious about. But instead of an exact figure, all it had was the vague phrase *passes very slowly*.

It said the reverse was true as well, so time in the game had to be passing too, however slowly.

*Then is the war still going on?*

Jin Wikyung came to mind. The Head Elder’s betrayal was already a given, and he would try to stab Wikyung in the back at the critical moment. Had Hyuk Mujin and the reconnaissance squad gotten that news to him?

*Ah. It’s still a long way off. The time ratio flipped.*

More than that, I had my own crisis staring me in the face. I checked the last key feature. Unlike the ones before it, I couldn’t understand this no matter how many times I read it.

*Synchronize with a character?*

Just in case, I even looked it up in a Korean dictionary. It meant exactly what I thought it meant. That only made it sound crazier.

*How do you even synchronize with a game character?*

I couldn’t make any sense of it. In the end, all I’d done was add another question.

One thing was certain: I wasn’t crazy.

I flopped onto the bed and read the front of the booklet again.

“Manufacturer. H Soft.”

In the end, every road led to the same place. If I looked into these bastards, something was bound to turn up.

I searched the internet for H Soft, but aside from a porn studio with the same name, I didn’t find a thing.

“…”

First I needed to lock the door and think.
