import sys
from bisect import bisect_right

input = sys.stdin.readline

n, m = map(int, input().split())

titles = []
powers = []

for _ in range(n):
    title, power = input().split()
    titles.append(title)
    powers.append(int(power))

for _ in range(m):
    char_power = int(input())
    # char_power 이하의 값 중 가장 오른쪽 위치의 다음 인덱스
    # = char_power보다 큰 첫 번째 값의 인덱스
    idx = bisect_right(powers, char_power)
    print(titles[idx])