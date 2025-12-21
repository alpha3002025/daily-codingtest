# 문자열 내림차순으로 배치하기

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12917)

문자열 `s`를 문자 단위로 내림차순 정렬하여 반환하세요.
(대문자는 소문자보다 작게 취급됨 -> 아스키 코드상 당연함)

## 해결 전략
`sorted(s, reverse=True)` 후 `join`.

### 알고리즘 순서
1. return `"".join(sorted(s, reverse=True))`

## Python 코드

```python
def solution(s):
    return "".join(sorted(s, reverse=True))
```

## 배운 점 / 팁
- **정렬 순서**: 파이썬은 기본적으로 아스키 코드 순으로 정렬하므로 'Z' < 'a'입니다. 따라서 내림차순 정렬 시 소문자가 먼저 오고 대문자가 나중에 옵니다. `gfedcbZ`
