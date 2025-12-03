import sys
input = sys.stdin.readline

## init
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
R,G,B = 0,1,2

## setup
min_red = board[0][R]
min_green = board[0][G]
min_blue = board[0][B]

## calc
for i in range(1, N):
    curr_red = min(min_green, min_blue) + board[i][R]
    curr_green = min(min_red, min_blue) + board[i][G]
    curr_blue = min(min_red, min_green) + board[i][B]
    min_red, min_green, min_blue = curr_red, curr_green, curr_blue

## answer
print(min(min_red, min_green, min_blue))

## 또는 다음과 같이 푸는 것 역시 가능하다. (이 방식이 덜 헷갈리긴한데, 가독성이 너무 떨어진다.)
## 8회차 연습 쯤에 이런식으로 연습해보자.
# for i in range(1, N):
#     min_red, min_green, min_blue = (
#         min(min_green, min_blue) + board[i][R],
#         min(min_red, min_blue) + board[i][G],
#         min(min_red, min_green) + board[i][B]
#     )