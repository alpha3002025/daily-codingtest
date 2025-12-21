# 유연근무제

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/388351)

일주일 동안 "유연근무제 이벤트"가 열립니다. 직원들은 각자 희망하는 출근 시간(`start_time`)을 설정하고, 이벤트 기간(7일) 동안 평일(월~금)에는 설정한 시간 + 10분 이내에 출근해야 상품을 받을 수 있습니다. (토, 일은 기록에 상관없이 영향을 주지 않습니다.)

- `schedules`: 각 직원의 희망 출근 시간 (정수 HHMM) 배열
- `timelogs`: 각 직원의 7일간 실제 출근 시간 (정수 HHMM) 2차원 배열
    - `timelogs[i][j]`는 i번 직원의 j+1일차 출근 시간
- `startday`: 이벤트 시작 요일 (1:월, 2:화, ..., 7:일)

상품을 받을 직원의 수를 구하세요.

## 해결 전략
단순한 구현(Simulation) 문제입니다. 각 직원에 대해 모든 평일의 출근 기록을 검사하여 조건을 만족하는지 확인하면 됩니다.

1. **시간 더하기 연산**: HHMM 형식의 시간에 10분을 더할 때, 분(MM)이 60을 넘어가면 시(HH)를 1 올리고 분을 조정해야 합니다.
    - 예: 0955 + 10분 -> 1005
    - 팁: 단순히 숫자로 더하면 965가 되므로, 시/분으로 쪼개서 계산하거나 전체를 분 단위로 변환해 계산 후 다시 HHMM으로 바꿀 수 있습니다. 여기서는 단순히 10분을 더해주는 `add_10_min` 함수를 만들면 편리합니다.
2. **요일 처리**: `startday`를 기준으로 각 `timelog` 인덱스가 무슨 요일인지 판별하고, 주말(6:토, 7:일)이면 검사에서 제외해야 합니다.
    - `(startday + j - 1) % 7` 등으로 요일 계산을 할 수 있지만, `startday`가 1-based index이므로 직관적인 매핑이 필요합니다.
    - `current_day`를 갱신하며 주말인지 확인하는 방법이 간단합니다.

### 알고리즘 순서
1. `schedules` 배열을 순회하며 각 직원을 검사합니다.
2. 직원의 희망 출근 시간에 인정 가능한 마지노선 시간(`limit_time`)을 계산합니다.
    - `HH * 60 + MM + 10` 분으로 변환 후 다시 HHMM으로 만들거나, 조건문으로 처리합니다.
3. 7일간의 `timelogs`를 순회합니다.
    - 오늘의 요일을 계산합니다. (시작 요일 + 경과 일수)
    - 요일이 토(6) 또는 일(7)이면 패스합니다. (주의: 요일 값이 7을 넘어가면 1로 돌아오도록 모듈러 연산 필요)
    - 평일인데 `actual_arrival > limit_time` 이면 실패(`flag = False`)하고 즉시 다음 직원으로 넘어갑니다.
4. 모든 평일에 대해 성공했다면 `answer`를 1 증가시킵니다.

## Python 코드

```python
def solution(schedules, timelogs, startday):
    answer = 0
    n = len(schedules)
    
    for i in range(n):
        # 1. 인정 가능한 시간 계산 (희망 시간 + 10분)
        target = schedules[i]
        
        # HHMM 분리
        target_h = target // 100
        target_m = target % 100
        
        target_m += 10
        if target_m >= 60:
            target_h += 1
            target_m -= 60
            
        limit_time = target_h * 100 + target_m
        
        # 2. 7일간의 기록 검사
        success = True
        
        # startday: 1(월) ~ 7(일)
        # timelogs 인덱스 j: 0 ~ 6
        for j in range(7):
            # 현재 요일 계산 (1~7로 맞추기 위해 약간의 조정)
            # 오늘 요일 = (시작요일 + 경과일수 - 1) % 7 + 1
            current_day = (startday + j - 1) % 7 + 1
            
            # 주말(6, 7)은 제외
            if current_day == 6 or current_day == 7:
                continue
                
            # 평일인데 늦었으면 실패
            if timelogs[i][j] > limit_time:
                success = False
                break
        
        if success:
            answer += 1
            
    return answer
```

## 배운 점 / 팁
- **시간 형식 처리**: HHMM 형식의 정수는 십진수 연산과 60진법 시간 연산이 섞여 있으므로 주의가 필요합니다. 분 단위로 통일하거나 `divmod` 등을 활용해 올림 처리를 정확히 해야 합니다.
- **모듈러 연산**: 요일이 순환될 때 `(day - 1) % 7 + 1` 패턴을 사용하면 1~7 범위를 유지하며 순환시킬 수 있습니다.
