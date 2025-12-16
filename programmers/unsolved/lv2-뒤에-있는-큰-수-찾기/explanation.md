# 뒤에 있는 큰 수 찾기

## 문제 설명
정수 배열 `numbers`가 주어집니다.
배열의 각 원소들에 대해 "자신보다 뒤에 있는 숫자 중에서 자신보다 크면서 가장 가까이 있는 수"를 뒷 큰수라고 합니다.
모든 원소에 대한 뒷 큰수를 차례로 담은 배열을 반환합니다. 뒷 큰수가 존재하지 않으면 -1을 담습니다.

## 풀이 개념
**단조 스택 (Monotonic Stack)** 알고리즘을 사용합니다.
단순 이중 반복문(`O(N^2)`)을 사용하면 시간 초과(`N` 최대 1,000,000)가 발생합니다. 스택을 사용하면 `O(N)`으로 해결 가능합니다.

1. 정답 배열 `answer`를 `-1`로 초기화합니다.
2. 인덱스를 저장할 스택을 생성합니다.
3. `numbers` 배열을 순회합니다.
   - 스택이 비어있지 않고, `numbers[stack[-1]]` (스택 top 인덱스의 값)보다 현재 숫자 `numbers[i]`가 크다면:
     - 스택 top에 해당하는 수의 "뒷 큰수"는 바로 현재 숫자 `numbers[i]`입니다.
     - 스택에서 pop 하고 `answer` 갱신을 반복합니다 (현재 숫자가 더 큰 동안 계속).
   - 현재 인덱스 `i`를 스택에 push 합니다.
4. 순회가 끝난 후 스택에 남아있는 인덱스들은 뒷 큰수가 없는 경우이므로 이미 초기화된 `-1`이 유지됩니다.

## 코드 (Python)

```python
def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stack = [] # 인덱스를 저장하는 스택
    
    for i in range(n):
        # 스택에 값이 있고, 현재 수가 스택 top의 수보다 크면 뒷 큰수 발견
        while stack and numbers[stack[-1]] < numbers[i]:
            idx = stack.pop()
            answer[idx] = numbers[i]
            
        stack.append(i)
        
    return answer
```
