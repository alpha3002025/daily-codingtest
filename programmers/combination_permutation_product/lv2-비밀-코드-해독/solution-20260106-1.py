from itertools import combinations

def solution(n, q, ans):
    passwords = [set(password) for password in q]
    
    answer = 0
    for curr_comb in combinations(range(1, n+1), 5):
        number_choice = set(curr_comb)
        is_answer = True
        
        for should_match_cnt, password in zip(ans, passwords):
            matched_cnt = len(password.intersection(number_choice))
            if matched_cnt != should_match_cnt:
                is_answer = False
                break
        
        if is_answer:
            answer += 1
    
    return answer

print(solution(10, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]], [2, 3, 4, 3, 3]))
print(solution(15, [[2, 3, 9, 12, 13], [1, 4, 6, 7, 9], [1, 2, 8, 10, 12], [6, 7, 11, 13, 15], [1, 4, 10, 11, 14]], [2, 1, 3, 0, 1]))