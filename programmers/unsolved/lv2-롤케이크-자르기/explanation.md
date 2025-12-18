# 롤케이크 자르기

## 문제 설명
롤케이크에 여러 가지 토핑이 일렬로 올려져 있습니다 (`topping` 배열).
롤케이크를 두 조각으로 잘랐을 때, 형과 동생이 **동일한 종류의 가짓수**의 토핑을 맛볼 수 있는 자르는 방법의 수를 구합니다.
(토핑의 개수가 아니라 **종류의 수**가 중요합니다).

## 풀이 개념
**해시 맵 (Counter / Set)**을 이용하여 O(N)안에 해결해야 합니다. N이 최대 1,000,000이기 때문입니다.

1. 전체 토핑의 개수를 `Counter` (오른쪽 조각 용)에 저장합니다.
2. 왼쪽 조각에 포함된 토핑 종류를 저장할 `Set`을 준비합니다.
3. 롤케이크를 왼쪽부터 하나씩 자르는 위치를 옮겨가며(Iterate):
   - 해당 토핑을 오른쪽 `Counter`에서 하나 줄입니다. 0이 되면 `del`하거나 `len` 체크 시 제외해야 합니다. (Counter는 0이 되어도 키가 남으므로 `len` 이용 시 주의하거나 0일 때 pop).
   - 해당 토핑을 왼쪽 `Set`에 추가합니다.
   - `len(left_set)`과 `len(right_counter)`가 같은지 비교하여 같으면 정답 카운트를 증가시킵니다.

## 코드 (Python)

```python
from collections import Counter

def solution(topping):
    # 오른쪽 부분: 전체 토핑 카운트
    right = Counter(topping)
    # 왼쪽 부분: 종류만 중요하므로 Set 사용
    left = set()
    
    answer = 0
    right_types = len(right) # 오른쪽 종류 수
    
    for t in topping:
        # 왼쪽으로 이동
        left.add(t)
        
        # 오른쪽에서 제거
        right[t] -= 1
        if right[t] == 0:
            right_types -= 1
            
        # 종류 수 비교
        if len(left) == right_types:
            answer += 1
            
    return answer
```
<br/>

## 코드 설명
### Q. 종류 수 비교(`if len(left) == right_types`)를 `if right[t] == 0` 내부에 넣지 않는 이유?
- **상황**: `right[t] == 0` 조건문은 오른쪽 조각에서 특정 토핑 토핑의 개수가 0이 되어 **종류 수가 감소할 때**만 실행됩니다.
- **이유**: 종류 수가 같아지는 경우는 오른쪽 토핑 종류가 줄어들 때뿐만 아니라, **왼쪽 토핑 종류가 늘어날 때**도 발생할 수 있습니다.
  - 예: 왼쪽 `set`에 새로운 토핑이 추가되어 `len(left)`가 증가해서 같아지는 경우.
  - 따라서 토핑 하나를 옮길 때마다 매번(`block` 밖에서) 확인해야 모든 경우의 수를 놓치지 않고 체크할 수 있습니다.



