A = [
        [1,2,3], 
        [4,5,6]
    ]

N = len(A)
M = len(A[0])

def print_matrix(matrix):
    for row in matrix:
        print(f"{row}")
    print()

print(f"===== original matrix =====")
print_matrix(A)


print(f"===== 90 rotation matrix =====")
r90 = [[0]*N for _ in range(M)]
for i in range(M):
    for j in range(N):
        r90[i][j] = A[N-1-j][i]
print_matrix(r90)
print("")


print(f"===== 180 rotation matrix =====")
r180 = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        r180[i][j] = A[N-1-i][M-1-j]
print_matrix(r180)
print("")


print(f"===== 270, -90 rotation matrix ===== ")
r270 = [[0]*N for _ in range(M)]
for i in range(M):
    for j in range(N):
        r270[i][j] = A[j][M-1-i]
print_matrix(r270)
print("")

