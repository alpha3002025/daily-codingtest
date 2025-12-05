import sys
input = sys.stdin.readline

M,N = map(int, input().split())
cookies = list(map(int, input().split()))

if N < M and sum(cookies) < M:
    print(0)
else:
    left,right = 1, max(cookies)

    ## 과자의 길이를 최대한 길게
    max_length = 0
    while left <= right:
        mid = (left + right)//2

        cnt = 0
        for cookie in cookies:
            cnt += cookie//mid
        
        if cnt >= M:
            left = mid+1
            max_length = max(max_length, mid)
        else:
            right = mid-1

    print(max_length)