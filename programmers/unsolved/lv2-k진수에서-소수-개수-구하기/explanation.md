# k진수에서 소수 개수 구하기

## 문제 설명
양의 정수 n을 k진수로 변환했을 때, 변환된 수 안에 있는 **소수(Prime Number)**의 개수를 구하는 문제입니다. 단, 소수는 0을 포함하지 않는 조건(0P0, P0, 0P, P)으로 끊어서 판별해야 합니다. 즉, **0을 기준으로 분리(split)**하여 나온 숫자들 각각이 소수인지 확인하면 됩니다.

### 핵심 개념
1.  **진수 변환**: 정수 n을 k진수 문자열로 변환해야 합니다. Python 내장 함수 `oct`, `hex` 등은 8, 16진수만 지원하므로, 직접 구현하거나 `divmod`를 사용합니다.
2.  **문자열 분리 (Split)**: 조건에 따르면 "0"을 기준으로 숫자를 끊어서 봅니다. Python의 `split('0')`을 사용하면 쉽게 분리할 수 있습니다.
3.  **소수 판별 (Primality Test)**: 분리된 숫자가 소수인지 판별합니다. $N$의 크기가 클 수 있으므로 $O(\sqrt{N})$ 시간 복잡도의 알고리즘을 사용해야 시간 초과를 피할 수 있습니다.

## Python 풀이

```python
import math

def is_prime(num):
    """소수 판별 함수 (O(sqrt(N)))"""
    if num < 2:
        return False
    # 2부터 제곱근까지만 확인
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def to_k_base(n, k):
    """정수 n을 k진수 문자열로 변환"""
    result = ''
    while n > 0:
        n, mod = divmod(n, k)
        result += str(mod)
    # 역순으로 기록되므로 뒤집어서 반환
    return result[::-1]

def solution(n, k):
    # 1. k진수로 변환
    k_num_str = to_k_base(n, k)
    
    # 2. 0을 기준으로 분리
    # 빈 문자열('')이 생길 수 있으므로 필터링 필요
    candidates = k_num_str.split('0')
    
    count = 0
    for s in candidates:
        if not s: # 빈 문자열 건너뛰기
            continue
            
        num = int(s)
        # 3. 소수 판별
        if is_prime(num):
            count += 1
            
    return count
```

### 코드 설명
- `to_k_base`: $n$을 $k$로 계속 나누며 나머지를 기록하여 k진수를 구합니다.
- `split('0')`: 문제의 복잡한 조건(0P0, P0 등)은 결국 "0을 기준으로 쪼갰을 때 나오는 숫자가 소수인가?"와 같습니다.
- **주의사항**: `split` 결과에 `''` (빈 문자열)이 포함될 수 있습니다. `int()` 변환 전 반드시 체크해야 합니다. (예: `110011` -> `['11', '', '11']`)
- `is_prime`: 1은 소수가 아님을 처리하고, 2부터 제곱근까지만 나눠보며 효율적으로 판별합니다. 문제에서 $n$이 최대 1,000,000인데, k진수로 바꾸면 자릿수가 늘어나 숫자가 매우 커질 수 있습니다. 따라서 $O(N)$ 판별법은 시간 초과가 발생할 수 있습니다.
