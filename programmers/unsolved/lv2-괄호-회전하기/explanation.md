# 괄호 회전하기
- stack 문제로 둘까 하다가, stack 이라기엔 완전 stack 으로 출제하는 문제들하고는 조금 유형이 동떨어져있다. stack 으로 괄호 검사하는건 helloworld!! 이기에.. 문자열 유형에 두는게 조금 더 맞겠다 싶기도 하고 그래야 연습을 더 할것 같았다. 그래서 이번 문제를 문자열 문제로 분류하기로 결정했다.

<br/>


## 문제 설명
대괄호`[]`, 중괄호`{}`, 소괄호`()`로 이루어진 문자열 `s`가 주어집니다. 이 문자열을 왼쪽으로 $x$칸($0 \le x < len(s)$)만큼 회전시켰을 때, 올바른 괄호 문자열이 되는 $x$의 개수를 구하는 문제입니다.

### 핵심 개념
1.  **문자열 회전**: 슬라이싱을 이용해 쉽게 구현할 수 있습니다. `s[i:] + s[:i]`
2.  **스택 (Stack)**: 올바른 괄호 문자열인지 판단하는 가장 표준적인 자료구조입니다.
    - 여는 괄호(`[`, `{`, `(`)가 나오면 push.
    - 닫는 괄호(`]`, `}`, `)`)가 나오면 stack이 비어있지 않은지 확인하고, top이 짝이 맞는 여는 괄호인지 확인 후 pop.
    - 문자열 끝까지 처리했을 때 stack이 비어있어야 올바른 문자열입니다.

## Python 풀이

```python
def is_valid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in "([{":
            stack.append(char)
        else:
            # 닫는 괄호인데 스택이 비어있으면 유효하지 않음
            if not stack:
                return False
            # 짝이 맞는지 확인
            top = stack.pop()
            if pairs[char] != top:
                return False
    
    # 순회 후 스택이 비어있어야 함
    return len(stack) == 0

def solution(s):
    answer = 0
    n = len(s)
    
    # n번 회전 (0 ~ n-1)
    for i in range(n):
        rotated_s = s[i:] + s[:i]
        if is_valid(rotated_s):
            answer += 1
            
    return answer
```

### 코드 설명
- `pairs` 딕셔너리로 닫는 괄호에 대응되는 여는 괄호를 매핑해두면 코드가 간결해집니다.
- 닫는 괄호가 나왔을 때 `stack`이 비어있거나, `pop()`한 결과가 매핑된 짝이 아니면 `False`를 반환합니다.
- `len(stack) == 0` 체크는 여는 괄호가 남아서 닫히지 않은 경우(예: `(()`)를 걸러내기 위함입니다.
- 문자열의 길이 $N$이 최대 1,000이므로, $O(N^2)$ 복잡도(회전 $N$회 $\times$ 검사 $N$)로 충분히 통과 가능합니다 ($10^6$ 연산).
