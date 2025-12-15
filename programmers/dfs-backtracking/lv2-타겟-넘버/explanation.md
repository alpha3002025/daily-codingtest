# 타겟 넘버 (Target Number)

## 1. 문제 설명
- **문제 링크**: [https://school.programmers.co.kr/learn/courses/30/lessons/43165](https://school.programmers.co.kr/learn/courses/30/lessons/43165)
- **정보**:
  - $n$개의 음이 아닌 정수가 주어집니다.
  - 이 정수들의 **순서를 바꾸지 않고**, 더하거나 빼서 **타겟 넘버**를 만들어야 합니다.
  - 타겟 넘버를 만들 수 있는 방법의 수를 반환하세요.
- **제한사항**:
  - 주어지는 숫자의 개수: 2개 이상 20개 이하.
  - 각 숫자는 1 이상 50 이하인 자연수.
  - 타겟 넘버는 1 이상 1000 이하인 자연수.

---

## 2. 접근법 및 핵심 개념 (DFS/BFS)

### 개념: 상태 공간 트리 (State Space Tree)와 탐색
이 문제는 주어진 숫자들을 순서대로 사용하며 `+`(더하기) 또는 `-`(빼기)라는 두 가지 선택을 반복적으로 수행하는 과정으로 볼 수 있습니다. 이를 트리 구조로 시각화하면 다음과 같습니다.

- **루트 노드**: 0 (초기 합계)
- **1단계**: 첫 번째 숫자를 더하거나 뺌 (2가지 경우)
- **2단계**: 두 번째 숫자를 더하거나 뺌 (각 경우에 대해 2가지 → 총 4가지 경우)
- ...
- **n단계**: $n$번째 숫자를 더하거나 뺌 (총 $2^n$가지 경우)

숫자의 개수가 최대 20개이므로, 최대 경우의 수는 $2^{20} \approx 1,000,000$(100만)입니다. 이는 통상적인 시간 제한(약 1초~수 초, 1억 연산 기준) 내에 충분히 **완전 탐색(Brute Force)** 할 수 있는 크기입니다.

따라서 **BFS(너비 우선 탐색)** 또는 **DFS(깊이 우선 탐색)** 를 사용하여 모든 경우의 수를 확인하고, 최종 결과가 `target`과 같은 경우를 세면 됩니다.

---

## 3. Python 풀이 (BFS 활용)

폴더 구조가 `bfs`이므로 **BFS(너비 우선 탐색)** 방식을 사용한 풀이를 소개합니다. BFS는 레벨(각 숫자 인덱스) 단위로 가능한 모든 합계 상태를 확장해 나가는 방식입니다.

### BFS 코드

```python
from collections import deque

def solution(numbers, target):
    # 큐에 초기 합계 0을 넣고 시작
    queue = deque([0])
    
    # 각 숫자를 순회하며 트리 확장
    for num in numbers:
        length = len(queue)
        # 현재 레벨(큐에 있는 모든 합계들)에 대해 반복
        for _ in range(length):
            current_sum = queue.popleft()
            
            # 현재 합계에 num을 더하는 경우
            queue.append(current_sum + num)
            # 현재 합계에서 num을 빼는 경우
            queue.append(current_sum - num)
            
    # 모든 숫자를 처리한 후, 큐에 남은 값들 중 target과 일치하는 개수를 반환
    return queue.count(target)
```

### 코드 분석
1. `queue`에는 현재 단계까지 계산된 **모든 가능한 합계**들이 저장됩니다.
2. `numbers`의 각 숫자 `num`을 순회하면서, 큐에 있는 기존 합계들에 `num`을 더한 값과 뺀 값을 새로운 큐에 추가합니다.
   - 예: `numbers = [1, 1]`, `target = 3`
   - 초기: `queue = [0]`
   - 첫 번째 1 처리: `queue = [1, -1]` (0+1, 0-1)
   - 두 번째 1 처리: `queue = [2, 0, 0, -2]` (1+1, 1-1, -1+1, -1-1)
3. 모든 숫자를 처리한 뒤 `queue`에는 최종 합계들이 남게 되며, 이 중 `target` 값의 개수를 셉니다.

---

## 4. 다른 풀이 (DFS - 재귀)

문제의 성격상 DFS(재귀) 구현도 매우 직관적입니다.

### DFS 코드

```python
def solution(numbers, target):
    # n: 현재 사용하고 있는 numbers의 인덱스
    # current_sum: 현재까지의 합
    def dfs(index, current_sum):
        # Base Case: 모든 숫자를 다 사용했을 때
        if index == len(numbers):
            # 타겟 넘버를 만들었으면 1 반환, 아니면 0 반환
            return 1 if current_sum == target else 0
        
        # Recursive Case:
        # (+)를 선택한 경우와 (-)를 선택한 경우의 합을 구함
        return dfs(index + 1, current_sum + numbers[index]) + \
               dfs(index + 1, current_sum - numbers[index])
               
    return dfs(0, 0)
```

---

## 5. 복잡도 분석
- **시간 복잡도**: $O(2^n)$
  - 각 숫자마다 2개의 분기가 생기므로 트리의 노드 수는 $2^{n+1} - 1$개입니다. 모든 노드를 방문해야 하므로 지수 시간이 소요됩니다.
  - 문제 제한조건 $n \le 20$ 하에서는 효율설 테스트를 통과합니다.
- **공간 복잡도**: $O(2^n)$ (BFS의 경우) / $O(n)$ (DFS의 경우)
  - BFS는 마지막 레벨에서 $2^n$개의 잎 노드(leaf node) 값을 저장해야 하므로 메모리를 더 많이 사용합니다.
  - DFS는 재귀 호출 스택 깊이가 $n$만큼만 들어가므로 공간 복잡도 면에서는 더 효율적일 수 있습니다.
