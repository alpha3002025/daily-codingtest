# 연속된 부분 수열의 합

## 문제 설명
오름차순으로 정렬된 수열 `sequence`와 정수 `k`가 주어집니다.
이 수열의 부분 수열 중 합이 `k`인 것을 찾으려 합니다.
여러 개인 경우 다음 조건에 따라 하나를 선택합니다:
1. 길이가 가장 짧은 것.
2. 길이가 같다면 시작 인덱스가 가장 작은 것.
결과로 `[시작 인덱스, 끝 인덱스]`를 반환합니다.

## 풀이 개념
**투 포인터 (Two Pointers)** 알고리즘을 사용합니다.
주어진 수열이 오름차순으로 정렬된 자연수들로 구성되어 있으므로, 구간의 길이를 늘리면 합이 커지고 줄이면 합이 작아지는 성질을 이용할 수 있습니다.

1. `left`, `right` 두 포인터를 0에서 시작합니다. `current_sum`은 `sequence[0]`으로 초기화합니다.
2. `right`가 수열 끝에 도달하기 전까지 반복합니다:
   - `current_sum < k`: 합이 부족하므로 `right`를 오른쪽으로 이동시켜 더합니다.
   - `current_sum > k`: 합이 초과하므로 `left`를 오른쪽으로 이동시켜 빼줍니다.
   - `current_sum == k`: 조건을 만족합니다.
     - 현재 발견한 구간 `[left, right]`의 길이가 기존에 찾은 최소 길이보다 짧다면 정답을 갱신합니다.
     - (길이가 같을 경우, 앞쪽부터 탐색하므로 굳이 갱신하지 않아도 "시작 인덱스가 작은 것" 조건이 자연스럽게 유지됩니다. 단, 뒤쪽에서 같은 길이의 해가 나올 수 있으므로 갱신 조건은 `<`를 사용합니다.)
     - 다음 탐색을 위해 `left`를 이동시켜 합을 줄이고 계속 진행합니다 (또는 `current_sum -= sequence[left]; left += 1`).

## 코드 (Python)

```python
def solution(sequence, k):
    n = len(sequence)
    left = 0
    right = 0
    current_sum = sequence[0]
    
    # 최라 정답을 저장할 변수 [start, end, length]
    # 초기값은 가장 긴 길이보다 큰 값으로 설정
    best_range = [0, 0, float('inf')]
    
    while right < n:
        if current_sum < k:
            right += 1
            if right < n:
                current_sum += sequence[right]
        elif current_sum > k:
            current_sum -= sequence[left]
            left += 1
        else: # current_sum == k
            # 현재 구간이 기존 최적 구간보다 짧으면 갱신
            if (right - left + 1) < best_range[2]:
                best_range = [left, right, right - left + 1]
            
            # 다음 탐색을 위해 left 이동
            current_sum -= sequence[left]
            left += 1
            
    return [best_range[0], best_range[1]]
```
