def solution(num, total):
    maybe = total // num
    
    for i in range(num):
        start = maybe - i
        end = maybe - i + num
        
        curr = sum(range(start, end))
        if curr == total:
            return list(range(start,end))
    
    answer = []
    return answer