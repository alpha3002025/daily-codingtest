from itertools import permutations

def solution(n, submit):
    """
    프로그래머스 숫자 야구 (Interactive) 솔루션
    
    :param n: 최대 시도 횟수
    :param submit: 질문을 던지는 함수 (int -> "xS yB" str)
    :return: 정답 숫자 (int)
    """
    # 1. 1~9까지의 숫자로 구성된 모든 4자리 순열 생성 (총 3024개)
    nums = [str(i) for i in range(1, 10)]
    candidates = list(permutations(nums, 4))
    
    # 점수 계산 헬퍼 함수
    def calculate_score(secret, guess):
        strikes = 0
        balls = 0
        for i in range(4):
            if secret[i] == guess[i]:
                strikes += 1
            elif guess[i] in secret:
                balls += 1
        return strikes, balls

    while candidates:
        # 후보군 중 하나를 선택 (첫 번째 후보 사용)
        guess_tuple = candidates[0]
        guess_val = int("".join(guess_tuple))
        
        # 질문 던지기
        result_str = submit(guess_val)
        
        # 결과 파싱 "xS yB"
        s_part, b_part = result_str.split()
        real_s = int(s_part.replace('S', ''))
        real_b = int(b_part.replace('B', ''))
        
        # 정답인 경우 반환
        if real_s == 4:
            return guess_val
        
        # 가지치기 (Pruning)
        next_candidates = []
        for cand in candidates:
            if cand == guess_tuple:
                continue
                
            temp_s, temp_b = calculate_score(cand, guess_tuple)
            
            # 실제 결과와 일치하는 후보만 유지
            if temp_s == real_s and temp_b == real_b:
                next_candidates.append(cand)
        
        candidates = next_candidates
        
    return 0
