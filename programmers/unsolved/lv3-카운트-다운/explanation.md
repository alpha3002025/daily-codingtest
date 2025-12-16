# 카운트 다운

## 문제 설명
다트 게임입니다. 목표 점수 `target`을 0으로 만들어야 합니다.
- 다트 점수: 싱글(1~20), 더블(2~40), 트리플(3~60), 불(50).
- 승리 조건: 최소한의 다트로 0점 만들기.
- 다트 수가 같다면: "싱글" 또는 "불"을 더 많이 맞춘 사람이 승리. (더블, 트리플은 비선호)
- 남은 점수보다 큰 점수를 얻으면 무효(Bust) 처리되나, 문제에서는 최적의 경로를 찾으므로 고려하지 않고 정확히 0으로 만드는 경로를 찾으면 됩니다.

## 문제 해결 전략

**다이나믹 프로그래밍(DP)** 문제입니다.
목표 점수 `target`이 최대 10만입니다.
각 점수 `i`를 만드는 데 필요한 `[최소 던짐 수, 최대 싱글/불 수]`를 구합니다.
`dp[i]`가 `[던짐, 싱글불]`일 때, 점수 $S$를 맞춰서 `i` 상태로 가는 경우를 갱신합니다.
단, 역으로 생각하여 `0`점에서 시작해 `target`으로 가는 방식 혹은 `target`에서 0으로 가는 방식(Knapsack)을 씁니다.

1. **점수 목록 생성**:
   - 싱글/불(선호): 1~20, 50
   - 더블/트리플(비선호): 1~20의 2배, 3배 (단, 위 싱글/불 점수와 겹치는 경우 선호 점수로 처리하는 게 유리하므로 중복 제거 시 주의. 하지만 문제 정의상 '싱글' 영역이나 '불' 영역을 맞추는 것이므로 점수 값이 같아도 영역이 다르면 다릅니다. 그러나 점수가 같다면 무조건 선호 영역(싱글/불)을 맞췄다고 가정하는 게 이득이므로, 50점을 더블 25로 맞출 필요 없이 불로 맞췄다고 치면 됩니다. 단, 트리플이나 더블로만 만들 수 있는 점수(예: 60)는 비선호입니다.)
   - 선호 점수 집합: `SB = {1..20, 50}`
   - 비선호 점수 집합: `DT = ({2*x | x in 1..20} U {3*x | x in 1..20}) - SB`

2. **DP 초기화**:
   - `dp[0] = [0, 0]`
   - `dp[k] = [infinity, 0]`

3. **점화식**:
   - `dp[i]`를 갱신하기 위해 가능한 모든 다트 점수 `P`에 대해:
     - `prev = i - P`
     - if `dp[prev]` valid:
       - `new_throw = dp[prev][0] + 1`
       - `new_sb = dp[prev][1] + (1 if P in SB else 0)`
       - 갱신 조건: `new_throw`가 작거나, 같으면 `new_sb`가 큰 쪽으로.

   - 하지만 `target`이 10만이므로, 모든 점수(1~60)에 대해 루프를 돌면 $100000 \times 60$ 으로 약 600만 연산. 충분히 가능합니다.
   
   - 더 최적화: 대부분의 큰 점수는 '60(트리플 20)'이나 '50(불)'로 채우는 게 유리합니다. 그리디하게 접근할 수도 있지만, DP가 확실합니다.

## Python 코드

```python
def solution(target):
    # dp[i] = [min_throws, max_single_bull]
    # 초기값: 던짐 수 무한대, 싱글불 -1
    dp = [[float('inf'), 0] for _ in range(target + 1)]
    dp[0] = [0, 0]
    
    # 가능한 점수들 (1점 ~ 60점)
    # 점수별로 [던짐1, 싱글불여부] 정보를 미리 매핑
    # 같은 점수라면 싱글/불이 무조건 이득이므로 우선순위 둠.
    
    scores = []
    
    # 싱글 (1~20), 불(50) -> SB +1
    for i in range(1, 21):
        scores.append((i, 1)) # (점수, SB증가량)
    scores.append((50, 1))
    
    # 더블, 트리플 (값이 싱글/불과 겹치면 무시해도 됨, 어차피 SB 1인게 더 좋으니)
    # 하지만 겹치지 않는 값(예: 21 이상 중 50 제외)은 필요.
    # 일단 생성 후, 더 좋은 조건이 있으면 덮어씌우기?
    # 아니, 그냥 다 넣고 DP 돌릴 때 최적해 선택하면 됨. 
    # 하지만 연산 줄이려면 유니크한 점수만 남기는 게 좋음.
    
    # 점수 p를 얻는 최상의 방법(SB 1 or 0) 미리 계산
    best_way = {} # score -> sb_point
    
    # 비선호 먼저 등록
    for i in range(1, 21):
        for mul in [2, 3]:
            val = i * mul
            if val not in best_way:
                best_way[val] = 0
            # 이미 있으면 0 (비선호)는 굳이 갱신 안 함.
            
    # 선호 덮어쓰기 (SB=1 이 무조건 좋음)
    for i in range(1, 21):
        best_way[i] = 1
    best_way[50] = 1
    
    # 리스트로 변환
    score_list = list(best_way.items()) # [(점수, sb_point), ...]
    
    for i in range(1, target + 1):
        for s, sb in score_list:
            if i - s >= 0:
                prev_throw, prev_sb = dp[i-s]
                
                if prev_throw == float('inf'): continue
                
                curr_throw = prev_throw + 1
                curr_sb = prev_sb + sb
                
                # 갱신 조건
                if curr_throw < dp[i][0]:
                    dp[i] = [curr_throw, curr_sb]
                elif curr_throw == dp[i][0]:
                    if curr_sb > dp[i][1]:
                        dp[i] = [curr_throw, curr_sb]
                        
    return dp[target]
```
