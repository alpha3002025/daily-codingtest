def solution(elements):
    double_elements = elements + elements
    sum_occurrence = set()
    
    for i in range(len(elements)):
        base = 0
        for distance in range(len(elements)):
            base += double_elements[i+distance]
            sum_occurrence.add(base)
    
    return len(sum_occurrence)

print(solution([7,9,1,1,4]))