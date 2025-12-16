# 야근 지수

## 문제 설명
야근 피로도는 야근한 작업량의 제곱의 합입니다.
`N`시간 동안 야근을 하여 피로도를 최소화하세요.
작업량 `works`가 주어짐. 1시간에 1만큼 작업량 감소.

## 문제 해결 전략

**Max Heap (Priority Queue)**.
제곱의 합을 최소화하려면 **큰 숫자를 줄이는 것**이 가장 효과적입니다. (예: $5^2 + 1^2 = 26$ vs $4^2 + 2^2 = 20$).
따라서 항상 현재 가장 큰 작업량을 1씩 줄입니다.
파이썬은 Min Heap이므로 음수로 변환하여 Max Heap 처럼 사용합니다.

## Python 코드

```python
import heapq

def solution(n, works):
    # 남은 작업량 총합보다 n이 크면 0
    if sum(works) <= n:
        return 0
    
    # Max Heap 구성 (음수)
    pq = [-w for w in works]
    heapq.heapify(pq)
    
    while n > 0:
        # 가장 큰 작업량 꺼내서 1 줄임 (음수니까 +1 하면 절댓값 작아짐)
        curr = heapq.heappop(pq)
        curr += 1 
        heapq.heappush(pq, curr)
        n -= 1
        
    # 제곱의 합 (음수 제곱해도 양수)
    return sum([w ** 2 for w in pq])
```
