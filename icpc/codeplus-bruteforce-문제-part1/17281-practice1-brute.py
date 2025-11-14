import sys
from itertools import permutations


N = int(input())
scores = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
players = [i for i in range(1, 9)] ## 1,2,3,4,5,6,7,8
result = float('-inf')
for p in permutations(players, 8):
    p = list(p)
    # print(f"p = {p}")
    game_players = p[:3] + [0] + p[3:]
    # print(f"game_players = {game_players}")

    for ining in range(N):
        out = 0
        p1,p2,p3 = 0,0,0
        current_scores = scores[ining]
        current_score = 0

        player_number = 0
        while out < 3:
            if current_scores[player_number] == 0:
                out+=1
            elif current_scores[player_number] == 1:
                current_score+=1
                p1,p2,p3 = 1,p1,p2
            elif current_scores[player_number] == 2:
                current_score+= p2+p3
                p1,p2,p3 = 0,1,p1
            elif current_scores[player_number] == 3:
                current_score+= p1+p2+p3
                p1,p2,p3 = 0,0,1
            elif current_scores[player_number] == 4:
                current_score+= p1+p2+p3+1
                p1,p2,p3 = 0,0,0

            player_number+=1
            if player_number == 9:
                player_number = 0
    
    result = max(result,current_score)
print(f"{current_score}")
