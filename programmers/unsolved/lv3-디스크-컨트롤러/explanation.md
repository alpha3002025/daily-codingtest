# 디스크 컨트롤러

## 문제 설명
작업 요청 `[요청시각, 소요시간]`이 들어옵니다.
평균 반환 시간(요청부터 종료까지 걸린 시간의 평균)을 최소화하도록 작업을 스케줄링하세요.
하드디스크는 한 번에 하나의 작업만 수행합니다.

## 문제 해결 전략

**SJF (Shortest Job First)** 스케줄링이 평균 대기 시간을 최소화합니다.
- 현재 시점에서 수행 가능한 작업들 중 **소요시간이 가장 짧은 작업**을 먼저 수행해야 합니다.
- **Priority Queue (Min Heap)**을 사용하여 소요시간이 짧은 작업을 관리합니다.

1. 요청 시각 순으로 작업 정렬.
2. 현재 시간 `time`보다 이전에 요청된 작업들을 모두 힙에 넣음 (소요시간 기준).
3. 힙에서 가장 짧은 작업을 꺼내 수행. (시간 업데이트, 반환 시간 누적)
4. 힙이 비어있는데 아직 남은 작업이 있다면, 시간을 다음 작업 요청 시간으로 점프.

## Python 코드

```python
import heapq

def solution(jobs):
    # 요청 시간 기준 정렬
    jobs.sort()
    
    curr_time = 0
    total_response_time = 0
    count = 0
    idx = 0
    n = len(jobs)
    
    pq = [] # (소요시간, 요청시간)
    
    while count < n:
        # 현재 시간까지 들어온 요청들을 큐에 넣기
        while idx < n and jobs[idx][0] <= curr_time:
            req_time, durations = jobs[idx]
            heapq.heappush(pq, (durations, req_time))
            idx += 1
            
        if pq:
            # 수행 가능한 작업 중 가장 짧은 것 수행
            durations, req_time = heapq.heappop(pq)
            curr_time += durations
            total_response_time += (curr_time - req_time)
            count += 1
        else:
            # 수행할 작업이 없으면 다음 작업 요청 시간으로 점프
            curr_time = jobs[idx][0]
            
    return total_response_time // n
```
