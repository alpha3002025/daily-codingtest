from collections import Counter

def solution(topping):
    answer = 0
    left = set()
    right = Counter(topping)
    
    for item in topping:
        left.add(item)
        right[item] -= 1
        
        if right[item] == 0:
            del right[item]
        
        if len(left) == len(right):
            answer += 1
    
    return answer


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
print(solution([1, 2, 3, 1, 4]))