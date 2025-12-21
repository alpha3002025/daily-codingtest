# [PCCP 기출문제] 1번 / 붕대 감기

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/250137)

붕대 감기 기술은 `t`초 동안 붕대를 감으며 1초마다 `x`만큼 체력을 회복합니다.
- `t`초 연속 성공 시 `y`만큼 추가 회복합니다.
- 최대 체력(`health`)을 초과할 수 없습니다.
- 기술 사용 중 몬스터에게 공격받으면 기술이 취소되고, **그 순간에는 회복할 수 없습니다.**
- 공격 당하면 연속 성공 시간이 0으로 초기화되고, 즉시 다시 붕대 감기를 시작합니다.
- 체력이 0 이하가 되면 캐릭터가 죽으며 `-1`을 반환합니다.

모든 공격(`attacks`)을 버티고 남은 체력을 반환하세요. (죽으면 -1)

**입력**:
- `bandage`: `[시전 시간(t), 초당 회복량(x), 추가 회복량(y)]`
- `health`: 최대 체력
- `attacks`: `[[공격 시간, 피해량], ...]` (오름차순 정렬됨)

## 해결 전략
시간 흐름에 따른 시뮬레이션 문제입니다.
공격이 일어나는 시간(`attack_time`)을 기준으로, **이전 공격 이후부터 현재 공격 직전까지의 시간 차이**를 계산하여 붕대 감기 회복량을 적용하면 효율적입니다.

1. **시간 차이 계산**: `time_diff = current_attack_time - last_attack_time - 1`
2. **회복량 계산**:
    - 초당 회복: `time_diff * x`
    - 추가 회복: `(time_diff // t) * y`
    - 총 회복량 = 초당 회복 + 추가 회복
    - 현재 체력에 더하되, 최대 체력을 넘지 않도록 조정.
3. **공격 처리**:
    - 현재 체력에서 피해량을 뺍니다.
    - 체력이 0 이하라면 즉시 `-1` 반환.
    - `last_attack_time`을 현재 공격 시간으로 갱신.

### 알고리즘 순서
1. `current_health` = `health`, `last_attack_time` = 0 초기화.
2. `bandage`에서 `t`, `x`, `y` 언패킹.
3. `attacks` 배열 순회:
    - 공격 전까지의 회복 시간 계산: `diff = attack_time - last_attack_time - 1`
    - 회복량 적용:
        - `heal_amount = diff * x + (diff // t) * y`
        - `current_health = min(health, current_health + heal_amount)`
    - 공격 적용:
        - `current_health -= damage`
    - 생존 확인:
        - `if current_health <= 0: return -1`
    - 시간 갱신:
        - `last_attack_time = attack_time`
4. 모든 공격 후 남은 `current_health` 반환.

## Python 코드

```python
def solution(bandage, health, attacks):
    t, x, y = bandage
    current_health = health
    last_attack_time = 0
    
    for attack_time, damage in attacks:
        # 공격 전까지 붕대 감기 시간
        diff = attack_time - last_attack_time - 1
        
        # 회복량 계산 (초당 회복 + 추가 회복)
        heal = (diff * x) + (diff // t * y)
        
        # 체력 회복 (최대 체력 초과 불가)
        current_health = min(health, current_health + heal)
        
        # 공격 받음
        current_health -= damage
        
        # 사망 확인
        if current_health <= 0:
            return -1
        
        # 마지막 공격 시간 갱신
        last_attack_time = attack_time
        
    return current_health
```

## 배운 점 / 팁
- **효율적인 시뮬레이션**: 1초 단위로 루프를 돌리는 것보다, 이벤트(공격)가 발생하는 시점 사이의 간격을 계산하여 한 번에 처리하는 것이 훨씬 효율적입니다.(`Time Jumping` 방식)
- **경계 조건**: `diff` 계산 시, 직전 공격 시간과 현재 공격 시간 사이의 *빈 시간*은 `current - last - 1`입니다. (예: 2초에 공격받고 5초에 공격받으면, 3, 4초 동안 감음 -> 5-2-1 = 2초)
