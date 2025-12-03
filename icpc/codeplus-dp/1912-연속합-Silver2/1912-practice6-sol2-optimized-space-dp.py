import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

curr_sum = A[0]
max_sum = A[0]

for i in range(1, N):
    curr_sum = max(A[i], curr_sum + A[i])
    max_sum = max(max_sum, curr_sum)

print(max_sum)