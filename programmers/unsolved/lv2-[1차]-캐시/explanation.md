# [1차] 캐시

## 문제 설명
DB 캐시를 적용할 때, 캐시 크기(`cacheSize`)와 도시 이름 배열(`cities`)이 주어지면 총 실행 시간을 구하는 문제입니다.
- 캐시 교체 알고리즘: **LRU (Least Recently Used)**.
- **Cache Hit**: 실행 시간 1.
- **Cache Miss**: 실행 시간 5.
- 대소문자 구분 없음.

### 핵심 개념
1.  **LRU 알고리즘**: 가장 오랫동안 사용하지 않은 항목을 제거합니다.
    - 접근된 항목(Hit 또는 New Insert)은 "가장 최근에 사용됨" 상태가 되어야 합니다.
2.  **덱 (Deque)**: 양쪽 끝에서 삽입/삭제가 가능한 자료구조입니다.
    - `maxlen`을 설정하면 크기가 고정된 큐처럼 쓸 수 있어 편리합니다.
    - 항목을 `remove`하고 다시 `append`하면 최근 사용으로 갱신할 수 있습니다.

## Python 풀이

```python
from collections import deque

def solution(cacheSize, cities):
    # 캐시 크기가 0인 경우 예외 처리
    if cacheSize == 0:
        return len(cities) * 5
    
    # maxlen을 설정하면 append 시 자동으로 오래된 항목(왼쪽)이 밀려남
    cache = deque(maxlen=cacheSize)
    total_time = 0
    
    for city in cities:
        # 대소문자 구분 X
        city = city.lower()
        
        if city in cache:
            # Cache Hit: 실행 시간 1
            total_time += 1
            
            # LRU 갱신: 뽑아서 다시 맨 뒤(최근)로 넣음
            cache.remove(city)
            cache.append(city)
        else:
            # Cache Miss: 실행 시간 5
            total_time += 5
            
            # 캐시에 추가 (꽉 찼다면 maxlen 덕분에 자동으로 popleft 수행됨)
            cache.append(city)
            
    return total_time
```

### 코드 설명
- `deque(maxlen=K)`: 큐의 길이가 K를 넘으면 `append` 시 제일 앞(왼쪽)의 요소가 자동으로 삭제됩니다. LRU 구현에 최적화된 기능입니다.
- `cache.remove(city)`: 덱 중간에 있는 요소를 삭제합니다. 시간 복잡도는 $O(N)$이지만 캐시 크기($N \le 30$)가 매우 작으므로 괜찮습니다.
- 캐시 사이즈가 0일 때는 아무것도 저장할 수 없으므로 모든 요청이 Miss가 됩니다. 별도로 처리해야 `maxlen=0` 에러 등을 피할 수 있습니다 (사실 maxlen=0이면 동작하긴 하지만 `in` 검사가 항상 false).
