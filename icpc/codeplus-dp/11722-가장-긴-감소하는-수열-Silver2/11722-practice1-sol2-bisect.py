import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# 가장 긴 감소하는 부분 수열(LDS)을 구하는 O(N log N) 방법
# 기본적으로 bisect는 오름차순 정렬을 유지하므로, 
# 1. 수열을 뒤집어서 가장 긴 증가하는 부분 수열(LIS)을 구하거나
# 2. 모든 원소의 부호를 반대로 뒤집어서 LIS를 구하면 됩니다.

# 여기서는 수열을 뒤집어서 LIS를 구하는 방식을 사용합니다.
A.reverse()

lis = []

for num in A:
    # num이 들어갈 위치 찾기 (lower_bound)
    idx = bisect_left(lis, num)
    
    if idx == len(lis):
        # lis의 모든 원소보다 크다면 끝에 추가
        lis.append(num)
    else:
        # 해당 위치의 원소를 num으로 교체 (더 작은 값으로 갱신하여 뒤에 더 많은 수를 붙일 가능성을 높임)
        lis[idx] = num

print(len(lis))
