def solution(people, limit):
    sorted_people = sorted(people)
    left, right = 0, len(people)-1
    
    boat_cnt = 0
    while left <= right:
        if sorted_people[left] + sorted_people[right] <= limit:
            left += 1
        right -= 1
        boat_cnt += 1
    
    return boat_cnt


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))