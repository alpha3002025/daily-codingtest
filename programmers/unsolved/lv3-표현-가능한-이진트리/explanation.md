# 표현 가능한 이진트리

## 문제 설명
십진수 숫자가 주어질 때(최대 $10^{15}$), 이를 이진수로 나타낸 문자열이 "포화 이진트리" 형태로 표현 가능한지 판별합니다.
여기서 "표현 가능하다"는 것은, 포화 이진트리의 노드들에 0 또는 1을 배치했을 때, `1`인 노드의 부모가 `0`인 경우가 없어야 한다는 것입니다. (즉, 더미 노드 0 밑에 실제 노드 1이 올 수 없음)

> 핵심 조건: 루트가 0(더미)이면, 그 자식들은 모두 0이어야 합니다. (루트가 없는데 자식이 있을 수 없으므로)

## 문제 해결 전략

1. **이진수 변환 및 포화 이진트리 만들기**:
   - 숫자를 이진수 문자열로 변환합니다.
   - 포화 이진트리의 노드 개수는 $2^h - 1$ 형태입니다 (1, 3, 7, 15, 31, 63...).
   - 변환된 문자열의 길이가 $2^h - 1$이 되도록 앞에 `0`을 패딩합니다.

2. **재귀적 검증 (분할 정복)**:
   - 트리(문자열)의 중앙값이 루트입니다.
   - 루트가 `0`이라면, 왼쪽 서브트리와 오른쪽 서브트리에 `1`이 하나라도 있으면 안 됩니다. (루트가 없는데 자식이 존재할 수 없음)
   - 루트가 `1`이라면, 왼쪽과 오른쪽 서브트리를 재귀적으로 검사하면 됩니다.
   - 기저 사례: 리프 노드(길이 1)는 항상 가능(True).

### 상세 알고리즘
- 입력 숫자 리스트를 순회하며 각각 판별.
- `bin(x)[2:]`로 이진수 변환.
- 길이를 $2^h - 1$ 꼴로 맞춤 (최소 필요한 길이 구해서 zfill).
- `check(substring)` 함수:
  - `mid = len // 2`
  - `root = substring[mid]`
  - `left = substring[:mid]`, `right = substring[mid+1:]`
  - 만약 `root == '0'`:
    - `left`나 `right`에 `'1'`이 하나라도 있으면 **불가능(False)**.
    - 모두 `'0'`이면 **가능(True)** (더미 트리).
  - 만약 `root == '1'`:
    - `check(left)` AND `check(right)`가 True여야 함.
- 결과 반환.

## Python 코드

```python
def solution(numbers):
    answer = []
    
    def check(s):
        if len(s) == 1: # 리프 노드
            return True
            
        mid = len(s) // 2
        root = s[mid]
        left_sub = s[:mid]
        right_sub = s[mid+1:]
        
        if root == '0':
            # 루트가 0이면 자식들 중 1이 있으면 안됨
            # 즉 자식 서브트리 전체가 0이어야 함
            if '1' in left_sub or '1' in right_sub:
                return False
            else:
                return True
        else: # root == '1'
            return check(left_sub) and check(right_sub)

    for num in numbers:
        bin_s = bin(num)[2:]
        length = len(bin_s)
        
        # 포화 이진트리 길이로 맞추기 (1, 3, 7, 15, 31...)
        # 2^h - 1 >= length 인 최소 h 찾기
        h = 1
        while (1 << h) - 1 < length:
            h += 1
        
        full_len = (1 << h) - 1
        bin_s = bin_s.zfill(full_len)
        
        if check(bin_s):
            answer.append(1)
        else:
            answer.append(0)
            
    return answer
```
