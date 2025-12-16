# 테이블 해시 함수

## 문제 설명
2차원 데이터 `data`가 주어집니다. 각 행은 튜플 `(col1, col2, ..., col_n)` 입니다.
1. `col`번째 컬럼의 값을 기준으로 오름차순 정렬합니다. 값이 같으면 첫 번째 컬럼(기본키) 기준 내림차순 정렬합니다.
2. 정렬된 데이터의 `row_begin`부터 `row_end`까지의 행에 대해 각 행의 `S_i`를 계산합니다.
   - `S_i`: `i`번째 행(1-based)의 모든 컬럼 값을 `i`로 나눈 나머지의 합.
3. 모든 `S_i`를 XOR한 값을 반환합니다.

## 풀이 개념
단순 **구현 및 정렬** 문제입니다.

1. **정렬**: Python의 `sort` 또는 `sorted` 함수와 lambda를 사용하여 다중 조건 정렬을 수행합니다.
   - 키: `(x[col-1], -x[0])` (오름차순, 내림차순)
2. **반복 및 연산**:
   - `row_begin`부터 `row_end`까지 반복하며 인덱스 `i`를 얻습니다. (문제는 1-based index임을 주의).
   - 각 행의 요소들을 `i`로 나눈 나머지를 더해 `S_i`를 구합니다.
   - `answer` 변수에 XOR 연산(`^`)을 누적합니다.

## 코드 (Python)

```python
def solution(data, col, row_begin, row_end):
    # 1. 정렬
    # col번째(인덱스 col-1) 기준 오름차순, 0번째 기준 내림차순
    data.sort(key=lambda x: (x[col-1], -x[0]))
    
    answer = 0
    
    # 2. S_i 계산 및 XOR
    for i in range(row_begin, row_end + 1):
        # i는 1-based index
        row_data = data[i-1]
        s_i = sum(val % i for val in row_data)
        
        answer ^= s_i
        
    return answer
```
