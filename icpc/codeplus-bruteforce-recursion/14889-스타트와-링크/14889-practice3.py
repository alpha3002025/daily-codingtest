import sys
input = sys.stdin.readline

N = int(input())
limit = N//2

board = [list(map(int, input().split())) for _ in range(N)]
min_gap = float('inf')


def calculate(team):
    total = 0
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            total += board[team[i]][team[j]] + board[team[j]][team[i]]
    return total


def backtracking(curr_idx, start_team):
    global min_gap

    if len(start_team) == limit:
        link_team = [i for i in range(N) if i not in start_team]
        start_score = calculate(start_team)
        link_score = calculate(link_team)
        min_gap = min(min_gap, abs(start_score - link_score))
        return

    if min_gap == 0:
        return
    
    for i in range(curr_idx, N):
        start_team.append(i) ### 이 부분으 curr_idx 를 추가했었다. 그러면 안된다!!! (그렇게 하는 건 이진 선택 기준에서 선택하는 방식이다.)
        backtracking(i+1, start_team) ### 이 부분에 curr_idx+1 을 지정하는 무리수를 뒀었다.
        start_team.pop()

backtracking(0, [])
print(f"{min_gap}")