import re
from itertools import permutations

def solution(expression):
    refined = re.split(r"([^0-9])", expression)
    operands = list(map(int, refined[::2]))
    operators = refined[1::2]
    max_value = -float('inf')
    
    ## (참고)
    # for curr_perm in permutations(operators): ## 이렇게 할 경우에는 에러가 난다. 조심!!
    
    ## 연산자 우선순위의 순열 
    for curr_perm in permutations(['+', '-', '*']):
        operators_copy = operators[:]
        operands_copy = operands[:]
        
        for curr_op in curr_perm:
            operator_idx = 0
            
            ## 복사한 연산자 배열에서 curr_op 의 위치를 찾는다.
            while operator_idx < len(operators_copy):
                
                ### 해당 연산자 위치에 도달
                if operators_copy[operator_idx] == curr_op: 
                    v1 = operands_copy[operator_idx]
                    v2 = operands_copy[operator_idx+1]
                    
                    if curr_op == '+': res = v1 + v2
                    elif curr_op == '-': res = v1 - v2
                    elif curr_op == '*': res = v1 * v2
                    
                    operands_copy[operator_idx] = res
                    del operands_copy[operator_idx+1]
                    del operators_copy[operator_idx]
                
                ### 해당 연산자를 찾을때까지 operator += 1
                else:
                    operator_idx += 1
        
        max_value = max(max_value, abs(operands_copy[0]))
    return max_value