import sys
from collections import deque

N,L = map(int, sys.stdin.readline().strip().split())

## 1 base 배열을 만들기 위해 [0] 추가
A = [0] + list(map(int, sys.stdin.readline().strip().split()))
window_size = L

dq = deque()

for i in range(1, len(A)):
    while dq and dq[-1][0] > A[i]: ## (1) : 걸러내기 
        dq.pop()
    
    dq.append((A[i], i)) ## (2) : (1) 에서 걸러낸 후 깨끗해진 곳에 새로운 요소를 append()

    if dq[0][1] < i - window_size +1: ## (3) : 사이즈를 넘어서면 pop
        dq.popleft()
    
    print(dq[0][0], end=' ')
