# 2차원 동전 뒤집기

## 문제 설명
$N \times M$ 크기의 2차원 공간에 동전(0: 앞면, 1: 뒷면)이 놓여 있습니다.
- 특정 행의 모든 동전을 뒤집거나, 특정 열의 모든 동전을 뒤집을 수 있습니다.
- 초기 상태 `beginning`을 목표 상태 `target`으로 만들기 위해 필요한 최소 뒤집기 횟수를 구하세요. 불가능하면 -1.

## 문제 해결 전략

$N, M$의 크기가 작습니다 (최대 10).
하지만 $2^{N+M}$은 100만이 넘어 다소 큽니다.
핵심 아이디어:
1. **순서 무관**: 행을 먼저 뒤집든 열을 먼저 뒤집든 결과는 같습니다.
2. **중복 무의미**: 같은 행/열을 2번 뒤집는 것은 0번 뒤집는 것과 같습니다. (0 또는 1번만 의미 있음)
3. **종속성**: **행을 뒤집을지 말지 결정하면, 목표를 달성하기 위해 열을 뒤집어야 하는지 여부가 자동으로 결정됩니다.**
   - 예를 들어, 모든 행의 뒤집기 여부를 고정했다고 합시다.
   - 첫 번째 열의 동전들을 `target`과 맞추려면, 해당 열을 뒤집을지 말지가 유일하게 결정됩니다. (행 상태가 고정되었으므로, 열 연산으로만 값을 맞출 수 있기 때문)
   - 각 열에 대해 필요한 조치를 취한 뒤, 전체가 `target`과 일치하는지 확인하면 됩니다.

따라서 **행에 대한 경우의 수($2^N$)만 완전 탐색**하면 됩니다. (최대 $2^{10} = 1024$가지).
각 경우에 대해 열 뒤집기 횟수를 계산하고 검증합니다.

### 알고리즘 상세
1. `beginning`과 `target`을 비교하여 차이점(`diff`)을 0(일치), 1(불일치)로 단순화할 수도 있습니다. 그냥 원본 값을 써도 됩니다.
2. 행의 뒤집기 조합을 비트마스크(0 ~ $2^N - 1$)로 순회합니다.
3. 각 비트마스크에 대해:
   - 해당 행들을 뒤집은 임시 상태를 만듭니다 (비용: 행 뒤집기 횟수).
   - 각 열을 검사합니다:
     - $j$번째 열의 모든 행이 `target`과 일치하면 OK.
     - 모든 행이 `target`과 정반대라면, 이 열을 뒤집어야 함 (비용 +1).
     - 일부는 일치하고 일부는 반대라면, 이 행 조합으로는 **불가능**한 상태.
   - 모든 열이 처리가능하다면 총 비용(`row_flips + col_flips`)을 `min_answer`와 비교 갱신.

## Python 코드

```python
def solution(beginning, target):
    n = len(beginning)
    m = len(beginning[0])
    
    min_flips = float('inf')
    
    # 각 행을 뒤집을지 말지 결정하는 모든 경우의 수 (2^n)
    for mask in range(1 << n):
        row_flips = 0
        current_map = [] # 이번 mask에 따라 뒤집힌 행 상태
        
        # 행 뒤집기 적용 및 구성
        for r in range(n):
            if mask & (1 << r): # r번째 행 뒤집기
                row_flips += 1
                row = [(1 - x) for x in beginning[r]]
            else:
                row = beginning[r][:]
            current_map.append(row)
            
        # 열 처리
        col_flips = 0
        possible = True
        
        for c in range(m):
            # c번째 열이 target의 c번째 열과 같은지 비교
            # 1. 완벽히 같은지
            is_same = True
            for r in range(n):
                if current_map[r][c] != target[r][c]:
                    is_same = False
                    break
            
            # 2. 완벽히 반대인지 (열을 뒤집으면 같아짐)
            is_diff = True
            for r in range(n):
                if current_map[r][c] == target[r][c]:
                    is_diff = False
                    break
                    
            if is_same:
                continue # 뒤집을 필요 없음
            elif is_diff:
                col_flips += 1 # 이 열을 뒤집어야 함
            else:
                possible = False # 이 행 조합으로는 해결 불가
                break
                
        if possible:
            min_flips = min(min_flips, row_flips + col_flips)
            
    return min_flips if min_flips != float('inf') else -1
```
