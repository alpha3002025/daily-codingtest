open_close = {
    '(': ')',
    '{': '}',
    '[': ']'
}

def check_valid(s):
    stack = []
    
    for c in s:
        if c in ['(', '{', '[']:
            stack.append(c)
        else:
            if not stack:
                return False
            
            prev = stack.pop()
            if open_close[prev] != c:
                return False
            
    return len(stack) == 0


def solution(s):
    answer = 0
    
    n = len(s)
    if n == 0:
        return 0
    
    for i in range(n):
        rotated = s[i:] + s[:i]
        if check_valid(rotated):
            answer += 1
    
    return answer
