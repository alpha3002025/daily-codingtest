# 6236번: 용돈 관리

## 1. 문제 개요
현우는 N일 동안 살면서 소비할 금액을 미리 알고 있습니다.  
현우는 통장에서 돈을 인출할 때 **정확히 M번**만 인출하고 싶어 합니다. 한 번 인출할 때마다 **K원**을 인출하며, 돈이 부족하면 남은 돈을 다시 통장에 넣고 K원을 새로 인출합니다.  
**K의 최소 금액**을 구하는 것이 목표입니다.

- **입력**: N(일수), M(인출 횟수), N일 동안의 소비 금액 리스트
- **출력**: 조건을 만족하는 K의 최솟값

---

## 2. 해결 전략: 파라메트릭 서치 (Parametric Search)
이 문제는 **"특정 금액 K를 정했을 때, M번 이하의 인출로 N일을 버틸 수 있는가?"** 라는 결정 문제(Yes/No)로 바꿀 수 있습니다.  
K의 값이 커질수록 인출 횟수는 줄어들고, K의 값이 작아질수록 인출 횟수는 늘어납니다. 이러한 단조성을 이용해 이분 탐색을 수행합니다.

### 1) 탐색 범위 설정 (`Left`, `Right`)
- **최솟값 (`Left`)**: `max(money_list)`
  - 하루에 소비해야 할 금액 중 가장 큰 금액보다는 K가 커야 합니다. 그렇지 않으면 어떤 날은 하루도 버틸 수 없게 됩니다.
- **최댓값 (`Right`)**: `sum(money_list)`
  - 모든 금액을 합친 만큼을 K로 설정하면, 딱 1번만 인출해서 N일을 모두 버틸 수 있습니다.

### 2) 시뮬레이션 (`check` 로직)
설정한 `mid` (인출 금액 K)로 N일을 순서대로 시뮬레이션합니다.
- 현재 가진 돈(`current`)이 오늘의 소비 금액(`money`)보다 부족하면:
  - 새로 인출합니다 (`count += 1`)
  - 잔액을 K원으로 리셋 (`current = mid`)
- 가진 돈에서 소비 금액을 뺍니다.

### 3) 조건 분기
- **인출 횟수 > M**:
  - 돈을 너무 조금씩 뽑아서 자주 인출하게 된 것입니다.
  - K를 늘려야 합니다. (`Left = mid + 1`)
- **인출 횟수 <= M**:
  - 조건 충족. (인출 횟수가 M보다 적더라도, 남은 돈을 다시 넣고 빼는 행위로 횟수를 늘릴 수 있으므로 유효한 해입니다.)
  - K를 더 줄일 수 있는지 확인해봅니다. (`Right = mid - 1`, `Answer = mid`)

---

## 3. Python 풀이 코드

```python
import sys

# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

N, M = map(int, input().split())
money_list = [int(input()) for _ in range(N)]

# 1. 탐색 범위 설정
# K는 적어도 하루 소비액 중 최댓값보다는 커야 함 (안 그러면 그 날 생활 불가)
left = max(money_list)
# K가 전체 합이면 한 번만 인출해도 됨
right = sum(money_list)

answer = 0

while left <= right:
    mid = (left + right) // 2  # 인출할 금액 K
    
    current_money = 0
    count = 0 # 인출 횟수
    
    # 2. 시뮬레이션
    for money in money_list:
        if current_money < money:
            # 돈이 부족하면 남은 돈 넣고(0원처리) 새로 인출
            current_money = mid
            count += 1
        
        current_money -= money
        
    # 3. 결과 판단
    if count > M:
        # M번보다 더 많이 인출함 -> 한 번 뽑는 금액(mid)이 너무 적음
        left = mid + 1
    else:
        # M번 이하로 인출함 -> 가능함 (M번보다 적으면 억지로 늘릴 수 있음)
        # 최소 K를 찾기 위해 금액을 줄여봄
        answer = mid # 일단 정답 후보 저장
        right = mid - 1

print(answer)
```

## 4. 시간 복잡도
- 탐색 범위의 크기: `sum(money_list)` (최대 약 $100,000 \times 10,000 = 10^9$)
- 이분 탐색 횟수: $O(\log(\sum \text{money}))$
- 1회 확인(Simulation) 시간: $O(N)$
- **총 시간 복잡도**: $O(N \log(\sum \text{money}))$
  - $N=100,000$ 이므로 충분히 시간 내(1초)에 통과 가능합니다.
