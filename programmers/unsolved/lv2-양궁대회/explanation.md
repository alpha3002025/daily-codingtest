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
    
    # idx: 현재 고려중인 점수 인덱스 (0: 10점, 1: 9점 ... )
    # arrows: 라이언이 쏜 화살 현황 리스트
    # remain: 남은 화살 수
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
                    # 낮은 점수를 더 많이 맞힌 경우 선택
                    # (리스트 역순 비교시 더 큰 것이 답)
                    # Python의 리스트 비교는 앞에서부터 하므로 역순으로 뒤집어서 비교해야
                    # 낮은 점수(인덱스가 큰 쪽) 우선 조건을 처리할 수 있음??
                    # 아니면 for문으로 뒤에서부터 비교
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

## 옛날 풀이 (python)
```python
def solution(n, info):
    apeach_score = sum(10-i for i in range(11) if info[i] != 0)
    weights = [-1] + [x+1 for x in info]
    
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

**1. 문제 치환**
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

**2. 변수 설정**
- `weights`: 각 점수(`i`)를 따기 위한 화살 비용 리스트 (인덱스 1부터 10점~0점 역순 배치 등 확인 필요)
- `values`: 각 점수(`i`)를 땄을 때의 가치 리스트
- `dp[i][w]`: `i`번째 과녁까지 고려하고, 화살 `w`개를 썼을 때 얻을 수 있는 **최대 점수 이득**

**3. DP 점화식**
```python
if current_weight > current_capacity:
    # 화살이 모자라서 현재 점수를 못 따는 경우: 이전 상태 유지
    dp[i][w] = dp[i-1][w]
else:
    # 점수를 따거나, 안 따거나 중 더 큰 이득 선택
    dp[i][w] = max(
        dp[i-1][w - current_weight] + current_value,  # 따는 경우
        dp[i-1][w]                                    # 안 따는 경우
    )
```

**4. 정답 추적 (Backtracking)**
- DP 테이블이 채워진 후, 역추적을 통해 실제로 어떤 과녁을 선택했는지 찾아냅니다.
- `dp[i][w]` 값이 **"따는 경우"**(`dp[i-1][w-weights[i]] + values[i]`)와 같다면, 해당 과녁을 맞힌 것으로 간주하여 `answer`에 기록하고 남은 화살 `w`를 차감합니다.

**5. 남은 화살 처리**
- 모든 추적이 끝난 후, 아직 화살이 남았다면 (`n - sum(answer)`), 이는 점수 이득엔 기여하지 못하는 잉여 화살이므로 0점(인덱스 10) 과녁에 몰아줍니다. (낮은 점수 우선 조건 충족에도 유리)

<br/>
<br/>

