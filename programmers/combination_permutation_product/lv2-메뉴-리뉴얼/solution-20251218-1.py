from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for k in course:
        candidates = []
        for order in orders:
            ## 메뉴 구성 통일을 위해 정렬 ("XY", "YX" -> "XY")
            sorted_order = sorted(order)
            
            ## 주문에 대해 길이 k 인 조합을 모두 생성
            for combination in combinations(sorted_order, k):
                candidates.append("".join(combination))
        
        ## 길이 k 인 모든 조합의 빈도수 산출
        counter = Counter(candidates)
        
        ## 가장 많이 주문된 횟수 찾기 + 2번 미만일 경우는 제외
        if counter:
            max_count = max(counter.values())
            if max_count >= 2:
                for menu, cnt in counter.items():
                    if cnt == max_count:
                        answer.append(menu)
    # 결과를 알파벳 오름차순으로 정렬
    return sorted(answer)