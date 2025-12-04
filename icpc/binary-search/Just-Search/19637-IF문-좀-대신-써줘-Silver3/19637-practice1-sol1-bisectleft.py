import sys
from bisect import bisect_left

input = sys.stdin.readline

n, m = map(int, input().split())

titles = []
powers = []

for _ in range(n):
    title, power = input().split()
    power = int(power)
    titles.append(title)
    powers.append(power)

for _ in range(m):
    char_power = int(input())
    idx = bisect_left(powers, char_power)
    
    # char_power와 정확히 같은 값이 있으면 그 인덱스 사용
    # 없으면 char_power보다 큰 첫 번째 값의 인덱스 사용
    if idx < n and powers[idx] == char_power:
        print(titles[idx])
    else:
        # char_power보다 큰 첫 번째 값
        if idx < n:
            print(titles[idx])
        else:
            print(titles[n-1])