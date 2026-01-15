def to_minute(time):
    h,m = map(int, time.split(":"))
    return h*60 + m


def solution(plans):
    answer = []
    tasks = []
    
    for name, start, playtime in plans:
        tasks.append((name, to_minute(start), int(playtime)))
    tasks.sort(key=lambda x:x[1])
    
    stack = []
    for i in range(len(tasks)-1):
        curr_name, curr_start_time, curr_playtime = tasks[i]
        next_start_time = tasks[i+1][1]
        
        curr_work_duration = next_start_time - curr_start_time
        
        if curr_playtime <= curr_work_duration:
            answer.append(curr_name)
            curr_free_time = curr_work_duration - curr_playtime
            
            while curr_free_time > 0 and stack: ## 남은시간이 있고 && 남아있는 작업이 있으면
                stopped_name, stopped_playtime = stack.pop()
                if stopped_playtime <= curr_free_time:
                    answer.append(stopped_name)
                    curr_free_time -= stopped_playtime
                else:
                    stack.append((stopped_name, stopped_playtime - curr_free_time))
                    curr_free_time = 0
                
            
        else: ## curr_playtime 이 더 커서, 다음작업 시작 전에 현재 작업이 끝나지 않으면, 
              ## 현재 작업을 넣어두고, 남은 시간도 함께 기록
            stack.append((curr_name, curr_playtime - curr_work_duration))
    
    ## 마지막 과제를 완료 처리
    answer.append(tasks[-1][0])
    
    while stack: ## 남은 모든 작업들을 추가
        answer.append(stack.pop()[0])
    
    return answer


print(solution(["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]))
print(solution(["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]))
print(solution(["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]))
