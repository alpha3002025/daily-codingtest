import sys

N = int(sys.stdin.readline().strip())
board = [list(map(int,sys.stdin.readline().split())) for r in range(N)]

min_diff = float('inf')

def calculate_team(team):
    total = 0
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            total += (board[team[i]][team[j]] + board[team[j]][team[i]])
    return total


def backtrack(curr, start_team):
    global min_diff

    if len(start_team) == N//2:
        link_team = [n for n in range(N) if n not in start_team]
        start_sum = calculate_team(start_team)
        link_sum = calculate_team(link_team)

        min_diff = min(min_diff, abs(start_sum - link_sum))
        return
    
    if min_diff == 0:
        return

    for i in range(curr, N):
        start_team.append(i)
        backtrack(i+1, start_team)
        start_team.pop()

backtrack(0, [])
print(min_diff)
