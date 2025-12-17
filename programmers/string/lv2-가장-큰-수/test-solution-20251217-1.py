def solution(numbers):
    # 1. 문자열 리스트로 변환
    numbers_str = list(map(str, numbers))
    
    # 2. 정렬 조건 설정
    # x*3을 하는 이유: 문자열 길이 확장하여 사전 순 비교
    # 예: '3', '30' -> '333', '303030'
    # '333'이 '303'보다 크므로 '3'이 앞에 옴 (큰 순서대로 정렬해야 하므로 reverse=True)
    numbers_str.sort(key=lambda x: x*3, reverse=True)
    
    # 3. 조인 후 반환
    answer = "".join(numbers_str)
    
    # 예외 처리: [0, 0, 0] -> "000"이 아니라 "0"이어야 함
    return str(int(answer))

print(solution([6, 10, 2]))
# print(solution([3, 30, 34, 5, 9]))
