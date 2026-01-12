from itertools import product

def solution(users, emoticons):
    answer = [0,0]
    discounts = [10,20,30,40]
    
    for discount_combo in product(discounts, repeat = len(emoticons)):
        plus = 0
        total = 0
        
        for user_min_discount, user_limit in users:
            revenue = sum(
                emoticons[i] * (100 - discount) // 100
                for i, discount in enumerate(discount_combo)
                if discount >= user_min_discount
            )
            
            if revenue >= user_limit:
                plus += 1
            else:
                total += revenue
        
        if plus > answer[0] or (plus == answer[0] and total > answer[1]):
            answer = [plus, total]
    
    return answer