# Fidelity Gate — Chapter 13

Audit the complete assembled English chapter against the Korean source.
Report only genuine source-fidelity defects: wrong action, subject, object,
causality, quantity, mechanism, terminology, ambiguity, joke logic, register,
or physical detail. Check repeated UI labels and counters against how they
behave across the whole scene. Interpret idioms by their function, not by
translating their component words. Do not report optional stylistic rewrites.

Return exactly one JSON object and no Markdown fence:

{
  "summary": "brief assessment",
  "findings": [
    {
      "id": "F01",
      "severity": "critical|major|minor",
      "source": "source location",
      "current": "exact uniquely occurring English span",
      "defect": "specific fidelity defect",
      "replacement": "finished replacement only when necessary",
      "rationale": "source-grounded reason",
      "confidence": 0.0
    }
  ]
}

Use an empty findings array when the chapter is faithful. A critical or major
finding blocks promotion; minor findings are recorded for human inspection.

## Korean source

```text
  1|＃13화
  2|
  3|
  4|
  5|다섯 마리의 말은 힘차게 달렸다. 산과 들, 강을 지나 마침내 목적지에 도착했을 때는 정오 무렵이었다.
  6|
  7|“어디에서 오셨습니까?”
  8|
  9|태원진가 수문위사의 긴장 섞인 물음에 선두의 청년이 웃었다. 비뚜름하게 올라간 입술에는 감출 수 없는 적의가 배어 있었다.
 10|
 11|“항산(恒山).”
 12|
 13|진위경이 가문 중진들을 소집한 것은 일 다경 후였다.
 14|
 15|
 16|
 17|* * *
 18|
 19|
 20|
 21|혁무진은 변화무쌍했다. 나는 그저 머릿속에 녀석의 모습을 그려 넣으면 되었다. 창, 검, 도, 활……. 이길 때도, 질 때도 있었지만 한 가지는 확실했다.
 22|
 23|“이제 감 잡았다.”
 24|
 25|무공이 몸에 익었다. 처음에는 처음부터 끝까지 차례차례 풀어내는 것에 집중했지만 이제는 다르다.
 26|
 27|상황에 따라 초식도 변한다. 꼭 초식 하나하나가 순서대로 이어져야만 무공인 건 아니다. 지금의 나는 초식의 순서를 뛰어넘어 무공을 연계할 수 있을 정도의 수준이 됐다.
 28|
 29|‘지금처럼 말이지.’
 30|
 31|쐐애애액!
 32|
 33|바람 소리가 들렸을 때는 이미 늦었다. 복부를 꿰뚫린 혁무진이 탄식했다.
 34|
 35|- 실력이 빨리도 느는군.
 36|
 37|“창질만 7년을 했다. 이 새끼야.”
 38|
 39|눈을 감았다 뜨니 텅 빈 수련동이 보인다. 내 승리를 축하하듯 시스템 알림이 울렸다.
 40|
 41|띠링.
 42|
 43|
 44|
 45|- [진가창법]이 사 성으로 올랐습니다!
 46|
 47|- [진가보법]이 사 성으로 올랐습니다!
 48|
 49|- 초식이 정교해지고 파괴력이 상승합니다.
 50|
 51|- 레벨 업!
 52|
 53|
 54|
 55|“이제 14레벨인가?”
 56|
 57|사흘 만에 3레벨을 올렸다.
 58|
 59|수련동에서 사흘을 짱박혀 있던 것치고는 가파른 상승세다.
 60|
 61|거기에 진가심법은 삼 성, 보법과 창법은 사 성에 도달했다.
 62|
 63|“상태창 오픈.”
 64|
 65|잔여 포인트를 분배하고 나자 어쩐지 코끝이 찡하다.
 66|
 67|
 68|
 69|상태창
 70|
 71|
 72|
 73|[Lv.14 진태경]
 74|
 75|직업 : 이류 무인
 76|
 77|명성 : 10
 78|
 79|칭호 : 3개 (칭호 효과 적용 중)
 80|
 81|- 명가의 자제 (모든 능력치 +5, 명성 +50)
 82|
 83|- 가문의 수치 (모든 능력치 –5, 명성 –50)
 84|
 85|- 초보 수련자 (수련 속도 +10%)
 86|
 87|근력 : 51체력 : 61
 88|
 89|민첩 : 61 지력 : 10
 90|
 91|매력 : 10 공력 : 10년
 92|
 93|잔여 포인트 : 0
 94|
 95|
 96|
 97|
 98|
 99|“아름답다. 아름다워.”
100|
101|이 균형 잡힌 능력치를 보라.
102|
103|이게 바로 전투의, 전투에 의한, 전투를 위한 능력치다.
104|
105|‘거기에 무공까지.’
106|
107|그때의 내가 아니다. 혁무진? 붙어도 이길 자신 있다.
108|
109|무공의 무자도 모르는 F급 헌터는 죽었다. 지금의 나는 절정 심법에 일류 무공을 두 개나 익힌 무림인이다.
110|
111|‘오늘부터 시작이야.’
112|
113|모든 준비는 끝났다. 오늘, 수련동에서 나가게 되면 생각해 둔 물건들을 챙겨 태원진가를 빠져나갈 것이다.
114|
115|‘진위경의 도움을 받을 수도 있겠지.’
116|
117|천력부 같은 얼뜨기 산적들만 처리해도 빠른 속도로 목표치에 도달할 수 있을 것이다. 길어 봤자 이틀. 그 후에는 따뜻한 가족의 품으로 돌아갈 수 있다.
118|
119|‘엄마, 하연아. 보고 싶다.’
120|
121|눈시울이 붉어지려던 그때였다.
122|
123|그그긍-
124|
125|“오, 오오오!”
126|
127|기다리던 순간이다. 수련동 입구를 막은 철문이 열리고 있었다. 그 거무튀튀하고 무거운 쇳덩어리가, 천국의 문처럼 아름답게 보였다.
128|
129|“드디어! 나간다!”
130|
131|나는 환희에 찬 얼굴로 천국 입구를 향해 달려 나갔다.
132|
133|날 이곳에서 꺼내 줄 천사가 문 뒤에서 모습을 드러냈다.
134|
135|“삼공자. 사흘 만이군요.”
136|
137|반가운 얼굴은 아니지만 지금은 마냥 기쁘다.
138|
139|“저 꺼내 주시려고 오신 거죠? 예? 맞죠?”
140|
141|사막여우를 닮은 천사, 위팽이 미묘한 말투로 대답했다.
142|
143|“예. 일단은요.”
144|
145|“……?”
146|
147|“나가긴 할 겁니다. 하지만 바로 들러야 할 곳이 있습니다.”
148|
149|“들러야 할 곳?”
150|
151|순간 등줄기가 오싹하다. 왠지 모를 생존 본능이 고개를 쳐들었다.
152|
153|“어딜 가는데요?”
154|
155|“대회의장입니다. 소가주님께서도 그곳에서 기다리고 계십니다. 그리고…….”
156|
157|위팽이 덧붙였다.
158|
159|“본가의 중진들과 항산검문의 사자(使者)도 와 있지요.”
160|
161|“항산검문이요? 걔네가 여길 왜 와요?”
162|
163|홍화루에서 월화가 그랬었다. 태원진가와 항산검문은 숙적관계라고. 그런데 그놈들이 왜 여기 있어?
164|
165|‘일이 잘못 돌아가고 있다.’
166|
167|불길하다. 불길해. 어떻게든 방법을 찾아야 한다.
168|
169|“저 그럼 잠깐 처소에서 옷만 갈아입고 가면 안 될까요?”
170|
171|“안 됩니다.”
172|
173|“중요한 자리인 것 같은데 냄새나면 안 되니까…….”
174|
175|“도망칠 생각이십니까?”
176|
177|생긴 건 사막여운데 눈치는 미어캣 저리 가라다. 내가 뭐라 할 새도 없이 위팽의 손이 어깨를 짓눌렀다.
178|
179|“삼공자. 지금부터 제가 묻는 말에 사실대로 대답해 주십시오. 아시겠습니까?”
180|
181|목소리는 건조하고 눈동자는 서늘하다. 그에게서 느껴지는 기세에 입을 뗄 수 없었다. 내가 할 수 있는 것이라곤 고개를 끄덕이는 것뿐이었다.
182|
183|‘진태경.’
184|
185|순간 머릿속에 떠오른 세 글자.
186|
187|확실했다. 분명히 이 새끼다. 나도 모르는 똥을 싸질러 놓은 거다.
188|
189|그리고…….
190|
191|“항산검문의 여식을 범하려 한 것이 사실입니까?”
192|
193|그 똥은 상상 이상으로 거대했다.
194|
195|
196|
197|* * *
198|
199|
200|
201|위팽을 따라 대회의장으로 향하는 길, 머릿속이 온통 백지장이었다.
202|
203|‘성폭행 미수?’
204|
205|미수에 그쳤다고는 하나, 때려죽여도 시원찮을 성범죄다.
206|
207|한 사람의 인간으로서, 여동생을 둔 오빠로서 성범죄자는 사형시켜야 한다고 입버릇처럼 말하던 기억이 떠올랐다.
208|
209|‘이런 미친 새끼.’
210|
211|손바닥이 식은땀으로 축축하다. 나는 몇 번째인지 모를 말을 내뱉었다.
212|
213|“저 진짜 아닙니다. 믿어 주세요.”
214|
215|위팽은 뒤도 돌아보지 않고 대답했다.
216|
217|“기억이 돌아오셨습니까?”
218|
219|“아니, 그게 아니고요. 저 진짜 아니라니까요. 제가 그럴 놈으로 보이세요? 그런 쓰레기 짓을 하고 다닐 정도로?”
220|
221|“예.”
222|
223|아니, 시발.
224|
225|숨도 안 쉬고 대답하네.
226|
227|“저기요. 그럼 저 화장실, 아니 변소 좀 들렀다 갈게요.”
228|
229|“안 됩니다.”
230|
231|“아니, 볼일은 보게 해 줘야지!”
232|
233|“그냥 싸십시오.”
234|
235|이런 개새끼. 나는 포기하고 곧장 뒤돌아 뛰기 시작했다. 모든 공력을 끌어올려 발에 집중시켰고.
236|
237|덥석.
238|
239|“삼공자.”
240|
241|세 걸음 만에 붙잡혔다. 내 목덜미를 움켜쥔 위팽이 서늘한 눈동자로 나를 내려다봤다.
242|
243|“계속 이러시면…… 제가 무례해질지도 모릅니다.”
244|
245|저항은 무의미하다. 위팽은 [기감]으로도 레벨을 파악할 수 없는 고수다.
246|
247|‘어쩔 수 없다.’
248|
249|참담한 마음으로 얼마나 걸었을까, 우뚝 선 전각이 눈에 들어왔다.
250|
251|앞에는 무사 여럿이 경계를 서는 중이었는데, 태원진가 특유의 남색 복장은 눈에 익었지만 몇 명은 처음 보는 붉은 색 옷을 걸치고 있었다.
252|
253|‘저놈들이 항산검문이구나.’
254|
255|양 문파의 평소 관계를 생각해 보면 견원지간일 텐데, 지금은 한마음 한뜻으로 나를 노려보는 중이다.
256|
257|“시발…….”
258|
259|내 중얼거림을 들은 위팽이 고개를 돌렸다.
260|
261|“소가주께서는 삼공자를 믿고 계십니다. 그 사실을 잊지 마십시오.”
262|
263|그래. 진위경이 있다. 내 가장 큰 희망이자 방패.
264|
265|그 사실을 되새길 때, 위팽이 대회의장의 문을 열어젖혔다.
266|
267|“삼공자를 데려왔습니다.”
268|
269|크게 심호흡한 나는 전각으로 발을 디뎠다. 속으로는 끊임없이 되뇌는 중이었다.
270|
271|‘호랑이한테 물려 가도 정신만 차리면 산다. 호랑이한테 물려 가도 정신만 차리면…….’
272|
273|내가 회의장 안으로 들어서자 낮게 웅성거리던 목소리가 뚝, 끊겼다. 젊고 늙은 남자 십여 명이 좌우로 도열해 있고 상석에는 진위경이 자리했다.
274|
275|그리고 중앙의 한 청년.
276|
277|“오랜만이오. 진 공자.”
278|
279|그 꺼림칙한 미소와 마주한 순간이었다.
280|
281|띠링.
282|
283|
284|
285|- [살기]를 감지했습니다!
286|
287|
288|
289|……깜빡이 좀 켜고 들어와라.
290|
291|
292|
293|* * *
294|
295|
296|
297|살기.
298|
299|익숙하다. 몬스터들은 말 그대로 악의와 살기로 똘똘 뭉친 녀석들이니까. 수도 없이 느껴 왔고, 이제는 익숙하다고 생각했다. 그런데 이놈은…….
300|
301|‘달라.’
302|
303|내가 겪어 온 그것과는 차원이 다르다.
304|
305|굳이 비교하자면 하급 몬스터와 중급 몬스터의 차이라고 하겠다. 훨씬 다듬어져 있고, 은밀하며 소름 끼친다.
306|
307|“지난번 저잣거리에서 스치듯이 본 적이 있었는데. 기억할지 모르겠소.”
308|
309|한 마디, 한 마디. 씹어뱉는 이소군의 머리 위로 시스템창이 둥둥 떠다닌다.
310|
311|
312|
313|[Lv.30 이소군]
314|
315|
316|
317|앞서 살기를 감지하자마자 [기감]으로 읽어 낸 녀석의 레벨이었다. 내 레벨의 두 배가 넘어간다.
318|
319|‘미치겠네.’
320|
321|더 서글픈 것은 다른 사람들의 눈초리다.
322|
323|젊은 사람, 늙은 사람 가릴 것 없이 흉험한 눈빛 수십 개가 나를 노려보는 광경에 오금이 저려 온다. 그런 분위기 속에서 이소군이 입을 열었다.
324|
325|“아쉽구려. 조금만 일찍 왔다면 더 깊은 대화를 나눠 볼 수 있었을 터인데. 방금까지 흥미로운 이야기를 하고 있던 참이어서 말이오.”
326|
327|“……그래요?”
328|
329|“무슨 이야기인지 궁금하지 않소?”
330|
331|“괘, 괜찮습니다.”
332|
333|목을 자를까, 불알을 자를까에 관한 토론이 아니길 바랄 뿐이다. 그리고 만약 이 불행한 짐작이 사실이라면, 목 대신 불알이 잘렸으면 했다.
334|
335|‘잘만 하면 레벨 업으로 회복할 수 있…… 내가 이런 것까지 생각해야 하나.’
336|
337|참담할 뿐이다. 그런 내 표정을 지그시 바라보던 이소군이 말했다.
338|
339|“며칠 전 가문에 돌아왔다 들었소만. 어디 있었소?”
340|
341|“홍화루요.”
342|
343|“그럼 홍화루에 가기 전에는 어디 있었소?”
344|
345|‘고시원에 있었다. 임마.’
346|
347|나도 솔직하게 다 털어놓고 싶다. 그날 저는 길드에서 잘리고, 고시원 형이랑 소주 한잔 걸친 다음에 캡슐에 들어가서 잤습니다. 눈 떠 보니까 홍화루였고, 로그아웃을 목표로 열심히 하고 있습니다. 뭐, 이렇게.
348|
349|‘칼이나 안 뽑으면 다행이지.’
350|
351|대답을 못 하고 머뭇거릴 때 이소군이 품에서 뭔가를 꺼내 들었다. 정말 칼이라도 뽑나 싶었는데, 웬 종이 뭉치다.
352|
353|“기억을 못 하는 것 같으니 내 알려 주겠소. 홍화루에 가기 전날 밤, 공자는 명월루에 들렀소. 예약해 두었던 특급 객실로 향했지.”
354|
355|“명월루요?”
356|
357|“한때 뻔질나게 드나들던 기루 아니오? 처음 들어 봤다고 변명하진 마시오. 그날 명월루에서 당신을 목격한 사람들의 증언과 수결이 여기 있으니.”
358|
359|말하자면 증언 목록인 셈이다. 나는 어디 한번 읽어나 보자 하는 심정으로 종이를 읽어 내렸다.
360|
361|그리고 이상한 점을 발견했다.
362|
363|“뭐야, 이거?”
364|
365|“직접 보고도 모르겠나?”
366|
367|이 자식이 은근슬쩍 말 놓네.
368|
369|“보니까 하는 소리지. 제대로 된 증언이 없잖아요.”
370|
371|수십 명의 증언을 빠짐없이 읽어 봤지만 결정적인 증언은 어디에도 없었다.
372|
373|하는 말도 비슷비슷하다. 진태경이 거나하게 취해서 방을 잘못 찾았고, 그 방의 주인이 항산검문의 여식이었다는 것. 그리고 비명을 지르는 소리가 났다는 것.
374|
375|“내 누이의 옷을 찢고 범하려 한 놈이 뻔뻔하기 그지없구나. 과연 소문 그대로야.”
376|
377|“아니, 그게 아니고…….”
378|
379|“이놈!”
380|
381|촤르륵!
382|
383|“아.”
384|
385|얼굴을 때린 종이 뭉치가 바닥에 흩어졌다. 이소군이 그 위로 가래를 탁 뱉었다.
386|
387|‘이 새끼 봐라.’
388|
389|짜증이 아니다. 그저 의심이 들 뿐이다.
390|
391|뭐라 할까, 이런 일련의 상황들. 특히 증언에 관련해서 굉장히 작위적인 느낌이 든다고나 할까?
392|
393|하지만 더 이상 찝찝함을 느낄 새도 없었다.
394|
395|“따라 나와라, 네놈이 저지른 짓의 대가를 치르게 해 주마!”
396|
397|이소군이 고함을 내지른 그 순간이었다.
398|
399|띠링.
400|
401|
402|
403|- [비무] 퀘스트가 생성되었습니다.
404|
405|
406|
407|이건 또 뭐야.
```

## Assembled English

```markdown
[P1]
# Chapter 13

[P2]
The five horses raced on. They crossed mountains, fields, and rivers, finally reaching their destination around noon.

[P3]
“Where have you come from?”

[P4]
When the Jin Family of Taiyuan’s gate guard asked the tense question, the young man in the lead smiled. Hostility he could not hide seeped from his crooked, lifted lips.

[P5]
“Mount Heng.”

[P6]
Fifteen minutes later, Jin Wikyung summoned the family’s senior members.

[P7]
* * *

[P8]
Hyuk Mujin could take on any form. All I had to do was picture him in my mind. Spear, sword, saber, bow… Sometimes I won, and sometimes I lost, but one thing was certain.

[P9]
“I’ve got the hang of it now.”

[P10]
The martial arts had become second nature. At first, I had focused on executing them from beginning to end, one form after another. But things were different now.

[P11]
The forms changed with the situation. Martial arts didn’t have to be performed in a fixed sequence, each form flowing into the next. I had reached the point where I could skip that prescribed order and link the forms together.

[P12]
*Like this.*

[P13]
Whoooosh!

[P14]
By the time I heard the wind, it was already too late. His abdomen pierced through, Hyuk Mujin let out a rueful sigh.

[P15]
- You’re improving quickly.

[P16]
“I trained with a spear for seven years, you bastard.”

[P17]
I closed my eyes, then opened them again to find the training hall empty. As if celebrating my victory, a System notification rang out.

[P18]
Ding.

[P19]
> **System**
>
> - **Jin Family’s Spear Technique** has risen to the Fourth Stage!
>
> - **Jin Family’s Manoeuvre Technique** has risen to the Fourth Stage!
>
> - The forms have become more refined, and destructive power has increased.
>
> - Level up!

[P20]
“So I’m Level 14 now?”

[P21]
I had gained three Levels in three days.

[P22]
That was a steep rise for someone who had spent three days holed up in the training hall.

[P23]
On top of that, the Jin Family’s Cultivation Technique had reached the Third Stage, while the Manoeuvre Technique and Spear Technique had both reached the Fourth Stage.

[P24]
“Open Status Window.”

[P25]
After distributing my remaining points, the tip of my nose prickled for some reason.

[P26]
> **System**
>
> **Status Window**
>
> **Lv. 14 Jin Taekyung**
>
> **Occupation:** Second Rate Martial Artist
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

[P27]
“Beautiful. Just beautiful.”

[P28]
Look at those perfectly balanced stats.

[P29]
These were stats *of* combat, *by* combat, and *for* combat.

[P30]
*And that’s not even counting the martial arts.*

[P31]
I wasn’t the same person I had been back then. Hyuk Mujin? I was confident I could beat him now.

[P32]
The F-rank Hunter who hadn’t known the first thing about martial arts was dead. I was now a Murim martial artist who had learned a Peak cultivation technique and two first-rate martial arts.

[P33]
*It starts today.*

[P34]
Everything was ready. Once I left the training hall today, I would gather the things I had in mind and leave the Jin Family of Taiyuan.

[P35]
*I might even be able to get Jin Wikyung’s help.*

[P36]
Just dealing with dim-witted bandits like the Heavenly Axe should let me reach my target quickly. Two days at most. After that, I could return to my family’s warm embrace.

[P37]
*Mom. Hayeon. I miss you.*

[P38]
The rims of my eyes were about to redden when—

[P39]
Grrrrrr—

[P40]
“O-oh! Ohhh!”

[P41]
This was the moment I had been waiting for. The iron door blocking the entrance to the training hall was opening. That dark, heavy chunk of metal looked as beautiful as the gates of heaven.

[P42]
“Finally! I’m getting out!”

[P43]
I ran toward the entrance to heaven with a face full of joy.

[P44]
The angel who would free me from this place appeared behind the door.

[P45]
“Third Young Master. It’s been three days.”

[P46]
He wasn’t exactly a welcome sight, but I was too happy to care.

[P47]
“You came to let me out, right? Huh? You did, right?”

[P48]
Wipeng, an angel who resembled a desert fox, answered in a strangely qualified tone.

[P49]
“Yes. For now.”

[P50]
“…What?”

[P51]
“You will be leaving. But there’s somewhere we need to stop by first.”

[P52]
“Somewhere we need to stop by?”

[P53]
A chill ran down my spine. Some unknown survival instinct reared its head.

[P54]
“Where are we going?”

[P55]
“The main assembly hall. The Lesser Family Head is waiting there as well. And…”

[P56]
Wipeng added,

[P57]
“Senior members of our family and an envoy from the Mount Heng Sword Sect are also there.”

[P58]
“The Mount Heng Sword Sect? Why the hell are they here?”

[P59]
Wolhwa had told me at Honghwaru that the Jin Family of Taiyuan and the Mount Heng Sword Sect were sworn enemies. So why were those bastards here?

[P60]
*Things are going wrong.*

[P61]
This was ominous. Very ominous. I had to find some way out of this.

[P62]
“Then could I stop by my residence and change clothes first?”

[P63]
“No.”

[P64]
“It seems like an important occasion, and I shouldn’t show up smelling like this…”

[P65]
“Are you thinking of running away?”

[P66]
He looked like a desert fox, but his instincts put a meerkat to shame. Before I could say anything, Wipeng’s hand pressed down hard on my shoulder.

[P67]
“Third Young Master. From now on, answer my questions truthfully. Understood?”

[P68]
His voice was dry, and his eyes were cold. The aura coming from him made it impossible for me to open my mouth. All I could do was nod.

[P69]
*Jin Taekyung.*

[P70]
The three-syllable name flashed through my mind.

[P71]
There was no doubt about it. This bastard was responsible. He had dumped a load of shit without me even knowing.

[P72]
And then…

[P73]
“Is it true that you tried to rape the daughter of the Mount Heng Sword Sect?”

[P74]
That shit was far bigger than I could have imagined.

[P75]
* * *

[P76]
As I followed Wipeng toward the main assembly hall, my mind went completely blank.

[P77]
*Attempted rape?*

[P78]
Even if it had only been an attempt, it was a sex crime so vile that beating the culprit to death wouldn’t have been enough.

[P79]
I remembered how I had always said that, as a human being and an older brother with a younger sister, sex offenders should be executed.

[P80]
*That crazy son of a bitch.*

[P81]
My palms were damp with cold sweat. I said it again, not knowing how many times I had repeated it already.

[P82]
“It really wasn’t me. Please believe me.”

[P83]
Without turning around, Wipeng replied,

[P84]
“Has your memory returned?”

[P85]
“No, that’s not what I mean. I’m telling you, it really wasn’t me. Do I look like the kind of guy who’d do that? Like someone who’d go around doing something that disgusting?”

[P86]
“Yes.”

[P87]
No, fuck.

[P88]
He answered without even taking a breath.

[P89]
“Look, then let me stop by the bathroom. Or the privy, I mean.”

[P90]
“No.”

[P91]
“You have to let me take care of business!”

[P92]
“Just do it in your pants.”

[P93]
Son of a bitch. I gave up and immediately turned around and ran, drawing up all my internal energy and concentrating it in my feet.

[P94]
Grab.

[P95]
“Third Young Master.”

[P96]
I was caught in three steps. Wipeng had me by the back of the neck, looking down at me with cold eyes.

[P97]
“If you keep this up… I might have to stop being polite.”

[P98]
Resistance was pointless. Wipeng was a master whose Level I couldn’t determine even with Qi Sense.

[P99]
*No choice.*

[P100]
With a sinking heart, I walked for who knew how long before a tall pavilion came into view.

[P101]
Several warriors were standing guard outside. I recognized the Jin Family of Taiyuan’s distinctive navy uniforms, but some of the men wore red clothes I had never seen before.

[P102]
*Those must be members of the Mount Heng Sword Sect.*

[P103]
Considering the usual relationship between the two sects, they should have been at each other’s throats. Yet right now, they were united in glaring at me.

[P104]
“Fuck…”

[P105]
Wipeng turned his head at my mutter.

[P106]
“The Lesser Family Head believes in you. Don’t forget that.”

[P107]
Right. Jin Wikyung was there. My greatest hope and my shield.

[P108]
As I reminded myself of that fact, Wipeng threw open the doors to the main assembly hall.

[P109]
“I’ve brought the Third Young Master.”

[P110]
I took a deep breath and stepped into the pavilion, repeating the same words over and over in my head.

[P111]
*Even if a tiger carries you off, you can survive if you keep your wits about you. Even if a tiger carries you off, if you just keep your wits about you…*

[P112]
The moment I entered the hall, the low murmuring abruptly stopped. A dozen men, young and old, stood arrayed along either side, while Jin Wikyung occupied the seat of honor.

[P113]
And in the center stood a young man.

[P114]
“It’s been a while, Young Master Jin.”

[P115]
The instant I faced that unpleasant smile—

[P116]
Ding.

[P117]
> **System**
>
> - **Killing intent** detected!

[P118]
…At least use your blinker before pulling in.

[P119]
* * *

[P120]
Killing intent.

[P121]
I knew it well. Monsters were literally bundles of malice and killing intent. I had felt it countless times and thought I had grown used to it.

[P122]
But this guy…

[P123]
*He was different.*

[P124]
This was on an entirely different level from anything I had experienced.

[P125]
If I had to compare it to something, it was like the difference between a low-level monster and a mid-level monster. His killing intent was far more refined, more furtive, and more chilling.

[P126]
“I believe I caught a glimpse of you in the marketplace last time. I don’t know whether you’ll remember me.”

[P127]
Lee Seogeun spat out each word. Above his head, a System window floated in the air.

[P128]
> **System**
>
> **Lv. 30 Lee Seogeun**

[P129]
That was the Level I had read with Qi Sense the instant I detected his killing intent. It was more than twice my Level.

[P130]
*This is insane.*

[P131]
Even worse were the looks from everyone else.

[P132]
Dozens of menacing gazes, young and old alike, were fixed on me. My knees began to go weak. In that atmosphere, Lee Seogeun opened his mouth.

[P133]
“What a shame. If you had come a little earlier, we could have had a deeper conversation. We were discussing something interesting until just now.”

[P134]
“…Were you?”

[P135]
“Wouldn’t you like to know what we were discussing?”

[P136]
“N-no, I’m fine.”

[P137]
I only hoped it wasn’t a discussion about whether to cut off my head or my balls. And if that miserable guess was correct, I would rather they cut off my balls than my head.

[P138]
*If I was lucky, I might be able to recover with a Level Up… Why am I even thinking about this?*

[P139]
It was simply miserable. Lee Seogeun studied my expression before speaking again.

[P140]
“I heard you returned to the family a few days ago. Where have you been?”

[P141]
“Honghwaru.”

[P142]
“Then where were you before you went to Honghwaru?”

[P143]
*I was at a goshiwon, you bastard.*

[P144]
I wanted to tell him everything honestly.

[P145]
*I got fired from my Guild that day, had a glass of soju with the hyung from the goshiwon, then went into the capsule and fell asleep. When I woke up, I was at Honghwaru, and now I’m working hard toward Logout. Something like that.*

[P146]
*I’d be lucky if he didn’t draw his sword.*

[P147]
As I hesitated, unable to answer, Lee Seogeun pulled something from inside his robes. I thought he really was drawing a sword, but it turned out to be a bundle of papers.

[P148]
“Since you don’t seem to remember, I’ll tell you. The night before you went to Honghwaru, you visited Myeongwollu. You went to the top-tier room you had reserved.”

[P149]
“Myeongwollu?”

[P150]
“The pleasure house you used to frequent? Don’t try to make excuses by saying you’ve never heard of it. These are the testimonies and signatures of the people who saw you there that day.”

[P151]
In other words, it was a list of witness statements. Figuring I might as well look, I read through the papers.

[P152]
Then I noticed something strange.

[P153]
“What is this?”

[P154]
“You don’t know even after seeing it yourself?”

[P155]
This bastard was dropping the formal speech now, too.

[P156]
“I’m saying that because I read it. There isn’t a single proper testimony here.”

[P157]
I read every one of the dozens of statements, but not one contained anything decisive.

[P158]
They all said roughly the same thing: Jin Taekyung had gotten thoroughly drunk, gone to the wrong room, and that room had belonged to the daughter of the Mount Heng Sword Sect. Then a scream had rung out.

[P159]
“The bastard who tore my sister’s clothes and tried to rape her is shameless beyond belief. You really are exactly as the rumors say.”

[P160]
“No, that’s not what—”

[P161]
“You bastard!”

[P162]
Flutter!

[P163]
“Ah.”

[P164]
The bundle of papers smacked me in the face and scattered across the floor. Lee Seogeun spat a wad of phlegm onto them.

[P165]
*Well, look at this asshole.*

[P166]
I wasn’t annoyed. Just suspicious.

[P167]
How should I put it? This whole chain of events—especially the witness statements—felt incredibly contrived.

[P168]
But I had no time to dwell on that unease.

[P169]
“Come out with me, you bastard! I’ll make you pay for what you’ve done!”

[P170]
The instant Lee Seogeun shouted—

[P171]
Ding.

[P172]
> **System**
>
> - The **Duel** Quest has been generated.

[P173]
What’s this now?
```


## Accepted baseline for regression comparison

This is the accepted English copy before mastering. Use it as a regression
anchor: report a finding when the assembled copy loses an established term,
source-specific image, formatting convention, continuity fact, or other detail
that the baseline preserved, unless the Korean source clearly requires the
change.

```markdown
[P1]
# Chapter 13

[P2]
The five horses ran hard. They passed mountains, fields, and rivers, finally reaching their destination around noon.

[P3]
“Where are you coming from?”

[P4]
When the Jin Family of Taiyuan’s gate guard asked the tense question, the young man in the lead smiled. Hostility he could not hide seeped from his crooked, lifted lips.

[P5]
“Mount Heng.”

[P6]
Jin Wikyung summoned the family’s senior members fifteen minutes later.

[P7]
* * *

[P8]
Hyuk Mujin could take on any form. All I had to do was picture him in my mind. Spear, sword, saber, bow… There were times I won and times I lost, but one thing was certain.

[P9]
“I’ve got the hang of it now.”

[P10]
The martial arts had become second nature. At first, I had focused on executing them from beginning to end, one form after another. But things were different now.

[P11]
The forms changed depending on the situation. Martial arts didn’t have to consist of one form flowing into the next in a fixed order. I had reached the point where I could skip the prescribed sequence and link forms together.

[P12]
*Like this.*

[P13]
Whoooosh!

[P14]
By the time I heard the wind, it was already too late. Hyuk Mujin, his abdomen pierced through, let out a rueful sigh.

[P15]
- You’re improving quickly.

[P16]
“I trained with a spear for seven years, you bastard.”

[P17]
When I opened my eyes again, the empty training hall came into view. As if celebrating my victory, the System notification rang out.

[P18]
Ding.

[P19]
> **System**
>
> - **Jin Family’s Spear Technique** has risen to the Fourth Stage!
>
> - **Jin Family’s Manoeuvre Technique** has risen to the Fourth Stage!
>
> - The forms have become more refined, and destructive power has increased.
>
> - Level up!

[P20]
“So I’m Level 14 now?”

[P21]
I had gained three Levels in three days.

[P22]
That was a steep rise for someone who had holed up in the training hall for three days.

[P23]
On top of that, the Jin Family’s Cultivation Technique had reached the Third Stage, while the Manoeuvre Technique and Spear Technique had reached the Fourth Stage.

[P24]
“Open Status Window.”

[P25]
After distributing my remaining points, I felt a sting at the tip of my nose for some reason.

[P26]
> **System**
>
> **Status Window**
>
> **Lv. 14 Jin Taekyung**
>
> **Occupation:** Second Rate Martial Artist
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

[P27]
“Beautiful. Just beautiful.”

[P28]
Look at those perfectly balanced stats.

[P29]
These were stats *of* combat, *by* combat, and *for* combat.

[P30]
*And that’s not even counting the martial arts.*

[P31]
I wasn’t the same person I had been back then. Hyuk Mujin? I was confident I could beat him now.

[P32]
The F-rank Hunter Jin Taekyung, who didn’t know the first thing about martial arts, was dead. I was now a Murim martial artist who had learned a Peak cultivation technique and two first-rate martial arts.

[P33]
*It starts today.*

[P34]
Everything was ready. Once I left the training hall today, I would gather the things I had in mind and leave the Jin Family of Taiyuan.

[P35]
*I might even be able to get Jin Wikyung’s help.*

[P36]
I could reach my target quickly just by dealing with idiot bandits like the Heavenly Axe. Two days at most. After that, I could return to my warm family.

[P37]
*Mom. Hayeon. I miss you.*

[P38]
That was when the rims of my eyes started to go red.

[P39]
Grrrrrr—

[P40]
“O-oh! Ohhh!”

[P41]
This was the moment I had been waiting for. The iron door blocking the entrance to the training hall was opening. That ugly, heavy chunk of metal looked as beautiful as the gates of heaven.

[P42]
“Finally! I’m getting out!”

[P43]
I ran toward the entrance to heaven with a face full of joy.

[P44]
The angel who would free me from this place appeared behind the door.

[P45]
“Third Young Master. It’s been three days.”

[P46]
He wasn’t exactly a welcome sight, but I was too happy to care.

[P47]
“You came to let me out, right? Huh? You did, right?”

[P48]
Wipeng, an angel who resembled a desert fox, answered in a strangely qualified tone.

[P49]
“Yes. For now.”

[P50]
“…What?”

[P51]
“You will be leaving. But there’s somewhere we need to stop by first.”

[P52]
“Somewhere we need to stop by?”

[P53]
A chill ran down my spine. Some kind of survival instinct raised its head.

[P54]
“Where are we going?”

[P55]
“The main assembly hall. The Lesser Family Head is waiting there as well. And…”

[P56]
Wipeng added,

[P57]
“Senior members of our family and an envoy from the Mount Heng Sword Sect have also arrived.”

[P58]
“The Mount Heng Sword Sect? Why the hell are they here?”

[P59]
Wolhwa had told me at Honghwaru. The Jin Family of Taiyuan and the Mount Heng Sword Sect were sworn enemies. So why were those bastards here?

[P60]
*Things are going wrong.*

[P61]
This was ominous. Very ominous. I had to find some kind of way out of this.

[P62]
“Then could I stop by my residence and change clothes first?”

[P63]
“No.”

[P64]
“It seems like an important occasion, and I can’t show up smelling like this…”

[P65]
“Are you thinking of running away?”

[P66]
He looked like a desert fox, but his instincts put a meerkat to shame. Before I could say anything, Wipeng’s hand pressed down hard on my shoulder.

[P67]
“Third Young Master. From now on, answer my questions truthfully. Understood?”

[P68]
His voice was dry, and his eyes were cold. The aura coming from him made it impossible for me to open my mouth. All I could do was nod.

[P69]
*Jin Taekyung.*

[P70]
The three-syllable name flashed through my mind.

[P71]
There was no doubt about it. This bastard was responsible. He had dumped a load of shit without me even knowing.

[P72]
And then…

[P73]
“Is it true that you tried to rape the daughter of the Mount Heng Sword Sect?”

[P74]
That shit was far bigger than I could have imagined.

[P75]
* * *

[P76]
On the way to the main assembly hall behind Wipeng, my mind was completely blank.

[P77]
*Attempted rape?*

[P78]
Even if it had ended at an attempt, it was a sex crime so vile that beating the culprit to death wouldn’t have been enough.

[P79]
I remembered how I had always said that, as a human being and an older brother with a younger sister, sex offenders should be executed.

[P80]
*What kind of fucking lunatic was he?*

[P81]
My palms were damp with cold sweat. I said it again, not knowing how many times I had repeated it already.

[P82]
“I really wasn’t the one. Please believe me.”

[P83]
Without turning around, Wipeng replied,

[P84]
“Has your memory returned?”

[P85]
“No, that’s not what I mean. I’m telling you, it really wasn’t me. Do I look like the kind of guy who’d do that? The kind of guy who’d go around committing trash like that?”

[P86]
“Yes.”

[P87]
No, fuck.

[P88]
He answered without even taking a breath.

[P89]
“Look, then let me stop by the bathroom. Or the privy, I mean.”

[P90]
“No.”

[P91]
“You have to let me take care of business!”

[P92]
“Just go here.”

[P93]
Son of a bitch. I gave up and immediately turned around and ran, drawing up all my internal energy and concentrating it in my feet.

[P94]
Grab.

[P95]
“Third Young Master.”

[P96]
I was caught in three steps. Wipeng had me by the back of the neck, looking down at me with cold eyes.

[P97]
“If you keep this up… I might have to stop being polite.”

[P98]
Resistance was pointless. Wipeng was a master whose Level I couldn’t determine even with Qi Sense.

[P99]
*No choice.*

[P100]
With a sinking heart, I walked for who knew how long before a tall pavilion came into view.

[P101]
Several warriors were standing guard outside. I recognized the Jin Family of Taiyuan’s distinctive navy uniforms, but some of the men wore red clothes I had never seen before.

[P102]
*Those must be members of the Mount Heng Sword Sect.*

[P103]
Considering the usual relationship between the two sects, they should have been sworn enemies. Yet right now, they were united in glaring at me.

[P104]
“Fuck…”

[P105]
Wipeng turned his head at my mutter.

[P106]
“The Lesser Family Head believes in you. Don’t forget that.”

[P107]
Right. Jin Wikyung was there. My greatest hope and my shield.

[P108]
As I reminded myself of that fact, Wipeng threw open the doors to the main assembly hall.

[P109]
“I’ve brought the Third Young Master.”

[P110]
I took a deep breath and stepped into the pavilion. Inside my head, I kept repeating the same words.

[P111]
*Even if a tiger carries you off, you can survive if you keep your wits about you. Even if a tiger carries you off, you can keep your wits—*

[P112]
The moment I entered the hall, the low murmuring abruptly stopped. A dozen men, young and old, stood arrayed along either side, while Jin Wikyung occupied the seat of honor.

[P113]
And in the center stood a young man.

[P114]
“It’s been a while, Young Master Jin.”

[P115]
The instant I met that unpleasant smile—

[P116]
Ding.

[P117]
> **System**
>
> - **Killing intent** detected!

[P118]
…At least use your blinker before pulling in.

[P119]
* * *

[P120]
Killing intent.

[P121]
I knew it well. Monsters were literally bundles of malice and killing intent. I had felt it countless times and thought I had grown used to it.

[P122]
But this guy…

[P123]
*He was different.*

[P124]
This was on an entirely different level from anything I had experienced.

[P125]
If I had to compare it to something, it was like the difference between a low-level monster and a mid-level monster. His killing intent was far more refined, more furtive, and more chilling.

[P126]
“I believe I caught a glimpse of you in the marketplace last time. I don’t know whether you’ll remember me.”

[P127]
Each word was spat out by Lee Seogeun. Above his head, a System window floated in the air.

[P128]
> **System**
>
> **Lv. 30 Lee Seogeun**

[P129]
That was the Level I had seen with Qi Sense the instant I detected his killing intent. It was more than twice my Level.

[P130]
*This is insane.*

[P131]
Even worse were the looks from everyone else.

[P132]
Dozens of sinister gazes, young and old alike, were fixed on me. My knees began to tremble. In that atmosphere, Lee Seogeun opened his mouth.

[P133]
“What a shame. If you had come a little earlier, we could have had a deeper conversation. We were discussing something interesting until just now.”

[P134]
“…Were you?”

[P135]
“Wouldn’t you like to know what we were discussing?”

[P136]
“N-no, I’m fine.”

[P137]
I only hoped it wasn’t a discussion about whether to cut off my head or my balls. And if that miserable guess was correct, I preferred them to cut off my balls instead of my head.

[P138]
*I might be able to recover with a Level Up if they did that… Why am I even thinking about this?*

[P139]
It was simply miserable. Lee Seogeun studied my expression before speaking again.

[P140]
“I heard you returned to the family a few days ago. Where have you been?”

[P141]
“Honghwaru.”

[P142]
“Then where were you before you went to Honghwaru?”

[P143]
*I was at a goshiwon, you bastard.*

[P144]
I wanted to tell him everything honestly.

[P145]
*I got fired from my Guild that day, had a glass of soju with the hyung from the goshiwon, then went into the capsule and fell asleep. When I woke up, I was at Honghwaru, and now I’m working hard toward Logout. Something like that.*

[P146]
*It’d be a miracle if he didn’t draw his sword.*

[P147]
As I hesitated, unable to answer, Lee Seogeun pulled something from inside his robes. I thought he really was drawing a sword, but it turned out to be a bundle of papers.

[P148]
“Since you don’t seem to remember, I’ll tell you. The night before you went to Honghwaru, you visited Myeongwollu. You went to the top-tier room you had reserved.”

[P149]
“Myeongwollu?”

[P150]
“The pleasure house you used to visit all the time? Don’t try to make excuses by saying you’ve never heard of it. These are the testimonies and seals of the people who saw you there that day.”

[P151]
In other words, it was a list of witness statements. I read through the papers, thinking I might as well take a look.

[P152]
Then I noticed something strange.

[P153]
“What is this?”

[P154]
“You don’t know even after seeing it yourself?”

[P155]
This bastard was dropping the formal speech now, too.

[P156]
“I’m saying that because I read it. There isn’t a single proper testimony here.”

[P157]
I read every one of the dozens of statements, but there wasn’t a decisive testimony anywhere.

[P158]
They all said roughly the same thing: Jin Taekyung had gotten thoroughly drunk, gone to the wrong room, and found that the room belonged to the daughter of the Mount Heng Sword Sect. Then someone had heard screaming.

[P159]
“The bastard who tore my sister’s clothes and tried to rape her is shameless beyond belief. You really are exactly as the rumors say.”

[P160]
“No, that’s not what—”

[P161]
“You bastard!”

[P162]
Flutter!

[P163]
“Ah.”

[P164]
The bundle of papers smacked me in the face and scattered across the floor. Lee Seogeun spat a wad of phlegm onto them.

[P165]
*Well, look at this asshole.*

[P166]
It wasn’t irritation. I was simply suspicious.

[P167]
How should I put it? This whole chain of events—especially the testimonies—felt incredibly contrived.

[P168]
But I had no time to dwell on that unease.

[P169]
“Come out with me, you bastard! I’ll make you pay for what you’ve done!”

[P170]
The instant Lee Seogeun shouted—

[P171]
Ding.

[P172]
> **System**
>
> - The **Duel** Quest has been generated.

[P173]
What’s this now?
```


## Deterministic QA

```json
{
  "version": 1,
  "chapter": 13,
  "passed": true,
  "metrics": {
    "source_characters": 5515,
    "translation_characters": 12683,
    "length_ratio": 2.3,
    "source_paragraphs": 185,
    "translation_paragraphs": 173
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "일류",
        "preferred": "First Rate"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "사형",
        "preferred": "Senior Brother"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "진가심법",
        "preferred": "Jin Family's Cultivation Technique"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "진가보법",
        "preferred": "Jin Family's Manoeuvre Technique"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "진가창법",
        "preferred": "Jin Family's Spear Technique"
      }
    }
  ]
}
```

## Binding editorial rules

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
- Use `qi` for Murim energy and `mana` for the modern Hunter system when the source distinguishes them. Preserve an established chapter-specific rendering such as `internal energy` when the exact glossary and surrounding Korean distinguish accumulated `공력` from resulting `기운`.
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

# Master Editorial Brief

You are the final English-language editor of an existing Korean-to-English novel translation.

The Korean source is the authority for meaning. The existing English is the baseline you are editing, not a draft to discard. Your task is to make the chapter read like professionally written native English commercial fiction while preserving the author's exact story, characterization, humor, register, pacing, ambiguity, and cultural texture.

## Editorial authority

You may freely recast sentences and paragraphs when the English is stiff, literal, repetitive for accidental reasons, awkwardly collocated, over-explained, or syntactically shaped by Korean. You may tighten dialogue, improve rhythm, repair transitions, and make action easier to follow. A technically correct sentence may still need rewriting if a fluent English novelist would not naturally phrase it that way.

Do not change text merely to make it different. If the baseline is already strong, leave it alone.

The accepted baseline is also the project's style and terminology anchor. Do not
replace an established rendering, cultural term, System label, Markdown form, or
recurring phrase with a synonym merely because the synonym sounds smoother.
Make that change only when the Korean source, `RULES.md`, or the exact glossary
requires it. In particular, do not turn a source-specific image into a nearby
English image, or change a gold-spoon joke, item name, technique name, or UI
label into a different expression without source support.

## Fidelity constraints

Never invent, omit, explain away, generalize, intensify, soften, or reinterpret source-supported content. In particular, preserve:

- exact actions, subjects, objects, directionality, causality, quantities, and physical details;
- deliberate ambiguity, euphemism, implication, profanity level, repetition, and withheld information;
- jokes and comic specificity, even when a more generic English joke would sound smoother;
- hierarchy, kinship, forms of address, characterization, and speaker attitude;
- System mechanics, Murim concepts, names, ranks, techniques, items, organizations, and established terminology.
- chapter-level logical consistency: interpret labels, counters, notifications, and repeated facts from how they behave across the scene, not from an isolated surface gloss;
- idioms by their narrative function rather than their component words, and jokes with their setup, recognition, and punchline timing intact;
- cross-sentence implications: do not create a claim that contradicts “again,” an increasing value, an earlier action, or the explanation immediately around it;
- repeated terminology and formatting: once the baseline or glossary establishes a rendering, keep it consistent throughout the chapter unless the source clearly changes the sense;

Do not add jokes, metaphors, explanations, emotional conclusions, or colorful details that are absent from the Korean. Do not replace a specific source image with a generic equivalent merely because the generic version is smoother.

When natural English and literal form conflict, preserve the source meaning and pragmatic effect while changing the English form as much as necessary.

Before returning the chapter, perform a silent continuity pass: trace every
counter, quantity, repeated System label, item or technique name, joke setup and
payoff, and physical cause-and-effect sequence from the Korean through the
finished English. Correct any local sentence that contradicts the sequence.

## Relationship to project files

`RULES.md` is binding. `POLISH.md` describes known translation-English failure modes and should guide the edit. Exact glossary matches are binding unless the packet explicitly marks them otherwise. Character/continuity material is context only and must never override the chapter's Korean source.

## Output

Return only the complete edited English Markdown chapter. Preserve the required chapter heading and project Markdown conventions. Do not provide commentary, a change log, explanations, or a Markdown code fence.
