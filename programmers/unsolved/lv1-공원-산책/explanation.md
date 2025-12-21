# 공원 산책

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/172928)

직사각형 격자 모양의 공원(`park`)에서 로봇 강아지가 주어진 명령(`routes`)에 따라 이동합니다.
- `S`: 시작 지점
- `O`: 이동 가능 통로
- `X`: 장애물
- 명령: `"방향 거리"` (예: "E 5")

로봇은 명령을 수행하기 전에 다음 두 가지를 미리 확인하고, 하나라도 해당되면 **해당 명령을 건너뜁니다(무시)**.
1. 공원을 벗어나는 경우
2. 이동 경로 중간에 장애물이 있는 경우

모든 명령 수행 후 최종 위치 `[세로, 가로]`를 반환하세요.

## 해결 전략
전형적인 2차원 배열 시뮬레이션 문제입니다.
**"이동 경로 전체"**에 대해 장애물 검사를 해야 한다는 점이 핵심입니다. 단순히 도착점만 검사하면 안 됩니다.

1. **시작점 찾기**: `park`를 순회하며 `S`의 위치 `(h, w)`를 찾습니다.
2. **방향 매핑**: `N, S, W, E`에 따른 `(dh, dw)` 델타 값을 딕셔너리로 정의합니다.
    - `{"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}`
3. **명령 처리**:
    - 각 명령을 파싱하여 `op`와 `n`을 얻습니다.
    - 현재 위치에서 `op` 방향으로 `1`부터 `n`칸까지 **한 칸씩** 이동해보며 검사합니다.
    - 도중에 하나라도 공원을 벗어나거나 `X`를 만나면, 해당 명령은 무시하고 루프를 탈출(`break`)합니다.
    - `n`칸까지 모두 통과했다면 실제 위치를 업데이트합니다.

### 알고리즘 순서
1. 공원 크기 `H`, `W` 저장.
2. 시작 위치 `y, x` 찾기.
3. 방향 딕셔너리 `dirs` 정의.
4. `routes`의 각 명령 `route`에 대해:
    - `op, n = route.split()`
    - `dy, dx = dirs[op]`
    - 이동 가능 여부 플래그 `valid = True`
    - 임시 위치 `ny, nx = y, x`
    - `n`번 반복 (`step` 1 to `n`):
        - `ny += dy`, `nx += dx`
        - 범위 체크: `0 <= ny < H` and `0 <= nx < W`
        - 장애물 체크: `park[ny][nx] != 'X'`
        - 위반 시 `valid = False`, `break`
    - `valid`하다면 `y, x = ny, nx` (위치 갱신)
5. `[y, x]` 반환.

## Python 코드

```python
def solution(park, routes):
    H = len(park)
    W = len(park[0])
    
    # 시작 위치 찾기
    y, x = 0, 0
    for i in range(H):
        for j in range(W):
            if park[i][j] == "S":
                y, x = i, j
                break
                
    # 방향 정의
    dirs = {
        "N": (-1, 0),
        "S": (1, 0),
        "W": (0, -1),
        "E": (0, 1)
    }
    
    for route in routes:
        op, n_str = route.split()
        n = int(n_str)
        dy, dx = dirs[op]
        
        # 이동 가능 여부 확인
        # 현재 위치에서 시작해서 한 칸씩 검사
        cur_y, cur_x = y, x
        is_possible = True
        
        for _ in range(n):
            cur_y += dy
            cur_x += dx
            
            # 1. 공원을 벗어나는지
            if not (0 <= cur_y < H and 0 <= cur_x < W):
                is_possible = False
                break
            
            # 2. 장애물을 만나는지
            if park[cur_y][cur_x] == "X":
                is_possible = False
                break
        
        # 문제가 없다면 위치 업데이트
        if is_possible:
            y, x = cur_y, cur_x
            
    return [y, x]
```

## 배운 점 / 팁
- **경로 전체 검증**: "이동 중 장애물을 만나는지"라는 조건이 있을 때는 반드시 시작점부터 도착점까지의 모든 경로를 순회하며 검사해야 합니다.
- **가상 이동**: 실제 위치 변수를 바로 갱신하지 말고, 임시 변수로 시뮬레이션을 완료한 뒤 유효할 때만 갱신하는 패턴이 안전합니다.
