# 최대공약수와 최소공배수

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12940)

두 수 `n`, `m`의 최대공약수(GCD)와 최소공배수(LCM)를 구해 `[GCD, LCM]` 형태로 반환하세요.

## 해결 전략
1. **최대공약수**: 유클리드 호제법(Euclidean algorithm)을 사용하거나 `math.gcd`를 씁니다.
2. **최소공배수**: `(n * m) // GCD` 공식으로 구합니다.

### 알고리즘 순서
1. `import math`
2. `gcd_val` = `math.gcd(n, m)`
3. `lcm_val` = `(n * m) // gcd_val`
4. return `[gcd_val, lcm_val]`

## Python 코드

```python
import math

def solution(n, m):
    # 최대공약수
    gcd_val = math.gcd(n, m)
    
    # 최소공배수 = 두 수의 곱 / 최대공약수
    lcm_val = (n * m) // gcd_val
    
    return [gcd_val, lcm_val]
```

## 배운 점 / 팁
- **수학 공식**: `LCM(a, b) * GCD(a, b) = a * b` 관계식은 반드시 기억해야 합니다.
