# 프로그래머스 - 서버 증설 횟수 (389479)


## 개념 설명 코드
```python
def solution(players, m, k):
    answer = 0
    ## 0시 ~ 23시
    server_status = [0] * 24
    
    for i in range(24):
        ## 현재 접속 사용자 수에 대해 m명당 1개의 서버를 배치할때 필요한 서버의 수
        required_cnt = players[i] // m
        
        ## 현재 서버의 수가 필요한 서버의 수(=required_cnt)를 넘어설 경우
        if server_status[i] < required_cnt:
            diff = required_cnt - server_status[i]
            answer += diff
            
            ## k 시간 동안 증설한 서버의 수를 +
            ## 범위 : i ~ i+k-1
            for j in range(i, min(i+k, 24)):
                server_status[j] += diff
    
    return answer
```



## 1. 문제 분석
- **목표**: 24시간 동안 사용자 수에 따라 서버를 증설해야 할 때, 총 증설된 서버의 횟수를 구해야 합니다.
- **규칙**:
  - 특정 시간대의 사용자 수가 `m`명 늘어날 때마다 서버 1대가 추가로 필요합니다.
  - 즉, 사용자 수가 `n * m`명 이상 `(n + 1) * m`명 미만이면, 최소 `n`대의 증설 서버가 필요합니다. (`needed = players[t] // m`)
  - 한 번 증설된 서버는 `k`시간 동안 유지된 후 반납됩니다.

## 2. 알고리즘 및 구현
- **접근 방식**: 그리디 (Greedy) & 시뮬레이션
- **설명**:
  1. 0시부터 23시까지 순차적으로 시간(`i`)을 확인합니다.
  2. 현재 시간(`i`)에 필요한 총 증설 서버 수(`required`)를 계산합니다.
  3. 현재 운영 중인 증설 서버 수(`server_status[i]`)가 `required`보다 적으면, 부족한 만큼(`diff`) 서버를 추가합니다.
  4. 서버를 추가하면 `answer`에 `diff`를 더하고, 현재 시간부터 `k`시간 동안(`i` ~ `i+k-1`) 운영될 것이므로 해당 구간의 `server_status` 값을 `diff`만큼 증가시킵니다.
     - 단, 24시를 넘어가는 부분은 고려할 필요가 없으므로 인덱스 범위를 `min(i + k, 24)`로 제한합니다.

## 3. 코드 설명

```python
def solution(players, m, k):
    answer = 0
    # 각 시간대별(0~23시) 현재 운영 중인 증설 서버의 수를 기록할 리스트
    server_status = [0] * 24
    
    for i in range(24):
        # 현재 시간대(i)의 사용자 수에 따른 필요 증설 서버 수 계산
        # 예: players[i]=5, m=3 이면 1대 필요
        required = players[i] // m
        
        # 현재 운영 중인 서버가 필요량보다 적다면 증설 필요
        if server_status[i] < required:
            diff = required - server_status[i] # 부족한 서버 수
            answer += diff # 총 증설 횟수 누적
            
            # 증설된 서버는 i시부터 k시간 동안 유지됨
            # 범위: i ~ i+k-1 (단, 24시를 넘지 않도록 제한)
            for j in range(i, min(i + k, 24)):
                server_status[j] += diff
                
    return answer
```

### 예제 시뮬레이션
만약 `players`가 `[..., 10, ...]`이고 `m=4`, `k=2`라고 가정합시다.
- 해당 시간에 필요한 서버 수: `10 // 4 = 2`대
- 만약 이전에 증설되어 아직 운영 중인 서버가 1대라면, `2 - 1 = 1`대를 추가로 증설합니다.
- 이 1대는 현재 시간과 다음 시간(총 2시간) 동안 `server_status`에 더해져, 다음 시간대의 계산에도 영향을 미칩니다.

## 4. 복잡도
- **시간 복잡도**: `O(T * k)` (여기서 `T=24`)
  - 24시간을 순회하며 매번 최대 `k`시간만큼 값을 업데이트합니다. `T`와 `k`가 매우 작으므로 사실상 `O(1)`에 가깝습니다.
- **공간 복잡도**: `O(T)`
  - 24시간의 상태를 저장하는 배열 하나만 사용합니다.


