# [1차] 뉴스 클러스터링

## 문제 설명
두 문자열의 자카드 유사도(Jaccard Similarity)를 구하는 문제입니다.
자카드 유사도 $J(A, B) = \frac{|A \cap B|}{|A \cup B|}$.
- 문자열을 두 글자씩 끊어서 다중집합(Multi-Set)을 만듭니다. (중복 허용)
- 영문자만 유효하며, 대소문자는 구분하지 않습니다.
- 예: `FRANCE`, `FRENCH` -> `{'FR', 'RA', 'AN', 'NC', 'CE'}`, `{'FR', 'RE', 'EN', 'NC', 'CH'}`
    - 교집합: `{'FR', 'NC'}`
    - 합집합: `{'FR', 'RA', 'AN', 'NC', 'CE', 'RE', 'EN', 'CH'}`

### 핵심 개념
1.  **다중집합 (Multiset)**: 일반적인 집합(`set`)은 중복을 제거하므로 사용할 수 없습니다. 리스트(`list`)나 `Counter`를 사용해야 합니다.
2.  **교집합/합집합 계산**:
    - 교집합 개수: 같은 원소에 대해 `min(count_A, count_B)` 만큼 존재.
    - 합집합 개수: 같은 원소에 대해 `max(count_A, count_B)` 만큼 존재.
3.  **문자열 처리**: 영문자 쌍만 추출하고 소문자로 통일(`lower()`). `isalpha()` 사용.

## Python 풀이

```python
from collections import Counter

def make_multiset(s):
    # 두 글자씩 끊어서 영문자인 경우만 리스트에 추가
    result = []
    s = s.lower()
    for i in range(len(s) - 1):
        token = s[i:i+2]
        if token.isalpha():
            result.append(token)
    return result

def solution(str1, str2):
    # 1. 다중집합 생성
    list1 = make_multiset(str1)
    list2 = make_multiset(str2)
    
    # 두 집합이 모두 비어있으면 유사도는 1
    if not list1 and not list2:
        return 65536
    
    # 2. Counter를 이용한 다중집합 연산
    c1 = Counter(list1)
    c2 = Counter(list2)
    
    # 3. 교집합 및 합집합 원소 개수 계산
    # 교집합: 두 카운터에 모두 있는 키에 대해 min count
    # 합집합: 모든 키에 대해 max count
    
    intersection_keys = set(c1.keys()) & set(c2.keys())
    union_keys = set(c1.keys()) | set(c2.keys())
    
    inter_count = sum(min(c1[k], c2[k]) for k in intersection_keys)
    union_count = sum(max(c1[k], c2[k]) for k in union_keys)
    
    # 4. 자카드 유사도 계산
    similarity = inter_count / union_count
    
    return int(similarity * 65536)
```

### 코드 설명
- `Counter` 객체는 다중집합 연산을 위한 메서드 `&`(교집합), `|`(합집합)을 지원하지만, 이 연산자들은 카운트가 `min`, `max`로 동작하는 것이 맞습니다.
- `(c1 & c2).elements()` 개수를 세도 되지만, 직접 키를 순회하며 `min`을 더하는 것이 명확합니다.
- `isalpha()`를 이용해 특수문자나 숫자, 공백이 포함된 쌍을 걸러냅니다.
