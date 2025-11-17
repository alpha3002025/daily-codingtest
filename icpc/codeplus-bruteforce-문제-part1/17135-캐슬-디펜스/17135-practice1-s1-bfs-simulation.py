import sys

N,M,D = map(int, sys.stdin.readline().split())

board = []
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

## 궁수 3
## 좌표를 순열로 만들어서 dfs 로 테스트해보면서 최적값을 조회해보는 개념