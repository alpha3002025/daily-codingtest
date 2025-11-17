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

start = (0,0)
end = (R-1, C-1)

def rotate_matrix(m1, start, end):
    for c in range(start[1], end[1]+1):
        m1_rotated[0][c] = m1[0][c-1]

    for r in range(start[0]+1, end[0]+1):
        m1_rotated[r][end[1]] = m1[r-1][end[1]]

    for c in range(end[1]-1, start[1]-1, -1):
        m1_rotated[end[0]][c] = m1[end[0]][c+1]

    for r in range(end[0]-1, start[0]-1, -1):
        m1_rotated[r][0] = m1[r+1][0]
    
    return m1_rotated

rotated = rotate_matrix(m1, (0,0), (R-1,C-1))
print("rotated >> ")
for row in rotated:
    print(row)