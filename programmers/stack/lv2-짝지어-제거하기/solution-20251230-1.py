def solution(s):
    stack = []
    
    for char in s:
        # 스택이 비어있지 않고, 마지막 문자가 현재 문자와 같으면 제거
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
            
    # 스택이 비어있으면 모두 제거된 것
    if not stack:
        return 1
    else:
        return 0