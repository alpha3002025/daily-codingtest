# 하샤드 수

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12947)

양의 정수 `x`가 하샤드 수인지 판별하세요.
- 하샤드 수: `x`가 **x의 자릿수의 합**으로 나누어 떨어져야 함.

## 해결 전략
자릿수의 합을 구하는 것이 핵심입니다.
1. `x`를 문자열로 변환 -> 각 문자를 정수로 변환 -> 합(`sum`).
2. `x % sum_val == 0` 체크.

### 알고리즘 순서
1. `s` = `str(x)`
2. `digit_sum` = `sum(map(int, s))`
3. return `x % digit_sum == 0`

## Python 코드

```python
def solution(x):
    # 자릿수 합 구하기 (문자열 변환 -> 정수 리스트 -> 합)
    digit_sum = sum(int(digit) for digit in str(x))
    
    # 나누어 떨어지는지 확인
    return x % digit_sum == 0
```

## 배운 점 / 팁
- **자릿수 분해**: `str(x)`와 `map(int, ...)` 조합이 가장 간결합니다. 수학적으로 10으로 계속 나누며(`divmod`) 구할 수도 있습니다.
