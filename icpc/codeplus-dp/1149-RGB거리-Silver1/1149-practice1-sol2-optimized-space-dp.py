n = int(input())
prev = list(map(int, input().split()))

for _ in range(n-1):
    cost = list(map(int, input().split()))
    curr = [0] * 3
    curr[0] = cost[0] + min(prev[1], prev[2])
    curr[1] = cost[1] + min(prev[0], prev[2])
    curr[2] = cost[2] + min(prev[0], prev[1])
    prev = curr

print(min(prev))