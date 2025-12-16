# 선입 선출 스케줄링

## 문제 설명
`n`개의 작업, 코어의 처리 시간 `cores`.
작업은 요청 순서대로 비어있는 코어에 할당됩니다. 동시에 비면 번호가 빠른 코어에 할당됩니다.
마지막 작업을 처리하는 코어 번호를 구하세요.
(초기에 모든 코어에 작업 하나씩 할당됨)

## 문제 해결 전략

**이분 탐색 (Parametric Search)**.
시간 `T`까지 처리할 수 있는 총 작업 수를 구하는 함수 `count_jobs(T)`.
`count_jobs(T) = 코어수(0초에 할당) + sum(T // c for c in cores)`
목표: `count_jobs(T) >= n`을 만족하는 최소 `T`를 찾습니다.
그 `T` 시점에 **작업이 막 끝난(그래서 새 작업을 받는) 코어**들 중 `n`번째 작업을 가져가는 놈을 찾습니다.

1. `count_jobs(T) >= n`인 최소 시간 `time` 찾기.
2. `time - 1` 시간까지 처리된 작업 수 계산 (`processed`).
3. `remaining = n - processed`.
4. `time` 시점에 새로 할당 가능한 코어(즉 `time % core_time == 0`인 코어)를 순서대로 확인하며 `remaining`을 감소시킴. `remaining`이 0이 될 때의 코어가 답.

## Python 코드

```python
def solution(n, cores):
    if n <= len(cores):
        return n
        
    left = 1
    right = max(cores) * n # 넉넉하게
    target_time = right
    
    # 1. 시간 탐색 (n개 이상 처리되는 최소 시간)
    while left <= right:
        mid = (left + right) // 2
        
        # 0초에 len(cores)개 처리됨
        capacity = len(cores) + sum([mid // c for c in cores])
        
        if capacity >= n:
            target_time = mid
            right = mid - 1
        else:
            left = mid + 1
            
    # 2. 해당 시간(target_time)에 마지막 작업 수행 코어 찾기
    
    # 직전 시간까지 처리량
    processed = len(cores) + sum([(target_time - 1) // c for c in cores])
    remaining = n - processed
    
    for i, c in enumerate(cores):
        # target_time에 작업이 끝나는(새 작업을 시작하는) 코어 판별
        # time % c == 0 이면 time 시점에 해당 코어는 작업을 마치고 새 작업 수락 가능
        if target_time % c == 0:
            remaining -= 1
            if remaining == 0:
                return i + 1
                
    return 0
```
