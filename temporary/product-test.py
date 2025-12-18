from itertools import product

str = "abc"

for p in product(str, repeat=2):
    print(p)

"""
('a', 'a')
('a', 'b')
('a', 'c')
('b', 'a')
('b', 'b')
('b', 'c')
('c', 'a')
('c', 'b')
('c', 'c')
"""

print(">>>>>>>")
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