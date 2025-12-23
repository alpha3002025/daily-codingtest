# itertools 모듈의 주요 함수

combination
- 순서고려 x 이면서, 같은 요소를 중복해서 선택x
- 종류를 골라내는 역할


permutation
- 순서고려 o 이면서, 같은 요소를 중복해서 선택x
- 같은 종류의 문자열을 사용해도 순서가 다른 문자열은 다른 문자열로 취급


product
- 순서고려 x 이면서, 같은 요소를 중복해서 선택o



1.  **`combinations(iterable, r)`**: 조합
    -   순서 고려 X (`AB` == `BA`)
    -   중복 허용 X
```python
# "abc" 중 2개 뽑기: ab, ac, bc
str = "abc"
comb = combinations(str, 2)
for combination in comb:
    print(combination)
"""
('a', 'b')
('a', 'c')
('b', 'c')
"""
```

2.  **`permutations(iterable, r)`**: 순열
    -   순서 고려 O (`AB` != `BA`)
    -   중복 허용 X
```python
# "abc" 중 2개 뽑아 나열: ab, ac, ba, bc, ca, cb

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
```
<br/>

3.  **`product(iterable, repeat=r)`**: 중복 순열 (데카르트 곱)
    -   순서 고려 X, 같은 원소 중복 선택 O (`AA`, `AB`...)
    -   `repeat`로 몇 번 뽑을지 지정

```python
# "abc" 중 중복 허용해 2개 뽑기

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
```
