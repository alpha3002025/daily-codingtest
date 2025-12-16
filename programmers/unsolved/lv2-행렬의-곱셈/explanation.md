# 행렬의 곱셈

## 문제 설명
2차원 행렬 `arr1`과 `arr2`를 곱한 결과를 반환하세요.
행렬 곱셈 조건: A ($M \times K$) $\times$ B ($K \times N$) = C ($M \times N$).

### 핵심 개념
1.  **행렬 곱셈 공식**:
    - 결과 행렬 `C[i][j]`는 `arr1`의 `i`행 벡터와 `arr2`의 `j`열 벡터의 내적(Dot Product)입니다.
    - $C_{ij} = \sum_{k} (A_{ik} \times B_{kj})$
2.  **3중 반복문**: $O(M \times N \times K)$ 복잡도.

## Python 풀이

```python
def solution(arr1, arr2):
    row1 = len(arr1)
    col1 = len(arr1[0]) # = row2
    col2 = len(arr2[0])
    
    # 결과 행렬 초기화 (M x N)
    answer = [[0] * col2 for _ in range(row1)]
    
    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                answer[i][j] += arr1[i][k] * arr2[k][j]
                
    return answer
```

### Pythonic 풀이 (zip, *)
`zip(*arr2)`를 사용하면 행렬 `arr2`를 전치(Transpose, 행과 열 뒤집기)하여, `j`번째 열을 쉽게 가져올 수 있습니다.

```python
def solution(arr1, arr2):
    # arr2 전치: 열 단위 접근을 행 단위로 바꿈
    # 예: [[1,2], [3,4]] -> [(1,3), (2,4)]
    arr2_T = list(zip(*arr2))
    
    answer = []
    for row in arr1:
        new_row = []
        for col in arr2_T:
            # 내적 계산
            dot_product = sum(a * b for a, b in zip(row, col))
            new_row.append(dot_product)
        answer.append(new_row)
        
    return answer
```
