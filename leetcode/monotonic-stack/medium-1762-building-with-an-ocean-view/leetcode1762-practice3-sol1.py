def solution(heights):
    stack = []
    answer = []

    for i in reversed(range(len(heights))):
        while stack and heights[stack[-1]] < heights[i]:
            stack.pop()
        
        if not stack:
            answer.append(i)

        stack.append(i)
    
    return list(reversed(answer))

heights1 = [4,2,3,1]
heights2 = [4,3,2,1]

print(solution(heights1))
print(solution(heights2))