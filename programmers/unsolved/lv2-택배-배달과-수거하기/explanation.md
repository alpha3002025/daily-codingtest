# 택배 배달과 수거하기

## 문제 설명
트럭 하나로 일렬로 늘어선 $n$개의 집에 택배를 배달하고 빈 상자를 수거해야 합니다. 트럭에는 최대 `cap`개 실을 수 있습니다.
각 집에 배달할 상자 개수와 수거할 빈 상자 개수가 주어질 때, 모든 배달과 수거를 마치고 물류창고로 돌아오는 **최소 이동 거리**를 구해야 합니다.

## 풀이 개념
**그리디(Greedy)** 알고리즘을 사용합니다.
**"가장 먼 집부터 해결"**하는 것이 핵심입니다. 먼 곳을 다녀오면서(가는 길/오는 길) 가까운 곳의 작업을 덤으로 처리하는 것이 효율적이기 때문입니다.

### 세부 전략
1. 집을 **가장 먼 곳부터 역순**으로 탐색합니다.
2. 현재 지점에서 배달(`deliveries`)하거나 수거(`pickups`)해야 할 양을 변수(`d_val`, `p_val`)에 누적합니다.
3. 누적된 양이 하나라도 양수(`> 0`)라면, 트럭이 해당 지점까지 와야 한다는 뜻입니다.
4. 트럭이 한 번 올 때마다 `cap`만큼을 처리(배달 및 수거)할 수 있습니다.
   - `d_val`과 `p_val`이 모두 음수나 0이 될 때까지 트럭 왕복 횟수를 늘리며 `cap`을 뺍니다.
   - 이때 트럭은 항상 배달 `cap`개, 수거 `cap`개 능력을 독립적으로 가집니다 (갈 때 배달, 올 때 수거).
5. 남은 음수 값(여유분)은 더 가까운 집의 물량을 처리하는 데 자동으로 사용됩니다.

## 코드 (Python)

```python
def solution(cap, n, deliveries, pickups):
    answer = 0
    d_val = 0 # 배달해야 할 누적량
    p_val = 0 # 수거해야 할 누적량
    
    # 가장 먼 집부터 역순으로 하나씩 확인
    for i in range(n - 1, -1, -1):
        d_val += deliveries[i]
        p_val += pickups[i]
        
        # 배달이나 수거할 짐이 남아있다면 트럭이 와야 함
        while d_val > 0 or p_val > 0:
            d_val -= cap
            p_val -= cap
            
            # 왕복 거리 추가 (거리: i+1)
            # 한번 오면 배달 cap, 수거 cap 만큼 해결 가능
            answer += (i + 1) * 2
            
    return answer
```

### 동작 예시 (`cap=4`)
1. 가장 먼 집(`i`)에 도착했는데 배달 `d_val=5`, 수거 `p_val=0`이라면?
   - 트럭이 1번 와서 4개 처리 -> `d_val=1`, `p_val=-4`. (수거 공간 4개 남음)
   - 아직 `d_val > 0`이므로 트럭 1번 더 옴 -> `d_val=-3`, `p_val=-8`.
   - 총 2번 왕복, `answer += (i+1)*2 * 2`.
   - 남은 `d_val=-3`은 앞쪽 집 3곳의 배달을 덤으로 처리했다는 의미.


## 나의 풀이
예전 풀이가 더 직관적이다.<br/>

```python
def solution(cap, n, deliveries, pickups):
    total_distance = 0
    curr_delivery_cnt = 0
    curr_return_cnt = 0
    last_house = n - 1 ## n = 들를 집의 수
    
    for house in range(n-1, -1,-1): ## 마지막 집에서부터 들른다.
        curr_delivery_cnt += deliveries[house]
        curr_return_cnt += pickups[house]
        
        while curr_delivery_cnt > cap or curr_return_cnt > cap:
            curr_delivery_cnt -= cap
            curr_return_cnt -= cap
            total_distance += 2 * (last_house + 1)
            last_house = house
    
    if curr_delivery_cnt > 0 or curr_return_cnt > 0:
        total_distance += 2 * (last_house + 1)
    
    return total_distance
```


## 코드 질문

### Q. `d_val`, `p_val` 이 음수일때의 의미는 무슨 의미인가요?
A<br/>
`d_val`과 `p_val`이 **음수(-)**라는 것은 **"트럭에 여유 공간(능력)이 남았다"**는 뜻입니다. 이를 **"잉여 능력(Surplus Capacity)"**이나 "미리 땡겨 쓴 빚의 반대(선결제)" 개념으로 생각하시면 이해하기 쉽습니다.

1\. 직관적인 비유 (택배 배달 `d_val` 예시)
상황: `cap=4` (트럭 용량 4)
- **가장 먼 집(5번 집)**에 배달 1개를 해야 합니다. (`d_val = 1`)
- 트럭은 어차피 한 번 가면 4개를 실어갈 수 있습니다.
- 그래서 트럭이 4개를 싣고 5번 집으로 갑니다.
- 5번 집에 1개를 배달하고 나면, 트럭에는 아직 3개의 배달 물품이 남아있습니다.
- 이때의 상태가 `d_val = 1 - 4 = -3` 입니다.
"-3"의 의미: "나는 지금 3개의 물건을 더 배달할 수 있는 여유가 있어. 오는 길에 있는 4번, 3번 집 물건도 3개까지는 추가 이동 없이 그냥 줄 수 있어."


2\. 수거 p_val의 경우
- **가장 먼 집(5번 집)**에서 수거 2개를 해야 합니다. (`p_val = 2`)
- 트럭은 4개를 수거할 수 있는 빈 트럭으로 갑니다.
- 5번 집에서 2개를 수거해도, 트럭엔 아직 2개를 더 실을 수 있는 빈 공간이 남습니다.
- 이때의 상태가 `p_val = 2 - 4 = -2` 입니다.
  - "-2"의 의미: "나는 돌아오는 길에 2개의 빈 상자를 더 수거할 수 있는 빈 공간이 있어. 4번 집 짐이 2개 이하라면 굳이 다시 올 필요 없이 가는 길에 태워 갈게."
