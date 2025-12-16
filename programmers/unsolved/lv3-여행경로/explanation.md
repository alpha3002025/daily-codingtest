# 여행경로

## 문제 설명
주어진 항공권(`tickets`)을 모두 이용하여 여행 경로를 짭니다.
항상 "ICN" 공항에서 출발합니다.
가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
모든 도시를 방문해야 합니다 (모든 티켓 사용).

## 문제 해결 전략

**DFS (깊이 우선 탐색)**을 사용합니다.
- 모든 티켓을 사용해야 하므로, 티켓 개수만큼 깊이 들어가야 합니다.
- 특정 공항에서 갈 수 있는 도착지들이 여러 개라면, **알파벳 순으로 정렬**하여 먼저 방문합니다.
- 방문하다가 끊기면(모든 티켓을 못 썼는데 갈 곳이 없음) 백트래킹합니다.
- 스택이나 재귀를 사용합니다.

## Python 코드

```python
from collections import defaultdict

def solution(tickets):
    # 인접 리스트 구성
    routes = defaultdict(list)
    for start, end in tickets:
        routes[start].append(end)
        
    # 알파벳 역순 정렬 (스택에서 꺼낼 때 알파벳 순이 되도록)
    for key in routes:
        routes[key].sort(reverse=True)
        
    stack = ["ICN"]
    path = []
    
    while stack:
        top = stack[-1]
        
        # 갈 곳이 없거나 티켓을 다 썼으면 경로에 추가
        if top not in routes or not routes[top]:
            path.append(stack.pop())
        else:
            # 갈 곳이 있으면 하나 꺼내서 스택에 넣음 (이동)
            stack.append(routes[top].pop())
            
    # 스택 처리 순서상 역순으로 경로가 만들어지므로 다시 뒤집음
    return path[::-1]
```
