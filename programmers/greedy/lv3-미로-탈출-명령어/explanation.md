# 미로 탈출 명령어

## 1. 문제 설명
- **문제 링크**: [https://school.programmers.co.kr/learn/courses/30/lessons/150365](https://school.programmers.co.kr/learn/courses/30/lessons/150365)
- **정보**:
  - $n \times m$ 크기의 격자.
  - 출발점 $(x, y)$에서 도착점 $(r, c)$로 이동.
  - 총 이동 거리가 정확히 $k$여야 함.
  - 탈출 경로는 "사전 순으로 가장 빠른 경로"여야 함.
  - 명령어: `d`(아래), `l`(왼쪽), `r`(오른쪽), `u`(위). 사전 순서는 `d < l < r < u`.
  - 불가능하면 `"impossible"` 반환.

---

## 2. 접근법 및 핵심 개념 (Greedy + Manhattan Distance)

### 개념 1: 사전 순으로 가장 빠른 경로 (Greedy)
모든 경로를 다 탐색(DFS/BFS)한 뒤 정렬하는 것은 비효율적입니다(시간 초과 가능성 큼).
우리는 $k$번의 이동을 순차적으로 결정할 때, 매 단계마다 사전 순으로 가장 앞선 방향(`d` -> `l` -> `r` -> `u`)을 우선적으로 선택해야 합니다. 선택한 방향으로 이동했을 때 남은 거리 내에 도착점에 도달할 수만 있다면, 그 선택은 무조건 **최적**입니다.

### 개념 2: 도달 가능성 판별 (Manhattan Distance & Parity)
현재 위치에서 도착점까지 갈 수 있는지 여부는 **맨해튼 거리(Manhattan Distance)**를 이용해 판단합니다.
- `남은 거리` ($k - \text{현재 이동 횟수}$) $\ge$ `현재 위치에서 목표까지의 최단 거리` ($|r - curr\_x| + |c - curr\_y|$) 이어야 합니다.
- 또한, 격자 공간에서 왔던 길을 되돌아가는 등 헛걸음을 하더라도, 소모되는 거리는 항상 2의 배수입니다. 따라서 `(남은 거리 - 최단 거리)`는 반드시 **짝수**여야 합니다 (Parity Check).

---

## 3. Python 풀이

이 문제는 탐색보다는 그리디(Greedy) 방식이 훨씬 효율적입니다.

### 코드

```python
import sys

# 재귀 깊이 제한 해제 (DFS 사용할 경우 필요하나, 여기서는 반복문 사용)
sys.setrecursionlimit(10**5)

def solution(n, m, x, y, r, c, k):
    # 1. 초기 가능성 체크
    # 최단 거리 계산
    dist = abs(x - r) + abs(y - c)
    
    # 남은 거리가 최단 거리보다 작거나, 홀짝성(Parity)이 맞지 않으면 이동 불가
    if k < dist or (k - dist) % 2 != 0:
        return "impossible"
    
    # 2. 그리디 탐색
    # 사전 순서: d (하) -> l (좌) -> r (우) -> u (상)
    answer = ""
    # 현재 위치
    cx, cy = x, y
    
    # 총 k번 이동
    for i in range(k):
        # 이번 단계에서 남은 이동 횟수 
        # (이번 턴을 포함해서 k-i번 남았다고 볼 수도 있으나, 
        #  일단 한 칸 이동 후 남은 거리를 계산하기 위해 루프 내에서 처리)
        
        # d (아래) 시도
        if (ks := k - 1 - i) >= abs(cx + 1 - r) + abs(cy - c): # 이동 후 남은 턴 >= 이동 후 위치에서 도착점까지 거리
            cx += 1
            answer += "d"
            continue
        
        # l (왼쪽) 시도
        if (ks := k - 1 - i) >= abs(cx - r) + abs(cy - 1 - c):
            cy -= 1
            answer += "l"
            continue
            
        # r (오른쪽) 시도
        if (ks := k - 1 - i) >= abs(cx - r) + abs(cy + 1 - c):
            cy += 1
            answer += "r"
            continue
            
        # u (위) 시도
        # 위 3가지가 안 되었다면 u로 가야하며, 초기 체크를 통과했으므로 반드시 가능함
        cx -= 1
        answer += "u"
        
    return answer
```

### 코드 분석 (개선된 방식)
위 코드는 약간의 비효율이 있을 수 있습니다. 예를 들어 매번 조건을 체크합니다. 
좀 더 직관적인 조건 로직을 적용하면 다음과 같습니다.

1. **사전 순서대로 우선권 부여**: `d`, `l`, `r`, `u` 순서로 리스트를 만듭니다.
2. 각 방향으로 한 칸 움직였을 때, `남은 횟수`로 도착점에 도달 가능한지 체크합니다.
   - `도달 가능 조건`: `abs(nx - r) + abs(ny - c) <= (k - 1 - 현재단계)`
   - 홀짝성은 초기 1회만 체크하면 이후에는 항상 유지됩니다 (한 칸 이동 시 거리 1 변화, 남은 턴 1 감소 -> 차이의 홀짝성은 불변).
3. 가능한 첫 번째 방향을 선택하고 바로 다음 단계(Next Iteration)로 넘어갑니다 `continue`.

### 최적화된 코드

```python
def solution(n, m, x, y, r, c, k):
    # 도착점까지의 최단 거리
    manhattan = abs(x - r) + abs(y - c)
    
    # 1. 불가능한 경우 빠른 종료
    if manhattan > k or (k - manhattan) % 2 != 0:
        return "impossible"
    
    answer = []
    
    # 2. 이동 반복
    for _ in range(k):
        # 아래(d)로 갈 수 있는지 확인
        # (현 위치에서 아래로 갔을 때, 남은 걸음 수(k-1)로 도착 가능?)
        if x < n and abs(x + 1 - r) + abs(y - c) <= k - 1:
            x += 1
            answer.append("d")
        # 왼쪽(l)
        elif y > 1 and abs(x - r) + abs(y - 1 - c) <= k - 1:
            y -= 1
            answer.append("l")
        # 오른쪽(r)
        elif y < m and abs(x - r) + abs(y + 1 - c) <= k - 1:
            y += 1
            answer.append("r")
        # 위(u)
        else:
            x -= 1
            answer.append("u")
        
        # 남은 이동 횟수 감소
        k -= 1
        
    return "".join(answer)
```
> **Tip**: 좌표가 1-based index (1~n, 1~m)이므로 경계 체크 시 주의해야 합니다 (`x < n`, `y > 1` 등).

---

## 4. 복잡도 분석
- **시간 복잡도**: $O(k)$
  - 정확히 $k$번 루프를 돌며, 각 루프 내부에서 상수 시간($O(1)$)의 연산을 수행합니다.
  - $k$는 최대 2,500이므로 매우 빠릅니다.
- **공간 복잡도**: $O(k)$
  - 정답 문자열의 길이가 $k$입니다.

## 5. 주의사항
- **좌표 체계**: 문제에서 주어지는 좌표는 $(1, 1)$부터 시작합니다. 배열 인덱스(0부터 시작)와 혼동하지 않도록 주의하거나, 입력값을 그대로 사용하는 것이 좋습니다.
- **문자열 연결**: Python에서 문자열 `+=` 연산도 빠르지만, 리스트 `append` 후 `join`하는 것이 더 관습적으로 권장됩니다.
