import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
MAX_TEAM_LIMIT = N//2


def calculate(team):
    total = 0
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            total += board[team[i]][team[j]] + board[team[j]][team[i]]
    return total


min_score = float('inf')
def backtracking(curr_idx, start_team):
    global min_score

    if len(start_team) == MAX_TEAM_LIMIT:
        link_team = [i for i in range(N) if i not in start_team]
        start_team_score = calculate(start_team)
        link_team_score = calculate(link_team)
        min_score = min(min_score, abs(start_team_score - link_team_score))
    
    if min_score == 0:
        return

    for i in range(curr_idx, N):
        start_team.append(i)
        backtracking(i+1, start_team)
        start_team.pop()
    

backtracking(0, [])
print(min_score)