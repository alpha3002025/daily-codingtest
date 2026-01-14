from collections import Counter

def solution(topping):
    left = set()
    right = Counter(topping)
    
    len_right = len(right)
    kind = 0
    
    for curr_topping in topping:
        left.add(curr_topping)
        right[curr_topping] -= 1
        
        ## 만약 현재 curr_topping 이 오른쪽 집합에서 완전히 제거되었다면
        if right[curr_topping] == 0:
            ## right 의 종류수 -= 1
            len_right -= 1
            
        if len(left) == len_right:
            # print(f"left = {left}, right = {right}")
            kind += 1
    
    return kind


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
print(solution([1, 2, 3, 1, 4]))