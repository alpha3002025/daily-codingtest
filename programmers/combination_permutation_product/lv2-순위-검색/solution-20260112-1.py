from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    answer = []
    score_data = defaultdict(list)
    
    for s in info:
        args = s.split()
        score = int(args[-1])
        conditions = args[:-1]
        
        for window_size in range(5):
            for dash_comb in combinations(range(4), window_size):
                conditions_copy = conditions[:]
                
                for idx in dash_comb:
                    conditions_copy[idx] = '-'
                
                key = "".join(conditions_copy)
                score_data[key].append(score)
    
    for key in score_data.keys():
        score_data[key].sort()
        
    for s in query:
        args = s.replace(" and ", "").split()
        key = args[0]
        score = int(args[-1])
        pos = bisect_left(score_data[key], score)
        answer.append(len(score_data[key]) - pos)
        
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))