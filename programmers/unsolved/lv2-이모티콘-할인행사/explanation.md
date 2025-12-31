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

### 코드 상세 설명

#### product 시 i 의 의미
`product`와 루프 변수 `i`의 동작 원리는 다음과 같습니다.

1.  **`product(discounts, repeat=len(emoticons))`의 역할**
    - 가능한 **모든 할인율 조합(case)**을 생성합니다.
    - 예: 이모티콘이 2개라면 `(10, 10)`, `(10, 20)`, ..., `(40, 40)`까지 총 $4^2=16$개의 튜플이 생성됩니다.
    - 각 `case`는 **모든 이모티콘에 적용될 할인율의 한 세트**입니다.

2.  **`for i in range(len(emoticons))`의 역할**
    - 여기서 `i`는 이모티콘의 **순서(인덱스)**를 나타냅니다.
    - `case`가 `(10, 20)`일 때:
        - `i=0`: 첫 번째 이모티콘(`emoticons[0]`)에 첫 번째 할인율(`case[0]=10%`) 적용
        - `i=1`: 두 번째 이모티콘(`emoticons[1]`)에 두 번째 할인율(`case[1]=20%`) 적용
    - 즉, `i`는 `case`의 일부분을 자르는 것이 아니라, **현재 `case` 세트 내에서 몇 번째 이모티콘의 할인율을 가져올지 결정하는 인덱스**입니다.





## 풀이기록 
### 2025.12.31
```python
from itertools import product

discounts = [10,20,30,40]

def solution(users, emoticons):
    
    optimal_plus_user = 0
    total_sales = 0
    
    for discount_combo in product(discounts, repeat = len(emoticons)):
        ### 현재 할인율 조합 A 에 대해 
        
        subscription_cnt = 0
        total_amount = 0
        
        for discount_limit, price_limit in users:
            ### 사용자 각각에 대해 판매한 이모티콘 판매액을 계산한다.
            
            user_total_purchase = 0
            for i in range(len(emoticons)):
                emo_price = emoticons[i] ## 이모 싸게 해줘
                discount_percent = discount_combo[i]
                
                if discount_percent >= discount_limit:
                    ## 실수하지 말자. 
                    #### emo_price * discount_percent // 100 은 할인액을 구하는거지 할인된 판매액이 아니다. 윽...
                    user_total_purchase += emo_price * (100 - discount_percent) // 100
            
            if user_total_purchase >= price_limit:
                subscription_cnt += 1
            else:
                total_amount += user_total_purchase
                    
            
        ### 이 부분 주의
        if subscription_cnt > optimal_plus_user:
            optimal_plus_user = subscription_cnt
            total_sales = total_amount
        elif subscription_cnt == optimal_plus_user:
            total_sales = max(total_sales, total_amount)
    
    return [optimal_plus_user, total_sales]
```



### (이거 혼동을 야기하는 풀이 방식이다. 너무 단축형으로 쓴다.) (언제풀었는지는 기억 안남)
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