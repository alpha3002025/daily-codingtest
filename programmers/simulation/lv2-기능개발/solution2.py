import math

def solution(progresses, speeds):
    duration_days = []
    
    for p,s in zip(progresses, speeds):
        days = math.ceil((100 - p) / s)
        duration_days.append(days)
    
    if not duration_days: return []

    answer = []
    
    prev_duration = duration_days[0]
    cnt = 1 ## duation_days[0] 을 prev_duration 으로 이미 포함시켰으므로 cnt = 1 부터 시작
    
    for i in range(1, len(duration_days)):
        curr_duration = duration_days[i]
        
        if curr_duration <= prev_duration: ## (1)
            cnt += 1 ## 현재 작업도 같이 배포된다.
            
        else: ## 
            answer.append(cnt)
            prev_duration = curr_duration
            cnt = 1
    
    ## (1) 이 다 끝나지 않은채로 끝나기에 아래 구문을 실행해서 마무리
    answer.append(cnt) ## 마지막 그룹 추가 !!
    
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
