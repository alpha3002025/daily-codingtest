def solution(elements):
    elem2 = elements + elements
    sum_occurrence = set()
    
    for i in range(len(elements)):
        curr_sum = 0
        for j in range(len(elements)):
            curr_sum += elem2[i + j]
            sum_occurrence.add(curr_sum)
    
    return len(sum_occurrence)


print(solution([1, 2, 3, 4, 5], 7))
print(solution([1, 1, 1, 2, 3, 4, 5], 5))
print(solution([2, 2, 2, 2, 2], 6))