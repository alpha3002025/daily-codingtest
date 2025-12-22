from collections import Counter

def solution(weights):
    counter = Counter(weights)
    
    answer = 0
    ## 1:1
    for number, count in counter.items():
        if number > 1:
            answer += count*(count-1)//2
    
    for number, count in counter.items():
        ## 1:2
        if number * 2 in counter:
            answer += counter[number] * counter[number*2]
        
        ## 2:3
        #### 2의 배수이면서 3k 에 해당하는 수가 counter 에 있다면
        if number % 2 == 0 and (number * 3 // 2) in counter:
            answer += counter[number] * counter[number * 3 // 2]
        
        ## 3:4
        if number % 3 == 0 and (number * 4 // 3) in counter:
            answer += counter[number] * counter[number * 4 // 3]
    
    
    return answer