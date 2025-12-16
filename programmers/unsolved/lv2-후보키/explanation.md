# 후보키

## 문제 설명
관계형 데이터베이스에서 후보키(Candidate Key)는 다음 두 가지 성질을 만족해야 합니다.
1.  **유일성 (Uniqueness)**: 릴레이션에 있는 모든 튜플에 대해 유일하게 식별되어야 함.
2.  **최소성 (Minimality)**: 유일성을 만족하는 키의 속성 중 불필요한 속성이 없어야 함.

주어진 `relation`에 대해 후보키의 최대 개수를 구하는 문제입니다.

### 핵심 개념
1.  **속성 조합 (Combinations)**: 컬럼의 개수가 최대 8개로 매우 적습니다.
    - 가능한 모든 속성 조합을 시도해볼 수 있습니다. ($\sum_{k=1}^8 \binom{8}{k} = 2^8 - 1 = 255$가지)
2.  **유일성 검사**: 선택된 속성들로 만들어진 튜플들의 행 집합(Set) 크기가 전체 행 개수와 같은지 확인합니다.
3.  **최소성 검사**: 이미 후보키로 선정된 조합이 현재 조합의 부분집합인지 확인합니다.
    - 예: `(학번)`이 후보키라면, `(학번, 이름)`은 유일성은 만족하지만 최소성을 만족하지 않아 후보키가 아닙니다.

## Python 풀이

```python
from itertools import combinations

def solution(relation):
    row_len = len(relation)
    col_len = len(relation[0])
    
    # 1. 모든 가능한 속성 인덱스의 조합을 생성 (길이 1부터 col_len까지)
    candidates = []
    for i in range(1, col_len + 1):
        candidates.extend(combinations(range(col_len), i))
        
    unique_keys = []
    
    for comb in candidates:
        # 2. 유일성 검사
        # 선택된 컬럼(comb)들로만 이루어진 튜플 리스트 생성
        # 예: comb=(0, 2) -> 각 행의 0번, 2번 값만 뽑음
        tmp = [tuple(item[i] for i in comb) for item in relation]
        
        # set으로 만들어서 중복 제거 후 길이 비교
        if len(set(tmp)) == row_len:
            # 유일성 만족
            
            # 3. 최소성 검사
            # 이미 등록된 후보키(key)가 현재 조합(comb)의 부분집합이면 탈락
            is_minimal = True
            for key in unique_keys:
                # key가 comb의 부분집합인지 확인 (issubset)
                if set(key).issubset(set(comb)):
                    is_minimal = False
                    break
            
            if is_minimal:
                unique_keys.append(comb)
                
    return len(unique_keys)
```

### 코드 설명
- `candidates`: 모든 컬럼 조합을 길이 순서대로(`1` -> `col`) 생성합니다.
    - 예: `[(0), (1), (2), (0,1), (0,2) ...]`
- 길이 순서대로 검사하기 때문에 **최소성** 검사가 쉽습니다.
    - 길이가 1인 `(0)`이 유일성을 만족해서 `unique_keys`에 들어갔다면, 나중에 나오는 `(0, 1)`은 `(0).issubset((0,1))` 이 참이 되어 걸러집니다.
    - 만약 길이 순서가 아니었다면, `(0,1)`이 먼저 들어갔을 때 나중에 `(0)`이 들어오면 `(0,1)`을 제거해야 하는 복잡함이 생깁니다.
- `set(key).issubset(set(comb))`: Python의 집합 연산을 활용하여 부분집합 여부를 판단합니다.

### 주의할 점
- 부분집합 검사 시 `set`을 사용해야 합니다. 튜플이나 리스트는 순서가 중요하지만, 키의 속성 집합은 순서가 상관없으므로 `set`으로 변환하여 비교합니다.
