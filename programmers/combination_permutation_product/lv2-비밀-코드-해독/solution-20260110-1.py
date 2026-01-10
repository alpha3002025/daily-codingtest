from itertools import combinations

def solution(n, q, ans):
    answer = 0
    
    try_list = [set(password) for password in q]
    
    for curr_comb in combinations(range(1,n+1), 5): ### 틀렸던 부분 (range(1,6), 5)를 하는 우를 범했었다.
        ### comb [k] 에 대한 각각의 처리
        current_choice = set(curr_comb)
        is_hit = True
        
        for should_match_cnt, tried_password in zip(ans, try_list):
            matched_cnt = len(current_choice.intersection(tried_password))
            if matched_cnt != should_match_cnt:
                is_hit = False
                break ### 내가 틀렸던 부분
        
        if is_hit:
            answer += 1
            
    return answer


print(solution(10, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]], [2, 3, 4, 3, 3]))
print(solution(15, [[2, 3, 9, 12, 13], [1, 4, 6, 7, 9], [1, 2, 8, 10, 12], [6, 7, 11, 13, 15], [1, 4, 10, 11, 14]], [2, 1, 3, 0, 1]))