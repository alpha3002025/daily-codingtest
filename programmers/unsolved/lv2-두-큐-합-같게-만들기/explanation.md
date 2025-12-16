# 두 큐 합 같게 만들기

## 문제 설명
길이가 같은 두 개의 큐 `queue1`, `queue2`가 주어집니다.
한 번의 작업은 큐에서 `pop`하여 다른 큐에 `insert`하는 것입니다.
두 큐의 원소 합을 같게 만들기 위해 필요한 최소 작업 횟수를 구합니다. 만들 수 없으면 -1을 반환합니다.

## 풀이 개념
**그리디 (Greedy)**와 **투 포인터 (Two Pointers)** 개념을 활용한 시뮬레이션입니다.
물리적인 큐의 `pop/insert`를 매번 수행하면 시간 초과(`O(N)` 연산)가 발생할 수 있으므로, 하나의 긴 배열로 합쳐서 인덱스(`ptr1`, `ptr2`)로 관리하거나, 단순 `sum` 변수만 갱신하며 `deque`의 `popleft/append`(`O(1)`)를 사용해야 합니다.

1. 두 큐의 합 `sum1`, `sum2`와 전체 합 `total_sum`을 구합니다.
2. `total_sum`이 홀수라면 절대 같게 만들 수 없으므로 -1을 반환합니다. 목표값 `target = total_sum // 2`입니다.
3. 반복문을 돌며(최대 횟수 제한: 약 `3 * len(q)`):
   - `sum1 > target`: 큐1의 원소를 빼서 큐2로 보냅니다. (`sum1` 감소, `sum2` 증가)
   - `sum1 < target`: 큐2의 원소를 빼서 큐1로 보냅니다.
   - `sum1 == target`: 정답 반환.
4. 최대 횟수를 초과하면 -1을 반환합니다.

## 코드 (Python)

```python
from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    s1 = sum(q1)
    s2 = sum(q2)
    total = s1 + s2
    
    if total % 2 != 0:
        return -1
        
    target = total // 2
    limit = len(q1) * 3 # 넉넉한 반복 제한 (원상복구 고려)
    count = 0
    
    while count <= limit:
        if s1 == target:
            return count
        
        if s1 > target:
            val = q1.popleft()
            q2.append(val)
            s1 -= val
            s2 += val
        else:
            val = q2.popleft()
            q1.append(val)
            s1 += val
            s2 -= val
            
        count += 1
        
    return -1
```
