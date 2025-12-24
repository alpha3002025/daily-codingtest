from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for wanted_len in course:
        candidates = []
        
        for order in orders:
            sorted_order = sorted(order)
            
            for menu_comb in combinations(sorted_order, wanted_len):
                candidates.append("".join(menu_comb))
            
        counter = Counter(candidates)
        
        if counter:
            max_cnt = max(counter.values())
            if max_cnt >= 2:
                for menu_name, menu_cnt in counter.items():
                    if menu_cnt == max_cnt:
                        answer.append(menu_name)
    
    return sorted(answer)