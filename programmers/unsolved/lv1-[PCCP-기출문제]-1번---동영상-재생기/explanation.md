# [PCCP 기출문제] 1번 / 동영상 재생기

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/340213)

동영상 재생기의 기능을 구현합니다.
- **prev (10초 전)**: 현재 위치에서 10초 뒤로 이동합니다. 0분 0초 미만으로 이동하면 0분 0초가 됩니다.
- **next (10초 후)**: 현재 위치에서 10초 앞으로 이동합니다. 동영상의 전체 길이를 초과하면 마지막 위치가 됩니다.
- **오프닝 건너뛰기**: 현재 위치가 오프닝 구간(`op_start` ≤ `pos` < `op_end`)에 포함되면, 자동으로 `op_end` 위치로 이동합니다.
    - **중요**: 이 기능은 사용자의 입력이 일어날 때마다 실행되며, **명령어를 수행하기 전**과 **수행한 후** 모두 체크해야 합니다. (문제 예시 설명 참조)

주어지는 모든 시간은 `"mm:ss"` 형태의 문자열입니다. 최종 위치를 `"mm:ss"` 형태로 반환하세요.

## 해결 전략
시간 처리 문제의 정석인 **"모든 시간을 초(second) 단위로 변환"**하여 계산하는 방식이 가장 간편하고 실수를 줄일 수 있습니다.

1. **Helper 함수 작성**:
    - `str_to_sec(time_str)`: "mm:ss" -> 정수 초
    - `sec_to_str(seconds)`: 정수 초 -> "mm:ss"

2. **오프닝 건너뛰기 로직**:
    - 현재 초(`current_pos`)가 `op_start_sec`와 `op_end_sec` 사이(`start <= curr <= end`, 보통 오프닝 끝 0초전까지 포함하므로 부등호 주의)에 있는지 확인하고, 맞다면 `op_end_sec`로 갱신합니다.
    - 문제 설명을 보면, "현재 재생 위치가 오프닝 구간인 경우 자동으로 오프닝이 끝나는 위치로 이동"한다고 되어 있습니다.

3. **명령어 처리**:
    - 시작 시점에 오프닝 구간인지 한 번 체크합니다.
    - 각 명령(`command`)에 대해:
        - `prev`: `current - 10`. (0보다 작아지면 0)
        - `next`: `current + 10`. (video_len보다 커지면 video_len)
        - 명령 수행 **후**에 다시 오프닝 구간 체크를 수행합니다.

### 알고리즘 순서
1. `video_len`, `pos`, `op_start`, `op_end`를 모두 초 단위 정수로 변환합니다.
2. 초기 `pos`에 대해 **오프닝 건너뛰기**를 수행합니다.
3. `commands` 배열을 순회합니다.
    - `prev`면 10초 뺍니다. (`max(0, pos)`)
    - `next`면 10초 더합니다. (`min(video_len, pos)`)
    - 이동 후, 다시 **오프닝 건너뛰기**를 수행합니다.
4. 최종 `pos`를 "mm:ss" 문자열로 변환하여 반환합니다.

## Python 코드

```python
def to_seconds(time_str):
    m, s = map(int, time_str.split(':'))
    return m * 60 + s

def to_string(seconds):
    m = seconds // 60
    s = seconds % 60
    return f"{m:02d}:{s:02d}"

def solution(video_len, pos, op_start, op_end, commands):
    # 1. 초 단위 변환
    full_len = to_seconds(video_len)
    current = to_seconds(pos)
    start = to_seconds(op_start)
    end = to_seconds(op_end)
    
    # 2. 초기 오프닝 체크
    if start <= current <= end:
        current = end
    
    # 3. 명령어 처리
    for cmd in commands:
        if cmd == "prev":
            current -= 10
            if current < 0:
                current = 0
        elif cmd == "next":
            current += 10
            if current > full_len:
                current = full_len
        
        # 이동 후 오프닝 체크 (구간 내에 있으면 끝으로 점프)
        if start <= current <= end:
            current = end
            
    return to_string(current)
```

## 배운 점 / 팁
- **단위 통일**: 시간(시:분:초) 문제는 무조건 가장 작은 단위(초)로 변환해서 계산하세요. 코드가 훨씬 간결해집니다.
- **경계값 처리**: 0초 미만이거나 전체 길이를 초과하는 경우에 대한 예외 처리를 꼼꼼히 해야 합니다 (`max`, `min` 활용).
- **조건 확인 시점**: 오프닝 건너뛰기와 같은 자동 트리거 기능이 "언제" 동작하는지(입력 전/후, 혹은 매 순간) 문제 지문을 꼼꼼히 읽어야 합니다. 여기서는 초기 시작 시와 이동 직후 모두 체크해야 합니다.
