# 이진 변환 반복하기

## 문제 설명
0과 1로 이루어진 문자열 `s`가 주어집니다. `s`가 "1"이 될 때까지 다음 연산을 반복합니다.
1. `s`의 모든 '0'을 제거합니다.
2. 제거 후 남은 문자열의 길이 $c$를 2진법으로 표현한 문자열로 `s`를 바꿉니다.
반복 횟수와 제거된 0의 총 개수를 반환해야 합니다.

### 핵심 개념
1.  **문자열 카운팅 (`count`)**: 0의 개수를 쉽고 빠르게 셀 수 있습니다. `s.count('0')`.
2.  **길이 변환 및 이진수 변환 (`bin`)**:
    - 0을 제거한 뒤의 길이는 `len(s) - zeros`
    - 이를 이진수로 변환: `bin(length)[2:]`
3.  **반복문 (While)**: `s`가 "1"이 아닐 때까지 계속 돕니다.

## Python 풀이

```python
def solution(s):
    loop_count = 0
    removed_zeros = 0
    
    while s != "1":
        loop_count += 1
        
        # 1. 0의 개수 세기 및 제거 카운트 누적
        count_zero = s.count('0')
        removed_zeros += count_zero
        
        # 2. 0을 제거하고 남은 1의 개수 -> 길이
        length_one = len(s) - count_zero
        
        # 3. 길이를 2진수 문자열로 변환
        s = bin(length_one)[2:]
        
    return [loop_count, removed_zeros]
```

### 코드 설명
- 문자열 크기가 최대 150,000이지만, 이진 변환을 하면 길이가 로그 스케일로 급격히 줄어들기 때문에 반복 횟수는 매우 적습니다.
- `bin()` 함수의 결과인 `0b110...`에서 `0b`를 제거하기 위해 `[2:]` 슬라이싱을 합니다.


## 나의 풀이
```python
def solution(s):
    loop_count = 0
    removed_zero_cnt = 0
    
    while s != "1":
        loop_count += 1
        
        ## 0의 개수 세기, 제거된 0ㅇ의 개수 누적
        zero_cnt = s.count('0')
        removed_zero_cnt += zero_cnt
        
        ## 0 을 제거 후 남은 1의 개수 -> 길이
        length_one = len(s) - zero_cnt
        
        ## 길이를 2진수 문자열로 변환
        s = bin(length_one)[2:]
    
    return [loop_count, removed_zero_cnt]
```

