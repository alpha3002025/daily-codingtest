def solution(picks, minerals):
    ## 곡괭이 총 개수
    total_cnt = sum(picks)
    ## 캘수 있는 만큼만 슬라이싱
    minerals = minerals[:total_cnt * 5]
    
    chunks = []
    for i in range(0, len(minerals), 5):
        curr_window = minerals[i:i+5]
        curr_window_cost = 0
        
        for mineral in curr_window:
            if mineral == 'diamond':
                curr_window_cost += 25
            elif mineral == 'iron':
                curr_window_cost += 5
            else:
                curr_window_cost += 1
        chunks.append((curr_window_cost, curr_window))
    
    chunks.sort(key=lambda x:x[0], reverse = True)
    
    total_cost = 0
    
    for curr_cost, curr_window in chunks:
        curr_pick = 0
        if picks[0] > 0:
            curr_pick = 0
            picks[0] -= 1
        elif picks[1] > 0:
            curr_pick = 1
            picks[1] -= 1
        elif picks[2] > 0:
            curr_pick = 2
            picks[2] -= 1
                
        for mineral in curr_window:
            if curr_pick == 0:
                total_cost += 1
            elif curr_pick == 1:
                if mineral == 'diamond':
                    total_cost += 5
                else:
                    total_cost += 1
            else:
                if mineral == 'diamond':
                    total_cost += 25
                elif mineral == 'iron':
                    total_cost += 5
                else:
                    total_cost += 1
    
    return total_cost