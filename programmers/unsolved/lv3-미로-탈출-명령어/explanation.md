# 미로 탈출 명령어

## 문제 설명
격자형 미로에서 `(x, y)`에서 출발하여 `(r, c)`로 정확히 `k`번 이동하여 도착하는 경로 중, **사전 순으로 가장 빠른 경로명**을 구하세요.
- 경로 문자열은 'd'(하), 'l'(좌), 'r'(우), 'u'(상) 문자로 구성됩니다.
- 사전 순: d < l < r < u

## 문제 해결 전략

**그리디(Greedy)** 전략이 효과적입니다.
도착지까지 가는 최단 거리를 `dist`라고 할 때, 남은 이동 횟수 `k`가 `dist`보다 작으면 도달 불가능합니다.
또한, `k - dist`가 홀수라면, 도달 불가능합니다. (왔다 갔다 하는 횟수는 항상 짝수여야 제자리에 돌아오거나 해당 위치 유지 가능)

### 그리디 탐색
현재 위치에서 다음 이동할 방향을 결정할 때, **사전 순으로 가장 빠른 방향(d -> l -> r -> u)** 순서로 시도합니다.
해당 방향으로 한 칸 이동했을 때, "남은 횟수 내에 도착지까지 갈 수 있는지" 확인합니다.
갈 수 있다면, 그 방향을 선택하고 바로 다음 스텝으로 넘어갑니다. (다른 방향 볼 필요 없음, 사전 순 최소 보장됨)

### 조건 검사 함수 (`can_reach`)
- 현재 위치 `(nx, ny)`에서 목표 `(r, c)`까지 거리 `diff = abs(nx - r) + abs(ny - c)`
- 남은 턴 `remain = k - 1`
- `diff <= remain` AND `(remain - diff) % 2 == 0` 이면 가능.

## Python 코드

```python
import sys
sys.setrecursionlimit(5000) # 재귀 깊을 수 있음

def solution(n, m, x, y, r, c, k):
    # 맨해튼 거리
    dist = abs(x - r) + abs(y - c)
    if dist > k or (k - dist) % 2 == 1:
        return "impossible"
    
    # 방향: d, l, r, u (사전 순)
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    d_char = ['d', 'l', 'r', 'u']
    
    answer = []
    curr_x, curr_y = x, y
    
    # 총 k번 이동
    for _ in range(k):
        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]
            
            # 격자 범위 체크
            if 1 <= nx <= n and 1 <= ny <= m:
                # 남은 턴 수로 도달 가능한지 체크
                remain_turns = k - (len(answer) + 1)
                dist_to_target = abs(nx - r) + abs(ny - c)
                
                if dist_to_target <= remain_turns and (remain_turns - dist_to_target) % 2 == 0:
                    # 가능하면 이 방향 확정 (break 하고 다음 턴 진행)
                    answer.append(d_char[i])
                    curr_x, curr_y = nx, ny
                    break
                    
    return "".join(answer)
```
