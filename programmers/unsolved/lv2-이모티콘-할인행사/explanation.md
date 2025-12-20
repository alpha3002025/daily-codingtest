# 이모티콘 할인행사
예전에 풀어보긴 했던 문제다.<br/>
<br/>


## 문제 설명
이모티콘마다 할인율(10%, 20%, 30%, 40% 중 하나)을 적용하여 판매합니다.
목표는 다음 두 가지를 **우선순위 순서대로** 최대로 만드는 것입니다.
1. **이모티콘 플러스 서비스 가입자 수** (가장 중요)
2. **이모티콘 판매액** (가입자 수가 같다면 판매액이 높은 쪽 선택)

각 사용자(`users`)는 자신의 기준(일정 비율 이상의 할인이면 구매, 총 구매액이 일정 금액 이상이면 서비스 가입)에 따라 행동합니다.

## 풀이 개념
**완전 탐색 (Brute Force)** 문제입니다.
이모티콘의 개수가 최대 7개로 매우 적고, 할인율의 종류도 4가지뿐입니다.
따라서 가능한 모든 할인 조합을 확인해도 충분합니다.
- 경우의 수: $4^7 = 16,384$가지 (충분히 작음).

### 알고리즘 단계
1. **순열/중복조합 생성**: `itertools.product`를 사용하여 모든 이모티콘에 대한 할인율 조합(예: [10, 40, ...])을 생성합니다.
2. **시뮬레이션**: 각 할인 조합에 대해 다음을 계산합니다.
   - 각 사용자별로 구매 비용 계산.
   - 사용자의 기준 할인율보다 높거나 같은 이모티콘만 구매.
   - 총 구매 비용이 사용자의 한계 금액(`user[1]`) 이상이면 **가입**, 아니면 **구매**.
3. **최댓값 갱신**: 가입자 수가 더 많거나, 가입자 수가 같으면서 매출액이 더 큰 경우 정답을 갱신합니다.

## 코드 (Python)

```python
from itertools import product

def solution(users, emoticons):
    # 할인율 후보
    discounts = [10, 20, 30, 40]
    
    # 정답 초기화 [가입자 수, 판매액]
    answer = [0, 0]
    
    # 1. 모든 할인율 조합 생성 (중복 순열)
    # emoticons 개수만큼의 할인율 조합을 만듦
    for case in product(discounts, repeat=len(emoticons)):
        current_subscribers = 0
        current_sales = 0
        
        # 2. 각 유저별 계산
        for rate_limit, price_limit in users:
            user_total = 0 # 이 유저의 구매 총액
            
            for i in range(len(emoticons)):
                discount_rate = case[i]
                price = emoticons[i]
                
                # 유저가 원하는 할인율 이상일 때만 구매
                if discount_rate >= rate_limit:
                    user_total += price * (100 - discount_rate) // 100
            
            # 3. 서비스 가입 여부 판단
            if user_total >= price_limit:
                current_subscribers += 1
            else:
                current_sales += user_total
        
        # 4. 정답 갱신 (우선순위: 가입자 구 > 판매액)
        if current_subscribers > answer[0]:
            answer = [current_subscribers, current_sales]
        elif current_subscribers == answer[0]:
            answer[1] = max(answer[1], current_sales)
            
    return answer
```

### 시간 복잡도
- 할인율 조합 생성: $4^m$ ($m$은 이모티콘 개수, 최대 7)
- 내부 루프: 유저 수 $n$ (최대 100)
- 총 복잡도: $O(4^m \times n \times m)$
- $16384 \times 100 \times 7 \approx 10^7$ 연산으로 1초 이내 충분히 통과합니다.


## 나의 풀이
```python
from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    
    for discount_combo in product(range(1, 5), repeat=len(emoticons)):
        plus = 0
        total = 0
        
        for user_min_discount, user_limit in users:
            # 각 사용자의 구매 금액 계산
            revenue = sum(
                emoticons[i] * (100 - discount_level * 10) // 100
                for i, discount_level in enumerate(discount_combo)
                if discount_level * 10 >= user_min_discount
            )
            
            # 플러스 가입 or 일반 구매
            if revenue >= user_limit:
                plus += 1
            else:
                total += revenue
        
        # 최적 결과 갱신
        if plus > answer[0] or (plus == answer[0] and total > answer[1]):
            answer = [plus, total]
    
    return answer
```