import sys
from itertools import permutations

N = int(input())
scores = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 메모이제이션: (이닝, 타자순서, 베이스상태) -> (다음 타자순서, 득점)
memo = {}

def simulate_inning(inning, start_batter, lineup):
    """한 이닝 시뮬레이션 with 메모이제이션"""
    key = (inning, start_batter, tuple(lineup))
    if key in memo:
        return memo[key]
    
    outs = bases = score = 0
    batter_idx = start_batter
    
    while outs < 3:
        player = lineup[batter_idx]
        hit = scores[inning][player]
        
        if hit == 0:
            outs += 1
        elif hit == 1:
            score += bases >> 2
            bases = ((bases << 1) | 1) & 7
        elif hit == 2:
            score += (bases >> 1 & 1) + (bases >> 2)
            bases = ((bases << 2) | 2) & 7
        elif hit == 3:
            score += (bases & 1) + (bases >> 1 & 1) + (bases >> 2)
            bases = 4
        else:
            score += (bases & 1) + (bases >> 1 & 1) + (bases >> 2) + 1
            bases = 0
        
        batter_idx = (batter_idx + 1) % 9
    
    result = (batter_idx, score)
    memo[key] = result
    return result

max_score = 0

for perm in permutations(range(1, 9), 8):
    lineup = list(perm[:3]) + [0] + list(perm[3:])
    
    total_score = 0
    batter_idx = 0
    
    for inning in range(N):
        batter_idx, inning_score = simulate_inning(inning, batter_idx, tuple(lineup))
        total_score += inning_score
    
    max_score = max(max_score, total_score)

print(max_score)