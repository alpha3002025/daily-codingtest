def solution(elements):
    duplicated = elements + elements
    occurence = set()
    
    for i in range(len(elements)):
        curr_sum = 0
        for sub_length in range(len(elements)):
            curr_sum += duplicated[i+sub_length]
            occurence.add(curr_sum)
    
    return len(occurence)

print(solution([7,9,1,1,4]))