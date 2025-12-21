def solution(num, total):
    # 0 ~ num-1 까지의 합 (등차수열 합 공식의 뒷부분)
    # sum(0..n-1) = n*(n-1)/2
    d_sum = num * (num - 1) // 2
    
    # total에서 d_sum을 뺀 후 num으로 나누면 시작 값 x가 나옴
    start = (total - d_sum) // num
    
    # start부터 num개의 연속된 정수 리스트 생성
    return [i for i in range(start, start + num)]

print(solution(3, 12))