# 괄호 변환
- 겉으로 한 번 봤을때보다는 은근 '재귀'성격이 더 강하다. stack 으로 유효한 괄호 문자열인지 체크하는 건 다 해봤으니까 쉽지. 근데 이걸 섞어서 나왔다는게 신기했다.
- 문법 중 `table = str.maketrans(src,dest)`와 `translate(table)`를 처음봤다.

<br/>


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
<br/>


### 코드 설명
- `split_uv`: 앞에서부터 `(`와 `)` 개수를 세다가 개수가 같아지는 순간, **즉시** 잘라서 반환합니다. 이는 $u$를 더 이상 분리할 수 없는 "균형잡힌 괄호 문자열"의 최소 단위로 만들기 위함입니다. 문제 조건상 $p$는 전체가 균형잡힌 문자열이므로 반드시 잘라집니다.
- `reverse_bracket`: 문제 설명에서 "문자열 괄호 방향 뒤집기"는 문자열 순서를 뒤집는게(`[::-1]`) 아니라, `(`를 `)`로, `)`를 `(`로 바꾸라는(Swap) 뜻임을 주의해야 합니다.

<br/>

split_uv 함수는 문자열 p의 처음(index 0)부터 시작해서 왼쪽 괄호 (와 오른쪽 괄호 )의 개수를 셉니다. 그리고 두 개수가 같아지는 순간, 즉시 그 지점까지를 u로, 나머지를 v로 잘라서 반환합니다.

문제 설명 2번 항목의 조건인 **"u는 '균형잡힌 괄호 문자열'로 더 이상 분리할 수 없어야 한다(즉, 최소 단위여야 한다)"**를 만족하기 위해서입니다. **개수가 같아지는 첫 번째 순간에 자르면** , 그 u 안에서는 더 작은 균형잡힌 문자열이 존재할 수 없으므로(가장 작은 단위) 조건을 충족하게 됩니다.<br/>

즉, 매 순간 호출될때마다 idx=0 부터 균형잡힌 괄호를 찾자마자 바로 return 하는 역할을 수행<br/>
<br/>


## 문법 설명

### `str.maketrans`와 `translate`
문자열 내의 특정 문자들을 다른 문자로 한 번에 치환(변환)할 때 사용합니다.

- **`table = str.maketrans("()", ")(")`**
    - 변환 규칙 테이블을 생성합니다.
    - 첫 번째 인자의 문자들을 두 번째 인자의 문자들로 1:1 매핑합니다.
    - 즉, `(` $\rightarrow$ `)`, `)` $\rightarrow$ `(` 로 매핑됩니다.

- **`s.translate(table)`**
    - 문자열 `s`에 위 `table`의 규칙을 적용하여 반환합니다.
    - `replace`를 여러 번 사용하는 것보다 훨씬 효율적이고 간결하게 문자 교체가 가능합니다.

**예시**:
```python
text = "Hello World"
# H -> h, W -> w 로 변환
table = str.maketrans("HW", "hw")
print(text.translate(table)) # "hello world"
```

