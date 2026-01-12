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