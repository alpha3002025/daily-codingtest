# [1차] 셔틀버스

## 문제 설명
셔틀버스가 `09:00`부터 `t`분 간격으로 `n`회 운행하며, 최대 `m`명 태울 수 있습니다.
대기열에 있는 크루들이 도착하는 시각 `timetable`이 주어질 때, 콘이 셔틀을 타고 사무실로 갈 수 있는 가장 늦은 시각을 구하세요.
콘은 같은 시각에 도착한 크루 중 가장 마지막에 탑승합니다.
결과는 `HH:MM` 형식.

## 문제 해결 전략

**시뮬레이션 (Simulation)**.
1. 모든 시간을 분(minute) 단위로 변환.
2. `timetable` 오름차순 정렬.
3. 각 셔틀 버스 도착 시각마다 태울 수 있는 크루를 태워보냄 (`index` 관리).
4. **마지막 버스**가 중요:
   - 마지막 버스에 자리가 남으면: 버스 도착 시각에 타면 됨.
   - 자리가 꽉 차면: 마지막에 탄 사람보다 1분 빨리 타면 됨.

## Python 코드

```python
def time_to_min(t):
    h, m = map(int, t.split(':'))
    return h * 60 + m

def min_to_time(m):
    h = m // 60
    mm = m % 60
    return f"{h:02d}:{mm:02d}"

def solution(n, t, m, timetable):
    # 크루 도착 시간 변환 및 정렬
    crews = [time_to_min(x) for x in timetable]
    crews.sort()
    
    bus_time = 9 * 60
    crew_idx = 0
    
    # 마지막 전 버스까지 태워보내기
    for i in range(n - 1):
        # 이번 버스에 탈 수 있는 인원 (최대 m명)
        cnt = 0
        while cnt < m and crew_idx < len(crews) and crews[crew_idx] <= bus_time:
            crew_idx += 1
            cnt += 1
        bus_time += t
        
    # 마지막 버스 (bus_time)
    cnt = 0
    last_crew_time = 0
    # 태울 수 있는 사람 확인 (인덱스만 증가시키지 말고 누구인지 기록 필요할 수도, 여기선 인원수만)
    # 꽉 찼는지 판별을 위해 실제로 태워봄
    while cnt < m and crew_idx < len(crews) and crews[crew_idx] <= bus_time:
        last_crew_time = crews[crew_idx]
        crew_idx += 1
        cnt += 1
        
    if cnt < m:
        # 자리가 남음 -> 버스 시간에 딱 맞춰 옴
        return min_to_time(bus_time)
    else:
        # 꽉 참 -> 마지막 사람보다 1분 빨리
        return min_to_time(last_crew_time - 1)
```
