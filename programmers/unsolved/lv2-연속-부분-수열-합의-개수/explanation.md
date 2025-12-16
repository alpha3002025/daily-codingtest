# 연속 부분 수열 합의 개수

## 문제 설명
원형 수열의 연속 부분 수열 합으로 만들 수 있는 수의 개수를 구합니다.
원형 수열이란 시작과 끝이 연결된 수열입니다.
길이가 1인 연속 부분 수열부터 길이가 n인 연속 부분 수열까지의 모든 합의 중복을 제거한 개수를 반환합니다.

## 풀이 개념
**슬라이딩 윈도우** 혹은 **단순 반복문**을 사용합니다.
원형 수열을 처리하기 위해 수열을 두 배로 늘려(`elements * 2`) 선형 수열처럼 다루면 인덱스 처리가 편해집니다.

1. `elements` 리스트 뒤에 `elements`를 한번 더 붙입니다. (길이 `2*n`)
2. 길이 1부터 `n`까지의 부분 수열 합을 구합니다.
   - 2중 반복문을 사용하여 각 시작점 `i`에 대해 길이 `length`만큼 더합니다.
   - 하지만 단순히 3중 반복문(길이, 시작점, 합)을 쓰면 O(N^3)이 될 수 있습니다 (N=1000이면 10억, 위험).
   - 더 효율적인 방법: 시작점 `i`에서 길이를 1씩 늘려가며 합을 갱신하면 O(N^2)로 가능합니다.
3. 구한 합들을 `Set`에 넣어 중복을 제거하고, `len(Set)`을 반환합니다.

## 코드 (Python)

```python
def solution(elements):
    n = len(elements)
    extended_elements = elements * 2
    sums = set()
    
    # 시작 위치
    for i in range(n):
        current_sum = 0
        # 부분 수열의 길이 (1 ~ n)
        for length in range(n):
            current_sum += extended_elements[i + length]
            sums.add(current_sum)
            
    return len(sums)
```
