# [PCCP 기출문제] 3번 / 충돌위험 찾기

## 문제 설명
`n`개의 포인트와 `x`대의 로봇이 있습니다. 각 로봇은 지정된 경로(`routes`)를 따라 운송을 수행합니다.
로봇은 0초에 출발하며, 1초마다 인접한 칸(상하좌우)으로 이동합니다.
다음 포인트로 이동할 때는 **최단 경로**를 선택하며, 여러 경로가 있다면 **r 좌표(행) 이동을 우선**합니다.

이동 중에 **같은 시간, 같은 좌표에 2대 이상의 로봇이 모이는 경우**를 "위험 상황"이라고 합니다.(시작점, 끝점 포함)
모든 로봇이 운송을 마칠 때까지 발생하는 위험 상황의 총 횟수를 구해야 합니다.

## 접근법 & 주요 개념

### 1. 시뮬레이션 및 경로 기록 (Simulation & Path Recording)
로봇의 이동 경로가 결정론적(Deterministic)이므로, 각 로봇의 **시간별 위치(Time-Space Coordinate)**를 모두 미리 계산할 수 있습니다.
- 모든 로봇들이 독립적으로 움직인다고 가정하고, 각자 자신의 전체 경로를 생성합니다.
- 경로 생성 규칙:
  1. 현재 좌표 `(r1, c1)`에서 목표 좌표 `(r2, c2)`로 이동.
  2. **r 좌표 우선 변경**: `r1`이 `r2`가 될 때까지 1칸씩 이동.
  3. **c 좌표 변경**: `c1`이 `c2`가 될 때까지 1칸씩 이동.

### 2. 빈도수 세기 (Frequency Counting)
모든 로봇의 `(시간, r, c)` 정보를 수집하여, 겹치는 횟수를 셉니다.
- `Counter` 혹은 해시맵(Dictionary)을 사용하여 `(time, r, c)` 키에 대한 등장 횟수를 기록합니다.
- 모든 기록이 끝난 후, 등장 횟수가 2 이상인 키의 개수를 셉니다.

### 3. 시간 복잡도
- 로봇 수(`x`) ≤ 100
- 경로 길이(`m`) ≤ 100
- 좌표 범위 ≤ 100
- 한 로봇의 최대 이동 거리 ≈ 100 * 200 = 20,000 Step
- 전체 기록 개수 ≈ 2,000,000개
- 해시맵을 이용한 카운팅은 O(N)으로 충분히 효율적입니다.

## Python 풀이

```python
from collections import Counter

def solution(points, routes):
    # 1. 포인트 좌표 매핑 (1-based index -> 0-based or direct access)
    # 문제에서는 1번부터 사용하므로 딕셔너리나 리스트로 관리
    # points[i]는 i+1번 포인트의 좌표
    point_map = {i+1: tuple(p) for i, p in enumerate(points)}
    
    # 모든 로봇의 경로를 (시간, r, c) 형태로 기록
    # key: (time, r, c)
    path_counter = Counter()
    
    for route in routes:
        time = 0
        # 시작 포인트 처리
        start_point_idx = route[0]
        curr_r, curr_c = point_map[start_point_idx]
        
        # 시작점 기록
        path_counter[(time, curr_r, curr_c)] += 1
        
        # 경로 순회
        for i in range(len(route) - 1):
            next_point_idx = route[i+1]
            next_r, next_c = point_map[next_point_idx]
            
            # r 좌표 이동 (우선)
            while curr_r != next_r:
                time += 1
                if curr_r < next_r:
                    curr_r += 1
                else:
                    curr_r -= 1
                path_counter[(time, curr_r, curr_c)] += 1
            
            # c 좌표 이동
            while curr_c != next_c:
                time += 1
                if curr_c < next_c:
                    curr_c += 1
                else:
                    curr_c -= 1
                path_counter[(time, curr_r, curr_c)] += 1
                
    # 2. 충돌 횟수 계산
    # 2대 이상이 모인 경우(count >= 2)만 셈
    answer = 0
    for count in path_counter.values():
        if count >= 2:
            answer += 1
            
    return answer
```

### 코드 분석
1.  **`point_map` 생성**: 문제에서 포인트 번호가 1부터 시작하므로, 이를 쉽게 조회하기 위해 딕셔너리로 변환했습니다.
2.  **`path_counter`**: `(시간, r, c)` 튜플을 키로 사용하여 해당 시공간에 존재하는 로봇의 수를 셉니다.
3.  **경로 추적**:
    -   각 로봇(`route` in `routes`)에 대해 시뮬레이션을 수행합니다.
    -   `time`을 0부터 증가시키며 이동 경로상의 모든 좌표를 기록합니다.
    -   **Rule**: r 좌표를 먼저 맞추고 (`r` 이동), 그 다음 c 좌표를 맞춥니다 (`c` 이동).
4.  **결과 도출**: `Counter`의 값들을 확인하여 2 이상인 경우(충돌 위험)를 모두 더해 반환합니다.

### 팁
-   이 문제는 로봇끼리의 상호작용(예: 길막)이 없고 모두 독립적으로 움직이므로, 단순히 이동 경로를 **모두 기록(Record)**하고 **나중에 집계(Aggregate)**하는 방식이 가장 덜 복잡하고 빠릅니다.
