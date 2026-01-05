def solution(n, s, a, b, fares):
    INF = 10000000
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        dist[i][i] = 0
        
    for u, v, w in fares:
        dist[u][v] = w
        dist[v][u] = w
        
    # Floyd-Warshall
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    # 최소 비용 찾기
    min_fare = INF
    
    # 합승 지점 k (1~n)
    for k in range(1, n + 1):
        cost = dist[s][k] + dist[k][a] + dist[k][b]
        if cost < min_fare:
            min_fare = cost
            
    return min_fare

강