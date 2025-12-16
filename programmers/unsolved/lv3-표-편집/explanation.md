# 표 편집

## 문제 설명
`n`행의 표에서 커서를 이동하고, 행을 삭제(`C`)하거나 복구(`Z`)하는 명령어를 처리합니다.
- `U X`: 현재 위치에서 위의 행으로 X칸 이동.
- `D X`: 현재 위치에서 아래의 행으로 X칸 이동.
- `C`: 현재 행 삭제. 커서는 바로 아래 행으로. (마지막 행이었다면 바로 윗 행으로)
- `Z`: 가장 최근에 삭제된 행 복구. (현재 커서는 변하지 않음)
모든 명령 처리 후, 초기 상태와 비교하여 삭제된 행은 'X', 남은 행은 'O'로 표시한 문자열 반환.

## 문제 해결 전략

$N$이 최대 100만, 명령어가 20만 개이므로 리스트의 `pop/insert`(`O(N)`)를 사용하면 시간 초과가 납니다.
삭제/복구가 $O(1)$인 **연결 리스트(Linked List)**를 사용해야 합니다.
Python에서는 Node 클래스를 만들거나, 딕셔너리/배열을 이용해 `prev`, `next` 포인터를 관리하면 됩니다.

1. **자료구조**:
   - `up`: `up[i]`는 i번 행의 윗 행 인덱스.
   - `down`: `down[i]`는 i번 행의 아래 행 인덱스.
   - 1차원 배열로 `up[N]`, `down[N]`을 만듭니다.
   - 초기화: `up[i] = i-1`, `down[i] = i+1`. (경계값 `up[0]=-1`, `down[n-1]=-1` 등으로 처리)

2. **명령어 처리**:
   - `U X`, `D X`: 연결된 `up`/`down` 인덱스를 따라 X번 이동. $O(X)$. $X$의 합이 100만 이하일지 모르지만, 보통 이동 거리는 효율성 테스트에서 크게 작용하지 않거나, 총합이 제한적임.
   - `C`:
     - 현재 노드 `k`를 삭제. 스택에 `(k, up[k], down[k])` 저장.
     - `up[k]`의 `down`을 `down[k]`로 변경.
     - `down[k]`의 `up`을 `up[k]`로 변경.
     - 커서 이동: `down[k]`가 있으면 그리로, 없으면 `up[k]`로.
   - `Z`:
     - 스택에서 `(node, prev, next)` 꺼냄.
     - `node`를 복구.
     - `prev`가 존재하면 `down[prev] = node`.
     - `next`가 존재하면 `up[next] = node`.
     - 중요: `prev`와 `next` 노드는 삭제되지 않은 상태임이 보장됨(스택 구조상).

3. **결과 출력**:
   - 처음에 'O'가 $N$개인 배열 생성.
   - 스택에 남아있는(삭제된 채 복구 안 된) 노드들의 인덱스 위치를 'X'로 변경.

## Python 코드

```python
def solution(n, k, cmd):
    # Linked List 구현 (배열)
    up = [i - 1 for i in range(n)]
    down = [i + 1 for i in range(n)]
    # 경계 처리
    down[n - 1] = -1 
    
    deleted_stack = []
    
    # 현재 커서
    curr = k
    
    for command in cmd:
        parts = command.split()
        op = parts[0]
        
        if op == 'U':
            steps = int(parts[1])
            for _ in range(steps):
                curr = up[curr]
                
        elif op == 'D':
            steps = int(parts[1])
            for _ in range(steps):
                curr = down[curr]
                
        elif op == 'C':
            # 삭제
            prev_node = up[curr]
            next_node = down[curr]
            
            deleted_stack.append((curr, prev_node, next_node))
            
            # 연결 끊기
            if prev_node != -1: # 첫 행이 아니면
                down[prev_node] = next_node
                
            if next_node != -1: # 마지막 행이 아니면
                up[next_node] = prev_node
                
            # 커서 이동
            if next_node != -1:
                curr = next_node
            else:
                curr = prev_node
                
        elif op == 'Z':
            # 복구
            node, prev_node, next_node = deleted_stack.pop()
            
            if prev_node != -1:
                down[prev_node] = node
            
            if next_node != -1:
                up[next_node] = node
                
            # note: up[node], down[node]는 복구할 필요 없음
            # (스택에 넣은 값 그대로일 것이므로? 
            #  사실 배열값 자체는 건드리지 않았으므로 up, down 연결정보는 남아있음.
            #  하지만 안전하게 하려면 여기서 재할당할 수도 있는데, 
            #  이미 up[node]=prev_node 상태 유지됨.)
                
    # 결과 생성
    answer = ['O'] * n
    for node, _, _ in deleted_stack:
        answer[node] = 'X'
        
    return "".join(answer)
```
