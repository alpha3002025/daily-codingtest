from collections import defaultdict
import math

def to_minute(s):
    hh, mm = s.split(":")
    return int(hh)*60 + int(mm)

def solution(fees, records):
    answer = []
    
    base_minute, base_price, unit_minute, unit_price = fees
    
    parking_events = defaultdict(int) ## 들어온 시각 기록
    parking_duration = defaultdict(int) ## 계산용도
    
    for record_str in records:
        time, car_num, in_out = record_str.split()
        
        if in_out == "IN":
            parking_events[car_num] = to_minute(time)
        else:
            duration = to_minute(time) - parking_events.pop(car_num, 0)
            parking_duration[car_num] += duration
        
    for car_num in parking_events.keys():
        parking_duration[car_num] += to_minute("23:59") - parking_events[car_num]
    
    
    for car_num in sorted(parking_duration.keys()):
        duration = parking_duration[car_num]
        
        if duration <= base_minute:
            answer.append(base_price)
        else:
            overflowed_time = duration - base_minute
            overflowed_fee = math.ceil(overflowed_time / unit_minute) * unit_price
            answer.append(base_price + overflowed_fee)
    
    return answer
