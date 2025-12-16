# 피로도

## 문제 설명
현재 피로도 `k`와 각 던전별 "최소 필요 피로도", "소모 피로도"가 담긴 `dungeons` 배열이 주어질 때, 유저가 탐험할 수 있는 최대 던전 수를 구하는 문제입니다.

### 핵심 개념
1.  **완전 탐색 (Exhaustive Search)**: 던전의 개수가 최대 8개로 매우 적습니다. 따라서 모든 순서를 다 고려해봐도 경우의 수가 $8! = 40,320$가지밖에 되지 않습니다.
2.  **순열 (Permutations)**: 던전을 도는 "순서"가 중요합니다. 어떤 순서로 도느냐에 따라 남은 피로도가 달라지고, 갈 수 있는 던전 수가 달라집니다. Python의 `itertools.permutations`를 사용하면 쉽게 구현할 수 있습니다.
3.  **DFS (깊이 우선 탐색)**: 순열 대신 재귀 함수(DFS)를 이용하여 백트래킹 방식으로 풀 수도 있습니다.

## Python 풀이 (순열 사용)

```python
from itertools import permutations

def solution(k, dungeons):
    max_dungeons = 0
    
    # 모든 던전 방문 순서를 생성
    for perm in permutations(dungeons):
        current_k = k
        count = 0
        
        # 해당 순서대로 던전 탐험 시도
        for min_required, consume in perm:
            if current_k >= min_required:
                current_k -= consume
                count += 1
            else:
                # 피로도 부족으로 이 순서에서는 더 이상 진행 불가인 경우가 많지만,
                # 문제 조건상 "순서대로" 탐험하므로, 여기서 멈추지 않고 
                # 다음 던전(이 순열 상의 다음)도 시도해봐야 할까요?
                # 문제의 뉘앙스는 "순서대로 돌 때 최대 몇 개" 이므로
                # 앞의 것을 못 가면 뒤의 것도 못 가는게 아니라, 
                # 단순히 이 case에서 몇 개 성공했는지를 세면 됩니다.
                # 다만 효율성을 위해 보통 그리디하게 접근하지 않고 완전탐색을 합니다.
                # 여기서는 순열의 순서대로 '방문 시도'를 했을 때 성공 횟수입니다.
                # 만약 현재 못 가면 count 증가는 안 하고, 피로도 소모도 안 함.
                # 하지만 일반적으로 던전 게임은 '입장 불가'면 그냥 못 들어가는 것이지
                # 다음 던전으로 바로 넘어갈 수 있는지는 문제에 따라 다르나,
                # 이 문제의 '순서' 개념은 "유저가 정한 순서대로 돌 때"입니다.
                # 못 들어가는 던전은 건너뛰고 다음 걸 갈 수 있는지?
                # -> 통상적으로 순열 완전탐색은 "방문 가능한 최대 깊이"를 말합니다.
                # 하지만 이 풀이(permutations)는 "순서가 고정되었을 때 앞에서부터 차례로 입장"을 가정합니다.
                # 중간에 못 들어가면 그 뒤에도 못 들어간다고 보는게 맞을까요?
                # 아닙니다. 중간에 소모가 큰 던전이라 못 들어가도, 그 뒤에 소모 적은 던전이 있을 수 있습니다.
                # 따라서 continue 하는 것이 맞습니다.
                # 단, 문제 예시를 보면 "하루에 한 번씩 탐험" 같은 제약이 아니라, 단순 최대 던전 수입니다.
                pass 
        
        # 위 로직보다 더 직관적인 것은:
        # "순열"은 내가 돌기로 한 계획표입니다. 
        # 계획표 순서대로 시도하되, 조건 안 맞으면 '실패'하고 넘어가는게 아니라
        # 보통 "이어서 탐험" 합니다.
        # 그러나 대부분의 풀이는 "조건 만족하는 것만 visit" 로직을 씁니다.
        
        # 다시 명확히: 이 문제는 "최대 몇 개를 돌 수 있는가?" 이므로
        # 순열을 쓰는 경우: "모든 순서 배치 중 하나"를 골라,
        # "순서대로 들어가되 못 들어가면 못 들어가는 것"으로 시뮬레이션 해서
        # count가 최대인 것을 찾으면 됩니다.
        
        if count > max_dungeons:
            max_dungeons = count
            
    return max_dungeons
```

### 개선된 풀이 (DFS)
순열은 $N!$을 다 만들어서 메모리를 쓸 수 있으니, DFS가 사실 더 깔끔할 수 있습니다.

```python
answer = 0

def dfs(k, count, dungeons, visited):
    global answer
    answer = max(answer, count)
    
    for i in range(len(dungeons)):
        min_req, consume = dungeons[i]
        # 방문하지 않았고, 피로도가 충분하면 진입
        if not visited[i] and k >= min_req:
            visited[i] = True
            dfs(k - consume, count + 1, dungeons, visited)
            visited[i] = False # 백트래킹

def solution(k, dungeons):
    global answer
    answer = 0
    visited = [False] * len(dungeons)
    
    dfs(k, 0, dungeons, visited)
    
    return answer
```

### 코드 설명 (DFS 방식)
- `visited` 리스트로 현재 탐색 경로에서 방문한 던전을 체크합니다.
- 모든 던전에 대해 Loop를 돌며, 갈 수 있는 조건(`!visited` and `k >= min_req`)이면 재귀 호출(`dfs`)합니다.
- 재귀 호출 시 `k`를 소모시키고 `count`를 1 증가시킵니다.
- 재귀가 끝나고 돌아오면(`visited[i] = False`) 다른 경로를 탐색할 수 있게 상태를 복구합니다 (백트래킹).
- `answer`는 전역 변수(또는 nonlocal)로 유지하며 최대값을 갱신합니다.
