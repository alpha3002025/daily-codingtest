# 문자열 내 마음대로 정렬하기

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12915)

문자열 리스트 `strings`를 각 문자열의 `n`번째 글자를 기준으로 정렬하세요.
`n`번째 글자가 같으면 사전순으로 정렬합니다.

## 해결 전략
정렬의 `key`를 튜플로 지정하여 1순위, 2순위 정렬 조건을 설정합니다.
`key=lambda x: (x[n], x)`

### 알고리즘 순서
1. `strings.sort(key=lambda x: (x[n], x))`
2. return `strings`

## Python 코드

```python
def solution(strings, n):
    # (n번째 글자, 전체 문자열) 순으로 정렬 키 지정
    return sorted(strings, key=lambda x: (x[n], x))
```

## 배운 점 / 팁
- **다중 정렬 조건**: `lambda`에서 튜플을 반환하면 앞에서부터 순서대로 우선순위를 가집니다.
