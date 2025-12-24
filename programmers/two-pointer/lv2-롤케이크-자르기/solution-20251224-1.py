from collections import Counter

def solution(topping):
    left = set()
    right = Counter(topping)
    
    cnt = 0
    for current_topping in topping:
        left.add(current_topping)
        right[current_topping] -= 1
        
        if right[current_topping] == 0:
            del right[current_topping]
        
        if len(left) == len(right):
            cnt += 1
    
    return cnt