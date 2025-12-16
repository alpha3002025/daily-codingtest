# 혼자서 하는 틱택토

## 문제 설명
틱택토 게임을 혼자서 O와 X를 번갈아가며 둡니다.
주어진 3x3 보드 상태가 규칙을 지키며 나올 수 있는 상황인지 판별하는 문제입니다.
규칙:
1. O가 선공입니다.
2. 번갈아 가며 둡니다.
3. 가로, 세로, 대각선 중 하나라도 3개가 같은 표시가 만들어지면 승리하고 즉시 종료합니다.
보드의 상태가 규칙을 위반하는 경우 0, 아니면 1을 반환합니다.

## 풀이 개념
가능한, 불가능한 케이스를 논리적으로 따져봅니다.

1. **개수 체크**:
   - O가 선공이므로 O의 개수는 X의 개수와 같거나 1개 많아야 합니다.
   - `count(O) < count(X)` 또는 `count(O) > count(X) + 1` 이면 불가능(0).

2. **승리 조건 체크**:
   - O가 승리한 경우:
     - X는 승리하면 안 됩니다 (이미 O가 이겨서 끝났으므로).
     - 승리하고 종료했으므로, O가 마지막 수를 두어야 합니다. 즉 `count(O) == count(X) + 1`.
   - X가 승리한 경우:
     - O는 승리하면 안 됩니다.
     - X가 마지막 수를 두어야 합니다. 즉 `count(O) == count(X)`.
   - 둘 다 승리한 경우: 불가능(0).
     - (참고: 한 번의 수로 두 줄이 동시에 완성되는 경우는 가능하지만, 그 경우 승리한 쪽이 마지막 수를 둔 조건을 만족해야 합니다. 하지만 O승리 & X승리는 절대 불가능합니다.)

## 코드 (Python)

```python
def check_win(board, player):
    # 가로, 세로 확인
    for i in range(3):
        if all(board[i][j] == player for j in range(3)): return True
        if all(board[j][i] == player for j in range(3)): return True
    # 대각선 확인
    if all(board[i][i] == player for i in range(3)): return True
    if all(board[i][2-i] == player for i in range(3)): return True
    return False

def solution(board):
    o_cnt = sum(row.count('O') for row in board)
    x_cnt = sum(row.count('X') for row in board)
    
    # 1. 개수 기본 조건 위반
    if not (o_cnt == x_cnt or o_cnt == x_cnt + 1):
        return 0
    
    o_win = check_win(board, 'O')
    x_win = check_win(board, 'X')
    
    # 2. 둘 다 승리한 경우 (불가능)
    if o_win and x_win:
        return 0
    
    # 3. O가 승리했는데 개수가 안 맞는 경우 (O가 마지막이어야 함)
    if o_win and o_cnt != x_cnt + 1:
        return 0
        
    # 4. X가 승리했는데 개수가 안 맞는 경우 (X가 마지막이어야 함)
    if x_win and o_cnt != x_cnt:
        return 0
        
    return 1
```
