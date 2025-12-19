# 숫자 변환하기

## 문제 설명
자연수 `x`, `y`, `n`이 주어집니다. `x`를 `y`로 변환하려고 합니다.
사용 가능한 연산은 3가지입니다:
1. `x + n`
2. `x * 2`
3. `x * 3`
`x`를 `y`로 변환하는 데 필요한 최소 연산 횟수를 구합니다. 불가능하면 -1을 반환합니다.

## 풀이 개념
**BFS (너비 우선 탐색)** 또는 **DP (동적 계획법)**으로 풀 수 있습니다.
최소 횟수를 구하는 문제이므로 BFS가 직관적이며 효율적입니다.

1. 큐에 `(현재값, 연산횟수)`를 넣고 시작합니다. 초기값: `[(x, 0)]`.
2. 이미 방문한 숫자를 다시 계산하지 않기 위해 `visited` 집합(Set)이나 dp 배열을 사용합니다.
3. 큐에서 값을 꺼내어 3가지 연산을 수행합니다.
   - 결과값이 `y`와 같으면 연산 횟수 `cnt + 1`을 반환합니다.
   - 결과값이 `y`보다 작고 방문하지 않았다면 큐에 추가하고 방문 처리합니다.
4. 큐가 빌 때까지 `y`에 도달하지 못하면 -1을 반환합니다.

## bfs 코드 (Python)

```python
from collections import deque

def solution(x, y, n):
    if x == y:
        return 0
    
    # (current_value, count)
    q = deque([(x, 0)])
    visited = set([x])
    
    while q:
        curr, cnt = q.popleft()
        
        # 3가지 연산
        next_vals = [curr + n, curr * 2, curr * 3]
        
        for v in next_vals:
            if v == y:
                return cnt + 1
            
            if v < y and v not in visited:
                visited.add(v)
                q.append((v, cnt + 1))
                
    return -1
```

## dp코드 (Python)
DP 배열(`dp[i]`: i를 만드는 최소 횟수)을 사용하여 **작은 숫자부터 y까지** 채워나가는 방식입니다. `x`에서 출발하여 `+n`, `*2`, `*3` 위치의 값을 갱신합니다.

```python
def solution(x, y, n):
    INF = float('inf')
    dp = [INF] * (y + 1)
    
    dp[x] = 0
    
    for i in range(x, y):
        # 도달할 수 없는 숫자는 건너뜀
        if dp[i] == INF:
            continue
            
        # 3가지 경우의 수 갱신
        if i + n <= y:
            dp[i + n] = min(dp[i + n], dp[i] + 1)
        if i * 2 <= y:
            dp[i * 2] = min(dp[i * 2], dp[i] + 1)
        if i * 3 <= y:
            dp[i * 3] = min(dp[i * 3], dp[i] + 1)
            
    if dp[y] == INF:
        return -1
        
    return dp[y]
```

**DP 풀이 설명**:
- `dp` 테이블을 `INF`로 초기화하고, 시작점 `dp[x] = 0`으로 설정합니다.
- `x`부터 `y` 직전까지 반복하며, 현재 숫자 `i`에 도달할 수 있다면(`dp[i] != INF`), 그 다음 단계(`i+n`, `i*2`, `i*3`)의 횟수를 **최솟값으로 갱신**합니다.
- BFS보다 직관적일 수 있으나, 불필요한 모든 숫자(`x`~`y`)를 순회해야 한다는 단점도 있습니다. (BFS는 필요한 숫자만 방문)

## 나의 풀이
### 2025/12/19 (bfs)
```python
from collections import deque

def solution(x, y, n):
    visited = set()
    queue = deque([])
    queue.append((x,0))
    visited.add(x)
    
    while queue:
        curr_number, curr_cost = queue.popleft()
        
        if curr_number == y:
            return curr_cost
        
        for next_number in [curr_number + n, curr_number * 2, curr_number * 3]:
            
            if next_number in visited: 
                continue
            if next_number > y:
                continue
            queue.append((next_number, curr_cost+1))
            visited.add(next_number)
    
    return -1
```
<br/>
<br/>

### 2025/12/19 (dp)
```python
def solution(x, y, n):
    dp = [float('inf')]*(y+1)
    dp[x] = 0
    
    for curr_number in range(x, y):
        if dp[curr_number] == float('inf'):
            continue
            
        # for next_number in [curr_number + n, curr_number * 2, curr_number * 3]:
        if curr_number + n <= y:
            dp[curr_number + n] = min(dp[curr_number]+1, dp[curr_number + n])
        if curr_number * 2 <= y:
            dp[curr_number * 2] = min(dp[curr_number]+1, dp[curr_number * 2])
        if curr_number * 3 <= y:
            dp[curr_number * 3] = min(dp[curr_number]+1, dp[curr_number * 3])
            
    if dp[y] == float('inf'):
        return -1
    
    return dp[y]
```

#### 코드 상세 설명
- `if curr_number + n <= y:`
    - 현재 숫자(`curr_number`)에서 `n`을 더했을 때 목표 값(`y`)를 넘어서는지 확인하는 **범위 체크 조건**입니다.
    - 리스트 `dp`의 길이는 `y+1`이므로, 인덱스가 `y`를 초과하면 `IndexError`가 발생합니다.
    - 따라서 연산 결과가 유효한 인덱스 범위(`<= y`) 내에 있을 때만 `dp` 값을 갱신해야 합니다.
<br/>
<br/>
