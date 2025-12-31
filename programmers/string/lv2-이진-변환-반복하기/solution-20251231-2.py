def solution(s):
    curr = s
    converting_cnt, removed_cnt = 0,0
    while int(curr, 10) > 1:
        ## 0 의 갯수
        zero_cnt = curr.count("0")
        
        ## 제거될 0 의 갯수 업데이트
        removed_cnt += zero_cnt
        
        ## c = 0 이 제거된 문자열의 길이
        c = len(curr) - zero_cnt
        
        ## c 를 이진수로 표현
        curr = bin(c)[2:]
        
        ## 변환 횟수
        converting_cnt += 1
    
    return [converting_cnt, removed_cnt]


print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))