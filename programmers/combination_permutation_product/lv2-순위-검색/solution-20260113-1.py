from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    answer = []
    
    score_db = defaultdict(list)
    
    for condition in info:
        args = condition.split()
        key_list = args[:-1]
        score = int(args[-1])
        
        for window_size in range(0, 5):
            for idx_comb in combinations(range(len(key_list)), window_size):
                key_list_copy = key_list[:]
                
                for idx in idx_comb:
                    key_list_copy[idx] = '-'
                
                key = "".join(key_list_copy)
                score_db[key].append(score)
        
        
    for key in score_db.keys():
        score_db[key].sort()
    
    for condition in query:
        args = condition.replace(" and ", " ").split()
        key = "".join(args[:-1])
        score = int(args[-1])
        scores = score_db[key]
        """
        [0,1,2,3,4]
             *
        """
        # print(f"key = {key}, score = {score}, scores = {scores}")
        ge_scorers_cnt =  len(scores) - bisect_left(scores, score)
        answer.append(ge_scorers_cnt)
    
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))