# 약수의 합

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12928)

정수 `n`의 모든 약수를 더한 값을 반환하세요.
(0인 경우 0 반환)

## 해결 전략
1. 0 처리.
2. 1부터 `n`까지 순회하며 나누어 떨어지면 더함. (O(N))
- `n`이 3000 이하이므로 O(N)으로 충분합니다.

### 알고리즘 순서
1. if `n == 0`: return 0
2. return `sum([i for i in range(1, n + 1) if n % i == 0])`

## Python 코드

```python
def solution(n):
    # 리스트 컴프리헨션 + sum
    return sum(i for i in range(1, n + 1) if n % i == 0)
```

## 배운 점 / 팁
- **효율성**: N이 커지면 `sqrt(N)`까지만 반복해야 합니다. (이 문제는 작아서 불필요)
