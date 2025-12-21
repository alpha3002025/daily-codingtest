# 햄버거 만들기

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/133502)

재료(`ingredient`)가 순서대로 들어옵니다. (1:빵, 2:야채, 3:고기)
순서가 `1-2-3-1` (빵-야채-고기-빵)이 되는 순간 햄버거 하나를 포장(제거)합니다.
만들 수 있는 총 햄버거 개수를 구하세요.

## 해결 전략
**스택(Stack)**을 사용하는 것이 가장 효율적입니다.
들어오는 재료를 하나씩 스택에 쌓다가, 스택의 상위 4개가 `[1, 2, 3, 1]`이면 4개를 `pop`하고 카운트를 증가시킵니다.
`replace`나 문자열 조작으로 풀면 매번 문자열을 새로 생성하므로 `O(N^2)` 시간 복잡도가 되어 실패할 수 있습니다(N=1,000,000). 스택은 `O(N)`입니다.

### 알고리즘 순서
1. `stack` = []
2. `count` = 0
3. `ingredient` 순회 (`i`):
    - `stack.append(i)`
    - `if stack[-4:] == [1, 2, 3, 1]`:
        - `count += 1`
        - `for _ in range(4): stack.pop()`
4. 반환 `count`.

## Python 코드

```python
def solution(ingredient):
    stack = []
    count = 0
    target = [1, 2, 3, 1]
    
    for item in ingredient:
        stack.append(item)
        
        # 마지막 4개가 1,2,3,1 패턴인지 확인
        if len(stack) >= 4 and stack[-4:] == target:
            count += 1
            # 4개 제거 (pop 4번)
            del stack[-4:]
            
    return count
```

## 배운 점 / 팁
- **패턴 매칭과 스택**: 연속된 패턴을 찾아서 제거하고, 제거된 후 이어지는 부분에서 다시 패턴을 찾아야 하는 문제(괄호 짝 맞추기 등)는 무조건 스택입니다.
- **Python List Slicing & Del**: `stack[-4:]`로 확인하고 `del stack[-4:]`로 한 번에 지우는 방식이 `pop()` 4번보다 약간 더 빠르고 가독성이 좋습니다.
