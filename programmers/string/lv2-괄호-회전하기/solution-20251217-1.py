def check_valid(s):
    stack = []
    
    map = {
        ')': '(',
        "}": '{',
        "]": '['
    }
    
    for c in s:
        if c in "({[": ## '(' 만 체크하는 문제가 아니다!! 조심!!
            stack.append(c)
        else:
            if not stack:
                return False
            prev = stack.pop()
            if c in map:
                ## stack 이 비어있지 않는 경우도 있기에 이 조건식을 사용하면 오답
                # if map[c] == prev: 
                #     return True
                if map[c] != prev:
                    return False
            
    return len(stack) == 0

def solution(s):
    answer = 0
    n = len(s)
    for i in range(n):
        ## 왼쪽 표를 보고서 코드를 치면 자연스럽게 써진다.
        slidded_str = s[i:] + s[:i]
        if check_valid(slidded_str):
            answer+=1
    return answer