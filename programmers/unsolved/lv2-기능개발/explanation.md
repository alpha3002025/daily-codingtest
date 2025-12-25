# 기능개발
내생각
- Gemini 의 로직은 좀 새로웠다. 예전 풀이에 비해 조금 더 간단한 코드이지만, 약간은 배열에 대해 암산을 머릿속으로 그릴 수 있어야 한다. 예를 들면 첫 두 작업 끝나든 말든 그 다음 3번째 작업에서 이미 끝난 두 작업에 대한 카운트를 한다든가 하는 로직이다.
- 예전에 작성했던 코드도 좋은 코드다. queue 를 사용했고, 시뮬레이션으로 작성했었다.
- 다만 Gemini 의 코드가 조금 더 다른 곳에 응용가능성이 높고, 예전 풀이는 약간은 교과서처럼 개념을 완전하게 보여주는 풀이인 것 같다고 느꼈다.

<br/>

## 문제 설명
각 기능의 현재 진도율 `progresses`와 개발 속도 `speeds`가 주어집니다.
뒤에 있는 기능이 먼저 개발되어도, 앞의 기능이 배포될 때 함께 배포됩니다.
각 배포마다 몇 개의 기능이 배포되는지 순서대로 구하세요.

### 핵심 개념
1.  **소요 일수 계산**: 남은 진도가 100이 되려면 며칠이 걸리는지 계산합니다.
    - `days = ceil((100 - progress) / speed)`
    - 예: 남은 작업 30, 속도 30 -> 1일. 속도 29 -> 2일.
    - 수식: `(100 - progress + speed - 1) // speed` (올림 테크닉)
2.  **순차적 배포 (스택/큐 활용)**:
    - 앞 기능의 배포 예정일(`max_day`)보다 현재 기능의 배포일이 빠르면, 앞 기능 배포 때 같이 나갑니다.
    - 현재 기능이 더 오래 걸리면, 앞 기능들 먼저 내보내고(배포 그룹 확정), 새로운 배포 그룹(`max_day` 갱신)을 시작합니다.

## Python 풀이

```python
import math

def solution(progresses, speeds):
    answer = []
    
    # 1. 각 기능별 배포 가능일까지 남은 일수 계산
    days_left = []
    for p, s in zip(progresses, speeds):
        # 올림 계산: (목표 - 현재 + 속도 - 1) // 속도
        # 또는 math.ceil((100 - p) / s)
        day = math.ceil((100 - p) / s)
        days_left.append(day)
        
    # 예: days_left = [7, 3, 9]
    # 7일 걸리는 기능 배포 때 3일 걸리는 것도 같이 나감 (2개)
    # 9일 걸리는 기능은 따로 나감 (1개)
    
    # 2. 배포 그룹 묶기
    if not days_left:
        return []
        
    prev_max = days_left[0]
    count = 1
    
    for i in range(1, len(days_left)):
        curr = days_left[i]
        
        if prev_max >= curr:
            # 앞 기능보다 빨리 끝나거나 같이 끝나면 묶음 배포
            count += 1
        else:
            # 앞 기능보다 오래 걸리면, 앞 그룹 정산하고 새로 시작
            answer.append(count)
            prev_max = curr
            count = 1
            
    # 마지막 그룹 추가
    answer.append(count)
    
    return answer
```
<br/>
<br/>


### 코드 설명
- `zip`을 이용해 두 리스트를 묶어서 순회합니다.
- `prev_max`는 현재 배포 그룹에서 가장 오래 걸리는 작업의 일수입니다. 이 값보다 작거나 같은 작업들은 모두 함께 배포됩니다.
- 새로운 `prev_max`보다 큰 값이 나오면, 지금까지 모은 `count`를 `answer`에 넣고 초기화합니다.


<br/>
<br/>


## 또 다른 Python 풀이 (시뮬레이션)
```python
from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    answer = []
    curr_time = 0
    curr_task = 0
    while progresses:
        if progresses[0] + (curr_time * speeds[0]) >= 100:
            progresses.popleft()
            speeds.popleft()
            curr_task += 1
        else:
            if curr_task != 0:
                answer.append(curr_task)
                curr_task = 0
            curr_time += 1
    
    answer.append(curr_task)
    
    return answer
```