# 의상

## 문제 설명
스파이가 가진 의상들이 주어졌을 때, 서로 다른 옷의 조합 수를 구하는 문제입니다. 스파이는 매일 최소 한 개의 의상은 입어야 합니다.
예: `[[yellow_hat, headgear], [blue_sunglasses, eyewear], [green_turban, headgear]]`

### 핵심 개념
1.  **해시 맵 (Dictionary / Counter)**: 의상 종류(Category)별로 몇벌이 있는지 셉니다.
    - 예: `headgear`: 2개, `eyewear`: 1개
2.  **경우의 수 (수학)**:
    - 각 종류별로 옷을 고르는 방법: (해당 종류 옷 개수) + 1 (안 입음)
    - 모든 종류에 대해 곱해줍니다. -> `(A+1) * (B+1) * ...`
    - 마지막에 **모두 안 입은 경우(알몸)** 1가지를 빼줍니다.

## Python 풀이

```python
from collections import Counter

def solution(clothes):
    # 의상 종류별 개수 세기
    # c[1]은 category
    counter = Counter([type for name, type in clothes])
    
    answer = 1
    # (각 종류별 개수 + 1) 을 모두 곱함
    for count in counter.values():
        answer *= (count + 1)
        
    # 아무것도 입지 않은 경우 1 빼기
    return answer - 1
```

### 코드 설명
- `Counter`를 사용하면 종류별 개수를 쉽게 구할 수 있습니다.
- `answer *= (count + 1)` : 해당 종류의 옷을 입는 경우들 + 입지 않는 경우(1).
- `return answer - 1` : 문제 조건인 "최소 한 개의 의상은 입는다"를 만족하기 위해, 모두 선택하지 않은 1가지 경우를 제외합니다.
