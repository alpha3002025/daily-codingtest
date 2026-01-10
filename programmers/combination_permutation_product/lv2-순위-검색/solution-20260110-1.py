from itertools import combinations
from collections import defaultdict
from bisect import bisect_left


def solution(info, query):    
    score_data = defaultdict(list)
    
    for data in info:
        args = data.split()
        score = int(args[-1])
        conditions = args[:-1]
        
        for window_size in range(5):
            for curr_comb in combinations(range(4), window_size): # ['cpp', 'java', 'python', '-']
                condition_copy = conditions[:]
                
                for index in curr_comb:
                    condition_copy[index] = '-'
                
                key = "".join(condition_copy)
                score_data[key].append(score)
    
    
    for key in score_data.keys():
        score_data[key].sort()
        
    answer = []
    
    for condition in query:
        args = condition.replace(" and ", "").split()
        key = args[0]
        score = int(args[1])
        
        scores = score_data[key]
        pos = bisect_left(scores, score)
        answer.append(len(scores) - pos)
    
    return answer