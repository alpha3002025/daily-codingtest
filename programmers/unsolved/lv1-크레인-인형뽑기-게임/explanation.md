# 크레인 인형뽑기 게임

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/64061)

격자(`board`)에 인형들이 쌓여 있습니다.
크레인으로 `moves` 위치의 맨 위 인형을 집어 바구니(`basket`)에 담습니다.
바구니에 **같은 모양의 인형 두 개가 연속**으로 쌓이면 터져서 사라집니다.
터진 인형의 총 개수를 구하세요.

## 해결 전략
1. **스택 (바구니)**: 바구니는 후입선출(LIFO) 구조이므로 스택을 사용합니다.
2. **2차원 배열 조작**: 크레인이 내려가면서(`row` 증가) 처음 만나는 인형(`!= 0`)을 찾아서 집어야 합니다.
3. **매칭 로직**: 인형을 집어서 스택에 넣기 전에, `stack[-1]`(맨 위)과 같은지 확인하고, 같으면 `pop` 후 `cnt += 2`.

### 알고리즘 순서
1. `basket` = [], `count` = 0
2. `moves` 순회 (`col`):
    - `col -= 1` (0-indexed 변환)
    - `board`의 각 `row` 순회:
        - `if board[row][col] != 0`: (인형 발견)
            - `doll = board[row][col]`
            - `board[row][col] = 0` (집었으므로 빈칸 처리)
            - **바구니 확인**:
                - `if basket and basket[-1] == doll`:
                    - `basket.pop()`
                    - `count += 2`
                - `else`:
                    - `basket.append(doll)`
            - `break` (한 번에 하나만 집음)
3. 반환 `count`.

## Python 코드

```python
def solution(board, moves):
    basket = []
    count = 0
    
    for move in moves:
        col = move - 1 # 0-indexed
        
        # 위에서부터 내려가며 인형 탐색
        for row in range(len(board)):
            if board[row][col] != 0:
                doll = board[row][col]
                board[row][col] = 0 # 인형 집기 (0으로 변경)
                
                # 바구니에 넣기 전 확인
                if basket and basket[-1] == doll:
                    basket.pop() # 터뜨리기
                    count += 2   # 2개 사라짐
                else:
                    basket.append(doll)
                    
                break # 하나 집었으면 해당 move 종료하고 다음 move로
                
    return count
```

## 배운 점 / 팁
- **시뮬레이션**: 문제의 격자 상태를 직접 수정(`board[r][c] = 0`)하며 진행해야 합니다.
- **스택 활용**: 연속된 중복 제거(애니팡 로직)는 스택의 전형적인 활용 사례입니다.
