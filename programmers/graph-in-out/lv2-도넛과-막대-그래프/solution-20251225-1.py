def solution(edges):
    ## degree : 정점별 차수 계산 (key=node, value=[in,out])
    degree = {}
    
    for u,v in edges:
        if u not in degree: degree[u] = [0,0]
        if v not in degree: degree[v] = [0,0]
        
        degree[v][0] += 1 ## in
        degree[u][1] += 1 ## out
    
    created_node, donut_cnt, bar_cnt, eight_cnt = 0,0,0,0
    
    
    ## in_degree = 0, out_degree >= 2
    ## in_degree = 0 인 노드 중 out_degree 가 큰 것을 선택하거나 보편적 기준 사용
    ## 문제에서 그래프 수는 2개 이상, 따라서 out_degree >= 2
    for node, (in_degree, out_degree) in degree.items():
        if in_degree == 0 and out_degree >= 2:
            created_node = node
            break
    
    total_graphs = degree[created_node][1]
    
    for node, (in_degree, out_degree) in degree.items():
        if node == created_node:
            continue
        
        if out_degree == 0:
            bar_cnt += 1
            
        elif out_degree == 2:
            eight_cnt += 1
    
    donut_cnt = total_graphs - bar_cnt - eight_cnt
    return [created_node, donut_cnt, bar_cnt, eight_cnt]