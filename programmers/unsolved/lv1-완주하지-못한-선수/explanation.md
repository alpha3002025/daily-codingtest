# 완주하지 못한 선수

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42576)

참여자 `participant`와 완주자 `completion`이 주어집니다.
완주하지 못한 **단 한 명**의 선수를 찾으세요. 동명이인이 있을 수 있습니다.

## 해결 전략
해시(Hash) 자료구조를 사용하는 것이 가장 효율적(`O(N)`)입니다.
1. `participant`의 이름을 카운트합니다.
2. `completion`에 있는 이름의 카운트를 뺍니다.
3. 카운트가 `1`인 이름이 완주하지 못한 선수입니다.
(정렬 후 비교하는 `O(N log N)` 방법도 있지만 해시가 더 빠릅니다.)

### 알고리즘 순서
1. `cnt` = `collections.Counter(participant)`
2. `cnt` -= `collections.Counter(completion)` (Counter끼리 뺄셈 가능)
3. `list(cnt.keys())[0]` 반환.

## Python 코드

```python
from collections import Counter

def solution(participant, completion):
    # 참여자 카운트
    # 예: {'leo': 1, 'kiki': 1, 'eden': 1}
    p_cnt = Counter(participant)
    
    # 완주자 카운트 빼기
    c_cnt = Counter(completion)
    
    # 차집합 (남은 1명이 완주 못한 사람)
    result = p_cnt - c_cnt
    
    # 키 리스트 중 첫 번째 반환
    return list(result.keys())[0]
```

## 배운 점 / 팁
- **Counter 객체의 연산**: 파이썬 `Counter`는 산술 연산(`-`)을 지원하여, 두 리스트의 요소 차이를 아주 쉽게 구할 수 있습니다.
- **Hash Table**: 문자열 검색/카운팅 문제는 십중팔구 해시(딕셔너리)가 정답입니다.
