from itertools import permutations

str = "abc"

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