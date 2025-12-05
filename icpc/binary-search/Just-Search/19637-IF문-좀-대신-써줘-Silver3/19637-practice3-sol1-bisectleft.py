from bisect import bisect_left

import sys
input = sys.stdin.readline

N,M = map(int, input().split())

rank_names = []
rank_limits = []

for i in range(N):
    rank_name, rank_value = input().split()
    rank_names.append(rank_name)
    rank_limits.append(int(rank_value))


for _ in range(M):
    curr = int(input())

    idx = bisect_left(rank_limits, curr)

    if idx < N:
        if rank_limits[idx] == curr:
            print(rank_names[idx])
        else:
            print(rank_names[idx])
    else:
        print(rank_limits[N-1])
