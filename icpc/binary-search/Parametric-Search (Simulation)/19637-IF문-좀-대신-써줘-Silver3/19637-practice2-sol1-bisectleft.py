from bisect import bisect_left

import sys
input = sys.stdin.readline

N,M = map(int, input().split())

rank_names = []
rank_limits = []

for i in range(N):
    args = input().split()
    rank_names.append(args[0])
    rank_limits.append(int(args[1]))

for _ in range(M):
    curr_power = int(input())
    i = bisect_left(rank_limits, curr_power)

    if i < N and rank_limits[i] == curr_power:
        print(rank_names[i])
    else:
        if i < N:
            print(rank_names[i])
        else:
            print(rank_names[N-1])