"""
{100, 100}
{180x2, 360x1}
{180x4, 360x2}
{180x3, 270x2}
"""

from collections import Counter

def solution(weights):
    counter = Counter(weights)
    answer = 0
    
    for k,v in counter.items():
        if k > 1:
            answer += v * (v-1) // 2
    
    for weight in counter:
        if weight % 2 == 0 and (weight * 3 // 2) in counter:
            answer += counter[weight] * counter[weight*3//2]
        if (weight*2) in counter:
            answer += counter[weight] * counter[weight*2]
        if weight % 3 == 0 and (weight * 4 // 3) in counter:
            answer += counter[weight] * counter[weight*4//3]
    
    return answer