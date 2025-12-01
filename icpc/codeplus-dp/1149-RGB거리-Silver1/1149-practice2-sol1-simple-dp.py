import sys
input = sys.stdin.readline

N = int(input())
houses = [list(map(int, input().split())) for _ in range(N)]

R,G,B = 0,1,2

dp = [[0]*3 for _ in range(N)]

"""
점화식
## i번째에서 R을 선택
dp[i][R] = cost[i][R] + min(dp[i-1][G], dp[i-1][B]) ## 두번 연속 같은 색상은 불가능하므로 빨->빨 제외한 계산
## i번째에서 G를 선택
dp[i][G] = cost[i][G] + min(dp[i-1][R], dp[i-1][B]) ## 두번 연속 같은 색상은 불가능하므로 초->초 제외한 계산
## i번째에서 B를 선택
dp[i][B] = cost[i][B] + min(dp[i-1][R], dp[i-1][G]) ## 두번 연속 같은 색상은 불가능하므로 파->파 제외한 계산
"""

dp[0][R] = houses[0][R]
dp[0][G] = houses[0][G]
dp[0][B] = houses[0][B]

for i in range(1,N):
    dp[i][R] = houses[i][R] + min(dp[i-1][G], dp[i-1][B])
    dp[i][G] = houses[i][G] + min(dp[i-1][R], dp[i-1][B])
    dp[i][B] = houses[i][B] + min(dp[i-1][R], dp[i-1][G])

print(min(dp[N-1]))