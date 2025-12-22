from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    answer = []
    score_data = defaultdict(list)
    
    for data in info:
        args = data.split()
        conditions = args[:-1]
        score = int(args[-1])
        
        for comb_size in range(5):
            comb = combinations(range(4), comb_size) ## idx 의 조합
            
            for idx_combination in comb:
                condition_copy = conditions[:]
            
                for idx in idx_combination:
                    condition_copy[idx] = '-'
                    
                key = "".join(condition_copy)
                score_data[key].append(score)
    
    for row in score_data:
        score_data[row].sort()
    
    for q in query:
        args = q.replace(" and ", "").split()
        condition = "".join(args[:-1])
        score = int(args[-1])
        pos = bisect_left(score_data[condition], score)
        """
        t = 3       *
        A = [ 1, 2, 3, 4, 5, 6]
              0  1  2  3  4  5
              
              idx = 2, 3 이상 받은 사람 : len(A) - (i(=2)) ('이상'이 조건이므로)
        """
        answer.append(len(score_data[condition]) - pos)

    return answer