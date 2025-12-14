# 격자 뒤집기 미로 문제 풀이 및 정답 코드

이 문서는 프로그래머스 Lv.4 "격자 뒤집기 미로" 문제의 풀이와 정답 코드를 포함하고 있습니다.

## 문제 분석

### 문제 개요
- **N x M 격자**: 각 칸은 양면(앞면/뒷면)에 숫자가 있습니다.
- **조작**:
    - 행(Row)을 뒤집거나, 열(Column)을 뒤집을 수 있습니다.
    - 뒤집기를 수행할 때마다 비용 `K`가 발생합니다. (단, 문제 해석상 최종 상태를 만들기 위한 뒤집기 횟수에 비례한 비용)
- **목표**: (1,1)에서 출발하여 (N,M)까지 상하좌우로 인접한 칸으로 이동하며, 방문한 칸의 숫자 합계에서 (뒤집기 총 비용)을 뺀 값을 최대화해야 합니다.
- **제약**:
    - 이미 방문한 칸은 다시 방문할 수 없습니다.
    - N은 14 이하로 매우 작습니다. (M은 최대 100)

### 핵심 아이디어

1.  **경로의 특성 (이분 그래프)**
    - 격자 그래프는 **이분 그래프(Bipartite Graph)**입니다. 체스판처럼 검은 칸과 흰 칸으로 나눌 수 있습니다.
    - **(1,1)이 검은 칸**이라고 가정하면, 상하좌우 이동 시 반드시 흰 칸으로 이동합니다.
    - **N과 M의 기우성(Parity)에 따른 방문 가능 여부**:
        - **N 또는 M 중 하나라도 홀수라면**: 전체 격자의 칸 개수는 짝수/홀수와 무관하게, 항상 모든 칸을 방문하는 경로(Hamiltonian Path)가 존재합니다. 따라서 모든 칸의 합을 얻을 수 있습니다.
        - **N과 M이 모두 짝수라면**: 전체 칸 개수는 짝수입니다. (1,1)은 검은 칸, (N,M)도 검은 칸입니다. 검은 칸에서 검은 칸으로 가는 경로의 길이는 짝수여야 하며(거쳐가는 간선 수), 이는 방문하는 정점의 개수가 홀수여야 함을 의미합니다. 그러나 전체 칸 개수는 짝수이므로, **적어도 하나의 칸은 방문하지 못하고 남겨야 합니다**.
        - 남겨지는 칸은 반드시 **흰 칸**((행+열)이 홀수인 칸)이어야 하며, 합을 최대화하기 위해 **가장 값이 작은 흰 칸** 하나를 제외하는 것이 최적입니다.

2.  **완전 탐색과 그리디의 결합**
    - **행 뒤집기 (Bitmask)**: N이 14 이하로 작으므로, 행을 뒤집는 모든 경우의 수($2^N$)를 비트마스크로 시도해볼 수 있습니다.
    - **열 뒤집기 (Greedy)**: 행 뒤집기 상태가 고정되면, 각 열은 서로 독립적으로 뒤집을지 말지 결정할 수 있습니다.
        - 각 열에 대해 '뒤집지 않았을 때의 합'과 '뒤집었을 때의 합(비용 K 차감)' 중 더 큰 이득을 취하는 것이 기본 전략입니다.
    - **N, M이 모두 짝수일 때의 예외 처리**:
        - 위 그리디 전략으로 구한 구성에서, 전체적으로 **단 하나의 흰 칸**을 제외해야 합니다.
        - 기본적으로 그리디하게 선택된 구성에서 가장 작은 흰 칸을 제외합니다.
        - 하지만, 특정 열의 선택을 최적(Max Sum)이 아닌 차선으로 바꾸더라도, 그로 인해 **훨씬 더 작은 흰 칸**을 제외할 수 있게 된다면 이득일 수 있습니다. 따라서 각 열에 대해 선택을 반대로 했을 경우도 고려하여 최댓값을 찾습니다.

## 알고리즘 단계

1.  $2^N$개의 모든 행 뒤집기 상태를 순회합니다.
2.  각 상태에 대해 비용(뒤집은 행 수 * K)을 계산합니다.
3.  각 열에 대해 두 가지 옵션(뒤집기/안 뒤집기)의 점수 합과, 해당 옵션에서의 '흰 칸들 중 최솟값'을 계산합니다.
4.  **Case 1 (N, M 중 하나라도 홀수)**: 각 열마다 점수가 더 높은 옵션을 선택하고 합산합니다.
5.  **Case 2 (N, M 모두 짝수)**:
    - 기본적으로 점수가 높은 옵션을 선택해 합산(Base Sum)합니다.
    - 선택된 옵션들에서 나오는 흰 칸들 중 전체 최솟값을 찾아 Base Sum에서 뺍니다.
    - 단, 하나의 열에 대해 선택을 바꿨을 때(점수는 손해를 보지만), 제외되는 흰 칸의 값이 더 작아져서 최종 결과가 더 커지는 경우를 모든 열에 대해 확인합니다.
6.  모든 행 뒤집기 케이스 중 최댓값을 반환합니다.

## Python 정답 코드

```python
import sys

def solution(visible, hidden, k):
    N = len(visible)
    M = len(visible[0])
    
    # N이 M보다 크다면 전치하여 N을 작게 만듭니다 (최적화)
    # 문제 제약상 N<=14이므로 필수는 아니지만, 일반성을 위해 처리
    if N > M:
        visible = [list(x) for x in zip(*visible)]
        hidden = [list(x) for x in zip(*hidden)]
        N, M = M, N

    # N과 M이 모두 짝수인지 확인 (Skip이 필요한 경우)
    need_skip = False
    if (N % 2 == 0) and (M % 2 == 0):
        need_skip = True

    max_score = -float('inf')

    # 1. 행 뒤집기 조합 순회 (Bitmask)
    for r_mask in range(1 << N):
        # 현재 행 뒤집기 비용 계산
        row_flips = bin(r_mask).count('1')
        current_k_cost = row_flips * k
        
        # 각 열(Column)에 대한 정보 계산
        # col_data[j] = (option0_sum, option1_sum, option0_min_white, option1_min_white)
        # option 0: 열 뒤집기 X
        # option 1: 열 뒤집기 O (비용 K 포함 전, 나중에 처리하거나 여기서 처리)
        # 여기서는 option1_sum에 비용 K를 미리 차감하여 저장
        col_data = []
        
        for j in range(M):
            g0 = 0 # Gain if col not flipped
            g1 = 0 # Gain if col flipped
            mw0 = float('inf') # Min white value if col not flipped
            mw1 = float('inf') # Min white value if col flipped
            
            for i in range(N):
                r_flipped = (r_mask >> i) & 1
                
                # 행이 뒤집힌 상태에 따라 현재 칸의 값 결정
                # r_flipped가 1이면 hidden이 위로, 0이면 visible이 위로
                val_no_col_flip = hidden[i][j] if r_flipped else visible[i][j]
                
                # 열까지 뒤집히면 반대가 됨
                val_col_flip = visible[i][j] if r_flipped else hidden[i][j]
                
                g0 += val_no_col_flip
                g1 += val_col_flip
                
                # 흰 칸((i+j)가 홀수)인 경우 최솟값 갱신
                if (i + j) % 2 == 1:
                    if val_no_col_flip < mw0: mw0 = val_no_col_flip
                    if val_col_flip < mw1: mw1 = val_col_flip
            
            g1 -= k # 열 뒤집기 비용 차감
            col_data.append((g0, g1, mw0, mw1))

        # 2. 열 선택 최적화
        if not need_skip:
            # 홀수 크기가 포함된 경우: 무조건 이득인 쪽 선택
            row_total = 0
            for g0, g1, _, _ in col_data:
                row_total += max(g0, g1)
            
            final_res = row_total - current_k_cost
            if final_res > max_score:
                max_score = final_res
        else:
            # 짝수 x 짝수인 경우: 흰 칸 하나를 제외해야 함
            
            # 우선 각 열에서 이득이 큰 쪽을 선택(Greedy)
            best_choices = [] # 0 or 1
            base_sum = 0
            best_min_whites = []
            
            for j in range(M):
                g0, g1, mw0, mw1 = col_data[j]
                if g0 >= g1:
                    best_choices.append(0)
                    base_sum += g0
                    best_min_whites.append(mw0)
                else:
                    best_choices.append(1)
                    base_sum += g1
                    best_min_whites.append(mw1)
            
            # 전략 A: Greedy 선택 유지, 그 중 최소 흰 칸 제외
            # (만약 Grid 내에 흰 칸이 없다면? N,M 짝수면 반드시 흰칸 존재)
            current_min_white = min(best_min_whites)
            res_A = (base_sum - current_min_white) - current_k_cost
            if res_A > max_score:
                max_score = res_A
            
            # 전략 B: 단 하나의 열에 대해 선택을 바꿈 (역전)
            # 이를 빠르게 계산하기 위해 Prefix Min, Suffix Min 활용
            
            # left_min[j]: 0~j열까지 best choice에서의 min white
            left_min = [float('inf')] * M
            curr = float('inf')
            for j in range(M):
                if best_min_whites[j] < curr: curr = best_min_whites[j]
                left_min[j] = curr
                
            # right_min[j]: j~M-1열까지 best choice에서의 min white
            right_min = [float('inf')] * M
            curr = float('inf')
            for j in range(M-1, -1, -1):
                if best_min_whites[j] < curr: curr = best_min_whites[j]
                right_min[j] = curr
                
            # 각 열 j를 반대로 선택했을 때 테스트
            for j in range(M):
                g0, g1, mw0, mw1 = col_data[j]
                chosen = best_choices[j]
                
                # 반대 선택에 의한 점수 변화
                # 원래 얻은 것(max(g0,g1))을 빼고 반대(min)를 더함
                # 즉, loss = max - min
                if chosen == 0:
                    loss = g0 - g1
                    alt_mw = mw1
                else:
                    loss = g1 - g0
                    alt_mw = mw0
                
                # 새로운 구성에서의 전체 Min White
                # min( j제외 나머지 열들의 min, j열의 새로운 min )
                neighbors_min = float('inf')
                if j > 0:
                    if left_min[j-1] < neighbors_min: neighbors_min = left_min[j-1]
                if j < M - 1:
                    if right_min[j+1] < neighbors_min: neighbors_min = right_min[j+1]
                
                final_min_white = min(neighbors_min, alt_mw)
                
                # 최종 점수 = (BaseSum - loss) - MinWhite - RowCost
                res_B = (base_sum - loss - final_min_white) - current_k_cost
                if res_B > max_score:
                    max_score = res_B

    return max_score
```
