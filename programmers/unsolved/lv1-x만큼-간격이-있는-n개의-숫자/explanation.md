# x만큼 간격이 있는 n개의 숫자

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12954)

정수 `x`와 자연수 `n`을 입력받아, `x`부터 시작해 `x`씩 증가하는 숫자를 `n`개 지니는 리스트를 반환하세요.

## 해결 전략
등차수열 생성 문제입니다.
`range` 함수나 리스트 컴프리헨션을 사용합니다.
`x`씩 증가하므로 `i`번째 수는 `x * (i + 1)` 또는 `x + x*i` 형태입니다.

### 알고리즘 순서
1. `return [x * i for i in range(1, n + 1)]`
    - 주의: `range(x, x*n + x, x)`는 `x=0`일 때 무한 루프나 에러가 날 수 있음. (step=0 불가능)

## Python 코드

```python
def solution(x, n):
    # x부터 시작, n개. 즉 x*1, x*2, ... x*n
    return [x * i for i in range(1, n + 1)]
```

## 배운 점 / 팁
- **예외 케이스**: `x`가 0일 수 있습니다. 등차수열의 공차가 0인 경우(`0, 0, 0...`)도 문제없이 처리되어야 합니다.
