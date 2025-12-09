import sys
input = sys.stdin.readline

## solution
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

heights1 = [10,2,9,5]
heights2 = [10,13,9,5]

print(solution(heights1))
print(solution(heights2))
