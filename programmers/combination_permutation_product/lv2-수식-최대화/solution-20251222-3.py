import re
from itertools import permutations

def solution(expression):
    all = re.split(r'([^0-9])', expression)
    operands = list(map(int, all[0::2]))
    operators = all[1::2]
    max_value = -float('inf')
    
    for prior_perm in permutations(['*', '+', '-']):
        operators_copy = operators[:]
        operands_copy = operands[:]
        
        for curr_op in prior_perm:
            operator_idx = 0
            
            while operator_idx < len(operators_copy):
                if operators_copy[operator_idx] == curr_op: ## 복사한 연산자 배열에서 curr_op 의 위치를 찾는다.
                    v1 = operands_copy[operator_idx]
                    v2 = operands_copy[operator_idx+1]

                    if curr_op == '+': res = v1 + v2
                    elif curr_op == '-': res = v1 - v2
                    elif curr_op == '*': res = v1 * v2
                    
                    operands_copy[operator_idx] = res
                    del operands_copy[operator_idx+1]
                    del operators_copy[operator_idx]
                else:
                    operator_idx += 1
        max_value = max(max_value, abs(operands_copy[0]))
    return max_value


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
