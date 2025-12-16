# n + 1 카드게임

## 문제 설명
1부터 n까지의 카드가 있습니다. 처음에 `n/3`장을 가지고 시작하며, 매 라운드 2장씩 카드를 뽑습니다. 뽑은 카드를 가지려면 코인(동전)을 써야 합니다. 매 라운드마다 손에 있는 카드 2장을 내서 합이 `n+1`이 되도록 해야 다음 라운드로 넘어갈 수 있습니다. 최대 몇 라운드까지 갈 수 있는지 구하는 문제입니다.

## 문제 해결 전략

이 문제는 **그리디(Greedy)** 알고리즘으로 해결할 수 있습니다.
핵심 아이디어는 "현재 뽑은 카드를 꼭 지금 사지 않아도 된다"는 점을 파악하는 것입니다.
- 뽑은 카드는 `drawn` 목록(가상의 임시 저장소)에 둡니다.
- 당장 라운드를 넘기기 위해 카드가 필요하다면, 그때 코인을 지불하고 가져오면 됩니다.
- 코인을 적게 쓰는 방법부터 고려합니다.

### 우선순위 전략
매 라운드(페이즈)마다 카드 2장을 `drawn`에 추가합니다.
생존을 위해 카드 한 쌍(합이 `n+1`)을 제출해야 합니다.
다음 순서로 제출 가능한 쌍을 찾습니다:

1. **내 손(Hand)에 있는 카드끼리 (`Cost 0`)**: 코인을 쓰지 않고 넘길 수 있다면 가장 좋습니다.
2. **내 손(Hand)에 있는 카드 + 뽑아둔 카드(Drawn) (`Cost 1`)**: 코인 1개를 써서 짝을 맞춥니다.
3. **뽑아둔 카드(Drawn)끼리 (`Cost 2`)**: 정 안되면 코인 2개를 써서 짝을 맞춰야 합니다.

매 라운드마다 위 1->2->3 순서로 가능한지 체크하고, 가능하면 해당 비용을 지불하고 라운드를 진행합니다. 불가능하면 게임이 종료됩니다.

## Python 코드

```python
def solution(coin, cards):
    n = len(cards)
    hand = set(cards[:n//3])
    deck = cards[n//3:]
    
    drawn = set() # 뽑았지만 아직 코인을 안 쓴 카드들 (구매 가능 목록)
    
    round_num = 1
    
    # 덱에서 2장씩 처리
    # deck을 큐처럼 사용하거나 인덱스로 접근
    idx = 0
    while idx < len(deck):
        # 카드 2장 뽑기
        c1 = deck[idx]
        c2 = deck[idx+1]
        drawn.add(c1)
        drawn.add(c2)
        idx += 2
        
        # 이번 라운드를 넘길 수 있는지 확인
        # 우선순위 1: Hand + Hand (Cost 0)
        passed = False
        
        # Hand 내에서 해결 가능한가?
        for card in list(hand):
            target = (n + 1) - card
            if target in hand:
                hand.remove(card)
                hand.remove(target)
                passed = True
                break
        
        if passed:
            round_num += 1
            continue
            
        # 우선순위 2: Hand + Drawn (Cost 1)
        if coin >= 1:
            for card in list(hand):
                target = (n + 1) - card
                if target in drawn:
                    hand.remove(card)
                    drawn.remove(target)
                    coin -= 1
                    passed = True
                    break
        
        if passed:
            round_num += 1
            continue
            
        # 우선순위 3: Drawn + Drawn (Cost 2)
        if coin >= 2:
            for card in list(drawn):
                target = (n + 1) - card
                if target in drawn:
                    drawn.remove(card)
                    drawn.remove(target)
                    coin -= 2
                    passed = True
                    break
        
        if passed:
            round_num += 1
        else:
            break
            
    return round_num
```
