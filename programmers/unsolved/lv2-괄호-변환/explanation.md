# 괄호 변환

## 문제 설명
"균형잡힌 괄호 문자열"(`(`와 `)` 개수가 같음) `p`가 주어질 때, 이를 "올바른 괄호 문자열"(`(`와 `)`의 짝도 맞음)로 변환하는 과정을 구현해야 합니다.
문제에서 주어진 알고리즘을 그대로 구현(Simulation/Recursive)하는 문제입니다.

**제시된 알고리즘**:
1. 입력이 빈 문자열이면 빈 문자열 반환.
2. 문자열을 두 "균형잡힌 괄호 문자열" $u, v$로 분리. 단, $u$는 더 이상 분리할 수 없는 최소 단위여야 함.
3. $u$가 "올바른 괄호 문자열"이면 $v$에 대해 1단계부터 다시 수행 후 이어 붙임. (`u + solution(v)`)
4. $u$가 아니면:
    - 빈 문자열 `(` 생성
    - `v`에 대해 재귀 수행 결과 붙임
    - `)` 붙임
    - $u$의 첫/마지막 문자 제거하고 나머지 괄호 방향 뒤집어서 뒤에 붙임.
    - 생성된 문자열 반환.

### 핵심 개념
1.  **재귀 (Recursion)**: 문제 자체가 재귀적 정의를 따릅니다.
2.  **구현력**: 알고리즘 설명이 복잡하므로 실수 없이 옮기는 것이 중요합니다.
3.  **문자열 분리**: `(`와 `)` 개수가 같아지는 첫 지점에서 $u$와 $v$를 나눕니다.
4.  **올바른 괄호 체크**: 스택 등을 이용해 $u$가 올바른지 확인합니다.

## Python 풀이

```python
def is_correct(s):
    """올바른 괄호 문자열인지 확인"""
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

def split_uv(p):
    """문자열을 u, v로 분리"""
    count_l = 0
    count_r = 0
    for i in range(len(p)):
        if p[i] == '(':
            count_l += 1
        else:
            count_r += 1
            
        if count_l == count_r:
            return p[:i+1], p[i+1:]
    return p, ""

def reverse_bracket(s):
    """괄호 방향 뒤집기"""
    table = str.maketrans("()", ")(")
    return s.translate(table)
    # 또는:
    # res = ""
    # for char in s:
    #     if char == '(': res += ')'
    #     else: res += '('
    # return res

def solution(p):
    # 1. 빈 문자열인 경우
    if not p:
        return ""
    
    # 2. u, v 분리
    u, v = split_uv(p)
    
    # 3. u가 올바른 괄호 문자열인 경우
    if is_correct(u):
        return u + solution(v)
    
    # 4. u가 올바르지 않은 경우
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        
        # u의 첫 번째와 마지막 문자 제거
        u = u[1:-1]
        # 나머지 문자열의 괄호 방향 뒤집기
        answer += reverse_bracket(u)
        
        return answer
```

### 코드 설명
- `split_uv`: 앞에서부터 `(`와 `)` 개수를 세다가 개수가 같아지는 순간 자릅니다. 문제 조건상 $p$는 균형잡힌 문자열이므로 반드시 잘라집니다.
- `reverse_bracket`: 문제 설명에서 "문자열 괄호 방향 뒤집기"는 문자열 순서를 뒤집는게(`[::-1]`) 아니라, `(`를 `)`로, `)`를 `(`로 바꾸라는(Swap) 뜻임을 주의해야 합니다.
