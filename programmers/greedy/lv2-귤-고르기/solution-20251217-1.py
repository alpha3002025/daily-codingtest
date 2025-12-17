from collections import Counter

def solution(k, tangerine):
    counts = Counter(tangerine)
    
    sorted_counts = sorted(counts.values(), reverse=True)
    
    answer = 0
    curr_count = 0
    
    # print(f"sorted_counts = {sorted_counts}")
    for count in sorted_counts:
        curr_count += count
        answer += 1
        
        if curr_count >= k:
            break
    
    return answer