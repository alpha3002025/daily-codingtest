# 숫자 카드 나누기

## 문제 설명
철수와 영희가 숫자 카드를 가지고 있습니다.
다음 두 조건 중 하나를 만족하는 가장 큰 양의 정수 `a`를 구해야 합니다.
1. `a`가 철수의 모든 카드를 나눌 수 있고, 영희의 모든 카드를 나눌 수 없음.
2. `a`가 영희의 모든 카드를 나눌 수 있고, 철수의 모든 카드를 나눌 수 없음.
만족하는 `a`가 없으면 0을 반환합니다.

## 풀이 개념
**최대공약수 (GCD)**를 활용하는 문제입니다.
"모든 카드를 나눌 수 있는 수"는 해당 카드들의 공약수 중 가장 큰 것, 즉 모든 카드의 **최대공약수**입니다.

1. 철수 카드의 최대공약수 `gcd_A`를 구합니다.
2. 영희 카드의 최대공약수 `gcd_B`를 구합니다.
3. 조건 1 확인: `gcd_A`가 영희의 카드 중 하나라도 나눌 수 있다면 탈락. 나눌 수 없다면 `gcd_A`는 후보.
4. 조건 2 확인: `gcd_B`가 철수의 카드 중 하나라도 나눌 수 있다면 탈락. 나눌 수 없다면 `gcd_B`는 후보.
5. 두 후보 중 더 큰 값을 반환합니다. 둘 다 없으면 0.

## 코드 (Python)

```python
import math

# 여러 수의 최대공약수 구하기 (reduce 활용 가능)
def get_gcd_from_list(nums):
    g = nums[0]
    for i in range(1, len(nums)):
        g = math.gcd(g, nums[i])
    return g

def solution(arrayA, arrayB):
    gcd_a = get_gcd_from_list(arrayA)
    gcd_b = get_gcd_from_list(arrayB)
    
    answer = 0
    
    # 조건 1: gcd_a로 arrayB 요소들을 나눌 수 없어야 함
    if all(num % gcd_a != 0 for num in arrayB):
        answer = max(answer, gcd_a)
        
    # 조건 2: gcd_b로 arrayA 요소들을 나눌 수 없어야 함
    if all(num % gcd_b != 0 for num in arrayA):
        answer = max(answer, gcd_b)
        
    return answer
```

## 참고 문법: `math.gcd`
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


## 나의 풀이
### 2025/12/19 (1)
```python
import math

def gcd_from_list(numbers):
    curr = numbers[0]
    for i in range(1, len(numbers)):
        curr = math.gcd(curr, numbers[i])
    return curr


def solution(arrayA, arrayB):
    gcdA = gcd_from_list(arrayA)
    gcdB = gcd_from_list(arrayB)
    
    foundA = False
    a = 0
    for n in arrayB:
        if n % gcdA == 0:
            foundA = True
            break
    
    foundB = False
    for n in arrayA:
        if n % gcdB == 0:
            foundB = True
            break
    
    return 0 if foundA and foundB else max(gcdA, gcdB)
```