# 소수 만들기

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12977)

숫자 배열 `nums`에서 서로 다른 3개를 골라 더했을 때, 그 합이 **소수(Prime Number)**가 되는 경우의 수를 구하세요.

## 해결 전략
1. **조합 생성**: 3개를 고르는 모든 경우의 수는 `itertools.combinations`로 구합니다.
2. **소수 판별**: 합이 소수인지 확인합니다.
    - 숫자의 합은 최대 3000 (1000*3) 이하이므로, 단순한 `sqrt(N)` 판별법으로도 충분히 빠릅니다.

### 알고리즘 순서
1. `answer` = 0
2. `combinations(nums, 3)` 순회:
    - `total` = `sum(trio)`
    - `is_prime(total)`인지 확인:
        - `2`부터 `int(total**0.5)`까지 나누어 떨어지는지 검사.
        - 나누어 떨어지면 소수 아님.
    - 소수면 `answer += 1`
3. 반환.

## Python 코드

```python
from itertools import combinations

def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    
    # 서로 다른 3개 숫자 뽑기
    for combo in combinations(nums, 3):
        total_sum = sum(combo)
        if is_prime(total_sum):
            answer += 1
            
    return answer
```

## 배운 점 / 팁
- **소수 판별**: `range(2, int(num**0.5) + 1)`까지만 검사하면 됩니다. 에라토스테네스의 체를 쓸 수도 있지만, 범위가 작을 땐 함수 하나로 해결하는 게 더 빠를 수 있습니다.
