from collections import deque

def solution(progresses, speeds):
    process_rates = deque(progresses)
    task_speeds = deque(speeds)
    
    time = 0
    task_cnt = 0
    
    answer = []
    while process_rates:
        if process_rates[0] + (time * task_speeds[0]) >= 100:
            process_rates.popleft()
            task_speeds.popleft()
            task_cnt += 1
        else:
            if task_cnt > 0:
                answer.append(task_cnt)        
                task_cnt = 0
            time += 1
            
    answer.append(task_cnt)
    
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
