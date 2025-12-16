# 자물쇠와 열쇠

## 문제 설명
`key`($M \times M$)와 `lock`($N \times N$)이 있습니다.
`key`는 회전과 이동이 가능합니다.
`key`의 돌기(1)와 `lock`의 홈(0)이 딱 맞게 겹쳐져서, `lock`의 모든 홈(0)을 채울 수 있는지(전부가 1이 되는지) 확인하세요.
`key`의 돌기와 `lock`의 돌기가 겹치면 안 됩니다.

## 문제 해결 전략

$N, M$이 최대 20으로 매우 작습니다. **완전 탐색 (Brute Force)**이 가능합니다.

1. **자물쇠 확장 (Padding)**:
   - `key`가 `lock`의 일부만 겹칠 수 있으므로, `lock`을 충분히 큰 격자 중앙에 배치합니다.
   - 격자 크기: `size = N + 2 * (M - 1)`. (Key가 Lock의 왼쪽 끝에 걸치는 경우 ~ 오른쪽 끝에 걸치는 경우)
   - 보통 3배 크기 (`3*N`) 정도면 충분히 커버됩니다.

2. **이동 & 회전**:
   - Key를 0, 90, 180, 270도 회전시킵니다.
   - 확장된 격자 위에서 Key를 한 칸씩 이동(슬라이딩)시키며 Lock과 맞춰봅니다.

3. **확인 로직**:
   - Key를 확장 격자에 더합니다 (`+=`).
   - Lock 영역의 값들이 모두 1인지 확인합니다.
     - 1이면 채워짐.
     - 0이면 안 채워짐.
     - 2이면 돌기끼리 충돌.
   - 확인 후에는 Key를 다시 빼주어(`-=`) 원상복구합니다.

## Python 코드

```python
def rotate(key):
    m = len(key)
    new_key = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            new_key[j][m-1-i] = key[i][j]
    return new_key

def check(new_lock, offset, n):
    # 중앙의 lock 영역(offset ~ offset+n)이 모두 1인지 확인
    for i in range(n):
        for j in range(n):
            if new_lock[offset + i][offset + j] != 1:
                return False
    return True

def solution(key, lock):
    m = len(key)
    n = len(lock)
    
    # 확장된 Lock 생성 (3배 크기)
    expand_size = n + 2 * m # 넉넉하게
    offset = m # lock 시작 위치
    
    # 초기화
    bg = [[0] * expand_size for _ in range(expand_size)]
    for i in range(n):
        for j in range(n):
            bg[offset + i][offset + j] = lock[i][j]
            
    # 4방향 회전
    for _ in range(4):
        # 모든 위치 탐색
        # key가 lock과 겹칠 수 있는 범위: 0 ~ expand_size - m
        for r in range(expand_size - m):
            for c in range(expand_size - m):
                # 키 끼우기
                for i in range(m):
                    for j in range(m):
                        bg[r + i][c + j] += key[i][j]
                        
                # 확인
                if check(bg, offset, n):
                    return True
                    
                # 키 빼기 (원상복구)
                for i in range(m):
                    for j in range(m):
                        bg[r + i][c + j] -= key[i][j]
                        
        key = rotate(key)
        
    return False
```
