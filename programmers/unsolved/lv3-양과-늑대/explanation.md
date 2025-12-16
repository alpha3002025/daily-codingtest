# 양과 늑대

## 문제 설명
이진 트리 모양의 초원에 양(0)과 늑대(1)가 있습니다. 루트(0번 노드)에는 항상 양이 있습니다.
- 루트에서 출발하여 각 노드를 돌아다닙니다.
- 방문한 노드에 있는 양과 늑대가 당신을 따라옵니다. (한 번 방문하면 수집되고 빈 노드가 됨)
- 만약 **늑대의 수 >= 양의 수**가 되면, 모든 양이 잡아먹힙니다.
- 늑대에게 잡아먹히지 않도록 하면서 양을 최대로 모을 때, 그 양의 수를 구하세요.

## 문제 해결 전략

트리 탐색이지만, 한 번 방문한 곳을 다시 지나가서 아직 방문 안 한 다른 가지로 갈 수 있습니다.
즉, **"현재 방문 가능한 노드들의 집합"**을 상태로 관리하는 **DFS(백트래킹) 혹은 BFS**가 필요합니다.
- 상태: `(현재 위치, 양의 수, 늑대의 수, 다음에 방문 가능한 노드 목록)`
- 초기 상태: `(0, 1, 0, {0의 자식들})`
- 탐색:
  - 방문 가능한 목록(`next_nodes`)에서 하나(`next_node`)를 골라 이동합니다.
  - 이동하면 양/늑대 수가 갱신됩니다.
  - 갱신 후 `늑대 >= 양`이면 실패(이 경로는 더 이상 탐색 불가, 가지치기).
  - 아니면, `next_nodes`에서 `next_node`를 제거하고, `next_node`의 자식들을 추가하여 새로운 `next_nodes`를 만듭니다. 그리고 재귀 호출.

**주의점**: 단순 DFS가 아니라, "갈 수 있는 후보군"을 계속 들고 다니는 형태여야 합니다. 트리 순서대로가 아니라, 1번 갔다가 2번 안 가고 다시 0번 거쳐 3번 갈 수도 있기 때문입니다. 하지만 "방문 가능한 목록" 개념을 쓰면, 논리적으로 순간이동이 가능하다고 봐도 무방합니다. (이미 방문한 길은 비용 없이 다닐 수 있으므로)

## Python 코드

```python
def solution(info, edges):
    # 인접 리스트
    adj = [[] for _ in range(len(info))]
    for p, c in edges:
        adj[p].append(c)
        
    global max_sheep
    max_sheep = 0
    
    # dfs(현재노드, 양수, 늑대수, 갈수있는노드들)
    def dfs(node, sheep, wolf, possible_nodes):
        global max_sheep
        
        # 현재 노드 처리
        if info[node] == 0:
            sheep += 1
        else:
            wolf += 1
            
        # 가지치기: 늑대가 양을 잡아먹음
        if wolf >= sheep:
            return
        
        # 최댓값 갱신
        max_sheep = max(max_sheep, sheep)
        
        # 다음 이동 후보 갱신
        # 1. 기존 후보들에서 현재 노드 제거 (이미 왔으므로) - 사실 현재 노드는 possible_nodes에서 뽑아온 것.
        # 2. 현재 노드의 자식들을 후보에 추가
        # 리스트 복사 주의
        next_possible = list(possible_nodes)
        if node in next_possible:
            next_possible.remove(node) # 호출할 때 제거하고 줘도 됨. 여기선 편의상.
        
        for child in adj[node]:
            next_possible.append(child)
            
        # 갈 수 있는 모든 곳 시도
        for next_node in next_possible:
            # next_possible을 그대로 넘기면 안되고, 
            # 다음 재귀 단계에서는 '해당 next_node'가 제거되고 '그의 자식'이 추가된 상태여야 함.
            # -> 위에서 만든 next_possible은 '현재 스텝에서 갈 수 있는 모든 후보'임.
            # 재귀 안에서 리스트를 수정해 넘겨줘야 함.
            
            # 여기서 next_possible 복사해서 넘기기? 아님.
            # dfs 정의를 바꿈: dfs(sheep, wolf, possible_set)
            # 현재 노드 방문 처리는 그 안에서.
            pass
            
    # 다시 정리:
    # dfs(sheep, wolf, visit_candidates)
    
    ans = []
    
    def search(sheep, wolf, candidates):
        # 이번 단계에서 sheep 갱신
        ans.append(sheep)
            
        for next_node in candidates:
            n_sheep = sheep
            n_wolf = wolf
            
            if info[next_node] == 0: n_sheep += 1
            else: n_wolf += 1
            
            if n_wolf >= n_sheep: continue
            
            # 다음 후보균: 현재 후보군 - {next_node} + {next_node의 자식들}
            new_candidates = [c for c in candidates if c != next_node]
            new_candidates.extend(adj[next_node])
            
            search(n_sheep, n_wolf, new_candidates)

    
    # 초기 호출: 루트(0)은 이미 방문한 것으로 치거나, 
    # 후보군에 0을 넣고 시작하여 처리.
    # 후보군에 [0] 넣고 시작하면:
    # search(0, 0, [0]) -> 0번 방문 -> sheep=1, wolf=0 -> candidates=child(0)
    search(0, 0, [0]) # 초기: 양3, 늑0 아님. 아직 방문 전.
    
    return max(ans)
```
