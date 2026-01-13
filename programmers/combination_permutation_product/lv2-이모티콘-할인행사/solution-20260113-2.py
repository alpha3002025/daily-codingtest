from itertools import product

def solution(users, emoticons):
    answer = []
    discount_rates = [10,20,30,40]
    
    optimal_plus_cnt = 0
    optimal_sales = 0
    
    for discount_combo in product(discount_rates, repeat=len(emoticons)):
        total_purchase = 0
        plus_cnt = 0
        
        for user_discount_want, user_price_limit in users:
            user_purchase = 0
            for i, discount in enumerate(discount_combo):
                discount_price = (100 - discount) * emoticons[i] // 100
                
                if user_discount_want <= discount:
                    user_purchase += discount_price
            
            if user_price_limit <= user_purchase:
                plus_cnt += 1
            else:
                total_purchase += user_purchase
        
        if optimal_plus_cnt < plus_cnt:
            optimal_plus_cnt = plus_cnt
            optimal_sales = total_purchase
        elif optimal_plus_cnt == plus_cnt:
            optimal_sales = max(optimal_sales, total_purchase)
    
    return [optimal_plus_cnt, optimal_sales]