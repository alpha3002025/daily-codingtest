from itertools import combinations

def solution(n, q, ans):
    answer = 0
    
    queries = [set(attempts) for attempts in q]
    
    ## 1 ~ n 까지의 자연수 중 5개의 수를 뽑는다.
    for combination in combinations(range(1, n+1), 5):
        curr_comb = set(combination)
        
        is_possible = True
        
        ## ans 가 모두 일치하는지 검사
        for i in range(len(q)):
            should_match = ans[i]
            match_count = len(curr_comb.intersection(queries[i]))
            if match_count != should_match:
                is_possible = False
                break
        
        if is_possible:
            answer += 1
    
    return answer

print(solution(10, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]], [2, 3, 4, 3, 3]))
print(solution(15, [[2, 3, 9, 12, 13], [1, 4, 6, 7, 9], [1, 2, 8, 10, 12], [6, 7, 11, 13, 15], [1, 4, 10, 11, 14]], [2, 1, 3, 0, 1]))