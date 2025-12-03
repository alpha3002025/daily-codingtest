from itertools import permutations

# 숫자의 개수
N = int(input())

# 주어진 수열
numbers = list(map(int, input().split()))

# 덧셈, 뺄셈, 곱셈, 나눗셈 연산자의 개수
add, sub, mul, div = map(int, input().split())

operators = []
operators.extend(['+']*add)
operators.extend(['-']*sub)
operators.extend(['*']*mul)
operators.extend(['/']*div)

max_sum = float('-inf')
min_sum = float('inf')

# print(f"operators = {operators}")
# print(f"permutations = {list(permutations(operators))}")
# perm = set(permutations(operators))
# print(f"perm = {perm}")

perms = list(permutations(operators))
for perm in perms:
    result = numbers[0] ## (1)

    for i in range(N-1): ## 0 ~ N-2 (연산자의 갯수는 1개 더 적으므로 N-2)
        curr_operator = perm[i]
        if curr_operator == '+':
            result += numbers[i+1] ## (1)에서 구한값 + next 요소 
                                   ## (이렇게 하는 이유는 연산자의 개수가 1개 더 적기에 for loop index를 맞추기 위함)
        if curr_operator == '-':
            result -= numbers[i+1] ## (1)에서 구한값 - next 요소 
                                   ## (이렇게 하는 이유는 연산자의 개수가 1개 더 적기에 for loop index를 맞추기 위함)
        if curr_operator == '*':
            result *= numbers[i+1]
        
        if curr_operator == '/':
            if result < 0:
                result = -(-result // numbers[i+1])
            else:
                result //= numbers[i+1]
    
    max_sum = max(max_sum, result)
    min_sum = min(min_sum, result)

print(max_sum)
print(min_sum)