def solution(n):
    r,c = -1, 0
    curr = 1
    triangle = [[0] * (i+1) for i in range(n)]
    for turn in range(n):
        for _ in range(turn, n):
            if turn % 3 == 0:
                r += 1
            elif turn % 3 == 1:
                c += 1
            elif turn % 3 == 2:
                r -= 1
                c -= 1
            
            triangle[r][c] = curr
            curr += 1
    
    answer = []
    for row in triangle:
        for n in row:
            answer.append(n)
    return answer

print(solution(4))
print(solution(5))
print(solution(6))