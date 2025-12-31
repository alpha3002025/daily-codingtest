from collections import defaultdict

def solution(clothes):
    table = defaultdict(list)
    
    for cloth_name, cloth_kind in clothes:
        table[cloth_kind].append(cloth_name)
    
    answer = 1
    for cloth_kind in table.keys():
        answer *= len(table[cloth_kind]) + 1
    
    return answer - 1