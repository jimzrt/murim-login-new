# Retrospective Patch Plan — Chapters 0–8

Create bounded exact-text patches; do not return complete chapters. Every `old`
string must occur exactly once in the identified current chapter. `new` must be
finished replacement prose. Combine adjacent findings when useful, never alter
unreported text, and disposition every finding.

Return exactly one JSON object with no Markdown fence:

{
  "summary": "brief patch summary",
  "patches": [
    {"chapter": 1, "finding_ids": ["R0000-01"], "old": "exact old text", "new": "exact replacement"}
  ],
  "dispositions": [
    {"finding_id": "R0000-01", "status": "applied|rejected|unresolved", "reason": "specific reason"}
  ]
}

Reject a finding only when its proposed change is not supported by the supplied
source. Leave genuinely uncertain findings unresolved. Do not intensify or
sanitize register.

## Audit rubric

# Retrospective Translation Audit Rubric

Audit accepted chapters for defects likely to survive an ordinary review. Do
not retranslate acceptable prose or optimize merely for difference.

Prioritize in this order:

1. Reversed or altered actions, negation, subjects, identities, kinship,
   quantities, causal relations, and physical direction.
2. Omitted source beats, explanatory mechanisms, pragmatic cues, ambiguity,
   jokes, and characterization.
3. Established terminology, Murim concepts, hierarchy, and address.
4. Register mismatch: intensified or sanitized profanity, euphemisms made more
   explicit, stiffness, or flattened comic timing.
5. Clear English defects that materially impede voice or meaning.

Semantic fidelity outranks polish. Preserve the source's degree of explicitness.
Do not report optional synonyms, generic praise, or whole-chapter rewrites.
Every finding must quote an exact current-English span and recommend a bounded
correction. Mark a finding critical only when it reverses or changes a scene
fact, action, identity, negation, or consequence; major for meaningful lost
hierarchy, mechanism, characterization, ambiguity, or register; minor for clear
localized defects without changed meaning.

## Structured findings

```json
{
  "findings": [
    {
      "chapter": 2,
      "confidence": 1.0,
      "correction": "Replace with “Tài lěng le.”",
      "current": "“It’s so cold.”",
      "defect": "The Chinese dialogue is translated before the Universal Language Pack is applied, contradicting the immediately following statement that Taekyung cannot understand her words and weakening the language-barrier mechanism.",
      "id": "R0000-01",
      "rationale": "The source presents the line phonetically and in Chinese rather than as Korean dialogue; Taekyung explicitly remains unable to understand the woman until the language pack is applied.",
      "severity": "major",
      "source": "“타이렁러太冷了.”"
    },
    {
      "chapter": 4,
      "confidence": 1.0,
      "correction": "Change “Mount Odae” to “Mount Wutai” here and at its later occurrence in the chapter.",
      "current": "A local born and raised near Mount Odae, he had never once left the area.",
      "defect": "The translation uses the Korean geographic reading Mount Odae for 五臺山, misidentifying the setting’s Shanxi mountain.",
      "id": "R0000-02",
      "rationale": "五臺山 in Shanxi is Mount Wutai; Mount Odae denotes a different mountain in Korea.",
      "severity": "major",
      "source": "생전 오대산(五臺山) 인근을 벗어난 적 없는 토박이였고 약관 무렵부터 만만한 산객들을 대상으로 통행료를 뜯어내 왔다."
    },
    {
      "chapter": 4,
      "confidence": 1.0,
      "correction": "Replace with “At that moment, a cold wind blew.”",
      "current": "A cold silence fell.",
      "defect": "A literal gust of cold wind is replaced with figurative silence.",
      "id": "R0000-03",
      "rationale": "The source explicitly describes cold wind blowing; it does not mention silence.",
      "severity": "minor",
      "source": "순간, 싸늘한 찬바람이 불었다."
    },
    {
      "chapter": 4,
      "confidence": 0.99,
      "correction": "Retain the first spoken line, but render the second as internal thought: *Goblins?*",
      "current": "“They’re goblins?”\n\n“Goblins?”",
      "defect": "The second line is formatted as new spoken dialogue, apparently assigning knowledge of goblins to another character. In the source it is Taekyung’s unspoken incredulous reaction.",
      "id": "R0000-04",
      "rationale": "Only the first source line has quotation marks. Treating the second as dialogue invents a speaker and implies that someone in Murim recognizes a modern-world monster category.",
      "severity": "critical",
      "source": "“고블린이네?”\n\n고블린이여?"
    },
    {
      "chapter": 4,
      "confidence": 1.0,
      "correction": "Replace with “Critical One Strike! Status effect Bleeding activated!”",
      "current": "Critical hit! Status effect Bleeding activated!",
      "defect": "The System notification replaces the required established term One Strike with “hit.”",
      "id": "R0000-05",
      "rationale": "The supplied glossary requires 일격 to be rendered as One Strike.",
      "severity": "minor",
      "source": "- 치명적인 일격! 상태 이상 [출혈]이 발동됩니다!"
    },
    {
      "chapter": 5,
      "confidence": 0.98,
      "correction": "Replace with: *Where had he seen this traveler he was so grateful to before?*",
      "current": "*Where have I seen this grateful traveler before?*",
      "defect": "The adjective’s direction is reversed: the coachman is grateful to the traveler; the traveler is not described as feeling grateful.",
      "id": "R0005-01",
      "rationale": "고마운 modifies the traveler as someone for whom the coachman feels gratitude in the immediate context.",
      "severity": "minor",
      "source": "이 고마운 나그네를 어디서 봤더라."
    },
    {
      "chapter": 6,
      "confidence": 0.97,
      "correction": "Replace with: “What business could a pleasure house possibly have with our family?”",
      "current": "“What business could a pleasure house possibly have with the main family?”",
      "defect": "본가 is rendered as the impersonal branch-hierarchy term “the main family,” contrary to the established block terminology and Hyuk Mujin’s perspective as a member of the family.",
      "id": "R0006-01",
      "rationale": "Here 본가 refers deictically to the Jin Family to which the speaker belongs, not specifically to a main branch contrasted with a cadet branch.",
      "severity": "minor",
      "source": "기루에서 본가에 무슨 용무가 있다고?"
    },
    {
      "chapter": 7,
      "confidence": 0.98,
      "correction": "Replace “You’ve got one hell of a chin” with “You’re ridiculously tough” or “You can take one hell of a beating.”",
      "current": "“Fuck. You’ve got one hell of a chin. Let go! I said let go!”",
      "defect": "맷집 means overall toughness or ability to absorb punishment, not specifically having a strong chin.",
      "id": "R0007-01",
      "rationale": "The source characterizes Taekyung’s general durability after repeatedly getting back up; it does not single out resistance to jaw blows.",
      "severity": "minor",
      "source": "시발. 맷집만 더럽게 좋아 가지고. 놔! 안 놔!"
    },
    {
      "chapter": 8,
      "confidence": 1.0,
      "correction": "Replace “older brother” with “eldest brother.”",
      "current": "Jin Taekyung’s older brother and the Lesser Family Head of the Jin Family of Taiyuan, Jin Wikyung.",
      "defect": "“Older brother” omits the source’s explicit eldest-brother hierarchy.",
      "id": "R0008-01",
      "rationale": "큰형 specifically identifies Jin Wikyung as Taekyung’s eldest brother, distinguishing him from the second brother discussed immediately afterward.",
      "severity": "major",
      "source": "진태경의 큰형이자 태원진가의 소가주인 진위경이다."
    },
    {
      "chapter": 8,
      "confidence": 0.99,
      "correction": "Replace with: “Weren’t buildings like this usually called pavilions in China?” Maintain “pavilion” for later references to this residence.",
      "current": "Weren’t buildings like this usually called halls in China?",
      "defect": "The generic architectural term 전각 is rendered as “hall,” conflicting with the established term “pavilion.”",
      "id": "R0008-02",
      "rationale": "The glossary reserves “hall” for established named buildings; this is an unnamed residential pavilion.",
      "severity": "minor",
      "source": "보통 이런 건물을 중국에서는 전각이라고 하던가?"
    },
    {
      "chapter": 8,
      "confidence": 1.0,
      "correction": "Replace with: **The Night King: Well-Endowed Man**",
      "current": "**The Night King: Big-Dick Man**",
      "defect": "The translation intensifies the euphemistic crude slang 대물남 into explicit anatomical profanity.",
      "id": "R0008-03",
      "rationale": "대물남 is a suggestive euphemism, and the block glossary explicitly fixes it as “Well-Endowed Man” to preserve the source’s degree of explicitness.",
      "severity": "major",
      "source": "[야왕 대물남]"
    }
  ],
  "summary": "11 findings across 2 blocks",
  "version": 1
}
```

## Chapter 2

### Korean source

```text
＃2화



찬 바람이 얼굴에 닿았다. 나는 어릴 적부터 추위를 많이 타는 체질이라 사시사철 창문을 닫고 산다. 그럼 누가 창문을 열었단 말인가?

‘뻔하지.’

성진호, 이 원수 같은 인간.

투덜거리며 이불을 목 끝까지 끌어올렸다. 옆에 누운 여자가 작게 칭얼거렸다.

“……어?”

여자? 여자 누구?

순간 잠이 확 깼다. 나는 기상나팔 소리를 들은 이등병처럼 벌떡 일어났다. 그리고 천천히 고개를 돌렸다.

“타이렁러太冷了.”

세상에. 두 번 놀랐다. 첫 번째, 지금 이 상황을 이해할 수 없어서, 두 번째, 옆에 누워 있는 여자가 너무 예뻐서.

연신 알아들을 수 없는 말을 중얼거리면서 이불로 파고드는데, 정신이 없는 와중에도 가슴이 떨릴 정도로 아름답다.

때마침 불어온 찬 바람이 아니었다면 한참을 넋 놓고 바라봤을 것이다.

‘그런데 여기가 어디지?’

주위를 둘러봤다. 은은하게 감도는 붉은 촛불. 이상하게 자극적인 향기와 이불로 벗은 몸을 가린 미녀.

가 본 적은 없지만 어디선가 많이 들어 본 그곳.

‘룸살롱?’

아니, 근데 내가 왜 여기 있어?

그저 어리둥절하다. 뭐가 어떻게 된 거지? 어제는 진호 형이랑 한잔하고 고시원에 있는 내 방으로 돌아왔는데.

요란한 코골이 소리를 피해 캡슐로 들어간 것까지, 전날의 기억이 생생하다.

‘꿈을 꾸고 있나?’

팔뚝을 강하게 꼬집었다. 아프다. 꿈이 아니다.

점점 미궁으로 빠지는 상황이다. 멍하니 주위를 둘러보던 나는 여자의 어깨를 잡고 흔들었다.

“저, 저기요.”

여자가 게슴츠레한 눈으로 나를 바라봤다. 검푸른색으로 반짝이는 눈동자에 가슴이 또 쿵쾅거린다.

“누구세요?”

“션머?”

“아, 선미 씨구나. 그런데 제가 물어본 건 그 뜻이 아닌데……”

“션머?”

“예……?”

“션머……?”

뭐야, 이게.

잠시 흐르는 적막 속에서 우리는 서로를 응시했다. 그리고 깨달았다. 이 여자, 한국인이 아니다.

“혹시 중국인이세요? 아니면 필리핀?”

“……짜이나오런마?”

‘이건 뭐, 말이 안 통하네.’

답답함에 뒤통수를 벅벅 긁은 나는 다음 순간 용수철처럼 튀어 올랐다.

띠링.



읽지 않은 메시지를 확인하시겠습니까?

수락    /    거절



어디선가 들려온 종소리.

유령처럼 허공에 둥둥 떠 있는 네모난 창.

어디서 튀어나왔는지, 그전에 왜 이런 게 보이는지 짐작도 가지 않는다. 소름이 쫙 끼쳤다.

“시발, 뭐야 이거.”

억지로 쥐어 짜낸 목소리와 함께 반사적으로 주먹을 뻗었다.

주먹이 그대로 네모 창을 관통, 아니, 통과했다. 정확히는 [수락]이라는 단어를.

띠링.



- 오랫동안 응답이 없어 캐릭터를 랜덤 선택 합니다.

- [무림]을 탐색 중…… 캐릭터, [진태경]으로 플레이를 시작합니다!

- [무림]에 로그인했습니다.

- 최초 접속 보상이 주어집니다.

.

.

- 현재 사용 중인 플레이어의 언어를 변경할 수 있습니다. [통합 언어 팩]을 적용하시겠습니까?



캐릭터? 무림? 로그인?

“어? 어어?”



- [통합 언어 팩]이 적용됩니다.



“잠깐, 잠깐만!”

그때 여자가 말했다.

“진 공자. 어디 아파요?”

정확한 한국어 발음이다. 나는 [통합 언어 팩]이 적용됐다는 네모 창과 여자를 번갈아 보다가 생각했다.

뭐가 어떻게 돌아가는 거야?



* * *



월화(月華). 여자의 이름이다.

희고 매끄러운 피부에 주먹만 한 얼굴. 오밀조밀한 이목구비에 눈은 얼마나 크고 맑은지, 연예인 뺨 칠 정도다.

나는 다시 한번 감탄했다.

‘그래픽 끝내준다.’

대강의 상황 파악은 끝난 후였다. 몇 가지만 맞춰 보면 간단한 사실이었다.

무림. 캐릭터. 로그인. 플레이. 내가 마지막으로 잠든 곳은 게임 캡슐. 그리고 결정적으로.



메시지창을 여시겠습니까?

수락    /    거절



시스템창이 있다. 소리 내서 말해도 되고, 속으로 생각해도 된다. 머리를 긁는 것은 일종의 단축키다. 허공에 원하는 항목을 클릭하는 것도 가능하다.

‘이건 볼수록 신기하네.’

마지막으로 플레이한 게임과는 상당한 괴리감이 있지만, 이곳은 게임 안이다. 나는 지금 게임을 하고 있다.

‘그런데 언제 로그인이 됐지?’

선을 꽂아 뒀던 기억은 없는데. 전날의 기억을 떠올리려는 찰나, 월화가 불쑥 손을 내밀었다. 잡티 하나 없는 두 손에는 물이 가득 찬 대접이 들려 있다.

“마셔요. 잠이 덜 깬 것 같은데.”

‘인공지능도 끝내주네.’

월화의 얼굴을 힐끔거리면서 물을 들이켰다. 그리고 깜짝 놀랐다.

‘뭐야, 이거?’

냉수를 삼킬 때 느껴지는 청량감. 식도를 타고 배 속까지 시원해지는 느낌. 팔뚝에 닭살이 돋을 정도로 생생하다.

실사 그래픽에 NPC의 인공지능, 하다못해 냉수 한 모금을 마셔도 게임이라곤 믿기 힘들 정도였다.

이야, 요즘 기술이 엄청나다는 소문은 들었지만 이 정도일 줄이야. 게임 폐인이 생기는 이유를 알겠다.

‘이래서 가상현실, 가상현실 하는구나.’

놀이공원에 온 유치원생처럼 입을 벌리고 주위를 둘러보는데, 어디선가 매캐한 연기가 피어올라 눈 앞을 가렸다.

고개를 돌려보니 어느새 곰방대를 문 월화가 나를 물끄러미 바라보는 중이었다.

“왜……요?”

워낙 사람 같아서 나도 모르게 존댓말이 튀어나왔다. 물론 그녀가 엄청난 미인이라는 이유도 한몫했다.

월화는 연기를 후, 내뿜으며 대답했다.

“그냥. 보고 싶어서?”

얘는 얼굴만 예쁜 줄 알았더니 분위기도 장난 아니구나.

여고생들이 봤으면 언니를 외치며 쌍코피를 터뜨릴 정도의 포스다. 머리부터 발끝까지 딱 이렇게 쓰여 있다.

‘팜므파탈.’

캐릭터 컨셉 잘 잡았네. 월화만 보고 게임 시작하는 유저들도 꽤 있을 것 같다.

“진 공자, 오늘 좀 이상한 거 알아요?”

진 공자? 오글거리는 호칭이다. 하지만 나는 시치미를 뚝 뗐다. 뭐랄까, 조금은 이 상황을 즐기고 싶었다.

‘게임이니까.’

“뭐가요?”

“전부 다? 실성한 것처럼 허공을 바라보질 않나, 갑자기 존댓말을 쓰질 않나. 도무지 종잡을 수가 없네.”

월화가 말을 마친 순간이었다.

띠링.



- [튜토리얼 퀘스트]가 생성되었습니다.



게임 진행 방식이 참신하다. 보통은 다짜고짜 ‘드디어 정신이 들었군.’으로 시작해서 튜토리얼 퀘스트를 줬던 것 같은데.

이런 걸 자유도라고 하나?

‘어…… 퀘스트 확인?’

하면서도 이게 맞나 헷갈렸는데, 예의 효과음과 함께 곧바로 퀘스트창이 떴다.



퀘스트



[튜토리얼 - 1단계]

이제 당신은 무림에서의 첫발을 내딛습니다.

기본적인 정보를 수집하고 상황을 인지하십시오.



등급 : 튜토리얼 (연계 퀘스트)

제한 : 최초 접속자

임무 : 정보 수집 (미완료)

         상황 인지 (미완료)

보상 : 단단한 무복 세트

        캐릭터 상태창 활성화

        인벤토리 기능 활성화

        스킬창 기능 활성화

        연계 퀘스트





‘정보 파악, 상황 인지?’

게임을 많이 해 본 건 아니지만 이런 퀘스트는 또 처음이다.

보통은 토끼를 몇 마리 잡으라거나, 게임 인터페이스 사용법을 연습시키지 않나?

어쨌건 시도는 해 봐야지.

“나에 대해서 얼마나 알아요?”

내가 생각해도 단도직입적인 질문이다. 담배 연기 너머로 웃고 있는 월화의 얼굴이 보였다.

“재밌는 질문이네요. 소문 그대로라고 해야 하나?”

“소문?”

“공자도 익히 알고 있는 그런 이야기들이죠. 당사자 면전에 대고 말할 만큼 좋은 이야기는 아니지만.”

“괜찮으니까 들어나 봅시다.”

나는 점점 이 게임에 대해 흥미가 생기기 시작했다. 오랜만에 하는 게임이기도 했지만, 기존의 방식과는 다른 참신함 때문이었다. 어디서 만든 건지, 게임 한번 잘 만들었다.

“궁금해서 그래요. 내가 들은 소문이랑 같은지. 뭐 하루 이틀도 아닌데 기분 나쁘고 자시고가 있나.”

“……뭐 그렇다면야.”

물었군. 나는 내심 흐뭇하게 웃었다. 이제 본격적으로 정보를 캐낼 일만 남았다.

“첫 번째. 내가 누군지 알아요?”

아까보다 더 괴상해진 질문이었지만 월화는 순순히 대답했다. 이 상황을 즐기는 것 같기도 했다.

“올해로 약관이 된 태원진가의 막내 도련님. 이름까지 알려 드릴 필요는 없겠죠?”

나는 자신 있게 대답했다.

“압니다. 진태경.”

제 이름은 진태경. 태원진가의 막내죠.

내 자신만만한 대답을 들은 월화는 연기를 내뱉다 말고 사레가 들렸다.

“두 번째. 태원진가는 어떤 곳입니까?”

간신히 기침을 멈춘 월화가 대답했다.

“세간의 평판이 좋아요. 이따금 마적 떼 토벌도 하고, 가뭄이 오면 관아보다 먼저 구휼미를 풀기도 하니까.”

이게 끝?

내 실망을 알아차리기라도 한 것처럼 월화의 말이 이어졌다.

“무엇보다 산서성을 대표하는 명가(名家)죠. 뿌리 깊은 거목이랄까.”

“오오!”

나도 모르게 탄성을 터트렸다. 태원진가의 대단함에 감동한 게 아니라, 시스템 알림 때문이다.

띠링.



- [태원진가]에 대한 정보를 수집했습니다.

- 칭호, [명가의 자제]를 얻었습니다. 추후 상태창을 통해 확인할 수 있습니다.



‘칭호? 명가의 자제?’

판타지 장르 게임에서의 타이틀 같은 건가 보다.

‘드래곤 슬레이어라든지. 뭐 그런 거.’

일정 업적을 달성하면 주어지고, 타이틀을 장착하면 부가 효과가 따라붙는다. 그런 면에서 나 같은 경우에는 상당히 운이 좋다고 할 수 있겠다.

‘이거 완전히 금수저 캐릭터잖아.’

명문가에서 태어난 것 자체가 업적이라니. 열받으면서도 기쁘다. 제멋대로 선택된 랜덤 캐릭터가 로또였다는 말이니까. 그러나 이야기는 거기서 끝이 아니었다.

“하지만 요즘은 안팎으로 문제가 있다고 들었어요.”

“문제? 무슨 문제요?”

그러고 보니 퀘스트창의 정보 수집은 여전히 [미완료]인 상태다. 아직 남은 정보가 있다는 뜻.

“밖의 문제는 호시탐탐 산서성의 맹주 자리를 노리는 항산검문(恒山劍門)과의 대립이고, 안의 문제는…….”

월화는 느긋하게 담뱃재를 털어 냈다.

“그 집안 셋째 아들이 그렇게 망나니라고 하더라고요.”

“아하, 어딜 가든 그런 놈들이 꼭 하나씩 있죠.”

나는 무의식적으로 고개를 끄덕이다가 이상한 기분에 사로잡혔다.

“저기요.”

“네?”

“이건 정말 장난삼아 묻는 건데, 태원진가에 아들이 몇 명이죠?”

해맑은 웃음과 함께 대답이 돌아왔다.

“셋이요.”

태원진가에는 아들이 셋이고 내가 그중 막내인데, 셋째 아들이 망나니란다. 그러니까 그게.

‘시벌. 나네?’

띠링.



- 칭호, [가문의 수치]를 얻었습니다. 추후 상태창을 통해 확인할 수 있습니다.

- [정보 수집]을 완료했습니다.



이걸 웃어야 할지, 울어야 할지. 고민하다가 피식거리는 월화를 보고 나도 허허 웃어 버렸다.

그래. 좋은 게 좋은 거지. 가문의 수치면 뭐 어때. 어차피 게임인데.

나는 퀘스트창을 열어 정보 수집이 [완료]로 바뀐 것을 확인했다.

‘문제는 상황 인지인데.’

이놈의 퀘스트는 두루뭉술해서 정확히 뭘 요구하는 건지 모르겠다. 결국 해결책은 월화밖에 없나?

“여기가 어디죠?”

“홍화루, 산서 제일의 기루죠. 여긴 내 방이고.”

대화를 통해 추가로 자질구레한 사실들을 알 수 있었다.

이곳이 태원 중심부에 위치한 홍화루라는 것. 월화는 상당히 높은 직급의 기녀이며 나와 하룻밤을…… 흠흠.

별의별 이야기가 다 나왔음에도 불구하고 시스템 알림은 뜨지 않았고, 급기야 물어볼 것은 바닥이 드러났다.

마지막에는 이런 질문까지 할 정도로.

“제 지금 상황은요?”

월화가 한숨을 내쉬었다.

“진 공자. 이런 말 해서 미안한데, 지금 살짝 미친놈 같아. 좀 쉬는 게 어때요?”

그러게. 나도 미칠 것 같다.

창문 사이로 햇살이 비치는 걸 보고 있자니 이게 무슨 짓인가 싶다.

‘무슨 추리 게임도 아니고.’

그래픽, 인공지능, 뭐 다 좋은데 튜토리얼부터 막히니까 재미가 뚝 떨어진다. 그나마 한 가지 수확이 있다면 어제 주운 캡슐이 보기보다 좋은 물건이라는 사실이다.

이 정도 게임이면 상당한 고사양인데, 렉 한번 걸리지 않았다. 중고 시장에 올려도 괜찮겠지.

‘오늘부터 새 일자리도 구해 봐야 하고.’

그래도 뭐, 잠깐 플레이한 것치곤 나쁘지 않았다.

나는 마지막으로 월화에게 눈인사를 건네고 외쳤다.

“로그아웃!”

- 로그아웃이 불가능합니다.

어라?

“로그아웃.”

- 로그아웃이 불가능합니다.

이거 왜 이래.

오류? 아니면 고물 캡슐이 드디어 렉이 걸렸나?

“……로그아웃?”

- 로그아웃이 불가능합니다.

확실하다. 오류건 렉이건, 빌어먹을 고물 캡슐이 드디어 일을 냈다. 그 뒤로도 열 번을 더 시도했지만 모두 실패했다.

이쯤 되니 분노는 슬슬 걱정과 후회로 바뀌고 있었다.

‘이거 무슨 일 나는 거 아니야?’

공짜라고 막 주워 오지 말걸. 진호 형이 쓰레기라고 했을 때 바로 갖다 버릴걸. 아니면 정신병자 같은 사용 설명서를 읽자마자…….

‘아니. 잠깐만.’

사용 설명서. 맞아, 그걸 읽었었지. 정확히는 주의 사항만 몇 개 읽고 집어 던졌지만 읽긴 했다.

‘그게 무슨 내용이었지?’

그리고 가까스로 읽었던 주의 사항의 내용을 모두 떠올린 순간, 온몸에 오한이 들었다.



- 플레이어 임의로 로그아웃할 수 없습니다.

- 플레이 도중 사망 시, 부활할 수 없습니다.



게임 안에 갇혔다고? 내가?

질문에 대한 대답은 시스템 알림이 대신했다.

띠링.



- [상황 인지]를 완료했습니다.

- [튜토리얼 - 1단계]를 완료했습니다. 보상이 지급됩니다.

- [상태창]이 활성화됩니다.

- [스킬창]이 활성화됩니다.

- [인벤토리]가 활성화됩니다.

- 연계 퀘스트, [튜토리얼 - 2단계]가 생성되었습니다.



그 순간, 단 한 가지 생각만이 머리를 채웠다.

‘좆 됐다.’
```

### Current accepted English

```markdown
# Chapter 2

A cold wind brushed my face.

I’ve been sensitive to the cold since I was a kid, so I kept my windows closed all year round. So who had opened the window?

*Obviously.*

Seong Jinho, that miserable excuse for a human being.

Grumbling, I pulled the blanket up to my neck. The woman lying beside me let out a small whine.

“…Huh?”

*A woman? Which woman?*

I woke up in an instant and shot upright, like a private jolted awake by reveille. Then I slowly turned my head.

“It’s so cold.”

Good heavens. I was startled twice. First, because I couldn’t make sense of the situation. Second, because the woman lying beside me was unbelievably beautiful.

She kept muttering words I couldn’t understand and burrowed deeper beneath the blanket. Even in my dazed state, she was beautiful enough to make my heart tremble.

If that cold wind hadn’t blown in right then, I might have stared at her for quite a while.

*But where am I?*

I looked around. Red candlelight glowed softly around the room. A strangely stimulating fragrance filled the air, and a beautiful woman covered her naked body with a blanket.

A place I’d never visited but had heard about plenty of times.

*A room salon?[^1]*

But why was I here?

I was completely bewildered. What had happened? Yesterday, I’d had a drink with Jinho and returned to my room at the goshiwon.

I clearly remembered climbing into the capsule to escape Jinho’s thunderous snoring.

*Am I dreaming?*

I pinched my forearm hard. It hurt. This wasn’t a dream.

The situation was becoming more and more of a mystery. I stared blankly around the room, then grabbed the woman by the shoulder and shook her.

“Excuse me?”

The woman looked at me through half-lidded eyes. Her irises shimmered a dark blue, and my heart began pounding again.

“Who are you?”

“Shenme?”

“Ah, Ms. Sunmi. But that wasn’t what I meant…”

“Shenme?”

“…Yes?”

“Shenme…?”

*What the hell is this?*

For a moment, silence flowed between us as we stared at each other. Then I realized it. This woman wasn’t Korean.

“Are you Chinese? Or Filipino?”

“…Zhōngguó rén ma?”

*This is useless. We can’t communicate at all.*

I scratched vigorously at the back of my head in frustration. The next moment, I sprang up like a released coil.

Ding.

> **System**
>
> Would you like to check your unread messages?
>
> Accept / Decline

A bell rang from somewhere.

A square window floated in midair like a ghost.

I had no idea where it had come from—or, more importantly, why I could see something like this. Goose bumps rose all over my body.

“What the fuck is this?”

I thrust out my fist on reflex, forcing the words through my clenched voice.

My fist pierced the square window—or rather, passed through it. More precisely, it passed through the word *Accept*.

Ding.

> **System**
>
> No response for an extended period. Randomly selecting a character.
>
> Searching Murim… Starting play as character Jin Taekyung!
>
> Logged in to Murim.
>
> First-login rewards granted.
>
> You can change the language of the player currently in use. Apply the Universal Language Pack?

*A character? Murim? Login?*

“Huh? Huh?”

> **System**
>
> Applying the Universal Language Pack.

“Wait, hold on!”

That was when the woman spoke.

“Young Master Jin. Are you feeling ill?”

The pronunciation was perfectly Korean. I looked back and forth between the square window announcing that the Universal Language Pack had been applied and the woman, then thought:

*What the hell is going on?*

* * *

Wolhwa. That was the woman’s name.

She had smooth, pale skin and a face the size of my fist. Her delicate features were perfectly arranged, and her eyes were so large and clear that she could have put a celebrity to shame.

I admired her once again.

*The graphics are incredible.*

I’d already worked out the general situation. Once I put a few things together, the truth was simple.

Murim. Character. Login. Play. The last place I’d fallen asleep was inside a game capsule. And most importantly—

> **System**
>
> Would you like to open the message window?
>
> Accept / Decline

There was a System window. I could speak aloud or think my commands. Scratching my head acted as a kind of shortcut. I could even click the options I wanted in midair.

*The more I see, the more amazing this gets.*

It was a far cry from the last game I’d played, but this was a game. I was inside a game right now.

*But when did I log in?*

I didn’t remember plugging anything in. Just as I was trying to recall what had happened the night before, Wolhwa suddenly held out her hands. Both spotless hands held a bowl filled with water.

“Drink. You don’t seem fully awake yet.”

*The AI is incredible, too.*

I glanced at Wolhwa’s face as I drank the water, then nearly jumped out of my skin.

*What the hell?*

The refreshing sensation of cold water going down my throat. The feeling of coolness traveling down my esophagus and spreading through my stomach. It was so vivid that goose bumps rose on my forearms.

The lifelike graphics and the NPC’s artificial intelligence were one thing, but even a sip of cold water felt too real for this to be a game.

Wow. I’d heard that technology had advanced by leaps and bounds, but I never imagined it had come this far. Now I understood why people became gaming addicts.

*So this is why they call it virtual reality.*

I looked around with my mouth hanging open like a kindergartener at an amusement park. Then acrid smoke rose from somewhere and obscured my view.

I turned my head. Wolhwa was already watching me intently, a long-stemmed tobacco pipe between her lips.

“Why…?”

She seemed so much like a real person that I slipped into polite speech without thinking. Of course, the fact that she was stunningly beautiful had something to do with it.

Wolhwa exhaled a stream of smoke and answered.

“Just because. I wanted to see you?”

*I thought she was just a pretty face, but she had one hell of a presence, too.*

If a bunch of high school girls saw her, they’d be screaming “Big Sis!” while blood poured from both nostrils. From head to toe, she practically had one phrase written all over her.

*Femme fatale.*

*They really nailed her character concept. Plenty of players probably start the game just for Wolhwa.*

“Young Master Jin, did you know you’ve been acting strange today?”

*Young Master Jin? What an embarrassing way to be addressed.*

Still, I pretended not to notice. Somehow, I wanted to enjoy the situation a little.

*It’s a game, after all.*

“What do you mean?”

“Everything? You keep staring into empty air as if you’ve lost your mind, and now you’re suddenly speaking formally. I can’t make heads or tails of you.”

The instant Wolhwa finished speaking—

Ding.

> **System**
>
> Tutorial Quest created.

*The game’s progression is pretty innovative.*

Usually, games started with something like, “At last, you’re awake,” before immediately handing out a tutorial quest.

*Is this what they call freedom?*

“Uh… Check quest?”

Even as I said it, I wasn’t sure whether that was the right command. But with the familiar sound effect, a quest window appeared at once.

> **System**
>
> Quest
>
> Tutorial—Stage 1
>
> You are now taking your first step into Murim.
>
> Gather basic information and understand the situation.
>
> **Rank:** Tutorial (Chain Quest)
>
> **Restriction:** First-time players
>
> **Missions:** Gather information (Incomplete)
>
> Understand the situation (Incomplete)
>
> **Rewards:** Sturdy martial uniform set
>
> Character Status Window unlocked
>
> Inventory function unlocked
>
> Skill Window function unlocked
>
> Chain Quest

*Gather information? Understand the situation?*

I hadn’t played many games, but I’d never seen a quest like this before.

Usually, they had you kill a few rabbits or practice using the game interface.

Still, I had to give it a try.

“How much do you know about me?”

Even I thought it was a very blunt question. I could see Wolhwa smiling through the smoke from her pipe.

“That’s an interesting question. Should I say you’re just like the rumors?”

“Rumors?”

“The stories you already know so well, Young Master. They aren’t exactly flattering enough to tell you to your face.”

“That’s fine. Let’s hear them.”

I was growing more interested in this game by the minute. It was the first game I’d played in a long time, but more than that, its approach was refreshingly different from the usual. Whoever had made it knew how to build a game.

“I’m just curious whether they match the rumors I’ve heard. It’s not like this has only been going on for a day or two. Why would I get offended?”

“…If you insist.”

*Got her.*

I smiled inwardly, pleased. Now all that remained was to pry out some real information.

“First. Do you know who I am?”

It was an even stranger question than the one before, but Wolhwa answered without hesitation. She almost seemed to be enjoying the situation, too.

“The youngest son of the Jin Family of Taiyuan, who came of age at twenty this year. Surely I don’t need to tell you his name as well?”

I answered confidently.

“I know. Jin Taekyung.”

*My name is Jin Taekyung. I’m the youngest son of the Jin Family of Taiyuan.*

At my confident answer, Wolhwa choked on the smoke she was exhaling.

“Second. What kind of place is the Jin Family of Taiyuan?”

After barely managing to stop coughing, Wolhwa answered.

“They have a good reputation among the public. From time to time, they wipe out bands of mounted bandits, and when droughts come, they release relief grain before even the local government does.”

*That’s it?*

As if she had noticed my disappointment, Wolhwa continued.

“More than anything, they’re a prestigious family representing Shanxi. You could say they’re a deeply rooted old tree.”

“Oh!”

I let out an involuntary exclamation—not because I was moved by the greatness of the Jin Family of Taiyuan, but because of the System notification.

Ding.

> **System**
>
> Information about the Jin Family of Taiyuan gathered.
>
> Title Scion of a Prestigious Family acquired. Check it later through the Status Window.

*A title? Scion of a Prestigious Family?*

I guessed it was something like a title in a fantasy game.

*Dragon Slayer, or something like that.*

You received one after accomplishing a certain feat, and equipping it granted additional effects. In that respect, I had to say I was pretty lucky.

*This character is totally born with a silver spoon in his mouth.*

Being born into a prestigious family counted as an achievement. It pissed me off and made me happy at the same time. That meant the random character selected against my will had turned out to be a lottery winner. But the story didn’t end there.

“I’ve heard there are problems inside and outside the family these days.”

“Problems? What kind of problems?”

Come to think of it, the quest window’s information-gathering mission was still marked *Incomplete*. That meant there was more information to collect.

“Externally, there’s the conflict with the Mount Heng Sword Sect, which is constantly eyeing the position of Shanxi’s leader. Internally…”

Wolhwa leisurely tapped the ash from her pipe.

“I hear that family’s third son is a notorious good-for-nothing.”

“Ah. There’s always one of those wherever you go.”

I nodded unconsciously, then was seized by a strange feeling.

“Excuse me.”

“Yes?”

“This is just a joke, but how many sons does the Jin Family of Taiyuan have?”

She answered with a sunny smile.

“Three.”

The Jin Family of Taiyuan had three sons, and I was the youngest of them. But the third son was a notorious good-for-nothing. Which meant—

*Fuck. That’s me, isn’t it?*

Ding.

> **System**
>
> Title Shame of the Family acquired. Check it later through the Status Window.
>
> Gather Information complete.

Whether I should laugh or cry, I had no idea. When I saw Wolhwa snickering, I let out a hollow laugh too.

*Well, better to look on the bright side. So what if I’m the shame of the family? It’s only a game, anyway.*

I opened the quest window and confirmed that *Gather Information* had changed to *Complete*.

*The problem is understanding the situation.*

This damn quest was so vague that I had no idea what exactly it wanted. In the end, was Wolhwa my only solution?

“Where are we?”

“Honghwaru, the finest pleasure house in Shanxi. This is my room.”

Through our conversation, I learned a few more miscellaneous facts.

We were in Honghwaru, located in the center of Taiyuan. Wolhwa was a high-ranking courtesan, and I had spent the night with her… Ahem.

Despite all the various things we discussed, no System notification appeared. Eventually, I ran out of questions to ask.

At the very end, I was reduced to asking this:

“What’s my situation right now?”

Wolhwa sighed.

“Young Master Jin, I’m sorry to put it this way, but you seem a little crazy right now. How about getting some rest?”

*Well, I feel like I’m going crazy, too.*

As sunlight streamed through the window, I began to wonder what on earth I was doing.

*This isn’t some kind of mystery game.*

The graphics and artificial intelligence were all great, but being stuck at the tutorial had completely drained the fun out of it. If there was one thing I’d learned, it was that the capsule I’d found yesterday was a much better piece of equipment than it looked.

A game this advanced had to require serious hardware, yet I hadn’t experienced a single bit of lag. It should sell for a decent price on the used market.

*I need to start looking for a new job today, too.*

Still, the game had been fun for a little while.

I gave Wolhwa a final nod and shouted:

“Log out!”

> **System**
>
> Logging out is impossible.

*Huh?*

“Log out.”

> **System**
>
> Logging out is impossible.

*What’s going on?*

An error? Or had the ancient capsule finally started lagging?

“…Log out?”

> **System**
>
> Logging out is impossible.

There was no doubt about it. Error or lag, the damn old capsule had finally caused trouble. I tried ten more times after that, but every attempt failed.

By this point, my anger had gradually turned into worry and regret.

*Is something bad going to happen to me?*

*I shouldn’t have picked it up just because it was free. I should have thrown it away the moment Jinho called it garbage. Or at least, the moment I read that insane instruction manual…*

*No. Wait.*

The instruction manual. That was right—I’d read it. More precisely, I’d read a few of the warnings before tossing it aside, but I had read them.

*What did they say?*

The moment I finally remembered every warning I’d managed to read, a chill ran through my entire body.

> **System**
>
> The player cannot log out at will.
>
> If the player dies during gameplay, resurrection is impossible.

*I’m trapped inside the game? Me?*

The System notification answered my question for me.

Ding.

> **System**
>
> Understand the Situation complete.
>
> Tutorial—Stage 1 complete. Rewards will be distributed.
>
> Status Window activated.
>
> Skill Window activated.
>
> Inventory activated.
>
> Chain Quest Tutorial—Stage 2 created.

At that moment, a single thought filled my head.

*I’m fucked.*

[^1]: A room salon is a Korean private-room entertainment venue where customers are served food, alcohol, and conversation by hostesses.
```
## Chapter 4

### Korean source

```text
＃4화



장삼은 산적이다.

생전 오대산(五臺山) 인근을 벗어난 적 없는 토박이였고 약관 무렵부터 만만한 산객들을 대상으로 통행료를 뜯어내 왔다.

밤낮을 가리지 않는 성실 영업 덕분인지 언제부턴가 천력부 장삼, 하면 제법 알아주었다.

오늘도 그랬다. 꼭두새벽부터 일어나 충실한 다섯 부하, 오색귀(五色鬼)를 거느리고 영업을 나왔는데…… 이상하게 발걸음이 멈추지 않는다.

앞마당인 오대산을 한참 벗어나 얼마나 걸었을까, 마침내 발걸음이 멈췄을 때 저 멀리 다가오는 마차가 보였다.

‘어쩌다 여기까지 왔지?’

귀신에 홀렸나? 장삼은 어리둥절했지만 고급스러운 사두마차를 본 순간 자신의 직업 정신이 깨어나는 것을 느꼈다.

‘저건 꼭 뺏어야 해.’

장삼과 오색귀가 길을 막아서자 마부가 고삐를 잡아당겼다.

털에 윤기가 자르르 흐르는 준마 네 마리가 콧김을 뿜어내며 멈췄다. 척 봐도 마리당 천 냥은 거뜬하게 나올 물건들이다.

오늘은 일진이 좋군. 장삼은 흐뭇하게 웃으며 도끼를 고쳐 잡았다. 자, 이제 단전에 힘을 빡 주고. 하나, 둘.

“돈 내놔!”



* * *



발성 뭐야, 성악가야?

하지만 이 정도로는 눈 하나 깜짝 안 한다. 헌터 외길 인생 7년에 산전수전 공중전까지 다 겪은 나다.

……근데 좀 무섭다.

“총 여섯 명. 매복은 없어 보입니다.”

마부는 비밀 요원처럼 침착한 목소리로 상황을 전달했다.

이 아저씨는 믿는 구석이라도 있나. 왜 이렇게 여유롭지.

물끄러미 바라보자 머리를 긁적인다.

“간혹 있는 일입니다. 이 근방에서는 처음이지만요.”

“왜요?”

“왜긴요. 어지간한 대형 산채가 아닌 이상 무림세가를 건드리는 건 자살행위나 다름없습니다. 태원진가의 앞마당에서 도적질이라니, 어느 간 큰 놈들인지 궁금하군요.”

‘누구긴. 튜토리얼 NPC지.’

그보다 태원진가의 앞마당 운운하는 걸 보니 제법 가까운 거리인가 보다.

‘시간을 끌어 볼까?’

현재 내 경지는 이류.

스탯 분배 후 느껴지는 체감은 F급 헌터의 그것을 뛰어넘지만, 무림에서 먹힐 만한 수준인지는 모르겠다.

6 대 1. 마부까지 끼워 넣어도 6 대 2.

‘될까?’

중과부적이라는 말이 괜히 있는 게 아니다. 손발이 묶이는 순간 골로 간다.

“목적지까지 얼마나 남았습니까?”

“거의 다 왔습니다. 앞으로 반 시진이면 충분합니다.

반 시진이면…… 한 시간이나 남았다고?

짐작은 했지만 마부와 나의 ‘가깝다’는 서로 기준이 달랐다.

‘거의 다 오기는 무슨.’

대륙 배경이라 그런가. 스케일이 다르다, 스케일이.

어쨌든 그렇다면 이제 증원군은 없는 셈 쳐야 한다. 그나마 다행인 것은 혼자가 아니라는 점이다.

시종일관 여유로운 태도를 보이는 마부는 고수의 냄새를 풍겼다. 지금처럼.

“제가 처리할까요?”

그러면서 말채찍을 말아 쥐는데, 채찍질 한 번으로 산적들의 뼈와 살을 분리시킬 기세다.

‘고수다!’

그럼 그렇지. 내가 명색이 명문세가의 후계자요, 홍화루의 특급 고객인데 평범한 마부를 보내 줬을 리가 있나.

‘월화가 신경 써 줬구나. 얼굴만 예쁜 게 아니라 마음도 예쁘네.’

불안감이 사라지고 절로 흐뭇한 웃음이 지어진다. 내 웃음을 승낙의 의미로 받아들인 마부가 돌아섰을 때, 두 번째 고함이 터져 나왔다.

“이놈들! 이 천력부의 말이 들리지 않느냐!”

마차 창문 너머로 넘겨다보니 거대한 양날 도끼를 든 털북숭이가 소리를 치고 있었다. 우람한 상반신에 팔다리가 기둥처럼 두껍다.

하지만 마부는 가소롭다는 듯이 중얼거렸다.

“하룻강아지 같은 놈들이 어딜 감히.”

캬, 기세에 취한다.

그리고 마부의 준엄한 질타가 시작됐다.

“양민의 고혈을 빨아먹는 산적 따위가 감히 뉘 앞을 막아서느냐! 네놈을 관아로 압송하여 지엄한 국법으로 다스려 주마!”

판관 포청천 뺨치는 연설이었지만 털북숭이, 천력부와 그 부하들은 그리 감동한 것 같지 않았다.

“그래, 막아섰다. 이제 어쩔래?”

“무수한 악행을 저질러 온 네놈들의 눈알을 파내고 사지를 절구로 빻아 그 가루를 구주에 뿌려 주마! 또한 구족을 멸하여…….”

……형벌 수위가 장난이 아닌데. 거의 역모죄다, 역모죄.

내 생각을 읽은 것처럼 천력부가 입을 열었다.

“거, 안에 황족 나리라도 타셨소? 듣고 있자니 오금이 저려서 못 참겠네. 그 귀하신 얼굴 구경 좀 합시다.”

“이분의 정체를 알면 지금 물러나지 않은 것을 후회하게 될 것이다!”

“알겠어. 알겠으니까 이제 좀 나와 보라고.”

“어리석은 놈들……!”

마부가 혀를 차며 내게 고개를 돌렸다. 이제 드디어 진짜 무림 고수의 활약을 볼 수 있는 건가 싶어 가슴이 두근거린다.

“공자님. 나와 보셔야 할 것 같습니다.”

“응?”

나? 나 왜?

“관을 봐야 눈물을 흘릴 놈들입니다. 감히 공자의 앞을 막아서다니, 고수를 몰라본 죗값을 똑똑히 치르겠군요.”

그러면서 결의에 찬 표정으로 마차 문을 열어 준다.

“진천검(振天劍)의 위명은 익히 들었습니다. 불과 약관의 나이로 절정의 경지에 오른 천재 검수! 공자의 이야기를 들을 때마다 늙은 제 가슴이 얼마나 떨렸는지 모릅니다.”

……진천검? 천재 검수?

‘뭐라는 거야.’

머리가 뒤죽박죽이다. 진천검은 누구고, 절정에 오른 천재 검수는 누구며 이 마부는 뭐 하는 새끼인가?

처리하겠다며. 당신 고수 아니었어?

“이놈들! 이분이 누구신지 알아보겠느냐!”

틀렸다. 마부는 핸들이 고장 난 8톤 트럭처럼 폭주 중이다.

안 돼, 그만해. 멈춰!

마부의 손목을 꽉 움켜잡자 그가 나를 돌아본다.

다 안다는 듯한 웃음. 무한한 신뢰의 눈빛.

“자, 잠깐만. 저는 진…….”

내가 뭐라 할 틈도 없이 쩌렁쩌렁한 외침이 터져 나왔다.

“태원진가의 이공자, 산서성을 떨어 울리는 절정 고수! 진천검 진무경 공자이시다!”

“저는 진……태경인데요.”

순간, 싸늘한 찬바람이 불었다.

“예?”

“그러니까 저는 진무경이 아니라 진태경이고 이공자가 아니라 삼공자…….”

“……삼공자? 바로 그 삼공자?”

그래, 이 양반아.

마부의 동공이 흔들린다. 진도 8.0의 강진이다.

“그, 그럼 진무경 공자는요.”

“저야 모르죠.”

이 시간이면 자고 있지 않을까?

마부는 나라 잃은 표정으로 나를 바라보다가 바람 빠진 풍선 인형처럼 쓰러졌다. 졸도다.

‘시바. 고수는 무슨.’

마부의 손목을 놔줬다.

닭 뼈처럼 가느다란 손목이다. 잡는 순간부터 뭔가 쎄하다 싶었다. 그렇게 허세를 부려 놓고 일반인이라니.

“으하, 으하하하!”

산적들이 자지러지게 웃었다. 나? 언제 식은땀이 났는지 벌써 등허리가 축축하다.

‘이거, 진짜 재수 없으면.’

죽음이란 단어는 차마 꺼내지 못하고 꿀꺽 삼켰다.

나는 긴장 어린 눈으로 산적들을 훑었다.

시발. 차라리 고블린 여섯 마리랑 싸우고 말지. 저런 덩치들을 내가 어떻게 이겨…… 어라?

“엥?”

뭐야, 기분 탓인가? 하지만 아무리 봐도 기분 탓이 아니다.

우람한 상반신, 두꺼운 팔다리. 그리고…… 짧다.

옆에 다섯 놈도 별반 다르지 않다. 천력부는 몸이라도 좋지, 이놈들은 아무리 봐도 ‘건장한’이라는 단어와는 오백 광년쯤 차이가 있다.

그러니까 산적들의 체격이 꼭…….

“고블린이네?”

고블린이여?

예상치 못한 상황에 잠시 멍해 있다가 갑자기 날아오는 도끼에 정신을 차렸다. 머릿수도 많은 새끼들이 선제공격까지 하다니.

“야, 야! 잠깐만 타임!”

그 순간 도끼가 그대로 10m 앞 땅에 처박혔다. 아니, 고꾸라졌다. 도끼를 날린 산적이 쑥스러운 듯이 뒤통수를 긁적였다.

“조금 더 위로 던졌어야 했나?”

……이거 어쩌면.

‘살 수 있겠는데?’

7년 동안 가장 많이 상대한 몬스터를 꼽자면 고블린이다.

그러다 보니 놈들에 관한 모든 것을 속속들이 알게 됐다. 견습 헌터 시절에 주력 무기로 창을 선택한 것도 그 이유였다. 공격 범위에서 엄청난 우위를 점할 수 있으니까.

마침 산적들이 딱 그 정도 체격이다. 내 눈에는 산적이 아니라 고블린 여섯 마리로 보인다. 천력부는 대장 고블린 정도?

‘나머지 다섯은 고블린보다 약할 수도 있고.’

고블린은 독침이라도 잘 쏘지. 방금 도끼 던지는 꼴을 보아하니 촉이 온다. 촉이 와.

나는 바짝 마른 입술을 핥은 다음 두 손을 번쩍 들어 올렸다.

항복 의사에 몇 놈은 당황하고 천력부는 전역한 아들을 보는 아버지처럼 흐뭇하게 웃었다.

“기특한 놈일세.”

‘그래, 많이 웃어 둬라.’

한 발, 두 발. 천천히 30m에 이르는 거리를 좁혀 나간다.

일정한 보폭과 균형 잡힌 자세로. 한 발에 한 호흡. 입에서 김이 새벽 공기를 뚫고 새어 나왔다.

단순히 발을 내딛는 것만으로도 느껴진다.

‘다르다!’

다시 한번 깨달았다.

이 게임에서의 나는, 현실의 나보다 강하다.

가슴이 뛴다. 동시에 경각심이 고개를 쳐들었다.

마지막 순간까지 집중해야 한다.

“태원진가에 내놓은 자식이 있다는 풍문을 들었지. 무공은 삼류, 계집질은 일류라고. 오늘 보니 눈치도 제법이야.”

천력부가 말했다. 도끼를 쥔 손은 느슨하게 늘어트린 채다.

놈들의 눈에 내가 어떻게 보일지 뻔했다.

무공은 형편없는, 가문만 좋은 한량. 텅 빈 두 손.

천력부는 지금 방심했다.

‘그리고 방심은 죽음이지.’

가족들에게 월급 대부분을 보내고 고시원 단칸방에서 궁상맞게 살지만 나도 헌터다.

F급 헌터도 게이트에서는 목숨을 걸고 싸운다. 아니, 고작 F급이라 목숨을 걸고 싸워야 한다.

7년을 하루도 빠짐없이 싸워 온 승부사이자, 헌터라는 이름의 무림인이었다.

그래서 안다.

생사는 한 끗 차이라는 것을. 방심은 곧 죽음이라는 사실을.

남은 거리가 절반으로 좁혀졌다. 서서히 발걸음이 빨라진다.

천력부가 나를 향해 손짓한다.

“어허. 천천히 오게, 천천히. 오다가 넘어지기라도 하면 몸값 떨어져.”

20m.

“두목. 쫄래쫄래 걸어오는 꼴이 꼭 강아지 같지 않습니까?”

15m.

“강아지? 으허허! 네 말이 딱 맞다!”

10m.

다음 발을 내딛는 바로 그 순간, 뱃속이 뜨겁게 끓어올랐다.

난생처음 느껴 보는 생소한 감각. 그러나 묘하게 익숙한 이 느낌은 도대체 뭘까?

‘설마. 공력?’

단전에서 흘러나온 열기는 하반신을 향해 질주했다.

그 목적은 오로지 하나다. 좀 더 빠르게, 가볍게, 강하게!

훅. 길게 숨을 들이마신다. 온몸의 근육이 활시위처럼 팽팽하게 당겨졌다. 그리고 마지막, 한 걸음.

쾅!

정면을 향해 쏘아졌다. 지면이 움푹 패고 소리가 그 뒤를 잇는다. 정지된 시간 속, 천력부의 입이 천천히 벌어졌다.

“말도 안…….”

천력부도, 그 부하들도 믿을 수 없다는 표정이다.

놈들의 모든 것이 지금의 내게는 보였다. 느껴졌다.

빳빳하고 기름진 머리카락, 가뭄철 논바닥처럼 갈라진 입술과 보기만 해도 악취를 풍기는 이빨…….

그 모든 것들이.

나도 모르게 입꼬리가 올라갔다.

‘인벤토리 오픈. [예리한 창] 장착.’

허공을 향해 뻗은 손아귀에 서늘한 창자루가 잡혔다.

그대로 힘껏 내지른다. 엉겁결에 들어 올린 도끼가 창날을 막아 냈지만 예리한 창날은 도끼날을 그대로 부숴 버리고 천력부의 가슴을 관통했다.

동시에.



- 치명적인 일격! 상태 이상 [출혈]이 발동됩니다!



“커헉.”

피 분수가 터져 나왔다. 한차례 파르르 떨리던 천력부의 눈동자에서 빛이 사그라졌다.



- [Lv.10 장삼]을 처치했습니다.

- 레벨 업!

- 레벨 업의 보상으로 스탯 포인트 10을 획득했습니다.

- 레벨 업의 보상으로 스킬 포인트 10을 획득했습니다.

- [진가심법]의 잠금이 해제됩니다.



후우.

길게 숨을 내뱉었다. 알림이 울렸지만, 오롯이 심장 뛰는 소리만 내 안을 가득 채웠다.

한 호흡. 이 모든 일이 한 호흡 만에 벌어진 일이었다. 나는 숨이 끊긴 천력부의 가슴에서 창을 뽑아냈다.

‘이런 게 가능하단 말이지.’

포인트로 능력치를 올리고, 공력으로 강화하며 스킬로 연계한다. 이게 바로 나만이 가지고 있는 시스템의 힘이었다.

F급 헌터 진태경은 꿈꿀 수 없었던 힘.

‘할 수 있다. 반드시.’

돌아갈 길이 점점 밝고 넓게 보이기 시작한다.

나는 창 자루를 움켜쥐고 돌아섰다.

“그래서…….”

내게 못 박혀 있던 다섯 쌍의 시선이 위태롭게 흔들린다.

“더 덤빌 사람?”

아까 도끼 던진 새끼부터 나와.

“…….”

털썩. 털썩. 챙그랑.

눈치를 보던 다섯 놈이 무기를 버리고 넙죽 엎드렸다.

“용서해 주십시오. 대협!”



- 우두머리를 잃은 적들이 전의를 상실하고 항복합니다.

- [산적 퇴치]를 완료했습니다.

- 모든 피로와 부상이 회복됩니다.

- 산적을 토벌했습니다. 명성이 10 상승합니다.

- [튜토리얼 - 3단계]를 완료했습니다. 보상이 지급됩니다.

- 연계 퀘스트, [튜토리얼 - 4단계]가 생성되었습니다.



이제 숨 좀 돌리자.
```

### Current accepted English

```markdown
# Chapter 4

Jang Sam was a bandit.

A local born and raised near Mount Odae, he had never once left the area. Since around the age of twenty, he had made a living extorting tolls from travelers who looked easy to bully.

Perhaps thanks to his diligent round-the-clock operation, Jang Sam the Heavenly Axe had eventually become fairly well known.

Today was no different. He had risen before dawn and set out to work with his five loyal underlings, the Five-Colored Ghosts… but for some reason, his feet refused to stop.

How long had he walked, leaving his home turf of Mount Odae far behind? At last, when his feet finally stopped, he saw a carriage approaching in the distance.

*How did I get all the way here?*

Had a ghost possessed him? Jang Sam was bewildered, but the moment he saw the luxurious four-horse carriage, his professional instincts came roaring back to life.

*I have to take that.*

When Jang Sam and the Five-Colored Ghosts blocked the road, the coachman pulled on the reins.

Four fine steeds, their coats gleaming, snorted clouds of vapor as they came to a halt. At a glance, each one looked worth a thousand nyang at least.

*Today’s my lucky day.*

Jang Sam smiled contentedly and adjusted his grip on his axe. Now, tighten the muscles in the dantian. One, two—

“Hand over your money!”

* * *

*What was that voice? Is he an opera singer?*

But it would take more than that to make me blink. I’d spent seven years as a Hunter and been through every kind of hell imaginable—even aerial combat.

…Still, he was kind of scary.

“There are six of them in total. I don’t see any signs of an ambush.”

The coachman reported the situation in a voice as calm as a secret agent’s.

*Does this guy have some kind of hidden ace? Why is he so relaxed?*

When I stared at him, he scratched his head.

“It happens from time to time. Though this is a first in this area.”

“Why?”

“Why? Unless it’s a sizable mountain stronghold, attacking a martial family is practically suicide. I wonder what kind of reckless fools would try robbing people in the Jin Family of Taiyuan’s own backyard.”

*Who else? Tutorial NPCs.*

Judging by the way he kept calling it the Jin Family’s backyard, we must have been fairly close.

*Should I stall for time?*

My current realm was Second Rate.

The way my body felt after distributing my stats was beyond what I’d experienced as an F-rank Hunter, but I had no idea whether it was enough to hold its own in Murim.

Six against one. Six against two, if I counted the coachman.

*Could I do it?*

There was a reason people said numbers could overwhelm skill. The moment my hands and feet were tied, I’d be finished.

“How much farther to our destination?”

“We’re nearly there. Another hour should be enough.”

*Another hour…?*

I’d suspected it, but apparently, the coachman and I had very different definitions of *nearby*.

*What do you mean, nearly there?*

Maybe it was because this was a continent-sized setting. The scale was different. The scale.

Either way, I had to assume no reinforcements were coming. At least I wasn’t alone.

The coachman’s consistently relaxed attitude practically screamed that he was a master. Just like now.

“Shall I handle this?”

As he said it, he coiled the whip in his hand with enough force to suggest that one crack would separate the bandits’ bones from their flesh.

*He’s a master!*

Of course. I was a scion of a prestigious martial family and a VIP customer of Honghwaru. There was no way they would have sent an ordinary coachman with me.

*Wolhwa must have arranged this. She isn’t just beautiful—she’s kind, too.*

My anxiety vanished, replaced by a pleased smile. The coachman must have taken it as my permission, because the moment he turned away, a second shout rang out.

“You bastards! Can’t you hear what the Heavenly Axe is saying?”

I leaned out past the carriage window and saw a hairy man shouting while holding an enormous double-bladed axe. His upper body was massive, and his arms and legs were as thick as pillars.

But the coachman muttered as if the sight were laughable.

“Where do these little pups get off blocking our way?”

*Damn, that aura.*

Then the coachman laid into them.

“How dare bandits who suck the blood from innocent civilians block the road before us! I will have you dragged to the authorities and subjected to the full severity of the law!”

It was a speech worthy of Judge Bao, but the hairy man—the Heavenly Axe—and his underlings didn’t seem particularly moved.

“Yeah, we blocked the road. What are you going to do about it?”

“I will gouge out your eyes, grind your limbs to powder in a mortar, and scatter them across the Nine Provinces! I will also exterminate all nine degrees of your kin—”

*…Those punishments are getting a little extreme. That’s practically treason.*

As if he had read my thoughts, the Heavenly Axe spoke up.

“Hey, is there an imperial prince riding inside? Listening to you is making my knees shake. Why don’t you show us that precious face of yours?”

“You will regret not retreating now once you learn this man’s identity!”

“Okay, okay. We get it. Now come out already.”

“You fools…!”

The coachman clicked his tongue and turned toward me. My heart began to race. Was I finally about to see a true Murim master in action?

“Young Master, I believe you’ll have to come out.”

“Huh?”

*Me? Why me?*

“They won’t shed tears until they see the coffin. Blocking your path so brazenly—they’ll pay dearly for failing to recognize a master.”

With a determined expression, he opened the carriage door for me.

“I have heard much of the Heaven Shaking Sword’s fame. A genius swordsman who reached the Peak realm at barely twenty! You cannot imagine how my old heart trembled whenever I heard stories about you, Young Master.”

*…The Heaven Shaking Sword? A genius swordsman?*

My thoughts tangled together. Who was the Heaven Shaking Sword? Who was this genius swordsman who had reached the Peak realm? And what the hell was this coachman doing?

*You said you’d handle it. Aren’t you a master?*

“You bastards! Do you know who this man is?”

This was bad. The coachman was careening out of control like an eight-ton truck with a broken steering wheel.

*No. Stop. Please stop!*

I grabbed his wrist tightly, and he turned to look at me.

He smiled as if he knew everything. His eyes shone with boundless trust.

“W-wait. I’m Jin—”

Before I could say another word, his thunderous voice rang out.

“He is the Second Young Master of the Jin Family of Taiyuan, the Peak master whose name resounds throughout Shanxi! The Heaven Shaking Sword, Young Master Jin Mukyung!”

“I’m Jin…Taekyung.”

A cold silence fell.

“Pardon?”

“I mean, I’m Jin Taekyung, not Jin Mukyung. And I’m the Third Young Master, not the Second…”

“…The Third Young Master? That Third Young Master?”

*Yes, you idiot.*

The coachman’s pupils began to tremble. It was an earthquake measuring 8.0 on the Richter scale.

“Th-then where is Young Master Jin Mukyung?”

“How should I know?”

*He’s probably sleeping right now.*

The coachman stared at me with the expression of a man who had lost his country, then collapsed like an inflatable toy with the air let out of it.

He had fainted.

*Fuck. Some master.*

I released his wrist.

It was as thin as a chicken bone. Something had felt off from the moment I grabbed it. He had put on quite a show, only to turn out to be an ordinary civilian.

“Ha-ha! Ha-ha-ha!”

The bandits shrieked with laughter. As for me, my back was already damp with cold sweat. I hadn’t even noticed when it started.

*If things go really badly…*

I couldn’t bring myself to say the word *death*. I swallowed it instead.

I swept my tense gaze over the bandits.

*Fuck. I’d rather fight six goblins than deal with this. How am I supposed to beat bodies that huge…?*

Wait.

“Huh?”

Was it my imagination? No matter how I looked at them, it wasn’t.

Massive upper bodies. Thick arms and legs. And…short.

The other five weren’t much different. The Heavenly Axe at least had a decent physique, but these guys were five hundred light-years away from anything you could call “well-built.”

In other words, the bandits’ physiques looked a lot like—

“They’re goblins?”

“Goblins?”

I stood there dazed for a moment, but a flying axe snapped me back to reality. They had the numbers and they were launching a preemptive attack, too?

“Hey, hey! Wait a second!”

The axe slammed into the ground ten meters ahead of me. No—it toppled over. The bandit who had thrown it scratched the back of his head sheepishly.

“Should I have thrown it a little higher?”

*…Maybe.*

*Could I actually survive this?*

The monster I had fought more than any other over the past seven years was the goblin.

Naturally, I knew everything there was to know about them. It was even why I had chosen a spear as my primary weapon when I was a novice Hunter. A spear gave me an enormous advantage in attack range.

And these bandits were exactly that size. To me, they didn’t look like bandits at all. They looked like six goblins. The Heavenly Axe was the goblin chieftain.

*The other five might be even weaker than goblins.*

At least goblins could shoot poison darts. Judging by the way this one had thrown that axe, I had a hunch. A very strong hunch.

I licked my dry lips, then raised both hands high.

A few of them looked confused at my gesture of surrender, while the Heavenly Axe smiled proudly, like a father looking at a son freshly discharged from the military.

“Good lad.”

*Yeah. Enjoy your laugh while it lasts.*

One step, two. I slowly closed the thirty-meter distance between us.

With a steady stride and balanced posture. One breath per step. My breath escaped my mouth in white clouds that pierced the dawn air.

I could feel it from the simple act of putting one foot in front of the other.

*It’s different!*

I realized it once more.

The version of me inside this game was stronger than the real me.

My heart pounded. At the same time, a warning stirred in the back of my mind.

I had to stay focused until the very last moment.

“I heard the Jin Family had a son they’d given up on. Third Rate at martial arts, First Rate with women. Looks like you’ve got decent instincts, too.”

The Heavenly Axe spoke with the hand holding his axe hanging loose at his side.

I knew exactly how I looked to them.

A useless playboy with a good family name. Empty hands.

The Heavenly Axe had let his guard down.

*And letting your guard down gets you killed.*

I might send most of my salary to my family and live miserably in a tiny goshiwon room, but I was still a Hunter.

Even an F-rank Hunter risked his life fighting inside Gates. No—an F-rank Hunter had to risk his life precisely because he was only F-rank.

I was a fighter who had battled every day for seven years without missing one, a martial artist in all but name.

So I knew.

Life and death were separated by a hair’s breadth. Letting your guard down was the same as dying.

The distance had been cut in half. My steps gradually quickened.

The Heavenly Axe beckoned me over.

“Now, now. Take your time. Don’t lower your price by tripping on the way.”

Twenty meters.

“Boss, doesn’t the way he’s toddling over look just like a puppy?”

Fifteen meters.

“A puppy? Ha-ha-ha! You’ve got that exactly right!”

Ten meters.

The moment I took my next step, something hot began to churn in my stomach.

It was a sensation I had never experienced before, yet somehow, it felt strangely familiar. What was it?

*Could it be…internal energy?*

The heat flowing from my dantian raced toward my lower body.

It had only one purpose: to make me faster, lighter, stronger!

Whoosh. I drew in a long breath. Every muscle in my body drew taut like a bowstring. Then came the final step.

Boom!

I shot straight forward. The ground sank beneath my foot, and the sound followed after me. In frozen time, the Heavenly Axe’s mouth slowly fell open.

“No way…”

The Heavenly Axe and his underlings wore expressions of disbelief.

I could see everything about them now. Feel it.

Their stiff, greasy hair. Their cracked lips, like a rice paddy in a drought. Their teeth that reeked just from looking at them…

I could see all of it.

The corners of my mouth lifted before I knew it.

*Open Inventory. Equip [Sharp Spear].*

A cold spear shaft appeared in the hand I had thrust into empty air.

I drove it forward with all my strength. The Heavenly Axe hastily raised his axe to block, but the sharp spearhead shattered the axe blade and punched straight through his chest.

At the same time—

> **System**
>
> Critical hit! Status effect Bleeding activated!

“Ghk!”

A fountain of blood erupted. The Heavenly Axe’s eyes flickered once, then went dark.

> **System**
>
> Lv. 10 Jang Sam defeated.
>
> Level up!
>
> You received 10 Stat Points as a level-up reward.
>
> You received 10 Skill Points as a level-up reward.
>
> Jin Family’s Cultivation Technique unlocked.

*Whew.*

I let out a long breath. A notification had sounded, but all I could hear was my own pounding heart.

One breath. Everything had happened in a single breath. I pulled the spear from the Heavenly Axe’s lifeless chest.

*So this is possible.*

Raise my abilities with points, reinforce them with internal energy, and chain them together with skills. This was the power of the System—the one power that belonged to me alone.

A power F-rank Hunter Jin Taekyung could never have dreamed of.

*I can do this. I will.*

The road home was beginning to look brighter and wider.

I gripped the spear shaft and turned around.

“So…”

The five pairs of eyes fixed on me trembled precariously.

“Who else wants to try me?”

*Start with the bastard who threw that axe.*

“…”

Thud. Thud. Clatter.

The five bandits exchanged glances, then dropped their weapons and prostrated themselves.

“Please forgive us, Great Hero!”

> **System**
>
> The enemies have lost their will to fight and surrendered after losing their leader.
>
> Defeat the Bandits complete.
>
> You have fully recovered from all fatigue and injuries.
>
> You have subdued the bandits. Fame increased by 10.
>
> Tutorial—Stage 3 complete. Rewards will be distributed.
>
> Chain Quest Tutorial—Stage 4 created.

*Now I can finally catch my breath.*
```
## Chapter 5

### Korean source

```text
＃5화



“하나에 착하게. 둘에 살자. 자, 하나.”

“착하게!”

“둘.”

“살자!”

“목소리가 작다.”

“착하게엑!”

지옥인가?

마부가 정신을 차린 직후 처음으로 한 생각이다. 몸은 물먹은 솜처럼 무겁고 머릿속은 빙빙 돌았다. 그사이에도 저 멀리 비명 같은 외침은 계속됐다.

“살자악!”

“더 크게!”

……지옥이 틀림없다. 저승사자의 냉혹한 음성이 들리고 난 후면 어김없이 망자들의 비명이 따라붙었다.

“착하게엑!”

그는 눈을 감은 채 통한의 눈물을 흘렸다. 지옥에 오다니. 이렇게 비명횡사할 줄 알았으면 절간에 시주라도 많이 할걸.

‘아이고, 어머니!’

마부는 꺼이꺼이 울기 시작했다. 누군가 자신을 가만히 내려다보는 것도 알아채지 못할 정도였다.

“저기요.”

찰나의 시간, 잠시 멈췄던 마부의 심장이 다시 펄떡거리며 뛰기 시작했다. 그는 놀란 가슴을 부여잡고 빽 소리쳤다.

“놀라서 죽을 뻔했잖아!”

“…….”

“……?”

말하고 보니 뭔가 이상하다. 마부는 멍한 얼굴로 가슴에 손을 올렸다. 뛴다. 심장이 뛰고 있다.

그뿐인가. 말들도 있고, 마차도 있다. 초겨울 찬 바람에 몸이 으슬으슬 떨린다.

“살았네?”

설마, 하는 마음에 돌아보니 한쪽 눈이 시퍼렇게 멍든 남자가 서 있었다. 어째 표정이 괴상했지만…… 틀림없다. 산 사람이다.

나는 살아 있다!

“살았다! 나는 살았다!”

격렬한 기쁨의 포옹에 남자가 마부를 밀어 내며 떨떠름하게 대답했다.

“축하합니다.”

“흑. 흑흑. 정말 감사합니다. 그런데 누구…….”

“아, 그. 아까 잠깐 뵀었는데.”

아까? 아까 누구? 홍화루 사람들이야 다 아는 얼굴이고 태원진가의 망나니가 오늘의 첫 손님이었다.

이 고마운 나그네를 어디서 봤더라. 뚫어져라 얼굴을 바라보던 마부가 일순 숨을 들이켰다.

“아까 그 산적!”

“예. 그게 바로 접니…….”

“덩치 큰 놈 옆에 있던! 멍청하게 생긴 다섯 놈!”

“……맞습니다.”

“그중에 제일 키 작고!”

“…….”

“제일 못생겼고!”

“…….”

“물건도 작은 놈!”

“아니야!”

산적의 외침과 함께 마부가 정신을 차렸다. 내가 방금 무슨 말을 한 거지? 이내 후회와 절망이 밀물처럼 밀려든다.

‘이제 진짜 죽었다.’

차라리 이미 죽은 거라면 좋겠다. 적어도 고통은 없을 테니까.

그런데.

“후. 헛소리 그만하고 따라오기나 하쇼.”

흉신악살 같던 산적이 순식간에 화를 가라앉히더니, 앞장서서 걷기 시작했다. 엉겁결에 뒤를 따르게 된 마부는 기시감을 느꼈다.

‘이거 꼭 안내받는 것 같네.’

기절하기 전에 비하면 얌전하다 못해 정중한 태도다. 마부는 모든 용기를 쥐어짜 입을 열었다.

“저어, 지금 어디 가는 겁니까?”

“대형께 갑니다.”

마부의 얼굴이 새하얗게 질렸다. 천력부에게 했던 말이 생각나서다. 눈알을 파고, 사지를 절구로 빻아서…….

‘지금이라도 도망쳐야 해.’

하지만 다음 순간, 다리가 후들후들 떨리고 식은땀이 비처럼 쏟아졌다. 한 발자국도 움직일 수 없었다.

사방에 튀어 있는 검붉은 핏물들. 길옆 풀숲에는 시체로 보이는 다리가 불쑥 튀어나와 있었다.

‘이런 미친놈들.’

설마 했지만 대낮에 사람을, 그것도 태원진가의 자제를 죽이다니. 마부는 죽음을 직감했다.

풀숲을 헤치고 한 사람이 걸어 나오기 전까지는.

“어, 깨어나셨네?”

뒤로는 어깨동무를 한 산적들이 숨을 헐떡이는 중이었다.

사이좋게 눈가에 멍 하나씩을 달고서.

“뭐 해, 인마. 동료들 개고생하고 있는 거 안 보여? 합류해.”

“넵, 대형.”

“저 새끼가 진짜. 대형이라고 부르지 말랬지.”

멍하니 상황을 지켜보던 마부는 생각했다.

일단 목숨은 건졌다.



* * *



“그래서 이렇게 된 겁니다.”

이야기를 들은 마부의 눈동자가 후레쉬처럼 반짝였다.

어후, 눈뽕. 눈이 부셔서 마주 보기도 힘드네.

“저어, 혹시.”

혹시?

“정말 진무경 공자 아니십니까?”

“……제발 그만 좀.”

진태경이라고 몇 번을 말하냐.

여러모로 사람 환장하게 만드는 NPC다. 이걸 인공지능 기술의 업적으로 봐야 할지, 실패로 봐야 할지.

내가 마차만 몰 줄 알았어도 진작 버리고 갔다.

“준비는 다 끝났어요?”

마부가 마지막 매듭을 지으며 대답했다.

“예. 이제 다 끝났습니다.”

무슨 매듭이냐고? 산적 다섯의 손발을 꽁꽁 묶은 밧줄 매듭이다. 얼마나 꽉 묶었는지 구슬픈 신음이 끊이지 않는다.

“대형. 조금만 느슨하게 풀어 주시면 안 될까요?”

“응. 안 돼. 안 바꿔 줘. 여기 있어.”

“부디 이 아우들에게 대형을 모실 기회를…….”

“한 번만 더 대형이라고 하면 염라대왕 모시게 해 준다.”

침묵을 뒤로하고 마차에 올랐다.

놈들이 갖고 있던 무기는 진작 압수해서 인벤토리에 넣어 놨고, 레벨 업 효과로 몸 상태는 최고다.

“출발하겠습니다.”

마부가 고삐를 쥐자 사두마차가 움직이기 시작했다.

뒷산 등산로만큼이나 잘 닦인 산길이다. 마차 창문으로 선선한 바람과 산 공기가 흘러들어 왔다.

‘아무리 봐도 신기해.’

나는 고개를 절레절레 저었다.

과학. 기술. 뭐라 부르든 내게는 이해 불가의 영역이다.

더군다나 지금 상황에는 이런 생각도 사치다.

‘빌어먹을. 이 게임은 도대체 시간 배율이 어떻게 돼먹은 거야?’

가상현실 게임에는 시간 배율이라는 게 있다. 현실과 가상의 시간 배율이 1:3이라고 한다면 가상현실에서 세 시간을 있어도 현실에서는 한 시간밖에 흐르지 않는다.

내가 굳이 홍화루에서 사흘을 버틴 것도 그 이유에서다.

이쯤이면 누가 꺼내 주겠지, 하는 희망.

‘성진호 이 인간은 도대체 뭘 하는 건지.’

깊은 한숨이 흘러나왔다. 동시에 슬며시 불안감이 고개를 쳐든다.

이거, 시간 배율이 엄청나게 차이 나는 거 아니야?

‘설마.’

그럴 리 없다. 전에 진호 형이 했던 말로는 시간 배율은 캡슐의 성능과 가격에 비례한다고 했다. 이따위 고물 캡슐은 턱도 없다.

물론 생각보다 성능이 좋긴 하지만.

‘아니, 이 정도면 엄청 좋지.’

몇 년째 게임과 담쌓은 나지만 이 정도도 모를 만큼 까막눈은 아니다. [무림]은 분명 상당한 고사양 게임이지만, 고물 캡슐은 무리 없이 작동하고 있다.

그것만으로도 충분히 놀랍다. 그러니까.

‘이제 더 이상 놀랄 일 좀 없게 해라.’

제발. 그 말을 주문처럼 중얼거리고 스킬창을 열었다.



스킬창



[LV.11 진태경]

심법 : 진가심법

무공 : 진가창법 / 진가보법 (사용 불가)

근골 : 70

근맥 : 50

잔여 포인트 : 10

- 잔여 포인트를 분배하십시오.

- 오랫동안 무공 수련을 하지 않아 구결을 잊은 상태입니다.

- 보유 스킬에 관한 정보를 열람할 수 있습니다.





다시 봐도 놀랍다. 수련을 안 해서 무공을 쓸 수 없다니.

‘얼마나 놀았으면.’

한숨과 함께 다음으로 넘어갔다. 첫 번째는 잔여 포인트다.

레벨이 1씩 오를 때마다 10포인트씩 주어지는 모양이다. 아마 상태창도 마찬가지겠지.

‘스킬창과 상태창을 합치면 레벨 업 한 번에 20포인트인가?’

뭔가 애매한 수치인데. 나는 능력치 분배를 뒤로 미뤄 두고 마지막 문장을 터치했다.



- 보유 스킬을 열람하시겠습니까?



‘전부 열람.’

띠링.



스킬창



[진가창법]

등급 : 일류

제한 : [진가심법]을 익힌 자

경지 : 알 수 없음

효과 : 알 수 없음

설명 : 태원진가의 가전 무공. 비급을 통해 습득 가능하다. 현재 구결을 잊어 사용할 수 없다.





스킬창



[진가보법]

등급 : 일류

제한 : [진가심법]을 익힌 자

경지 : 알 수 없음

효과 : 알 수 없음

설명 : 태원진가의 가전 무공. 비급을 통해 습득 가능하다. 현재 구결을 잊어 사용할 수 없다.





스킬창



[진가심법]

등급 : 절정

제한 : 태원진가의 직계

경지 : 이 성

효과 : [운기조식]으로 공력을 운용, 축적할 수 있다.

설명 : 안정성이 매우 뛰어나나 공력 축적 속도가 느리다.





‘음.’

우선 가장 먼저 눈이 가는 곳은 등급이었다.

창법과 보법은 일류. 진가심법만 절정 등급이다. 경지와 효과가 명확하게 적혀 있는 것도 심법뿐이다.

‘진가창법, 보법은 써 보지도 못했고. 진가심법은…… 괜찮네.’

공력이 쌓이는 속도가 무슨 상관이냐. 매우 뛰어난 안정성. 그거 하나면 된 거지. 내 인생 모토가 가늘고 길게다.

그런 생각을 하고 있을 때였다.

띠링.



퀘스트



[튜토리얼 - 4단계]

이제 당신은 운기조식을 사용하여 공력을 다룰 수 있습니다.

그러나 통제되지 않는 공력은 양날의 검.

마지막까지 긴장의 끈을 놓지 마십시오!



등급 : 튜토리얼 (최종)

제한 : 최초 접속자

임무 : 운기조식 (미완료)

보상 : 아이템 상자

         [기감] 획득

         [메인 퀘스트] 오픈

실패 : 상태 이상 [주화입마] or [사망]



퀘스트를 수락하시겠습니까?

수락    /    거부



나는 망설임 없이 대답했다.

‘응. 안 해.’

보상? 그까짓 거 안 받아도 된다. 미친놈들이 장난질을 쳐도 정도가 있지. 게임 아이템이랑 목숨을 두고 딜을 걸어?



- 대답이 지연되고 있습니다.



얕은 수작 부리는 거 보소. 나는 마부의 시선도 아랑곳하지 않고 또박또박 발음했다.

“거. 부.”



- 튜토리얼 퀘스트는 거부할 수 없습니다.



“……?”



퀘스트를 수락하시겠습니까?

수락    /    수락



“거부한다고! 왜 수락만 두 개야!”



- 퀘스트가 강제 수락 되었습니다!



“야! 이 개새끼들아!”

끝내 참았던 쌍욕이 터져 나왔다.



* * *



- [운기조식]을 시작합니다.

- [진가심법]의 효과로 안정성이 대폭 상승합니다.



지금처럼 가족이 그리운 적이 없다. 사랑하는 우리 엄마. 사랑스러운 여동생……과는 거리가 있는 지랄맞은 하연이.

오빠가 나가면 치킨 배 터지게 먹여 주마.

‘나가기만 하면.’



- 최초 1회에 한하여 운기조식 도우미가 실행됩니다.



이건 뭐 칼빵 놓고 약 발라 주는 것도 아니고…….



도우미 시스템을 생략하시겠습니까?

수락    /    거부



나는 파르르 떨리는 시선을 메시지창에 고정시켰다.

“거, 거부.”



- 계속 실행합니다.



방금 우연이겠지? 그래, 우연이었을 거야.

찜찜한 기분이 채 사라지기도 전에 시야가 뒤집혔다.

그리고 정신을 차린 곳은. 낯선 회색 공간이었다.

- 이리로.

화들짝 놀라 고개를 돌리니 웬 노인이 손짓하고 있었다.

꿈속에서 저렇게 생긴 할아버지가 오라고 하면 냅다 도망가겠지만 여긴 게임이다.

‘저 노인이 도우미구나.’

그런 계산이 없었어도 별 의심 없이 따라갔을 것이다.

스스로 생각하기에도 이상한 일이었지만 그런 생각이 들었다. 왠지 모를 친근감. 그리고 신뢰.

- 가장 편안한 자세를 잡아라.

엥? 운기조식하면 가부좌 아닌가?

내 생각을 읽은 것처럼 노인이 대꾸했다.

- 원래 약한 놈들이 이것저것 따지지, 고수는 그런 거 없다.

담담한 말투에서 냄새가 난다. 냄새가 나.

이건 고수의 냄새다. 이번엔 진짜가 나타났다!

- 어허. 그놈 참.

주름진 손이 다가온다 싶더니 휙 사라졌다. 어?

탁. 탁탁.

뭔가가 지나간다 싶은 다음 순간, 나는 그대로 정지했다.

눈 뜬 송장이 이런 느낌일까? 정말 옴짝달싹도 할 수 없다.

- 단순한 점혈이니 놀라지 말고 지금부터 집중해라.

노인은 말과 함께 내 등을 손으로 짚었다. 그리고 낮은 목소리로 빠르게 말을 뱉어 냈다.

- 운기조식은 무인에게 있어 가장 중요한 수련이다. 공력을 축적하는 것만이 아니라 정精, 기氣, 신神을 갈고 닦으며 더 높은 경지로 나아갈 수 있기 때문이다. 그래서…….

귀 기울여 들었지만 뒷말은 무슨 말을 하는 건지 하나도 못 알아듣겠다. 운기조식이 굉장히 중요하다는 사실을 빼면.

- 정신을 시냇물처럼 맑게 하여 집중을 유지하고 흐름을 끌어내라. 그럼 이제 진가심법의 구결을 들려주마.

그러고는 말릴 틈도 없이 콩 볶듯이 빠른 속도로 구결을 읊는데…… 들린다. 처음 듣는 외국어가 머릿속에서 자동으로 번역되는 느낌이랄까.

‘뭐야, 이거.’

정확히 318자의 구결이다. 진가심법의 구결이 머릿속에 완벽하게 각인됐다고 느낀 순간, 변화도 일어났다.

- 내려가라.

노인의 한마디.

어디로요?

순간 들었던 의문이 사라지기도 전에, 나는 깊은 어딘가로 빨려 가고 있었다. 아니, 빨려 가는 듯했다.

분명히 눈을 감고 있는데, 보인다. 느껴진다.

슬쩍 불어오다 흩어지는 바람, 햇빛, 마부의 숨소리와 말들의 투레질…….

그 모든 것을 밀어냈다. 오직 한 곳. 내 몸만 집중했다.



- [진가심법]의 운기를 시작합니다. 빛나는 혈을 따라 이동하십시오.



어느새 노인이 사라진 것도, 시스템 음성이 울리는 것도 느끼지 못했다.

머리에서 깨어난 정신은 아래를 향해 미끄러진다. 별처럼 빛나는 점들이 혈이라는 것도 몰랐다. 그냥, 이제껏 그래 왔던 것처럼 모든 것이 익숙했다.

그리고 마침내 단전에 도달했다.

작지만 순수한 기운. 10년의 공력이다.

‘그런데 저건?’

단전 한구석, 바위처럼 단단하고 커다란 또 다른 무언가.

나는 본능적으로 깨달았다.

‘또 다른 공력이다.’

내가, 진태경이 아직 자기 것으로 녹여 내지 못한 기운이었고 기존의 공력과 비슷할 정도로 컸다.

‘저걸 흡수한다면?’

두말할 것도 없이 강해질 수 있다.

하지만 지금의 내게는 무모한 도전, 목적 없는 모험이다.

‘무리수를 두다가 여기서 객사할 수는 없지.’

나는 마음을 가다듬고 공력을 일으켰다. 시스템 음성이 알려 준 길을 따라 공력을 천천히 이끌었다.

그러던 중, 어렴풋이 누군가의 목소리를 들은 것도 같다.

- 좋은 판단이야.



* * *



- [운기조식]을 완료했습니다.

- [튜토리얼 - 4단계]를 완료했습니다. 보상이 지급됩니다!

- 스킬, [기감]을 깨달았습니다. 기의 수발이 보다 자유로워지며 상대의 기운을 파악할 수 있습니다.

- 탁기가 소량 배출되었습니다.

.

.

.

- [튜토리얼]을 모두 완료했습니다.

- [메인 퀘스트]가 생성되었습니다.



시스템의 마지막 음성과 함께 마부가 말했다.

“도착했습니다. 태원진가입니다.”

그래. 드디어.
```

### Current accepted English

```markdown
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

*Where have I seen this grateful traveler before?* The coachman stared intently at his face, then suddenly sucked in a breath.

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
```
## Chapter 6

### Korean source

```text
＃6화



언덕에서 내려다본 태원진가는 하나의 마을 같았다.

너른 대지 위, 크고 작은 수십 채의 건물이 펼쳐져 있었고 높이 쌓아 올린 돌담은 가문의 외곽을 빈틈없이 둘러쌌다.

그뿐인가, 태원진가의 뒤에 드리워진 절벽은 장관 그 자체다.

세월을 품은 자연과 그 아래 웅크린 하나의 가문.

보는 것만으로도 상당한 위압감이 느껴졌다.

“우와.”

마부도 감탄할 정도다. 아니, 잠깐만.

“여기 자주 와 보신 거 아니었어요?”

“두 번짼데요.”

“……혹시 일 시작하신 지가?”

“달포도 안 됐습니다.”

이런 양파 같은 인간을 봤나.

얼굴이나 분위기는 20년 차 베테랑인데 신입 사원이라니.

‘하긴, 그 정도 경력이면 이 얼굴을 못 알아봤을 리가 없지.’

홍화루 문지방이 닳도록 드나들던 얼굴이다. 신입 사원이라면 나를 진무경으로 착각할 법도 하다.

‘일이 잘 풀려서 다행이지.’

마지막 튜토리얼 퀘스트도 끝냈고, 태원진가도 코앞에 둔 상황이라 나는 조금 안심할 수 있었다.

“조금만 천천히 몰아 주세요.”

“아, 예.”

마차의 속도가 줄어드는 것을 느끼며 스킬창을 열었다.



스킬창



[기감]

등급 : 無

제한 : 無

경지 : 일 성

효과 : 30레벨 이하의 대상을 파악할 수 있다.

설명 : 지정 범위 내의 대상을 탐색한다. 경지가 오를수록 탐색 가능한 범위와 레벨이 상승한다.





설명을 다 읽고 나니 문득 떠오르는 게 있었다.

‘딱 그거네. 전투력 측정기.’

유명 만화에서는 기계 장치로 상대의 전투력을 수치화해서 파악하던데 [기감]은 어떨지 모르겠다.

나는 호기심을 느끼며 명령어를 떠올렸다.

‘기감 발동.’

이게 맞나? 잠깐 멈칫한 그 순간 발밑에 푸른 원이 생성됐다. 동시에 알림이 울렸다.

띠링.



- [기감]을 사용하셨습니다. 현재 1성의 경지이므로 Lv.30 이하, 10장 이내의 대상을 탐색할 수 있습니다.



10장이면 30m다.

솨아악. 쭉 뻗어 나가는 푸른 동심원에 한 사람이 걸려들었다. 마부의 둥그런 뒤통수 위로 시스템창이 불쑥 솟아오른다.



- [기감]으로 상대를 파악했습니다.



[Lv.4 장삼]



아하, 이런 식이구만.

‘쉽고, 간단하고, 무엇보다…….’

생존을 위해서 꼭 필요한 스킬이다. 적이 강한지, 약한지, 혹은 나랑 비등한지. 기감을 사용한다면 바로 파악할 수 있다.

‘괜찮은 거 하나 건졌네.’

고개를 끄덕이고 퀘스트창을 열었다. 그리고 새로 받은 [메인 퀘스트]를 확인한 순간, 나도 모르게 입이 벌어졌다.

“……어?”

눈앞이 환하게 밝아지는 기분이다. [기감]이 시궁창에 비친 한 줄기 빛이라면 이건 태양이다. 가슴이 쿵쿵 뛰고 머리가 뜨겁게 달아오른다.



퀘스트



[로그아웃]

이제 당신은 이 험난한 무림을 헤쳐 나가야 합니다.

더욱더 강해지고, 유명해지십시오.

언젠가 다가올 그 날을 위해…….



등급 : 메인 퀘스트

제한 : 진태경

임무 : [일류] 경지 달성 (미완료)

         Lv.30 달성 (미완료)

         명성 500 달성 (미완료)

보상 : [로그아웃]





간절히 바랐던 네 글자.

‘로그아웃!’

기쁘면서도 얼떨떨했다. 무슨 수를 써서라도 살아남겠다는 의지는 있었지만 일말의 불안감이 마음 한구석에 자리했던 탓이다. 내가 나갈 수 있을까? 영영 나가지 못하는 건 아닐까? 하는 그런 불길한 짐작.

‘나갈 수 있다.’

하지만 이제는 다르다. 로그아웃할 수 있다는 확신이 생겼다. 정신이 새로 깨어나는 기분이다.

‘그래, 시발. 기껏해야 게임이지.’

퀘스트? 그까짓 게 뭐 얼마나 어렵다고.

7년간 하루가 멀다고 사선을 넘나들었다. 헌터의 생존력과 의지는 일반인의 그것에 비할 바가 아니다.

‘그리고 이 힘.’

자연스럽게 주먹이 쥐어진다. 이 모든 것은 가상에 불과하지만, 몸에 넘쳐흐르는 힘만큼은 생생하게 느껴진다.

그래서 알 수 있었다.

게임에서의 내가, 현실의 나보다 강하다는 사실을.

아주 근소한 차이에 불과하지만 확실했다.

‘시스템 덕분이지.’

레벨 업, 퀘스트, 스탯 분배와 스킬. 이 모든 게 시스템의 힘이다. 게임이라서, 유저라서 가능한 일.

헌터로서의 경험과 시스템을 활용한다면 로그아웃은 시간문제에 불과하다.

‘나가면 다 뒤졌어.’

게임 개발진부터 족친다. 시발 새끼들. 부득부득 이를 가는 내 귓가로 누군가의 외침이 들려왔다.

“정지!”



* * *



통일된 복장. 절도 있는 자세와 딱딱한 목소리.

태원진가의 대문을 지키는 무사들을 본 순간 ‘무림인’이라는 단어가 뇌리를 스쳤다.

‘명문가라더니.’

확실히 다르다. 앞서 맞닥트린 천력부와 산적들이 오합지졸이라면 이쪽은 훈련받은 정규군이라고 해야 하나.

그중 한 NPC가 마부를 향해 다가왔다. 앳된 얼굴에 굵은 송충이 눈썹이 인상적인 무사였다.

“대태원진가의 수문조장 혁무진입니다. 신원과 방문 목적을 밝혀 주십시오.”

수문조장이라. 그러고 보니 혼자 완장 비슷한 띠를 두르고 있다. 딱 봐도 스물이나 됐을까 싶은 젊은 녀석인데.

‘하긴, 능력만 좋으면 장땡이지.’

내가 그런 생각을 하고 있을 때 마부가 대답했다.

“홍화루에서 왔습니다.”

“홍화루? 설마 기루를 말하는 거요?”

“예.”

창문 너머로 NPC. 아니, 혁무진의 얼굴이 찡그려지는 게 보였다. 제법 정중했던 말투도 대번에 반 토막이 났다.

“기루에서 본가에 무슨 용무가 있다고?”

“아, 그게…….”

어딜 가나 꼭 저런 놈들이 있다. 대기업에서 근무한다고 본인이 재벌인 줄 아는 놈. 정작 재벌은 따로 있는데 말이지. 나는 조용히 창문을 열고 기침했다.

“커험. 흠흠.”

다분히 의도된 헛기침이다. 성공한 인생들만 할 수 있다는 일명 ‘나 누군지 몰라?’ 헛기침.

“음.”

아니나 다를까, 혁무진은 한눈에 나를 알아봤다. 나는 잔잔한 미소와 함께 입을 열었다.

고위급 정치인, 군인, 기업인들 사이에서 폭넓게 사용되는 마법의 대사다.

“음. 그래. 수고.”

그리고 창문을 닫으려는데…….

턱. 덜컥.

“응?”

안 닫힌다. 불쑥 튀어나온 손이 창문을 붙잡고 있었다.

손의 주인은 당연하게도 혁무진이었다. 닫히다 만 창문 사이로 딱딱하게 굳은 얼굴이 보였다.

“내리시오.”

“어, 나?”

“그럼 내가 허공에 대고 얘기했겠소?”

뭐야, 이거. 이 자식 반응이 왜 이래?

‘못 알아봤군.’

나는 너그러운 미소를 지어 보였다.

“모르나 본데, 나 이 집 사는 사람이야.”

“나도 여기 사는 사람이오.”

“아니, 내 말은 그러니까…….”

“태원진가의 삼공자다. 뭐 그런 말을 하고 싶은 거요?”

“…….”

정확히 맞췄다. 혁무진이 말을 이었다.

“공자가 누군지는 충분히 알고 있으니 이제 마차에서 내리시오. 절차대로 진행하겠소.”

별수 있나. 절차라는데. 하지만 마차에서 내리는 내 머릿속에서는 경고등이 울리고 있었다.

‘어째 느낌이 쎄한데.’

태원진가의 다른 NPC들도 왠지 모르게 싸늘한 눈빛을 던졌다. 얼굴이 따가워지려고 할 때 혁무진이 종이와 붓을 꺼내 들고 말했다.

“이름.”

“…….”

“다시 묻겠소. 이름.”

이건 뭐 범죄자 취조하는 것도 아니고.

기분이 더러웠지만 일단 상황을 지켜보기로 마음먹었다.

“……진태경.”

“소속.”

“태원진가.”

“나이와 무공 경지.”

“스물. 이류.”

그 순간 혁무진의 붓이 멈칫했다.

“괜한 자존심 부리지 말고 정직하게 대답하시오.”

정직하게?

‘스탯 분배해서 이류로 올랐습니다. 하면 알아듣겠냐?’

대답 대신 혁무진의 얼굴을 빤히 바라보자 놈이 고개를 절레절레 저었다.

“뭐, 정 그렇다면 넘어갑시다. 그럼 어디 보자…… 며칠간 자리를 비우셨는데, 어딜 다녀오셨는지?”

“홍화루.”

“이야, 그 비싸다는 홍화루에서 며칠씩이나? 좋았겠소. 한 재산 썼겠구먼. 아니면 이번에도 문파 공금을 슬쩍하셨나?”

“이번에도?”

“뭘 발뺌을 하고 그러시오. 공자가 종종, 왕왕, 으레 해 왔던 일 아니오?”

혁무진의 적의 어린 눈빛을 본 순간, 어떤 사실 하나가 떠올랐다.

‘진태경.’

잠시 잊고 있었다. 이 게임에서, 특히 태원진가에서 진태경이라는 캐릭터가 어떤 존재인지.

‘가문의 수치.’

이따위 칭호까지 달고 있는 놈을, 태원진가의 NPC들이 좋아할 리 만무했다. 그걸 증명이라도 하듯 이 순간 저들의 경멸은 오롯이 나를 향하고 있다.

뭐 하나 내 뜻대로 되지 않는 이 게임 속에서.

‘아, 진짜…….’

폐부 깊숙한 곳에서 뭔가가 울컥거렸다. 머리가 아프고 눈이 뜨겁게 달아오른다. 그런 내게 나지막한 목소리가 들려왔다.

“삼공자, 내 비록 말단 조장이지만 한마디만 합시다.”

한심한 놈. 혁무진이 그런 표정으로 말했다.

“더 이상 가문의 명성에 먹칠하지 마시오. 최소한 사람답게 살란 말이오. 알겠소?”

한마디를 툭 던져 놓고 돌아서는 놈의 뒤통수를 멍하니 바라봤다. 헛웃음이 나온다.

“사람답게 살라고?”

안다. 혁무진은 아무것도 모르는 NPC에 불과하다는 것을.

내가 아니라 진태경에게 하는 말이라는 것을.

하지만…….

‘좆 같네.’

이곳이 게임 안이고 혁무진이 NPC라는 사실은 중요하지 않았다. 아니, 생각하지 않기로 했다.

그동안 쌓인 모든 스트레스가 터져 나오면서 마지막 인내심마저 허물어졌다.

“야. 거기 딱 서.”

혁무진이 돌아섰다. 짜증 난 얼굴이다. 아까부터 저 면상에 한 대 꽂아 주고 싶었지.

나는 산타클로스를 본 아이처럼 활짝 웃었다.

“넌…… 뒤졌어.”

불끈 쥔 주먹을 놈의 턱주가리를 향해 날렸다.



* * *



묵직한 공기. 탁자 위로 높게 솟은 서류 더미. 그리고 늘 그림자처럼 주인의 곁을 지키는 서늘한 인상의 호위 무사.

사각. 사각.

수문각주는 침을 삼켰다. 집무실에 들어온 순간부터 그의 입은 바싹바싹 타들어 가고 있었다.

“말해 보게.”

서류 더미 너머로 들리는 담담한 목소리는 오아시스다.

수문각주가 간신히 말문을 뗐다.

“제 수하 중에 아까운 놈이 하나 있습니다. 본가에 대한 충성심도 제법이고 무재가 뛰어난 녀석인데…….”

“듣고 있네.”

“어린놈이라 그런지 오만불손하고, 앞뒤 재는 법을 모릅니다.”

“본론만.”

“삼공자와 시비가 붙었답니다.”

“……알 만하군. 막내는?”

“신속히 약왕당으로 옮겼습니다. 지금은 혼절 상태인데 타박상이 조금…….”

순간 침묵이 흘렀다.

“모두 속하의 잘못입니다. 엄벌을 내려 주십시오!”

눈앞이 캄캄해진 수문각주는 고개를 깊게 숙였다. 재차 목소리가 들려온 것은 한참 후였다.

“그만하면 되었네. 이만 나가 보게.”

수문각주가 기사회생의 심정으로 고개를 들었을 때였다.

“아, 하나만 더.”

“하명하십시오.”

“그 친구 좀 볼 수 있겠나? 잠시 이야기를 나눠 보고 싶은데.”

“저어, 소가주님. 말씀드리기 송구스럽지만, 아직 치료가 덜 끝났습니다.”

“치료?”

“예. 그 친구도 약왕당에 있습니다. 듣기로는 뼈에 금이 갔다더군요.”

“……그런가? 그럼 되었네.”

수문각주가 물러난 후에도 이어지던 침묵은 위태롭게 쌓여 있던 서류 탑이 와르르 무너지면서 깨졌다.

“위팽.”

태원진가의 소가주이자 올해 서른다섯이 된 진위경이 굳은 얼굴로 자신의 충복을 불렀다.

“예.”

“잠시 자리 좀 비우겠네.”

또 시작이군. 진위경의 호위 무사, 위팽은 의미를 알 수 없는 한숨을 내쉬며 진위경의 뒷모습을 바라봤다.
```

### Current accepted English

```markdown
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

“What business could a pleasure house possibly have with the main family?”

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
```
## Chapter 7

### Korean source

```text
＃7화



나는 꿈을 꾸고 있다.

어떻게 꿈인 줄 알았느냐 묻는다면, 글쎄.

‘내가 나를 보고 있으니까?’

말 그대로다. 나는 나를 구경하고 있다. 정확히 말하면 현실의 내가 아닌 게임 속의 진태경을 보는 중이다.

“헉, 허억.”

진태경이 가쁜 숨을 몰아쉬었다. 옷은 찢어졌고, 얼굴과 몸 곳곳이 멍들고 부어오른 모습이다.

반면에.

‘저 새낀 멀쩡하네.’

혁무진은 쌩쌩했다. 상대를 비웃어 줄 여유까지 있었다.

“생각보다 제법이긴 한데…… 그렇게 무식하게 싸워서야 쓰나. 무인이라면 응당 무공을 써야지.”

아오, 저 얄미운 새끼. 당장이라도 달려가 놈의 뒤통수를 후려치고 싶었지만 꿈이라 그런지 몸을 움직일 수도, 소리 내어 말할 수도 없었다.

‘이렇게 보니까 더 열받네.’

맞다. 이 꿈은 앞서 혁무진과의 싸움을 제삼자의 시선으로 나에게 보여 주고 있었다.

“이런 개애새끼가아!”

진태경이 악을 쓰며 달려들었지만 소용없는 일이다. 내가 해 봐서 안다.

‘저땐 이미 지쳐 있었지.’

팔다리는 무겁고 숨은 가쁘다. 동작이 커지니 빈틈도 많다.

아니나 다를까, 간단히 주먹을 피해 낸 혁무진은 진태경의 다리를 걷어차 중심을 무너트렸다.

물 흐르듯 매끄럽고 날렵한 동작이다. 놈과의 싸움은 그런 장면의 반복이었다.

‘새끼, 잘 싸우긴 하네.’

인정해야 한다. 혁무진은 나보다 강하다. 공력을 효율적으로 운용했고 매번 알 수 없는 무공으로 나를 무력화시켰다.

한마디로 놈은 ‘무림인’이었다.

‘충격이었지.’

천력부를 해치운 직후라 자만심에 빠져 있었다. 이 정도면 어느 정도 먹힐 거란 막연한 기대감. 거기에 헌터로서 쌓은 전투 경험과 시스템의 힘이 합쳐지면 로그아웃은 시간문제라고 생각했다.

‘죽기 딱 좋은 생각이었어.’

천력부와 그 산적들은 튜토리얼 몬스터에 불과한 존재다.

초보자 사냥터의 1레벨 토끼를 잡아 놓고 희희낙락했던 거다. 7년 차 헌터? 경력이 우스울 정도로 얄팍한 생각이었다.

‘무공을 익혀야 해.’

이건 단순한 게임이 아니다. 내 목숨이 걸려 있다.

살아남기 위해서는 뭐든 해야 한다. 레벨 업, 무공. 뭐든 익히고 발버둥 칠 각오가 되어 있다.

F급 헌터가 아닌 무림인이 될 각오.

퍽. 퍽. 퍽.

“시발. 맷집만 더럽게 좋아 가지고. 놔! 안 놔!”

“크아아악!”

쓰러져도, 넘어져도 계속해서 일어나는 진태경. 아니, 내 모습이 보였다.

‘결국 마지막에 한 방 먹였지.’

빡!

그래, 저렇게 하는 거다. 지난 7년처럼. 지금까지 그래 왔던 것처럼.

‘그런데 혁무진 저놈은 레벨이 몇이야?’

그 순간, 누가 대답이라도 하듯 혁무진의 머리 위로 시스템창이 솟아올랐다.



[Lv.20 혁무진]



……닥치고 레벨부터 올려야 되나?



* * *



- 수면 모드가 종료되었습니다.



시스템 음성과 함께 눈을 떴다. 아주 잠깐, 고시원 내 방에서 깨어나는 상상을 했지만 부질없는 짓이었다.

“정신이 드십니까?”

흰옷을 걸친 남자의 말에 주위를 둘러봤다. 깨끗하게 정돈된 방 안에는 희한한 냄새가 감돌고 있었다.

여기가 어디지?

내 의문을 알아차리기라도 한 것처럼 남자가 대답했다.

“약왕당입니다. 공자께서는 혼절하신 지 반 시진 만에 깨어나셨고요.”

한의원이었군. 이 NPC는 의원이고.

‘반 시진이면…… 한 시간이나 기절해 있었다고?’

혁무진 그 자식, 야무지게도 때렸다.

“타박상 때문에 상당히 아프실 겁니다. 움직이지 마시고 잠시만 누워 계십시오.”

그 말을 끝으로 의원이 방을 나갔다. 발소리가 멀어지는 것을 확인한 나는 조용히 중얼거렸다.

“상태창 오픈.”

띠링.



상태창



[Lv.11 진태경]

직업 : 이류 무인

명성 : 10

칭호 : 명가의 자제 / 가문의 수치 (칭호 효과 적용 중)

근력 : 40체력 : 40

민첩 : 50 지력 : 10

매력 : 10 공력 : 10년

잔여 포인트 : 10

- 잔여 포인트를 분배하십시오.





천력부를 잡으면서 얻은 10포인트가 그대로 남아 있다. 혹시 모를 상황을 대비해서 포인트 분배를 미뤘었는데, 혁무진과 싸우게 될 줄은 몰랐다.

‘이렇게 얻어터질 줄도 몰랐고.’

나는 잠시 고민하다가 10포인트를 모두 체력에 투자했다.

혁무진과의 싸움에서 지쳐 헐떡거리던 내 모습이 떠올랐기 때문이었다.

‘포인트를 미리 분배해 뒀으면 승산이 있었을까?’

문득 그런 생각이 들었지만 이내 고개를 저었다.

‘결과는 달라지지 않았겠지.’

어른과 아이의 싸움. 혁무진과 나 사이에는 그 정도로 큰 격차가 있었다.

그리고 내가 생각하기에 그것은 레벨과 스탯의 문제가 아니라 무공의 유무로 벌어진 격차였다.

‘어떻게 그런 대응이, 움직임이 가능하지?’

현실에서도 무공이란 게 존재하긴 한다. 권투, 크라브마가, 주짓수 등등. 현대에 들어 실전 무술이라 불리는 것들이다.

하지만 이곳에서의 무공은 차원이 다르다.

동작 하나하나가 실전적이면서도 정교하다. 공력을 중심으로 움직이는 톱니바퀴를 연상시킨다.

‘무공을 익혀야 해.’

튜토리얼에서 마주친 게 천력부가 아니라 혁무진이었다면?

패배, 죽음이라는 단어가 자연스럽게 떠올랐다.

무공을 익혀야 한다. 익혀야 살아남을 수 있다.

“씨이발…….”

폐부 깊은 곳에서 우러나온 쌍욕을 내뱉었을 때였다.

문밖에서 인기척이 들려왔다.

“이 방입니다.”

“고맙네.”

드르륵.

뭐라 반응할 새도 없이 열린 문. 그리고 그곳에…….

“가관이로구나.”

싸늘한 눈빛을 쏟아내는 한 중년인이 있었다.



* * *



“상태는 어떤가?”

“타박상이 있지만 그리 심한 정도는 아닙니다.”

“아쉽군. 다리라도 부러졌어야 했는데.”

“…….”

중년인이 흉흉한 시선으로 나를 바라봤다.

“이 천둥벌거숭이 같은 놈!”

나는 잠자코 눈을 내리깔았다. 생전 처음 보는 사람, 아니 NPC였지만 왠지 그래야 할 것 같았다.

아니, 반드시 그래야 한다.



[Lv.???]



물음표 세 개. [기감]으로도 파악할 수 없는 고레벨이다.

‘최소 30레벨 이상.’

혁무진이 귀여워 보일 정도다. 무엇보다 의원의 태도나 나에게 하는 언행으로 보건대 결코 보통 NPC가 아니다.

최소한 태원진가 삼공자의 아구창을 시원하게 날려 버릴 정도의 권한은 있을 것 같다.

‘저걸로 한 대 맞으면…….’

꿀꺽.

솥뚜껑만 한 손바닥을 보는 순간 나도 모르게 침을 삼켰다.

레벨이고 자시고, 전체적으로 그냥 위험하게 생겼다.

2m에 가까운 거구, 온몸을 감싼 근육은 방탄조끼 같았고 차가운 눈빛은 사람을 얼어붙게 만든다.

취미도 살인, 특기도 살인일 것 같은 이 중년인의 정체가 궁금해지는 순간이었다.

‘그런데 묘하게 낯익은 얼굴이란 말이야.’

이 아저씨를 어디서 봤더라. 곰곰이 생각하다가 깨달았다.

‘진태경?’

중년인은 진태경을 닮았다. 아니, 진태경이 그를 닮았다고 해야 맞다.

까마득히 높은 레벨에 태원진가 삼공자를 깔아뭉개는 언행. 그리고 마지막으로 얼굴.

결론은 하나다. 바로 진태경의…….

“아버지?”

나도 모르게 내뱉은 그 말에 중년인이 눈을 부릅떴다.

“아, 아버지이?”

주먹까지 파르르 떨린다. 누가 보면 내가 엄마 욕이라도 한 줄 알겠다. 나는 그의 주먹을 주의 깊게 바라보며 말했다.

“저, 저기. 잠깐만 진정하시고…….”

“진정? 네놈 입에서 그딴 소리가 나와? 이 상황에서도 장난질을 쳐!”

“아니라면 정말 죄송합니다. 제가 실례했어요.”

“입 다물어.”

서늘한 눈빛으로 내 입을 틀어막더니 아직도 대기 중인 의원에게 고개를 돌렸다.

“안내해 줘서 고맙네. 이만 나가 보게.”

나는 간절한 눈빛으로 구조 신호를 보냈지만, 의원은 잽싸게 돌아섰다.

‘아니, 시바…… 의사가 환자를 외면해?’

쾅. 문이 닫히는 소리가 지옥문 입장 소리처럼 들린다.

단둘이 남게 된 방 안. 그가 솥뚜껑만 한 손바닥을 치켜들고 다가오기 시작했다.

“망나니 짓거리도 정도가 있지, 언제까지 이렇게 살 테냐!”

어느새 나는 벌떡 일어나 슬금슬금 뒷걸음질을 치는 중이었다.

타박상? 고통? 그런 건 이미 느껴지지 않았다. 어쩌면 더 이상 고통을 느낄 수 없는 몸이 될지도 모른다.

“저, 저한테 딱 십 분만. 아니, 일 다경만 주시면 제가 잘 설명해 드릴 수 있거든요. 뭐 때문에 화가 나신 건데요. 네? 아버지라고 부른 것 때문에 그러세요? 혹시 어머니세요?”

“이노옴!”

쩌렁쩌렁한 음성에 순간 몸이 굳는다. 등이 벽에 닿는 것이 느껴졌다.



- 당신은 [혼란]에 빠졌습니다. 3초간 몸을 움직일 수 없습니다!



이런 개 같은 경우를 봤나…….

‘끝났구나.’

27년 인생이 주마등처럼 스쳐 지나간다. 거짓말 조금 보태서 정자 시절 치열했던 착상 레이스까지 떠오른다. 그때 참 힘들었지.

‘엄마, 아빠, 하연아…….’

가족들을 생각하며 스르륵 눈을 감은 그 순간이었다.

“틈만 나면 계집질이나 하고!”

쓰담쓰담.

“도박장이나 들락거리고!”

만지작만지작.

“네놈이 이따위로 행동하니 가문에서 멸시받는 것이다!”

문질문질.

……이 아저씨 지금 뭐 하는 거야?

입으로는 분노와 질책 어린 말들을 쏟아 내면서, 손은 부드럽게 내 몸 곳곳을 어루만진다. 등골이 오싹했다.

‘설마 이거.’

띠링.



- 당신은 [공포]에 휩싸였습니다. 5초간 몸을 움직일 수 없습니다!



“너는 가문의 수치다, 수치!”

극도의 수치심을 느끼고 있긴 하다. 인공지능에게, 그것도 중년 남성의 모습을 한 NPC에게 성추행을 당하다니.

‘엄마…….’

모든 게 내 오해라는 걸 깨달은 것은 잠시 후였다.

손은 바쁘게 움직인다. 그런데 그게 꼭 환자를 살피는 의사의 그것 같다.

눈꺼풀도 뒤집고, 맥도 한 번 짚어 보고, 타박상 부위도 세심하게 살핀다. 그의 손이 스쳐 갈 때마다 안마를 받는 것처럼 시원해지고 고통이 사라졌다.

“너 이 녀석! 계속 이따위로 행동하면, 어? 어! 아주 경을 칠 것이다. 알겠느냐?”

“…….”

마침내 손을 멈춘 그가 작은 목소리로 속삭였다.

“생각보다 경미해서 다행이다. 그러게 왜 싸웠느냐. 평소에 무공 수련도 안 하던 녀석이.”

나는 진심을 담아 입을 열었다. 여러 가지가 함축된 한마디였다.

“누구세요?”

다음 순간, 엄격. 근엄. 진지. 세 가지가 모두 담겨 있던 얼굴이 돌연 상처받은 아기 사슴으로 변했다.

“갑자기 왜 존댓말을 쓰고 그러느냐. 아까 가문의 수치라고 한 건 그냥 사람들 들으라고 한 소린데…… 혹시 섭섭했던 거냐?”

“예?”

“형은 슬프구나. 너 어릴 때 내가 매일 똥 기저귀도 갈고, 울면 업어 주고, 달래서 재우고. 얼마나 애지중지 키웠는지 알면서.”

“예? 형이요?”

순간 침묵이 찾아왔다.

‘아버지가 아니라 형이었어?’

나는 이 나이 든 아저씨가 형이라는 사실에 놀랐고.

“아이고, 우리 막내가 머리를 다쳤나 보네. 이보게. 의원! 의원!”

중년인은 의원을 부르짖으며 뛰쳐나갔다. 그 뒷모습을 보면서 문득 퍼즐 하나가 맞춰졌다는 생각이 들었다.

‘진태경이 개판으로 자란 이유를 알겠네.’

잘못된 가정교육의 훌륭한 사례다.
```

### Current accepted English

```markdown
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

“Fuck. You’ve got one hell of a chin. Let go! I said let go!”

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
```
## Chapter 8

### Korean source

```text
＃8화



“이상 없습니다.”

의원이 내린 결론이었다. 확신에 찬 말투에 나는 내심 고개를 끄덕였다. 그 말이 사실이니까.

‘뇌에는 이상 없지.’

단지 내가 이 몸에 들어와 있을 뿐이다.

하지만 누군가는 진찰 결과가 마음에 들지 않는 모양이었다.

“그럼 왜 기억을 못 하는 건가?”

위엄 있는 분위기와 목소리. 이제는 그의 이름을 안다.

‘진위경.’

진태경의 큰형이자 태원진가의 소가주인 진위경이다. 맞다. 정말 아버지가 아니었다.

‘저 양반, 아까는 눈물까지 글썽이더니.’

지금은 시침 뚝 떼고 엄격 근엄 진지의 가면을 뒤집어썼다.

죄 없는 의원만 쩔쩔매며 대답했다.

“그것이, 분명 제 판단은 그렇습니다만 가끔 예외가 있을 수도…….”

“됐네. 이만 나가 보게.”

의원이 상처받은 얼굴로 떠나자 진위경이 기다렸다는 듯이 내게 바짝 붙었다. 목소리에는 애정과 걱정이 넘쳐흘렀다.

“정말 기억이 나지 않느냐?”

“예.”

“하나도?”

조용히 고개를 끄덕였다. 이미 머릿속에서는 어떻게 행동해야 할지 계산이 끝난 상태였다.

‘이대로 쭉 가자.’

드라마에서나 보던 기억상실증 환자. 지금 상황에서는 이보다 편할 수가 없다. 굳이 게임 속 상황에 맞추려고 노력할 필요도 없고, 정보를 얻지 않아도 된다.

가만히 누워서 아무것도 몰라요, 하는 얼굴로 눈만 깜빡이면 알아서 상황이 흘러가는 것이다. 마치 지금처럼.

“방금 했던 말은 기억나느냐?”

“어떤 거요?”

내가 기억을 잃었다고 생각한 진위경은 기본적인 사실 몇 가지를 알려 주었는데 진위경의 정체도 그때 알았다.

“내 이름을 말해 보아라.”

“진위경. 태원진가의 소가주.”

“나이는?”

“서른다섯.”

세상에, 저 얼굴로 삼십 대라니. 심지어 아직 결혼도 안 한 총각이란다.

“부모님은?”

“아버지는 중원 유람 중. 어머니는 십 년 전 사망.”

“옳지. 둘째 형은?”

“진천검 진무경. 스물다섯. 현재 천무학관 생도.”

천무학관이 어디 붙어 있는 곳인지는 모른다. 그냥 앵무새처럼 들은 그대로 읊어 댈 뿐이다. 내 대답에 기계처럼 옳지, 옳지를 반복하던 진위경이 고개를 갸웃거렸다.

“진천검? 내가 별호도 말해 줬던가?”

아니. 그건 마부가 알려 줬는데.

진위경과 눈이 마주친 순간, 나는 냅다 이마를 짚었다.

“아, 머리가! 머리가 아픕니다!”

“아이고오, 막내야!”

이 정도면 치트키 수준이다.



* * *



“단순한 타박상이니, 길어도 사흘이면 붓기와 멍이 전부 사라질 겁니다.”

의원의 마지막 말을 뒤로하고 약왕당을 나왔다. 입구에는 수더분한 인상의 하인이 나를 기다리고 있었다.

“공자님의 처소로 안내해 드리겠습니다.”

앞서 걷는 하인은 거침없이 발걸음을 옮겼다. 이미 내가 기억을 잃었다는 사실을 알고 있는 듯, 간혹 어떤 건물이나 사람을 보면 조용한 목소리로 설명하고는 했다.

‘길잡이, 심부름꾼, 백과사전.’

진위경이 하인을 보낸 의도가 대충 짐작이 간다.

본인이 업무로 바쁘니 이렇게라도 신경 써 주는 거겠지.

“도착했습니다.”

마침내 발걸음이 멈춘 곳은 2층으로 이루어진 목제 건물이었다.

보통 이런 건물을 중국에서는 전각이라고 하던가? 제법 고풍스러운 멋이 있었다.

“우와.”

그리고 무지하게 넓다. 하인이 문을 연 순간 나도 모르게 입이 딱 벌어질 정도였다.

“이 층이 침실입니다. 내부 곳곳에 종을 설치해 두었으니 필요한 일이 생기시면 종을 울려 주십시오.”

하인이 떠난 뒤, 나는 정신을 차리고 전각 내부를 돌아보기 시작했다. 1층만 해도 얼추 100평도 넘어 보인다.

2평 남짓한 고시원 원룸에 살던 내게는 올림픽 경기장이나 다름없다.

‘NPC가 부럽긴 처음이네.’

1층에만 방이 여섯 개다. 문득 호기심이 치솟았다.

‘저 안에 뭐가 있을까.’

보물? 무공 비급? 아니면 기똥찬 아이템들?

뭐라도 상관없다. 가장 가까운 방문을 열어젖혔다.

“이야.”

문을 여는 순간 탄성이 튀어나왔다. 형광등이 달린 것도 아닌데 사방이 환하다. 벽을 따라 세워진 선반, 그 안을 가득 채운 비단옷들 때문이다. 언뜻 봐도 엄청난 양이다.

물론 내가 찾던 물건은 아니었다.

‘이 자식은 옷도 많네.’

클럽, 아니 기루 죽돌이답다. 나는 혀를 차고 문을 닫았다. 그리고 곧장 두 번째 방으로 직행. 다시 문을 열어젖혔다.

“또 옷이야?”

진태경을 과소평가했다. 이 정도면 이 시대의 패션 피플쯤 되지 않을까. 스멀스멀 기어오르는 불안감을 애써 무시하며 세 번째 방으로 이동했다.

벌컥.

“……이런 쇼핑 중독자 새끼.”

와, 뭐 이런 놈이 다 있지? 방 세 개가 옷으로 꽉꽉 채워진 걸 보니 고구마를 먹은 것처럼 목이 꽉 막힌다.

‘이거 어쩌면…….’

불안감이 점점 실체화되어 몸을 짓누른다. 나는 무거운 발걸음으로 마지막 방 앞에 섰다. 앞서 들른 방들과는 달리 잘 쓰지 않아 녹슨 문고리를 잡고 천천히 밀었다.

끼이익.

거슬리는 소리와 함께 마지막 방이 속살을 드러냈다.

자그맣게 뚫린 창 사이로 스며드는 햇빛. 걸음마다 피어오르는 먼지. 그리고 그 너머로 보이는, 여러 개의 책장.

“찾았다.”

나도 모르게 웃음이 나왔다.



* * *



책장은 총 다섯 개. 그중 가장 가까운 책장에 다가가 한 권을 뽑아 들었다. 두껍게 쌓인 먼지를 털어 내자 겉표지에 적힌 글씨가 드러난다.

시스템은 이래서 편하다. 언어가 동기화된 덕분에 외계어 같은 글씨도 모국어처럼 읽고 발음할 수 있으니까.

“삼전보?”

띠링.



아이템창



[삼전보]

종류 : 비급

등급 : 삼류

제한 : 없음

설명 : 가장 기본적인 실전 보법. 시중에서도 구할 수 있다.

- 해당 무공을 수련하시겠습니까? (3 / 10)





됐다!

나는 두근거리는 마음으로 시스템창을 읽어 내려갔다.

삼전보. 가장 기본적인 삼류 보법. 맞다. 소설 속에서나 보던 바로 그 무공 비급이다.

내가 세운 첫 번째 계획은 바로 무공을 익히는 것이었다.

‘역시 무공 수련에도 시스템이 적용되는 거였어.’

앞서 태원진가에 오기 전, 운기조식 퀘스트를 끝낸 직후 느꼈던 짐작이 확신으로 바뀌는 순간이다.

‘다행이다.’

설마 소설 속 주인공이나 NPC들처럼 하나부터 열까지 차근차근 익혀 나가야 하는 건 아닌지 걱정했는데 다행히 기우에 그쳤다.

‘망겜도 게임은 게임이지.’

일반 무공에도 운기조식 때처럼 시스템이 적용된다면 고속 성장은 식은 죽 먹기다. 나는 수락을 외치……려다가 말았다.



- 해당 무공을 수련하시겠습니까? (3 / 10)



괄호 사이의 숫자가 심히 거슬린다. 마침 내가 익힌 무공도 딱 세 개다. 진가심법과 진가창법, 그리고 진가보법.

이거 설마.

‘익힐 수 있는 무공에 제한이 있나?’

만약 이 짐작이 사실이라면 지금 [삼전보] 같은 삼류 무공을 익힐 때가 아니다. 로그아웃 전까지 내 목숨을 지키고, 레벨과 명성치를 빠르게 올릴 수 있을 만한 상급 무공을 찾아야 한다.

그나마 다행인 건 이 방에는 어림잡아 몇백 권의 무공 비급이 존재한다는 사실이다.

“좋아. 좋아.”

앞으로 익힐 수 있는 무공은 일곱 개. 알짜배기 무공으로 꽉꽉 채워 넣는다면 로그아웃은 시간문제다.

나는 흐뭇한 미소를 지으며 다음 책을 뽑아 들었다.

띠링.



아이템창



[야왕 대물남]

종류 : 야설

등급 : 無

제한 : 없음

설명 : 삽화를 곁들여 읽으면 더욱 좋다.





“…….”



* * *



오늘도 업무와의 전쟁은 치열했다. 아침부터 자정이 되어 가는 지금까지 집무실을 벗어나지 못했으니까. 벌써 두 달째 이어지는 강행군이었다.

“고생하셨습니다.”

금일 업무의 종료를 알리는 위팽의 한마디였다.

진위경은 뻣뻣해진 몸을 일으켜 집무실을 나섰다. 이곳의 주인은 어느 날 홀연히 사라진 그의 아버지이지, 진위경 자신이 아니기 때문이다.

그가 기거하는 곳은 태원진가의 중심부에 위치한 내원(內院)의 전각이었고, 일 다경 정도를 걸어야 했다.

“날이 춥습니다.”

그림자처럼 따라붙은 위팽이 두툼한 모피를 어깨에 둘러 주자 진위경은 피곤한 얼굴로 웃었다.

“고맙네. 자네마저 없었으면 진작 몸져누웠을지도 몰라.”

“어쩌겠습니까. 저라도 안주인 역할을 해야지요.”

“관두세. 안 그래도 노인네들이 성화야.”

진위경은 뻑뻑한 눈가를 문질렀다. 서른 중반의 나이지만 그는 아직 미혼이다. 젊음을 핑계로 차일피일 미루던 것이 쌓이고 쌓여 십여 년 세월이 됐다.

‘하긴 해야겠지. 가문을 위해서라면.’

사랑해 본 경험이 없느냐고 묻는다면, 아니다.

하지만 진위경은 철부지 어린애가 아니었다. 언젠가는 가솔들을 책임질 가주가 될 터였고, 정략혼으로 가문을 일으킬 수 있다면 그로서는 값싼 희생이었다.

“별이 밝군요. 횃불이 없어도 될 뻔했습니다.”

분위기를 알아챈 위팽이 말을 돌렸다. 진위경은 고개를 절레절레 흔들었다. 어느새 처소가 보이고 있었다.

“음?”

“왜 그러십니까?”

진위경의 시선을 따라간 위팽은 고개를 갸우뚱했다. 멀지 않은 전각에서 희미한 불빛이 새어 나오고 있었다.

“삼공자의 처소 아닙니까?”

“맞네. 밤이 깊었는데 불이 켜져 있군.”

진위경은 말과 함께 성큼성큼 앞서 나갔다. 위팽도 어쩔 수 없이 그 뒤를 따랐다.

“주군, 그냥 다음에 보시죠. 기억을 잃은 건 핑계고 술이나 마시고 있을 게 뻔합니다.”

“쉿.”

두 사람은 전각에 들어섰다. 불빛이 새어 나오는 곳은 가장 왼쪽의 낡은 방이었다. 누가 움직이는지 쉴 새 없이 삐걱거리는 소리도 났다.

- 제가 삼공자를 과소평가했군요. 여자까지 부른 모양입니다. 소리 들어 보세요. 제 이번 달 봉급을 걸겠습니다.

위팽이 입을 달싹였다. 공력으로 소리를 전달하는 전음(傳音)이었다.

- 위팽.

- 예?

- 입 좀 닥치게.

전음으로 굵고 짧은 한마디를 던진 진위경이 문으로 바짝 다가섰다. 열린 문틈 사이로 방 안의 광경이 보였다.

이어 위팽이 상처받은 얼굴로 끼어들었다.

- 그렇게 안 봤는데 주군 취미가 상당히 독특…… 허억.

다음 순간, 위팽의 입이 딱 벌어졌다. 내가 방금 뭘 본거지?

요즘 몸이 허해서 헛것이 보이나? 소매로 눈을 비볐지만 그의 오감은 눈앞의 광경을 그대로 받아들였다.

“이제 대각선으로 두 걸음 내딛으면서…….”

건장한 체구의 청년이다. 연신 중얼거리며 쉴 새 없이 몸을 움직인다. 먼지에 덮인 바닥 위에는 수많은 발자국이 찍혀 있고 지금도 생겨나는 중이다.

스륵. 삐끗.

“시발, 무공 좆같이 만들었네에에엑!”

삼공자다. 저 지랄 맞은 성격과 말투. 분명히 삼공자 진태경이 맞다.

열두 살 이후로 무공을 수련하지 않았던 그가, 자정이 넘은 시각까지 먼지와 땀에 범벅이 될 정도로 수련을 하고 있다!

- 위팽.

넋 놓고 바라보던 위팽이 퍼뜩 정신을 차렸다.

- 예, 예?

진위경은 몽롱한 눈동자로 방 안을 바라봤다. 넘어진 채 천장을 향해 쌍욕을 퍼붓던 진태경이 다시 일어나 보법을 밟고 있었다.

- 약속대로 이번 달 봉급은 없네.
```

### Current accepted English

```markdown
# Chapter 8

“There are no abnormalities.”

That was the physician’s conclusion. I nodded inwardly at his confident tone. He was telling the truth.

*There’s nothing wrong with my brain.*

I was simply inhabiting this body.

But someone didn’t seem satisfied with the diagnosis.

“Then why can’t he remember?”

The dignified atmosphere. The commanding voice. I knew his name now.

*Jin Wikyung.*

Jin Taekyung’s older brother and the Lesser Family Head of the Jin Family of Taiyuan, Jin Wikyung. Right. He really wasn’t my father.

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

Weren’t buildings like this usually called halls in China? It had a rather impressive old-fashioned charm.

“Wow.”

It was unbelievably spacious, too. The moment the servant opened the door, my jaw dropped.

“The second floor contains your bedroom. Bells have been installed throughout the building, so please ring one if you need anything.”

After the servant left, I came to my senses and began exploring the hall. The first floor alone looked to be more than three hundred square meters.

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
> **The Night King: Big-Dick Man**
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

His residence was a hall in the inner compound at the center of the Jin Family estate, and it took about a quarter hour to walk there.

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

Following Jin Wikyung’s gaze, Wipeng tilted his head. A faint light was leaking from a nearby hall.

“Isn’t that the Third Young Master’s residence?”

“It is. It’s late, but the lights are still on.”

As he spoke, Jin Wikyung strode forward. Wipeng had no choice but to follow.

“My lord, why don’t we come back another time? The memory loss is just an excuse. He’s obviously drinking.”

“Shh.”

The two men entered the hall. The light was coming from the old room on the far left. The constant creaking made it clear that someone was moving around inside.

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
```
