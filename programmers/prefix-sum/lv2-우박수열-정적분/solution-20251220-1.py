def solution(k, ranges):
    ### 1) 우박수열 생성
    sequence = [k]
    while k > 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        sequence.append(k)
    
    n = len(sequence) - 1
    
    ### 2) 누적 면적 계산
    # prefix_area[i] : 0부터 i까지 구간의 누적 면적
    prefix_area = [0.0] * (n + 1)
    
    for i in range(n):
        area = (sequence[i] + sequence[i+1]) / 2 ## 삼각형
        prefix_area[i+1] = prefix_area[i] + area ## 이전 넓이 prefix_area[i] 에 삼각형을 더해서 구한다.
    
    answer = []
    ### 각 구간에서의 정적분 값들을 구한다.
    for a,b in ranges:
        start, end = a, n + b
        
        if start > end: ## 유효하지 않은 질문(query)일때 (문제 조건 참고)
            answer.append(-1.0)
        else:
            ## 각 구간의 정적분 결과
            result = prefix_area[end] - prefix_area[start]
            answer.append(result)
    
    return answer