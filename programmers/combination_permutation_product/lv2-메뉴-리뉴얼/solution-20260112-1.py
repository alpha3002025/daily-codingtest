from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for window_size in course:
        candidates = []
        for menu_items in orders:
            ## 메뉴 구성 통일을 위해 정렬 ("XY", "YX" -> "XY")
            sorted_items = sorted(menu_items)
            for menu_comb in combinations(sorted_items, window_size):
                candidates.append("".join(menu_comb))
        
        ## window_size 에 대한 메뉴 조합 카운팅
        counter = Counter(candidates)

        if counter:
            max_count = max(counter.values())
            if max_count >= 2:
                for menu_name, menu_cnt in counter.items():
                    if menu_cnt == max_count:
                        answer.append(menu_name)
    
    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))