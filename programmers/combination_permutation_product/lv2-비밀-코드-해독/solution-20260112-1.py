from itertools import combinations

def solution(n, q, ans):
    answer = 0
    
    ### intersection 으로 뽑아내기 위한 정답지 조합
    passwords = [set(n) for n in q]
    print(passwords)
    
    for number_combination in combinations(range(1, n+1), 5):
        is_matched = True
        curr_comb = set(number_combination)
        
        for should_match_password, should_match_cnt in zip(passwords, ans):
            matched_cnt = len(should_match_password.intersection(curr_comb))
            if matched_cnt != should_match_cnt:
                is_matched = False
                break
        
        if is_matched:
            answer += 1
    
    return answer

print(solution(10, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]], [2, 3, 4, 3, 3]))
print(solution(15, [[2, 3, 9, 12, 13], [1, 4, 6, 7, 9], [1, 2, 8, 10, 12], [6, 7, 11, 13, 15], [1, 4, 10, 11, 14]], [2, 1, 3, 0, 1]))