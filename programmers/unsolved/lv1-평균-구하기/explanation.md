# 평균 구하기

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12944)

정수 배열 `arr`의 평균값을 반환하세요.

## 해결 전략
평균 = 총합 / 개수.

### 알고리즘 순서
1. return `sum(arr) / len(arr)`

## Python 코드

```python
def solution(arr):
    return sum(arr) / len(arr)
```

## 배운 점 / 팁
- **기초 통계**: `sum`과 `len`은 파이썬 내장 함수의 핵심입니다.
