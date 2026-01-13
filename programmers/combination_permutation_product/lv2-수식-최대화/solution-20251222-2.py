import re
from itertools import permutations

def solution(expression):
    tokens = re.split(r'([^0-9])', expression)
    
    operands = list(map(int, tokens[0::2]))
    operators = tokens[1::2]
    
    max_value = 0
    
    for prior_perm in permutations(['+', '-', '*']):
        operands_copy = operands[:]
        operators_copy = operators[:]
        
        for op in prior_perm:
            idx = 0
            while idx < len(operators_copy):
                if operators_copy[idx] == op:
                    v1,v2 = operands_copy[idx], operands_copy[idx+1]
                    
                    if op == "+": res = v1 + v2
                    elif op == "-": res = v1 - v2
                    elif op == "*": res = v1 * v2
                    
                    operands_copy[idx] = res
                    del operands_copy[idx+1]
                    
                    del operators_copy[idx]
                else:
                    idx += 1
                    
        max_value = max(max_value, abs(operands_copy[0]))
    return max_value


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
