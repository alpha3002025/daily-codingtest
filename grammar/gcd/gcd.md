`math.gcd`
- **기능**: 두 정수의 최대공약수(Greatest Common Divisor)를 반환합니다.
- **Python 3.9 이상**: `math.gcd(a, b, c, ...)` 처럼 3개 이상의 인자도 한 번에 받을 수 있습니다. (코딩테스트 환경 버전에 주의 필요, 보통 `3.8` 이하인 경우 두 개씩 연쇄적으로 해야 함)
- **사용 예시**:
```python
import math
print(math.gcd(12, 18)) # 6
print(math.gcd(0, 5))   # 5 (0과의 gcd는 0이 아닌 수 자기 자신)
```
- **여러 수의 GCD 구하기**:
  - Python 3.9+: `math.gcd(*array)`
  - Python 3.8 이하: 반복문 사용 (`g = gcd(g, next_val)` 형태) 또는 `functools.reduce(math.gcd, array)` 사용.
