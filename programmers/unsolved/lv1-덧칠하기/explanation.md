# 덧칠하기

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/161989)

길이가 `n`인 벽의 일부 구역이 칠이 벗겨졌습니다. 벗겨진 구역의 번호가 담긴 배열 `section`이 주어집니다.
길이가 `m`인 롤러로 페인트를 칠하는데, 롤러는 벽을 벗어나면 안 되며 한 번에 `m` 길이만큼 칠합니다.
최소 롤러 사용 횟수를 구하세요.

## 해결 전략
그리디(Greedy) 알고리즘을 사용합니다.
칠해야 할 구역이 나타나면, 그 구역을 시작점으로 해서 **가능한 한 멀리(`m`만큼)** 한 번에 칠해버리는 것이 가장 이득입니다.

### 알고리즘 순서
1. `answer` (횟수) = 0
2. `painted_until` = 0 (어디까지 칠해졌는지 기록하는 변수)
3. `section`의 각 구역 `target`에 대해:
    - 만약 `target`이 이미 칠해진 범위(`painted_until`보다 작거나 같음)에 있다면 넘어갑니다.
    - 칠해지지 않았다면:
        - 롤러 칠하기: `answer += 1`
        - 칠해진 범위 갱신: `painted_until = target + m - 1`
4. 최종 `answer` 반환.

## Python 코드

```python
def solution(n, m, section):
    answer = 0
    painted_until = 0  # 칠해진 마지막 위치
    
    for target in section:
        # 이미 칠해진 영역 안에 있으면 패스
        if target <= painted_until:
            continue
            
        # 칠해지지 않았다면, 여기서부터 m만큼 칠함
        answer += 1
        painted_until = target + m - 1
        
    return answer
```

## 배운 점 / 팁
- **그리디 접근법**: "현재 상황에서 가장 최선의 선택(여기서는 가장 왼쪽의 안 칠해진 곳부터 꽉 채워 칠하기)"이 전체 최적해를 보장하는 유형입니다.
- **상태 관리**: 배열을 복잡하게 조작하는 대신, `painted_until` 같은 변수 하나로 상태를 관리하면 효율적입니다.
