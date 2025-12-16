# 연속 펄스 부분 수열의 합

## 문제 설명
어떤 수열의 연속 부분 수열에 "펄스 수열"을 곱하여 얻을 수 있는 가장 큰 합을 구합니다.
펄스 수열은 [1, -1, 1, -1 ...] 또는 [-1, 1, -1, 1 ...] 형태를 가집니다.
즉, 부분 수열의 각 원소에 부호를 번갈아 가며 곱한 뒤 합을 구하는 것입니다.

## 문제 해결 전략

펄스 수열의 패턴은 두 가지입니다.
1. `[1, -1, 1, -1, ...]`
2. `[-1, 1, -1, 1, ...]`

이 두 패턴을 전체 수열에 적용한 뒤, 각각에서 **가장 큰 연속 부분 합(Maximum Subarray Sum)**을 구하면 됩니다.
가장 큰 연속 부분 합은 **카데인 알고리즘(Kadane's Algorithm)** 또는 **누적 합(Prefix Sum)**을 이용해 $O(N)$에 구할 수 있습니다.

여기서는 누적 합을 이용하는 방법이 직관적입니다.
전체 수열 `S`에 대해 1번 펄스를 적용한 수열을 `P1`이라 하면, 2번 펄스를 적용한 수열 `P2`는 `-P1`입니다.
따라서 `P1` 하나만 구해서 누적 합 배열 `prefix_sum`을 만들면,
어떤 구간 `[i, j]`의 합은 `prefix_sum[j+1] - prefix_sum[i]`입니다.
이 값이 최대가 되려면 `prefix_sum[j+1]`은 최대, `prefix_sum[i]`는 최소가 되어야 합니다.
단, `P2`의 경우는 부호가 반대이므로 절대값의 차이가 가장 큰 조합을 찾으면 됩니다.

더 간단하게는, `transformed_sequence` (1번 펄스 적용)에 대해:
1. 카데인 알고리즘으로 최대 구간 합 $Max1$ 구하기.
2. 카데인 알고리즘으로 최소 구간 합 $Min1$ 구하기.
3. 답은 `max(Max1, -Min1)`입니다. (왜냐하면 2번 펄스는 1번 펄스의 부호 반대이므로, 1번에서의 최소 합의 부호를 뒤집으면 2번에서의 최대 합이 됩니다.)

### 알고리즘 상세
1. `sequence`의 각 원소에 `1, -1, 1, -1 ...`을 곱한 `new_seq` 생성.
2. `new_seq`에 대해 DP(카데인)를 수행:
   - `dp_max[i] = max(0, dp_max[i-1]) + new_seq[i]`
   - `global_max = max(global_max, dp_max[i])`
   - `dp_min[i] = min(0, dp_min[i-1]) + new_seq[i]`
   - `global_min = min(global_min, dp_min[i])`
3. `max(global_max, -global_min)` 반환.

## Python 코드

```python
def solution(sequence):
    n = len(sequence)
    
    # 펄스 수열 적용 (1, -1, 1, -1 ...)
    p_seq = []
    pulse = 1
    for num in sequence:
        p_seq.append(num * pulse)
        pulse *= -1
        
    # 카데인 알고리즘
    # max_ending_here: 현재 위치에서 끝나는 최대 부분합
    # min_ending_here: 현재 위치에서 끝나는 최소 부분합
    
    best_max = -float('inf')
    best_min = float('inf')
    
    current_max = 0
    current_min = 0
    
    for x in p_seq:
        current_max = max(x, current_max + x)
        best_max = max(best_max, current_max)
        
        current_min = min(x, current_min + x)
        best_min = min(best_min, current_min)
        
    return max(best_max, -best_min)
```
