def split_uv(p):
    count_l = 0
    count_r = 0
    for i in range(len(p)):
        if p[i] == '(':
            count_l += 1
        else:
            count_r += 1
        
        if count_l == count_r:
            return p[:i+1], p[i+1:]
    return p,""


def reverse_bracket(s):
    table = str.maketrans("()", ")(")
    return s.translate(table)


def is_correct(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0


def solution(p):
    ## 문제에 적혀있는 절차를 그대로 따라서 구현
    ## 1. 빈문자열
    if not p:
        return ""
    
    ## 2. u,v 분리
    u,v = split_uv(p)
    
    ## 3. u가 올바른 괄호 문자열일때
    if is_correct(u):
        return u + solution(v)
    
    ## 4. u 가 올바른 문자열이 아닐 경우
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        
        ## u 의 첫번째문자, 마지막 문자를 제거한 안쪽 문자
        u = u[1:-1]
        ## 해당 문자열에 대해 괄호 방향 뒤집기
        answer += reverse_bracket(u)
        return answer