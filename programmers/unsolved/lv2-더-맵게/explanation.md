# 더 맵게

## 문제 설명
모든 음식의 스코빌 지수를 `K` 이상으로 만들고 싶습니다.
스코빌 지수가 가장 낮은 두 음식(가장 맵지 않은 것, 두 번째로 맵지 않은 것)을 섞어 새로운 음식을 만듭니다.
- `섞은 음식 지수 = 가장 안 매운 + (두 번째 안 매운 * 2)`
이 과정을 반복하여 횟수를 구하세요.

### 핵심 개념
1.  **우선순위 큐 (Priority Queue) / 힙 (Heap)**:
    - 매번 **최솟값** 두 개를 꺼내야 하고, 새로운 값을 다시 넣고 정렬 상태를 유지해야 합니다.
    - 일반 리스트 정렬(`sort`)은 $O(N \log N)$이므로 반복하면 느립니다. 힙은 삽입/삭제 $O(\log N)$입니다.
2.  **힙큐 (heapq)** 모듈 사용.

## Python 풀이

```python
import heapq

def solution(scoville, K):
    # 최소 힙으로 변환
    heapq.heapify(scoville)
    mix_count = 0
    
    # 가장 맵지 않은 음식(root)이 K 미만일 때 계속 반복
    while scoville[0] < K:
        # 음식이 하나밖에 안 남았는데 K 미만이면 불가능
        if len(scoville) < 2:
            return -1
            
        # 가장 작은 2개 추출
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        # 섞어서 다시 넣기
        new_food = first + (second * 2)
        heapq.heappush(scoville, new_food)
        
        mix_count += 1
        
    return mix_count
```

### 코드 설명
- `heapq.heapify(list)`: 리스트를 힙 구조로 변환 ($O(N)$).
- `heappop`: 최솟값 추출 ($O(\log N)$).
- `heappush`: 원소 삽입 ($O(\log N)$).
- `scoville[0]`: 힙의 루트는 항상 최솟값입니다. 이를 확인하여 Loop 조건을 설정합니다.
