def solution(elements):
    n = len(elements)
    extended_elements = elements * 2
    sums = set()
    
    for i in range(n):
        current_sum = 0
        for length in range(n):
            current_sum += extended_elements[i+length]
            sums.add(current_sum)
    
    return len(sums)

print(solution([7,9,1,1,4]))