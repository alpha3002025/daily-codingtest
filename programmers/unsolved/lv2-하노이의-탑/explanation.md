# 하노이의 탑

## 문제 설명
하노이의 탑은 3개의 기둥과 크기가 서로 다른 `n`개의 원판으로 이루어져 있습니다.
모든 원판을 1번 기둥에서 3번 기둥으로 옮기는 최소 과정을 구하세요.
조건:
1. 한 번에 하나의 원판만 이동.
2. 큰 원판이 작은 원판 위에 있을 수 없음.

### 핵심 개념
1.  **재귀 (Recursion)**: 문제를 작은 문제로 쪼갭니다.
    - $N$개를 `from` -> `to`로 옮기려면:
        1. 상위 $N-1$개를 `from` -> `mid`로 옮긴다. (재귀)
        2. 가장 큰 원판(마지막 1개)을 `from` -> `to`로 옮긴다. (기록)
        3. 상위 $N-1$개를 `mid` -> `to`로 옮긴다. (재귀)
2.  **기둥 번호**: 1, 2, 3번 기둥. 합이 6이므로 `mid = 6 - start - end` 로 구할 수 있습니다.

## Python 풀이

```python
def solution(n):
    answer = []
    
    def hanoi(count, start, end, mid):
        # Base Case: 원판 1개면 그냥 이동
        if count == 1:
            answer.append([start, end])
            return
        
        # 1. N-1개를 보조 기둥(mid)으로 이동
        hanoi(count - 1, start, mid, end)
        
        # 2. 가장 큰 원판을 목적지(end)로 이동
        answer.append([start, end])
        
        # 3. N-1개를 보조 기둥(mid)에서 목적지(end)로 이동
        hanoi(count - 1, mid, end, start)
        
    hanoi(n, 1, 3, 2)
    return answer
```

### 코드 설명
- 전형적인 재귀 문제입니다.
- 이동 경로는 `[출발, 도착]` 형태로 리스트에 담습니다.
- 총 이동 횟수는 $2^n - 1$회입니다.
