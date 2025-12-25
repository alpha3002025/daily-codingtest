# 다리를 지나는 트럭
문제에서는 거리 1을 지나가는 데에 몇초가 지난다는 조건은 명시되지 않았다. 다만 `bridge_length=2` 인 다리를 건널때 모든 요소가 동일하게 2 초 동안 이동하는 것을 통해 거리 1을 이동하는 데에 1초가 걸린다는 사실을 추측해야 하는 것이 문제를 풀때 부딪히게 되는 첫 번째 어려운 점이다.<br/>
<br/>


## 문제 설명
트럭 여러 대가 일차선 다리를 정해진 순서대로 건너야 합니다.
다리는 무게 제한 `weight`가 있고, 길이는 `bridge_length`입니다.
> **조건 (유추)**: 문제에 속도가 명시되지는 않았지만, "다리에 최대 `bridge_length`대가 올라갈 수 있다"는 조건과 예시를 통해 **트럭은 1초에 1만큼 이동**함을 알 수 있습니다.
> 따라서, 길이 `bridge_length`인 다리를 완전히 건너는 데에는 정확히 **`bridge_length`초**가 걸립니다.

모든 트럭이 다리를 건너려면 몇 초가 걸리는지 구하세요.

<br/>


### 핵심 개념
1.  **큐 (Queue) 시뮬레이션**: 다리 위 상태를 큐로 관리합니다.
    - 다리 길이만큼의 리스트(또는 큐)를 만들고, 0으로 채워 초기화합니다. `[0, 0, ..., 0]`
    - 매 초마다
        1. 맨 앞(다리를 다 건넌 트럭)을 `pop`.
        2. 대기 중인 트럭이 다리에 올라올 수 있는지(무게 제한) 확인.
        3. 가능하면 트럭을 `push`, 아니면 무게 0(공기)을 `push`.
2.  **시간 관리**: `time` 변수를 1씩 증가시킵니다.

## Python 풀이

```python
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    # 다리 위 상태를 나타내는 큐 (길이만큼 0으로 초기화)
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    
    # 다리 위 현재 무게 (sum(bridge)는 느리므로 변수로 관리)
    current_weight = 0
    
    # 다리 위에 트럭이 있거나, 대기 중인 트럭이 있는 동안 반복
    while bridge:
        time += 1
        
        # 1. 다리 끝에서 트럭(또는 0)이 나감
        exited = bridge.popleft()
        current_weight -= exited
        
        if trucks:
            # 2. 다음 트럭이 올라올 수 있는지 확인
            if current_weight + trucks[0] <= weight:
                new_truck = trucks.popleft()
                bridge.append(new_truck)
                current_weight += new_truck
            else:
                # 못 올라오면 빈 공간(0) 채움
                bridge.append(0)
                
    return time
```

### 코드 설명
- `sum(bridge)`를 매번 호출하면 $O(Bridge\_Length)$가 소요되어 전체 성능이 떨어질 수 있습니다. `current_weight` 변수로 무게 합을 관리하는 것이 좋습니다.
- 처음에 `bridge` 큐에 0을 채워두고 시작하면, "1초 지남 -> pop -> push" 로직을 자연스럽게 구현할 수 있습니다.
- **트럭 대기열(`trucks`)이 비어있는 경우**:
  - 더 이상 다리에 올릴 새 트럭은 없지만, **만약 이미 다리 위에 올려져 있는 트럭들이 있다면, 이들이 끝까지 건너야 하므로** 시뮬레이션(루프)은 계속되어야 합니다.
  - 이때 `if trucks:` 조건문은 거짓이 되어 새로운 트럭을 올리는(push) 과정은 생략되지만, `while bridge:` 반복문은 다리가 텅 빌 때까지 계속 돌며 `time += 1`을 수행합니다.
  - 즉, 마지막 트럭이 다리에 올라간 이후에도 다리를 건너는 시간만큼 시간이 계속 흐르게 됩니다.
