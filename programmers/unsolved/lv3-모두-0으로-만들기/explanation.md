# 모두 0으로 만들기

## 문제 설명
트리의 각 노드에 가중치 `a[i]`가 있습니다.
다음 연산을 반복하여 모든 가중치를 0으로 만들고자 합니다.
- 간선으로 연결된 두 노드 `u, v`를 골라 `a[u] += 1`, `a[v] -= 1` (또는 반대)을 수행합니다.
필요한 최소 연산 횟수를 구하세요. 불가능하면 -1.

## 문제 해결 전략

1. **불가능 조건**:
   - 연산은 가중치를 이동시키는 것과 같습니다. (총합 불변)
   - 따라서 **모든 가중치의 합이 0**이어야만 가능합니다.

2. **최소 연산 횟수 (탐욕법 + DFS)**:
   - 트리 구조이므로, **리프 노드(Leaf Node)**부터 처리하면 선택지를 줄일 수 있습니다.
   - 리프 노드의 가중치 $W$를 0으로 만들려면, 부모 노드와 $-W$만큼 주고받아야 합니다.
   - 즉, 리프 노드의 값을 부모에게 더해버리고(이동), 이동한 절대값 $|W|$만큼 연산 횟수에 추가합니다.
   - 이를 루트까지 반복합니다. (Post-order Traversal, 후위 순회)

## Python 코드

```python
import sys
sys.setrecursionlimit(300000)

def solution(a, edges):
    if sum(a) != 0:
        return -1
        
    n = len(a)
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    answer = 0
    visited = [False] * n
    
    # DFS (Post-order)
    def dfs(u):
        nonlocal answer
        visited[u] = True
        
        for v in adj[u]:
            if not visited[v]:
                # 자식 노드 처리 후 결과값 받기 (자식의 남은 가중치)
                child_weight = dfs(v)
                
                # 자식의 가중치를 0으로 만들기 위해 부모(u)로 넘김
                answer += abs(child_weight)
                a[u] += child_weight
                
        return a[u]
        
    dfs(0)
    
    return answer
```
