import sys

# 표준 입력을 받기 위한 설정
input = sys.stdin.readline

def solve():
    try:
        # N과 K 입력 받기
        # N: 배열의 크기 (1 <= N <= 10^5)
        # K: 찾고자 하는 순서 (1 <= K <= min(10^9, N^2))
        N = int(input())
        K = int(input())
    except (ValueError, IndexError):
        # 입력이 없는 경우 등을 대비 (로컬 테스트용)
        return

    # 이분 탐색 범위 설정
    # lo: 가능한 최솟값 (1)
    # hi: 가능한 최댓값 (K). K번째 수는 K보다 클 수 없음이 증명되어 있음.
    # 물론 N*N까지 잡아도 무방함.
    start = 1
    end = K
    
    ans = 0
    
    while start <= end:
        mid = (start + end) // 2
        
        # count: mid보다 작거나 같은 수의 개수
        count = 0
        for i in range(1, N + 1):
            # i번째 행에서 mid보다 작거나 같은 수의 개수는
            # min(N, mid // i)
            count += min(N, mid // i)
        
        if count >= K:
            # mid보다 작거나 같은 수가 K개 이상이면, mid는 K번째 수의 후보임
            # 더 작은 수 중에서도 가능한지 확인하기 위해 범위를 줄임
            ans = mid
            end = mid - 1
        else:
            # mid보다 작거나 같은 수가 K개 미만이면, mid는 너무 작음
            start = mid + 1
            
    print(ans)

if __name__ == '__main__':
    solve()
