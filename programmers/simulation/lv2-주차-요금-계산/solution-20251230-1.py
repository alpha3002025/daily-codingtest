from collections import defaultdict
import math

def to_minute(time_str):
    hour, minute = time_str.split(":")
    return int(hour)*60 + int(minute)

def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees
    base_time = int(base_time)
    unit_time = int(unit_time)
    
    parking_cars = defaultdict(int)
    parking_duration = defaultdict(int)
    for record in records:
        time_str, car_num, in_out = record.split()
        time = to_minute(time_str)
        
        if in_out == "IN":
            parking_cars[car_num] = time
        else:
            last_time = parking_cars.pop(car_num, 0)
            parking_duration[car_num] += time - last_time
    
    end_time = to_minute("23:59")
    for car_num in parking_cars.keys():
        parking_duration[car_num] += end_time - parking_cars[car_num]
    
    answer = []
    for car_num in sorted(parking_duration.keys()):
        parked_time = parking_duration[car_num]
        if parked_time <= base_time:
            answer.append(base_fee)
        else:
            remain_price = math.ceil((parked_time - base_time)/unit_time) * unit_fee
            answer.append(base_fee + remain_price)
    
    return answer