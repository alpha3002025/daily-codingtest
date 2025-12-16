# 이중우선순위큐

## 문제 설명
다음 연산을 처리하는 큐를 구현하세요.
- `I 숫자`: 큐에 숫자 삽입.
- `D 1`: 큐에서 최댓값 삭제.
- `D -1`: 큐에서 최솟값 삭제.
모든 연산 후 `[최댓값, 최솟값]`을 반환 (비어있으면 `[0, 0]`).

## 문제 해결 전략

**Min-Heap**과 **Max-Heap** 두 개를 쓰거나, 파이썬의 `heapq` (Min-Heap)와 `nlargest` 등을 쓰거나, 단순히 리스트를 `sort` 하면서 처리할 수 있습니다.
$N$이 크지 않다면 리스트에서 `max()`, `min()`을 찾고 `remove()` 해도 통과되지만, 효율성을 위해 Heap을 쓰는 것이 정석입니다.
하지만 삭제 시 동기화가 필요하므로, `visited` 배열을 쓰거나 삭제된 원소를 체크해야 합니다.
파이썬의 간편함을 이용한다면:
- 삽입: `heapq.heappush`
- 최솟값 삭제: `heapq.heappop`
- 최댓값 삭제: `heapq.nlargest`로 찾아서 remove하거나 list를 다시 heapify.
- 혹은 2개의 힙을 쓰고 `valid` 배열로 삭제 여부 관리.

가장 쉬운 방법(데이터가 적을 때): 그냥 리스트 쓰고 매번 정렬/max/min. $O(N^2)$.
효율적 방법: `heapq` (Min Heap) 하나와 `max_heap` (Max Heap, 음수 저장) 하나를 쓰고, 삭제된 ID를 기록하는 방식.

## Python 코드 (동기화 방식)

```python
import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    visited = [False] * 1000001 # operation index max
    
    for i, op in enumerate(operations):
        cmd, val = op.split()
        val = int(val)
        
        if cmd == 'I':
            heapq.heappush(min_heap, (val, i))
            heapq.heappush(max_heap, (-val, i))
            visited[i] = True
            
        elif cmd == 'D':
            if val == 1: # 최댓값 삭제
                # 이미 삭제된 값(최솟값 삭제로 인해)은 팝업
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            else: # 최솟값 삭제
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
                    
    # 남은 값 정리
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
        
    if not min_heap:
        return [0, 0]
    
    return [-max_heap[0][0], min_heap[0][0]]
```
