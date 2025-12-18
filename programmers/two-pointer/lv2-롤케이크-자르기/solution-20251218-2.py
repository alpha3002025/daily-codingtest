"""
del counter[key] 를 사용하는 케이스
"""
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
            # len_right -= 1
            del right[curr_topping]
            
        # if len(left) == len_right:
        if len(left) == len(right): ## 이렇게 안하는 이유는 right[x] == 0 인 케이스도 계속 남아있기 때문
            # print(f"left = {left}, right = {right}")
            kind += 1
    
    return kind