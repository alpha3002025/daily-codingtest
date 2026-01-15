def solution(people, limit):
    sorted_people = sorted(people)
    left, right = 0, len(people)-1
    
    boat_cnt = 0
    while left <= right:
        if sorted_people[left] + sorted_people[right] <= limit:
            ## 용량 한도 내에서 가벼운 친구를 우겨넣을수 있다면 우겨넣는다.
            left += 1
        
        right -= 1 ## 매 순간 제일 무거운 사람은 무조건 태운다.
        boat_cnt += 1
    
    return boat_cnt