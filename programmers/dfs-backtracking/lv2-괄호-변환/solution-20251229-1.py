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

def reverse_bracket(s):
    table = str.maketrans("()", ")(")
    return s.translate(table)

def solution(p):
    if not p:
        return ""
    
    u,v = split_uv(p)
    # print(f"u: {u}, v: {v}")

    if is_correct(u):
        return u + solution(v)
    
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        
        ## u 의 첫번째 문자, 마지막 문자를 제거한 안쪽 문자
        u = u[1:-1]
        
        ## 해당 문자열에 대해 괄호 방향 뒤집기
        answer += reverse_bracket(u)
        return answer


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))