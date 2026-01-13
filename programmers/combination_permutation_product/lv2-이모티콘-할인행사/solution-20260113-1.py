from itertools import product

def solution(users, emoticons):
    answer = []
    discounts = [10,20,30,40]
    
    optimal_subscriber_cnt, optimal_sales = 0, 0
    for discount_combo in product(discounts, repeat=len(emoticons)):
        plus = 0
        total_sales = 0
        
        for user_discount, user_price_limit in users:
            user_total_sales = 0
            for i, discount_rate in enumerate(discount_combo):
                emoticon_price = emoticons[i]
                discounted_price = (100 - discount_rate) * emoticon_price // 100
                
                if discount_rate >= user_discount:
                    user_total_sales += discounted_price
            
            if user_total_sales >= user_price_limit:
                plus += 1
            else:
                total_sales += user_total_sales
        
        if plus > optimal_subscriber_cnt:
            optimal_subscriber_cnt = plus
            optimal_sales = total_sales
        elif plus == optimal_subscriber_cnt:
            optimal_sales = max(optimal_sales, total_sales)
        
    return [optimal_subscriber_cnt, optimal_sales]