def solution(storey):
    answer = 0
    
    while storey > 0:
        lsb = storey % 10
        next_lsb = (storey // 10) % 10
        
        if lsb > 5:
            answer += (10 - lsb) 
            storey+= 10
        elif lsb == 5:
            answer += 5 ## 1 을 5 만큼
            if next_lsb >= 5: ## 그 다음 자릿수가 반올림에 해당될 경우에만 10+
                storey += 10
        else:
            answer += lsb ## 1 을 lsb 만큼
            
        storey //= 10
    return answer