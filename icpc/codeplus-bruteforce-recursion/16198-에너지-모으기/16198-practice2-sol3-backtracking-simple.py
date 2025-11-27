def dfs(w):
    if len(w) == 2:
        return 0
    
    result = 0
    for i in range(1, len(w)-1):
        energy = w[i-1] * w[i+1]
        result = max(result, energy + dfs(w[:i]+w[i+1:]))
    
    return result

N = int(input())
W = list(map(int, input().split()))
print(dfs(W))