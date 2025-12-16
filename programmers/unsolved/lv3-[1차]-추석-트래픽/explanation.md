# [1차] 추석 트래픽

## 문제 설명
로그 데이터 `[응답완료시간, 처리시간]`가 주어집니다.
초당 최대 처리량(1초간 처리하는 요청의 최대 개수)을 구하세요.
1초 구간은 `[t, t + 999ms]` 입니다 ("응답완료시간" `S`가 포함되거나, `S`부터 시작하거나 등등).
정확히는, 어떤 구간 `[t, t+1)` (1초, inclusive start, inclusive end interval length 1s -> 문제 예시: x ~ x+0.999초)에 걸쳐있는 요청의 개수.

## 문제 해결 전략

**슬라이딩 윈도우** 또는 **이벤트 포인트 검사**.
요청의 시작 시간과 끝 시간을 모두 밀리초(ms)로 변환합니다.
- `end_time`: 응답 완료 시간.
- `start_time`: `end_time` - `processing_time` + 1ms.
- 후보 구간의 시작점은 **각 요청의 시작점** 또는 **각 요청의 끝점**이 될 수 있습니다.
  - 보통 로그의 끝점 `end_time`을 기준으로 `[end_time, end_time + 999ms]` 구간을 검사하면 충분합니다. (왜냐하면 최대 트래픽 구간의 끝은 어떤 요청의 끝과 맞물리거나 시작과 맞물릴 것이므로)
  - 정확히는 모든 `start_time`과 `end_time`을 후보로 두고, 그 시각부터 1초간 몇 개가 겹치는지 세면 됩니다.
  - 데이터 2000개 -> $O(N^2)$ 가능.

## Python 코드

```python
def get_ms(time_str):
    h, m, s = time_str.split(':')
    s, ms = s.split('.')
    total_ms = int(h)*3600000 + int(m)*60000 + int(s)*1000 + int(ms)
    return total_ms

def solution(lines):
    logs = []
    for line in lines:
        _, time_s, duration_s = line.split()
        end_ms = get_ms(time_s)
        dur_ms = int(float(duration_s[:-1]) * 1000)
        start_ms = end_ms - dur_ms + 1
        logs.append((start_ms, end_ms))
        
    max_count = 0
    
    # 각 로그의 끝점을 기준으로 1초 구간 검사
    # (시작점을 기준으로 해도 되지만, 문제 특성상 끝점 기준만으로도 최대가 발견됨이 증명됨
    #  혹은 시작점, 끝점 모두 검사해도 N=2000이라 4000^2 ok)
    # 여기선 끝점 기준만 검사
    for i in range(len(logs)):
        # 구간: [logs[i][1], logs[i][1] + 999]
        window_start = logs[i][1]
        window_end = window_start + 999
        
        cnt = 0
        for start, end in logs:
            # 겹치는지 확인
            # 요청 기간: [start, end]
            # 윈도우 기간: [window_start, window_end]
            # 안 겹치는 경우: 요청 끝 < 윈도우 시작 OR 요청 시작 > 윈도우 끝
            if end < window_start or start > window_end:
                continue
            cnt += 1
            
        if cnt > max_count:
            max_count = cnt
            
    return max_count
```
