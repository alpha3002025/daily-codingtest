import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1] * N
prev = [-1] * N

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1 ## (1)
            # dp[i] = max(dp[i], dp[j]+1)
            prev[i] = j


max_length = max(dp)
max_index = dp.index(max_length)

curr = max_index
sublist = []

while curr != -1:
    sublist.append(A[curr])
    curr = prev[curr]

print(f"{max_length}")
sublist.reverse()
print(*sublist)
