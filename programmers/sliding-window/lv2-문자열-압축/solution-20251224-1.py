def solution(s):
    n = len(s)
    
    # 문자열의 길이가 1 이면 압축 불가, 길이는 1
    if n == 1: return 1
    
    min_length = n ## 압축 안했을때를 초기값으로 지정
    
    ## 자르는 단위 : unit = 1 ~ n//2
    for unit in range(1, n//2 +1):
        compressed = ""
        prev = s[:unit]
        count = 1
        
        ## unit 간격으로 순회
        for i in range(unit, n, unit):
            curr = s[i:i+unit]
            
            if prev == curr:
                count += 1
            else:
                ## 이전까지의 패턴 기록
                if count > 1:
                    compressed += str(count) + prev
                else:
                    compressed += prev
                
                ## 초기화
                prev = curr
                count = 1
        
        ## 마지막 조각 처리
        if count > 1:
            compressed += str(count) + prev
        else:
            compressed += prev
        
        min_length = min(min_length, len(compressed))
    
    return min_length


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))