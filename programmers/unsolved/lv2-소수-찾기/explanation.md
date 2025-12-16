# 소수 찾기

## 문제 설명
한 자리 숫자가 적힌 종이 조각들이 주어집니다. 이 조각들을 붙여 만들 수 있는 소수의 개수를 구하는 문제입니다.
예: "17" -> 7(소수), 17(소수), 71(소수)...

### 핵심 개념
1.  **순열 (Permutations)**: 주어진 숫자 조각으로 만들 수 있는 모든 숫자를 생성합니다. 길이가 1인 것부터 N인 것까지 모두 시도합니다.
2.  **소수 판별 (Primality Test)**: 에라토스테네스의 체 또는 제곱근까지만 나누어보는 방식을 사용하여 소수인지 확인합니다.
3.  **집합 (Set)**: "011"과 "11"은 같은 숫자 11입니다. 중복을 제거하기 위해 집합 자료구조를 사용합니다.

## Python 풀이

```python
from itertools import permutations
import math

def is_prime(n):
    if n < 2: 
        return False
    # 2부터 제곱근까지만 나눔 (효율성)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    num_set = set()
    
    # 1. 모든 길이의 순열 생성
    # 예: numbers="17" -> (1), (7), (1,7), (7,1)
    for i in range(1, len(numbers) + 1):
        perms = permutations(list(numbers), i)
        for p in perms:
            # 튜플을 합쳐서 정수로 변환 ("011" -> 11)
            num_val = int("".join(p))
            num_set.add(num_val)
            
    # 2. 소수 판별
    count = 0
    for num in num_set:
        if is_prime(num):
            count += 1
            
    return count
```

### 코드 설명
- `permutations`로 가능한 숫자 조합을 모두 만들고 `set`에 넣어 중복을 제거합니다.
- `int("".join(p))`를 통해 문자열 조합을 정수로 바꿉니다. 이때 앞의 '0'이 자연스럽게 처리됩니다.
- 만들어진 각 숫자에 대해 소수인지 확인합니다. 숫자의 크기가 최대 $10^7$ 미만이므로, 개별 판별($O(\sqrt{N})$)을 반복해도 시간 내에 충분합니다.
