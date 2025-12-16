# [PCCP 기출문제] 2번 / 퍼즐 게임 챌린지

## 문제 설명
주어진 퍼즐들을 순서대로 풀어야 하며, 각 퍼즐은 난이도(`diff`)와 소요 시간(`time_cur`)을 가집니다.
당신의 숙련도(`level`)에 따라 퍼즐을 푸는 데 걸리는 시간이 달라집니다.

- `diff <= level` : `time_cur` 시간 소요 (틀리지 않음)
- `diff > level` : `diff - level`번 틀림.
  - 틀릴 때마다 `time_cur + time_prev` 시간 소요 (`time_prev`는 이전 퍼즐 소요 시간)
  - 틀린 후 다시 풀 때 `time_cur` 시간 추가 소요
  - 즉, 총 소요 시간 = `(diff - level) * (time_cur + time_prev) + time_cur`

전체 제한 시간(`limit`) 내에 모든 퍼즐을 해결하기 위한 **숙련도(`level`)의 최솟값**을 구해야 합니다.

## 접근법 & 주요 개념

### 1. 이진 탐색 (Binary Search) / 매개 변수 탐색 (Parametric Search)
이 문제는 "조건(제한 시간 이내)을 만족하는 최솟값"을 찾는 최적화 문제입니다.
숙련도(`level`)가 높을수록 퍼즐을 푸는 전체 소요 시간은 줄어듭니다.
즉, **숙련도와 소요 시간 사이에는 반비례(단조 감소) 관계**가 성립하므로 이진 탐색을 사용할 수 있습니다.

- **탐색 범위 (Search Space)**: `1` ~ `max(diffs)`
  - 최소 숙련도는 1입니다.
  - 최대 숙련도는 퍼즐의 최대 난이도(`max(diffs)`)면 충분합니다. 그 이상이어도 소요 시간은 더 줄어들지 않기 때문입니다.
- **결정 함수 (Check Function)**: 특정 `level`일 때 총 소요 시간이 `limit` 이하인지 확인합니다.

### 2. 시간 복잡도
- 퍼즐의 개수 `n`: 최대 300,000
- 퍼즐의 최대 난이도 `max_diff`: 최대 100,000
- 이진 탐색 수행 횟수: `log(max_diff) ≈ 17`
- 각 탐색마다 전체 퍼즐을 순회하며 시간을 계산하므로 `O(n)` 소요
- **총 시간 복잡도**: `O(n * log(max_diff))`
  - 약 `300,000 * 17 ≈ 5,100,000` 연산으로, 충분히 시간 내에 해결 가능합니다.

## Python 풀이

```python
def solution(diffs, times, limit):
    def get_total_time(level):
        total_time = 0
        for i in range(len(diffs)):
            diff = diffs[i]
            time_cur = times[i]
            
            # 첫 번째 퍼즐은 항상 틀리지 않음 (diffs[0]=1 이고 level>=1 이므로)
            if i == 0:
                total_time += time_cur
                continue
            
            time_prev = times[i-1]
            
            if diff <= level:
                total_time += time_cur
            else:
                failures = diff - level
                # 틀릴 때마다 (현재 시간 + 이전 시간) 소요 + 성공 시 현재 시간
                total_time += failures * (time_cur + time_prev) + time_cur
                
        return total_time

    start = 1
    end = max(diffs)
    answer = end
    
    while start <= end:
        mid = (start + end) // 2
        
        if get_total_time(mid) <= limit:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
            
    return answer
```

### 코드 분석
1. **`get_total_time(level)` 함수**:
   - 주어진 숙련도 `level`로 모든 퍼즐을 푸는 데 걸리는 총 시간을 계산합니다.
   - 문제의 조건에 따라 `diff > level`인 경우 반복 실패에 따른 시간을 추가합니다.
2. **이진 탐색**:
   - `start`는 1, `end`는 난이도의 최댓값으로 설정합니다.
   - `mid` 값을 조절해가며 `limit` 시간 내에 가능한지 확인합니다.
   - 조건을 만족하면(`<= limit`) 더 작은 `level`도 가능한지 확인하기 위해 `end`를 줄이고(`answer` 갱신), 만족하지 않으면 `start`를 늘립니다.
