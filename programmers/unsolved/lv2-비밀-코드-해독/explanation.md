# 비밀 코드 해독
- combination , set 활용 능력이 필요하다.
- 5개의 숫자들을 고른 조합 각각에 대해 조합 하나별로 `queries[0]`, `queries[1]`, ... `queries[n-1]` 이 `ans[0]`, `ans[1]`, ... `ans[n-1]` 에서 원하는 정답개수와 일치하는지 확인한다.
- 즉 숫자를 뽑은 나열 각각에 대해 그게 해당 회차에서 원하는 실제 정답갯수와 일치하는지 확인하고, 그 조합이 합당한 정답갯수와 일치하면 answer+=1 을 한다.
- 근데 특이한건 ans 의 배열에 모두 일치하는 배열이어야 한다. 즉 어떤 비밀번호 숫자열을 시험했을때 원하는 맞춘 갯수가 2,3,4,5,6 이면 여러 조합 중 특정 조합 k 는 `queries[0]`, `queries[1]`, ... `queries[n-1]` 에 대해 2,3,4,5,6 의 순서로 정답갯수가 일치해야 한다.
- 뭔가 로또 맞추는 듯한 문제인데, 이게 문제 내용 자체가 좀 설명도 좀 술취한 사람이 쓴 것 같고 설명을 제대로 못한 티가 좀 나기도 하고 머릿속에 떠오른 생각을 남이 이해해주길 바라는데 제대로 작성을 못한듯한 티가 나는 문제인데 이게 1차 예선 문제로 나왔다고 하니... 알아서 센스있게 살살 맞춰가면서 풀어가야 하는 문제로 보인다.<br/>
<br/>


## 개념설명 코드
```python
from itertools import combinations

def solution(n, q, ans):
    answer = 0
    
    ## 사용자의 입력 시도 숫자열의 set 들 (교집합 연산을 위해 set 으로 변환)
    queries = [set(attempt) for attempt in q]
    
    ## 1 ~ n 까지 5개의 수를 뽑아서 임의의 수를 조합으로 생성
    for combination in combinations(range(1, n+1),5):
        combo_set = set(combination) ## 교집합 연산을 위해 set 으로 변환
        is_possible =  True
        
        for i in range(len(q)):
            ## combo_set 과 queries[i] (=i번째 query) 를 비교해 일치하는 개수 카운트
            match_count = len(combo_set.intersection(queries[i]))
            if match_count != ans[i]:
                is_possible = False
                break
        
        if is_possible:
            answer += 1
    
    return answer
```
<br/>


## 문제 설명
1부터 `n`까지의 정수 중 서로 다른 5개의 정수로 구성된 오름차순 비밀 코드가 있습니다.
`m`번의 시도(`q`)와 각 시도에서 맞춘 개수(`ans`)가 주어졌을 때, 가능한 비밀 코드 조합의 총 개수를 구하는 문제입니다.

- `n`: 정수 범위 (10 ~ 30)
- `q`: 시도한 정수 배열들 (각 길이는 5)
- `ans`: 각 시도별 일치하는 정수의 개수

## 풀이 개념
**완전 탐색 (Brute Force)** 문제입니다.
`n`의 최대 크기가 30으로 매우 작기 때문에, 가능한 모든 5개의 숫자 조합을 생성하여 조건에 맞는지 확인하면 됩니다.

1.  **가능한 조합의 수 계산**:
    - $_nC_5$ (30개 중 5개 선택)
    - $_{30}C_5 = \frac{30 \times 29 \times 28 \times 27 \times 26}{5 \times 4 \times 3 \times 2 \times 1} = 142,506$개
    - 14만 개 정도의 조합은 Python으로 1초 내에 충분히 검사할 수 있습니다.

2.  **알고리즘**:
    - `itertools.combinations`를 사용하여 1부터 `n`까지의 숫자 중 5개를 뽑는 모든 조합을 생성합니다.
    - 각 조합이 주어진 `m`개의 힌트(`q`, `ans`)를 모두 만족하는지 검사합니다.
    - `set` 자료구조의 `intersection` (교집합) 연산을 사용하면 두 조합 간에 일치하는 숫자 개수를 빠르게 구할 수 있습니다.
    - 모든 조건을 만족하는 조합의 수를 카운트하여 반환합니다.

## Python 풀이

```python
from itertools import combinations

def solution(n, q, ans):
    answer = 0
    
    # 입력된 시도(q)를 집합(set)으로 변환하여 교집합 연산 최적화
    q_sets = [set(attempt) for attempt in q]
    
    # 1부터 n까지의 숫자 중 5개를 뽑는 모든 경우의 수 탐색
    for combo in combinations(range(1, n + 1), 5):
        combo_set = set(combo)
        is_possible = True
        
        # 주어진 m개의 힌트를 모두 만족하는지 확인
        for i in range(len(q)):
            # 교집합의 크기(= 일치하는 숫자의 개수)가 ans[i]와 같은지 확인
            match_count = len(combo_set.intersection(q_sets[i]))
            if match_count != ans[i]:
                is_possible = False
                break
        
        if is_possible:
            answer += 1
            
    return answer
```

## 코드 설명
- **`q_sets` 변환**: 반복문 안에서 매번 `set(q[i])`를 호출하는 오버헤드를 줄이기 위해, 미리 `q`의 원소들을 집합으로 변환해 둡니다.
- **`itertools.combinations(range(1, n + 1), 5)`**: 1부터 `n`까지의 숫자 중 5개를 순서 없이 뽑는 모든 조합을 생성합니다.
- **`combo_set.intersection(q_sets[i])`**: 생성된 후보 조합과 시도한 조합 사이의 공통 원소를 구합니다. 이 길이가 `ans[i]`와 다르면 해당 후보는 비밀 코드가 될 수 없습니다.
- 모든 힌트를 통과한(`is_possible == True`) 조합만 카운트합니다.

### 시간 복잡도
- 조합 생성: $_nC_5$
- 검사: $m \times (\text{set intersection cost})$
- 전체 복잡도: $O(_nC_5 \times m)$
- 최악의 경우($n=30, m=10$)에도 연산 횟수는 약 $1.4 \times 10^6$회 정도로, 매우 빠르게 수행됩니다.

## 코드 상세 설명

### `is_possible = False` 처리와 `break`의 의미
후보 조합이 정답(비밀 코드)이 되려면, 주어진 **모든** 시도(`q`)와 결과(`ans`) 조건을 동시에 만족해야 합니다.
- `match_count != ans[i]`인 경우가 **단 하나라도 발생하면**, 해당 조합은 정답 후보에서 탈락입니다.
- 따라서 `is_possible`을 `False`로 설정하여 "이 조합은 불가능함"을 표시하고, `break`를 통해 남은 힌트들에 대한 불필요한 확인 과정을 즉시 중단(Early Exit)합니다.

**구체적인 예시**:
`n = 10`, `q = [[1, 2, 3, 4, 5], [1, 2, 6, 7, 8]]`, `ans = [5, 0]` 이라고 가정하고,
현재 검사 중인 **후보 조합이 `[1, 2, 3, 4, 5]`** 인 상황입니다.

1.  **힌트 1**: 시도 `[1, 2, 3, 4, 5]` 결과 `5`개 일치
    -   후보와 시도의 교집합: `{1, 2, 3, 4, 5}` (5개)
    -   `5 == 5` 이므로 **통과**. (다음 힌트 확인)

2.  **힌트 2**: 시도 `[1, 2, 6, 7, 8]` 결과 `0`개 일치
    -   후보와 시도의 교집합: `{1, 2}` (2개)
    -   `2 != 0` 이므로 **실패**.
    -   이 후보는 힌트 2를 만족하지 못하므로 비밀 코드가 아닙니다.
    -   즉시 `is_possible = False`로 설정하고 `break`합니다. (남은 힌트는 확인할 필요 없음)

