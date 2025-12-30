import math

def solution(k, d):
    answer = 0
    
    # x 좌표를 0, k, 2k, ... 순으로 증가
    for x in range(0, d + 1, k):
        # 피타고라스 정리로 가능한 최대 y 거리 계산
        max_dist_y = math.isqrt(d**2 - x**2)
        
        # 0부터 max_dist_y 사이의 k 배수 개수
        count_y = max_dist_y // k + 1
        answer += count_y
        
    return answer

print(solution(2, 4))
print(solution(1, 5))