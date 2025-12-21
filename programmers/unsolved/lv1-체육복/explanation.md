# 체육복

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42862)

학생들이 체육복을 도난당했습니다(`lost`). 여벌이 있는 학생(`reserve`)들이 빌려줄 수 있습니다.
- 빌려줄 수 있는 대상: 바로 앞 번호나 바로 뒷 번호 학생.
- 여벌이 있는 학생도 도난당할 수 있음 (이 경우 빌려줄 수 없고, 자기 하나만 입음).
최대한 많은 학생이 체육복을 입을 수 있게 하세요.

## 해결 전략
그리디(Greedy) 문제입니다.
1. **중복 제거**: `lost`와 `reserve`의 교집합을 제거해야 합니다. ("여벌이 있지만 도난당한 학생"은 빌려주지도, 빌리지도 않음)
2. **빌려주기**: 번호 순서대로 처리해야 최적해를 찾을 수 있습니다.
    - 잃어버린 학생(`l`)에게 앞 번호(`l-1`)가 있으면 빌리고, 없으면 뒷 번호(`l+1`)가 있는지 확인합니다.
    - 앞 번호를 먼저 확인하는 것이 유리합니다 (작은 번호부터 처리하므로).

### 알고리즘 순서
1. `set_reserve` = `set(reserve) - set(lost)`
2. `set_lost` = `set(lost) - set(reserve)`
3. `set_lost`는 순서를 위해 `sorted(list(...))` 처리.
4. `set_lost` 순회 (`student`):
    - `if student - 1 in set_reserve`: (앞 번호에게 빌림)
        - `set_reserve.remove(student - 1)`
    - `elif student + 1 in set_reserve`: (뒷 번호에게 빌림)
        - `set_reserve.remove(student + 1)`
    - `else`:
        - `n -= 1` (못 빌림 -> 전체 수업 학생 수 감소)
5. `n` 반환.

## Python 코드

```python
def solution(n, lost, reserve):
    # 여벌 체육복을 가져온 학생이 도난당한 경우 제거
    # (set의 차집합 연산 활용)
    real_reserve = set(reserve) - set(lost)
    real_lost = set(lost) - set(reserve)
    
    # 잃어버린 학생들을 번호 순으로 정렬하여 처리 (앞 번호부터 빌려야 최적)
    for student in sorted(list(real_lost)):
        # 앞 번호 확인
        if student - 1 in real_reserve:
            real_reserve.remove(student - 1)
        # 뒷 번호 확인
        elif student + 1 in real_reserve:
            real_reserve.remove(student + 1)
        else:
            # 못 빌린 경우 전체 인원에서 뺌
            n -= 1
            
    return n
```

## 배운 점 / 팁
- **Set 차집합**: `set_a - set_b` 문법으로 간단히 중복을 제거할 수 있습니다.
- **그리디 순서**: 양방향(앞, 뒤) 선택지가 있을 때, 한쪽 방향(여기선 앞 번호)을 우선순위로 두고 순차적으로 처리하면 최적해가 보장되는 유형입니다.
