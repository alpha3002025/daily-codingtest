import sys
input = sys.stdin.readline

from bisect import bisect_left


N = int(input())
A = list(map(int, input().split()))

sublist = []

for num in A:
    pos = bisect_left(sublist, num)

    if pos == len(sublist):
        sublist.append(num)
    else:
        sublist[pos] = num

print(len(sublist))