#그리디 
def solution(picks, minerals):
    total_picks = sum(picks)
    if total_picks == 0:
        return 0
    
    minerals = minerals[:total_picks*5] ## 곡괭이 총 갯수 x 5 (광물 5개)
    
    chunks = []
    for i in range(0, len(minerals), 5):
        mines = minerals[i:i+5]
        cost = 0
        for mine in mines: ## 돌곡괭이 기준 cost 산정
            if mine == 'diamond':
                cost += 25
            elif mine == 'iron':
                cost += 5
            else:
                cost += 1
        chunks.append((cost, mines))
    
    chunks.sort(key=lambda x:x[0], reverse=True)
    
    answer = 0
    for cost, mines in chunks:
        if picks[0] > 0: ## 다이아몬드 곡괭이 있으면 먼저 소모
            pick_type = 0
            picks[0] -= 1
        elif picks[1] > 0: ## 그 다음 편한 도구인 iron 곡괭이 소모
            pick_type = 1
            picks[1] -= 1
        elif picks[2] > 0: ## 돌곡괭이
            pick_type = 2
            picks[2] -= 1
        else:
            break
        
        for mine in mines:
            if pick_type == 0:
                answer += 1
            elif pick_type == 1:
                if mine == 'diamond': ## 철 곡괭이로 다이아 : 5
                    answer += 5
                else: 
                    answer += 1 # 철 곡괭이로 철,돌 : 1
            elif pick_type == 2:
                if mine == 'diamond': ## 돌 곡괭이로 다이아 : 25
                    answer += 25
                elif mine == 'iron':
                    answer += 5
                else:
                    answer += 1
    return answer