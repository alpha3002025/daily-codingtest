import sys

N = int(sys.stdin.readline().strip())
board = [list(map(int,sys.stdin.readline().split())) for r in range(N)]

min_diff = float('inf')

def calculate(team):
    return sum(board[i][j] for j in team for i in team)

def backtracking(curr, start_team):
    global min_diff
    if curr == N:
        if 0 < len(start_team) < N:
            link_team = [n for n in range(N) if n not in start_team]
            start_sum = calculate(start_team)
            link_sum = calculate(link_team)
            min_diff = min(min_diff, abs(start_sum - link_sum))
        return


    backtracking(curr+1, start_team + [curr])
    backtracking(curr+1, start_team)


backtracking(0, [])
print(f"{min_diff}")