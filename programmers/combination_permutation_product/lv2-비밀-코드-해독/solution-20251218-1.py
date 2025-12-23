from itertools import combinations

def solution(n, q, ans):
    answer = 0
    
    ## 사용자의 입력 시도 숫자열의 set 들 (교집합 연산을 위해 set 으로 변환)
    queries = [set(attempt) for attempt in q]
    
    ## 1 ~ n 까지 5개의 수를 뽑아서 임의의 수를 조합으로 생성
    for combination in combinations(range(1, n+1),5):
        combo_set = set(combination) ## 교집합 연산을 위해 set 으로 변환
        is_possible =  True
        
        for i in range(len(q)):
            ## combo_set 과 queries[i] (=i번째 query) 를 비교해 일치하는 개수 카운트
            match_count = len(combo_set.intersection(queries[i]))
            if match_count != ans[i]:
                is_possible = False
                break
        
        if is_possible:
            answer += 1
    
    return answer

print(solution(10, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]], [2, 3, 4, 3, 3]))
print(solution(15, [[2, 3, 9, 12, 13], [1, 4, 6, 7, 9], [1, 2, 8, 10, 12], [6, 7, 11, 13, 15], [1, 4, 10, 11, 14]], [2, 1, 3, 0, 1]))
