from collections import deque

def solution(progresses, speeds):
    answer = []
    
    completed_queue = deque(progresses)
    speeds_queue = deque(speeds)
    
    task_cnt = 0
    time = 0
    
    while completed_queue:
        if completed_queue[0] + (time * speeds_queue[0]) >= 100:
            task_cnt += 1
            completed_queue.popleft()
            speeds_queue.popleft()
        else:
            if task_cnt > 0:
                answer.append(task_cnt)
                task_cnt = 0
            time += 1
    
    answer.append(task_cnt)
    
    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))