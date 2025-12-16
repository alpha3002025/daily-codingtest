# 입국심사

## 문제 설명
`n`명이 입국심사를 기다립니다.
심사관마다 심사 걸리는 시간 `times`가 다릅니다.
모든 사람이 심사를 받는데 걸리는 최소 시간을 구하세요.

## 문제 해결 전략

전형적인 **이분 탐색 (Parametric Search)** 문제입니다.
"시간 `T` 내에 `n`명을 모두 심사할 수 있는가?" 라는 결정 문제로 바꿉니다.
- 가능하다면: `T`를 줄여서 최솟값을 찾습니다. (왼쪽 탐색)
- 불가능하다면: `T`를 늘립니다. (오른쪽 탐색)

**결정 문제 로직**:
- 시간 `T` 동안 각 심사관이 처리할 수 있는 사람 수: `T // times[i]`
- 전체 처리 가능 인원 = `sum(T // t for t in times)`
- 이 합이 `n` 이상이면 가능.

범위:
- 최소: 1분
- 최대: 가장 느린 심사관 * n명 (최악의 경우)

## Python 코드

```python
def solution(n, times):
    left = 1
    right = max(times) * n
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        
        # mid 시간 동안 처리 가능한 사람 수 합계
        people = 0
        for t in times:
            people += mid // t
            
        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return answer
```
