def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i, curr_price in enumerate(prices):
        while stack and prices[stack[-1]] > curr_price: ## 현재 가격이 더 낮은 케이스 발견
            prev_idx = stack.pop()
            answer[prev_idx] = i - prev_idx
        stack.append(i)
    
    while stack:
        prev_idx = stack.pop()
        answer[prev_idx] = len(prices) - 1 - prev_idx
        
    return answer