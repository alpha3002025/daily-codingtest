# 양궁대회

## 문제 설명
라이언(전 우승자)과 어피치(도전자)가 양궁 시합을 합니다.
어피치가 먼저 `n`발을 쏘고 결과가 `info` 배열(10점~0점 과녁 맞힌 개수)로 주어집니다.
라이언이 `n`발을 쏘아 어피치를 가장 큰 점수 차이로 이기는 경우를 구합니다.
1. `k`점에 대해 더 많이 맞힌 사람이 `k`점을 가져갑니다. (동점이면 어피치가 가져감. 둘 다 0발이면 아무도 못 가져감).
2. 점수 차이가 최대가 되는 라이언의 과녁 정보를 반환합니다.
3. 최대 점수 차이가 여러 개라면, 가장 낮은 점수를 더 많이 맞힌 경우를 반환합니다.
4. 이길 수 없으면 `[-1]`을 반환합니다.

## 풀이 개념
**BFS/DFS** 또는 **중복 조합(Backtracking)**을 이용한 완전 탐색 문제입니다.
과녁의 종류가 11개(0~10점)로 적고 화살 개수 `n`도 작기 때문에 모든 경우를 따져볼 수 있습니다. 하지만 단순히 화살을 쏘는 모든 경우(하키 스틱 패턴 등)보다는 **"각 점수를 얻느냐 마느냐"**의 관점에서 접근하는 것이 효율적입니다.

**전략**:
1. 각 점수(10점~0점)에 대해 라이언의 선택지는 두 가지입니다.
   - **이기기**: 어피치가 쏜 개수 + 1발을 쏘아 점수를 획득한다.
   - **포기하기**: 0발을 쏘고 점수를 포기한다 (아낀 화살은 다른데 투자).
2. DFS로 10점부터 0점까지 순회하며 이 두 가지 경우를 탐색합니다.
3. 화살을 다 썼거나 0점까지 탐색했을 때 점수 차이를 계산합니다.
   - 남은 화살은 0점에 몰아서 쏩니다 (낮은 점수 우선 조건 때문에 0점에 두는 게 유리).
4. 최대 점수 차이를 갱신합니다. 차이가 같을 경우 "낮은 점수가 더 많은지" 비교하여 갱신합니다.

## 코드 (Python)

```python
def solution(n, info):
    max_diff = 0
    answer = []
    
    def dfs(idx, arrows, remain):
        nonlocal max_diff, answer
        
        if idx == 11 or remain == 0:
            # 남은 화살은 0점(idx 10)에 몰아줌
            if remain > 0:
                arrows[10] += remain
                
            # 점수 계산
            apeach_score = 0
            ryan_score = 0
            for i in range(11):
                if info[i] == 0 and arrows[i] == 0:
                    continue
                if info[i] >= arrows[i]:
                    apeach_score += (10 - i)
                else:
                    ryan_score += (10 - i)
            
            diff = ryan_score - apeach_score
            
            if diff > 0:
                if diff > max_diff:
                    max_diff = diff
                    answer = list(arrows)
                elif diff == max_diff:
                    # 낮은 점수를 더 많이 맞힌 경우 선택 (리스트 역순 비교시 더 큰 것이 답)
                    for i in range(10, -1, -1):
                        if arrows[i] > answer[i]:
                            answer = list(arrows)
                            break
                        elif arrows[i] < answer[i]:
                            break
            
            # 화살 회수 (Backtracking) - 0점 몰아준거 취소
            if remain > 0:
                arrows[10] -= remain
            return

        # 1. 현재 점수(10-idx)를 먹는 경우 (어피치보다 1발 더 쏨)
        needed = info[idx] + 1
        if remain >= needed:
            arrows[idx] = needed
            dfs(idx + 1, arrows, remain - needed)
            arrows[idx] = 0 # 복구
            
        # 2. 현재 점수를 포기하는 경우 (0발 쏨)
        dfs(idx + 1, arrows, remain)

    dfs(0, [0]*11, n)
    
    if max_diff == 0:
        return [-1]
        
    return answer
```
<br/>
<br/>


### 코드 상세 설명 (Top Down DFS 풀이)

**1. 재귀 종료 조건(Base Case)**
```python
if idx == 11 or remain == 0:
    # 남은 화살은 0점(idx 10)에 몰아줌
    if remain > 0:
        arrows[10] += remain
```
-   `idx == 11`: 10점(idx 0)부터 0점(idx 10)까지 모든 점수 구간을 다 훑었을 때 탐색을 종료합니다.
-   `remain == 0`: 쏠 수 있는 화살을 모두 소진한 경우 탐색을 종료합니다.
-   재귀가 끝나기 전, 만약 화살이 남았다면? **"가장 낮은 점수를 더 많이 맞힌 경우"**를 우선하는 문제 조건 때문에, 남은 화살은 모두 **0점(인덱스 10)**에 몰아주는 것이 유리합니다.

**2. 점수 계산**
```python
# 점수 계산
apeach_score = 0
ryan_score = 0
for i in range(11):
    if info[i] == 0 and arrows[i] == 0: # 둘 다 0발이면 점수 변화 없음
        continue
    if info[i] >= arrows[i]: # 어피치가 같거나 더 많이 쏘면 어피치 득점
        apeach_score += (10 - i)
    else: # 라이언이 더 많이 쏘면 라이언 득점
        ryan_score += (10 - i)
```
-   현재까지 `arrows`에 기록된 라이언의 화살 분포를 바탕으로 최종 점수를 계산합니다.
-   양궁 대회 룰에 따라 동점(`info[i] >= arrows[i]`)인 경우에도 어피치가 점수를 가져감을 주의해야 합니다.

**3. 최대 점수 차이 갱신**
```python
diff = ryan_score - apeach_score

if diff > 0: # 라이언이 이긴 경우에만
    if diff > max_diff:
        # 1. 점수 차가 기존보다 크면 무조건 갱신
        max_diff = diff
        answer = list(arrows)
    elif diff == max_diff:
        # 2. 점수 차가 같다면 "낮은 점수를 더 많이 맞힌" 경우 선택
        # 뒤(0점, idx 10)에서부터 비교하여 라이언이 더 많이 쏜 경우가 정답
        for i in range(10, -1, -1):
            if arrows[i] > answer[i]:
                answer = list(arrows) # 갱신
                break
            elif arrows[i] < answer[i]:
                break # 기존 답 유지
```
-   `diff > max_diff`: 더 큰 점수 차로 이길 수 있는 방법을 찾았다면, `answer`를 즉시 교체합니다.
-   `diff == max_diff`: 점수 차가 같은 또 다른 방법이 발견된 경우, 문제에서 요구한 **"낮은 점수를 더 많이 맞힌 경우"**를 찾기 위해 배열의 뒤쪽(0점)부터 비교합니다.

**4. 화살 회수 (Backtracking)**
```python
# 화살 회수 (Backtracking) - 0점 몰아준거 취소
if remain > 0:
    arrows[10] -= remain
return
```
-   **중요**: Base Case 진입 시 `arrows` 배열을 직접 수정(남은 화살 몰아주기)했으므로, 재귀를 빠져나가기 전에 **원래 상태로 되돌려놓아야 합니다.** (Backtracking의 핵심)

**5. 재귀 호출 (투 트랙 전략)**
```python
# 1. 현재 점수(10-idx)를 먹는 경우 (어피치보다 1발 더 쏨)
needed = info[idx] + 1
if remain >= needed:
    arrows[idx] = needed
    dfs(idx + 1, arrows, remain - needed)
    arrows[idx] = 0 # 복구 (Backtracking)
    
# 2. 현재 점수를 포기하는 경우 (0발 쏨)
dfs(idx + 1, arrows, remain)
```
-   **Case 1 (승리)**: 현재 점수를 얻기 위해 어피치보다 딱 1발 더 쏩니다 (`info[idx] + 1`). 단, 남은 화살이 충분할 때만 가능합니다.
-   **Case 2 (포기)**: 현재 점수를 포기하고 화살을 아껴 다음 점수(더 낮은 점수) 공략에 투자합니다.
-   이 두 가지 경우를 모두 시도함으로써 가능한 모든 승리 전략을 탐색합니다.

<br/>
<br/>

## 옛날 풀이 (python)
```python
def solution(n, info):
    apeach_score = sum(10-i for i in range(11) if info[i] != 0)
    weights = [-1] + [x+1 for x in info] ## 어피치가 맞힌 화살수 + 1 (라이언이 해당라운드에서 이기기 위해 맞춰야 할 화살 수)
                            ## 득점하기 위해 어피치의 화살수 + 1 값이 되어야 하므로 cost 가 된다.
    
    ## 어피치보다 높은 점수를 받아야 하는 요소 : 2*(10-i) 점 획득
    ## 어피치가 득점을 하지 못한 과녁 : 10-i
    values = [-1] + [2*(10-i) if info[i] != 0 else (10-i) for i in range(11)]
    
    dp = [[0] * (n+1) for _ in range(12)]
    
    for i in range(1, 12): ## info 의 길이 1 ~ 12
        for w in range(1, n+1): ## 화살 개수(1<=n<=10)
            if weights[i] > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(
                    dp[i-1][w - weights[i]] + values[i],
                    dp[i-1][w]
                )
    
    last_score = dp[-1][-1] - apeach_score
    if last_score <= 0:
        return [-1]
    
    answer = [0] * 11
    w = n 
    for i in range(11, 0, -1):
        if dp[i][w] == dp[i-1][w-weights[i]] + values[i]:
            answer[i-1] = weights[i]
            w = w - weights[i]
            
    answer[-1] += (n - sum(answer))
    return answer
```

<br/>
<br/>


### 코드 상세 설명 (Knapsack DP 풀이)

이 풀이는 문제를 **배낭 채우기 문제(0/1 Knapsack Problem)**로 치환하여 해결한 방식입니다.

**문제 치환**
- **과녁 점수 매핑 (`10 - i`)**: 
    - `i`는 배열의 **인덱스**입니다. (0부터 10까지)
    - `10 - i`는 해당 인덱스가 의미하는 **과녁 점수**입니다.
        - `i=0` -> 10점
        - `i=1` -> 9점
        - ...
        - `i=10` -> 0점
- **가방 용량 (Capacity)**: 사용 가능한 화살의 수 `n`
- **아이템 (Item)**: 각 점수별 과녁 (0점~10점)
- **무게 (Weight)**: 해당 과녁 점수를 얻기 위해 필요한 화살 수 (`weights[i]`)
    - 어피치가 3발 쐈다면, 라이언은 4발 필요 (`info[i] + 1`)
- **가치 (Value)**: 화살을 투자했을 때 얻을 수 있는 점수의 이득 (`values[i]`)
    - **핵심**: 만약 `10점` 과녁을 라이언이 이긴다면?
        - 라이언은 10점 획득 (+10)
        - 어피치는 10점 상실 (-10)
        - **Value = 20점** (10 - (-10))
    - 단, 어피치가 0발 쐈던 과녁이라면, 어피치 점수 변화는 없으므로 **Value = 10점**



### 코드 라인별 설명

**(1) 가치(Value)와 무게(Weight) 설정**
```python
## 어피치보다 높은 점수를 받아야 하는 요소 : 2*(10-i) 점 획득
## 어피치가 득점을 하지 못한 과녁 : 10-i
values = [-1] + [2*(10-i) if info[i] != 0 else (10-i) for i in range(11)]
```
-   **Knapsack 문제의 '가치' 정의**: 라이언이 이 과녁을 차지할 때 얻는 **상대적 점수 이득**입니다.
    -   `info[i] != 0` (어피치도 맞힌 과녁): 라이언이 뺏으면 `(라이언 +k)` + `(어피치 -k)` 효과가 나므로 **2배의 이득(2k)**이 발생합니다.
    -   `info[i] == 0` (어피치가 못 맞힌 과녁): 라이언이 가져가면 단순히 `(라이언 +k)` 효과이므로 **1배의 이득(k)**만 발생합니다.


**변수 설정**
- `weights`: 각 점수(`i`)를 **'따기 위해 라이언이 써야 하는'** 화살 개수입니다.
    - 즉, **어피치가 쏜 화살 수 + 1**입니다. (`info[i] + 1`)
    - 만약 어피치보다 더 많이 쏘지 못한다면 점수를 가져올 수 없으므로, 이 값 자체가 해당 점수의 **비용(Cost)**이 됩니다.
- `values`: 각 점수(`i`)를 땄을 때의 가치 리스트
- `dp[i][w]`: `i`번째 과녁까지 고려하고, 화살 `w`개를 썼을 때 얻을 수 있는 **최대 점수 이득**

<br/>
<br/>

**(2) DP 테이블 초기화**
```python
dp = [[0] * (n+1) for _ in range(12)]
```
-   `dp[i][w]`: `i`번째 과녁까지 고려했을 때, 화살 `w`개를 사용하여 얻을 수 있는 **최대 점수 차이**를 저장합니다.
-   행(Row)은 0~11까지(1-based indexing을 위한 패딩 포함), 열(Column)은 화살 개수 0~`n`개를 의미합니다.

**(3) 점화식 (Knapsack Logic)**
```python
for i in range(1, 12): ## info 의 길이 1 ~ 12
    for w in range(1, n+1): ## 화살 개수(1<=n<=10)
        if weights[i] > w:
            dp[i][w] = dp[i-1][w]
        else:
            dp[i][w] = max(
                dp[i-1][w - weights[i]] + values[i], # 따는 경우
                dp[i-1][w]                           # 안 따는 경우
            )
```
-   **`weights[i] > w`**: 현재 과녁을 맞히기에 화살이 부족하면, 이전 상태(`dp[i-1][w]`)를 그대로 가져옵니다.
-   **`else`**:
    -   1. `dp[i-1][w - weights[i]] + values[i]`: 현재 과녁을 맞히는 경우 (필요한 화살만큼 빼고 가치 추가)
    -   2. `dp[i-1][w]`: 현재 과녁을 포기하는 경우
    -   두 경우 중 더 큰 이득을 취합니다.


`dp[i-1][w - weights[i]] + values[i]` : 
- `w - weights[i]` 
  - 현재 (i번째) 과녁 점수를 얻으려면 `weights[i]` 만큼을 반드시 소비해야 하는데, 
  - 이런 이유로 남은 화살(전체w)에서 지금 사용할 화살만큼을 미리 뺀것

- `dp[i-1][w - weights[i]]` : i 번째 화살을 쓰기 전(i-1)의 상태 (화살 수는 한정적이기에 `weights[i]` 를 차감)
  - `i-1` 번째 과녁까지만 고려했을 때, `w - weights[i]` 개의 화살로 얻을수 있었던 최대 점수 이득

- `+ values[i]`
- 여기에 **"지금 과녁을 맞혀서 얻는 점수 이득"**을 더합니다.
- 결과적으로 **"이전까지의 최적 점수 + 이번 과녁의 점수"**가 됩니다.

<br/>
<br/>


**정답 추적 (Backtracking)**
- DP 테이블이 채워진 후, 역추적을 통해 실제로 어떤 과녁을 선택했는지 찾아냅니다.
- `dp[i][w]` 값이 **"따는 경우"**(`dp[i-1][w-weights[i]] + values[i]`)와 같다면, 해당 과녁을 맞힌 것으로 간주하여 `answer`에 기록하고 남은 화살 `w`를 차감합니다.

<br/>
<br/>

**(4) 최종 결과 확인**
```python
last_score = dp[-1][-1] - apeach_score
if last_score <= 0:
    return [-1]
```
-   `dp[-1][-1]`: 라이언이 얻을 수 있는 **최대 점수 이득**입니다.
-   여기서 초기 `apeach_score`(어피치가 혼자 다 쐈을 때의 점수)를 뺐을 때 `0` 이하라면, 라이언이 아무리 잘 쏘아도 어피치를 이길 수 없거나 비기는 경우이므로 `-1`을 반환합니다.

**(5) 역추적 (Backtracking)**
```python
answer = [0] * 11
w = n 
for i in range(11, 0, -1):
    if dp[i][w] == dp[i-1][w-weights[i]] + values[i]:
        answer[i-1] = weights[i]
        w = w - weights[i]
```
-   DP 테이블을 역순(과녁 0점 쪽 `i=11`부터 거꾸로)으로 탐색하며, **어떤 과녁을 선택했는지** 확인합니다.
-   만약 현재 `dp[i][w]` 값이 '선택했을 때의 값'과 일치한다면, 해당 과녁을 정답 배열에 기록하고 소모한 화살(`weights[i]`)만큼 `w`를 줄입니다.

**(6) 남은 화살 처리**
```python
answer[-1] += (n - sum(answer))
return answer
```
- 최적 해를 구성하고도 화살이 남을 수 있습니다. (`n - sum(answer)`)
- 이 남은 화살은 점수에 영향을 주지 않는 잉여 화살이므로, 문제 조건(가장 낮은 점수를 더 많이 맞힌 경우)에 따라 **가장 낮은 점수(0점, 맨 마지막 인덱스)**에 모두 더해줍니다.
- 모든 추적이 끝난 후, 아직 화살이 남았다면 (`n - sum(answer)`), 이는 점수 이득엔 기여하지 못하는 잉여 화살이므로 0점(인덱스 10) 과녁에 몰아줍니다. (낮은 점수 우선 조건 충족에도 유리)


<br/>
<br/>



## Q&A

### Q1. 점수 차이가 같을 때, 왜 `range(10, -1, -1)` 처럼 역순으로 순회하며 비교하나요?

문제의 조건 중 **"가장 큰 점수 차이로 우승할 수 있는 방법이 여러 가지 일 경우, 가장 낮은 점수를 더 많이 맞힌 경우를 return 한다"**는 규칙 때문입니다.

`arrows` 리스트는 인덱스 0부터 10점, 9점, ..., 0점 순서로 저장되어 있습니다.
- 인덱스 0: 10점
- ...
- 인덱스 10: 0점 (가장 낮은 점수)

따라서 **낮은 점수(인덱스 10, 9, 8...)부터 먼저 확인**하여, 해당 점수의 화살 수가 더 많은 쪽을 선택해야 하기 때문에 `range(10, -1, -1)` (10부터 0까지 역순)으로 순회하며 비교하는 것입니다.

이 과정에서 뒤쪽(낮은 점수)에서 차이가 발견되면 즉시 그 쪽을 정답으로 갱신(`answer = list(arrows)`)하고 반복을 멈춥니다(`break`). 앞쪽(높은 점수) 차이는 볼 필요가 없기 때문입니다.



### Q2. `idx == 11` 또는 `remain == 0`일 때, 남은 화살을 0점에 몰아주는 이유는 무엇인가요?

이 부분은 DFS 탐색이 종료되었을 때, **아직 쏘지 않은 남은 화살들을 처리**하는 로직입니다.

1.  **화살 소진 규칙**: 라이언은 대회가 끝날 때 반드시 가져온 **N개의 화살을 모두 쏴야 합니다.**
2.  **잔여 처리**: DFS 탐색 과정에서 점수를 따기 위해 필요한 만큼만 쏘고 넘어가다 보면, `idx == 11` (모든 점수 구간 탐색 종료)이 되었는데도 화살(`remain`)이 남아있을 수 있습니다.
3.  **0점에 몰아주기**: 남은 화살은 점수에 영향을 주지 않는 **0점 과녁(인덱스 10)**에 모두 쏘는 것으로 처리합니다.
    -   어차피 0점은 몇 발을 쏘든 점수는 0점이므로 승패(점수 차이) 자체에는 영향을 주지 않습니다.
    -   하지만 문제 조건상 '가장 낮은 점수를 더 많이 맞힌 경우'를 따지게 되므로, 0점에 몰아주는 것이 유리할 수 있습니다.

요약하자면, **규칙상 모든 화살을 사용해야 하므로, 점수에 영향이 없는 0점에 남은 화살을 모두 버리는(처리하는) 과정**입니다.



