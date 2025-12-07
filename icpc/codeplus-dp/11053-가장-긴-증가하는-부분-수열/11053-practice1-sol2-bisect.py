"""
11053 : 증가수열에서 오름차순 연속 부분수열 중 가장 큰 '길이'
11055 : 증가수열에서 오름차순 연속 부분수열 중 가장 큰 '합'
11722 : 감소수열에서 내림차순 연속 부분수열 중 가장 큰 '길이'
"""

from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))

# lis[i]: 길이가 i+1인 증가 부분 수열의 마지막 원소 중 최솟값
lis = []

for num in arr:
    # num이 들어갈 위치 찾기 (lower_bound)
    pos = bisect_left(lis, num)
    
    if pos == len(lis):
        # num이 lis의 모든 원소보다 크면 추가
        lis.append(num)
    else:
        # 해당 위치의 값을 num으로 갱신
        lis[pos] = num

print(len(lis))