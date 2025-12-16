# 고고학 최고의 발견

## 문제 설명
$N \times N$ 크기의 격자에 시계들이 있습니다. 시계는 12시(0), 3시(1), 6시(2), 9시(3) 중 하나의 방향을 가리킵니다.
시계를 90도 시계방향으로 돌리면(0->1->2->3->0), 그 시계와 상하좌우 인접한 시계들도 함께 돌아갑니다.
모든 시계바늘이 12시(0)를 가리키게 하는 최소 조작 횟수를 구하세요.

## 문제 해결 전략

이 문제는 N이 작고(2~8), 시계의 상태가 한정적이라는 점을 이용합니다.
핵심 아이디어는 **"첫 번째 행의 조작 상태가 결정되면, 나머지 행의 조작은 자동으로 결정된다"**는 것입니다.

1. **첫 번째 행 결정**:
   - 첫 번째 줄의 각 시계는 0번, 1번, 2번, 3번 회전할 수 있습니다.
   - $N$개의 시계가 있으므로 총 $4^N$가지 경우의 수가 있습니다. ($N=8$일 때 $4^8 = 65,536$, 충분히 작음)
   - 재귀나 중복순열로 첫 줄의 모든 경우를 시도합니다.

2. **나머지 행 자동 결정 (Greedy)**:
   - 첫 번째 줄의 회전이 끝나면, (0, 0) 시계의 상태를 봅니다.
   - (0, 0) 시계가 12시(0)가 아니라면, 이를 0으로 만들 수 있는 유일한 방법은 그 바로 아래인 (1, 0) 시계를 돌리는 것뿐입니다. (왜냐하면 (0, 0) 주변 중 (0, 1)이나 (0, -1) 등의 영향은 이미 첫 줄 결정 단계에서 끝났고, 이제 (1, 0)만 남았기 때문입니다. 정확히는, 위에서부터 아래로 순차적으로 맞출 때, $(r, c)$를 맞추기 위해 $(r+1, c)$를 조작한다고 정하면 됩니다.)
   - 즉, $(r, c)$ 상태가 $k$라면, $(r+1, c)$를 $(4-k) \% 4$번 돌려서 $(r, c)$를 0으로 만듭니다.
   - 이 과정을 마지막 행 직전까지 반복합니다.

3. **검증**:
   - 마지막 행까지 모두 조작한 뒤, 마지막 행의 시계들이 모두 0인지 확인합니다.
   - 모두 0이면 성공, 그때의 총 조작 횟수를 기록합니다.

## Python 코드

```python
import copy
from itertools import product

def solution(clockHands):
    n = len(clockHands)
    min_clicks = float('inf')
    
    # 첫 번째 줄의 모든 경우의 수: 4^n
    for first_row_clicks in product(range(4), repeat=n):
        # 원본 복사
        grid = [row[:] for row in clockHands]
        
        clicks = 0
        
        # 1. 첫 번째 줄 조작 적용
        for j in range(n):
            cnt = first_row_clicks[j]
            clicks += cnt
            
            # (0, j) 본인 회전
            grid[0][j] = (grid[0][j] + cnt) % 4
            
            # 주변 영향
            # 상하좌우: (0, j-1), (0, j+1), (1, j) -> (0, -1)은 없음.
            if j > 0:
                grid[0][j-1] = (grid[0][j-1] + cnt) % 4
            if j < n - 1:
                grid[0][j+1] = (grid[0][j+1] + cnt) % 4
            if n > 1: # 행이 2개 이상일 때만
                grid[1][j] = (grid[1][j] + cnt) % 4
                
        # 2. 두 번째 줄부터 마지막 줄까지 (Greedy)
        for i in range(1, n):
            for j in range(n):
                # 바로 위 (i-1, j)가 0이 되도록 현재 (i, j)를 회전
                # 위쪽 시계 값
                val_up = grid[i-1][j]
                if val_up != 0:
                    needed = (4 - val_up) % 4
                    clicks += needed
                    
                    # (i, j) 회전 및 영향 전파
                    # 본인
                    grid[i][j] = (grid[i][j] + needed) % 4
                    # 위 (i-1, j) -> 0이 됨 (목표 달성)
                    grid[i-1][j] = (grid[i-1][j] + needed) % 4 
                    # 왼쪽
                    if j > 0:
                        grid[i][j-1] = (grid[i][j-1] + needed) % 4
                    # 오른쪽
                    if j < n - 1:
                        grid[i][j+1] = (grid[i][j+1] + needed) % 4
                    # 아래 (i+1, j)
                    if i < n - 1:
                        grid[i+1][j] = (grid[i+1][j] + needed) % 4
                        
        # 3. 마지막 줄 검증
        if all(val == 0 for val in grid[n-1]):
            min_clicks = min(min_clicks, clicks)
            
    return min_clicks
```
