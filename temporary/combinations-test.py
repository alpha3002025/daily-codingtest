from itertools import combinations, permutations, product

str = "abc"
comb = combinations(str, 2)
for combination in comb:
    print(combination)

"""
('a', 'b')
('a', 'c')
('b', 'c')
"""