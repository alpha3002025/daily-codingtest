from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for wanted_len in course:
        multi_menu_list = [] ### 틀렸던 부분
        for order in orders:
            sorted_order = sorted(order)
            
            for menu_comb in combinations(sorted_order, wanted_len):
                menu_str = "".join(menu_comb)
                multi_menu_list.append(menu_str)
        
        ### (start) 틀렸던 부분
        counter = Counter(multi_menu_list)

        if counter:
            max_cnt = max(counter.values())
            if max_cnt >= 2:
                for menu_name, cnt in counter.items():
                    if cnt == max_cnt:
                        answer.append(menu_name)
        ### (end) 틀렸던 부분
        ### 들여쓰기를 한단계 안쪽으로 했었다. combination 결과 카운팅이 order 별로 이뤄지도록 하고 있었다. 이렇게 하면 안되고 모든 order 에 대해 counting 을 한 결과를 wanted_len 에 대해서 산출해야 한다.
    
    return sorted(answer)