from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

sublist = []

for number in A:
    pos = bisect_left(sublist, number)
    if pos == len(sublist):
        sublist.append(number)
    else:
        sublist[pos] = number

print(len(sublist))