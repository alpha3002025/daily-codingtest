# 다단계 칫솔 판매

## 문제 설명
다단계 조직이 있습니다. 판매원이 칫솔을 팔면 이익의 10%를 추천인에게 줘야 합니다.
- 추천인도 받은 이익의 10%를 자신의 추천인에게 줍니다.
- 10% 계산 시 1원 미만은 절사하며, 자신이 가집니다(분배 중단).
- 각 판매원의 총 수익을 구하세요.
- `center`(민호)는 최상위이며 수익을 모으지만 결과에는 포함되지 않습니다.

## 문제 해결 전략

각 판매 건수(`seller`, `amount`)마다 이익 분배 로직을 실행합니다.
트리 높이가 크지 않거나(문제 제한: 1만명), 분배 금액이 빠르게 0원이 되어 루프가 일찍 종료되므로 **단순 시뮬레이션(재귀 또는 반복문)**으로 충분합니다.
시간 복잡도: 판매 건수 $M$ $\times$ 트리 높이 $H$. $M=10만$, $H$는 최악의 경우 만. 하지만 금액이 $100 \times 10000$원 정도인데 10%씩 줄어들면 금방 0원이 됨 (로그 스케일). 따라서 $M \times \log(\text{amount})$ 정도의 성능.

1. **트리 구성**: `enroll`과 `referral`을 이용해 `parent` 딕셔너리 생성. `name -> recommender`.
2. **이익 정산**:
   - `seller`가 `amount * 100`원을 범.
   - 현재 사람 `curr`, 현재 금액 `money`.
   - `give = money // 10`
   - `mine = money - give`
   - `curr`의 수익에 `mine` 추가.
   - `curr = parent[curr]`, `money = give`
   - `money`가 0이거나 `curr`가 없으면("-" 등) 종료.

## Python 코드

```python
def solution(enroll, referral, seller, amount):
    # 1. 트리 구성 및 수익 초기화
    parent = {}
    profit = {}
    
    for i, name in enumerate(enroll):
        parent[name] = referral[i]
        profit[name] = 0
        
    # 2. 판매 집계
    for s, amt in zip(seller, amount):
        money = amt * 100
        curr = s
        
        while curr != "-" and money > 0:
            give = money // 10
            mine = money - give
            
            profit[curr] += mine
            
            # 상위로 이동
            curr = parent[curr]
            money = give
            
    # 3. 결과 리스트
    return [profit[name] for name in enroll]
```
