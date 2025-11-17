import sys
input = sys.stdin.readline

N,M = map(int, input().split())

# 친구 관계를 set 으로 저장 (O(1) 조회)
friends = [set() for _ in range(N+1)]
edges = []

for _ in range(M):
    a,b = map(int, input().split())
    friends[a].add(b)
    friends[b].add(a)

min_result = float('inf')

for a,b in edges:
    if len(friends[a] < len(friends[b])):
        small, large = a,b
    else:
        small, large = b,a
    
    for c in friends[small]:
        if c in friends[large]:
            total = len(friends[a]) + len(friends[b]) + len(friends[c]) - 6
            min_result = min(min_result, total)


if min_result == float('inf'):
    print(-1)
else:
    print(min_result)
