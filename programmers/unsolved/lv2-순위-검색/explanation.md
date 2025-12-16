# 순위 검색

## 문제 설명
지원자들의 정보(언어, 직군, 경력, 소울푸드, 점수)가 주어지고, "조건"에 맞는 지원자가 몇 명인지 찾는 쿼리를 여러 번 수행해야 합니다.
조건에는 `-`(상관없음)이 포함될 수 있습니다.

### 핵심 개념
1.  **효율성 문제**: 지원자는 최대 50,000명, 쿼리는 최대 100,000개입니다. 단순 반복문으로 매 쿼리마다 지원자를 찾으면 $50,000 \times 100,000 = 50억$ 연산이 되어 시간 초과(Time Limit)가 발생합니다.
2.  **해시 맵 (Dictionary) + 조합 (Combinations)**:
    - 지원자 한 명의 정보는 4가지 속성을 가집니다 (언어, 직군, 경력, 소울푸드).
    - 쿼리에서는 각 속성이 특정 값이거나 `-`(상관없음)일 수 있습니다.
    - **Trick**: 지원자 정보를 미리 "가능한 모든 쿼리 조합"으로 만들어 딕셔너리에 저장합니다.
    - 예: `java backend junior pizza 150` 지원자는 `java - - -`, `- backend - -`, `java backend - pizza` 등 총 16가지($2^4$) 쿼리에 검색될 수 있습니다.
    - Key: 조건 조합(문자열), Value: 점수들의 리스트.
3.  **이진 탐색 (Binary Search)**:
    - 딕셔너리의 Value인 점수 리스트에서 "X점 이상"인 사람 수를 빨리 세어야 합니다.
    - 점수 리스트를 미리 정렬해두고, `bisect_left` (Lower Bound)를 사용하여 $O(\log N)$에 찾습니다.

## Python 풀이

```python
from bisect import bisect_left
from itertools import combinations
from collections import defaultdict

def solution(info, query):
    answer = []
    # 검색 조건을 Key, 점수 리스트를 Value로 저장할 딕셔너리
    data = defaultdict(list)
    
    # 1. 지원자 정보 전처리 (모든 경우의 수 저장)
    for i in info:
        temp = i.split()
        conditions = temp[:-1] # 점수 제외한 4가지 속성
        score = int(temp[-1])
        
        # 4가지 속성에 대해 '-'가 포함될 수 있는 모든 조합 생성 (0개~4개 선택)
        for k in range(5):
            for c in combinations(range(4), k):
                # c에 포함된 인덱스는 '-'로 대체하는 방식 or 
                # c에 포함된 인덱스만 값을 유지하고 나머지는 '-'로 하는 방식
                # 여기서는 combinations로 뽑은 인덱스를 조건 값으로 쓰고, 나머지는 '-'로 채우는 식으로 가거나
                # 반대로 combinations로 뽑은 위치를 '-'로 바꿈.
                
                # 구현 편의상: 4개의 속성을 16가지 key로 만듦
                key_list = conditions[:]
                for idx in c:
                    key_list[idx] = '-'
                
                key = "".join(key_list)
                data[key].append(score)
                
    # 2. 이진 탐색을 위해 점수 리스트 정렬
    for key in data:
        data[key].sort()
        
    # 3. 쿼리 수행
    for q in query:
        # "java and backend and junior and pizza 100" 형태 파싱
        q = q.replace('and', '').split()
        target_key = "".join(q[:-1])
        target_score = int(q[-1])
        
        scores = data[target_key]
        
        # scores 리스트에서 target_score 이상인 첫 번째 위치 찾기
        # bisect_left: target_score보다 크거나 같은 첫 위치
        idx = bisect_left(scores, target_score)
        
        # 전체 개수 - idx = target_score 이상인 개수
        answer.append(len(scores) - idx)
        
    return answer
```

### 코드 설명
- `combinations(range(4), k)`: 4개의 속성 중 $k$개를 골라 `-`로 바꿉니다. 이렇게 하면 해당 지원자가 검색될 수 있는 모든 쿼리 키를 생성할 수 있습니다.
- `key = "".join(key_list)`: 딕셔너리 키로 사용하기 위해 문자열로 합칩니다.
- **정렬**: 전처리가 끝난 후 한 번만 정렬합니다.
- `bisect_left`: 정렬된 리스트에서 특정 값 이상이 처음 등장하는 인덱스를 반환합니다. 이를 이용해 $O(1)$이 아닌 $O(\log N)$으로 쿼리를 처리합니다.
- 복잡도: 전처리 $O(N \cdot 2^4)$, 정렬 $O(Key \cdot L \log L)$, 쿼리 $O(M \cdot \log L)$. $N, M$이 커도 충분히 빠릅니다.
