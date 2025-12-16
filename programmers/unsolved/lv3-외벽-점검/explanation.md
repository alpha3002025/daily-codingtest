# 외벽 점검

## 문제 설명
외벽의 길이 `n`, 취약 지점 `weak` (원형으로 배치), 친구들의 이동 거리 `dist`가 주어집니다.
친구들을 투입하여 모든 `weak` 지점을 점검할 때, 투입해야 하는 최소 친구 수를 구하세요.
(시계/반시계 이동 가능하지만, 사실 원형을 펼쳐서 한 방향으로만 생각해도 모든 케이스 커버 가능)

## 문제 해결 전략

$N$은 최대 200이지만 `weak` 개수는 최대 15개, `dist` 개수(친구 수)는 최대 8명입니다.
매우 작은 제약조건이므로 **완전 탐색 (Permutation)**이 가능합니다.

1. **원형 -> 선형 변환**:
   - 원형을 처리하기 쉽게 `weak` 배열을 2배로 늘립니다.
   - 예: `[1, 5, 6, 10]`, `n=12` -> `[1, 5, 6, 10, 13, 17, 18, 22]`
   - 이제 길이 `len(weak)`인 모든 연속된 구간(윈도우)을 검사하면 모든 시작점을 고려할 수 있습니다.

2. **친구 순서 순열 (Permutations)**:
   - 친구를 투입하는 순서에 따라 커버 거리가 달라지므로 `dist`의 순열을 구합니다.
   - $8! = 40320$, 충분히 작음.

3. **탐색**:
   - 각 시작점(`weak`의 각 원소)에 대해:
     - 각 친구 순열에 대해:
       - 친구들을 한 명씩 투입하며 어디까지 커버 가능한지 확인.
       - 모든 취약점이 커버되면 그때의 친구 수를 기록(최소 갱신).

## Python 코드

```python
from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    # 원형을 선형으로 (2배 확장)
    weak_linear = weak + [w + n for w in weak]
    
    min_cnt = float('inf')
    
    # 1. 시작점 설정 (0 ~ length-1)
    for start in range(length):
        # 이번에 점검해야 할 취약점들: start부터 start+length-1 까지
        # 실제 값: weak_linear[start] ... weak_linear[start + length - 1]
        
        # 2. 친구 투입 순서 결정
        for friends in permutations(dist):
            cnt = 1 # 투입 친구 수
            pos = weak_linear[start] + friends[cnt-1] # 첫 친구의 커버 한계
            
            # 취약점 순회
            for index in range(start, start + length):
                # 현재 친구로 커버 안 되는 지점이 나오면
                if weak_linear[index] > pos:
                    cnt += 1 # 다음 친구 투입
                    if cnt > len(dist): # 친구 다 씀
                        break
                    pos = weak_linear[index] + friends[cnt-1] # 새 친구 커버 시작
                    
            if cnt <= len(dist):
                min_cnt = min(min_cnt, cnt)
                
    if min_cnt == float('inf'):
        return -1
    return min_cnt
```
