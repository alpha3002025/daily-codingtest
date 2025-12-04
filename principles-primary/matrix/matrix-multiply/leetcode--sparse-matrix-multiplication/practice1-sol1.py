"""
참고 : obsidian/개념정리-행렬곱셈
"""


from typing import List

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        M = len(mat1)
        T = len(mat1[0])
        N = len(mat2[0])

        result = [[0]*N for _ in range(M)]

        for i in range(M):
            for j in range(N):
                for k in range(T):
                    result[i][j] += mat1[i][k] * mat2[k][j]
        
        return result