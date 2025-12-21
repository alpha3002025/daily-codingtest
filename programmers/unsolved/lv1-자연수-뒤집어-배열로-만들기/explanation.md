# 자연수 뒤집어 배열로 만들기

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12932)

자연수 `n`을 뒤집어 각 자리 숫자를 원소로 가지는 배열로 반환하세요.
예: `12345` -> `[5, 4, 3, 2, 1]`

## 해결 전략
문자열 변환 후 뒤집고, 각 문자를 정수로 변환(`map`)합니다.

### 알고리즘 순서
1. `s` = `str(n)[::-1]` (뒤집기)
2. return `list(map(int, s))`

## Python 코드

```python
def solution(n):
    # 뒤집어진 문자열을 만들고, map으로 각 문자를 int로 변환
    return list(map(int, str(n)[::-1]))
```

## 배운 점 / 팁
- **Slicing**: `[::-1]`은 시퀀스를 뒤집는 가장 파이썬다운 방법(Idiomatic Python)입니다.
