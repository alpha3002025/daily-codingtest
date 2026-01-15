# 광물 캐기
지금까지 풀이법을 이해했던 문제 들 중 가장 어려웠던 문제였다.<br/>
<br/>

**데이터 변환 (1) : cost 높은 순의 처리용도 데이터 생성**<br/>
먼저 5개 단위로 cost, sublist(5개의 광물) 를 다음의 형태로 저장한다. 
```python
[(cost1, sublist1), (cost2, sublist2), ...]
```
<br/>

이때 cost 는 돌 곡괭이를 사용했을 때의 피로도를 기준으로 계산한다. 최악의 경우를 가정하는 것이라고 생각할수도 있고, 가장 '기저'(Base) 가 되는 단위가 이번 문제에서는 '돌곡괭이'가 되기 때문에, 기본단위인 돌곡괭이를 기준으로 cost 를 산정했다.<br/>
<br/>

이렇게 저장한 데이터는 cost 를 기준으로 다음과 같이 역순 정렬해서 cost가 높은순으로 정렬한다.
```python
# 피로도가 높은(캐기 힘든) 순서대로 정렬
chunks.sort(key=lambda x: x[0], reverse=True)
```
<br/>
<br/>


**데이터 처리 - 곡괭이 작업**<br/>
데이터를 처리하는 로직은 '시뮬레이션' 유형 처럼 처리하게 된다. 로직이 단순하지만, if \~ elif \~ elif \~ else 로 처리하는 부분에서 원하는 우선순위의 조건문을 앞에 두어서 우선처리 순서를 부여했다는 점에 주목하자. 이 부분은 문제가 뭔지 알고 봐야 그 의미구나 하고 알게되는 듯 하다.<br/>

```python
answer = 0
# 좋은 곡괭이부터 소진
# picks[0]: dia, picks[1]: iron, picks[2]: stone
for _, chunk in chunks:
    ## (1) : start
    if picks[0] > 0:
        pick_type = 0
        picks[0] -= 1
    elif picks[1] > 0:
        pick_type = 1
        picks[1] -= 1
    elif picks[2] > 0:
        pick_type = 2
        picks[2] -= 1
    else:
        break
    ## (1) : end
    
    ## (2) : start
    # 선택된 곡괭이로 피로도 계산
    for m in chunk:
        if pick_type == 0: # Dia pick
            answer += 1
        elif pick_type == 1: # Iron pick
            if m == "diamond": answer += 5
            else: answer += 1
        else: # Stone pick
            if m == "diamond": answer += 25
            elif m == "iron": answer += 5
            else: answer += 1
    ## (2) : end
```
<br/>
<br/>

(1)
- 곡괭이를 다이아 ➝ 철 ➝ 돌 순서로 소진하도록 if 문을 구성했고, 선택에 따라 곡괭이 수 차감 (`pick[0,1,2] -= 1`) + 현재 선택한 곡괭이 유형 업데이트 (`pick_type = 0,1,2`)를 한다.

(2) 현재 선택된 곡괭이(`pick_type`)으로 광물 5개(`chunk`)를 캔다.
- 다이아곡괭이: answer += 1, 철곡괭이: answer += 5, 돌곡괭이: answer += 25

<br/>
<br/>

## 문제 설명
다이아몬드, 철, 돌 곡괭이가 0 ~ 5개씩 주어집니다.
곡괭이로 광물을 캘 때 피로도가 소모됩니다.
- 다이아 곡괭이: 다이아(1), 철(1), 돌(1)
- 철 곡괭이: 다이아(5), 철(1), 돌(1)
- 돌 곡괭이: 다이아(25), 철(5), 돌(1)
각 곡괭이는 5개의 광물을 캐면 부러집니다. 광물은 주어진 순서대로 캐야 합니다.
최소 피로도를 구하는 문제입니다. 곡괭이가 없거나 광물이 없으면 종료합니다.

## 풀이 개념
**그리디 알고리즘**과 **정렬**을 사용합니다.
광물을 순서대로 캐야 하지만, **어느 곡괭이를 사용할지는 선택**할 수 있습니다.
한 번 곡괭이를 선택하면 5개를 연속으로 캐야 하므로, 광물들을 **5개씩 묶어서(Chunk)** 생각합니다.

1. **캘 수 있는 광물 제한**: 곡괭이 개수의 총합에 5를 곱한 만큼만 광물을 캘 수 있습니다. 만약 광물이 더 많다면, 뒤쪽 광물은 어차피 못 캐므로 잘라냅니다.
2. **그룹화 및 가중치 계산**: 남은 광물들을 5개씩 묶고, 각 묶음의 중요도(피로도 가중치)를 계산합니다.
   - 이때 "돌 곡괭이"로 캘 때의 피로도를 기준으로 계산하면 해당 묶음이 얼마나 처리가 어려운지 알 수 있습니다.
   - (다이아 25, 철 5, 돌 1 가중치 적용).
3. **정렬**: 피로도가 높은(어려운) 묶음부터 처리하기 위해 내림차순 정렬합니다.
4. **곡괭이 할당**: 가장 어려운 묶음에는 가장 좋은 곡괭이(다이아 > 철 > 돌)를 할당하여 피로도를 최소화합니다.

## 코드 (Python)

```python
def solution(picks, minerals):
    # 캘 수 있는 최대 광물 수
    total_picks = sum(picks)
    if total_picks == 0:
        return 0
    
    # 곡괭이로 캘 수 있는 만큼만 광물 자르기
    minerals = minerals[:total_picks * 5]
    
    # 5개씩 묶어서 (돌 곡괭이 기준 피로도, 묶음 내용) 저장
    chunks = []
    
    for i in range(0, len(minerals), 5):
        chunk = minerals[i:i+5]
        cost = 0
        for m in chunk:
            if m == "diamond": cost += 25
            elif m == "iron": cost += 5
            else: cost += 1
        chunks.append((cost, chunk))
    
    # 피로도가 높은(캐기 힘든) 순서대로 정렬
    chunks.sort(key=lambda x: x[0], reverse=True)
    
    answer = 0
    # 좋은 곡괭이부터 소진
    # picks[0]: dia, picks[1]: iron, picks[2]: stone
    for _, chunk in chunks:
        if picks[0] > 0:
            pick_type = 0
            picks[0] -= 1
        elif picks[1] > 0:
            pick_type = 1
            picks[1] -= 1
        elif picks[2] > 0:
            pick_type = 2
            picks[2] -= 1
        else:
            break
            
        # 선택된 곡괭이로 피로도 계산
        for m in chunk:
            if pick_type == 0: # Dia pick
                answer += 1
            elif pick_type == 1: # Iron pick
                if m == "diamond": answer += 5
                else: answer += 1
            else: # Stone pick
                if m == "diamond": answer += 25
                elif m == "iron": answer += 5
                else: answer += 1
                
    return answer
```
<br/>
<br/>


## 코드 상세 설명
### 가중치 설정
```python
for i in range(0, len(minerals), 5):
    chunk = minerals[i:i+5]
    cost = 0
    for m in chunk:
        if m == "diamond": cost += 25
        elif m == "iron": cost += 5
        else: cost += 1
    chunks.append((cost, chunk))
```
<br/>

**설명**<br/>
1. **5개씩 묶기**: `range(0, len(minerals), 5)`를 사용하여 광물 리스트를 5개 단위의 묶음(`chunk`)으로 나눕니다.
2. **비용(Cost) 계산**: 각 묶음별로 `cost`를 계산하는데, 이때 기준은 **"돌 곡괭이"를 사용했을 때의 피로도**입니다.
    - 다이아몬드: 25점
    - 철: 5점
    - 돌: 1점
3. **목적**: 이렇게 계산된 `cost`는 해당 구간을 처리하기가 얼마나 힘든지를 나타내는 일종의 **난이도 점수(가중치)**가 됩니다. 이후 이 점수가 높은 구간부터 우선적으로 다이아몬드/철 곡괭이를 할당하게 됩니다.

<br/>
<br/>


## Q&A
### Q1 : 그런데, 철 곡괭이, 다이아 곡괭이는 어디에 저장하고 있나요?
A : <br/>
철 곡괭이나 다이아 곡괭이의 가중치는 **별도로 저장하지 않습니다.**

이 문제의 핵심(Greedy 전략)은 다음과 같습니다:

1.  **가중치는 오직 "돌 곡괭이" 기준으로만 계산**합니다. (`chunks` 리스트에 저장된 `cost`)
    *   이유: 돌 곡괭이로 캘 때의 피로도가 **그 광물 묶음의 "난이도"를 가장 잘 대변**하기 때문입니다. (다이아가 많을수록 값이 폭증함)
2.  **정렬**: 이 난이도(`cost`)가 높은 순서대로 리스트를 정렬합니다.
3.  **할당**: 정렬된 순서대로, **내가 가진 가장 좋은 곡괭이부터 사용**합니다.
    *   난이도가 제일 높은 구간(다이아가 많은 구간) -> 다이아 곡괭이 사용 (효율 최상)
    *   그 다음 힘든 구간 -> 남은 것 중 제일 좋은 곡괭이 (철, 혹은 돌) 사용

즉, 철/다이아 곡괭이일 때의 피로도를 미리 계산해서 비교하는 것이 아니라, **광물 묶음 자체의 난이도를 평가해 놓고, 가장 어려운 놈부터 좋은 무기로 처리**하는 방식입니다.

코드의 뒷부분(아래쪽 `선택된 곡괭이로 피로도 계산` 주석 부분)에서, 실제로 곡괭이를 선택한 후(`pick_type`)에야 비로소 해당 곡괭이에 맞는 실제 피로도(`answer += ...`)를 계산하여 더하게 됩니다.

<br/>
<br/>


### Q2 : `minerals = minerals[:total_picks * 5]` 의 의미는 무엇인가요?
A : **보유한 곡괭이로 캘 수 있는 최대 광물 수만큼만 잘라서 남기는** 작업을 수행합니다.

**이유 및 의미**
1.  **자원 한정**: 곡괭이 하나당 5개의 광물을 캘 수 있습니다. 만약 곡괭이가 3개라면 총 15개의 광물만 캘 수 있습니다.
2.  **쓸모없는 광물 제거**: 만약 광물이 100개 있는데 곡괭이가 3개(15개 채굴 가능)뿐이라면, 16번째 이후의 광물들은 어차피 캘 수 없으므로 **피로도 계산이나 우선순위 정렬에 영향을 줘서는 안 됩니다.**
3.  **최적화 및 오류 방지**:
    -   캘 수 없는 뒤쪽 광물들이 다이아몬드라고 해서, 앞쪽의 돌 광물들을 아끼기 위해 다이아 곡괭이를 아낄 필요가 없기 때문입니다.
    -   따라서, **"내가 캘 수 있는 범위 내에서"** 가장 피로도가 높은 구간을 찾아야 하므로 범위를 미리 제한하는 것입니다.


