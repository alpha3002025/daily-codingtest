from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)
    sorted_cnt = sorted(counter.values(), reverse = True)
    
    answer = 0
    for curr_cnt in sorted_cnt:
        if k > 0:
            k -= curr_cnt
            answer += 1
    
    return answer