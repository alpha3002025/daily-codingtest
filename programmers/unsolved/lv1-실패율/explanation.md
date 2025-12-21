# 실패율

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42889)

스테이지 `N`개가 있습니다.
- **실패율** = (스테이지에 도달했으나 클리어 못한 수) / (스테이지에 도달한 수)

`stages` 배열(사용자가 멈춰있는 스테이지 번호)이 주어질 때, **실패율이 높은 스테이지부터 내림차순**으로 정렬하여 반환하세요.
- 실패율이 같으면 작은 번호가 먼저 옵니다.
- 도달한 유저가 없으면 실패율은 0입니다.

## 해결 전략
1. 각 스테이지별로 "머물러 있는 사람 수"(`count`)를 셉니다. (Counter 활용)
2. `reached` (도달한 사람 수)를 전체 사용자 수로 초기화합니다.
3. 1번부터 `N`번 스테이지까지 순회하며:
    - 실패율 = `count` / `reached`
    - 다음 스테이지를 위해 `reached -= count` (현재 스테이지에서 멈춘 사람은 다음 스테이지 도달 못함)
    - 예외 처리: `reached`가 0이면 실패율 0.
4. `(스테이지 번호, 실패율)` 리스트를 만들어 정렬합니다.

### 알고리즘 순서
1. `answer` = []
2. `people_count` = `people_at_stage` (Counter or list)
3. `reached` = `len(stages)`
4. `i` from 1 to `N`:
    - `at_stage` = `people_count[i]` (해당 스테이지에 멈춘 수)
    - `fail_rate` = `at_stage / reached` if `reached > 0` else 0
    - `answer.append((i, fail_rate))`
    - `reached -= at_stage`
5. `answer` 정렬: 1순위 key=`-fail_rate`(내림차순), 2순위 key=`stage_num`(오름차순).
6. 스테이지 번호만 반환.

## Python 코드

```python
def solution(N, stages):
    result = {}
    total_people = len(stages)
    
    # 1단계 ~ N단계 순회
    for stage in range(1, N + 1):
        if total_people != 0:
            # 현재 스테이지에 멈춘 사람 수
            count = stages.count(stage) 
            # 참고: count()는 O(M)이므로 전체 O(N*M)이 됩니다.
            # M(stages길이)이 20만이므로, 시간 초과 방지를 위해 collections.Counter를 쓰는 게 좋습니다.
            # 하지만 N이 500이라서 500 * 200,000 = 1억 회 연산 -> 아슬아슬하게 통과하거나 느릴 수 있음.
            # 개선: 정렬 후 처리 or Counter 사용. 아래는 정석적인 개선 버전.
            
            fail_rate = count / total_people
            result[stage] = fail_rate
            total_people -= count
        else:
            result[stage] = 0
            
    # 실패율 기준 내림차순 정렬 (실패율 같으면 스테이지 오름차순 - 파이썬 기본 안정 정렬)
    return sorted(result, key=lambda x: result[x], reverse=True)

# 최적화된 버전 (Counter 사용)
from collections import Counter
def solution_optimized(N, stages):
    counts = Counter(stages)
    reached = len(stages)
    fail_rates = []
    
    for stage in range(1, N + 1):
        if reached > 0:
            count = counts[stage]
            rate = count / reached
            reached -= count
            fail_rates.append((stage, rate))
        else:
            fail_rates.append((stage, 0))
            
    # 정렬: 비율 내림차순 -> 번호 오름차순
    # 파이썬 sort는 stable하므로 비율로만 정렬해도 번호 순서는 유지되지만, 
    # 명시적으로 (-rate, stage) 튜플 비교가 안전함
    fail_rates.sort(key=lambda x: (-x[1], x[0]))
    
    return [stage for stage, rate in fail_rates]
```

**참고**: 위 코드 중 `solution_optimized`를 사용하는 것이 좋습니다.

## 배운 점 / 팁
- **시간 복잡도**: `list.count()`를 반복문 안에서 쓰면 `O(N*M)`이 되어 위험할 수 있습니다. `Counter`나 정렬을 통해 `O(M log M)` 혹은 `O(M)`으로 최적화해야 합니다.
- **다중 조건 정렬**: `lambda x: (조건1, 조건2)` 형태로 튜플을 반환하면 우선순위대로 정렬됩니다. 내림차순은 `-`를 붙이면 편리합니다.
