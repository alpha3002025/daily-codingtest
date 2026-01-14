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
    min_distance = float('inf')
    start,end = 0,0
    window = [start, end]
    
    occurrence = defaultdict(int)
    kind = set(gems)
    kind_cnt = len(kind)
    
    while True:
        ### 조심!!) 탈출 조건문을 맨 앞에 두면, 보석이 들어있어서 윈도우를 줄일 여지가 있어도 break 할때가 있다.
        # if end == len(gems):
        #     break
        
        # elif len(occurrence) == kind_cnt:
        if len(occurrence) == kind_cnt:
            ## 원하는 종류수를 채웠으면? => 윈도우를 줄여본다.
            # start += 1
            
            if min_distance > end - start:
                min_distance = end - start

                window = [start+1, end]

            occurrence[gems[start]] -= 1
            if occurrence[gems[start]] == 0:
                del occurrence[gems[start]]

            start += 1
            
        elif end == len(gems):
            break
        
        else:
            ## 종류수를 아직 못채웠으면? => 새로운 item 을 탐색한다.
            # end += 1
            
            occurrence[gems[end]] += 1
            end += 1
    
    return window
```



## Q & A

### Q1. `if end == len(gems): break` 구문을 `while` 문 맨 처음에 두었을 때 오답이 발생하는 이유와 예시는?

두 코드는 `break` 문을 포함한 **조건문의 배치 순서** 때문에 하나는 정답이 되고, 다른 하나는 오답이 됩니다. 핵심은 **조건을 만족하는 경우(윈도우 축소)를 `end` 체크보다 상위에 두어야 한다**는 점입니다.

#### 1. 에러 발생 원인
`end`가 리스트의 끝(`len(gems)`)에 도달했더라도, 현재 윈도우(`start` ~ `end`) 안에 불필요한 보석이 포함되어 있을 수 있습니다. 이때 `break`를 먼저 해버리면, **마지막으로 윈도우를 축소하여 최솟값을 갱신할 기회를 잃어버리게 됩니다.**

#### 2. 반례 예시
`gems = ["A", "A", "B", "C"]` (종류: 3개) 일 때를 가정해 봅시다.

**정상 로직 (축소 먼저 체크):**
1. `end`가 4까지 이동하여 `['A', 'A', 'B', 'C']` (길이 4)를 모두 포함합니다.
2. 루프 진입 시 `len(gem_dict) == 3` (조건 만족)을 먼저 체크합니다.
3. `start`를 이동시켜 맨 앞의 `A`를 제거합니다. → `['A', 'B', 'C']` (길이 3)
4. **최단 구간 길이 갱신 (4 → 3)** 성공.

**오류 로직 (`end` 체크 먼저):**
1. `end`가 4까지 이동하여 `['A', 'A', 'B', 'C']`를 포함합니다.
2. 루프 진입 시 `if end == 4:`를 먼저 만나서 **즉시 종료(`break`)** 됩니다.
3. 맨 앞의 `A`를 제거하는 축소 과정을 수행하지 못함.
4. **최단 구간 길이는 여전히 4**로 남게 되어 **오답** 처리됩니다.

따라서 종료 조건은 **"더 이상 확장할 수도 없고(끝 도달), 줄일 수도 없을 때(조건 불만족)"** 수행되어야 합니다.