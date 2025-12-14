# 프로그래머스 - 완전범죄 (Lv.2)

## 1. 문제 분석
두 명의 도둑 A와 B가 팀을 이뤄 물건을 훔칩니다. 각 물건마다 A가 훔칠 때 남기는 흔적과 B가 훔칠 때 남기는 흔적이 다릅니다.
- **목표**: 모든 물건을 훔치면서, A와 B 모두 경찰에 잡히지 않아야 합니다. 이때 **A가 남긴 흔적의 합을 최소화**해야 합니다.
- **제한 조건**:
  - A는 누적 흔적이 `n` 이상이면 잡힙니다. (즉, `n` 미만이어야 함)
  - B는 누적 흔적이 `m` 이상이면 잡힙니다. (즉, `m` 미만이어야 함)
  - 불가능한 경우 `-1`을 반환합니다.

## 2. 알고리즘 설계 (Dynamic Programming)
이 문제는 전형적인 배낭 문제(Knapsack Problem)의 변형으로 볼 수 있습니다.
각 물건에 대해 **"A가 훔친다"** 또는 **"B가 훔친다"** 두 가지 선택지가 있으며, 이 선택에 따라 두 개의 상태값(A의 흔적, B의 흔적)이 변합니다.

우리는 **A의 흔적을 최소화**하는 것이 목표이므로, DP 테이블의 인덱스를 **B의 흔적 합**으로, 값을 **A의 최소 흔적 합**으로 설정하여 관리할 수 있습니다.

### 상태 정의 (State Definition)
`dp[j]` = **B의 누적 흔적이 `j`일 때, 가능한 A의 최소 누적 흔적**

- `j`의 범위: `0`부터 `m-1`까지 (B가 잡히지 않는 범위)
- `dp` 값: A가 잡히지 않는 범위(`0` ~ `n-1`) 내의 최소값. 초기값은 무한대(`INF`)로 설정.

### 점화식 (Transition)
각 물건(Item)을 순회하며 기존 DP 테이블을 갱신합니다.
현재 물건의 흔적이 `trace_A`, `trace_B`일 때, 기존 `dp[b]` (B의 흔적이 `b`, A의 흔적이 `dp[b]`) 상태에서 두 가지 경우로 파생됩니다.

1.  **A가 훔치는 경우**:
    - 새로운 A 흔적: `dp[b] + trace_A`
    - 새로운 B 흔적: `b` (변화 없음)
    - 조건: `dp[b] + trace_A < n`
    - 갱신: `new_dp[b] = min(new_dp[b], dp[b] + trace_A)`

2.  **B가 훔치는 경우**:
    - 새로운 A 흔적: `dp[b]` (변화 없음)
    - 새로운 B 흔적: `b + trace_B`
    - 조건: `b + trace_B < m`
    - 갱신: `new_dp[b + trace_B] = min(new_dp[b + trace_B], dp[b])`

### 시간 복잡도
- 물건의 개수(`len(info)`) × B의 한계(`m`)
- 최대 연산 횟수: 40 × 120 = 4,800회 (매우 효율적)

## 3. Python 풀이 코드

```python
def solution(info, n, m):
    # dp[j] = B의 누적 흔적이 j일 때, A의 최소 누적 흔적
    # 초기화: 불가능한 상태는 INF로 설정
    INF = float('inf')
    dp = [INF] * m
    dp[0] = 0  # 초기 상태: 아무것도 훔치지 않았을 때 (A=0, B=0)
    
    for trace_a, trace_b in info:
        new_dp = [INF] * m  # 이번 아이템을 처리한 후의 상태를 저장할 배열
        
        for b in range(m):
            if dp[b] == INF:  # 도달 불가능한 상태는 건너뜀
                continue
            
            # 현재 상태: A의 흔적 = dp[b], B의 흔적 = b
            current_a = dp[b]
            
            # 1. A가 훔치는 경우
            if current_a + trace_a < n:
                new_dp[b] = min(new_dp[b], current_a + trace_a)
            
            # 2. B가 훔치는 경우
            if b + trace_b < m:
                new_dp[b + trace_b] = min(new_dp[b + trace_b], current_a)
        
        dp = new_dp  # DP 테이블 업데이트

    # 모든 아이템 처리 후, 가능한 상태 중 A의 최소 흔적 찾기
    answer = min(dp)
    
    return answer if answer != INF else -1
```

## 4. 예시 설명
만약 `info = [[2, 3], [4, 1]]`, `n = 10`, `m = 5`라면:

1. **초기 상태**: `dp[0] = 0`, 나머지 INF
2. **첫 번째 물건 [2, 3]**:
   - A가 훔침: `new_dp[0] = min(INF, 0+2) = 2` (B는 0 유지)
   - B가 훔침: `new_dp[3] = min(INF, 0) = 0` (B는 0+3=3 됨)
   - 결과 `dp`: `[2, INF, INF, 0, INF]`
3. **두 번째 물건 [4, 1]**:
   - `dp[0]=2`에서 파생:
     - A가 훔침: `new_dp[0] = 2+4 = 6`
     - B가 훔침: `new_dp[1] = 2` (B는 0+1=1)
   - `dp[3]=0`에서 파생:
     - A가 훔침: `new_dp[3] = 0+4 = 4`
     - B가 훔침: `new_dp[4] = 0` (B는 3+1=4)
   - 최종 `dp`: `[6, 2, INF, 4, 0]`
4. **결과**: `min(dp) = 0`.
   - 이 경우 두 번째 물건에서 `dp[4]=0`이 된 경로는 (1번: B가 훔침, 2번: B가 훔침) -> A흔적 0, B흔적 4.
