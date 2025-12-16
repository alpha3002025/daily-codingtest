# [PCCP 기출문제] 4번 / 수식 복원하기

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/340210)

당신은 2진법에서 9진법 사이의 진법 시스템 중 하나를 사용하는 수식들을 복원해야 합니다.
주어진 수식들은 "A + B = C" 또는 "A - B = C" 형태이며, 10진법이 아닌 특정 진법으로 표기되어 있습니다.
이 중 일부 수식은 결괏값이 "X"로 지워져 있습니다.
당신은 주어진 **완전한 수식**들을 분석하여 가능한 **진법들의 집합**을 추론하고, 이를 바탕으로 지워진 수식("X")의 결과를 복원해야 합니다.

만약 가능한 진법이 여러 개이고, 그에 따라 결괏값이 달라진다면 "?"를 출력해야 합니다. 하지만 가능한 모든 진법에서 결괏값이 동일하다면 그 값을 출력합니다.

## 핵심 개념
### 1. 진법 변환 (Base Conversion)
이 문제의 핵심은 특정 문자열을 $N$진수로 해석하여 10진수 값으로 변환하고, 연산 결과를 다시 $N$진수 문자열로 변환하는 것입니다.
- 파이썬의 `int(value, base)`를 사용하면 쉽게 $N$진수를 10진수로 변환할 수 있습니다.
- 반대로 10진수를 $N$진수 문자열로 변환하는 기능은 직접 구현해야 합니다.

### 2. 가능한 진법 추론 (Deduction)
가능한 진법(2~9) 중 어떤 진법이 유효한지 좁혀나가는 과정이 필요합니다.
1. **숫자 제약**: 수식에 등장하는 가장 큰 숫자가 $k$라면, 진법은 최소 $k+1$ 이상이어야 합니다. (예: 5가 등장하면 최소 6진법)
2. **수식 검증**: 결괏값이 있는 모든 완전한 수식에 대해, 해당 진법에서 수식이 성립하는지 확인합니다. 모든 완전한 수식을 만족하는 진법만이 후보가 됩니다.

### 3. 결과 도출
모든 후보 진법에 대해 지워진 수식을 계산해 봅니다.
- 유일한 결과가 나온다면 그 값을 채웁니다.
- 서로 다른 결과가 나온다면 "?"를 채웁니다.

## 추천 풀이 (Python)

```python
def to_base(number, base):
    """10진수 number를 base진법 문자열로 변환"""
    if number == 0:
        return "0"
    digits = []
    while number:
        digits.append(str(number % base))
        number //= base
    return "".join(digits[::-1])

def solution(expressions):
    # 1. 수식 분류 및 최대 자릿수 찾기
    completed = []
    problems = []
    max_digit = 0
    
    for expr in expressions:
        A, op, B, _, C = expr.split()
        
        # 등장하는 모든 숫자 중 최댓값 갱신 for 진법 하한선
        for char in A + B + (C if C != "X" else ""):
            if char.isdigit():
                max_digit = max(max_digit, int(char))
                
        if C == "X":
            problems.append([A, op, B])
        else:
            completed.append([A, op, B, C])

    # 2. 가능한 진법 후보 찾기 (min_base ~ 9)
    # 최소 진법은 (등장한 가장 큰 숫자 + 1). 기호만 있는 경우는 드물지만 최소 2진법.
    min_base = max(2, max_digit + 1)
    possible_bases = []
    
    for base in range(min_base, 10):
        is_valid = True
        for A, op, B, C in completed:
            val_a = int(A, base)
            val_b = int(B, base)
            val_c = int(C, base)
            
            if op == '+':
                if val_a + val_b != val_c:
                    is_valid = False
                    break
            else: # op == '-'
                if val_a - val_b != val_c:
                    is_valid = False
                    break
        
        if is_valid:
            possible_bases.append(base)
            
    # 3. 문제 풀기 (가능한 베이스들을 기반으로 결과 추론)
    answer = []
    for A, op, B in problems:
        results = set()
        for base in possible_bases:
            val_a = int(A, base)
            val_b = int(B, base)
            
            if op == '+':
                res_dec = val_a + val_b
            else:
                res_dec = val_a - val_b
            
            results.add(to_base(res_dec, base))
        
        # 결과가 유일하면 그 값, 아니면 ?
        if len(results) == 1:
            final_res = results.pop()
        else:
            final_res = "?"
            
        answer.append(f"{A} {op} {B} = {final_res}")
        
    return answer
```

## 코드 설명
1.  **전처리**: 입력된 `expressions` 리스트를 순회하며 완전한 수식(`completed`)과 풀어야 할 수식(`problems`)으로 나눕니다. 이 과정에서 등장하는 숫자 중 최댓값(`max_digit`)을 찾아 가능한 최소 진법(`min_base`)을 결정합니다.
2.  **후보 진법 탐색**: `min_base`부터 9까지의 모든 진법에 대해, `completed`에 있는 모든 수식이 성립하는지 검사합니다. 모두 성립하는 진법만 `possible_bases` 리스트에 담습니다.
3.  **결과 추론**: `problems`에 있는 각 수식에 대해, `possible_bases`에 있는 모든 진법을 적용하여 결괏값을 구합니다.
    *   구한 결괏값들(`results` 집합)의 개수가 1개라면, 진법에 상관없이 답이 정해지므로 해당 값을 "X" 자리에 채웁니다.
    *   결괏값이 여러 종류라면 "?"를 채웁니다.
4.  **출력 형식**: 문제에서 요구하는 형식인 "A + B = 결과" 문자열 리스트로 변환하여 반환합니다.
