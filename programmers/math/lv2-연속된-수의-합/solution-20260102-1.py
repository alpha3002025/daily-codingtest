def solution(num, total):
    sum_of_diff = (num * (num - 1))//2
    
    start = (total - sum_of_diff) // num
    
    return list(range(start, start+num))