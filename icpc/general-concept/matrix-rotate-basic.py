## 참고 : 17406 배열돌리기 4

from copy import deepcopy

m1 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]

m1_rotated = deepcopy(m1)
print("original>")
for row in m1:
    print(f"{row}")

R = len(m1)
C = len(m1[0])

## 위
# m1_rotated[0][0] = m1[1][0] (아래 -> 위에서 복사되므로 이 부분은 필요x)
for c in range(1, C):
    m1_rotated[0][c] = m1[0][c-1]

for r in range(1, R):
    m1_rotated[r][C-1] = m1[r-1][C-1]

for c in range(C-1-1, -1, -1):
    m1_rotated[R-1][c] = m1[R-1][c+1]

for r in range(R-1-1, -1, -1):
    m1_rotated[r][0] = m1[r+1][0]


print()
print("rotated>")
for row in m1_rotated:
    print(f"{row}")