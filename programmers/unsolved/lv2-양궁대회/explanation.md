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
    # left: 남은 화살 수
    def dfs(idx, arrows, left):
        nonlocal max_diff, answer
        
        if idx == 11 or left == 0:
            # 남은 화살은 0점(idx 10)에 몰아줌
            if left > 0:
                arrows[10] += left
                
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
            if left > 0:
                arrows[10] -= left
            return

        # 1. 현재 점수(10-idx)를 먹는 경우 (어피치보다 1발 더 쏨)
        needed = info[idx] + 1
        if left >= needed:
            arrows[idx] = needed
            dfs(idx + 1, arrows, left - needed)
            arrows[idx] = 0 # 복구
            
        # 2. 현재 점수를 포기하는 경우 (0발 쏨)
        dfs(idx + 1, arrows, left)

    dfs(0, [0]*11, n)
    
    if max_diff == 0:
        return [-1]
        
    return answer
```
