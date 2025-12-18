# 두 큐 합 같게 만들기

## link
- https://school.programmers.co.kr/learn/courses/30/lessons/118667

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

## 코드 설명
- **반복 제한 (`limit`)의 이유**: 단순히 무한 루프를 방지하기 위함이 아니라, **"모든 경우의 수"**를 고려한 값입니다.
    - 최악의 경우, 큐 A의 원소가 큐 B로 모두 넘어가고(`N`), 다시 큐 B의 원래 원소들이 큐 A로 넘어오고(`N`), 다시 일부가 넘어가는 등의 순환 과정을 거쳐야 답이 나올 수 있습니다.
    - 큐 길이 $N$에 대해, 한쪽 큐가 완전히 비워졌다가 다시 채워지는 사이클 등을 고려하면 대략 $3N \sim 4N$ 정도의 횟수 안에는 반드시 결론(성공 혹은 불가능)이 나야 합니다. 
    - 만약 이 횟수를 넘어서도 합이 맞춰지지 않는다면, 영원히 맞출 수 없는 사이클에 빠진 것으로 간주하고 `-1`을 반환합니다.

###  **Q. 왜 2 * N 이 아니라 3 * N 인지?**  
- Q : `2 * len(q1) 정도는 약간 넘어설수 있어서 3 * len(q1) 으로 잡은걸까요?`
- A
  - `2 * N`은 큐 A의 원소가 모두 큐 B로 가고, 큐 B의 원소들이 자리를 바꾸는 정도의 횟수입니다. 하지만 원소들이 완전히 교체된 후에도 **순서를 미세하게 조정하기 위해 추가적인 이동**이 필요한 경우가 있을 수 있습니다.  
  - `2 * N`은 이런 경계값 케이스에서 살짝 부족할 수 있으므로, 안전하게(Safety Margin) `3 * N` (또는 `4 * N`)으로 설정하는 것이 일반적입니다.



