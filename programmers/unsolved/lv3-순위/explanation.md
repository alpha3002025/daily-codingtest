# 순위

## 문제 설명
`n`명의 선수가 있고, 경기 결과(`results`, `[A, B]`는 A가 B를 이김)가 주어집니다.
순위를 정확하게 알 수 있는 선수의 수를 구하세요.
순위를 알 수 있다 = **나를 제외한 나머지 모든 선수와의 승패 관계가 간접적으로라도 연결**되어 있다.
(A > B, B > C 이면 A > C)

## 문제 해결 전략

**플로이드-워셜 (Floyd-Warshall)** 알고리즘을 사용하여 모든 선수 간의 승패 관계를 파악합니다.
$N \le 100$ 이므로 $O(N^3)$ 가능합니다.

1. **그래프 초기화**:
   - `wins[i][j] = 1` if i wins j.
   - `dist[i][j]`로 해도 되고, 별도 `graph` 배열 사용해도 됨.

2. **플로이드-워셜**:
   - `k`를 거쳐갈 수 있는지 확인.
   - `if A 이김 k and k 이김 B: A 이김 B`

3. **순위 확정 조건**:
   - 어떤 선수 `i`에 대해, 다른 선수 `j`와의 관계가 명확해야 함.
   - 즉, `i`가 `j`를 이겼거나 (`graph[i][j]`), `j`가 `i`를 이겼거나 (`graph[j][i]`).
   - 모든 `j (!= i)`에 대해 승패 중 하나가 결정되어 있으면 순위를 알 수 있습니다.
   - `count(Graph[i]) + count(Graph 역방향[i]) == n - 1`

## Python 코드

```python
def solution(n, results):
    # win graph
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    
    for u, v in results:
        graph[u][v] = True
        
    # Floyd-Warshall
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                # i가 k를 이기고, k가 j를 이기면 -> i가 j를 이김
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = True
                    
    answer = 0
    for i in range(1, n + 1):
        count = 0
        for j in range(1, n + 1):
            if i == j: continue
            # i가 j를 이겼거나, j가 i를 이겼거나 (승패 관계 확인됨)
            if graph[i][j] or graph[j][i]:
                count += 1
        
        if count == n - 1:
            answer += 1
            
    return answer
```
