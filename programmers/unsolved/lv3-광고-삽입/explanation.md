# 광고 삽입

## 문제 설명
동영상 재생 시간(`play_time`), 공익광고 재생 시간(`adv_time`), 시청자들의 로그(`logs`)가 주어집니다.
공익광고를 동영상 내에 삽입할 때, **가장 많은 시청자(누적 재생 시간의 합이 최대)**가 볼 수 있는 시작 시간을 구하세요.
시간 포맷: `HH:MM:SS`.

## 문제 해결 전략

1. **시간 변환**:
   - 모든 시간을 **초(second)** 단위 정수로 변환합니다.
   - 최대 시간은 99:59:59 = 약 36만 초. 배열로 다루기에 충분합니다.

2. **누적합 (Imos법 / Prefix Sum)**:
   - `total_time` 길이만큼의 배열 `time_arr`를 만듭니다.
   - 각 로그 `start ~ end`에 대해, 시청자 수를 표시해야 합니다.
   - 단순히 루프로 더하면 로그가 30만 개라 시간 초과 ($O(L \times T)$).
   - **Imos 법**: `time_arr[start] += 1`, `time_arr[end] -= 1`.
   - 그 후 배열 전체를 한 번 스캔(누적합)하면 `time_arr[i]`는 **시각 i에 시청 중인 사람 수**가 됩니다.
   - 한 번 더 누적합을 구하면 `prefix_sum[i]`는 **0초부터 i초까지의 누적 시청 시간**이 됩니다.

3. **슬라이딩 윈도우 (구간 합)**:
   - 광고 시간 `adv_time`이 주어지면, 구간 `[start, start + adv_len]`의 시청 시간 합을 구합니다.
   - 이미 `prefix_sum`을 구했으므로, $O(1)$에 구할 수 있습니다.
   - `sum = prefix_sum[start + adv_len] - prefix_sum[start]`.
   - 모든 가능한 `start` (0 ~ play_len - adv_len)에 대해 최댓값을 찾습니다.

## Python 코드

```python
def str_to_int(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s

def int_to_str(time_val):
    h = time_val // 3600
    m = (time_val % 3600) // 60
    s = time_val % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def solution(play_time, adv_time, logs):
    play_len = str_to_int(play_time)
    adv_len = str_to_int(adv_time)
    
    if adv_len == play_len:
        return "00:00:00"
    
    # 시간별 시청자 수 변화 기록
    # play_len + 1 크기 (종료 시각 처리를 위해)
    time_arr = [0] * (play_len + 1)
    
    for log in logs:
        start, end = log.split('-')
        s = str_to_int(start)
        e = str_to_int(end)
        time_arr[s] += 1
        time_arr[e] -= 1
        
    # 1차 누적합 -> 시각 t의 시청자 수
    for i in range(1, play_len + 1):
        time_arr[i] += time_arr[i-1]
        
    # 2차 누적합 -> 0~t까지 누적 시청 시간
    # 주의: time_arr[i]는 i~(i+1) 구간의 시청자 수로 해석 가능
    for i in range(1, play_len + 1):
        time_arr[i] += time_arr[i-1]
        
    # 슬라이딩 윈도우로 최대 구간 찾기
    max_time = 0
    max_start = 0
    
    # 구간 [t, t + adv_len]
    # 누적합 P[x]는 0~x까지 합.
    # 구간 합 = P[end] - P[start]
    # 여기서 start=0일 때 P[adv_len-1]? 
    # 시간 i의 값은 i ~ i+1 구간 값이므로
    # 0시작, 길이 5초 -> 0,1,2,3,4 -> 총합 P[4] - P[-1].
    # 즉 P[start + adv_len - 1] - P[start - 1].
    
    # 하지만 time_arr 인덱스를 '종료 시각' 기준으로 생각하면 편함.
    # time_arr[t] : 0초부터 t초까지의 누적 합.
    # 광고 시작 t=0, 끝 t=adv_len. 구간 합 = time_arr[adv_len-1] (0초~adv_len초)
    # -> 인덱스 0부터 adv_len-1까지의 합.
    
    # 초기값 (0초 시작)
    # time_arr는 0~N까지 있음.
    # 0초~1초 구간 값은 time_arr[0] (1차누적합 후)
    # 2차누적합 후 time_arr[x] = sum(1차[0]...1차[x])
    # 따라서 0초부터 adv_len초까지 합은 time_arr[adv_len - 1]
    
    max_time = time_arr[adv_len - 1]
    max_start = 0
    
    for start in range(1, play_len - adv_len + 1):
        # start초에 시작, start + adv_len초에 끝남
        # 구간: [start, start + adv_len)
        # 누적합: time_arr[start + adv_len - 1] - time_arr[start - 1]
        
        current_sum = time_arr[start + adv_len - 1] - time_arr[start - 1]
        
        if current_sum > max_time:
            max_time = current_sum
            max_start = start
            
    return int_to_str(max_start)
```
