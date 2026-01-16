def split_uv(s):
    left,right = 0,0
    
    for i in range(len(s)):
        if s[i] == '(':
            left += 1
        else:
            right += 1
        
        if left == right:
            return s[:i+1], s[i+1:]
    return s, ""


def is_valid(s):
    stack = []
    
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                return False
            stack.pop()
    return False if stack else True


def replace(s):
    table = s.maketrans('()',')(')
    return s.translate(table)


def solution(p):
    ## (1) 1번 요구사항
    if p == '' or len(p.replace(' ', '')) == 0:
        return ''
    ## (2) 2번 요구사항
    u,v = split_uv(p)
    
    ## (3) 
    if is_valid(u):
        return u + solution(v)
    else:
        empty_str = ''
        empty_str += '('
        empty_str += solution(v)
        empty_str += ')'
        
        return empty_str + replace(u[1:-1])