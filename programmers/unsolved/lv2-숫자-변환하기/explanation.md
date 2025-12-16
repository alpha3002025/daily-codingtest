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

## 코드 (Python)

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
