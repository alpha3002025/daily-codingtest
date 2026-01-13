from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []
    
    for window_size in course:
        candidates = []
        for ordered in orders:
            menu = sorted(ordered)
            for menu_combo in combinations(menu, window_size):
                menu_combo_str = "".join(menu_combo)
                candidates.append(menu_combo_str)
        
        counter = Counter(candidates)
        
        if counter:
            max_cnt = max(counter.values())
            if max_cnt >= 2:
                for menu, cnt in counter.items():
                    if cnt == max_cnt:
                        answer.append(menu)
    
    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))