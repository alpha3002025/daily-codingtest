# 쿼드압축 후 개수 세기

## 문제 설명
0과 1로 이루어진 정사각형(n x n) 이미지를 압축하려고 합니다.
- 전체 영역이 모두 같은 수(0 또는 1)라면 하나로 압축합니다.
- 그렇지 않다면 정확히 4등분하여 각 영역에 대해 같은 과정을 반복합니다. (재귀)
최종적으로 남은 0의 개수와 1의 개수를 반환합니다.

### 핵심 개념
1.  **분할 정복 (Divide and Conquer)**: 문제를 작은 부분 문제(4개의 하위 사각형)로 나누어 해결합니다.
2.  **재귀 (Recursion)**:
    - Base Case 1: 영역의 크기가 1이면 더 이상 나눌 수 없으므로 `answer`에 해당 숫자를 카운트하고 종료.
    - Uniform Check: 현재 영역의 숫자가 모두 같은지 확인. 같다면 카운트하고 종료.
    - Recursive Step: 다르다면 4등분하여 재귀 호출.

## Python 풀이

```python
def solution(arr):
    # [0의 개수, 1의 개수]
    answer = [0, 0]
    
    def compress(x, y, n):
        init_val = arr[x][y]
        
        # 1. 현재 영역이 모두 같은 값인지 확인
        is_uniform = True
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != init_val:
                    is_uniform = False
                    break
            if not is_uniform:
                break
                
        # 2-A. 모두 같다면 해당 값 카운트 증가 후 종료 (압축 성공)
        if is_uniform:
            answer[init_val] += 1
            return
            
        # 2-B. 다르다면 4등분하여 재귀 호출
        half = n // 2
        compress(x, y, half)          # 왼쪽 위
        compress(x, y + half, half)   # 오른쪽 위
        compress(x + half, y, half)   # 왼쪽 아래
        compress(x + half, y + half, half) # 오른쪽 아래
        
    compress(0, 0, len(arr))
    return answer
```

### 코드 최적화 (Slicing vs Indexing)
위 코드는 `is_uniform` 검사에서 $O(N^2)$이 걸릴 수 있습니다. 재귀 깊이를 고려하면 전체 복잡도는 괜찮지만, Python 슬라이싱이나 `sum`을 이용하면 조금 더 깔끔하게 작성할 수 있습니다. 하지만 메모리 복사가 일어나므로 인덱싱 방식이 가장 효율적입니다.

팁: `sum`을 이용한 검사
- 현재 영역의 합이 `0`이면 모두 0, `n*n`이면 모두 1입니다.
- 그 외의 값이면 섞여 있는 것입니다.

```python
def solution(arr):
    answer = [0, 0]
    
    def compress(x, y, n):
        # 첫 번째 값과 비교
        init = arr[x][y]
        
        # 반복문으로 확인
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != init:
                    # 섞여 있으면 4분할
                    half = n // 2
                    compress(x, y, half)
                    compress(x, y + half, half)
                    compress(x + half, y, half)
                    compress(x + half, y + half, half)
                    return
        
        # 반복문을 무사히 통과했다면 모두 동일한 값
        answer[init] += 1
        
    compress(0, 0, len(arr))
    return answer
```
