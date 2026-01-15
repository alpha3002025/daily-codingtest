def solution(picks, minerals):
    ## 전체 곡괭이의 수
    total_picks = sum(picks)
    if total_picks == 0:
        return 0
    
    ## 곡괭이 총 갯수 x 5 (곡괭이별 5회)
    minerals = minerals[:total_picks * 5]
    
    ## 돌곡괭이 기준으로 피로도(비용) 산정
    chunks = []
    for i in range(0, len(minerals), 5):
        sub_minerals = minerals[i:i+5]
        cost = 0
        
        for mineral in sub_minerals:
            if mineral == 'diamond':
                cost += 25
            elif mineral == 'iron':
                cost += 5
            else:
                cost += 1
        chunks.append((cost, sub_minerals))
    
    ## 피로도가 가장 높은 순으로 정렬
    chunks.sort(key=lambda x:x[0], reverse=True)
    
    total_cost = 0
    ## 다이아곡괭이 먼저 소모(피로도가 높은 순으로 정렬했으므로)
    for cost, sub_minerals in chunks:
        if picks[0] > 0: ## 다이아 곡괭이 사용, 피로도 1 감소
            pick_type = 0 ## 다이아 곡괭이 선택
            picks[0] -= 1
        elif picks[1] > 0:
            pick_type = 1
            picks[1] -= 1
        elif picks[2] > 0:
            pick_type = 2
            picks[2] -= 1
        else:
            break
            
        for mineral in sub_minerals:
            ## 다이아몬드 곡괭이는 어떤 광물이든 cost=1 소모
            if pick_type == 0:
                total_cost += 1
            
            ## 철 곡괭이는 다이아몬드는 cost=5 소모, 그 외에 cost=1
            elif pick_type == 1: 
                if mineral == 'diamond':
                    total_cost += 5 ## 철 곡괭이로 다이아몬드
                else:
                    total_cost += 1 ## 철 곡괭이로 철, 돌
            
            ## 돌 곡괭이는 다이아몬드는 cost=25, 철은 cost=5, 돌은 cost=1
            elif pick_type == 2:
                if mineral == 'diamond':
                    total_cost += 25
                elif mineral == 'iron':
                    total_cost += 5
                else:
                    total_cost += 1
                    
    return total_cost