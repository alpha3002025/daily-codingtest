# 문자열 다루기 기본

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12918)

문자열 `s`의 길이가 4 혹은 6이고, 숫자로만 구성되어 있는지 확인하세요.

## 해결 전략
두 가지 조건을 모두 검사해야 합니다.
1. `len(s) in [4, 6]`
2. `s.isdigit()`

### 알고리즘 순서
1. return `(len(s) == 4 or len(s) == 6) and s.isdigit()`

## Python 코드

```python
def solution(s):
    return (len(s) == 4 or len(s) == 6) and s.isdigit()
```

## 배운 점 / 팁
- **isdigit()**: 문자열이 숫자로만 구성되었는지 확인하는 가장 확실한 방법입니다.
