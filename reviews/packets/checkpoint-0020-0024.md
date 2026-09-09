# Checkpoint Review — 20–24

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

# Chapters 20–24

## Plot

The Jin Family and the Lower District Sect formalize a wartime alliance. In exchange for half of Mount Heng’s shops and exclusive rights to its pleasure district, the Lower District Sect stops selling Shanxi intelligence to other sects and devotes its resources to war intelligence. Wolhwa disguises the agreement by publicly claiming that she and Taekyung spent a passionate night together, presenting it as an unpaid Honghwaru tab. Her investigation has found neither evidence clearing Taekyung nor Lee Seogeun’s killer; she supports the Jin Family because either Taekyung is legitimate or the family is powerful enough to conceal the truth.

Taekyung recognizes Wolhwa’s coachman as Yama Whip, a Peak master. When the gate guards mistake Taekyung for the hero who helped Yama Whip defeat Cheonryeokbu, he encourages the story. The System reports that Poisoner rumors are fading, the Sleeping Dragon of Shanxi rumor is strengthening, and Taekyung gains 20 Fame. Meanwhile, Lee Cheonbaek, Mount Heng’s Sect Leader and Lee Seogeun’s father, expels the poison from his son’s body, vows revenge, and sends about two hundred armed martial artists toward the Jin Family.

Mount Heng’s attack begins with the murder of twenty-five children from the Jin Family’s Saneum, Eung-hyeon, and Sakju branches. The Head Elder calls the deaths necessary sacrifices and uses the Sleeping Dragon rumor and Taekyung’s supposed alliance with Yama Whip to force him into wartime service. Taekyung becomes leader of White Tiger Hall’s ten-person reconnaissance squad and receives a repeating quest to earn 100 Merit.

The squad consists mostly of inexperienced second-rate martial artists. Taekyung appoints Level 22 Hyuk Mujin, who has killed five bandits, as deputy squad leader and assigns everyone numbers. He imposes a practical Hunter-style schedule, equips three members with wooden shields, and drills formations, dispersal, and all-out retreat. Hyuk mocks the retreat strategy and accuses Taekyung of causing the war. Taekyung knocks him unconscious with a sequence of slaps, then does so again when Hyuk attacks after waking in a hunter’s shelter during a blizzard. The rest of the squad accepts Taekyung’s methods and asks him to train them.

The squad is ordered to scout near Jeongyang and return within five days. A Lower District Sect messenger hawk reports that Jopil, One Question, One Kill, and a special detachment have appeared there. Jopil leads about fifty wandering martial artists in massacring survivors from the Sakju Branch, killing the defending martial artist and several women and children. He orders his First Rate subordinate Black Mountain Blade to pursue one escaping martial artist and two children toward Honju.

Fourteen-year-old Socheon flees with his younger sister, Soyul. Their mother led other survivors away earlier, while their father and the branch families were killed. Gong Yacheong, an old friend of Socheon’s father, guides the children and stays behind to delay the pursuers; his fate is unknown. The siblings reach the reconnaissance squad’s hunter’s shelter as more than twenty Mount Heng pursuers arrive. The System creates the Sudden Quest **Survivors of the Sakju Branch**.

Taekyung first orders an attack formation, then changes to a defensive formation so the squad can hold the enemy back while he claims the kills, EXP, and Merit. He charges alone through the low-level pursuers, using the Jin Family’s Manoeuvre and Spear Techniques and cycling through their forms. He finishes Level 32 Black Mountain Blade with Cheongwan-il, completes the Survivors Quest, receives substantial EXP and Merit, levels up repeatedly, and triggers a Chain Quest.

## Continuity

- The Jin Family–Lower District Sect alliance lasts for the war. Its terms are half of Mount Heng’s shops, exclusive pleasure-district rights, and exclusive Lower District Sect intelligence support.
- Wolhwa is Eun Sowol, the Level 50 Branch Leader of the Lower District Sect’s Shanxi branch. Yama Whip is her Peak-level coachman.
- Lee Cheonbaek is Mount Heng’s Sect Leader, the Blood Wolf Sword, and Lee Seogeun’s father. He has committed Mount Heng to revenge.
- Taekyung leads White Tiger Hall’s ten-person reconnaissance squad. The squad has nine sword users, one spear user—Level 13 Han Yeop—and no experienced shield user before Taekyung assigns three wooden shields.
- Hyuk Mujin is Level 22, has killed five bandits, and is Taekyung’s deputy squad leader. Han Yeop enthusiastically follows Taekyung’s orders.
- The squad is scouting near Jeongyang under a five-day return deadline. Taekyung’s standard movement cycle is two hours of travel followed by fifteen minutes of rest.
- Jopil, One Question, One Kill, commands about fifty wandering martial artists. Black Mountain Blade, his First Rate right-hand man, is dead.
- Socheon and Soyul survived the Sakju Branch massacre. Their mother’s fate and Gong Yacheong’s fate remain unresolved.
- Taekyung completed the Sudden Quest **Survivors of the Sakju Branch**, gained large EXP and Merit, levelled up repeatedly, and activated a Chain Quest. Its requirements and outcome remain unresolved.
- The war, the unidentified assassin who killed Lee Seogeun, the capsule’s purpose, the route home, and Murim’s death and resurrection rules remain unresolved.

## Translation Decisions

- Preserve **Lower District Sect**, **Branch Leader**, **Honghwaru**, **Yama Whip**, **White Tiger Hall**, **One Question, One Kill**, **Black Mountain Blade**, **Sakju Branch**, **Honju**, and **Jeongyang**.
- Keep the alliance terms precise: half of Mount Heng’s shops, exclusive pleasure-district rights, and exclusive wartime intelligence support.
- Render Taekyung’s staged introduction as: “Yama. Whip. Great Hero!”
- Preserve the repeating 100-Merit quest, the Sudden Quest **Survivors of the Sakju Branch**, and the Chain Quest as distinct System events.
- Retain Taekyung’s practical Hunter-style command, the numbered-squad joke, the formation commands “Form up,” and his EXP-driven decision to claim the enemies himself.
- Preserve the dark comedy and violence of the five-blow sequence, including Hyuk’s accusation and Taekyung’s grip holding him upright.
- Keep **Cheongwan-il** as the final form of the Jin Family’s Spear Technique and retain “Splurt!” for the finishing impact.
- Render `반 시진` as “more than half a shichen,” with a brief factual footnote if used in the chapter translation.

## Durable state

{
  "version": 1,
  "safe_through": 24,
  "continuity_sources": [23, 24],
  "active_continuity": [
    "Jin Taekyung is trapped in Murim through an old game capsule; death is presented as permanent and he cannot log out at will.",
    "Taekyung is the disgraced third son of the Jin Family of Taiyuan and narrates with dry, self-mocking, occasionally profane humor.",
    "Logout is the Main Quest reward for reaching First Rate, Lv. 30, and 500 Fame.",
    "Taekyung is Lv. 17; his Jin Family’s Cultivation, Spear, and Manoeuvre Techniques are at the Fourth Stage, and Third-Stage Qi Sense detects targets through Lv. 50.",
    "Hyuk Mujin is Lv. 22; earlier Training Mode can summon him and Taekyung can partially adjust a summoned opponent’s abilities.",
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
    "The Lower District Sect offers aid against Mount Heng in exchange for half of Mount Heng’s shops and assets, which Wikyung accepts as acting Family Head.",
    "The Jin Family and Lower District Sect form a wartime alliance: the sect will stop selling Shanxi information to other sects and devote all resources to war intelligence in exchange for half of Mount Heng’s shops and exclusive pleasure-district rights.",
    "Wolhwa’s investigation has found neither proof clearing Taekyung nor Lee Seogeun’s killer. She treats the alliance as a profitable investment in either Taekyung’s legitimacy or the Jin Family’s ability to conceal the crime.",
    "Yama Whip is a Peak whip master who serves as Wolhwa’s coachman; the gate guards identify him as the legendary whip master who vanished more than ten years ago after fighting remnants of the Demonic path.",
    "Taekyung deliberately encourages the gate guards’ mistaken belief that he helped Yama Whip defeat Cheonryeokbu; the System reports Poisoner rumors dying down, the Sleeping Dragon rumor gaining credibility, 20 Fame gained, and passionate supporters appearing.",
    "Lee Cheonbaek, the Blood Wolf Sword and Sect Leader of Mount Heng, is Lee Seogeun’s father. He expels the poison from his own body after touching his son’s corpse, vows revenge, and sends about two hundred armed martial artists out that night.",
    "In Chapter 21, Mount Heng’s war begins with twenty-five murdered children from the Jin Family’s Saneum, Eung-hyeon, and Sakju branches. The Head Elder pressures Taekyung into service by invoking the Sleeping Dragon rumor and Yama Whip story; Taekyung becomes leader of White Tiger Hall’s reconnaissance squad with a repeating 100-Merit quest and moves into its communal quarters.",
    "In Chapter 22, Taekyung takes command of the ten-person reconnaissance squad, appoints Level 22 Hyuk Mujin deputy squad leader after learning that Hyuk has killed five bandits, assigns squad numbers, and leads the rookies toward the county towns near the Jin Family.",
    "The Chapter 22 reconnaissance squad has nine sword users, one spear user (Level 13 Han Yeop), and no shield user; four members have never killed anyone, while Hyuk is the only member with a kill record. Taekyung applies his F-rank Hunter experience to practical melee training.",
    "The reconnaissance squad’s first deployment is announced by three bells at Mi-si, approximately 1–3 p.m.; after one day, Wikyung remains worried about Taekyung but insists he is grown and can manage without being coddled.",
    "A Lower District Sect messenger hawk reports that Jopil, One Question, One Kill, and twenty special-detachment members have appeared in Jeongyang. Wikyung orders fifty martial artists to retrieve Jin Family members safely and learns that Taekyung went to Jeongyang.",
    "Taekyung’s reconnaissance squad is ordered to scout near Jeongyang and return within five days. He enforces two hours of travel followed by fifteen minutes of rest, equips three members with shields, and drills basic formation, dispersal, and all-out retreat.",
    "Hyuk Mujin mocks Taekyung’s retreat tactics and accuses him of causing the war. Taekyung catches Hyuk’s fourth punch, keeps him upright by holding his fist, and knocks him unconscious with a fifth blow; Hyuk is knocked out again after charging Taekyung at the shelter.",
    "A sudden blizzard forces the squad into a small hunter’s shelter. After seeing Taekyung beat Hyuk, the other squad members ask him to train them.",
    "Jopil, One Question, One Kill, leads about fifty wandering martial artists in massacring Jin Family survivors from the Sakju Branch near Jeongyang.",
    "Black Mountain Blade is Jopil’s right-hand man and a First Rate wandering martial artist. Jopil orders him to take half the group and pursue one martial artist and two children who escaped through Jeongyang toward Honju.",
    "In Chapter 24, fourteen-year-old Socheon flees the Sakju Branch massacre with his younger sister Soyul; their mother led other survivors away earlier, and her fate remains unknown.",
    "Gong Yacheong (Uncle Gong), an old friend of Socheon's father, guides and protects the siblings toward Honju, then stays behind to delay the pursuers.",
    "Taekyung's reconnaissance squad encounters Socheon and Soyul near its hunter's shelter as more than twenty Mount Heng Sword Sect pursuers arrive; the System creates the Sudden Quest — Survivors of the Sakju Branch, requiring Taekyung to rescue them.",
    "Taekyung orders the squad into attack and defensive formations, then charges alone so he can claim the enemies' EXP and Merit. The System identifies several pursuers at Levels 11 and 12.",
    "Taekyung kills the pursuers with the Jin Family's Manoeuvre and Spear Techniques, using the fourth forms and finishing with Cheongwan-il, the final form of the Jin Family's Spear Technique.",
    "The final opponent is Level 32 Black Mountain Blade. Taekyung defeats him, completes the Survivors Quest, receives large EXP and Merit, levels up, and triggers a Chain Quest."
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
    "Preserve the System titles Gambler and Sex Fiend, and render the Mount Heng demand as commanderies and counties.",
    "Preserve the alliance terms, the approximate count “about two hundred,” the rank “Super First Rate,” and the guards’ crude insult.",
    "Keep Taekyung’s staged title delivery as “Yama. Whip. Great Hero!” rather than treating Yama Whip as a personal name."
  ]
}

## Reading copies

## Chapter artifact 20

# Chapter 20

The hour-long negotiation was finally entering its closing phase.

“Half the shops owned by the Mount Heng Sword Sect. And exclusive rights to the pleasure district. Is that correct?”

“Without a doubt. And your sect?”

“From this moment onward, we will not sell information to any sect in Shanxi other than the Jin Family of Taiyuan. We will also devote all our resources to gathering and delivering information about the war.”

The terms had already been decided after dozens of rounds of push and pull.

Jin Wikyung and Wolhwa carefully checked everything one last time to make sure there were no loopholes, then drafted and exchanged the document.

“We’re officially in the same boat now. I look forward to working with you, Lesser Family Head.”

“Likewise.”

That was when they shook hands.

Ding.

> **System**
>
> - The **Jin Family of Taiyuan** and the **Lower District Sect** have formed an alliance.
>
> - The alliance will remain in effect for the duration of the war.

Even this showed up. Then again, a similar notification had appeared when the war with the Mount Heng Sword Sect began.

*With the Lower District Sect joining in, have our odds of winning gone up a little?*

The Lower District Sect specialized in information.

Wolhwa had confidently claimed that all the information in Shanxi passed through her hands. If that was true, their assistance would be enormous.

*Nothing is more important than information.*

I didn’t know how things worked in Murim, but I knew that much. Information could become anything depending on how it was handled. A sword, a shield, or sometimes even a bomb capable of turning the tide in a single stroke.

It would be nice if Wolhwa brought us information like that.

“Then I’ll be taking my leave.”

“Please understand that you cannot go far while there are eyes on us.”

“Of course.”

*It’s finally over.*

Wipeng bowed with his usual impassive expression, and I gave an awkward half-bow of my own.

“Goodbye.”

Wolhwa’s eyes curved like crescent moons when she looked at me.

“Young Master Jin is coming with me.”

“Huh?”

“You’re not going to see me off?”

“…Why would I?”

“Because we spent a hot night together?”

That full-force fastball straight to the body left me momentarily stunned. No, seriously. I’d told this woman to bring information, so why was the first thing she was spreading this kind of adults-only information?

And in front of everyone, too.

“Oh?”

“A hot, hot night? Together?”

Wipeng looked back and forth between Wolhwa and me with interest, while an earthquake shook Jin Wikyung’s pupils.

“Taekyung, is that true? Is it really true?”

After a long silence, I answered.

“I’ll see her out.”

I grabbed Wolhwa by the wrist and dashed out. Behind me, Jin Wikyung’s mournful voice echoed through the hall.

“Little brother!”

* * *

Wolhwa was a rare beauty. Her slender figure, combined with her extravagant clothing, made it impossible for people not to stare.

“Did the family have a beauty like that?”

“Of course not. She’s an outsider.”

“An outsider?”

“Yeah. According to a friend among the gate guards, she’s a courtesan from Honghwaru.”

“Ah, that Honghwaru everyone says is ridiculously expensive. I know the place. Wait, but why would a courtesan come here?”

“They say she came to collect an unpaid tab from the Third Young Master. She probably wants to collect the money before the war turns into a full-scale conflict.”

“…Huh. The Third Young Master really gets up to all kinds of things, doesn’t he?”

The people’s whispers wormed into my ears. Wolhwa, who had been walking ahead of me while humming, suddenly turned around.

“Young Master Jin, why are you walking so far behind?”

I answered in a sullen tone.

“If we walk together, people will get the wrong idea. There are already all kinds of rumors going around…”

“Oh, the unpaid tab?”

Yeah. That.

“That rumor isn’t actually false.”

Wolhwa smiled brightly.

“When the gate guards asked why I came, I simply told them I was here to collect an unpaid tab. It’s not an outright lie.”

“What?”

“Were you planning to announce our alliance to the whole world?”

“…No.”

Why did she have to use my name? My image was already a complete disaster.

If rumors like this spread while we were in the middle of a war, I’d have no way to deny them. My reputation as a piece of trash would be set in stone.

“Considering you’ve already been falsely accused of poisoning someone, being a kept man is comparatively mild. Given your usual behavior, people will believe it.”

That was strangely persuasive. I nodded without thinking, then sensed something off in Wolhwa’s words.

“Falsely accused?”

Now that I thought about it, she had never once mentioned Lee Seogeun. She had adjusted the negotiations like a fastidious businesswoman, then formed an alliance as if it were the most natural thing in the world.

*What exactly is she relying on?*

Wolhwa gave a small smile at my suspicious look.

“Young Master Jin, have you forgotten who I am?”

“The Lower District Sect’s Shanxi Branch Leader…”

My eyes flew open.

Information. She had information.

Information proving I wasn’t the culprit.

I quickly moved alongside Wolhwa.

“Can you clear my name? Do you really have information like that?”

The war had begun with Lee Seogeun’s poisoning. If we could prove that all of this was a conspiracy carried out by someone else, we could stop the war.

But that hope was shattered by Wolhwa’s next words.

“No. I don’t.”

What?

“Then why did you form an alliance with us?”

“Because I’m a merchant.”

Wolhwa continued in a light, cheerful tone.

“We of the Lower District Sect are merchants at heart. We move strictly according to profit and loss.”

“If that’s the case, this makes even less sense.”

“Oh? Why?”

“Because the Mount Heng Sword Sect is stronger than we are. If you’re weighing profit and loss, shouldn’t you be siding with them?”

“You’re honest. No, perhaps I should say naïve.”

Wolhwa snickered.

“This is an investment. It’s the result of placing both sides on a scale and analyzing them coldly.”

“So as long as you profit, it doesn’t matter? Even if I really did poison Lee Seogeun?”

“Young Master Jin, what do you think it means that the Lower District Sect’s Shanxi branch devoted all its resources to investigating this, yet still couldn’t verify the truth?”

I hesitated, but Wolhwa didn’t wait for an answer.

“It’s simple. Either Young Master Jin is truly innocent, or you concealed it so perfectly that even we couldn’t uncover it.”

“Ah.”

“Either way, I don’t lose. If the former is true, then you have legitimacy, which is enough for us. If the latter is true, then it proves the Jin Family of Taiyuan is that capable.”

I was more than a little surprised. So that was one way of looking at it.

Thorough profit-and-loss calculation. I finally understood exactly what Wolhwa meant when she called herself a merchant.

The fact that someone like her was on our side gave me a reassuring feeling.

But…

“You’re overlooking one important thing. If I’m innocent, then who actually poisoned Lee Seogeun?”

That was the heart of the war. The biggest piece of the puzzle—one Wolhwa had failed to find.

If the Lower District Sect had discovered the culprit’s identity, she would have brought that information today.

Wolhwa sighed.

“I’m ashamed to say that nothing has been uncovered yet. But our sect is doing its best. Ah, we’re almost there.”

There were still plenty of things I wanted to ask, but I had no choice but to fall silent when I noticed the approaching gate guards.

*Our alliance with the Lower District Sect is still a secret.*

A four-horse carriage that appeared to be the one Wolhwa had arrived in came into view, surrounded by gate guards in a wide circle. The strange tension around it reached us even from here.

*Did something happen?*

I sent internal energy through my eyes and ears. Soon, my enhanced senses picked up the gate guards’ tense voices.

“He’s a master. No doubt about it. At least Super First Rate, maybe even Peak. See the whip at his waist? He must be someone who handles a whip like a ghost.”

“A master of that level volunteering to be a coachman? A peerless beauty really is different.”

The martial artists speaking to each other sounded fairly experienced, and their voices were deadly serious. A younger martial artist cautiously murmured:

“But for someone like that, doesn’t his posture have too many openings? He’s thin, too…”

The senior martial artists clicked their tongues.

“Kid, this fellow and I have ten years of experience at the gate-watch office. We can tell from a person’s eyes alone. What the hell would a little shit like you know, butting into your elders’ conversation?”

“Tsk. Openings? You call that an opening? Can’t you see the ease and naturalness that only masters possess?”

“Then what about his temples? Masters with profound internal energy have bulging temples.”

“That’s just Returning to the Origin…”

Unfortunately, the conversation ended there. The gate guards noticed us standing blankly in front of the main gate and scattered.

Thanks to them, I was able to confirm the identity of the Peak master who handled a whip like a ghost and had volunteered to be a coachman because he had fallen for Wolhwa’s beauty.

“Young Master, do you remember me?”

“…”

As if I could forget.

That heavy voice. The air of a master coming off those sharp eyes.

He was the coachman who had brought me to the Jin Family of Taiyuan a few days ago.

I never expected to see that face here. I was momentarily speechless, and Wolhwa spoke up.

“I hear you two are acquainted. Last time, you crossed life and death together and formed a deep friendship that transcended age and status…”

*No. That isn’t what happened. Please stop.*

I tugged at Wolhwa’s sleeve, but it was already too late. The coachman opened his mouth with a gentle smile.

“Even now, if I close my eyes, the memories of that day remain vivid. Cheonryeokbu… He was a truly strong bastard.”

The gate guards, who had been listening intently, let out exclamations.

“Oh!”

“Cheonryeokbu… Surely he means that Cheonryeokbu of the Eighteen Strongholds of Green Forest?”

“Wasn’t he the infamous Peak master of Green Forest? To kill a man like that, as expected, this gentleman must be…”

“…”

They seemed to have gotten something seriously wrong.

I had no idea where to start correcting them—or where to stop.

While I stood there blankly, the coachman grabbed me in a hug.

“If it weren’t for you, Young Master, I would have been in serious trouble.”

This man had a strange way of putting things. Without me, he would have been drinking a cup of makgeolli at the top of Mount Beimang.[^1]

“Please let go of me first, then we can talk…”

That was when I was just about to pry him off.

“Yama Whip. The master of the whip arts who vanished without a trace more than ten years ago. It’s him. It has to be.”

A ripple passed through the gate guards at someone’s mutter.

“Yama Whip? You mean that Peak master who traveled the realm beating down remnants of the Demonic path?”

“I’ve heard that name, too. A master standing between the orthodox and unorthodox paths, with no known sect or past… Come to think of it, wasn’t the place where his trail disappeared somewhere near Shanxi?”

“Then the Third Young Master—no, our Young Master—is acquainted with Great Hero Yama Whip.”

“And not only that. He must have played a major role in taking down Cheonryeokbu.”

“Oh! Ohhh!”

Hot, admiring gazes poured in from every direction. Perhaps sensing that something was wrong, the coachman tried to pull away, but my hand was gripping his shoulder tightly.

“Young Master?”

I gave him the brightest smile in the world.

“To meet you again like this—Yama. Whip. Great Hero!”

My words had the effect of throwing oil onto a fire.

“Woooah!”

The overheated gate guards stomped their feet, while Wolhwa bent over, desperately trying to hold back her laughter.

Ding.

> **System**
>
> - Rumors about the **Poisoner** are dying down!
>
> - Rumors about the **Sleeping Dragon of Shanxi** are gaining credibility!
>
> - **Fame** increases by 20!
>
> - Passionate supporters have appeared!

As the beautiful System notifications rang out, I remembered a famous saying.

*The perfect lie… is a true story.*

* * *

The young man stared at the ceiling with his eyes wide open. His once-bright black eyes had lost their light, and his face was twisted with fear and pain.

“Seogeun. My son.”

A large, rough hand caressed the young man’s face. The intense poisonous energy that had seeped in through the skin was blocked by internal energy that rose naturally.

“How did this happen to you?”

The middle-aged man lamented.

He had grown up a complete orphan and spent decades in Murim.

He had met countless people and watched countless people leave. From the days when he was a green twenty-year-old wandering martial artist to the moment he became the master of a sect, his memories were beyond counting.

“Did it hurt? Were you so bitter you couldn’t even close your eyes?”

He quietly looked down at his son’s wide-open eyes. Every blood vessel had burst, staining the irises red.

He was barely twenty. Blood tears flowed from the eyes of a father who stood before his poisoned son.

“My son.”

The poisonous energy that had entered through his hand was spreading throughout his body. Within only a few breaths, his head began to spin and his limbs went numb.

Such a deadly poison.

He could vividly picture his son’s final moments—his entire body stiffening until he couldn’t even struggle.

“I’ll remember this pain.”

The next moment, powerful internal energy rose like a wildfire and drove the poisonous energy away. The poison that had been consuming his insides vanished in an instant, as if it had been torn apart by a pack of hundreds of wolves.

“I’ll make them pay a hundred times over. A thousand.”

The Sect Leader of the Mount Heng Sword Sect, Blood Wolf Sword Lee Cheonbaek, left his son’s corpse behind and walked away.

When he opened the pavilion door, he saw the black night sky and the torches flickering beneath it.

A group of about two hundred fully armed men stood outside. The man at the front bowed his head.

“Father.”

Lee Cheonbaek nodded at his eldest son.

“Go. Tonight… is the beginning of our revenge.”

That night, about two hundred martial artists left the Mount Heng Sword Sect.

[^1]: A Korean image for being dead; Mount Beimang is the legendary mountain of the afterlife.
## Chapter artifact 21

# Chapter 21

Ding.

> **System**
>
> - Practiced the **Jin Family’s Cultivation Technique**.
>
> - As a result of repeated practice, **Sinews** and **Bones** each increase by 1.

“Whew.”

I opened my eyes with a deep breath. In the dimness before dawn, the candlelit room rippled with an amber glow.

*Failed again.*

My fist clenched in the silence.

How many times had I tried? Twenty? Thirty? The result was what mattered. Once again, I had failed to draw out the hardened internal energy.

*Should I take comfort in the fact that I’m getting better?*

I was gradually getting used to handling internal energy. If I had been a C-Rank Hunter instead of an F-Rank—or at least a D-Rank—I would have adapted much faster. But reality was cold and unforgiving.

*My Sinews and Bones improving steadily must be helping, too.*

Internal energy flowed through the body’s blood vessels. The more one practiced a cultivation technique, and the more one’s Sinews and Bones improved, the wider and sturdier those pathways became. Compared to when I had started, I could circulate more internal energy at a much faster speed.

*It’s all thanks to the Skill Points.*

The ten Skill Points awarded with every level-up were doing their job well. There was no better nourishment for improving my Sinews and Bones.

*Open Skill Window.*

> **Skill Window**
>
> **Lv. 17 Jin Taekyung**
>
> **Cultivation Technique:** Jin Family’s Cultivation Technique (Fourth Stage)
>
> **Martial Arts:** Jin Family’s Spear Technique (Fifth Stage) / Jin Family’s Manoeuvre Technique (Fifth Stage)
>
> **Sinews and Bones:** 105
>
> **Remaining Points:** 0

*I can see the possibility.*

The impregnable fortress was getting smaller and more ramshackle. If I kept pounding away at it, I felt as if I could open the gate soon.

Fortunately, I might lack talent, but I had persistence.

*I’ll keep trying. Until it works.*

I was just about to sit cross-legged and begin circulating my qi again when it happened.

Through my senses, pulled taut by the earlier rounds of circulating my qi, I heard an unusual sound.

*This is…*

A low, droning hum. At first, it sounded like a swarm of bees, but it was actually the murmur of many people.

*What’s going on?*

I let internal energy flow to my ears. Perhaps because of the distance, I couldn’t make out everything clearly. But I heard enough.

One word stood out among the indistinct voices.

*Battle!*

The Mount Heng Sword Sect. The battle had finally begun.

I hurriedly uncrossed my legs and stood. Then I leaped through the half-open window.

I landed like a cat. Before me, the pavilions lit up one by one.

*In the end…*

It had begun.

* * *

Twenty-five.

That was the number of corpses laid out in orderly rows.

When I saw them lying like dead trees, every trace of vitality gone, I was left speechless.

“This is…”

I was a Hunter. I had fought countless battles and witnessed death countless times.

Poisoned, cut apart, crushed, blown apart…

The kinds of death varied wildly depending on the monster involved. But all those deaths had one thing in common.

They were all adults.

That was one of the basic conditions for awakening. No one knew what the standard was or why it existed. It was a law as naturally established as the existence of Gates.

That was why none of the countless deaths I had witnessed had involved a child.

*This is a game. It’s just a game.*

I kept repeating the words to myself. But the sight before me was too horrific to dismiss so simply.

**BLOOD**

The character had been carved into their foreheads. Torchlight reflected off the dried blood.

More than ten children had gone cold like that.

They were middle-school age at most. Some looked even younger. Every single one of them was dead.

“Urgh!”

One of the martial artists, holding a torch in a shaking hand, doubled over, and soon the sound of retching rang out from all around us.

Then a hand reached down and picked up the torch he had dropped.

“Somi. That was definitely her name. On the day I became acting Family Head, the Branch Leader of Eung-hyeon bragged about her endlessly, calling her his treasure.”

It was Jin Wikyung. With eyes that seemed ready to go out, he lifted the torch and illuminated the children’s faces.

One by one.

As each face was revealed, he unfailingly spoke its name.

After naming the last child, Jin Wikyung looked at me.

“Do you know who these children are?”

“…No.”

“They were members of our family sent to the branches in Eung-hyeon, Saneum, and Sakju.”

I didn’t know where those places were. But I could guess what end the children’s parents had met.

And I was sickened by the Mount Heng Sword Sect’s intentions.

*Those lunatics. Those fucking psychopaths.*

*Look. We can slaughter even children this young. Soon, you’ll end up the same way.*

I could almost hear the voice of the Mount Heng Sword Sect’s Sect Leader, whose face I had never seen.

“This is all my fault. To slaughter even children who don’t know martial arts so cruelly…”

Jin Wikyung was blaming himself in a trembling voice when—

“That is the essence of war, Lesser Family Head.”

The Head Elder appeared, stroking his silver beard. His eyes had settled calmly as he looked over the corpses.

“Victory and defeat. Death is absent from neither. The Mount Heng Sword Sect’s Leader—Blood Wolf Sword Lee Cheonbaek, was it? As one would expect of a former wandering martial artist, he understands war well. These children alone make that clear.”

The casual way he said it sent a chill through me.

*What the hell is wrong with this AI?*

This NPC was missing something. That made him feel even more dangerous.

I kept my mouth shut, while Jin Wikyung spoke with a twisted expression.

“…Please choose your words carefully. They are members of our family.”

“No. Those children are casualties of war. Countless more will die from now on. Perhaps even at this very moment.”

“Head Elder. I told you to watch your words.”

Jin Wikyung growled. If no one else had been watching, he looked ready to start something right then and there.

But the Head Elder remained calm.

“Did you not anticipate this?”

It was a sudden shift to informal speech. Yet it was so natural that neither I nor Jin Wikyung even registered it.

“Saneum, Eung-hyeon, Sakju. All of them were places within the Mount Heng Sword Sect’s reach. When you sent messenger pigeons to the branches the day before, did you truly not consider that something like this might happen?”

“That…”

“You knew harm would come to them. Sending those pigeons was nothing more than a way to ease your conscience.”

“Enough. Please, enough.”

“It was an excellent decision. If you had wanted to save the branches, you would have had to run for seven days and nights without rest, then fight the enemy in a state of extreme exhaustion. Isn’t that right?”

Jin Wikyung stared at the Head Elder with a pale face. Fresh blood flowed between his tightly clenched fingers.

“I—I…”

“Everything comes with a sacrifice. Look at the bigger picture. You are the Lesser Family Head responsible for the hundreds of family members of the Jin Family of Taiyuan.”

Jin Wikyung’s body trembled. The anger and sorrow had drained from his face, leaving it filled with a strange emptiness.

“Sacrifice…”

“The war has only just begun. Isn’t that so, Lesser Family Head?”

The Head Elder made a respectful fist-and-palm salute. I bit down hard on my lip.

*What an impossible old man to figure out.*

The Head Elder was clearly dangerous. His position in the family, his utterly unreadable motives, and even his psychopathic side—he didn’t so much as twitch an eyebrow while looking at the corpses of children.

But…

*He was right.*

From my perspective, Jin Wikyung was a good Lesser Family Head. He was deeply humane and sharp-minded.

But the moment he saw the corpses, he had been shaken more than anyone. Without the Head Elder’s cold rebuke, it would have taken him a long time to regain his composure.

*He helped. The Head Elder, of all people…*

*Were they enemies in peacetime but united during war?*

*Then that’s fortunate.*

I was looking at the Head Elder with a mixture of suspicion and relief when he spoke.

“So the Third Young Master is here as well.”

My heart dropped at the sight of those seasoned gray eyes. It was the first time the Head Elder had spoken to me.

“Greetings, Head Elder.”

The Head Elder looked at me with a strange smile as I did my best to hide my surprise.

“I’ve been hearing an interesting rumor within the family lately. Something about… the Sleeping Dragon of Shanxi?”

I never expected to hear that ridiculous nickname from the Head Elder.

“I’ve also heard that you are acquainted with Yama Whip. They say you joined forces with him to defeat Cheonryeokbu.”

“Cough. Cough.”

“Are you ill?”

“N-no. I’m just feeling a little chilly.”

“Oh dear. That won’t do for someone who is about to accomplish great things.”

My awkward smile slowly froze.

“What do you mean?”

“Someone capable of helping eliminate an exceptional demon like Cheonryeokbu is valuable combat strength. Surely that rumor isn’t false.”

“…”

“Therefore, as a direct-line member of our family, I believe it is only natural that you take the lead in battle. What do you think, Lesser Family Head?”

The Head Elder smiled faintly. Jin Wikyung, who had been gazing at that smile, asked me,

“What do you think?”

I was cornered.

The moment the word came to mind, a familiar notification rang out.

Ding.

* * *

> **System**
>
> **Quest**
>
> **Mission**
>
> You have been appointed reconnaissance squad leader of White Tiger Hall.
>
> From now on, lead the subordinates assigned under you on missions and build merit!
>
> **Grade:** Repeating Quest  
> **Restriction:** Jin Taekyung  
> **Mission:** Achieve 100 Merit (0 / 100)  
> **Reward:** Changes according to the degree of success.  
> **Failure:** Changes according to the degree of failure.

I closed the Quest Window. I had already seen it several times, and besides, the White Tiger Hall martial artist who had been away for a while had just returned.

“These are the supplies issued to squad leaders.”

A sword.

A black martial uniform with a crude white tiger embroidered on it.

And a smooth wooden plaque that smelled strongly of fresh wood.

That was everything.

“The newly assigned members are waiting at the reconnaissance squad’s quarters. The location is…”

Fortunately, I knew the place. The pavilion I had passed several times was the quarters assigned to the reconnaissance squad.

After leaving White Tiger Hall, I first ducked into an empty alley.

*Open Inventory.*

Ten seconds was enough to put on the full uniform. I changed clothes, shoved the sword deep into my Inventory, then pulled out the *Sharp Spear*.

Until now, I had thoroughly enjoyed the privileges of being the Third Young Master in a lavish private pavilion.

But things were different from here on out.

*It’s communal living, right?*

We would eat together and sleep together. I couldn’t have a two-meter iron spear pop out of thin air whenever I needed one.

Once I hung the wooden plaque engraved with *Squad Leader* at my waist, I felt like I’d become Ordinary Martial Artist #1 of the Jin Family of Taiyuan.

*Not just an ordinary martial artist. I’m a reconnaissance squad leader.*

White Tiger Hall reconnaissance squad leader.

I had never expected to receive a position like this.

Of course, there had been some fierce disagreement over it. The Head Elder wanted to place me in a combat unit under the Elder Council faction, while Jin Wikyung had vehemently opposed him.

*In the end, we reached a compromise.*

An easy mission as reconnaissance squad leader, but under the command of White Tiger Hall’s Leader, who belonged to the Elder Council faction.

Before I knew it, I had received this position.

*I never imagined this was how I’d get dragged into the war.*

I could have just told them to do whatever the hell they wanted, but I held back. The first reason was the Head Elder’s eyes, which flashed every time Yama Whip was mentioned.

The second reason was…

The children.

*It’s a game. It’s all graphics and nothing more than an illusion.*

No matter how many times I repeated that to myself, the corpses and the character carved into their foreheads kept flickering before my eyes.

That was right. This decision had an emotional component.

This wasn’t good.

*Don’t get immersed. I can’t confuse reality with the game.*

Things like this had been happening more and more often lately. At first, I had treated the NPCs like people for fun. But these days, I was actually thinking of them as real people and forming relationships with them.

Every time it happened, I was startled.

Maybe this was a side effect of playing the game for too long.

“Is this it?”

Before I knew it, I had arrived at the reconnaissance squad’s quarters, and my mouth fell open.

Cracked wood and a musty smell.

Good lord, there was even a beehive under the eaves. I had never seen one that big before.

*Just like a family-like company…*

Look at those benefits.

Or maybe it was a mean-spirited prank by the White Tiger Hall Leader, who disliked me. Perhaps he couldn’t openly give me grief yet, so this was his way of telling me to eat shit.

*All right. Let’s give it a shot.*

I took a deep breath, opened the door, and stepped inside.

Creeeak.

The old floor let out a wailing sound that felt especially ominous.
## Chapter artifact 22

# Chapter 22

The smell of mold stabbed at my nose as soon as I entered the room. The place reminded me of a military barracks, and the members of the reconnaissance squad were waiting inside.

*Ten people.*

I raised my senses and looked over each of them.

Every time my gaze passed over an unfamiliar face, a Level display popped up.

*Level 14. Level 15. Level 14…*

Most of them were around the same level. Then, as I moved on to the ninth person—

> **Lv. 22 Hyuk Mujin**

The number jumped sharply. The face was familiar, too.

*Hyuk Mujin?*

It was the same Hyuk Mujin who had picked a fight with me when I first arrived at the Jin Family of Taiyuan a few days ago. When our eyes met, he curled the corners of his mouth.

“What a pleasure to see you again, Third. Young. Master.”

I stared at his openly hostile smile and said,

“From now on, call me Squad Leader.”

“……As you wish.”

I let Hyuk Mujin’s piercing gaze slide off me and looked at the tenth member of the reconnaissance squad. The young man who had been smiling brightly since I first appeared shot to his feet.

“Young Master—no, Squad Leader! I look forward to working with you.”

> **Lv. 13 Han Yeop**

It seemed some assignments had been changed because of the war. The White Tiger Hall clerk I had met earlier said that the reconnaissance squad itself was made up of martial artists drawn from several different places.

*Hyuk Mujin originally belonged to the Gate Watch Office, too.*

Maybe that was why the atmosphere in the room was so disorganized.

The squad members looked at me with expressions that mixed the awkwardness of strangers meeting for the first time with anxiety and anticipation about the war.

I spoke first.

“I’m Jin Taekyung, appointed leader of White Tiger Hall’s reconnaissance squad. I look forward to working with you.”

Clap, clap, clap.

Someone’s lonely applause died out within a few seconds, and Han Yeop lowered his hand with an embarrassed expression.

The atmosphere was stiffer than I had expected.

*But that isn’t necessarily a bad thing.*

We were in wartime. Maintaining the current tension was better than laughing together and trying to socialize.

Of course, too much tension could become poisonous. Easing it at the right moment was one of my duties as squad leader.

*That much, I’m used to.*

Newbie Hunters froze the moment they entered a Gate for the first time. Real combat was different from practice. Everything they had learned and trained for at the Hunter training center flew off into outer space, and they were overwhelmed by the primal scent of death.

That was why veterans in the Guild handled mental care for the rookies. I had been one of them.

*Though I was assigned exclusively to F-ranks.*

The levels were similar, too. From what I could tell, a Second Rate martial artist from Murim was somewhere between an E-rank and an F-rank.

In other words, I had become the leader of a ten-person F-rank party. I had never actually been a party leader, but I had watched what they were supposed to do until I was sick of it.

“Raise your hand if you have combat experience.”

At my abrupt question, every member of the reconnaissance squad raised a hand. They all looked bewildered.

“Raise your hand if you’ve been in combat at least five times.”

Half the hands went down. Han Yeop was among them.

Five people with experience in at least five battles. That wasn’t bad. No, it was better than expected.

But the most important question remained.

“Raise your hand if you’ve killed someone.”

Four hands dropped weakly. I looked at the only member of the reconnaissance squad who still had his hand raised.

> **Lv. 22 Hyuk Mujin**

“How many?”

He snorted.

“Five. It was during last year’s bandit suppression campaign. One of them was a bandit chieftain. He was quite a strong bastard—”

I cut him off before he could continue.

“Good. You’re the deputy squad leader from now on.”

Hyuk Mujin’s mouth, which had been preparing to ramble on, snapped shut.

“Deputy squad leader?”

“Yeah. Speak up now if you don’t like it.”

With nothing but rookies gathered here, experience mattered more than anything.

Hyuk Mujin was the only one who could swing a weapon at the enemy without hesitation.

*Black cat, white cat.*

White cat, black cat, or even a rude cat—it didn’t matter as long as it caught mice.

Hyuk Mujin thought for a while with a complicated expression before answering.

“……Hmph. Since it’s an order, I suppose it can’t be helped.”

He sure had a difficult way of saying he wanted to be deputy squad leader.

“Then Hyuk Mujin is deputy squad leader. From now on, we’ll call you Number One.”

“Number One? What’s that supposed to mean?”

“Number order. From now on, the reconnaissance squad will be referred to by number instead of name. Hyuk Mujin is Number One. Next, you sitting over there. Yes, you’re Number Two.”

I finished assigning numbers one by one, from Number One to Number Ten.

Hyuk Mujin frowned.

“Why are you doing this?”

“It’s more convenient. We might be fighting today. Do you want to spend all day memorizing names?”

“That’s—”

“Then do as you’re told. It’s an order.”

I didn’t look away from Hyuk Mujin as he glared at me with a hard expression.

Part of me even hoped he would act insolent like he had that day. A battle could break out within the next few days. If things continued as they were, that would be a problem.

If he challenged me, I would have to show him the difference in our strength.

Clearly.

“……I will follow your orders.”

“What did you say?”

“Number One. I said Number One.”

Hyuk Mujin’s voice trembled as he answered. He was more perceptive than I had expected. Maybe it was because of the rumors about the Sleeping Dragon of Shanxi.

The important thing was that Hyuk Mujin had submitted to me.

Without showing anything on my face, I continued.

“What I’m about to say may sound strange and unfamiliar. But bear with it. It’s better than getting stabbed to death, isn’t it? Don’t you agree?”

The other reconnaissance squad members didn’t show their displeasure as openly as Hyuk Mujin, but they also looked at me anxiously.

Everyone except one.

“I’ll follow whatever the Squad Leader says!”

Han Yeop shouted like a teenage girl idol fan. The only difference was that he was holding a spear instead of an idol light stick.

*Oh, right.*

I grinned at the reconnaissance squad.

“Now, raise your hand if you use a sword.”

The core of party hunting was dividing up positions.

* * *

Raid strategies in the real world had been standardized into manuals long ago.

Three tanks. Four damage dealers. Two mages and one healer. For a ten-person party, that was the ideal combination.

*Of course, there are no mages or healers.*

I had to balance things as much as possible with tanks and damage dealers alone, but—

“……You’re telling me no one knows how to use a shield?”

My voice trembled at the shocking result. Good lord, there were ten damage dealers. Nine used swords, and the only person with a spear was Han Yeop.

*What kind of horrifying single-species party is this?*

A hybrid would be better. At least that would mean something had been mixed in.

Hyuk Mujin spoke with an expression that suggested he couldn’t understand what was wrong.

“A man ought to wield a sword.”

I was speechless when I saw the others nodding along with him.

*You’re too well-fed. Way too well-fed.*

Try slamming your head into a pool of blood and see if you still talk like that.

Sword? Spear? There was no such distinction. You bashed people with whatever rock you happened to grab, threw dirt, climbed on top of them, and bit them with your teeth.

On the line between life and death, anything in your hand was a weapon and a lifeline.

These people, who had only ever fought bandits at best, still didn’t understand that.

*Do I need to start training them tomorrow?*

Not for their sake. For my survival.

Even teaching them a few tricks would make a real difference in a melee.

*I worked like a dog for seven years. I can’t die because of a bunch of rookies.*

That was when it happened.

Ding. Ding. Ding.

A large bell rang three times.

In a place where individuals couldn’t know the exact time, bells were rung at set intervals. The three tolls that had just sounded announced that it was Mi-si, roughly one to three in the afternoon.[^1]

And—

“Get ready. This is our first deployment.”

The bells also served as the signal announcing the reconnaissance squad’s first mission.

* * *

“He should be doing fine.”

Jin Wikyung looked up at Wipeng’s sudden remark. Until a moment ago, he had been staring blankly at a teacup as it slowly cooled.

“What are you talking about?”

“The Third Young Master.”

A full day had passed since the reconnaissance squad led by Jin Taekyung departed from the Jin Family of Taiyuan. Their mission was to scout the county towns near the Jin Family.

“They left around noon yesterday, so they should arrive within two days.”

“Ah. Taekyung.”

Jin Wikyung let out a weak laugh. He looked exhausted.

“I thought you meant something else. That’s not it.”

“It’s not?”

“How long are you going to treat him like a child? He’s a grown man now. I’m sure he’ll manage on his own.”

“……I’m beginning to doubt my ears.”

“I did coddle him quite a bit. He was very young back then.”

“I agree, to some extent. He’s changed considerably over the past few days.”

“Heroes grow by overcoming adversity.”

“……”

“Anyway, I can stop worrying about the youngest now. I’ll be able to focus more on the main family.”

“You should rest for a while. You look tired.”

“Wipeng. Members of our family have died.”

At the sorrow and determination in his voice, Wipeng fell silent, and Jin Wikyung returned to his work.

But the silence broke after a mere two hours.

“What is that…?”

A black dot in the sky was gradually drawing closer. Spreading its enormous wings, the messenger hawk landed by the window of the office. It belonged to the Lower District Sect.

Jin Wikyung hurriedly stood and opened the tube fastened to the hawk’s leg. The moment he unfolded the letter, tiny writing caught his eye.

> Jopil, One Question, One Kill, and twenty members of a special detachment have appeared in Jeongyang.

“Jeongyang…!”

Beyond Jeongyang was Honju. Beyond Honju was Taiyuan. Even if they were a special detachment, he had never expected them to cover hundreds of li in only a few days.

That wasn’t all.

There were still family members from the branches who had not returned to the main family. What if the enemy was tracking them?

*Every moment counts.*

It didn’t take Jin Wikyung long to make a decision.

“Select fifty martial artists immediately and send them to Jeongyang. One Question, One Kill Jopil is a brutal Peak master. Bring our family members—”

He thought of the children.

Their small limbs. Their faces twisted in pain. Their vacant eyes.

Jin Wikyung clenched his teeth.

“Bring our family members home safely.”

“My lord.”

Wipeng’s expression had hardened. As if possessed by something, Jin Wikyung stared blankly at his face before speaking.

“Taekyung. Where did you say Taekyung went?”

His voice came out strained.

“……Jeongyang.”

[^1]: Mi-si is one of the traditional two-hour divisions of the day, corresponding roughly to 1–3 p.m.
## Chapter artifact 23

# Chapter 23

Jin Family of Taiyuan.

As its name suggests, its headquarters were in Taiyuan. But like a conglomerate in the real world, the Jin Family of Taiyuan’s influence was not limited to a single city.

The family had been established for two hundred years. It had long since expanded its sphere of influence by establishing branches in county towns scattered throughout Shanxi.



Scout the area near Jeongyang and return within five days.



That was the first mission assigned to the reconnaissance squad. When they heard the order, the squad members’ reactions fell into two categories.

“Doesn’t sound like much.”

Some, like Hyuk Mujin, were disappointed. Others, like Han Yeop, let out sighs of relief.

Of course, neither reaction pleased me.

Hyuk Mujin was caught up in a pointless hunger for glory, while Han Yeop was afraid of fighting.

*Still, I’d rather have a safe mission.*

Try running into the enemy with a bunch of guys like these. It was horrifying just to imagine. I’d be safer fighting on the front lines with people I could trust.

*Should I apply for a transfer?*

Suppressing a sigh, I raised my fist. It was one of the hand signals I had taught them earlier. It meant stop.

Snort.

The eleven horses moving at a moderate pace stopped with a chorus of snorts. Hyuk Mujin, riding to my right, spoke irritably.

“Why are we stopping?”

“Rest.”

“Again?”

“Two hours of travel, fifteen minutes of rest. Didn’t I tell you that beforehand?”

“I can keep going!”

“Then go by yourself.”

I jerked my chin toward the rear. The other squad members were breathing heavily. Riding a horse was faster than traveling on foot, but it consumed a considerable amount of stamina.

Hyuk Mujin’s much higher Level let him endure fairly well, but fatigue was accumulating in the others.

“Rest if I tell you to. That’s an order.”

Ignoring Hyuk Mujin’s crumpled face, I addressed the squad.

“Fifteen minutes of rest.”

They had fifteen minutes to rest, but the reconnaissance squad members didn’t look particularly happy. That was because I immediately pulled out a large leather backpack.

I reached into the backpack and thought,

*Open Inventory.*

With a clatter, three shields were summoned into the backpack.

The wooden shields had been coated with iron on the surface. I had taken them from the armory before leaving the Jin Family of Taiyuan. They were light, sturdy, and perfectly usable.

“Number Seven. Number Eight. Number Nine.”

The three designated reconnaissance squad members accepted the shields with faces that looked ready to die.

Those three had been forcibly selected by me as tanks.

*Seven damage dealers. Three tanks. And me.*

It was a party that would be wiped out the moment it entered a Gate, but for now, I had to be satisfied with this.

“Everyone to your positions.”

Next came formation.

“Basic formation.”

The three shield bearers stood at the front. Six swordsmen, from Number One Hyuk Mujin through Number Six, formed the second row. Han Yeop and I took the rear.

A formation focused on watching the front.

“Spread out. Scatter and assemble. Disperse.”

Their faces were still full of complaints, but they now carried out the commands fairly skillfully. At this point, they were much better than F-Rank Hunters who had just graduated from a Hunter training center.

*These NPCs are better than people.*

It was probably the difference created by the presence or absence of internal energy.

Unlike F-Rank Hunters, who couldn’t manipulate mana at all, Murim’s NPCs could use internal energy, however faintly.

They were merely low-Level and inexperienced.

I moved on to the final stage of formation training.

“All-out retreat.”

The reconnaissance squad members froze.

“What?”

“What does ‘all-out retreat’ mean?”

“It means exactly what it says. Retreat with all your strength.”

“Then what formation should we—?”

“By then, formation will be meaningless. Just run with all your strength. Don’t even look back. Scatter as much as possible.”

“Heh. You call that an order?”

The owner of the mocking voice was, naturally, Hyuk Mujin.

“I can’t stand this any longer. Third Young Master, is war some children’s game? If you want to make nonsense sound convincing, you should at least have read one military strategy manual before coming here.”

“A military strategy manual?”

“Yes, a military strategy manual! Retreating in good order is one of the most basic principles of warfare. What kind of nonsense are you spouting?”

Hyuk Mujin’s open defiance drew hesitant voices from the other reconnaissance squad members.

“He’s not wrong.”

“We aren’t government soldiers, so why are we practicing formations and being forced to carry shields…?”

“I’ve never heard of an all-out retreat.”

See? Everyone thinks the same way I do. Hyuk Mujin’s smug face seemed to say exactly that.

Then Han Yeop joined in, his voice wavering.

“I-I don’t think that way.”

“What?”

“The Third Young Master—I mean Squad Leader—must have a reason for doing this… right?”

“A reason?”

Hyuk Mujin glared at him.

“What reason could there be? The Third Young Master spent his youth drinking with women instead of training. He caused every kind of trouble despite being like that. And that’s not all. He was also the one who caused this war—”

“Enough.”

Hyuk Mujin flinched when I cut him off. He seemed to realize that he had made a mistake.

But some people were like that. When they needed to back down, they took another step forward instead.

“Wasn’t the Third Young Master the one who caused this war?”

Hyuk Mujin’s pride was too great for him to stop himself.

The words finally left his mouth, and a chilly silence descended.

Gulp.

Someone’s throat bobbed loudly. Nine pairs of eyes turned toward Hyuk Mujin and me.

“D-do you have something to say?”

Something to say? Of course I did.

“Everyone gets another fifteen minutes of rest.”

At the same time, I slapped Hyuk Mujin across the cheek with my flat palm.

Smack!

“One.”

His jaw twisted to the side. It was an ordinary slap, without even a trace of internal energy. His face was still dazed by the sudden turn of events when I struck him a second time.

“What the—!”

He wasn’t completely helpless, at least. He raised his arm to block.

What he had failed to account for was the difference in strength.

Smack!

“Two.”

Hyuk Mujin’s upper body slammed into the ground. He sprang back up, a palm print stamped onto one cheek like a tattoo.

It didn’t take long for his bewilderment to turn into rage.

“You fucking bastard!”

He was properly furious now. As he charged at me with his eyes bulging, I hooked his leg and tripped him. At the same time, I put force into my left hand and struck him.

Smack.

“Three.”

“Urgh.”

His legs seemed to give out, and he staggered. After taking three consecutive blows with this much force, it was only natural that his head would be rattled.

“What, were you saving your internal energy to boil soup?”

That got through to him. Strength filled his wavering legs, and power surged through his body. His eyes glared at me, venom dripping from them.

“You’ll regret this.”

“No, I won’t.”

I caught the fist flying toward my face.

Speed, strength, timing.

I could see all of them. Compared to Lee Seogeun, he was far behind.

“Four.”

Hyuk Mujin’s head snapped back. Sticky blood sprayed through the air in slow motion. His pupils were unfocused, and his legs hung limp.

Yet somehow, he didn’t fall. He couldn’t—not unless I let go of his fist.

“Five.”

Smack!

That was his limit. Hyuk Mujin could no longer endure and passed out. Something fell with a soft thud onto his body, sprawled out in a bizarre position.

*An eye?*

I raised my head toward the sky. The winter sky was raining down small white scraps of garbage.

“Rest is over. We’re leaving.”

I tossed out the words and turned away. Behind me, the reconnaissance squad members finally exhaled the breath they had been holding.



* * *



When Hyuk Mujin woke up two hours later, the first thing he did was charge at me.

“You fucking—!”

Smack. Thud.

“Move him.”

“Y-yes, sir!”

After another ringing slap, he passed out again. The other reconnaissance squad members dragged him into a corner of the cabin.

*A cabin. We got lucky.*

According to one squad member who knew the surrounding area well, we should have reached Jeongyang before sunset at the latest.

But there had been nothing we could do about the sudden blizzard, and this cabin was the only place we had managed to find.

Apparently, it was a hunter’s shelter known only to those in the know.

*It’s ridiculously small, but I’ll take it.*

The mission might be delayed, but this was a hundred times better than walking through the snow all night, collapsing from exhaustion, and then running into the enemy.

That was when—

“Squad Leader?”

It was Han Yeop. The squad members behind him glanced at me, watching my mood.

“What should we do now?”

“Hm? Sleep.”

“N-no, that’s not what I meant…”

As I looked at the fidgeting reconnaissance squad members, something suddenly occurred to me.

*Don’t tell me…*

“Do you want to train?”

Nod, nod.

Look at the vigorous nodding and those eyes full of passion.

*Seeing once, my ass—beating once is better than a hundred hearings.*

One beating really was better than explaining a hundred times.



* * *



It was around noon. A sword blade flashed in the sunlight. It was the only thing the martial artist could see.

“Urgh.”

Thud.

His knees buckled, and his face slammed into the frozen ground.

Blood poured from the gaping wound that stretched from his shoulder to his chest. It was a fatal injury. The martial artist knew he was going to die.

“The others… Please, let them live.”

His exhausted voice cut off abruptly. Looking at the martial artist’s wide-open eyes, a middle-aged man clicked his tongue.

“Good grief, you poor fool.”

What were you thinking, charging in like that?

The words that followed never reached the dead man. The fifty-odd wandering martial artists surrounding them snickered.

“Of all people, he had to run into the boss. What rotten luck.”

“Only an orthodox-faction bastard would keep playing the hero right to the end. What should we do, Boss?”

Their gleaming eyes turned toward the survivors. There were six or seven women and children huddled together.

“Great Hero, please spare the children.”

At the plea from the oldest-looking woman, the middle-aged man—Jopil, One Question, One Kill—smiled gently.

“I’m sorry, but what can I do? I’m no Great Hero.”

“But you’re still a person. How can you kill children who can’t even tell right from wrong?”

“Hah. For a woman, you have quite a bit of spirit. Wait. I heard that the family of the Sakju Branch Leader survived. Could it be…?”

“He is my husband.”

“Ah, so he is. I never imagined such a virtuous wife would belong to such a pathetic man.”

Jopil smiled broadly, and the woman’s expression hardened.

“You have no intention of sparing us.”

“Rest easy. I don’t have a taste for tormenting people.”

“The children…”

“This is a harsh world. How are little ones supposed to survive without their mother?”

“You’re worse than a beast.”

“I heard your last words.”

That was the signal.

Swordlight flashed, and screams rang out.

A short while later, the blood-soaked wandering martial artists tossed the corpses into the thickets in the mountains.

“Only the wild animals will feast tonight.”

The man with the tiny birdlike eyes muttered. He was Jopil’s right-hand man, a First Rate wandering martial artist known by the nickname Black Mountain Blade.

“We should feast, too. If we finish this job properly, what’s a mere thousand pieces of gold?”

Jopil laughed happily. The payment for this job would be enormous, but he was enjoying the situation itself.

“I never imagined the day would come when we’d hunt the Jin Family of Taiyuan.”

His dirty leather shoe stepped on the fallen martial artist’s corpse.

The martial artist had belonged to the Sakju Branch, one of the ten or so branches of the Jin Family of Taiyuan.

“Was that the last one?”

“No, Boss.”

“They’re slipping away like rats. How many?”

“Three in total. One martial artist and two children. They passed through Jeongyang only a few two-hour periods ago and are headed for Honju.”

“That’s troublesome. It’ll take half a day.”

“You don’t need to go yourself. I’ll take care of it.”

“Would you?”

A pleased smile spread across Jopil’s lips.

“Good. Take half of them with you. You have half a day. How does that sound?”

The answer had already been decided. Black Mountain Blade bowed deeply.
## Chapter artifact 24

# Chapter 24

He ran. It was the only thing he could do.

Even as his father and the people of the Sakju Branch who had been like family to him died one after another, there was only one thing a fourteen-year-old boy could do: run.

“Oppa, I’m cold.”

His little sister whimpered in his arms. The boy, Socheon, blew warm breath onto her hands, which had gone stiff with cold.

“We’re almost there, so just hold on a little longer. Okay?”

“When are we going home? Soyul wants to see Mom…”

“She visited yesterday, too.”

“You’re lying. Did you see her?”

“Of course I did.”

*In my dream.*

Socheon swallowed the words that followed.

His mother had appeared in his dream the night before, exactly as she had three days earlier. She had spent a long time stroking and gazing at Soyul, who had fallen asleep from exhaustion, before speaking.



*Survive. You must survive.*



Her voice still rang in his ears, and the sight of her back as she led the others away still shimmered before his eyes.

*What happened to Mother? Could she have…? No. That can’t be.*

It was then, as he struggled to suppress his ominous feelings, that he heard something.

Rustle.

“Who’s there?”

The sequence of movements came naturally: pulling his little sister close while drawing the dagger from inside his clothes.

After the night when his home had burned and he had witnessed countless deaths, the cheerful boy had gained the eyes of a wild beast.

“I’ll count to three. One, two…”

“It’s me.”

The dagger slowly lowered when a face suddenly appeared from the darkness.

“Uncle Gong?”

“Shh. Keep your voice down.”

The man called Uncle Gong was a middle-aged man with a weary face. He had been an old friend of Socheon’s father, the Branch Leader of the Sakju Branch, and was now the young siblings’ guide and protector.

“I was worried because you hadn’t returned for more than half a shichen.[^1]”

“I should have been more careful. We have a tail.”

“Already?”

“Yes. Every moment counts.”

Socheon stood without hesitation. Uncle Gong hoisted the bewildered Soyul onto his back and led the way through the brush.

“Where are we going?”

“Honju. No matter how cruel those bastards are, they won’t pursue us that far.”

*Will they really not chase us that far?*

Socheon had his doubts.

The Sakju Branch had already fallen. The building had burned, and everyone was dead. He did not know who the attackers were, but their purpose was clear.

*Massacre.*

He blew the word away with his breath and started walking again.

How long had they walked?

The white snow, which had been drifting down like sleet, had risen to their calves when—

“Quiet.”

Uncle Gong stopped walking. Socheon held his breath as well. The only sounds were the howling wind and the clatter of bare branches striking one another.

But Socheon knew instinctively.

“Is it them?”

Uncle Gong answered with a rigid expression.

“At least ten. They’ll catch up soon.”

The situation was bleak. Yet strangely, Socheon’s heart settled into a calm stillness.

“It was my fault. I should have hurried before the snow began… I curse the heavens.”

“You did everything you could, Uncle.”

Socheon drew the dagger from inside his clothes. It had been handed down to him by his father a year ago—the only trace his father had left behind.

“I’ve learned a little martial arts myself. I’ll fight and die like a martial artist.”

“…It’s too soon to give up.”

That was all Uncle Gong could say. They summoned what little strength they had left and started moving again.

But their stamina, pushed to its limit by days and nights of nonstop flight, dragged at their feet. Their steps grew slower, and their breathing became labored.

“There!”

“We’re almost on them!”

Now Socheon could hear them, too. The pursuers’ voices and their torchlight were drawing closer.

At that moment, Uncle Gong handed the soundly sleeping Soyul to Socheon.

“I’ll bring up the rear.”

“Uncle!”

“Don’t worry. This Gong Yacheong isn’t such an easy man to take down.”

“But how can you…”

“Go!”

Socheon left Gong Yacheong behind and started up the mountain again. His stamina was at its limit, but he did not stop.

When he reached a hill on the snow-covered mountain, the clash of weapons and someone’s scream rang out.

*Uncle Gong.*

Socheon gritted his teeth. He wanted to draw his dagger and leap down there immediately. But…

*Hold on. I have to hold on.*

He had repeated those words hundreds, thousands of times over the past five days. He had sworn that he would survive, protect the little sister in his arms, and take revenge on the murderers.

From the hilltop, Socheon stared at the flickering torches with eyes that seemed to pour fire.

*I will survive.*

Then he turned his back and climbed the hill. The next moment, his body shook as if struck by lightning.

“A-ah…”

Ten men in navy martial uniforms were looking at Socheon from the wide clearing atop the hill.

A single character, 陳—the character for Jin—was prominently embroidered in silk thread across their chests.



* * *

I sensed something strange just as we were about to begin training.

A sound carried faintly over the howling wind. When I raised my internal energy, the sound grew clearer.

*A human voice?*

There seemed to be more than ten people, at the very least. They were close enough that I wondered how I had failed to notice them until now.

*That many people in this weather…*

All right. I’d made up my mind.

“Pack your things.”

“Huh?”

The squad members, who had been preparing for training with their weapons in hand, looked at me blankly.

“Pack up, quickly. One of you, go inside and get Hyuk Mujin—”

“Squad Leader. There’s a kid over there.”

Damn it. There really was one.

A little boy carrying an even smaller child on his back was staring blankly at us.

“Who’s that?”

“I don’t know. Is he the owner of this cabin?”

*Please let that be the case.*

But why did I find it so hard to believe that the people following him were members of one happy, extended family?

“He’s crying.”

As someone pointed out, the boy was crying. He was running while sobbing his heart out.

The problem was where he was headed.

“Uh, he’s coming this way… Squad Leader, where are you going?”

Suspicious gazes turned toward me. I had already retreated a good distance.

“I’m going to ride a horse. We should be leaving soon.”

“In this weather? The horses won’t even be able to move.”

“Really? Then we’ll leave them behind.”

“What?”

“That’s how missions work. Snow or rain, we still have a job to do. Shut up and pack your things.”

“But still…”

“Pack your things! Wake Hyuk Mujin!”

The admiring looks I’d enjoyed barely fifteen minutes ago had now turned into the sort reserved for a lunatic.

“What’s gotten into you all of a sudden?”

*What’s gotten into me?*

I had a really bad feeling about this.

By now, I knew the signs. The closer the kid got, the stronger the stink of a huge shitshow grew.

I could see exactly how this would play out. There was only one way out.

“Then I’ll head down first by my—”

At that moment, the uninvited guests appeared over the hill amid a chorus of shouts.

There were more than twenty men.

*Oh, fuck.*

Ding.



> **System**
>
> - Sudden Quest has been created!
>
> **Quest**
>
> **Survivors of the Sakju Branch**
>
> You have encountered survivors from the Sakju Branch of the Jin Family of Taiyuan.
>
> Rescue the survivors from the Mount Heng Sword Sect’s merciless pursuers!
>
> **Rank:** Sudden Quest  
> **Limit:** Jin Taekyung  
> **Task:** Rescue the survivors — Incomplete  
> **Reward:** Chain Quest  
> ???  
> **Failure:** ???

“…”

“…”

We looked at them. They looked at us.

A deathly silence settled over the frozen clearing.

*I knew it. I knew this was how it would turn out.*

But regret was useless now. What could I do about my cursed luck?

I let out a deep sigh and shouted.

“Attack formation. Form up!”

Clack-clack-clack. The situation had taken us by surprise, but the squad members moved as they had been taught. By the time they had formed up, the enemy had realized who we were and started shouting.

“They’re brats from the Jin Family of Taiyuan!”

“There aren’t many of them. Wipe them out!”

*Brats. Outnumbered.*

Those facts, plucked out with surgical precision, tore at my chest.

I hadn’t even finished teaching them. Their martial arts were weak, they had no real combat experience, and they were complete rookies.

*If things go bad, should I bolt by myself?*

Feeling utterly hopeless, I used Qi Sense. Blue waves of qi visible only to me swept over the enemies charging forward with shrieks.

Ding. Ding. Ding.



> **System**
>
> - Level 12
> - Level 11
> - Level 12

“…Huh?”

The reconnaissance squad members turned deathly pale.

“What do we do?”

“They’re coming! They’re coming!”

“Squad Leadeeeer!”

As I watched the enemies rush toward us at incredible speed—thirty meters, twenty meters—I opened my mouth.

“Don’t worry. The enemy is nothing but simple EXP… I mean, a rabble. But!”

“But?”

“Stop them with everything you have. Just hold them back.”

“What? What do you mean?”

*What do I mean?*

*Don’t get the last hit.*

“Defensive formation. Form up!”

Yes. All the EXP was mine.



* * *

“Squad Leader!”

“No! Squad Leadeeeer!”

“The squad leader went to commit suicide!”

That wasn’t what I was doing, you lunatics.

I ignored the reconnaissance squad members’ screams and charged toward the enemies.

Internal energy surged from my dantian and spread through my limbs and bones.

“You crazy bastard.”

The enemy at the front grinned, baring yellow teeth.

I grinned back.

“Pretty boy.”

“What?”

Slash.

The man clutched his throat and collapsed. As I passed him, the voice I had been waiting for rang out.

Ding.



> **System**
>
> - You gained EXP.
> - You gained 50 Merit!

“What the—!”

“How dare this fucking bastard…”

The enemy’s appearances were impressive in their own way. Facial scars were standard equipment, and their poor hygiene produced a stench that stabbed at my nose.

And yet…

“Ah, this is great.”

I felt like I was in a flower garden.

Twenty flowers filled with the sweet honey of EXP.

I charged into them with a blissful expression and sucked out the honey.

Stab. Stab. Stab.

Ding. Ding. Ding.



> **System**
>
> - You gained EXP.
> - You gained 50 Merit!
> - You gained EXP…
> - You gained 50 Merit…
> - You gained EXP…
> - You gained 50 Merit…

I tore through them without restraint.

The front line collapsed in an instant, and the enemies instinctively began to falter.

*That works for me.*

The Jin Family’s Manoeuvre Technique and Spear Technique were martial arts based on pressing forward.

I advanced with the Manoeuvre Technique, bored into their center, and swung my spear.

“Gaaah!”

“Aaaargh!”

The spear was razor-sharp and massively heavy, and the technique was domineering to boot. On top of that, the enemies were steadily backing away.

It was time for the Jin Family’s Spear Technique to show its true worth.

*First form.*

I began swinging the spear in step with my footwork. Every swing and thrust brought forth someone’s scream and a burst of blood.

“Ghk.”

“Grrrgh.”

Second form. Third form. Fourth form.

At some point, I surrendered myself to the flow.

The ripples became waves, and the enemies were swept away by them. Every sense in my body stood on end.

More. More. More…

“You fucking bastard!”

Stab. Slash.

Throat, chest, abdomen.

I stabbed and cut them down one after another. The System alerts confirmed the fatalities for me.

How much time passed?

Only one person remained standing.

“Our boss will find you no matter what…”

I didn’t wait.

A wave was momentum. And the final wave burst from the tip of my spear.

The final form of the Jin Family’s Spear Technique:

*Cheongwan-il* (天貫軼).

Splurt!

The last man, the one with the narrow birdlike eyes, stared at his sword, which had been shattered into pieces, before dropping to his knees.

The center of his chest had burst open as if struck by a cannonball.

Ding.



> **System**
>
> - You defeated **Level 32 Black Mountain Blade**!
> - You completed the **Survivors** Quest!
> - A Chain Quest has been created!
> - You gain a large amount of EXP!
> - You gain a large amount of Merit!
> - You have leveled up!
> - You have leveled up!
> - You have leveled…

As the System alerts continued without pause, I rubbed my stomach.

“Buuurp.”

Ah, I’m stuffed.

[^1]: A shichen is a traditional Chinese time period of roughly two hours.
