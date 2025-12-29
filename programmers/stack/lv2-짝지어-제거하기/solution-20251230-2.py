def solution(s):
    stack = []
    
    for curr in range(len(s)):
        if stack and s[stack[-1]] == s[curr]:
            stack.pop()
        else:
            stack.append(curr)

    return 1 if not stack else 0