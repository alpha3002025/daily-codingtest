# 귤 고르기

## 문제 설명
수확한 귤 중 `k`개를 골라 상자에 담아 판매하려고 합니다.
귤의 크기가 다를 수 있는데, 상자에 담긴 귤의 크기 종류가 최소가 되도록 골라야 합니다.
서로 다른 종류의 수의 최솟값을 반환합니다.

## 풀이 개념
**그리디 (Greedy)** 알고리즘과 **해시 맵 (Counter)**, **정렬**을 사용합니다.
적은 종류로 `k`개를 채우려면, **개수가 많은 종류(빈도수가 높은 크기)**부터 우선적으로 선택해야 합니다.

1. `Counter`를 이용해 각 크기별 귤의 개수를 셉니다.
2. 개수(value)만 뽑아서 **내림차순 정렬**합니다. (어떤 크기인지는 중요하지 않고, 몇 개가 있는지가 중요)
3. 정렬된 개수를 순서대로 더해가며 `k` 이상이 될 때까지 종류 수를 카운트합니다.

## 코드 (Python)

```python
from collections import Counter

def solution(k, tangerine):
    # 크기별 개수 세기
    counts = Counter(tangerine)
    
    # 개수가 많은 순으로 정렬
    sorted_counts = sorted(counts.values(), reverse=True)
    
    answer = 0
    current_count = 0
    
    for count in sorted_counts:
        current_count += count
        answer += 1
        
        if current_count >= k:
            break
            
    return answer
```
