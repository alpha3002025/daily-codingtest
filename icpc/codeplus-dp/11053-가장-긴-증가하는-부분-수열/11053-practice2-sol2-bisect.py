"""
11053 : 증가수열에서 오름차순 연속 부분수열 중 가장 큰 '길이'
11055 : 증가수열에서 오름차순 연속 부분수열 중 가장 큰 '합'
11722 : 감소수열에서 내림차순 연속 부분수열 중 가장 큰 '길이'
"""

from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

sublist = []
for num in A:
    pos = bisect_left(sublist, num)
    if pos == len(sublist):
        sublist.append(num)
    else:
        sublist[pos] = num

print(f"{len(sublist)}")