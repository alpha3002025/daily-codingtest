from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    answer = []
    curr_time = 0
    curr_task = 0
    while progresses:
        if progresses[0] + (curr_time * speeds[0]) >= 100:
            progresses.popleft()
            speeds.popleft()
            curr_task += 1
        else:
            if curr_task != 0:
                answer.append(curr_task)
                curr_task = 0
            curr_time += 1
    
    answer.append(curr_task)
    
    return answer