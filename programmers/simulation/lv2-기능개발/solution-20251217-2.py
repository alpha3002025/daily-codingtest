import math

def solution(progresses, speeds):
    answer = []
    
    # 1. 각 기능별 배포 가능일까지 남은 일수 계산
    days_left = []
    for p, s in zip(progresses, speeds):
        # 올림 계산: (목표 - 현재 + 속도 - 1) // 속도
        # 또는 math.ceil((100 - p) / s)
        day = math.ceil((100 - p) / s)
        days_left.append(day)
        
    # 예: days_left = [7, 3, 9]
    # 7일 걸리는 기능 배포 때 3일 걸리는 것도 같이 나감 (2개)
    # 9일 걸리는 기능은 따로 나감 (1개)
    
    # 2. 배포 그룹 묶기
    if not days_left:
        return []
        
    prev_max = days_left[0]
    count = 1
    
    for i in range(1, len(days_left)):
        curr = days_left[i]
        
        if prev_max >= curr:
            # 앞 기능보다 빨리 끝나거나 같이 끝나면 묶음 배포
            count += 1
        else:
            # 앞 기능보다 오래 걸리면, 앞 그룹 정산하고 새로 시작
            answer.append(count)
            prev_max = curr
            count = 1
            
    # 마지막 그룹 추가
    answer.append(count)
    
    return answer