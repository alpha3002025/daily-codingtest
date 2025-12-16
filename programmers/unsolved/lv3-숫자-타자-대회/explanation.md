# 숫자 타자 대회

## 문제 설명
숫자 키패드(3x4)에서 두 엄지손가락으로 숫자를 타이핑합니다.
- 초기 위치: 왼손 4, 오른손 6.
- 이동 가중치:
  - 제자리: 1
  - 상하좌우 인접: 2
  - 대각선 인접: 3
  - 그 외: 인접 이동의 합으로 봅니다(직선 거리가 아님). 사실상 유클리드 거리나 맨해튼 거리가 아니라, 문제에서 정의한 그래프 가중치입니다.
  - 문제의 예시를 보면, (0,0)에서 (0,2)로 가는 가중치는 2+2=4 가 아니라 최적 경로로 계산해야 합니다. 하지만 여기서 '인접하지 않은 곳은 최소 경로 가중치 합'이라 했으므로, BFS로 미리 모든 키 간의 거리를 구해두는 것이 좋습니다.

목표: 주어진 숫자 문자열을 타이핑하는 최소 가중치 합.
제약: 두 손가락은 같은 키 위에 있을 수 없습니다.

## 문제 해결 전략

**다이나믹 프로그래밍(DP)** 문제입니다.
숫자 문자열의 길이가 최대 10만입니다.
상태 정의: `dp[index][left_pos][right_pos]`
- `index`: 눌러야 할 숫자의 인덱스
- `left_pos`, `right_pos`: 현재 왼손, 오른손 위치

하지만 $N$이 크므로 3차원 배열을 다 채우는 `N * 10 * 10`은 가능하지만, 공간 복잡도를 줄일 수 있습니다.
다음 숫자를 누를 때, 왼손 아니면 오른손이 그 숫자로 이동합니다. 즉, 다음 상태에서 손가락 중 하나는 무조건 `target_num`입니다.
따라서 상태를 `dp[index][other_pos]` (눌린 손가락 이외의 다른 손가락 위치)로 줄일 수 있습니다.
- 현재 누를 숫자가 `num`이고, 이전 단계에서 다른 손가락이 `pos`에 있었다면,
- 직전 상태는 `(target_prev, pos)` 였을 것입니다. (`target_prev`는 `index-1`번째 숫자)
- 여기서 `num`을 누르려면:
  1. `target_prev`에 있던 손이 `num`으로 이동 -> 비용 `cost(target_prev, num)`. 새 상태 `(num, pos)`
  2. `pos`에 있던 손이 `num`으로 이동 -> 비용 `cost(pos, num)`. 새 상태 `(num, target_prev)`

하지만 이렇게 하면 단순히 `left`, `right` 구분이 모호해지므로, 그냥 `dp[index][left][right]` 관점에서 생각하되, `left`나 `right` 중 하나는 반드시 `numbers[index]`가 됨을 이용합니다.
더 정확히는, `dp[index][right_pos]` = 왼손이 `numbers[index]`에 있고 오른손이 `right_pos`에 있을 때의 최소 비용. (왼손으로 눌렀을 경우)
그리고 `dp[index][left_pos]` = 오른손이 `numbers[index]`에 있고 왼손이 `left_pos`에 있을 때의 최소 비용. (오른손으로 눌렀을 경우)
이렇게 두 가지 테이블을 관리하거나, `Dictionary`를 이용해 `dp[(left, right)] = cost` 형태로 관리하는 것이 편합니다.

### 거리 계산
키패드 좌표를 `(r, c)`로 매핑하고, 미리 모든 쌍 `(from, to)`에 대한 비용을 계산해둡니다.
- 거리 가중치가 단순 유클리드 등과 다르므로, 문제 조건(인접 2, 대각선 3, 제자리 1)에 맞춰 BFS 혹은 Floyd-Warshall로 전처리합니다. (키패드가 작으므로 하드코딩이나 BFS나 비슷)

## Python 코드

```python
import sys
# 재귀 한도 해제 (필요시)
sys.setrecursionlimit(200000)

def solution(numbers):
    # 키패드 좌표
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # * 0 #
    # 0~9 번호의 좌표
    coords = {
        '1':(0,0), '2':(0,1), '3':(0,2),
        '4':(1,0), '5':(1,1), '6':(1,2),
        '7':(2,0), '8':(2,1), '9':(2,2),
        '0':(3,1)
    }
    
    # 비용 미리 계산 (BFS 불필요, 단순 계산 가능)
    # 하지만 문제 정의상 "최소 경로 가중치 합"이므로 
    # (1->3) 은 (1->2->3) 비용 2+2=4.
    # (1->9) 는 (1->5->9) 대각선 3+3=6.
    # 이를 위해 하드코딩보다 로직이 낫음.
    
    dist = [[1e9]*10 for _ in range(10)]
    
    def get_cost(src, dst):
        if src == dst: return 1
        r1, c1 = coords[str(src)]
        r2, c2 = coords[str(dst)]
        
        dr, dc = abs(r1-r2), abs(c1-c2)
        min_diff = min(dr, dc)
        max_diff = max(dr, dc)
        
        # 대각선 이동(3)을 최대한 많이 하고, 나머지는 직선 이동(2)
        # 대각선 횟수: min_diff
        # 직선 횟수: max_diff - min_diff
        return min_diff * 3 + (max_diff - min_diff) * 2

    # dist 배열 채우기
    for i in range(10):
        for j in range(10):
            dist[i][j] = get_cost(i, j)
            
    # DP
    # 현재 단계에서 (손1, 손2) 위치에 도달하는 최소 비용
    # 초기: (4, 6), 비용 0
    current_states = {(4, 6): 0}
    
    for char in numbers:
        num = int(char)
        next_states = {}
        
        for (left, right), cost in current_states.items():
            # 목표 숫자를 누를 때 같은 손가락 위에 있으면 안 됨
            # 1. 왼손 이동
            if right != num: # 오른손과 겹치지 않아야 함
                new_cost = cost + dist[left][num]
                # 상태: (num, right) 
                # (항상 left < right 로 정렬해서 키를 줄일 수도 있지만, 
                # 손가락 구분(L/R)이 없으면 안됨. 초기엔 4(L), 6(R)임.
                # 그러나 문제에서 어느 손인지 중요하지 않고 위치 조합만 중요함.
                # 단, 시작 위치가 고정이라 L/R 구분됨. 여기선 그냥 (left, right) 유지)
                
                # 최솟값 갱신
                if (num, right) not in next_states or next_states[(num, right)] > new_cost:
                    next_states[(num, right)] = new_cost
                    
            # 2. 오른손 이동
            if left != num:
                new_cost = cost + dist[right][num]
                if (left, num) not in next_states or next_states[(left, num)] > new_cost:
                    next_states[(left, num)] = new_cost
                    
        current_states = next_states
        
    return min(current_states.values())
```
