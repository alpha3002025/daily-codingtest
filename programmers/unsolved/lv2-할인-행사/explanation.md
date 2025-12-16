# 할인 행사

## 문제 설명
XYZ 마트는 10일 동안 회원 자격을 가진 사람에게 할인 혜택을 줍니다.
매일 한 가지 제품을 할인하며, 하루에 하나씩만 구매할 수 있습니다.
자신이 원하는 제품 목록(`want`)과 수량(`number`)이 주어질 때, 10일 연속으로 회원 자격이 있을 때 모든 물품을 할인받아 살 수 있는 날짜(회원가입 가능한 날짜)의 총 일수를 구합니다. `discount` 배열은 날짜별 할인 상품입니다.

## 풀이 개념
**슬라이딩 윈도우 (Sliding Window)**와 **해시 맵 (Counter)**을 사용합니다.
10일 간격의 윈도우를 이동시키며, 윈도우 내 상품 구성이 `want` + `number`와 일치하는지 확인합니다.

1. 원하는 상품과 수량을 `Counter`나 딕셔너리로 만듭니다.
2. 처음 10일(`discount[:10]`)의 상품 구성을 셉니다.
3. 두 구성을 비교하여 일치하면 `answer`를 증가시킵니다.
4. 11일째부터 마지막 날까지 반복(Slide):
   - 윈도우 맨 앞의 상품(어제 날짜)을 제거(Count 감소)합니다.
   - 윈도우 맨 뒤의 상품(오늘 날짜)을 추가(Count 증가)합니다.
   - 구성을 비교하여 일치하면 `answer`를 증가시킵니다. (전체 비교 대신 불일치 개수만 관리할 수도 있지만, 종류가 적으므로 전체 비교 `O(K)`도 충분함).

## 코드 (Python)

```python
from collections import Counter

def solution(want, number, discount):
    # 원하는 품목 딕셔너리 생성
    target = {}
    for w, n in zip(want, number):
        target[w] = n
        
    answer = 0
    
    # 윈도우 크기는 10 (항상 10일치 물품을 구매하므로)
    window_size = 10
    
    # 초기 윈도우
    current_counter = Counter(discount[:window_size])
    
    # 초기 비교
    if current_counter == target: # (순서 무관, 내용물 비교)
         # Counter 비교시 0개인 키값 처리가 중요할 수 있으나,
         # target에 없는 물품은 current에 있어도 상관 없지 않음 (정확히 일치해야함? 문제 조건: "원하는 제품을 모두 할인 받을 수 있는")
         # -> 남는건 상관 없고 부족하면 안됨?
         # 문제: "자신이 원하는 제품과 수량이 할인하는 날짜와 10일 연속으로 일치할 경우"
         # 즉, 10일 동안의 목록에 원하는게 다 들어있어야 함. (총합이 10개이므로 정확히 구성이 같아야 함)
         answer += 1

    for i in range(1, len(discount) - window_size + 1):
        prev_item = discount[i-1]
        next_item = discount[i + window_size - 1]
        
        current_counter[prev_item] -= 1
        if current_counter[prev_item] == 0:
            del current_counter[prev_item]
            
        current_counter[next_item] += 1
        
        if current_counter == target:
            answer += 1
            
    return answer
```
