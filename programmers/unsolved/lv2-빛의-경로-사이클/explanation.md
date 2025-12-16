# 빛의 경로 사이클

## 문제 설명
격자 모양의 보드에서 빛이 이동하며 사이클을 만드는 문제입니다. 각 칸에는 'S'(직진), 'L'(좌회전), 'R'(우회전)이 적혀있습니다. 빛은 격자를 넘어가면 반대편에서 나옵니다. 가능한 모든 사이클을 찾고, 각 사이클의 길이를 오름차순으로 정렬하여 반환해야 합니다.

### 핵심 개념
1.  **3차원 방문 배열 (Visited Array)**: 빛의 상태는 "위치(행, 열)"뿐만 아니라 "**들어오는 방향(Direction)**"도 중요합니다. 같은 칸이라도 위에서 왔는지, 아래에서 왔는지에 따라 나가는 방향이 다릅니다. 따라서 `visited[row][col][direction]` 형태의 3차원 배열이 필요합니다.
2.  **방향 전환 로직**:
    - **S**: 방향 그대로 직진.
    - **L**: 왼쪽으로 90도 회전. (상 -> 좌, 하 -> 우, 좌 -> 하, 우 -> 상)
    - **R**: 오른쪽으로 90도 회전. (상 -> 우, 하 -> 좌, 좌 -> 상, 우 -> 하)
3.  **모듈러 연산 (격자 순환)**: 격자 밖으로 나가면 반대편으로 돌아오므로, 좌표 계산 시 `% R`, `% C` 연산이 필요합니다.
4.  **완전 탐색**: 보드의 모든 칸, 모든 4개 방향에 대해 아직 방문하지 않은 경로라면 사이클을 탐색합니다.

## Python 풀이

```python
import sys

# 재귀 깊이 제한 해제
sys.setrecursionlimit(10**6)

def solution(grid):
    R = len(grid)
    C = len(grid[0])
    
    # 상, 하, 좌, 우 (0, 1, 2, 3)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    # 3차원 방문 배열 [행][열][방향]
    visited = [[[False] * 4 for _ in range(C)] for _ in range(R)]
    answer = []
    
    for r in range(R):
        for c in range(C):
            for d in range(4):
                if not visited[r][c][d]:
                    # 새로운 사이클 탐색 시작
                    cnt = 0
                    cr, cc, cd = r, c, d
                    
                    while not visited[cr][cc][cd]:
                        visited[cr][cc][cd] = True
                        cnt += 1
                        
                        # 현재 칸의 명령에 따라 다음 방향 결정
                        cmd = grid[cr][cc]
                        if cmd == 'S':
                            nd = cd # 직진
                        elif cmd == 'L':
                            # 상(0)->좌(2), 하(1)->우(3), 좌(2)->하(1), 우(3)->상(0)
                            # 규칙 찾아보면: (0->2, 1->3, 2->1, 3->0) 좀 복잡함
                            # 간단한 방향 배열 순서로: 상 우 하 좌 (0, 1, 2, 3) 시계방향
                            # 상(0), 하(1), 좌(2), 우(3) 이 순서는 계산하기 힘듦
                            
                            # 방향 정의를 다시: 상(0), 우(1), 하(2), 좌(3) (시계방향)
                            # 이렇게 하면 L은 -1, R은 +1 로 간단해짐.
                            # 하지만 위 dr, dc 배열을 그대로 쓴다면 if문 분기 필요
                            
                            if cd == 0: nd = 2
                            elif cd == 1: nd = 3
                            elif cd == 2: nd = 1
                            else: nd = 0
                        elif cmd == 'R':
                            if cd == 0: nd = 3
                            elif cd == 1: nd = 2
                            elif cd == 2: nd = 0
                            else: nd = 1
                            
                        # 다음 좌표 이동 (모듈러 연산으로 격자 순환 처리)
                        nr = (cr + dr[nd]) % R
                        nc = (cc + dc[nd]) % C
                        
                        # 상태 업데이트
                        cr, cc, cd = nr, nc, nd
                        
                    answer.append(cnt)
    
    return sorted(answer)
```

### 코드 개선 (방향 인덱스 재정의)
`dr`, `dc` 순서를 시계 방향으로 맞추면 회전 로직이 훨씬 간단해집니다.
`상(0) -> 우(1) -> 하(2) -> 좌(3)`

```python
def solution(grid):
    R = len(grid)
    C = len(grid[0])
    
    # 상, 우, 하, 좌 (시계 방향)
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    visited = [[[False] * 4 for _ in range(C)] for _ in range(R)]
    answer = []
    
    for r in range(R):
        for c in range(C):
            for d in range(4):
                if not visited[r][c][d]:
                    cnt = 0
                    cr, cc, cd = r, c, d
                    
                    while not visited[cr][cc][cd]:
                        visited[cr][cc][cd] = True
                        cnt += 1
                        
                        # 다음 방향 계산
                        cmd = grid[cr][cc]
                        if cmd == 'L':
                            cd = (cd - 1) % 4 # 반시계 90도
                        elif cmd == 'R':
                            cd = (cd + 1) % 4 # 시계 90도
                        # 'S'는 cd 그대로
                        
                        # 이동
                        cr = (cr + dr[cd]) % R
                        cc = (cc + dc[cd]) % C
                        
                    answer.append(cnt)
    
    return sorted(answer)
```

### 코드 설명
- 개선된 코드가 훨씬 직관적입니다.
- `dr`, `dc`를 시계방향(상->우->하->좌)으로 정의함으로써, **L(좌회전)**은 인덱스 `-1`, **R(우회전)**은 인덱스 `+1` 만 해주면 됩니다.
- 모든 좌표와 모든 방향에서 출발해보고, 이미 방문한 경로(`visited`)는 건너뜁니다.
- 사이클이 형성되므로 `while not visited[...]` 루프는 반드시 종료됩니다. 처음 시작점(및 방향)으로 돌아오게 되어 있습니다.
