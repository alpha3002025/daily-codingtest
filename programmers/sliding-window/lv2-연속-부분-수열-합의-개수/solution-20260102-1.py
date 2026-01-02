def solution(elements):
    duplicated = elements + elements
    sum_set = set()
    
    for i in range(len(elements)):
        curr_sum = 0
        for ii in range(len(elements)):
            curr_sum += duplicated[i + ii]
            sum_set.add(curr_sum)
    
    return len(sum_set)

print(solution([7,9,1,1,4]))