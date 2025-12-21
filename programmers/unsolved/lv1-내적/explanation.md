# 내적

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/70128)

길이가 같은 두 1차원 정수 배열 `a`, `b`의 내적(Dot Product)을 구하세요.
내적 = `a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1]`

## 해결 전략
단순 반복문으로 곱의 합을 구합니다.
`zip`을 사용하거나 리스트 컴프리헨션을 사용하면 한 줄로도 가능합니다.

### 알고리즘 순서
1. `answer` = `sum(x * y for x, y in zip(a, b))`
2. 반환.

## Python 코드

```python
def solution(a, b):
    # zip으로 같은 인덱스끼리 묶어서 곱한 뒤 합산
    return sum(x * y for x, y in zip(a, b))
```

## 배운 점 / 팁
- **수학적 정의 구현**: 내적의 정의를 그대로 코드로 옮기면 되는 기초 문제입니다.
