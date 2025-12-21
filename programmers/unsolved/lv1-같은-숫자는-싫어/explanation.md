# 같은 숫자는 싫어

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12906)

배열 `arr`에서 연속적으로 나타나는 숫자는 하나만 남기고 제거하세요. (순서 유지)
예: `[1, 1, 3, 3, 0, 1, 1]` -> `[1, 3, 0, 1]`

## 해결 전략
스택(Stack)을 사용하거나 직전 값(`prev`)과 비교합니다.
`arr[i] != arr[i-1]`인 경우만 담습니다.

### 알고리즘 순서
1. `result` = []
2. `arr` 순회 (`x`):
    - `if not result` or `result[-1] != x`:
        - `result.append(x)`
3. return `result`

## Python 코드

```python
def solution(arr):
    result = []
    
    for x in arr:
        # 비어있거나, 마지막 요소와 다를 때만 추가
        if not result or result[-1] != x:
            result.append(x)
            
    return result
```

## 배운 점 / 팁
- **연속 중복 제거**: `set`을 쓰면 순서가 망가지고 떨어진 중복도 다 사라지므로 쓰면 안 됩니다. 리스트나 스택으로 직전 값과 비교해야 합니다.
