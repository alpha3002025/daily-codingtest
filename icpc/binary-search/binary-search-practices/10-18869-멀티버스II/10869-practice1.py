import sys
from collections import defaultdict

M, N = map(int, sys.stdin.readline().split())
universe = defaultdict(int)

for planet_idx in range(M):
    planets = list(map(int, sys.stdin.readline().split()))
    sorted_planets = sorted(list(set(planets))) ## set 으로 변환후 중복 제거 -> list 로 변환 -> 오름차순 정렬
    rank_planets = {sorted_planets[rank]: rank for rank in range(len(sorted_planets))}

    vector = tuple([rank_planets[planet] for planet in planets])
    print("")
    print(f"vector = {vector}")
    universe[vector] += 1
    print(f"universe = {universe}")

sum = 0
for i in universe.values():
    sum += (i*(i-1)) // 2

print(f"{sum}")