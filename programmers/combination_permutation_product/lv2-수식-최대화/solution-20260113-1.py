import re
from itertools import permutations

def solution(expression):
    refined = re.split(r"([^0-9])", expression)
    
    operands = list(map(int, refined[::2]))
    operators = refined[1::2]
    
    max_result = -float('inf')
    for reorganized in permutations(["+", "-", "*"], 3):
        operators_copy = operators[:]
        operands_copy = operands[:]
        
        for curr_op in reorganized:
            idx = 0
            
            while idx < len(operators_copy):
                if operators_copy[idx] != curr_op:
                    idx += 1
                    
                else: ## operators[idx] == curr_op
                    v1 = operands_copy[idx]
                    v2 = operands_copy[idx+1]
                    
                    curr = 0
                    if curr_op == '+': curr = v1 + v2
                    elif curr_op == '-': curr = v1 - v2
                    elif curr_op == '*': curr = v1 * v2
                    
                    operands_copy[idx] = curr
                    del operands_copy[idx+1]
                    del operators_copy[idx]
        
        max_result = max(max_result, abs(operands_copy[0]))
    
    return max_result


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
