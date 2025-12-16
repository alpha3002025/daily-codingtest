# 등굣길

## 문제 설명
집(1, 1)에서 학교(m, n)까지 가는 최단 경로의 개수를 구하세요.
중간에 물에 잠긴 지역(`puddles`)은 갈 수 없습니다.
오른쪽과 아래쪽으로만 움직일 수 있습니다.
결과를 1,000,000,007로 나눈 나머지 반환.

## 문제 해결 전략

**다이나믹 프로그래밍 (DP)**.
`dp[i][j] = dp[i-1][j] + dp[i][j-1]` (위에서 오는 길 + 왼쪽에서 오는 길)
물에 잠긴 곳은 0으로 처리합니다.
좌표 주의: 문제에서 `(m, n)`은 `(열, 행)` 순서로 줍니다. `puddles`도 `[x, y]`입니다.

## Python 코드

```python
def solution(m, n, puddles):
    # dp[y][x] : 행 n, 열 m
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # 웅덩이 set (좌표 변환 편의)
    puddle_set = set((p[0], p[1]) for p in puddles)
    
    dp[1][1] = 1
    
    for i in range(1, n + 1): # 행
        for j in range(1, m + 1): # 열
            if i == 1 and j == 1:
                continue
                
            if (j, i) in puddle_set: # puddles는 [x, y] = [열, 행]
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
                
    return dp[n][m]
```
