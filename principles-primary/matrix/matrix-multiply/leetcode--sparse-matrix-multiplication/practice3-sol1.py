from typing import List

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        N = len(mat1)
        T = len(mat1[0])
        M = len(mat2[0])

        result = [[0]*M for _ in range(N)]

        for i in range(N):
            for j in range(M):
                for k in range(T):
                    result[i][j] += mat1[i][k] * mat2[k][j]
        
        return result