import re
from itertools import permutations

def solution(expression):
    answer = 0
    
    refined = re.split(r"([^0-9])", expression)
    operands = list(map(int, refined[::2]))
    operators = refined[1::2]
    
    max_result = -float('inf')
    
    for reorganized in permutations(['+','-','*'], 3):
        operands_copy = operands[:]
        operators_copy = operators[:]
        
        for curr_op in reorganized:
            idx = 0
            while idx < len(operators_copy):
                if operators_copy[idx] == curr_op:
                    value1 = operands_copy[idx]
                    value2 = operands_copy[idx+1]
                    curr = 0
                    
                    if curr_op == '+': curr = value1 + value2
                    elif curr_op == '-': curr = value1 - value2
                    elif curr_op == '*': curr = value1 * value2
                    
                    operands_copy[idx] = curr
                    del operands_copy[idx+1]
                    del operators_copy[idx]
                else:
                    idx += 1
        
        max_result = max(max_result, abs(operands_copy[0]))
        
    return max_result