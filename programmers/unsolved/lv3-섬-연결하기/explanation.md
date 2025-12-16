# 섬 연결하기

## 문제 설명
`n`개의 섬 사이에 다리를 건설하는 비용 `costs`가 주어집니다.
모든 섬을 연결하는 최소 비용을 구하세요.

## 문제 해결 전략

**최소 신장 트리 (MST)** 문제입니다.
**크루스칼 (Kruskal)** 알고리즘이 구현하기 편합니다.
1. 비용 기준으로 간선 정렬.
2. 비용이 낮은 순서대로 간선을 선택하되, 사이클을 형성하지 않는 경우에만 연결 (Union-Find 사용).
3. 연결된 간선 수가 `n-1`개가 되면 종료.

## Python 코드

```python
def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b):
        rootA = find(a)
        rootB = find(b)
        if rootA < rootB:
            parent[rootB] = rootA
        else:
            parent[rootA] = rootB
            
    total_cost = 0
    edges = 0
    
    for u, v, cost in costs:
        if find(u) != find(v):
            union(u, v)
            total_cost += cost
            edges += 1
            if edges == n - 1:
                break
                
    return total_cost
```
