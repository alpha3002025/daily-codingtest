import sys

N,L = map(int, sys.stdin.readline().strip().split())

## 1 base 배열을 만들기 위해 [0] 추가
A = [0] + list(map(int, sys.stdin.readline().strip().split()))
window_size = L


result = ''
for i in range(1, len(A)):
    start = i - window_size + 1 ## (-1 -> 0 -> 1 -> ...)
    t = 123456789

    for curr in range(start, start+window_size):
        if curr <= 0:
            continue
        t = min(t, A[curr])
    
    result += (str(t) + ' ')

print(result)