import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

curr_max = A[0]
total_max = curr_max

for i in range(1,N):
    curr_max = max(A[i], curr_max + A[i])
    total_max = max(total_max, curr_max)

print(total_max)