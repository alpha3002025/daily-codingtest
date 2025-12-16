# 파괴되지 않은 건물

## 문제 설명
$N \times M$ 격자(`board`)에 건물의 내구도가 주어집니다.
`skill` 배열을 통해 건물들에 공격(내구도 감소)하거나 회복(내구도 증가)합니다.
`skill`은 `[type, r1, c1, r2, c2, degree]` 형태로 주어지며, `(r1, c1)`부터 `(r2, c2)`까지의 직사각형 영역에 `degree`만큼 영향을 줍니다.
- `type=1`: 공격 (감소)
- `type=2`: 회복 (증가)

모든 스킬 처리 후 내구도가 1 이상인 건물의 개수를 구하세요.

## 문제 해결 전략

$N, M$은 최대 1000, `skill` 개수는 최대 25만입니다.
단순히 `skill` 루프($K$)마다 2차원 영역($N \times M$)을 업데이트하면 $O(K \times N \times M)$이 되어 시간 초과가 발생합니다($25만 \times 1000 \times 1000 \approx 2500억$).
따라서 **$O(K + N \times M)$** 알고리즘이 필요합니다.
이를 위해 **2차원 누적합(Difference Array / Imos법)**을 사용합니다.

1. **차분 배열(Difference Array) 생성**:
   - `(N+1) x (M+1)` 크기의 `diff` 배열을 만듭니다.
   - `type=1`은 `-degree`, `type=2`는 `+degree`로 간주합니다.
   - `(r1, c1)` ~ `(r2, c2)`에 `val`을 더하고 싶다면:
     - `diff[r1][c1] += val`
     - `diff[r1][c2+1] -= val`
     - `diff[r2+1][c1] -= val`
     - `diff[r2+1][c2+1] += val`

2. **누적합 계산**:
   - 모든 스킬 처리가 끝나면, `diff` 배열에 대해 행 방향 누적합, 그 다음 열 방향 누적합(순서 무관)을 수행합니다.
   - 이렇게 하면 `diff[i][j]`에는 해당 위치에 적용된 변화량의 총합이 저장됩니다.

3. **결과 합산**:
   - 원본 `board[i][j]`에 `diff[i][j]`를 더합니다.
   - 결과가 1 이상인 셀을 카운트합니다.

## Python 코드

```python
def solution(board, skill):
    n = len(board)
    m = len(board[0])
    
    # 누적합을 위한 차분 배열 (padding +1)
    diff = [[0] * (m + 1) for _ in range(n + 1)]
    
    for type, r1, c1, r2, c2, degree in skill:
        val = -degree if type == 1 else degree
        
        diff[r1][c1] += val
        diff[r1][c2+1] -= val
        diff[r2+1][c1] -= val
        diff[r2+1][c2+1] += val
        
    # 행 방향 누적합
    for i in range(n):
        for j in range(m):
            diff[i][j+1] += diff[i][j]
            
    # 열 방향 누적합
    for j in range(m):
        for i in range(n):
            diff[i+1][j] += diff[i][j]
            
    # 결과 계산
    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] + diff[i][j] > 0:
                answer += 1
                
    return answer
```
