# 순위 검색
**combination + hash + binary search**<br/>
<br/>

- 좋은 문제다. 처음에는 우습게 보고 풀었었다. 
- 이 문제는 `info` 배열의 크기가 최대 50000, `query` 배열의 크기가 최대 100000 인데, 이중 반복문을 사용해야 하기 때문에 최악의 경우 50000 x 100000 = 50억번의 연산횟수가 필요하다. 
- 1ns 는 1/10억분이고, 32비트 컴퓨터 기준 약 1/4 클록이기에 클록의 25% 를 쓴다는 것은 최악의 경우 많이 느리다는 의미다.
- 따라서 미리 조합을 통해서 조건값들을 해시에 넣어두어 조회하는 것이 필요하고, 특정 점수 이상을 조회하는 것 역시 이분탐색을 통해 검색 속도를 최적화해야 한다.

<br/>
<br/>


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


## 개념 설명 코드
```python
from itertools import combinations
from collections import defaultdict
from bisect import bisect_left


def solution(info, query):    
    score_data = defaultdict(list)
    
    for data in info:
        args = data.split()
        score = int(args[-1])
        conditions = args[:-1]
        
        for window_size in range(5):
            for curr_comb in combinations(range(4), window_size): # ['cpp', 'java', 'python', '-']
                condition_copy = conditions[:]
                
                for index in curr_comb:
                    condition_copy[index] = '-'
                
                key = "".join(condition_copy)
                score_data[key].append(score)
    
    
    for key in score_data.keys():
        score_data[key].sort()
        
    answer = []
    
    for condition in query:
        args = condition.replace(" and ", "").split()
        key = args[0]
        score = int(args[1])
        
        scores = score_data[key]
        pos = bisect_left(scores, score)
        answer.append(len(scores) - pos)
    
    return answer
```



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
        
        # 4가지 속성 중 0개~4개를 선택하여 '-'로 바꾼 모든 경우의 수(16가지)를 생성
        # 예: java backend junior pizza 
        # -> java - junior pizza (backend를 '-'로 바꿈)
        # -> - - - - (모두 '-'로 바꿈) 등
        for k in range(5):
            for c in combinations(range(4), k):
                key_list = conditions[:] 
                for idx in c:
                    key_list[idx] = '-' # 선택된 인덱스를 와일드카드('-')로 변경
                
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


## 나의 풀이
### 2025/12/19
```python
from bisect import bisect_left
from itertools import combinations
from collections import defaultdict

def solution(info, query):
    answer = []
    results = defaultdict(list)
    
    for data in info:
        args = data.split()
        conditions = args[:-1]
        score = int(args[-1])
        
        ## 4가지 조건 중 '-'가 포함되는 케이스의 조합 생성
        ## e.g. java backend junior pizza ➝ java - junior pizza ➝ - - - -
        for curr_len in range(5):
            for c in combinations(range(4), curr_len): 
                    ## '-' 는 4개까지만 가능하다. 
                    ## score 는 '-'가 올수 없는 것이 문제의 조건이기 때문
                key_list = conditions[:]
                
                ## 0 일때에는 for loop 이 수행되지 않으므로 조건 문자열 그대로 유지 가능
                for idx in c:
                    key_list[idx] = '-' ## 선택된 인덱스의 위치를 '-'로 변경
                                        
                
                key = "".join(key_list)
                results[key].append(score)
                
    for key in results:
        results[key].sort() ## 해당 조건내의 점수들을 점수 순 오름차순 정렬
    
    for q in query:
        lang,job,level,food,score = q.replace('and', '').split()
        key = lang+job+level+food
        scores = results[key]
        idx = bisect_left(scores, int(score))
        
        answer.append(len(scores) - idx)
    
    return answer
```