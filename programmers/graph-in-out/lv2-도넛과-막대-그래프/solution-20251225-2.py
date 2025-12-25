def solution(edges):
    graph = {}
    for src, dest in edges:
        if src not in graph: graph[src] = [0,0] ## in, out
        if dest not in graph: graph[dest] = [0,0] ## in, out
        graph[src][1] += 1
        graph[dest][0] += 1
    
    ## result = 생성된노드, 도넛개수,막대개수,8개수
    
    ## (1) 생성된 노드
    created_node = None
    total_cnt = 0
    for vertex, (in_cnt, out_cnt) in graph.items():
        if in_cnt == 0 and out_cnt >= 2:
            created_node = vertex
            total_cnt = out_cnt
            break
    
    ## (3),(4) : 막대 개수, 8 개수
    bar_cnt, eight_cnt = 0,0
    for vertex, (in_cnt, out_cnt) in graph.items():
        if vertex == created_node:
            continue
        
        
        # if in_cnt == 1 and out_cnt == 0: ## 안되는 이유 : 새로운 정점에서 연결할 경우 in_cnt 가 늘어나기 때문
        if out_cnt == 0: ## 따라서 외부로 나가는 것만 체크해야 오류가 없다.
            bar_cnt += 1
        
        # if in_cnt >= 2 and out_cnt == 2: ## 안되는 이유 : 새로운 정점에서 연결할 경우 in_cnt 가 늘어나기 때문
        if out_cnt == 2: ## 따라서 외부로 나가는 것만 체크해야 오류가 없다.
            eight_cnt += 1
    
    ## (2) 도넛 개수
    donut_cnt = total_cnt - (bar_cnt + eight_cnt)
    
    return [created_node, donut_cnt, bar_cnt, eight_cnt]

print(solution([[2, 3], [4, 3], [1, 1], [2, 1]]))
print(solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]))
