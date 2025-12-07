"""
11053 : 증가수열에서 오름차순 연속 부분수열 중 가장 큰 '길이'
11055 : 증가수열에서 오름차순 연속 부분수열 중 가장 큰 '합'
11722 : 감소수열에서 내림차순 연속 부분수열 중 가장 큰 '길이'
"""

import sys

def solve():
    # 입력 받기
    # n: 수열의 크기 (1 <= n <= 1,000)
    n = int(sys.stdin.readline())
    # a: 수열
    a = list(map(int, sys.stdin.readline().split()))

    # dp[i]: a[i]를 마지막으로 하는 가장 큰 증가하는 부분 수열의 합
    # 초기값은 해당 숫자 자체 (자기 자신만 있는 경우)
    dp = [x for x in a]

    for i in range(n):
        for j in range(i):
            if a[j] < a[i]:
                # 이전 원소(a[j])가 현재 원소(a[i])보다 작다면 (증가 조건)
                # 현재 dp[i]와 dp[j] + a[i] 중 더 큰 값으로 갱신
                dp[i] = max(dp[i], dp[j] + a[i])

    print(max(dp))

if __name__ == "__main__":
    solve()