# 비밀 코드 해독
- 일단 문제 자체가 이해가 쉽지 않은 문제다. 자주 보자 이문제는.
- combination, set 으로 교집합 구하는 문제, 중복요소 찾기 문제.
- for loop 돌리면 누구나 다한다. 그런데, 머리를 쓰는 힘도 아껴가면서 써야 하는데, 이건 주어진 라이브러리를 좀 쓰는 연습도 이렇게 할 수 있구나 싶었다.

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
