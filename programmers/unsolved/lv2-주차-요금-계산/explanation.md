# 주차 요금 계산

## 문제 설명
주차장의 요금표와 차량이 들어오고(입차) 나간(출차) 기록이 주어졌을 때, 차량별로 주차 요금을 계산하는 문제입니다.

### 핵심 개념
1.  **해시 맵 (Dictionary)**: 차량 번호를 키(Key)로, 입차 시간을 값(Value)으로 저장하여 입/출차 상태를 관리합니다.
2.  **누적 시간 계산**: 하루 동안의 총 주차 시간을 누적해서 요금을 정산해야 하므로, 출차 시 `(출차 시간 - 입차 시간)`을 계산하여 누적합니다.
3.  **예외 처리**: 입차 후 출차 기록이 없는 경우 23:59에 출차한 것으로 간주합니다.
4.  **수학 (올림)**: 기본 시간을 초과한 경우, 단위 시간으로 나누어 떨어지지 않으면 올림(`math.ceil`) 처리를 해야 합니다.

## Python 풀이

```python
import math

def time_to_min(time_str):
    """HH:MM 형식을 분 단위 정수로 변환"""
    h, m = map(int, time_str.split(':'))
    return h * 60 + m

def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees
    
    # 차량별 입차 시간 기록 (입차 상태)
    parked = {}
    # 차량별 누적 주차 시간
    total_time = {}
    
    for record in records:
        time_str, car_num, action = record.split()
        minutes = time_to_min(time_str)
        
        if action == "IN":
            parked[car_num] = minutes
        elif action == "OUT":
            in_time = parked.pop(car_num)
            parked_duration = minutes - in_time
            if car_num in total_time:
                total_time[car_num] += parked_duration
            else:
                total_time[car_num] = parked_duration
                
    # 출차 기록이 없는 차량 처리 (23:59 출차)
    end_of_day = time_to_min("23:59")
    for car_num, in_time in parked.items():
        pass_time = end_of_day - in_time
        if car_num in total_time:
            total_time[car_num] += pass_time
        else:
            total_time[car_num] = pass_time
            
    # 요금 계산 및 차량 번호 정렬
    answer = []
    # 차량 번호 오름차순으로 정렬
    for car_num in sorted(total_time.keys()):
        time = total_time[car_num]
        
        if time <= base_time:
            fee = base_fee
        else:
            fee = base_fee + math.ceil((time - base_time) / unit_time) * unit_fee
        answer.append(fee)
        
    return answer
```

### 코드 설명
- `time_to_min`: "HH:MM" 문자열을 분(minute) 단위 정수로 변환합니다. 계산을 쉽게 하기 위함입니다.
- `parked` 딕셔너리: 현재 주차 중인 차를 추적합니다. 'IN'이면 넣고, 'OUT'이면 pop하여 시간을 계산합니다.
- 루프가 끝난 후 `parked`에 남은 차들은 자정(23:59)에 나간 것으로 처리합니다.
- `sorted(total_time.keys())`: 문제 요구사항인 "차량 번호가 작은 자동차부터"를 만족하기 위해 정렬합니다.
- `math.ceil`: 초과 시간을 단위 시간으로 나눌 때 올림 처리를 위해 사용합니다.
