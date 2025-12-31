from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    discounts = [10,20,30,40]
    
    for discount_combo in product(discounts, repeat=len(emoticons)):
        plus = 0
        total = 0
        
        for user_min_discount, user_limit in users:
            # 각 사용자의 구매 금액 계산
            revenue = sum(
                emoticons[i] * (100 - discount) // 100
                for i, discount in enumerate(discount_combo)
                if discount >= user_min_discount
            )
            
            # 플러스 가입 or 일반 구매
            if revenue >= user_limit:
                plus += 1
            else:
                total += revenue
        
        # 최적 결과 갱신
        if plus > answer[0] or (plus == answer[0] and total > answer[1]):
            answer = [plus, total]
    
    return answer

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))