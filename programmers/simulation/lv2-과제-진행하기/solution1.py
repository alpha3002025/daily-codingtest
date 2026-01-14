def to_minute(time):
    h,m = map(int, time.split(":"))
    return h*60 + m


def solution(plans):
    answer = []
    tasks = []
    
    for name, start, playtime in plans:
        tasks.append([name, to_minute(start), int(playtime)])
    
    tasks.sort(key = lambda x: x[1])
    
    stack = []
    for i in range(len(tasks)-1):
        curr_name, curr_start, curr_playtime = tasks[i]
        next_start = tasks[i+1][1]
        
        curr_work_duration = next_start - curr_start
        
        if curr_playtime <= curr_work_duration: ## 다음 작업 시작 전에 현재 작업이 끝나면
            answer.append(curr_name)
            curr_free_time = curr_work_duration - curr_playtime
            
            while curr_free_time > 0 and stack:
                stopped_name, stopped_free_time = stack.pop()
                if stopped_free_time <= curr_free_time:
                    answer.append(stopped_name)
                    curr_free_time -= stopped_free_time
                else:
                    stack.append((stopped_name, stopped_free_time - curr_free_time))
                    curr_free_time = 0
        
        else: ## 다음 작업 시작 전에 현재 작업이 끝나지 못하면, 현재 작업을 넣어두고, 남은 시간도 함께 기록 
            stack.append((curr_name, curr_playtime - curr_work_duration))
    
    answer.append(tasks[-1][0])
    
    while stack:
        answer.append(stack.pop()[0])
    
    return answer