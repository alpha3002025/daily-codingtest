from collections import deque

def solution(game_board, table):
    empty_shapes = [normalize(b) for b in extract_shapes(game_board, 0)]
    puzzle_shapes = [normalize(b) for b in extract_shapes(table, 1)]
    
    answer = 0
    puzzle_used = [False] * len(puzzle_shapes)
    
    for empty_shape in empty_shapes:
        filled = False
        for i, puzzle in enumerate(puzzle_shapes):
            if puzzle_used[i]: continue
            
            ## 칸 수가 다르면 패스
            if len(empty_shape) != len(puzzle): continue
            
            curr_puzzle = puzzle
            match_found = False
            for _ in range(4):
                if curr_puzzle == empty_shape:
                    match_found = True
                    break
                curr_puzzle = rotate(curr_puzzle)
            
            if match_found:
                answer += len(empty_shape)
                puzzle_used[i] = True
                break ## 다음 빈 공간
    
    return answer


def extract_shapes(board, target_value):
    n = len(board)
    visited = [[False] * n for _ in range(n)]
    
    directions = [[-1,0], [1,0], [0,-1], [0,1]]
    shapes = []
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == target_value and not visited[i][j]:
                queue = deque([(i,j)])
                visited[i][j] = True
                shape = []
                
                while queue:
                    curr_r, curr_c = queue.popleft()
                    shape.append((curr_r, curr_c))
                    
                    for dr, dc in directions:
                        nr, nc = curr_r + dr, curr_c + dc
                        if not (0 <= nr < n and 0 <= nc < n): continue
                        if visited[nr][nc] == True: continue
                        if board[nr][nc] == target_value:
                            visited[nr][nc] = True
                            queue.append((nr,nc))
                
                shapes.append(shape)
    return shapes
    

# 좌표 정규화: (0,0) 시작으로 평행이동
def normalize(shape):
    # 좌표 정렬 (행 우선, 열 차선)
    shape.sort()
    # 기준점 (가장 위, 가장 왼쪽)
    min_r, min_c = shape[0]
    
    normalized = []
    for r, c in shape:
        normalized.append((r - min_r, c - min_c))
    return normalized


# 90도 회전 함수
def rotate(block):
    if not block: return []
    # 현재 블록의 크기(범위) 계산 -> 회전 중심? 아님 그냥 좌표 변환 후 다시 정규화하면 됨.
    # 90도 회전: (r, c) -> (c, -r) 혹은 (c, max_r - r)
    # 단순히 (c, -r) 하고 normalize 하면 됨.
    new_block = [(c, -r) for r,c in block]
    return normalize(new_block)