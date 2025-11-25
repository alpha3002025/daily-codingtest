import sys

N = int(sys.stdin.readline().strip())

if N == 1:
    print(0)
elif N == 2:
    print(1)
elif N == 3:
    print(1)
else:
    dp = [float('inf')] * (N+1)

    dp[1] = 0
    dp[2] = 1
    dp[3] = 1

    for n in range(4, N+1):
        if n % 3 == 0:
            dp[n] = min(dp[n//3] + 1, dp[n])
        if n % 2 == 0:
            dp[n] = min(dp[n//2] + 1, dp[n])
        
        dp[n] = min(dp[n-1] + 1, dp[n])

    print(f"{dp[N]}")