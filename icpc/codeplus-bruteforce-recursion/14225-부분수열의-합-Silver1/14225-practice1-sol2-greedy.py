import sys
# 입력 데이터가 많지 않으므로 한 줄씩 읽습니다.
input = sys.stdin.readline

def solve_greedy():
    # N: 수열의 크기
    N = int(input())
    
    # S: 수열을 입력받아 정렬
    S = list(map(int, input().split()))
    S.sort() # 그리디 접근의 핵심: 오름차순 정렬

    # reachable_sum: 현재까지의 원소들로 만들 수 있는 1부터 시작하는 연속된 합의 최댓값
    reachable_sum = 0 
    
    for s in S:
        # 현재 원소 s가 (현재 만들 수 있는 최대 합 + 1)보다 크다면,
        # 'reachable_sum + 1'은 s나 그 이후 원소를 이용해서도 만들 수 없는 최소값이다.
        if s > reachable_sum + 1:
            # 만들 수 없는 최소값을 찾았으므로 종료
            break
        
        # s를 포함함으로써 만들 수 있는 연속된 합의 범위를 확장
        # (기존의 합 1 ~ reachable_sum) + s = (s+1) ~ (reachable_sum + s)
        # 따라서 1 ~ (reachable_sum + s)까지 모두 만들 수 있게 됨
        reachable_sum += s
        
    # 루프가 끝난 후에도 찾지 못했다면,
    # 1부터 reachable_sum까지는 모두 만들 수 있으며, 
    # 그 다음 수인 reachable_sum + 1이 만들 수 없는 최소값이다.
    print(reachable_sum + 1)

solve_greedy()