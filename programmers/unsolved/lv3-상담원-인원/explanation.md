# 상담원 인원

## 문제 설명
`k`개의 상담 유형이 있고 `n`명의 상담원(멘토)이 있습니다.
각 유형별로 상담원이 적어도 1명 이상 배정되어야 합니다.
참가자들의 상담 요청(시간, 기간, 유형)이 주어질 때, 모든 참가자의 상담 대기 시간을 최소화하도록 멘토를 배정하고 그 때의 최소 대기 시간을 구하세요.

## 문제 해결 전략

상담 유형의 수 `k`는 최대 5, 멘토 수 `n`은 최대 20으로 매우 작습니다.
따라서 **완전 탐색**과 **우선순위 큐(Heap)**를 이용한 시뮬레이션이 가능합니다.

1. **멘토 배정 조합 탐색**:
   - 각 유형에 최소 1명을 배치하고 남은 `n-k`명을 `k`개 유형에 분배하는 모든 경우를 찾습니다.
   - `itertools.combinations_with_replacement` 또는 `product`를 활용.

2. **유형별 대기 시간 계산**:
   - 특정 유형에 상담원 $m$명이 배정되었을 때의 총 대기 시간을 계산하는 함수를 만듭니다.
   - 각 참가자의 `(도착시간, 상담시간)`을 순회하며, 상담원들의 `종료 시각`을 Min-Heap으로 관리합니다.
   - 가장 빨리 끝나는 상담원을 Pop하고, 현재 참가자의 요청을 처리한 뒤 종료 시각을 Push합니다.

3. **최적화**:
   - $N$이 작으므로 매번 시뮬레이션해도 통과 가능하지만, 미리 `Cost[유형][인원수]` 테이블을 만들어두면 더 빠릅니다.
   - `Cost[type_id][count]` = 해당 유형에 `count`명을 배정했을 때의 총 대기 시간.
   - 모든 분배 조합에 대해 $\sum Cost[t][c_t]$ 를 계산하여 최솟값을 찾습니다.

## Python 코드

```python
import heapq
from itertools import combinations_with_replacement

def solution(k, n, reqs):
    # 1. 유형별로 요청 분리
    requests_by_type = [[] for _ in range(k + 1)]
    for a, b, c in reqs:
        requests_by_type[c].append((a, b))
        
    # 2. 각 유형에 대해 1명 ~ (n-k+1)명 배정했을 때의 대기 시간 미리 계산
    # wait_times[type][count]
    wait_times = [[0] * (n + 1) for _ in range(k + 1)]
    
    for t in range(1, k + 1):
        # 해당 유형의 요청이 없으면 0
        if not requests_by_type[t]:
            continue
            
        for count in range(1, n - k + 2):
            # count명의 상담원으로 시뮬레이션
            pq = [0] * count # 각 상담원의 끝나는 시간
            total_wait = 0
            
            for start, duration in requests_by_type[t]:
                earliest_end = heapq.heappop(pq)
                
                wait = max(0, earliest_end - start)
                total_wait += wait
                
                # 상담 끝나는 시간 업데이트
                finish_time = max(start, earliest_end) + duration
                heapq.heappush(pq, finish_time)
                
            wait_times[t][count] = total_wait
            
    # 3. 멘토 인원 분배 조합 찾기
    # 각 유형에 최소 1명씩 이미 배정했다고 가정.
    # 남은 n - k 명을 k개 유형에 분배.
    # bars approach: k bins, distribute (n-k) items.
    
    remain = n - k
    min_total_wait = float('inf')
    
    # 중복조합으로 분배 케이스 생성
    # indices: k개의 유형 중 선택된 횟수가 추가 배정 인원
    for comb in combinations_with_replacement(range(1, k + 1), remain):
        # 각 유형별 배정 인원 계산 (기본 1명 + 추가)
        counts = [1] * (k + 1)
        for t in comb:
            counts[t] += 1
            
        current_total_wait = 0
        for t in range(1, k + 1):
            current_total_wait += wait_times[t][counts[t]]
            
        if current_total_wait < min_total_wait:
            min_total_wait = current_total_wait
            
    return min_total_wait
```
