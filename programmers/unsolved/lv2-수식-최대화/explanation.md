# 수식 최대화

## 개념 설명 코드
```python
import re
from itertools import permutations

def solution(expression):
    refined = re.split(r"([^0-9])", expression)
    operands = list(map(int, refined[::2]))
    operators = refined[1::2]
    max_value = -float('inf')
    
    ## (참고)
    # for curr_perm in permutations(operators): ## 이렇게 할 경우에는 에러가 난다. 조심!!
    
    ## 연산자 우선순위의 순열 
    for curr_perm in permutations(['+', '-', '*']):
        operators_copy = operators[:]
        operands_copy = operands[:]
        
        for curr_op in curr_perm:
            operator_idx = 0
            
            ## 복사한 연산자 배열에서 curr_op 의 위치를 찾는다.
            while operator_idx < len(operators_copy):
                
                ### 해당 연산자 위치에 도달
                if operators_copy[operator_idx] == curr_op: 
                    v1 = operands_copy[operator_idx]
                    v2 = operands_copy[operator_idx+1]
                    
                    if curr_op == '+': res = v1 + v2
                    elif curr_op == '-': res = v1 - v2
                    elif curr_op == '*': res = v1 * v2
                    
                    operands_copy[operator_idx] = res
                    del operands_copy[operator_idx+1]
                    del operators_copy[operator_idx]
                
                ### 해당 연산자를 찾을때까지 operator += 1
                else:
                    operator_idx += 1
        
        max_value = max(max_value, abs(operands_copy[0]))
    return max_value
```
<br/>
<br/>


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

## 참고 - 정규식 `r'([^0-9])'` 설명
- `[]` (문자 클래스): 대괄호 안의 문자 중 하나와 매치됩니다.
- `^` (Not): 대괄호 안에서 맨 앞에 쓰이면 **"반대(Not)"**를 의미합니다.
    - `[0-9]`: 숫자와 매치
    - `[^0-9]`: **숫자가 아닌 문자**와 매치 (여기서는 `+`, `-`, `*`)
- `()` (그룹핑): `re.split` 사용 시, 구분자 패턴을 괄호로 감싸면 **구분자도 결과 리스트에 포함**됩니다.
    - 감싸지 않으면: `['100', '200']` (연산자 사라짐)
    - 감싸면: `['100', '-', '200']` (연산자 보존)


## 코드 설명
```python
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
```


### 코드 상세 설명

#### 1. 리스트 조작 방식 (In-place Reduction)
-   **`while idx < len(tmp_operators)`**: `for` 문이 아닌 `while` 문을 사용하는 이유는 연산 과정에서 리스트의 크기가 수시로 변하기 때문입니다.
-   **`del`과 인덱스 유지**:
    -   연산자(`idx`)와 피연산자(`idx+1`)를 삭제하면 뒤에 있던 요소들이 앞으로 한 칸씩 당겨집니다.
    -   이때 `idx += 1`을 하지 않고 그대로 두면, **방금 당겨져 온 다음 연산자**를 같은 인덱스에서 즉시 다시 검사하게 됩니다. 이를 통해 현재 우선순위인 `op`가 연속해서 나타나더라도 누락 없이 처리할 수 있습니다.
-   **숫자 대체**: `tmp_operands[idx] = res`를 통해 두 숫자의 계산 결과를 앞쪽 포지션에 덮어쓰고, 뒤쪽 숫자(`idx+1`)를 지워 수식을 축소합니다.

---

#### 2. 예시 시뮬레이션: `"50*6-3*2"` (우선순위: `-` > `*`)
> 우선순위 순열이 `['-', '*', '+']`인 경우의 시뮬레이션입니다.

**초기 상태:**
- `tmp_operands`: `[50, 6, 3, 2]`
- `tmp_operators`: `['*', '-', '*']`

**Step 1: 1순위 연산자 `-` 처리**
1.  **`idx = 0`**: `tmp_operators[0]`은 `*`입니다. 찾는 연산자가 아니므로 **`idx`를 1 증가**시킵니다.
2.  **`idx = 1`**: `tmp_operators[1]`은 **`-`**입니다. **발견!**
    -   **계산**: `tmp_operands[1]`(6)과 `tmp_operands[2]`(3)을 빼서 **`3`**을 얻습니다.
    -   **리스트 갱신**: 
        -   `tmp_operands[1]`을 `3`으로 변경하고, `tmp_operands[2]`를 삭제합니다. → `[50, 3, 2]`
        -   `tmp_operators[1]`인 `-`를 삭제합니다. → `['*', '*']`
    -   **결과**: 이 단계가 끝나면 수식은 `50 * 3 * 2`의 형태가 됩니다.

**Step 2: 2순위 연산자 `*` 처리**
현재 상태: `tmp_operands = [50, 3, 2]`, `tmp_operators = ['*', '*']`
1.  **`idx = 0`**: `tmp_operators[0]`은 **`*`**입니다. **발견!**
    -   **계산**: `50 * 3 = 150`
    -   **리스트 갱신**: 
        - `tmp_operands`: `50` 자리에 `150`을 덮어쓰고, 뒤의 **`3`을 삭제** → `[150, 2]`
        - `tmp_operators`: 0번 인덱스의 **`*`를 삭제** → `['*']`
    -   **인덱스**: `idx`는 `0`으로 유지되어 당겨져 온 다음 연산을 대기합니다.
2.  **`idx = 0`**: `tmp_operators[0]`은 **`*`**입니다. **발견!**
    -   **계산**: `150 * 2 = 300`
    -   **리스트 갱신**: 
        - `tmp_operands`: `150` 자리에 `300`을 덮어쓰고, 뒤의 **`2`를 삭제** → `[300]`
        - `tmp_operators`: 0번 인덱스의 **`*`를 삭제** → `[]`


**최종 결과:**
-   최종 결과: `abs(300) = 300`
-   보통의 사칙연산(`*` 먼저)이라면 `300 - 6 = 294`가 나왔겠지만, 우선순위 재정의에 의해 `300`이 도출되었습니다.


---

#### 3. 예시 시뮬레이션: `"50*6+3-2"` (우선순위: `+` > `-` > `*`)
> 우선순위 순열이 `['+', '-', '*']`인 경우의 시뮬레이션입니다.

**초기 상태:**
- `tmp_operands`: `[50, 6, 3, 2]`
- `tmp_operators`: `['*', '+', '-']`

**Step 1: 1순위 연산자 `+` 처리**
1.  **`idx = 0`**: `tmp_operators[0]`은 `*`입니다. 패스 (`idx` 1 증가).
2.  **`idx = 1`**: `tmp_operators[1]`은 **`+`**입니다. **발견!**
    -   **계산**: `6 + 3 = 9`
    -   **리스트 갱신**: 
        -   `tmp_operands`: `[50, 9, 2]` (`6` 자리에 `9`를 넣고, 뒤의 `3` 삭제)
        -   `tmp_operators`: `['*', '-']` (`+` 삭제)
    -   **결과**: 이 단계가 끝나면 수식은 `50 * 9 - 2`가 됩니다.

**Step 2: 2순위 연산자 `-` 처리**
현재 상태: `tmp_operands = [50, 9, 2]`, `tmp_operators = ['*', '-']`
1.  **`idx = 0`**: `tmp_operators[0]`은 `*`이므로 패스 (`idx` 1 증가).
2.  **`idx = 1`**: `tmp_operators[1]`은 **`-`**입니다. **발견!**
    -   **계산**: `9 - 2 = 7`
    -   **리스트 갱신**: 
        -   `tmp_operands`: `[50, 7]` (`9` 자리에 `7`을 넣고, 뒤의 `2` 삭제)
        -   `tmp_operators`: `['*']` (`-` 삭제)
    -   **결과**: 이 단계가 끝나면 수식은 `50 * 7`이 됩니다.

**Step 3: 3순위 연산자 `*` 처리**
현재 상태: `tmp_operands = [50, 7]`, `tmp_operators = ['*']`
1.  **`idx = 0`**: `tmp_operators[0]`은 **`*`**입니다. **발견!**
    -   **계산**: `50 * 7 = 350`
    -   **리스트 갱신**: `tmp_operands = [350]`, `tmp_operators = []`

**최종 결과:**
-   최종 결과: `abs(350) = 350`
-   일반적인 사칙연산(`*` 먼저)이었다면 `300 + 3 - 2 = 301`이 나왔겠지만, 우선순위 조정을 통해 `350`이 도출되었습니다.
