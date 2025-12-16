# 메뉴 리뉴얼

## 문제 설명
손님들이 주문한 단품 메뉴들의 조합을 분석하여, 가장 많이 함께 주문된 조합을 코스 요리 메뉴로 구성하려고 합니다.
단, 코스 요리는 최소 2가지 이상의 단품 메뉴로 구성되어야 하며, 최소 2명 이상의 손님에게서 주문된 조합이어야 합니다.
주어진 `course` 리스트(예: [2, 3, 5])의 길이에 맞는 최빈 조합을 찾아야 합니다.

### 핵심 개념
1.  **조합 (Combinations)**: 각 손님이 주문한 메뉴들에서 `course`에 있는 길이만큼의 조합을 모두 찾습니다.
    - 예: "ABCDE" 주문, course=2 -> AB, AC, AD, ..., DE (10개)
2.  **카운터 (Counter)**: 찾아낸 모든 조합들의 등장 횟수를 셉니다. `collections.Counter`가 매우 유용합니다.
3.  **정렬 (Sorting)**:
    - 조합을 만들 때 메뉴 구성 "XY"와 "YX"는 같습니다. 따라서 **문자열을 정렬한 뒤 조합**을 만들어야 통일된 키를 얻을 수 있습니다 (예: 'A', 'C' -> "AC").

## Python 풀이

```python
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for k in course:
        candidates = []
        for order in orders:
            # 메뉴 구성 통일을 위해 정렬 ("XY", "YX" -> "XY")
            sorted_order = sorted(order)
            
            # 해당 주문에서 길이 k인 조합을 모두 생성
            for comb in combinations(sorted_order, k):
                candidates.append("".join(comb))
        
        # 길이 k인 모든 조합의 빈도수 계산
        counted = Counter(candidates)
        
        # 가장 많이 주문된 횟수 찾기, 2번 미만이면 제외
        if counted:
            max_count = max(counted.values())
            if max_count >= 2:
                for menu, cnt in counted.items():
                    if cnt == max_count:
                        answer.append(menu)
                        
    # 결과를 알파벳 오름차순으로 정렬
    return sorted(answer)
```

### 코드 설명
- `course` 루프: 각 코스 길이(예: 2가지, 3가지...)마다 별도로 최빈 조합을 구합니다.
- `sorted(order)`: 조합을 만들기 전에 정렬하는 것이 필수입니다.
- `Counter(candidates)`: 리스트에 담긴 모든 조합의 개수를 셉니다.
    - `counted.values()`의 최댓값이 `max_count`입니다.
    - 같은 `max_count`를 가진 메뉴가 여러 개일 수 있으므로(공동 1등), 순회하며 다 넣어줍니다.
- 조건 체크: `max_count >= 2` 이어야 합니다.
- 마지막에 전체 정답 리스트를 정렬하여 반환합니다.
