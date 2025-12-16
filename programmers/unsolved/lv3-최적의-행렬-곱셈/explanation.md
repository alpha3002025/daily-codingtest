# 최적의 행렬 곱셈

## 문제 설명
행렬의 크기들이 주어질 때 (`matrix_sizes`), 모든 행렬을 곱하는데 필요한 곱셈 연산 횟수의 최솟값을 구하세요.
행렬 곱셈 순서에 따라 연산 횟수가 달라집니다 (결합법칙 성립).

## 문제 해결 전략

**다이나믹 프로그래밍 (Matrix Chain Multiplication)**.
`dp[i][j]`: i번째 행렬부터 j번째 행렬까지 곱했을 때의 최소 연산 횟수.
점화식:
`dp[i][j] = min(dp[i][k] + dp[k+1][j] + (sizes[i][0] * sizes[k][1] * sizes[j][1]))` for `k` in range `i` to `j-1`.
대각선 방향(구간 길이 순)으로 채워나갑니다.

## Python 코드

```python
def solution(matrix_sizes):
    n = len(matrix_sizes)
    # dp[i][j] -> i~j 구간 최소 비용
    dp = [[0] * n for _ in range(n)]
    
    # gap: 구간 길이 (1 ~ n-1)
    for gap in range(1, n):
        for i in range(n - gap):
            j = i + gap
            dp[i][j] = float('inf')
            
            # 분할 지점 k
            for k in range(i, j):
                # (i~k) * (k+1~j) 비용
                # 곱셈 비용: i행 * k열 * j열 (matrix_sizes[i][0] * matrix_sizes[k][1] * matrix_sizes[j][1])
                cost = dp[i][k] + dp[k+1][j] + \
                       (matrix_sizes[i][0] * matrix_sizes[k][1] * matrix_sizes[j][1])
                
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    
    return dp[0][n-1]
```
