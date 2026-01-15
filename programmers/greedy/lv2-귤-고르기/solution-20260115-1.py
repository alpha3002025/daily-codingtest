from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)
    
    answer = 0
    tangerine_reversed = sorted(counter.values(), reverse=True)
    for cnt in tangerine_reversed:
        if k > 0:
            k -= cnt
            answer += 1 
    
    return answer