# 문자열 내 p와 y의 개수

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12916)

문자열 `s`에서 'p'의 개수와 'y'의 개수가 같은지 확인하세요. (대소문자 구분 없음)

## 해결 전략
전부 소문자로 바꾼 뒤 개수를 셉니다.

### 알고리즘 순서
1. `s` = `s.lower()`
2. return `s.count('p') == s.count('y')`

## Python 코드

```python
def solution(s):
    s = s.lower()
    return s.count('p') == s.count('y')
```

## 배운 점 / 팁
- **정규화**: 대소문자 구분 없이 비교할 땐 `lower()`나 `upper()`로 통일하는 것이 기본입니다.
