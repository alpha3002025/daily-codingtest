# 등대

## 문제 설명
`n`개의 등대와 이들을 연결하는 뱃길이 트리 구조로 주어집니다.
어떤 뱃길을 이용하려면 양 끝 등대 중 적어도 하나는 켜져 있어야 합니다.
모든 뱃길을 안전하게 만들기 위해 켜야 하는 등대의 최소 개수를 구하세요.

## 문제 해결 전략

이 문제는 **트리에서의 DP (Tree DP)** 문제입니다.
이 문제는 "Vertex Cover (버텍스 커버)" 문제와 유사하지만, 트리는 이분 그래프이므로 다항 시간에 풀 수 있습니다.

**상태 정의**:
임의의 노드(예: 1번)를 루트로 하는 트리에서 DFS를 수행합니다.
각 노드 $u$에 대해:
- `dp[u][0]`: $u$가 꺼져 있을 때, 서브트리를 커버하기 위한 최소 비용.
- `dp[u][1]`: $u$가 켜져 있을 때, 서브트리를 커버하기 위한 최소 비용.

**점화식**:
$v$가 $u$의 자식일 때,
1. $u$가 켜져 있다면(`dp[u][1]`): 자식 $v$는 켜져 있어도 되고 꺼져 있어도 됩니다. 둘 중 작은 값을 취합니다.
   $$dp[u][1] = 1 + \sum_{v \in children(u)} \min(dp[v][0], dp[v][1])$$
   (1을 더하는 이유는 $u$ 자신을 켰기 때문)

2. $u$가 꺼져 있다면(`dp[u][0]`): 자식 $v$는 **반드시 켜져 있어야** 합니다. (그래야 $u-v$ 뱃길이 커버됨)
   $$dp[u][0] = 0 + \sum_{v \in children(u)} dp[v][1]$$

**최종 답**:
$\min(dp[root][0], dp[root][1])$

## Python 코드

```python
import sys
sys.setrecursionlimit(10**6)

def solution(n, lighthouse):
    # 인접 리스트 생성
    adj = [[] for _ in range(n + 1)]
    for u, v in lighthouse:
        adj[u].append(v)
        adj[v].append(u)
        
    # DP 테이블: [꺼짐, 켜짐]
    # dp[i][0] : i가 꺼졌을 때, dp[i][1] : i가 켜졌을 때
    dp = [[0, 0] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    
    def dfs(u):
        visited[u] = True
        
        # 리프 노드 처리 및 기본값
        dp[u][0] = 0
        dp[u][1] = 1
        
        for v in adj[u]:
            if not visited[v]:
                dfs(v)
                # u가 꺼짐 -> v는 반드시 켜짐
                dp[u][0] += dp[v][1]
                # u가 켜짐 -> v는 켜지든 꺼지든 최소값
                dp[u][1] += min(dp[v][0], dp[v][1])
                
    # 1번 노드를 루트로 설정하여 탐색
    dfs(1)
    
    return min(dp[1][0], dp[1][1])
```
