# 보석 쇼핑

## 문제 설명
진열대에 여러 종류의 보석들이 일렬로 놓여 있습니다.
특정 구간의 보석을 싹쓸이 쇼핑하려고 합니다.
**모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간**을 찾으세요.
가장 짧은 구간이 여러 개라면 시작 진열대 번호가 가장 작은 것을 선택합니다.

## 문제 해결 전략

전형적인 **투 포인터 (Two Pointers)** 또는 **슬라이딩 윈도우** 문제입니다.
구간 `[start, end]`를 관리하면서 모든 종류가 포함되는지 검사합니다.

1. **초기화**:
   - `gem_set`: 전체 보석 종류 집합. (`kind_cnt` = `len(gem_set)`)
   - `gem_dict`: 현재 윈도우 내 보석 종류별 개수.
   - `start = 0`, `end = 0`

2. **확장 (Expand)**:
   - `end`를 증가시키며 `gems[end]`를 `gem_dict`에 추가합니다.
   - 현재 윈도우의 보석 종류 수(`len(gem_dict)`)가 `kind_cnt`와 같아질 때까지 반복합니다.

3. **축소 (Shrink)**:
   - 모든 종류가 포함된 상태라면, `start`를 증가시키며 범위를 줄여봅니다.
   - `gems[start]`를 `gem_dict`에서 하나 빼고, 만약 개수가 0이 되면 `gem_dict`에서 키를 제거합니다.
   - 여전히 모든 종류가 포함된다면 더 짧은 구간을 찾은 것이므로 답을 갱신하고 계속 축소합니다.
   - 종류가 부족해지면 다시 확장을 시작합니다.

4. **결과**: `[최소구간 시작+1, 최소구간 끝+1]` 반환.

## Python 코드

```python
from collections import defaultdict

def solution(gems):
    kinds = len(set(gems))
    n = len(gems)
    
    answer = [1, n] # 일단 전체 구간으로 초기화
    min_len = n
    
    gem_dict = defaultdict(int)
    
    start = 0
    end = 0
    
    # 슬라이딩 윈도우
    # end가 n보다 작을 때까지, 혹은 start가 end보다 작거나 같을 때까지
    
    while True:
        # 모든 종류가 다 모였으면 -> start를 줄여서 최소 찾기
        if len(gem_dict) == kinds:
            current_len = end - start
            if current_len < min_len:
                min_len = current_len
                answer = [start + 1, end] # end는 이미 증가되어 있는 상태가 아니라, 현재 포함된 마지막 인덱스를 가리켜야 함?
                                         # 로직을: gems[end] 추가 -> check -> start 이동 방식이면 end는 현재 마지막 위치
            
            # start 이동 (축소)
            gem_dict[gems[start]] -= 1
            if gem_dict[gems[start]] == 0:
                del gem_dict[gems[start]]
            start += 1
            
        elif end == n:
            break
            
        else:
            # 아직 부족하면 -> end 늘리기
            gem_dict[gems[end]] += 1
            end += 1
            
    return answer
```
