# 거스름돈

## 문제 설명
물건 가격 `n`원을 거슬러 줄 때, `money`에 있는 화폐 단위들을 사용하여 거슬러 주는 방법의 수를 구하세요. (화폐 개수는 무한)

## 문제 해결 전략

**다이나믹 프로그래밍 (DP)**.
`dp[i]` = 합이 `i`원이 되는 경우의 수.
동전 종류별로 반복하며 dp 테이블을 갱신합니다 (Knapsack 유사, 순서 없는 조합).
점화식: `dp[i] += dp[i - coin]`

## Python 코드

```python
def solution(n, money):
    dp = [0] * (n + 1)
    dp[0] = 1 # 0원을 만드는 방법 1가지 (아무것도 안 냄)
    
    for coin in money:
        for i in range(coin, n + 1):
            dp[i] = (dp[i] + dp[i - coin]) % 1000000007
            
    return dp[n]
```
