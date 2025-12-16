# 거리두기 확인하기

## 문제 설명
5x5 크기의 대기실 5개가 주어집니다. 각 대기실별로 응시자들이 거리두기 수칙을 지키고 있는지 확인해야 합니다.
- **수칙**: 맨해튼 거리 $ |r1 - r2| + |c1 - c2| \le 2 $ 인 경우, 파티션으로 막혀있지 않다면 거리두기 위반입니다.
- **파티션**: 응시자 사이에 파티션('X')이 있으면 거리가 2여도 괜찮습니다.
- **빈 테이블**: 빈 테이블('O')은 막아주지 못합니다.

### 핵심 개념
1.  **BFS (너비 우선 탐색)**: 각 응시자('P') 위치에서 시작하여 거리 2 이내에 다른 응시자가 도달 가능한지 탐색합니다.
2.  **맨해튼 거리**: 상하좌우 이동 횟수와 동일합니다. BFS 탐색 깊이(depth)가 2 이하인 영역을 검사하면 됩니다.
3.  **조건부 탐색**: 'X'(파티션)를 만나면 그 방향으로는 더 이상 갈 수 없습니다. 'O'(빈 테이블)이면 계속 이동합니다.

## Python 풀이

```python
from collections import deque

def check_place(place):
    # 응시자(P)들의 위치 찾기
    people = []
    for r in range(5):
        for c in range(5):
            if place[r][c] == 'P':
                people.append((r, c))
                
    # 각 응시자마다 BFS 탐색
    for r, c in people:
        q = deque()
        q.append((r, c, 0)) # r, c, distance
        visited = [[False]*5 for _ in range(5)]
        visited[r][c] = True
        
        while q:
            cr, cc, dist = q.popleft()
            
            # 거리가 2 이상이면 더 볼 필요 없음 (2까지만 검사)
            if dist >= 2:
                continue
                
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = cr + dr, cc + dc
                
                if 0 <= nr < 5 and 0 <= nc < 5 and not visited[nr][nc]:
                    if place[nr][nc] == 'X':
                        continue # 파티션 막힘
                    
                    if place[nr][nc] == 'P':
                        return 0 # 거리 2 이내에 다른 응시자 발견 -> 위반
                        
                    visited[nr][nc] = True
                    q.append((nr, nc, dist + 1))
                    
    return 1 # 모두 통과

def solution(places):
    answer = []
    for place in places:
        answer.append(check_place(place))
    return answer
```

### 코드 설명
- 각 대기실(`place`)마다 독립적으로 `check_place`를 수행합니다.
- `check_place`는 먼저 모든 'P'의 위치를 찾습니다.
- 각 'P'에서 출발하여 거리 2 이내(`dist < 2`)를 탐색합니다.
    - 상하좌우 인접한 칸(`nr, nc`)을 봅니다.
    - 'X'면 막혀서 못 가므로 `continue`.
    - 'P'면 거리두기 위반이므로 즉시 `0` 반환. (출발점 제외, `visited` 체크로 해결됨)
    - 'O'면 통과 가능하므로 큐에 넣고 계속 탐색(`dist + 1`).
- 모든 'P'에 대해 문제가 없으면 `1`을 반환합니다.

### 주의사항
- BFS 탐색 시 `visited` 배열을 매번 초기화해야 합니다 (각 사람 기준이므로).
- 거리가 2인 지점까지만 검사하면 되므로, 큐에서 꺼낸 `dist`가 2이면 더 이상 확장하지 않습니다(`continue`). 하지만 `dist`가 1인 상태에서 발견한 'P'는 거리가 2인 P이므로 검출해야 합니다. 코드상으로는 `dist` 0, 1일 때 큐에 넣고, 꺼냈을 때 `dist`가 2인 상태에서는 다음 칸(거리 3)으로 가지 않게 막습니다. 단, 'P' 검사는 큐에 넣기 전(`nr, nc`) 단계에서 이루어지므로, `dist=0`일 때 인접(거리1) P 발견, `dist=1`일 때 인접(거리2) P 발견 구조입니다.

