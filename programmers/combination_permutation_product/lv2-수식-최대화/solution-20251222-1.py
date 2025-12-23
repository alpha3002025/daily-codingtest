import re
from itertools import permutations

def solution(expression):
    # 숫자와 연산자 분리
    # 정규식 '([^0-9])' : 숫자가 아닌 문자를 그룹으로 잡아 분리
    tokens = re.split(r'([^0-9])', expression)
    # -> ['100', '-', '200', '*', '300']
    
    operands = list(map(int, tokens[0::2])) # 짝수 인덱스는 숫자
    operators = tokens[1::2]                # 홀수 인덱스는 연산자
    
    max_value = 0
    
    # 3가지 연산자의 모든 우선순위 순열
    for prior in permutations(['+', '-', '*']):
        # 리스트 복사
        tmp_operands = operands[:]
        tmp_operators = operators[:]
        
        for op in prior:
            # 현재 우선순위인 op 연산자를 모두 처리
            idx = 0
            while idx < len(tmp_operators):
                if tmp_operators[idx] == op:
                    val1 = tmp_operands[idx]
                    val2 = tmp_operands[idx+1]
                    
                    if op == '+': res = val1 + val2
                    elif op == '-': res = val1 - val2
                    elif op == '*': res = val1 * val2
                    
                    # 계산 결과로 대체 (두 숫자를 없애고 하나 넣기)
                    tmp_operands[idx] = res
                    del tmp_operands[idx+1]
                    
                    # 사용한 연산자 제거
                    del tmp_operators[idx]
                    
                    # idx를 증가시키지 않음 (다음 연산자가 당겨져 왔으므로 확인 필요)
                else:
                    idx += 1
                    
        max_value = max(max_value, abs(tmp_operands[0]))
        
    return max_value