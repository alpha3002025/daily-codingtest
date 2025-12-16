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
def get_gcd_list(nums):
    g = nums[0]
    for i in range(1, len(nums)):
        g = math.gcd(g, nums[i])
    return g

def solution(arrayA, arrayB):
    gcd_a = get_gcd_list(arrayA)
    gcd_b = get_gcd_list(arrayB)
    
    answer = 0
    
    # 조건 1: gcd_a로 arrayB 요소들을 나눌 수 없어야 함
    if all(num % gcd_a != 0 for num in arrayB):
        answer = max(answer, gcd_a)
        
    # 조건 2: gcd_b로 arrayA 요소들을 나눌 수 없어야 함
    if all(num % gcd_b != 0 for num in arrayA):
        answer = max(answer, gcd_b)
        
    return answer
```
