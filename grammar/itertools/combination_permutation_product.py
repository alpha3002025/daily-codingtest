from itertools import combinations, permutations, product 

str = "abc"

print("combinations >>>>>>>")
comb = combinations(str, 2)
for combination in comb:
    print(combination)
"""
('a', 'b')
('a', 'c')
('b', 'c')
"""
print()


print("permutations >>>>>>>")
for p in permutations(str, 2):
    print(p)

"""
('a', 'b')
('a', 'c')
('b', 'a')
('b', 'c')
('c', 'a')
('c', 'b')
"""
print()

print("product >>>>>>>")
for p in product(str, repeat=3):
    print(p)

"""
('a', 'a', 'a')
('a', 'a', 'b')
('a', 'a', 'c')
('a', 'b', 'a')
('a', 'b', 'b')
('a', 'b', 'c')
('a', 'c', 'a')
('a', 'c', 'b')
('a', 'c', 'c')
('b', 'a', 'a')
('b', 'a', 'b')
('b', 'a', 'c')
('b', 'b', 'a')
('b', 'b', 'b')
('b', 'b', 'c')
('b', 'c', 'a')
('b', 'c', 'b')
('b', 'c', 'c')
('c', 'a', 'a')
('c', 'a', 'b')
('c', 'a', 'c')
('c', 'b', 'a')
('c', 'b', 'b')
('c', 'b', 'c')
('c', 'c', 'a')
('c', 'c', 'b')
('c', 'c', 'c')
"""


print("permutation example (2) >>>>>>>")
# 두 번째 인자를 지정하지 않으면 리스트의 모든 요소를 포함하는 순열을 생성합니다.
for curr_perm in permutations(["+", "-", "*"]):
    print(curr_perm)

"""
('+', '-', '*')
('+', '*', '-')
('-', '+', '*')
('-', '*', '+')
('*', '+', '-')
('*', '-', '+')
"""