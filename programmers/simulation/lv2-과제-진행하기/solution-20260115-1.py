def to_minute(time):
    hh,mm = map(int, time.split(":"))
    return hh*60 + mm


def solution(plans):
    answer = []
    
    tasks = []
    for name, start, playtime in plans:
        tasks.append((name, to_minute(start), int(playtime)))
    tasks.sort(key = lambda x:x[1])
    
    stack = []
    ## 1 index 기반으로 푸는 prev, next 방식으로도 해보자 (나중에!! 😭🎡)
    for i in range(len(tasks)-1):
        next_task = tasks[i+1]
        next_start_time = next_task[1]
        
        curr_name, curr_start_time, curr_playtime = tasks[i]
        curr_period = next_start_time - curr_start_time
        
        if curr_playtime <= curr_period:
            answer.append(curr_name)
            curr_free_time = curr_period - curr_playtime
            
            while curr_free_time > 0 and stack: ## 남은 작업이 있는지 검사
                stopped_name, stopped_duration = stack.pop()
                
                if stopped_duration <= curr_free_time:
                    answer.append(stopped_name)
                    curr_free_time -= stopped_duration
                else:
                    stack.append((stopped_name, stopped_duration - curr_free_time))
                    curr_free_time = 0
        else:
            ## 현재 작업을 다음작업 시작 전에 끝내지 못했을때 남은 작업으로 등록한다.
            stack.append((curr_name, (curr_start_time + curr_playtime) - next_start_time))
            # stack.append((curr_name, curr_playtime - curr_period))
    
    answer.append(tasks[-1][0]) ## 위에서 n-2 까지만 순회했으므로 남은 작업인 n-1 요소 추가
    
    while stack:
        answer.append(stack.pop()[0])
    
    return answer


print(solution(["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]))
print(solution(["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]))
print(solution(["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]))