# 자릿수 더하기

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12931)

자연수 `N`의 각 자릿수의 합을 구하세요.
예: `123` -> `6`

## 해결 전략
문자열 변환 후 각 자릿수 합산.

### 알고리즘 순서
1. return `sum(map(int, str(n)))`

## Python 코드

```python
def solution(n):
    return sum(int(digit) for digit in str(n))
```

## 배운 점 / 팁
- **Map vs Generator**: `sum(map(int, str(n)))`과 `sum([int(i) for i in str(n)])` 모두 가능합니다.
