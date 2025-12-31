def solution(s):
    loop_count = 0
    removed_zeros = 0
    
    while s != "1":
        loop_count += 1
        
        # 1. 0의 개수 세기 및 제거 카운트 누적
        count_zero = s.count('0')
        removed_zeros += count_zero
        
        # 2. 0을 제거하고 남은 1의 개수 -> 길이
        length_one = len(s) - count_zero
        
        # 3. 길이를 2진수 문자열로 변환
        s = bin(length_one)[2:]
        
    return [loop_count, removed_zeros]

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))
