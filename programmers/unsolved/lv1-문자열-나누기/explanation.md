# 문자열 나누기

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/140108)

문자열 `s`를 왼쪽부터 읽으며 분해합니다.
1. 첫 글자를 `x`로 정의합니다.
2. 이제부터 글자를 읽어가며 `x`와 같은 글자의 수, 다른 글자의 수를 셉니다.
3. 두 횟수가 같아지는 순간 멈추고, 지금까지 읽은 문자열을 분리합니다.
4. 남은 부분에 대해 반복합니다.
분해된 문자열의 총 개수를 반환하세요.

## 해결 전략
문제 설명 그대로 구현(Simulation)하면 됩니다.
상태를 저장할 변수 (`x`, `same_cnt`, `diff_cnt`)를 두고 문자열을 한 번 순회합니다.

### 알고리즘 순서
1. `answer` = 0
2. `x` = None (현재 기준 문자)
3. `same` = 0, `diff` = 0
4. `s` 순회 (`char`):
    - `x`가 None이면: `x = char`, `same = 1`, `x` 설정 완료.
    - `x`가 설정되어 있으면:
        - `char == x` 이면 `same += 1`
        - `char != x` 이면 `diff += 1`
    - 만약 `same == diff`:
        - 분리 발생: `answer += 1`
        - 상태 초기화: `x = None`, `same = 0`, `diff = 0`
5. 순회 끝났는데 `x`가 남아있다면(마지막 덩어리가 횟수 안 맞아도 분리):
    - `answer += 1`
6. `answer` 반환.

## Python 코드

```python
def solution(s):
    answer = 0
    
    x = None
    same_cnt = 0
    diff_cnt = 0
    
    for char in s:
        if x is None:
            x = char
            same_cnt = 1
            diff_cnt = 0 # 굳이 필요없지만 명시
            continue
            
        if char == x:
            same_cnt += 1
        else:
            diff_cnt += 1
            
        if same_cnt == diff_cnt:
            answer += 1
            x = None # 초기화하여 다음 글자가 새로 x가 되도록 함
            
    # 다 돌았는데 아직 처리 중인 덩어리가 있다면 하나로 셈
    if x is not None:
        answer += 1
        
    return answer
```

## 배운 점 / 팁
- **상태 기계(State Machine) 사고방식**: "초기 상태" -> "진행 상태" -> "조건 충족 시 초기화" 흐름을 코드로 옮기는 연습이 됩니다.
- **잔여 처리**: 반복문 종료 후 남은 데이터(마지막 조각)를 처리하는 로직을 빼먹지 않도록 주의해야 합니다.
