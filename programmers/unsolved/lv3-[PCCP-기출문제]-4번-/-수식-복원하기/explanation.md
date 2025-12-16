# [PCCP 기출문제] 4번 / 수식 복원하기

## 문제 설명
알 수 없는 진법(2진법~9진법 중 하나)으로 쓰인 덧셈, 뺄셈 수식들이 주어집니다. 일부 수식은 결괏값이 지워져 있습니다. 주어진 완전한 수식들을 통해 가능한 진법들을 추론하고, 지워진 수식의 결과를 채워 넣어야 합니다. 만약 특정 수식의 결과가 가능한 진법들에 따라 여러 가지로 나온다면 결괏값을 `?`로 표시해야 합니다.

## 문제 해결 전략

### 1. 사용된 숫자 파악으로 최소 진법 찾기
수식에 등장하는 모든 숫자 중 가장 큰 숫자를 찾습니다. 예를 들어 `13 + 3 = 16`이 있다면 6이 등장하므로 최소 7진법 이상이어야 합니다.

### 2. 가능한 진법 후보 필터링
2진법부터 9진법까지 모든 진법을 후보로 둡니다.
완전한 수식(`A + B = C` 형태)을 이용하여 검증합니다.
- A, B, C를 각 진법 `base`로 10진수로 변환하여 연산 결과가 맞는지 확인합니다.
- 하나라도 틀리면 해당 `base`는 후보에서 탈락합니다.

### 3. 지워진 수식 채우기
남은 "가능한 진법" 후보들에 대해 각각 지워진 수식을 계산해봅니다.
- 후보 진법이 여러 개라면, 모든 후보 진법에서 계산한 결과가 "동일한지" 확인합니다.
- 모든 후보에 대해 결과가 같다면 그 값을, 하나라도 다르면 `?`를 결과로 합니다.

## Python 코드

```python
def solution(expressions):
    answer = []
    
    # 파싱: 완전한 수식(hints)과 풀어야 할 수식(targets) 분리
    hints = []
    targets = []
    
    max_digit = 0
    
    for expr in expressions:
        parts = expr.split()
        A = parts[0]
        op = parts[1]
        B = parts[2]
        C = parts[4]
        
        # 문자에 포함된 최대 숫자 찾기 (진법 하한선)
        for char in A + B:
            max_digit = max(max_digit, int(char))
        if C != 'X':
            for char in C:
                max_digit = max(max_digit, int(char))
                
        if C == 'X':
            targets.append([A, op, B])
        else:
            hints.append([A, op, B, C])
            
    # 가능한 진법 후보 (max_digit + 1 ~ 9)
    possible_bases = []
    for base in range(max_digit + 1, 10):
        is_valid = True
        for A, op, B, C in hints:
            try:
                valA = int(A, base)
                valB = int(B, base)
                valC = int(C, base)
            except ValueError:
                is_valid = False
                break
                
            if op == '+':
                if valA + valB != valC:
                    is_valid = False
            else: # '-'
                if valA - valB != valC:
                    is_valid = False
                    
            if not is_valid: break
            
        if is_valid:
            possible_bases.append(base)
            
    # 10진수 -> base진법 변환 함수
    def to_base(num, base):
        if num == 0: return "0"
        res = []
        while num > 0:
            res.append(str(num % base))
            num //= base
        return "".join(res[::-1])
    
    # 타겟 수식 계산
    for A, op, B in targets:
        results = set()
        for base in possible_bases:
            valA = int(A, base)
            valB = int(B, base)
            
            if op == '+':
                res_val = valA + valB
            else:
                res_val = valA - valB
                
            results.add(to_base(res_val, base))
            
        if len(results) == 1:
            ans_str = results.pop()
        else:
            ans_str = "?"
            
        answer.append(f"{A} {op} {B} = {ans_str}")
        
    return answer
```
