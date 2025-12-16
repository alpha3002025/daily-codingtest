# 전력망을 둘로 나누기

## 문제 설명
$n$개의 송전탑이 전선으로 연결되어 하나의 트리(Tree) 형태를 이루고 있습니다. 이 중 전선 하나를 끊어서 전력망을 두 개의 독립된 네트워크로 나눌 때, 두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)를 최소로 만드는 문제입니다.

### 핵심 개념
1.  **그래프 탐색 (BFS/DFS)**: 전력망은 트리 구조이므로 그래프로 표현할 수 있습니다. 연결 상태를 인접 리스트 등으로 저장합니다.
2.  **완전 탐색 (Brute Force)**: 송전탑 개수 $n$이 최대 100으로 매우 작습니다. 따라서 "모든 전선을 하나씩 끊어보고", 그때마다 두 네트워크의 크기를 세어보는 방식을 사용해도 충분합니다.
    - 전선의 개수는 트리의 성질에 따라 $n-1$개입니다.
    - 각 전선을 끊을 때마다 BFS/DFS를 한 번 돌리면 $O(n)$이 걸리므로, 전체 시간 복잡도는 $O(n^2)$이 됩니다. ($100^2 = 10,000$ 연산은 매우 빠름)
3.  **트리 순회**: 하나를 끊었을 때 나뉘어진 한쪽 덩어리의 노드 개수를 $cnt$라고 하면, 나머지 덩어리의 개수는 $n - cnt$가 됩니다. 두 덩어리의 차이는 $|n - 2 \cdot cnt|$ 입니다.

## Python 풀이 (완전 탐색 + BFS)

```python
from collections import deque

def solution(n, wires):
    answer = n # 최댓값으로 초기화 (차이는 n보다 클 수 없음)
    
    # 간선 정보 하나를 제외한 그래프에서 BFS를 수행하여 노드 개수를 셈
    # wires[i] 번째 간선을 끊었다고 가정
    for i in range(len(wires)):
        # i번째 간선을 제외한 나머지 간선들로 그래프 생성
        graph = [[] for _ in range(n + 1)]
        for j in range(len(wires)):
            if i == j: continue # i번째 간선은 끊음
            v1, v2 = wires[j]
            graph[v1].append(v2)
            graph[v2].append(v1)
            
        # 1번 노드(임의의 노드)에서 시작하여 연결된 노드 개수(count) 구하기
        # 만약 1번 노드가 끊겨서 고립되었다면 자기 자신 1개만 카운트됨
        visited = [False] * (n + 1)
        q = deque([1]) # 항상 1번부터 탐색 시작
        visited[1] = True
        count = 1
        
        while q:
            curr = q.popleft()
            for nxt in graph[curr]:
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)
                    count += 1
        
        # 한쪽 전력망의 개수가 count이면, 다른 쪽은 n - count
        diff = abs(count - (n - count))
        answer = min(answer, diff)
        
    return answer
```

### 코드 설명
- `wires` 리스트를 `enumerate` 하거나 인덱스로 순회하면서, 현재 인덱스의 전선만 제외(`continue`)하고 나머지로 그래프를 구성합니다.
- `BFS`를 통해 임의의 노드(여기서는 1번)가 포함된 네트워크의 크기(`count`)를 구합니다.
- 전선을 끊으면 그래프는 두 개의 컴포넌트로 나뉘므로, 전체 $n$에서 한쪽 크기 `count`를 빼면 다른 쪽 크기가 나옵니다.
- 두 크기의 차이(`abs(n - 2*count)`)의 최솟값을 갱신합니다.
