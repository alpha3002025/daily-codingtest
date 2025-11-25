def solve():
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    
    min_diff = float('inf')
    
    def calculate_team_ability(team):
        """팀의 능력치 합 계산"""
        ability = 0
        for i in range(len(team)):
            for j in range(i + 1, len(team)):
                ability += S[team[i]][team[j]] + S[team[j]][team[i]]
        return ability
    
    def backtrack(idx, start_team):
        nonlocal min_diff
        
        # 스타트 팀이 N//2명이 되면 계산
        if len(start_team) == N // 2:
            # 링크 팀 구성
            link_team = [i for i in range(N) if i not in start_team]
            
            # 각 팀의 능력치 계산
            start_ability = calculate_team_ability(start_team)
            link_ability = calculate_team_ability(link_team)
            
            # 최소 차이 갱신
            min_diff = min(min_diff, abs(start_ability - link_ability))
            return
        
        # 가지치기: 이미 최적해를 찾았으면 종료
        if min_diff == 0:
            return
        
        # idx부터 N-1까지 선택
        for i in range(idx, N):
            start_team.append(i)
            backtrack(i + 1, start_team)
            start_team.pop()
    
    backtrack(0, [])
    print(min_diff)

solve()