# 과제 진행하기

## 문제 설명
과제를 시작 시간과 소요 시간이 포함된 `plans` 배열로 받습니다. 
과제는 시작 시각이 되면 시작하며, 새로운 과제 시작 시각이 되면 하던 과제를 멈추고 새로운 과제를 시작합니다.
멈춘 과제는 스택에 저장되어 있다가, 현재 과제를 끝내고 다음 새로운 과제 시작까지 시간이 남으면 재개합니다.
과제를 끝낸 순서대로 이름을 배열에 담아 반환합니다.

## 풀이 개념
**스택(Stack)과 시뮬레이션** 문제입니다.

1. 시간을 분 단위 정수(`HH * 60 + MM`)로 변환하여 처리하기 쉽게 만듭니다.
2. `plans`를 시작 시간 순으로 정렬합니다.
3. 정렬된 과제들을 순회하며 `current_task`와 `next_task` 사이의 시간 간격(`time_gap`)을 계산합니다.
   - `current_task`의 소요 시간이 `time_gap`보다 작거나 같다면:
     - `current_task`를 완료합니다. (`answer`에 추가)
     - 남은 시간(`time_gap - playtime`) 동안 멈춰 둔 과제(`stack`)를 처리합니다. 스택에서 꺼내서 남은 시간만큼 수행하고, 다 끝내면 또 꺼내는 식입니다.
   - `current_task`의 소요 시간이 `time_gap`보다 크다면:
     - `time_gap`만큼만 진행하고, 남은 시간(`playtime - time_gap`)을 갱신하여 스택에 `[name, remaining_time]` 형태로 저장합니다.
4. 모든 과제 순회가 끝나면, 스택에 남아있는 과제들을 순서대로 꺼내 `answer`에 추가합니다 (LIFO).

## 코드 (Python)

```python
def convert_to_minutes(time_str):
    h, m = map(int, time_str.split(':'))
    return h * 60 + m

def solution(plans):
    # 시간을 분으로 변환하고 시작 시간 순 정렬
    parsed_plans = []
    for name, start, playtime in plans:
        parsed_plans.append([name, convert_to_minutes(start), int(playtime)])
    
    parsed_plans.sort(key=lambda x: x[1])
    
    stack = [] # 멈춘 과제들 [(name, remaining_time)]
    answer = []
    
    for i in range(len(parsed_plans) - 1):
        name, start, playtime = parsed_plans[i]
        next_start = parsed_plans[i+1][1]
        
        time_gap = next_start - start
        
        if playtime <= time_gap:
            # 현재 과제 완료
            answer.append(name)
            remain_gap = time_gap - playtime
            
            # 남은 시간 동안 멈춘 과제 수행
            while remain_gap > 0 and stack:
                prev_name, prev_rem = stack.pop()
                if prev_rem <= remain_gap:
                    # 멈춘 과제 완료
                    answer.append(prev_name)
                    remain_gap -= prev_rem
                else:
                    # 멈춘 과제 일부 수행 후 다시 스택
                    stack.append((prev_name, prev_rem - remain_gap))
                    remain_gap = 0
        else:
            # 현재 과제 다 못 끝냄, 스택에 저장
            stack.append((name, playtime - time_gap))
            
    # 마지막 과제는 무조건 완료
    answer.append(parsed_plans[-1][0])
    
    # 스택에 남은 과제들 역순으로 완료
    while stack:
        answer.append(stack.pop()[0])
        
    return answer
```


## 코드 설명

**else (현재 과제 다 못 끝낸 경우)**<br/>
- 현재 과제의 소요 시간(`playtime`)이 다음 과제 시작까지 남은 시간(`time_gap`)보다 더 긴 경우입니다.
- 다음 과제 시작 시간이 되면 무조건 하던 일을 멈춰야 하므로, 현재 과제는 완료되지 못합니다.
- 따라서, **진행한 시간(time_gap)만큼을 뺀 나머지 소요 시간**(`playtime - time_gap`)을 계산하여 스택에 보관(Push)해 둡니다. 이는 나중에 짬이 날 때 다시 꺼내서 이어서 진행하게 됩니다.


**Q : 다음 작업이 있을 때 현재 작업이 진행 중이라면 멈춰두고 다음 작업을 수행한다는 의미인가요?**<br/>
**A : 네, 맞습니다. 문제의 핵심 규칙 중 하나입니다.**<br/>
- **"과제는 시작 시각이 되면 시작해야 한다"**는 규칙이 최우선입니다.
- 만약 지금 하고 있는 과제 A가 아직 안 끝났는데, 다음 과제 B의 시작 시각이 되었다면?
  - **즉시 과제 A를 멈춥니다.**
  - 과제 A의 남은 시간(잔여량)을 기록해서 잠시 치워둡니다(스택에 저장).
  - 그리고 바로 과제 B를 시작합니다.
- 멈춰둔 과제 A는 나중에 **"다음 과제 시작 전까지 시간이 붕 뜰 때(여유 시간이 생길 때)"** 다시 꺼내서 이어서 하게 됩니다.


