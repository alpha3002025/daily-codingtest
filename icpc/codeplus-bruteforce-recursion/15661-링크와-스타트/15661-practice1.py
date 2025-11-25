def solution():
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    
    min_diff = float('inf')
    
    def calculate_score(team):
        return sum(S[i][j] for i in team for j in team)
    
    def backtrack(idx, start_team):
        nonlocal min_diff
        
        if idx == N:
            if 0 < len(start_team) < N:  # 양쪽 모두 1명 이상
                link_team = [i for i in range(N) if i not in start_team]
                diff = abs(calculate_score(start_team) - calculate_score(link_team))
                min_diff = min(min_diff, diff)
            return
        
        # idx를 스타트팀에 포함
        backtrack(idx + 1, start_team + [idx])
        # idx를 링크팀에 포함
        backtrack(idx + 1, start_team)
    
    backtrack(0, [])
    print(min_diff)

solution()