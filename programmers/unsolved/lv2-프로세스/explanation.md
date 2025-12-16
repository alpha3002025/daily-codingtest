# 프로세스 (구: 프린터)

## 문제 설명
중요도가 높은 문서가 먼저 인쇄되도록 큐를 관리합니다.
1. 큐의 가장 앞에 있는 문서를 꺼냅니다.
2. 중요도가 더 높은 문서가 큐에 하나라도 있다면, 방금 꺼낸 문서를 인쇄하지 않고 맨 뒤로 보냅니다.
3. 그렇지 않으면 인쇄합니다.
내가 요청한 문서가 몇 번째로 인쇄되는지 구하세요.

### 핵심 개념
1.  **큐 (Queue) / 덱 (Deque)**: 앞에서 꺼내고 뒤로 넣는 동작이 빈번합니다.
2.  **시뮬레이션**: 문제의 로직을 그대로 구현합니다.
3.  **위치 추적**: 문서들의 위치가 계속 바뀌므로, `(중요도, 초기인덱스)` 형태의 튜플로 큐에 저장해야 내가 찾는 문서(`location`)인지 알 수 있습니다.

## Python 풀이

```python
from collections import deque

def solution(priorities, location):
    # (중요도, 초기인덱스) 큐 생성
    # 예: [(2,0), (1,1), (3,2), (2,3)]
    q = deque([(p, i) for i, p in enumerate(priorities)])
    
    print_order = 0
    
    while q:
        # 1. 큐에서 하나 꺼냄 (J)
        current = q.popleft()
        
        # 2. 나머지 중 중요도가 더 높은 게 있는지 확인
        # any() 함수 사용: 하나라도 True면 True
        if any(current[0] < other[0] for other in q):
            # 더 중요한 게 있으면 뒤로 보냄
            q.append(current)
        else:
            # 3. 없으면 인쇄
            print_order += 1
            # 내가 찾던 그 문서(location)인가?
            if current[1] == location:
                return print_order
                
    return print_order
```

### 코드 설명
- `any(...)`를 사용하여 현재 꺼낸 문서보다 중요도가 높은 문서가 큐에 남아있는지($O(N)$) 확인합니다.
- N이 100 이하이므로 $O(N^2)$ 복잡도여도 충분히 빠릅니다.
- 만약 찾는 문서라면 현재까지의 `print_order`를 반환합니다.
