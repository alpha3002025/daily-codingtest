# [PCCP 기출문제] 1번 / 동영상 재생기

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/340213)

## 문제 설명
동영상 재생기의 3가지 기능(10초 전 이동, 10초 후 이동, 오프닝 건너뛰기)을 구현하는 문제입니다.
주어진 명령(`commands`)을 순차적으로 처리했을 때 최종 재생 위치를 "mm:ss" 형식으로 반환해야 합니다.

### 기능 상세
1.  **10초 전 이동 (`prev`)**: 현재 위치에서 10초 뒤로 이동합니다. 0분 0초 미만으로는 이동하지 않습니다.
2.  **10초 후 이동 (`next`)**: 현재 위치에서 10초 앞으로 이동합니다. 동영상의 길이를 초과하지 않습니다.
3.  **오프닝 건너뛰기**: 현재 재생 위치가 오프닝 구간(`op_start` ≤ `현재 위치` ≤ `op_end`)에 있다면, 자동으로 오프닝이 끝나는 위치(`op_end`)로 이동합니다.

**주의사항**: "오프닝 건너뛰기"는 명령 실행 전과 후에 모두 체크해야 합니다. 즉, 사용자의 입력을 기다리는 상태일 때 항상 오프닝 구간인지 확인하여 건너뛰기를 수행해야 합니다.

## 해결 방법

시간을 문자열("mm:ss")로 다루는 것보다 **초(second) 단위의 정수로 변환**하여 계산하는 것이 훨씬 간편합니다.
모든 시간 관련 입력을 초 단위로 변환한 후, 로직을 수행하고 마지막에 다시 "mm:ss"로 변환합니다.

### 알고리즘

1.  모든 입력 시간(`video_len`, `pos`, `op_start`, `op_end`)을 초 단위 정수로 변환합니다.
2.  **초기 오프닝 체크**: 시작 위치(`pos`)가 오프닝 구간에 포함되는지 확인하고, 맞다면 `op_end`로 이동시킵니다.
3.  각 명령(`command`)에 대해:
    *   `prev`: 현재 위치에서 10을 뺍니다. (단, 0보다 작아지면 0으로 설정)
    *   `next`: 현재 위치에서 10을 더합니다. (단, 영상 길이를 초과하면 영상 길이로 설정)
    *   **명령 후 오프닝 체크**: 이동한 위치가 오프닝 구간에 포함되는지 확인하고, 맞다면 `op_end`로 이동시킵니다.
4.  최종 위치를 "mm:ss" 형식으로 변환하여 반환합니다.

## Python 풀이

```python
def time_to_seconds(t):
    """ 'mm:ss' 문자열을 초 단위 정수로 변환 """
    m, s = map(int, t.split(':'))
    return m * 60 + s

def seconds_to_time(s):
    """ 초 단위 정수를 'mm:ss' 문자열로 변환 """
    m = s // 60
    s = s % 60
    return f"{m:02d}:{s:02d}"

def solution(video_len, pos, op_start, op_end, commands):
    total_len = time_to_seconds(video_len)
    current = time_to_seconds(pos)
    op_s = time_to_seconds(op_start)
    op_e = time_to_seconds(op_end)
    
    # 1. 초기 위치가 오프닝 구간인지 확인
    if op_s <= current <= op_e:
        current = op_e
        
    for cmd in commands:
        # 2. 명령어 실행
        if cmd == "prev":
            current = max(0, current - 10)
        elif cmd == "next":
            current = min(total_len, current + 10)
            
        # 3. 이동 후 위치가 오프닝 구간인지 확인 (필수)
        if op_s <= current <= op_e:
            current = op_e
            
    return seconds_to_time(current)
```

### 핵심 포인트
*   **단위 통일**: 복잡한 시간 계산을 피하기 위해 모든 시간을 가장 작은 단위인 '초'로 변환하여 처리했습니다.
*   **오프닝 체크 시점**: 문제의 설명에 따르면 사용자의 입력을 처리하기 전, 그리고 처리한 후 항상 오프닝 구간 체크가 이루어져야 합니다. 따라서 반복문 진입 전 1회, 그리고 반복문 내부에서 명령 실행 후 1회 체크해야 합니다.
