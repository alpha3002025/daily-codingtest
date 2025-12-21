# 명예의 전당 (1)

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/138477)

매일 점수(`score`)가 발표됩니다. 이 중 상위 `k`번째 이내의 점수들만 "명예의 전당"에 오릅니다.
매일매일 명예의 전당에 있는 점수들 중 **최하위 점수(k번째 점수)**를 발표해야 합니다.
- 초기에는 `k`일까지 모든 점수가 전당에 오릅니다.
- `k`일 이후부터는 새로운 점수가 전당의 최하위보다 높으면 교체됩니다.

## 해결 전략
상위 `k`개를 유지하면서 그 중 최솟값을 빠르게 찾아야 합니다.
**최소 힙(Min Heap)** 자료구조를 사용하면 매우 효율적입니다.
힙의 크기를 `k`로 유지하면, 힙의 루트(`heap[0]`)가 항상 `k`번째로 큰 값(전당 내 최하위 값)이 됩니다.

### 알고리즘 순서
1. `q` = [] (Min Heap으로 사용할 리스트)
2. `answer` = []
3. `s` in `score`:
    - `heapq.heappush(q, s)`
    - 만약 `len(q) > k`:
        - `heapq.heappop(q)` (가장 작은 값 제거 -> 상위 k개 유지)
    - `answer.append(q[0])` (현재 전당 내 최솟값 기록)
4. `answer` 반환.

## Python 코드

```python
import heapq

def solution(k, score):
    answer = []
    hall_of_fame = [] # Min Heap
    
    for s in score:
        heapq.heappush(hall_of_fame, s)
        
        # k개 넘어가면 최솟값(탈락자) 제거
        if len(hall_of_fame) > k:
            heapq.heappop(hall_of_fame)
            
        # 현재 전당의 최하위 점수 (Min Heap의 root)
        answer.append(hall_of_fame[0])
        
    return answer
```

## 배운 점 / 팁
- **Heap 자료구조 (`heapq`)**: 데이터 스트림에서 상위 N개, 혹은 중앙값 등을 실시간으로 유지/관리해야 할 때 필수적입니다.
- **Top-K 패턴**: 크기가 K인 Min Heap을 유지하면 들어온 모든 데이터 중 Top K를 `O(N log K)`에 관리할 수 있습니다.
