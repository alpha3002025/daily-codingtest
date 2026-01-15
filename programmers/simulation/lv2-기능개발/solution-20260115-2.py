import math

def solution(progresses, speeds):
    answer = []
    
    duration_days = []
    for progress, speed in zip(progresses, speeds):
        days_left = math.ceil((100 - progress) / speed)
        duration_days.append(days_left)
    
    if not duration_days: return []
    
    prev_duration = duration_days[0]
    task_done = 1
    
    for i in range(1, len(duration_days)):
        curr_duration = duration_days[i]
        
        if curr_duration <= prev_duration:
            task_done += 1
        else:
            answer.append(task_done)
            task_done = 1
            prev_duration = curr_duration
            
    
    answer.append(task_done)
    
    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))