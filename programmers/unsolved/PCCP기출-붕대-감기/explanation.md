# [PCCP 기출문제] 1번 / 붕대 감기

## 문제 설명
몬스터의 공격 사이 시간 동안 "붕대 감기" 기술을 사용하여 체력을 회복하고, 몬스터의 공격을 버텨내는 시뮬레이션 문제입니다.
- **붕대 감기**: `t`초 동안 시전하며 1초당 `x`만큼 회복. `t`초 연속 성공 시 `y`만큼 추가 회복.
- **공격**: 공격 당하는 순간 회복 불가, 기술 취소(연속 성공 초기화). 공격 후 즉시 다시 붕대 감기 시도.
- **죽음**: 체력이 0 이하가 되면 -1 반환.
- **최대 체력**: 회복 시 최대 체력을 초과할 수 없음.

## 접근법 & 주요 개념

### 1. 시뮬레이션 (Simulation)
전체 시간을 1초 단위로 시뮬레이션할 수도 있지만, 공격 시간이 최대 1,000초이고 공격 횟수가 100회 이하이므로 **공격과 공격 사이의 시간(Gap)**을 계산하여 한 번에 처리하는 것이 효율적입니다.

### 2. 시간 차이 계산
- 현재 공격 시간(`current_time`)과 직전 공격 시간(`last_attack_time`)의 차이를 이용해 회복 가능한 시간(`gap`)을 구합니다.
- `gap = current_time - last_attack_time - 1`
  - 예: 2초에 공격, 9초에 공격 -> 3, 4, 5, 6, 7, 8초 (총 6초) 동안 회복 가능.

### 3. 회복량 계산 공식
회복 가능한 시간 `gap` 동안:
- **기본 회복**: `gap * x`
- **추가 회복**: `(gap // t) * y` (시전 시간 `t`를 채운 횟수만큼 추가 회복)
- 총 회복량 = `gap * x + (gap // t) * y`
- **단, 공격을 당하면 연속 성공 시간이 초기화되므로, 다음 구간 계산 시 연속 성공 시간은 항상 0부터 시작한다고 볼 수 있습니다.**

## Python 풀이

```python
def solution(bandage, health, attacks):
    # bandage: [시전 시간(t), 초당 회복량(x), 추가 회복량(y)]
    t, x, y = bandage
    max_health = health # 최대 체력 저장
    current_health = health
    last_attack_time = 0 # 마지막 공격 시간 (초기값 0)
    
    for attack_time, damage in attacks:
        # 1. 공격 전까지의 시간 동안 회복
        gap = attack_time - last_attack_time - 1
        
        if gap > 0:
            # 기본 회복
            heal_amount = gap * x
            # 추가 회복 (연속 성공 횟수)
            bonus_heal = (gap // t) * y
            
            current_health = min(max_health, current_health + heal_amount + bonus_heal)
            
        # 2. 몬스터 공격 적용
        current_health -= damage
        
        # 3. 사망 여부 확인
        if current_health <= 0:
            return -1
            
        # 4. 마지막 공격 시간 갱신
        last_attack_time = attack_time
        
    return current_health
```

### 코드 분석
1.  **변수 초기화**: `max_health`, `last_attack_time`.
2.  **공격 루프**: `attacks` 배열을 순회하며 각 공격에 대해 처리합니다.
3.  **회복 계산**:
    -   `gap`이 0보다 클 때만 수행합니다. (연속된 공격의 경우 `gap`이 0일 수 있음)
    -   `min(max_health, ...)`를 사용하여 최대 체력을 넘지 않도록 합니다.
4.  **피해 적용 및 종료 조건**:
    -   체력을 감소시키고 `0` 이하인지 체크하여 즉시 `-1`을 반환합니다.
5.  **상태 갱신**: 공격이 끝난 후 `last_attack_time`을 현재 공격 시간으로 업데이트합니다.
