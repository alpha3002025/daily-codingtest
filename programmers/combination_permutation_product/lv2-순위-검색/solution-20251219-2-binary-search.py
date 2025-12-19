from bisect import bisect_left
from itertools import combinations
from collections import defaultdict

def solution(info, query):
    answer = []
    results = defaultdict(list)
    
    for data in info:
        args = data.split()
        conditions = args[:-1]
        score = int(args[-1])
        
        ## 4가지 조건 중 '-'가 포함되는 케이스의 조합 생성
        ## e.g. java backend junior pizza ➝ java - junior pizza ➝ - - - -
        for curr_len in range(5):
            for c in combinations(range(4), curr_len): 
                    ## '-' 는 4개까지만 가능하다. 
                    ## score 는 '-'가 올수 없는 것이 문제의 조건이기 때문
                key_list = conditions[:]
                
                ## 0 일때에는 for loop 이 수행되지 않으므로 조건 문자열 그대로 유지 가능
                for idx in c:
                    key_list[idx] = '-' ## 선택된 인덱스의 위치를 '-'로 변경
                                        
                
                key = "".join(key_list)
                results[key].append(score)
                
    for key in results:
        results[key].sort() ## 해당 조건내의 점수들을 점수 순 오름차순 정렬
    
    for q in query:
        lang,job,level,food,score = q.replace('and', '').split()
        key = lang+job+level+food
        scores = results[key]
        idx = bisect_left(scores, int(score))
        
        answer.append(len(scores) - idx)
    
    return answer