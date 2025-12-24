def solution(storey):
    
    answer = 0
    while storey > 0:
        lsb = storey % 10
        
        if lsb > 5:
            storey += 10
            answer += (10-lsb)
            
        elif lsb == 5:
            next_lsb = (storey // 10) % 10
            answer += 5
            if next_lsb >= 5:
                storey += 10
            
        else: ## lsb < 5
            answer += lsb
    
        storey //= 10
    return answer

print(solution(16))
print(solution(2554))