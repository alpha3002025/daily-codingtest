# 삼총사

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/131705)

학생들의 번호(`number`)가 주어집니다. 이 중 **3명의 번호를 더했을 때 0**이 되는 경우(삼총사)의 수를 구하세요.

## 해결 전략
주어진 배열에서 3개를 뽑는 **조합(Combination)** 문제입니다.
학생 수(배열 길이)가 최대 13명으로 매우 작으므로, 모든 조합을 다 확인해봐도(`13C3`) 연산량이 매우 적습니다.
`itertools.combinations`를 사용하면 간단히 해결됩니다.

### 알고리즘 순서
1. `from itertools import combinations`
2. `count` = 0
3. `combinations(number, 3)` 순회 (`trio`):
    - `sum(trio) == 0` 이면 `count += 1`
4. 반환.

## Python 코드

```python
from itertools import combinations

def solution(number):
    count = 0
    # 3명을 뽑는 모든 조합 확인
    for trio in combinations(number, 3):
        if sum(trio) == 0:
            count += 1
            
    return count
```

## 배운 점 / 팁
- **itertools.combinations**: 순서와 상관없이 k개를 뽑는 경우 필수 라이브러리입니다.
- **제약 조건 확인**: 입력 크기가 작으면(N <= 20 정도) 완전 탐색(Brute Force)이 가장 빠르고 정확한 해법입니다.
