# 네트워크

## 문제 설명
컴퓨터 개수 `n`, 연결 정보 `computers` (인접 행렬)가 주어집니다.
네트워크(연결된 컴포넌트)의 개수를 구하세요.

## 문제 해결 전략

**DFS** 또는 **BFS** 또는 **Union-Find**로 연결 요소를 셉니다.
가장 간단한 DFS/BFS로 방문하지 않은 노드를 만날 때마다 카운트를 증가시키고 연결된 모든 노드를 방문 처리합니다.

## Python 코드

```python
def solution(n, computers):
    visited = [False] * n
    count = 0
    
    def dfs(node):
        visited[node] = True
        for neighbor in range(n):
            if computers[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)
                
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1
            
    return count
```
