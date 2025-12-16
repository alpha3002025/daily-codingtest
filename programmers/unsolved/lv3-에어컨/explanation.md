# 에어컨

## 문제 설명
현대모비스의 실내 공조 제어 시스템 문제입니다.
차량 내부 온도를 조절하기 위해 에어컨을 켭니다.
- 실외 온도 `outdoor_temp`가 주어집니다.
- 승객이 탑승 중인 시간 `onboard` 배열이 주어집니다.
- 승객이 있는 시간에는 실내 온도를 $t1 \le \text{temp} \le t2$ 사이로 유지해야 합니다.
- 희망 온도를 설정하여 에어컨을 가동하면 전력이 소모됩니다.
    - 현재 온도와 희망 온도가 다르면 코스트 $a$.
    - 현재 온도와 희망 온도가 같으면 코스트 $b$.
    - 에어컨을 끄면 코스트 0 (온도가 실외 온도로 1도씩 수렴).
- 총 전력 소비량을 최소화해야 합니다.

## 문제 해결 전략

**다이나믹 프로그래밍(DP)**을 사용합니다.
시간($t$)과 실내 온도($temp$)를 상태로 가집니다.
$DP[i][j]$: $i$분에 실내 온도가 $j$도일 때의 최소 소비 전력.

### 범위 조정
온도 범위가 -10 ~ 40이므로, 배열 인덱스로 사용하기 위해 +10을 하여 0 ~ 50으로 변환합니다.

### 점화식
$DP[i][j]$는 $DP[i-1]$의 상태들(`j-1`, `j`, `j+1`)에서 전이됩니다.
1. **에어컨을 끄는 경우**:
   - 온도가 실외 온도 방향으로 1도 변하거나, 이미 실외 온도라면 유지됩니다. 비용 0.
2. **에어컨 가동 (온도 변경)**:
   - 온도를 1도 올리거나 내리기 위해 비용 $a$ 사용.
3. **에어컨 가동 (온도 유지)**:
   - 현재 온도를 유지하기 위해 비용 $b$ 사용.

**승객 탑승 조건**:
`onboard[i] == 1`인 경우, 온도 $j$가 $t1$ ~ $t2$ 범위를 벗어나면 $DP[i][j] = \infty$ 처리합니다.

## Python 코드

```python
def solution(temperature, t1, t2, a, b, onboard):
    # 온도 범위 보정 (0 ~ 50)
    temperature += 10
    t1 += 10
    t2 += 10
    
    # DP 테이블 초기화
    # dp[time][temp]
    # 최대 시간: len(onboard)
    # 온도 범위: 0 ~ 50
    curr_dp = [1e9] * 52 # 0~51 (padding)
    
    # 시작 상태: 실외 온도에서 시작, 비용 0
    curr_dp[temperature] = 0
    
    for i in range(1, len(onboard)):
        next_dp = [1e9] * 52
        
        # 승객 탑승 여부에 따른 유효 온도 범위
        valid_low, valid_high = 0, 51
        if onboard[i] == 1:
            valid_low, valid_high = t1, t2
            
        for t in range(51):
            # 1. 에어컨 OFF (실외 온도로 수렴)
            if t == temperature:
                # 이전 온도 t, t-1, t+1 에서 올 수 있음? 
                # OFF면 방향성 있음.
                # temperature < t : t-1 -> t (1도 상승) 불가. 자연상승은 실외온도 방향.
                # temperature > t : t+1 -> t (1도 하강) 불가.
                pass 
                
            # 정석 전이:
            # next_dp[t]를 계산하기 위해 가능한 prev_temp을 찾는다?
            # 반대로 prev_dp[t]에서 next_dp의 어디로 갈 수 있는지 뿌려주는게 편함.
            if curr_dp[t] == 1e9: continue
            
            cost = curr_dp[t]
            
            # CASE 1: 에어컨 OFF
            # 1-1. 현재 t가 실외온도보다 낮으면 -> t+1 로 상승
            if t < temperature:
                next_t = t + 1
                if valid_low <= next_t <= valid_high or onboard[i] == 0:
                    next_dp[next_t] = min(next_dp[next_t], cost)
            # 1-2. 현재 t가 실외온도보다 높으면 -> t-1 로 하강
            elif t > temperature:
                next_t = t - 1
                if valid_low <= next_t <= valid_high or onboard[i] == 0:
                     next_dp[next_t] = min(next_dp[next_t], cost)
            # 1-3. 같으면 유지
            else:
                if valid_low <= t <= valid_high or onboard[i] == 0:
                    next_dp[t] = min(next_dp[t], cost)
                    
            # CASE 2: 에어컨 ON (온도 변경, 비용 a)
            # t -> t+1
            if t + 1 <= 50:
                if valid_low <= t+1 <= valid_high or onboard[i] == 0:
                    next_dp[t+1] = min(next_dp[t+1], cost + a)
            # t -> t-1
            if t - 1 >= 0:
                if valid_low <= t-1 <= valid_high or onboard[i] == 0:
                    next_dp[t-1] = min(next_dp[t-1], cost + a)
                    
            # CASE 3: 에어컨 ON (온도 유지, 비용 b)
            if valid_low <= t <= valid_high or onboard[i] == 0:
                next_dp[t] = min(next_dp[t], cost + b)
        
        curr_dp = next_dp

    return min(curr_dp)
```
