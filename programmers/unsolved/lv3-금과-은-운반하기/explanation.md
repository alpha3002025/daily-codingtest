# 금과 은 운반하기

## 문제 설명
여러 도시에서 금과 은을 캐서 새 도시로 운반합니다.
- `i`번 도시: 금 `g[i]`, 은 `s[i]`, 트럭 1대 보유.
- 트럭 스펙: 편도 시간 `t[i]`, 최대 적재량 `w[i]`.
- 목표: 금 `a` kg, 은 `b` kg을 모으는 가장 빠른 시간.

## 문제 해결 전략

최단 시간을 구하는 최적화 문제입니다. 하지만 상태공간이 복잡하여 DP나 그리디로 풀기 어렵습니다.
**이분 탐색 (Parametric Search)**을 사용합니다.
- "시간 `T`가 주어졌을 때, 금 `a`와 은 `b`를 모두 모을 수 있는가?" (결정 문제)
- 이 결정 문제를 풀 수 있다면, 가능한 `T`의 최소값을 이분 탐색으로 찾을 수 있습니다.

**결정 문제 로직**:
시간 `T`가 주어지면, 각 도시는 `CNT`회의 왕복이 가능합니다.
- 총 이동 횟수: `cnt = T // (t[i] * 2)`
- 편도 추가 가능 여부: `if T % (2 * t[i]) >= t[i]: cnt += 1`
- 총 운반 가능량: `W = cnt * w[i]`

각 도시에서 가져올 수 있는 최대 금: `G_max = min(g[i], W)`
각 도시에서 가져올 수 있는 최대 은: `S_max = min(s[i], W)`
각 도시에서 가져올 수 있는 최대 광물 합: `Total_max = min(g[i] + s[i], W)`

전체 도시 합산:
- `sum_G`: 모든 도시의 `G_max` 합
- `sum_S`: 모든 도시의 `S_max` 합
- `sum_Total`: 모든 도시의 `Total_max` 합

조건 만족 여부:
- `sum_G >= a`
- `sum_S >= b`
- `sum_Total >= a + b`
세 조건이 모두 만족해야 합니다.
(왜냐하면 금을 최대로 가져오면서 은을 포기해야 할 수도 있고, 그 반대일 수도 있는데, 전체 용량 합(`sum_Total`)이 `a+b` 이상이고 각각 최대치 합도 충족한다면, 적절히 배분하여 `a`, `b`를 맞출 수 있음이 보장됩니다.)

## Python 코드

```python
def solution(a, b, g, s, w, t):
    
    def is_possible(time):
        total_gold = 0
        total_silver = 0
        total_mix = 0
        
        for i in range(len(g)):
            # 왕복 횟수 + 편도 1회
            # 왕복 시간 2*t[i]
            cnt = time // (2 * t[i])
            if time % (2 * t[i]) >= t[i]:
                cnt += 1
                
            capacity = cnt * w[i]
            
            # 이 도시에서 가져올 수 있는 최대치들
            can_take_gold = min(g[i], capacity)
            can_take_silver = min(s[i], capacity)
            can_take_mix = min(g[i] + s[i], capacity)
            
            total_gold += can_take_gold
            total_silver += can_take_silver
            total_mix += can_take_mix
            
        if total_gold >= a and total_silver >= b and total_mix >= a + b:
            return True
        return False
    
    # 이분 탐색 범위
    # 최소 0, 최대 ?
    # 최악의 경우: 광물 10^9 + 10^9 = 2*10^9.
    # 무게 1, 시간 10^5 인 트럭 1대
    # -> 2*10^9 번 왕복 * 2*10^5 시간 ~~ 4*10^14. 매우 큼.
    # 넉넉히 10^15 (10**15)
    start = 0
    end = 10**15 
    answer = end
    
    while start <= end:
        mid = (start + end) // 2
        if is_possible(mid):
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
            
    return answer
```
