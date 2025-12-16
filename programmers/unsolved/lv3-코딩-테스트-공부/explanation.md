# 코딩 테스트 공부

## 문제 설명
코딩 테스트 통과를 위해 `alp`(알고리즘력)과 `cop`(코딩력)을 길러야 합니다.
- 시작 시 `alp`, `cop`을 가집니다.
- 목표는 모든 문제들을 풀 수 있는 능력치(`max_alp`, `max_cop`)에 도달하는 것입니다.
- 1시간 공부하여 `alp` 1 증가 또는 `cop` 1 증가 가능.
- 주어진 `problems` 리스트의 문제들을 풀면 `alp`, `cop`이 증가하며 시간이 소요됨. (문제마다 요구 능력치 `alp_req`, `cop_req`와 보상 `alp_rwd`, `cop_rwd`, 소요시간 `cost`가 있음)
- 모든 문제를 풀 수 있는 능력치(각 요구사항의 최대값)까지 도달하는 최단 시간을 구하세요.

## 문제 해결 전략

**다이나믹 프로그래밍(DP)** 또는 **다익스트라(Dijkstra)** 문제입니다.
상태 공간 `(alp, cop)`에서 목표 상태 `(max_alp, max_cop)`까지 가는 최단 거리(시간)를 찾는 문제입니다.

1. **목표 설정**:
   `target_alp` = max(`problems`의 `alp_req`)
   `target_cop` = max(`problems`의 `cop_req`)
   단, 초기 능력이 이미 목표보다 높을 수 있으므로 `alp = min(alp, target_alp)` 처리를 해야 합니다.

2. **DP 테이블**:
   `dp[a][c]` = 알고리즘력 `a`, 코딩력 `c`에 도달하는 최소 시간.
   범위는 `start_alp` ~ `target_alp`, `start_cop` ~ `target_cop`.
   초기값: `dp[start_alp][start_cop] = 0`, 나머지 무한대.

3. **전이 (Transitions)**:
   현재 상태 `(i, j)`에서:
   - 공부하기:
     - `dp[i+1][j] = min(..., dp[i][j] + 1)`
     - `dp[i][j+1] = min(..., dp[i][j] + 1)`
   - 문제 풀기:
     - 각 문제 `p`에 대해, 만약 `i >= p.alp_req`이고 `j >= p.cop_req`라면:
       - `next_alp = min(target_alp, i + p.alp_rwd)`
       - `next_cop = min(target_cop, j + p.cop_rwd)`
       - `dp[next_alp][next_cop] = min(..., dp[i][j] + p.cost)`

   DP 순서는 `alp` 오름차순, `cop` 오름차순으로 진행하면 됩니다 (기본 공부가 1씩 증가시키므로).

## Python 코드

```python
def solution(alp, cop, problems):
    # 목표 능력치
    max_alp = 0
    max_cop = 0
    
    for p in problems:
        max_alp = max(max_alp, p[0])
        max_cop = max(max_cop, p[1])
        
    # 초기 능력이 이미 목표를 넘었을 경우 보정
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    
    # DP 테이블 초기화 (최대값 넉넉히)
    # dp[i][j] : alp=i, cop=j 도달 최소 시간
    # 인덱스는 max_alp, max_cop까지
    
    dp = [[float('inf')] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0
    
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            # 1. 1시간 공부해서 증가
            if i + 1 <= max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            if j + 1 <= max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
                
            # 2. 문제 풀어서 증가
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    next_alp = min(max_alp, i + alp_rwd)
                    next_cop = min(max_cop, j + cop_rwd)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + cost)
                    
    return dp[max_alp][max_cop]
```
