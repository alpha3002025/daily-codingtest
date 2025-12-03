from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))
op_counts = list(map(int, input().split()))

# 연산자 리스트 생성
operators = []
operators.extend(['+'] * op_counts[0])
operators.extend(['-'] * op_counts[1])
operators.extend(['*'] * op_counts[2])
operators.extend(['/'] * op_counts[3])

max_value = float('-inf')
min_value = float('inf')

# 모든 연산자 순열 확인 (중복 제거)
for perm in set(permutations(operators)):
    result = numbers[0]
    
    for i in range(n - 1):
        if perm[i] == '+':
            result += numbers[i + 1]
        elif perm[i] == '-':
            result -= numbers[i + 1]
        elif perm[i] == '*':
            result *= numbers[i + 1]
        else:  # perm[i] == '/'
            if result < 0:
                result = -(-result // numbers[i + 1])
            else:
                result = result // numbers[i + 1]
    
    max_value = max(max_value, result)
    min_value = min(min_value, result)

print(max_value)
print(min_value)