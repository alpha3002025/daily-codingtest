import sys

N, T = map(int, sys.stdin.readline().split())


def binarysearch(bus_times):
    left, right = 0, len(bus_times) - 1  # right를 len-1로 설정
    
    while left < right:
        mid = (left + right) // 2  # 괄호 추가
        if bus_times[mid] >= T:
            right = mid
        else:
            left = mid + 1
    
    # left가 T 이상인 첫 번째 버스를 가리킴
    if left < len(bus_times) and bus_times[left] >= T:
        return bus_times[left] - T
    return float('inf')  # 탈 수 있는 버스가 없음


min_wait = float('inf')

for bus_idx in range(N):
    start_at, interval, num = map(int, sys.stdin.readline().split())
    
    # 버스 시간표 생성
    bus_times = [start_at + i * interval for i in range(num)]
    
    # T 이상인 가장 빠른 버스 찾기
    wait_time = binarysearch(bus_times)
    min_wait = min(min_wait, wait_time)

# 결과 출력
if min_wait == float('inf'):
    print(-1)
else:
    print(min_wait)