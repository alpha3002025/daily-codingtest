# 두 개 뽑아서 더하기

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/68644)

정수 배열 `numbers`에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 **모든 수를 오름차순**으로 담아 반환하세요.

## 해결 전략
모든 가능한 두 수의 조합을 구하고, 그 합을 집합(`set`)에 넣어 중복을 제거한 뒤 정렬하면 됩니다.

### 알고리즘 순서
1. `answer` = `set()`
2. `itertools.combinations(numbers, 2)` 순회:
    - 합을 `answer`에 추가.
3. `sorted(list(answer))` 반환.

## Python 코드

```python
from itertools import combinations

def solution(numbers):
    answer = set()
    
    # 2개 뽑아서 더하기 (모든 조합)
    for a, b in combinations(numbers, 2):
        answer.add(a + b)
        
    # 오름차순 정렬
    return sorted(list(answer))
```

## 배운 점 / 팁
- **Set**: 중복 제거에 가장 효과적인 자료구조입니다.
- **Sorted**: `sorted()` 함수는 이터러블 객체를 받아 정렬된 **리스트**를 반환합니다.
