# 다리를 지나는 트럭

## 문제 설명
트럭 여러 대가 일차선 다리를 정해진 순서대로 건너야 합니다.
다리는 무게 제한 `weight`가 있고, 길이는 `bridge_length`입니다. 트럭은 1초에 1만큼 이동합니다. 모든 트럭이 다리를 건너려면 몇 초가 걸리는지 구하세요.

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
- 마지막 트럭이 다리에 올라간 순간 `trucks`가 비게 되지만, `bridge` 큐에 트럭들이 남아있으므로 루프는 계속 돕니다. 모든 트럭(및 0)이 빠져나가면 루프가 종료됩니다.
