from collections import defaultdict
def solution(clothes):
    PRODUCT, KIND = (0,1)
    table = defaultdict(list)

    for c in clothes:
        table[c[KIND]].append(c[PRODUCT])

    answer = 1
    for kind, value in table.items():
        answer *= (len(table[kind])+1)

    return answer-1