# 무인도 여행

## 문제 설명
`X`와 `1`~`9`의 숫자로 이루어진 지도가 주어집니다.
`X`는 바다, 숫자는 무인도의 식량 값을 의미합니다.
상하좌우로 연결된 땅(숫자)들은 하나의 무인도를 이룹니다.
각 무인도에 있는 식량의 합을 구해서 오름차순으로 담아 반환해야 합니다.
만약 무인도가 하나도 없다면 `[-1]`을 반환합니다.

## 풀이 개념
**BFS (너비 우선 탐색)** 또는 **DFS (깊이 우선 탐색)**를 사용하여 연결된 컴포넌트(Connected Component)를 찾는 문제입니다.

1. 지도를 전체 탐색하며 방문하지 않은 숫자(`!X`)를 찾습니다.
2. 해당 위치에서 BFS/DFS를 시작하여 연결된 모든 숫자 칸을 방문하고, 그 합을 계산합니다.
3. 방문 처리(`visited`)를 하여 중복 방문을 방지합니다.
4. 구한 합을 리스트에 추가합니다.
5. 모든 탐색이 끝나면 리스트를 오름차순 정렬합니다. 빈 리스트면 `[-1]`을 반환합니다.

## 코드 (Python)

```python
from collections import deque

def solution(maps):
    rows = len(maps)
    cols = len(maps[0])
    visited = [[False] * cols for _ in range(rows)]
    answer = []
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    for r in range(rows):
        for c in range(cols):
            if maps[r][c] != 'X' and not visited[r][c]:
                # BFS 탐색 시작
                q = deque([(r, c)])
                visited[r][c] = True
                total_food = int(maps[r][c])
                
                while q:
                    cur_r, cur_c = q.popleft()
                    
                    for i in range(4):
                        nr, nc = cur_r + dr[i], cur_c + dc[i]
                        
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if maps[nr][nc] != 'X' and not visited[nr][nc]:
                                visited[nr][nc] = True
                                total_food += int(maps[nr][nc])
                                q.append((nr, nc))
                                
                answer.append(total_food)
                
    if not answer:
        return [-1]
    
    return sorted(answer)
```

### 코드 (DFS - 재귀 방식)
시스템 스택(재귀 호출)을 이용하여 더 간결하게 구현할 수도 있습니다. 단, 재귀 깊이 제한(`setrecursionlimit`)에 주의해야 합니다.

```python
import sys
sys.setrecursionlimit(10**6)

def solution(maps):
    rows, cols = len(maps), len(maps[0])
    visited = [[False] * cols for _ in range(rows)]
    answer = []
    
    def dfs(r, c):
        # 1. 방문 처리 및 현재 값 더하기
        visited[r][c] = True
        total = int(maps[r][c])
        
        # 2. 4방향 탐색
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if maps[nr][nc] != 'X' and not visited[nr][nc]:
                    total += dfs(nr, nc) # 재귀 호출 반환값을 누적
        
        return total

    for r in range(rows):
        for c in range(cols):
            if maps[r][c] != 'X' and not visited[r][c]:
                answer.append(dfs(r, c))
                
    if not answer:
        return [-1]
        
    return sorted(answer)
```
