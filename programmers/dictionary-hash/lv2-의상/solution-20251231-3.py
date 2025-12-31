from collections import Counter

def solution(clothes):
    counter = Counter([kind for name,kind in clothes])
    
    answer = 1
    for kind in counter:
        answer *= counter[kind] + 1
    
    return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))