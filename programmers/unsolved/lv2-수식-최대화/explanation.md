# 수식 최대화

## 문제 설명
숫자와 연산자(`+`, `-`, `*`)로 이루어진 수식이 주어집니다. 연산자의 우선순위를 자유롭게 재정의하여 만들 수 있는 결과값의 절댓값 중 가장 큰 값을 구하는 문제입니다.
단, 같은 순위의 연산자는 없으며, 무조건 3가지 연산자의 우선순위가 서로 달라야 합니다. (총 $3! = 6$가지 경우)

### 핵심 개념
1.  **순열 (Permutations)**: 3가지 연산자의 우선순위 조합 6가지를 모두 시도해봅니다. `itertools.permutations`.
2.  **문자열 파싱 (Parsing)**: 수식 문자열을 숫자와 연산자로 분리해야 합니다. 정규표현식(`re.split`)을 쓰면 편합니다.
3.  **후위 표기법 (Postfix) 또는 리스트 처리**:
    - 스택을 이용해 후위 표기법으로 바꾼 뒤 계산할 수도 있지만,
    - 연산자 종류가 적으므로, 우선순위가 높은 연산자부터 차례대로 리스트에서 찾아서 계산하고 줄여나가는(In-place reduction) 방식이 직관적입니다.

## Python 풀이 (리스트 처리 방식)

```python
import re
from itertools import permutations

def parse_expression(expression):
    # 정규식으로 숫자와 연산자 분리
    # (\D)는 숫자가 아닌 것(연산자)을 포함해서 split하라는 의미
    tokens = re.split(r'(\D)', expression)
    # 결과 예: ['100', '-', '200', '*', '300']
    return tokens

def calculate(nums, ops, priority_ops):
    # 원본 리스트 복사 (매번 계산해야 하므로)
    curr_nums = nums[:]
    curr_ops = ops[:]
    
    # 설정된 우선순위 순서대로 연산 수행
    for op in priority_ops:
        stack_nums = []
        stack_ops = []
        
        # 현재 처리할 연산자(op)를 찾아서 계산
        # 하지만 스택을 쓰는 것보다 while 루프가 나을 수 있음
        # '리스트 재조립' 방식
        idx = 0
        while idx < len(curr_ops):
            if curr_ops[idx] == op:
                # 해당 연산자이면 앞뒤 숫자 계산
                val1 = curr_nums.pop(idx)
                val2 = curr_nums.pop(idx) # val1이 빠졌으므로 같은 인덱스
                
                # eval은 보안상/성능상 좋지 않지만 코테에서는 편함
                # 여기서는 직접 구현
                if op == '+': res = val1 + val2
                elif op == '-': res = val1 - val2
                elif op == '*': res = val1 * val2
                
                curr_nums.insert(idx, res)
                
                # 연산자 리스트에서도 제거
                curr_ops.pop(idx)
                # 인덱스 증가하지 않음 (다시 그 자리부터 봐야 할 수도..는 아니지만, 뒤쪽 당겨짐)
            else:
                idx += 1
                
    return abs(curr_nums[0])

# 개선된 풀이: split을 명확히 하고 로직 단순화
def solution(expression):
    # 숫자와 연산자 분리
    # 정규식 '([^0-9])' : 숫자가 아닌 문자를 그룹으로 잡아 분리
    tokens = re.split(r'([^0-9])', expression)
    # -> ['100', '-', '200', '*', '300']
    
    operands = list(map(int, tokens[0::2])) # 짝수 인덱스는 숫자
    operators = tokens[1::2]                # 홀수 인덱스는 연산자
    
    max_value = 0
    
    # 3가지 연산자의 모든 우선순위 순열
    for prior in permutations(['+', '-', '*']):
        # 리스트 복사
        tmp_operands = operands[:]
        tmp_operators = operators[:]
        
        for op in prior:
            # 현재 우선순위인 op 연산자를 모두 처리
            idx = 0
            while idx < len(tmp_operators):
                if tmp_operators[idx] == op:
                    val1 = tmp_operands[idx]
                    val2 = tmp_operands[idx+1]
                    
                    if op == '+': res = val1 + val2
                    elif op == '-': res = val1 - val2
                    elif op == '*': res = val1 * val2
                    
                    # 계산 결과로 대체 (두 숫자를 없애고 하나 넣기)
                    tmp_operands[idx] = res
                    del tmp_operands[idx+1]
                    
                    # 사용한 연산자 제거
                    del tmp_operators[idx]
                    
                    # idx를 증가시키지 않음 (다음 연산자가 당겨져 왔으므로 확인 필요)
                else:
                    idx += 1
                    
        max_value = max(max_value, abs(tmp_operands[0]))
        
    return max_value
```

### 코드 설명
- `re.split(r'([^0-9])', expression)`: 숫자가 아닌 문자(연산자)를 기준으로 자르면서, 괄호`()`를 사용해 그 구분자 자체도 결과 리스트에 포함시킵니다.
    - 예: `100-200` -> `['100', '-', '200']`
- `permutations(['+', '-', '*'])`: `('*', '+', '-')` 등 6가지 튜플이 나옵니다.
- 내부 `while` 루프: 현재 우선순위에 해당하는 연산자 `op`를 `tmp_operators`에서 발견하면 즉시 계산합니다.
    - `tmp_operands[idx]`와 `tmp_operands[idx+1]`을 연산하고, 결과를 `tmp_operands[idx]`에 저장.
    - `tmp_operands[idx+1]` 삭제.
    - `tmp_operators[idx]` 삭제.
    - 삭제 후에는 리스트가 당겨지므로 `idx`를 증가시키지 않고 다시 검사합니다.

## 참고 - 정규식 `r'([^0-9])'` 설명
- `[]` (문자 클래스): 대괄호 안의 문자 중 하나와 매치됩니다.
- `^` (Not): 대괄호 안에서 맨 앞에 쓰이면 **"반대(Not)"**를 의미합니다.
    - `[0-9]`: 숫자와 매치
    - `[^0-9]`: **숫자가 아닌 문자**와 매치 (여기서는 `+`, `-`, `*`)
- `()` (그룹핑): `re.split` 사용 시, 구분자 패턴을 괄호로 감싸면 **구분자도 결과 리스트에 포함**됩니다.
    - 감싸지 않으면: `['100', '200']` (연산자 사라짐)
    - 감싸면: `['100', '-', '200']` (연산자 보존)

