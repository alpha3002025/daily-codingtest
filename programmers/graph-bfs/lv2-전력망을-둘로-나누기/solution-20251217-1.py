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