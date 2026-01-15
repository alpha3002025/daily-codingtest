from collections import deque

def solution(progresses, speeds):
    answer = []
    
    progress_queue = deque(progresses)
    speed_queue = deque(speeds)
    
    days = 0
    task_cnt = 0
    while progress_queue:
        if progress_queue[0] + speed_queue[0] * days >= 100:
            progress_queue.popleft()
            speed_queue.popleft()
            task_cnt += 1
        else:
            if task_cnt > 0:
                answer.append(task_cnt)
                task_cnt = 0
            days += 1
    
    answer.append(task_cnt)
    
    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))