# 주사위 고르기

## 문제 설명
`n`개의 주사위가 주어집니다. 각 주사위의 6개 면에는 숫자가 적혀 있습니다. A와 B는 이 중 `n/2`개씩 주사위를 나누어 가집니다. 각자 가진 주사위를 모두 굴려 나온 수의 합이 더 큰 사람이 이깁니다. A가 승리할 확률(이기는 경우의 수)이 가장 높아지도록 주사위를 골라야 합니다.

## 문제 해결 전략

주사위의 개수 `n`은 최대 10입니다. 이는 완전 탐색을 하기에 충분히 작은 수입니다.
1. **조합 생성**: A가 `n/2`개의 주사위를 고르는 모든 경우의 수는 $_{10}C_5 = 252$가지로 매우 적습니다.
2. **점수 분포 계산**: 선택된 `n/2`개의 주사위(최대 5개)를 굴렸을 때 나올 수 있는 합의 분포를 구합니다.
   - 각 주사위는 6면이므로 $6^5 = 7776$가지 경우가 있습니다. 이를 백트래킹이나 재귀로 순회하며 합의 빈도수를 계산합니다.
3. **승패 비교**:
   - A의 점수 목록과 B의 점수 목록을 비교하여 A가 이기는 횟수를 계산합니다.
   - 효율적인 계산을 위해 점수 리스트를 정렬하고 이분 탐색(bisect)을 사용하거나, 빈도수 딕셔너리를 활용하여 $O(K \times M)$ (K, M은 합의 종류 수) 시간 내에 계산합니다.

### 알고리즘 상세
1. `itertools.combinations`로 A가 5개 주사위를 갖는 모든 조합을 순회.
2. 나머지 주사위는 B가 가짐.
3. 각 조합에 대해:
   - `get_sum_distribution(dice_list)` 함수로 `{합: 개수}` 맵 생성.
   - A의 합 분포와 B의 합 분포를 이중 루프(또는 정렬 후 투포인터/이분탐색)로 비교.
   - `Wins = sum(CountA[scoreA] * CountB[scoreB] for scoreA > scoreB)`
4. 최대 `Wins`를 기록하는 조합을 반환.

## Python 코드

```python
from itertools import combinations, product
from bisect import bisect_left

def solution(dice):
    n = len(dice)
    indices = list(range(n))
    max_wins = -1
    best_comb = []
    
    # 주사위 조합에 따른 합의 분포를 구하는 함수
    def get_sums(dices):
        # product를 쓰면 6^5 = 7776을 쉽게 생성 가능
        # dice_faces = [dice[i] for i in indices_subset]
        # sums = []
        # for p in product(*dices): ...
        # 더 효율적인 방법: 딕셔너리로 {합: 개수} 관리
        
        sum_counts = {0: 1}
        for d in dices:
            new_counts = {}
            for s, c in sum_counts.items():
                for face in d:
                    new_val = s + face
                    new_counts[new_val] = new_counts.get(new_val, 0) + c
            sum_counts = new_counts
        return sum_counts

    # A가 indices_A를 가질 때 승수 계산
    for indices_A in combinations(indices, n // 2):
        indices_B = tuple(set(indices) - set(indices_A))
        
        dice_A = [dice[i] for i in indices_A]
        dice_B = [dice[i] for i in indices_B]
        
        count_A = get_sums(dice_A)
        count_B = get_sums(dice_B)
        
        # 승수 계산
        # B의 합들을 정렬된 리스트로 변환하여 누적합(prefix sum) 혹은 이분탐색 활용 가능
        # 여기서는 단순히 정렬된 keys를 순회하며 최적화
        
        sorted_B_sums = sorted(count_B.keys())
        # accumulated counts for B
        # counts_B_list[i] = (sum_val, count, accumulated_count_upto_this)
        
        wins = 0
        
        # 간단한 이중 루프 대신 최적화
        # A의 합 `a_sum`에 대해, B의 합 `b_sum < a_sum` 인 모든 경우의 수 합
        
        # B의 누적합 미리 계산
        cum_B = 0
        b_cum_list = [] # (value, accumulated_count)
        for s in sorted_B_sums:
            cum_B += count_B[s]
            b_cum_list.append((s, cum_B))
            
        for s_a, c_a in count_A.items():
            # bisect를 위해 keys만 추출하거나 직접 구현
            # b_cum_list에서 s_a보다 작은 가장 큰 값 찾기
            
            # 이분 탐색 (bisect_left 등 활용)
            # 여기서는 list가 작으므로 수동 or bisect
            # python bisect는 key 지원(3.10+)하지만 호환성 고려하여 keys 리스트 별도 생성
            
            # 그냥 파이썬 bisect 사용
            # 찾고자 하는 값: s_a (이보다 작은 값들의 누적합 필요)
            idx = bisect_left(sorted_B_sums, s_a)
            
            if idx > 0:
                wins += c_a * b_cum_list[idx-1][1]
        
        if wins > max_wins:
            max_wins = wins
            best_comb = indices_A
            
    # 결과는 1-based index, 오름차순 정렬
    return sorted([i + 1 for i in best_comb])
```
