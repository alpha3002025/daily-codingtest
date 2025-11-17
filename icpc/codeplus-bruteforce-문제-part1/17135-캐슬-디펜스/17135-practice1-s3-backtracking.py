import sys
import copy

N,M,D = map(int, sys.stdin.readline().split())

board = []
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))


def simulate(archer_positions, grid, N, M, D):
    """게임 시뮬레이션"""
    game_grid = copy.deepcopy(grid)
    killed = 0

    for turn in range(N):
        targets = set()



