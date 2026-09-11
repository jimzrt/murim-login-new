# Fidelity Gate — Chapter 10

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
  1|＃10화
  2|
  3|
  4|
  5|십여 분을 걸어 도착한 곳은 태원진가의 후방을 가로막은 절벽이었다. 커다랗게 아가리를 벌린 동공(洞空). 그 앞에 한 사람이 있었다.
  6|
  7|“음. 왔느냐?”
  8|
  9|불곰 같은 덩치에 근엄한 말투. 진위경이다. 나는 엉거주춤하게 고개를 숙여 보였다.
 10|
 11|“안녕하십니까, 형……님.”
 12|
 13|진위경은 껄끄러운 존재다. 졸지에 NPC 가족이 생긴 것도 모자라 나한테 엄청 관심이 많기 때문이다.
 14|
 15|저 봐라, 남들 보는 눈이 있다고 티 내지 않으려고 무지 애쓰는 거. 하지만 자세히 보면 눈동자가 촉촉하게 젖어 있다.
 16|
 17|‘감수성 실화냐.’
 18|
 19|외관상으로는 삼합회 두목도 한 수 접고 들어갈 것 같은데, 이 게임 캐릭터들은 어째 다 요지경인지 모르겠다.
 20|
 21|“네 행실을 더 이상 묵과할 수 없어 소가주이자 가주 대행의 직분으로 폐관을 명했다. 하고 싶은 말이 있느냐?”
 22|
 23|‘당연히 있지.’
 24|
 25|그러나 짜고 치는 고스톱이다. 수련동으로 오는 길에 위팽에게 돌아가는 사정을 들었다. 태원진가 내에서 권력층 간의 힘 싸움이 있고, 진위경이 내 방패 역할을 해 주고 있다는 것.
 26|
 27|이번 강제 폐관 행은 그러니까, 쇼인 거다.
 28|
 29|
 30|
 31|‘어차피 공자도 수련 공간이 필요하다고 하지 않았습니까? 사흘만 참으십시오.’
 32|
 33|
 34|
 35|나는 위팽의 마지막 말을 떠올리며 반성하는 척 고개를 숙였다.
 36|
 37|“죗값을 달게 받겠습니다.”
 38|
 39|이 연극의 장점은 대사가 짧다는 것이다. 진위경은 애잔한 눈빛으로 마지막 대사를 읊었다.
 40|
 41|“죄인을 수련동에 가둬라. 출관 날짜는 차후 통보하겠다.”
 42|
 43|말이 끝나기가 무섭게 수련동 입구를 지키던 무사 두 명이 다가와 내 양팔을 붙들었다. 연극이 끝났으니 퇴장할 차례.
 44|
 45|나는 수련동 입구에 섰다.
 46|
 47|- 필요한 것은 가져다 놨다. 막내야, 무리하지 말거라.
 48|
 49|진위경의 전음과 함께 첫발을 내디뎠다.
 50|
 51|
 52|
 53|* * *
 54|
 55|
 56|
 57|수련동은 한마디로 동굴이었다. 그것도 절벽을 파서 만든 인공 동굴. 높고, 넓었다. 그리고 축축했다.
 58|
 59|철벅철벅.
 60|
 61|수련동 소속 무사를 따라 얼마나 걸었을까. 내가 신은 것이 가죽신인지 물걸레인지 헷갈릴 때쯤 거대한 철문이 나타났다.
 62|
 63|‘와…….’
 64|
 65|보는 순간 입이 벌어졌다. 통로를 빈틈없이 채운 그것은 문이라기보다 모든 출입을 금지하는 벽처럼 보였다.
 66|
 67|안내해 준 무사가 횃불을 들고 외쳤다.
 68|
 69|“개문!”
 70|
 71|그그긍-
 72|
 73|거대한 철문이 천천히 아가리를 벌렸다. 무슨 열려라 참깨 같은 마법 주문은 아니고, 미리 대기하고 있던 NPC 한 명이 삐죽 튀어나와 있는 개폐 장치를 잡아당긴 것뿐이었지만 압도적인 광경이었다.
 74|
 75|그리고 내부가 눈에 들어온 순간.
 76|
 77|“우와.”
 78|
 79|이번만큼은 나도 새어 나오는 탄성을 숨기지 못했다.
 80|
 81|처음 수련동에 들어올 때만 해도 축축한 지하 동굴을 생각했는데…….
 82|
 83|“이게 다 뭐야.”
 84|
 85|넓은 침상에 보기만 해도 기분이 좋아지는 털 이불. 축축하고 울퉁불퉁한 돌바닥 대신 깔끔한 회색 지면이 펼쳐져 있다.
 86|
 87|‘시멘트……는 당연히 아니겠고 석회석인가?’
 88|
 89|냉기가 감도는 것만 빼면, 아니, 그걸 감안해도 상상 이상으로 괜찮은 환경이다.
 90|
 91|‘이게 처벌이라고?’
 92|
 93|얼떨떨하게 주위를 바라보는데 등 뒤에서 헛기침 소리가 들렸다. 돌아보니 안내역을 한 수련동 무사다.
 94|
 95|“필요한 것들은 모두 갖춰 놓았습니다. 그럼 저는 이만.”
 96|
 97|그그긍. 천천히 닫히는 철문을 바라보다가 문득 수련동 입구에서 들었던 전음이 생각났다.
 98|
 99|
100|
101|‘필요한 것은 가져다 놨다. 막내야, 무리하지 말거라.’
102|
103|
104|
105|아아, 그것은 동생을 생각하는 NPC의 마음.
106|
107|이 못난 유저는 목 놓아 웁니다.
108|
109|
110|
111|* * *
112|
113|
114|
115|현실에서도 숱하게 일어나는 일이다. 비리를 저지른 고위층들이 휠체어를 타고 검찰을 드나들고, 수사를 피하기 위해 병원 특실에 입원하는 것.
116|
117|조금 다르긴 해도 내가 지금 그 모양새다. 나는 감동한 얼굴로 수련동 특실을 바라봤다.
118|
119|“이런 게 금수저의 삶이구나.”
120|
121|그래픽, 인공지능만 현실적인 게 아니다. 아무리 날고 기어도 금수저가 최고라는 사회적 메시지를 담고 있다.
122|
123|세상에, 이 캐릭터 아니면 어쩔 뻔했어. 아빠가 가주, 큰형이 소가주에 둘째 형은 무공의 천재다. 마음 놓고 기루 죽돌이 짓 할 만하다.
124|
125|‘진태경 이 새끼…….’
126|
127|알고 보니 어린 나이에 세상 돌아가는 이치를 깨달은 대현자가 아닌가.
128|
129|나는 현실적인 갓-수저 시스템에 전율하며 백여 평에 달하는 수련동을 돌아다녔다. 그리고 수련동 무사가 말한 ‘필수품들’을 찾을 수 있었다.
130|
131|‘우선 식량.’
132|
133|식량은 항아리 두 개에 나뉘어 보관되어 있었다. 속을 들여다보니 약재 냄새가 진하게 풍기는 주먹밥이다.
134|
135|
136|
137|아이템창
138|
139|
140|
141|[뛰어난 벽곡단]
142|
143|종류 : 단환
144|
145|등급 : 일류
146|
147|제한 : 없음
148|
149|설명 : 온갖 좋은 약재를 무식하게 때려 박아 만든 벽곡단. 섭취 시 원기를 회복하며, 장복할 경우 추가적인 효과를 얻는다.
150|
151|
152|
153|
154|
155|“아, 이게 바로 그 벽곡단?”
156|
157|무협 소설에서 많이 봤다. 가볍고 부피가 작아서 휴대하기 편한 데다 영양 보충까지 된단다. 나머지 항아리에도 벽곡단이 그득했다.
158|
159|‘일단 인벤토리에 넣어 둬야지.’
160|
161|양손으로 항아리를 잡고 중얼거렸다.
162|
163|“아이템 습득.”
164|
165|다른 사람이 이 모습을 봤다면 놀라 자빠졌을 거다. 멀쩡하게 놓여 있던 항아리 두 개가 증발한 듯이 사라졌으니까.
166|
167|나는 인벤토리에 수납된 항아리를 흐뭇하게 바라봤다.
168|
169|‘이걸로 식량 문제는 해결됐고.’
170|
171|그다음으로 발견한 두 번째 필수품은 물이다. 수련동 내부는 엄연히 동굴이라, 한쪽 구석에 차가운 지하 샘물이 있어 식수 문제를 해결해 주었다.
172|
173|그리고 마지막 세 번째.
174|
175|“흠.”
176|
177|여러 개의 병기가 나란히 걸려 있는 무기 거치대. 당연하게도 가장 먼저 손에 쥔 것은 단단해 보이는 목창(木槍)이다.
178|
179|‘아이템 감정.’
180|
181|띠링.
182|
183|
184|
185|아이템창
186|
187|
188|
189|[수련용 목창]
190|
191|종류 : 병장기
192|
193|등급 : 삼류
194|
195|제한 : 없음
196|
197|설명 : 초보자용으로 제작되었다.
198|
199|
200|
201|
202|
203|“오.”
204|
205|초보자를 대상으로 만들어진 수련용 목창. 지금의 내게 딱 맞는 물건이다. 여기에 하나만 더 있으면 완벽하지.
206|
207|“인벤토리 오픈.”
208|
209|나는 씩 웃으며 인벤토리에서 [진가창법]이 적힌 비급을 꺼냈다.
210|
211|띠링.
212|
213|
214|
215|- [진가창법]을 습득하시겠습니까? (3 / 10)
216|
217|
218|
219|“당연히 예스지.”
220|
221|나는 시스템이 참 좋다. 가끔은 사랑스럽다.
222|
223|
224|
225|* * *
226|
227|
228|
229|어제 진가보법을 익히며 처음 알게 됐다. 시스템 알림은 띠링, 하나만이 아니라는 사실을.
230|
231|그리고 저 소리가 얼마나 듣기 싫은 소리인지를.
232|
233|삑!
234|
235|
236|
237|- 동작이 실패했습니다.
238|
239|- 남은 성공 횟수 (2 / 100)
240|
241|
242|
243|실패 메시지. 일명 삑사리가 나면 어김없이 뜨는 시스템창이다. 도대체 몇 번째 보는 메시지인지 모르겠다.
244|
245|나는 손에 쥔 [수련용 목창]을 바라봤다.
246|
247|‘잘못 생각했네.’
248|
249|목창이라 그런가, 가볍다. 찌르면 찌르는 대로, 휘두르면 휘두르는 대로 빠르게 움직인다. 그래서 문제다.
250|
251|‘너무 가벼워서 조절하기가 힘들어.’
252|
253|미세한 조정이 어렵다 보니 자꾸만 삐끗한다. 더럽게 깐깐한 시스템이 그런 사소한 실수를 눈감아 줄 리가 없다.
254|
255|삑.
256|
257|
258|
259|- 동작이 실패했습니다.
260|
261|- 남은 성공 횟수 (5 / 100)
262|
263|
264|
265|“아오. 시발.”
266|
267|결국 [수련용 목창]을 내던지고 [예리한 창]을 인벤토리에서 꺼냈다. 길이나 창대의 굵기가 내가 현실에서 쓰던 창과 얼추 맞아떨어진다.
268|
269|그런데 왜 처음부터 꺼내지 않았냐고?
270|
271|“더럽게 무겁네. 진짜.”
272|
273|통짜 강철로 만들었다 보니 무게가 장난이 아니다. 체감상 느껴지는 무게만 얼추 50kg에 육박하는 괴물인 것이다.
274|
275|이런 걸 몇 시간이고 휘둘렀다가는 내 체력이 못 버틴다.
276|
277|현재 내 경지는 이류, 시스템의 힘을 빌렸다지만 쌀 반 가마니가 넘는 무게를 팔랑개비처럼 휘두르는 건 무리다.
278|
279|‘어디서 호랑이 기운이 솟아나는 것도 아니고.’
280|
281|그런 생각을 했을 때였다.
282|
283|“……어?”
284|
285|내가 방금 뭐라고 했지? 호랑이 힘?
286|
287|“있네?”
288|
289|이곳은 게임이다. 시스템이 있고 능력치가 있다. 그리고 공력이 있다. 심법을 통해 이끌어 낼 수 있는 10년의 공력이!
290|
291|잠깐이나마 잊고 있었다는 게 쪽팔릴 정도다.
292|
293|“내가 그런 걸 써 봤어야지…….”
294|
295|고기도 먹어 본 놈이 안다고 했다. F급 헌터가 괜히 F급이겠나. 마나라고는 쥐뿔도 없이 맨몸으로 때우니까 헌터들 사이에서도 반푼이 취급받는 거다.
296|
297|‘그래도 문제 하나는 해결했네.’
298|
299|허허, 나는 어이없게 웃으며 창을 집어 들었다. 그리고 천천히, 신중하게 공력을 끌어 올렸다.
300|
301|머릿속에서는 시스템이 각인시킨 진가심법의 구결이 빠르게 되감기며 공력을 정해진 길로 이끈다.
302|
303|찌릿.
304|
305|반응은 즉각적이었다.
306|
307|단전에 웅크리고 있던 10년 공력이 전신으로 퍼져 나간다. 게임이라서, 무림인이라서 느낄 수 있는 그 기운이 사지백해로 뻗어 나가는 것이 느껴졌다.
308|
309|‘이건…….’
310|
311|온몸에 힘이 넘쳐흐른다. 월등히 상향된 신체 능력과 감각은 F급 헌터로 살아온 내게 다시 한번 황홀함을 선사해 주었다.
312|
313|‘이렇게 달라질 수 있다니.’
314|
315|나는 창을 잡고 [진가창법]을 펼쳤다. 더 이상 무겁게 느껴지지 않는 50kg의 철창은 내가 원하는 길을 따라 허공을 찌르고 베었다.
316|
317|이윽고.
318|
319|띠링.
320|
321|
322|
323|- 남은 성공 횟수 (6 / 100)
324|
325|
326|
327|기다리던 알림이 울리기 시작했다.
328|
329|
330|
331|* * *
332|
333|
334|
335|진위경이 근심 섞인 얼굴로 입을 열었다.
336|
337|“잘하고 있겠지?”
338|
339|“잘하고 있겠지요. 염치가 있으면.”
340|
341|“아직 몸도 성치 않은데…… 괜찮겠지?”
342|
343|“모르는 사람이 보면 삼공자가 오늘내일하는 줄 알겠습니다. 저 정도면 침 발라도 나아요.”
344|
345|“아니야. 막내가 어릴 때부터 얼마나 허약했는지 자네가 몰라서 하는 말이야.”
346|
347|위팽이 기가 찬 얼굴로 대답했다.
348|
349|“삼공자 입으로 들어간 영약과 보양제만 해도 방 하나를 채울 겁니다. 그리고 벌써 잊으셨습니까? 작년에 있었던 백년설삼 절도 사건!”
350|
351|“어허. 그건…….”
352|
353|“그때 약왕당주가 대노해서 삼공자 배를 갈라 보겠다고 날뛰는데, 솔직히 말리면서도 그런 생각이 들더군요. 갈라도 정당방위라고.”
354|
355|진위경은 슬쩍 시선을 회피했다. 결국 진위경의 개인 사재를 털어 보상하는 것으로 마무리됐지만 당시 약왕당주의 분노는 대단했다.
356|
357|“그 정도 영약을 꿀꺽했으니 모르긴 몰라도 죽을 때까지 잔병치레는 안 할 겁니다.”
358|
359|“그래도 부족해. 자네는 딱 보면 모르나? 나는 막내 볼 때마다 안쓰러워. 애가 뼈다귀에 살점 몇 개 붙어 있는 꼴이잖나. 아침마다 비리비리해서 힘도 없고.”
360|
361|“힘이 없다고요?”
362|
363|위팽은 순간 과거에 들었던 소문을 떠올렸다. 태원 홍등가 기녀들 사이에서 진태경이 야왕(焲王)이라는 별명으로 불린다는 소문이었다.
364|
365|‘도대체 어느 정도길래.’
366|
367|약발 하나는 제대로 받은 모양이군. 위팽은 자신도 모르게 팔뚝을 들어 크기를 상상해 보았다.
368|
369|“자네 뭐 하나?”
370|
371|“아, 아닙니다.”
372|
373|진위경은 산더미처럼 쌓인 서류 더미를 보며 한숨을 내쉬었다.
374|
375|“막내도 그렇고, 가문 안팎으로 신경 쓸 일 천지야. 특히…… ‘그들’이 접선해 온 것도 꺼림칙하고.”
376|
377|“항산검문 말씀이시군요.”
378|
379|항산검문. 그 이름이 갖는 무게는 결코 가볍지 않았다.
380|
381|수십 년 전, 어느 불패(不敗)의 낭인이 현판을 내건 이래 무서운 속도로 성장해 왔고, 작금에 이르러서는 태원진가의 입지를 위협할 정도가 되었다.
382|
383|“무슨 의도일까?”
384|
385|“수하들을 풀어 알아보고 있습니다.”
386|
387|진위경은 항산검문에서 온 서신을 만지작거렸다.
388|
389|왜? 어떤 목적으로 그들이 오는가? 꼬리에 꼬리를 무는 의문 끝에 내린 결론은 하나였다.
390|
391|“산서성 각 지부에 알리게. 항산검문의 목적이 무엇이든 간에 만반의 준비를 갖추라고.”
392|
393|이곳은 무림이다.
394|
395|준비된 자만이 살아남아 내일을 맞이할 수 있으리라.
```

## Assembled English

```markdown
[P1]
# Chapter 10

[P2]
After walking for more than ten minutes, we arrived at a cliff that blocked off the rear of the Jin Family of Taiyuan. A massive cavern gaped open in its face. One person stood in front of it.

[P3]
“Hmm. You came?”

[P4]
He had the build of a brown bear and a solemn way of speaking.

[P5]
Jin Wikyung.

[P6]
I bowed awkwardly.

[P7]
“Hello, big… brother.”

[P8]
Jin Wikyung was an awkward presence. As if suddenly gaining an NPC family wasn’t enough, he also paid an absurd amount of attention to me.

[P9]
Just look at him. He was trying his damnedest not to show it with everyone watching. But if you looked closely, his eyes were glistening.

[P10]
*Is this guy seriously that sentimental?*

[P11]
With his appearance, he looked like the kind of man who could make even a triad boss back down. Yet somehow, every character in this game was completely bizarre.

[P12]
“I can no longer overlook your conduct. In my capacity as Lesser Family Head and acting Family Head, I have ordered you to undergo closed-door training. Do you have anything to say?”

[P13]
*Of course I do.*

[P14]
But this was all staged. On the way here, Wipeng had explained what was really going on. There was a power struggle among the Jin Family of Taiyuan’s upper ranks, and Jin Wikyung was shielding me from it.

[P15]
In other words, this forced confinement was all for show.

[P16]
*You needed somewhere to train anyway, didn’t you, Young Master? Just endure it for three days.*

[P17]
Remembering Wipeng’s final words, I bowed my head and pretended to repent.

[P18]
“I will gladly accept my punishment.”

[P19]
The advantage of this play was that the lines were short.

[P20]
Jin Wikyung delivered his final line with a sorrowful look in his eyes.

[P21]
“Confine the criminal to the training hall. The release date will be announced later.”

[P22]
The moment he finished speaking, two warriors guarding the entrance to the training hall approached and grabbed me by both arms.

[P23]
The play was over. Time to exit the stage.

[P24]
I stood at the entrance to the training hall.

[P25]
*I’ve had everything you need brought inside. Don’t push yourself too hard, little brother.*

[P26]
Along with Jin Wikyung’s Sound Transmission, I took my first step inside.

[P27]
* * *

[P28]
The training hall was, in a word, a cave. An artificial cave carved into the cliff, at that.

[P29]
It was tall, spacious, and damp.

[P30]
Splash. Splash.

[P31]
How long had I been following the warrior assigned to the training hall? By the time I could no longer tell whether I was wearing leather shoes or wet mops, a massive iron gate appeared before me.

[P32]
*Wow…*

[P33]
My mouth fell open the moment I saw it. The gate filled the passage without leaving a single gap. It looked less like a door than a wall built to prevent anyone from entering or leaving.

[P34]
The warrior guiding me raised his torch and shouted, “Open the gate!”

[P35]
Grrrnnng—

[P36]
The enormous iron gate slowly opened its jaws.

[P37]
It wasn’t some magical command like “Open, Sesame.” One NPC who had been waiting nearby simply grabbed and pulled the protruding gate mechanism.

[P38]
Even so, the sight was overwhelming.

[P39]
And the moment I saw what lay beyond it—

[P40]
“Whoa.”

[P41]
This time, I couldn’t hide the exclamation that escaped me.

[P42]
When I first entered the training hall, I had imagined a damp underground cave, but…

[P43]
“What is all this?”

[P44]
A broad bed with a fur blanket so inviting that merely looking at it lifted my spirits. Instead of a damp, uneven stone floor, a neat gray surface stretched out before me.

[P45]
*Cement… Obviously not. Limestone, maybe?*

[P46]
Aside from the chill in the air—and even with that taken into account—the place was far better than I had imagined.

[P47]
*This is supposed to be punishment?*

[P48]
As I stared around in bewilderment, someone cleared his throat behind me. I turned to find the warrior who had guided me here.

[P49]
“We’ve prepared everything you need. I’ll be going now.”

[P50]
Grrrnnng.

[P51]
As I watched the iron gate slowly close, I suddenly remembered the Sound Transmission I had heard at the entrance.

[P52]
*I’ve had everything you need brought inside. Don’t push yourself too hard, little brother.*

[P53]
Ah. The heart of an NPC who cared about his little brother.

[P54]
This pathetic user was bawling his eyes out.

[P55]
* * *

[P56]
It happened all the time in the real world, too.

[P57]
High-ranking officials who had committed corruption would show up at the prosecutors’ office in wheelchairs or check themselves into private hospital suites to avoid an investigation.

[P58]
My situation was a little different, but I looked much the same. I gazed at the private suite of the training hall with a deeply moved expression.

[P59]
“So this is the life of a gold spoon.”[^1]

[P60]
It wasn’t only the graphics and artificial intelligence that were realistic. The game also carried the social message that, no matter how high you flew or how low you crawled, gold spoons had it best.

[P61]
God, what would I have done if I hadn’t gotten this character? His father was the Family Head, his eldest brother was the Lesser Family Head, and his second brother was a martial arts prodigy. No wonder he could spend all his time loafing around pleasure houses without a care in the world.

[P62]
*Jin Taekyung, you bastard…*

[P63]
Now that I thought about it, wasn’t he actually some great sage who had grasped the ways of the world at a young age?

[P64]
Shuddering at the realistic God-Spoon System, I walked around the training hall, which covered well over three thousand square feet. Before long, I found the “necessities” the warrior had mentioned.

[P65]
*Food first.*

[P66]
The food was stored in two jars. When I looked inside, I found rice balls that gave off a strong medicinal scent.

[P67]
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

[P68]
“Oh, so this is the famous grain-repelling pill?”

[P69]
I had seen them plenty of times in martial arts novels. They were light, compact, easy to carry, and apparently provided nutritional supplementation, too.

[P70]
The other jar was packed full of them too.

[P71]
*I should put these in my inventory for now.*

[P72]
I took hold of both jars and muttered, “Acquire item.”

[P73]
If someone else had seen me, they would have fallen over in shock. The two perfectly ordinary jars had vanished as if they had evaporated.

[P74]
I gazed fondly at the jars stored in my inventory.

[P75]
*That takes care of food.*

[P76]
The second necessity I found was water. Since the training hall was, after all, a cave, a cold underground spring in one corner took care of my drinking water.

[P77]
Then came the third and final necessity.

[P78]
“Hmm.”

[P79]
Several weapons hung in a neat row on a rack. Naturally, the first one I picked up was a sturdy-looking wooden spear.

[P80]
*Appraise item.*

[P81]
Ding.

[P82]
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

[P83]
“Oh.”

[P84]
A training wooden spear made for beginners. It was exactly what I needed right now.

[P85]
If I had just one more thing, everything would be perfect.

[P86]
“Open inventory.”

[P87]
Grinning, I took a martial arts manual titled *Jin Family’s Spear Technique* out of my inventory.

[P88]
Ding.

[P89]
> **System**
>
> - Would you like to learn the Jin Family’s Spear Technique? (3 / 10)

[P90]
“Obviously.”

[P91]
The System was great.

[P92]
Sometimes, it was even adorable.

[P93]
* * *

[P94]
While practicing the Jin Family’s Manoeuvre Technique yesterday, I had learned something for the first time.

[P95]
Ding wasn’t the System’s only notification sound.

[P96]
And I had learned just how much I hated the other one.

[P97]
Beep!

[P98]
> **System**
>
> - The movement failed.
>
> - Successful attempts (2 / 100)

[P99]
The failure message. A System window that appeared without fail whenever I botched a movement.

[P100]
I had lost count of how many times I’d seen it.

[P101]
I stared at the *Training Wooden Spear* in my hand.

[P102]
*I got this all wrong.*

[P103]
Maybe it was because it was made of wood, but the spear was light. Whether I thrust or swung it, it moved as quickly as I wanted.

[P104]
That was the problem.

[P105]
*It’s too light to control.*

[P106]
Its lightness made fine adjustments difficult, so I kept slipping up. There was no way this filthy picky System would overlook minor errors.

[P107]
Beep.

[P108]
> **System**
>
> - The movement failed.
>
> - Successful attempts (5 / 100)

[P109]
“Ah, fuck.”

[P110]
In the end, I tossed the *Training Wooden Spear* aside and pulled the *Sharp Spear* from my inventory. Its length and the thickness of its shaft were roughly the same as the spear I had used in the real world.

[P111]
So why hadn’t I taken it out from the start?

[P112]
“It’s fucking heavy. Seriously.”

[P113]
Since it was made entirely of solid steel, its weight was no joke. By feel alone, the monster had to weigh close to fifty kilograms.

[P114]
My Stamina wouldn’t last if I swung something like this for hours.

[P115]
My current realm was Second Rate. Even with the System’s help, swinging around more than half a sack of rice as if it were a pinwheel was impossible.

[P116]
*It’s not like I suddenly have tiger power or something.*

[P117]
That was when it hit me.

[P118]
“…Huh?”

[P119]
What had I just said?

[P120]
The strength of a tiger?

[P121]
“I do have it.”

[P122]
This was a game. It had a System and stats.

[P123]
And I had internal energy.

[P124]
Ten years of internal energy that I could draw out through a cultivation technique!

[P125]
It was embarrassing that I had forgotten, even for a moment.

[P126]
“It’s not like I’ve ever used anything like that before…”

[P127]
They say you only know what something is like once you’ve experienced it. Was it any wonder an F-rank Hunter was F-rank? With barely any mana to speak of, I made do with my bare body. Even among Hunters, I was treated like a half-baked amateur.

[P128]
*Still, that solves one problem.*

[P129]
I let out a dumbfounded laugh, then picked up the spear. Slowly and carefully, I began drawing out my internal energy.

[P130]
The formula of the Jin Family’s Cultivation Technique, imprinted in my mind by the System, rewound rapidly through my thoughts, guiding my internal energy along its prescribed path.

[P131]
A prickling sensation ran through me.

[P132]
The response was immediate.

[P133]
The ten years of internal energy coiled in my dantian spread throughout my body. Because this was a game and I was a martial artist, I could feel it spreading through every part of me.

[P134]
*This is…*

[P135]
Power surged through my entire body. My vastly heightened physical abilities and senses once again brought exhilaration to someone who had spent his life as an F-rank Hunter.

[P136]
*How can a person change this much?*

[P137]
I gripped the spear and began practicing the *Jin Family’s Spear Technique*. The fifty-kilogram iron spear no longer felt heavy. It thrust and slashed through the air along the paths I wanted it to follow.

[P138]
Before long—

[P139]
Ding.

[P140]
> **System**
>
> - Successful attempts (6 / 100)

[P141]
The notification I had been waiting for began to ring.

[P142]
* * *

[P143]
Jin Wikyung spoke with a worried expression.

[P144]
“He’s doing well, right?”

[P145]
“He should be, if he has any sense of shame.”

[P146]
“He still hasn’t fully recovered… He’ll be all right, won’t he?”

[P147]
“Anyone who didn’t know better would think the Third Young Master was on death’s door. At that point, even spit would cure him.”

[P148]
“No. You only say that because you don’t know how frail the youngest has been since childhood.”

[P149]
Wipeng answered with an incredulous look.

[P150]
“The elixirs and tonics that have gone into the Third Young Master alone would be enough to fill an entire room. And have you already forgotten about the hundred-year snow ginseng theft last year?”

[P151]
“Ahem. That was…”

[P152]
“At the time, the Medicine King Hall Master was so furious that he ran around shouting that he was going to cut open the Third Young Master’s stomach. To be honest, even while I was stopping him, I found myself thinking that cutting him open would qualify as self-defense.”

[P153]
Jin Wikyung subtly averted his gaze.

[P154]
The matter had ultimately been settled by compensating the Medicine King Hall out of Jin Wikyung’s personal fortune, but the Hall Master’s fury at the time had been extraordinary.

[P155]
“He swallowed that much elixir. Whatever else may be true, he probably won’t suffer from minor ailments until the day he dies.”

[P156]
“It still isn’t enough. Can’t you tell just by looking at him? Every time I see the youngest, I feel sorry for him. He looks like a skeleton with a few scraps of flesh stuck to it. Every morning he’s so feeble and drained of strength.”

[P157]
“Drained of strength?”

[P158]
Wipeng suddenly remembered a rumor he had heard in the past.

[P159]
Among the courtesans of Taiyuan’s red-light district, Jin Taekyung was supposedly known as the Night King.

[P160]
*Just how impressive is he?*

[P161]
The medicine must have worked properly in at least one respect. Without realizing it, Wipeng raised his forearm and began imagining the size.

[P162]
“What are you doing?”

[P163]
“Ah, nothing.”

[P164]
Jin Wikyung sighed as he looked at the mountain of documents piled before him.

[P165]
“Between the youngest and everything happening inside and outside the family, there’s no end to my worries. Especially… I don’t like that ‘they’ have made contact.”

[P166]
“You mean the Mount Heng Sword Sect.”

[P167]
Mount Heng Sword Sect. The weight of that name was anything but light.

[P168]
Since an undefeated wandering martial artist first hung its signboard decades ago, the sect had grown at a frightening pace. Now, it had become powerful enough to threaten the Jin Family of Taiyuan’s position.

[P169]
“What could their intentions be?”

[P170]
“I’ve sent my subordinates to investigate.”

[P171]
Jin Wikyung fidgeted with the letter from the Mount Heng Sword Sect.

[P172]
Why were they coming? For what purpose?

[P173]
One question led to another, until he arrived at a single conclusion.

[P174]
“Notify every branch in Shanxi. Whatever the Mount Heng Sword Sect’s purpose may be, tell them to make every possible preparation.”

[P175]
This was Murim.

[P176]
Only those who were prepared would survive to see tomorrow.

[P177]
[^1]: In Korean, “gold spoon” is shorthand for someone born into wealth; “God-Spoon” is a pun that escalates the expression.
```

## Deterministic QA

```json
{
  "chapter": 10,
  "errors": [],
  "metrics": {
    "length_ratio": 2.447,
    "source_characters": 5697,
    "source_paragraphs": 169,
    "translation_characters": 13942,
    "translation_paragraphs": 177
  },
  "passed": true,
  "version": 1,
  "warnings": [
    {
      "code": "terminology",
      "details": {
        "korean": "진가심법",
        "preferred": "Jin Family's Cultivation Technique"
      },
      "message": "matched preferred term is absent"
    },
    {
      "code": "terminology",
      "details": {
        "korean": "진가보법",
        "preferred": "Jin Family's Manoeuvre Technique"
      },
      "message": "matched preferred term is absent"
    },
    {
      "code": "terminology",
      "details": {
        "korean": "진가창법",
        "preferred": "Jin Family's Spear Technique"
      },
      "message": "matched preferred term is absent"
    },
    {
      "code": "terminology",
      "details": {
        "korean": "보상",
        "preferred": "Reward"
      },
      "message": "matched preferred term is absent"
    },
    {
      "code": "terminology",
      "details": {
        "korean": "습득",
        "preferred": "Acquired"
      },
      "message": "matched preferred term is absent"
    },
    {
      "code": "terminology",
      "details": {
        "korean": "대사",
        "preferred": "Master for a senior Buddhist monk"
      },
      "message": "matched preferred term is absent"
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

# Master Editorial Brief

You are the final English-language editor of an existing Korean-to-English novel translation.

The Korean source is the authority for meaning. The existing English is the baseline you are editing, not a draft to discard. Your task is to make the chapter read like professionally written native English commercial fiction while preserving the author's exact story, characterization, humor, register, pacing, ambiguity, and cultural texture.

## Editorial authority

You may freely recast sentences and paragraphs when the English is stiff, literal, repetitive for accidental reasons, awkwardly collocated, over-explained, or syntactically shaped by Korean. You may tighten dialogue, improve rhythm, repair transitions, and make action easier to follow. A technically correct sentence may still need rewriting if a fluent English novelist would not naturally phrase it that way.

Do not change text merely to make it different. If the baseline is already strong, leave it alone.

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

Do not add jokes, metaphors, explanations, emotional conclusions, or colorful details that are absent from the Korean. Do not replace a specific source image with a generic equivalent merely because the generic version is smoother.

When natural English and literal form conflict, preserve the source meaning and pragmatic effect while changing the English form as much as necessary.

## Relationship to project files

`RULES.md` is binding. `POLISH.md` describes known translation-English failure modes and should guide the edit. Exact glossary matches are binding unless the packet explicitly marks them otherwise. Character/continuity material is context only and must never override the chapter's Korean source.

## Output

Return only the complete edited English Markdown chapter. Preserve the required chapter heading and project Markdown conventions. Do not provide commentary, a change log, explanations, or a Markdown code fence.
