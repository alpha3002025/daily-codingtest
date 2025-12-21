# 정수 제곱근 판별

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12934)

양의 정수 `n`이 어떤 양의 정수 `x`의 제곱(`x^2`)이라면 `(x+1)^2`을 반환하고, 아니라면 `-1`을 반환하세요.

## 해결 전략
제곱근을 구하고, 그 값이 정수인지 판별합니다.
`sqrt = n ** 0.5`
- 정수 판별: `sqrt % 1 == 0` 또는 `int(sqrt) == sqrt`

### 알고리즘 순서
1. `sqrt` = `n ** 0.5`
2. `if sqrt == int(sqrt)`:
    - return `(sqrt + 1) ** 2`
3. else:
    - return `-1`

## Python 코드

```python
def solution(n):
    sqrt = n ** 0.5
    
    # 제곱근이 정수인지 확인 (예: 11.0 == 11)
    if sqrt == int(sqrt):
        return (sqrt + 1) ** 2
    
    return -1
```

## 배운 점 / 팁
- **부동소수점 비교**: 단순히 `is_integer()` 메소드를 쓸 수도 있습니다 (`(n**0.5).is_integer()`).
