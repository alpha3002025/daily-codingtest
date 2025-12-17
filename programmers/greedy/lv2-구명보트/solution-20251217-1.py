def solution(people, limit):
    people.sort()
    left,right = 0, len(people)-1
    boats = 0
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left+=1
        right-=1 ## 무거운 사람은 항상 탑승 (혼자든 같이든)
        boats+=1
    
    return boats