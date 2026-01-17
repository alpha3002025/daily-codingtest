def solution(A, B):
    # A는 오름차순 정렬
    A.sort()
    # B는 내림차순 정렬
    B.sort(reverse=True)
    
    answer = 0
    # zip으로 묶어서 순차적으로 곱함
    for a, b in zip(A, B):
        answer += a * b
        
    return answer


print(solution([1, 4, 2], [5, 4, 4]))
print(solution([1, 2], [3, 4]))