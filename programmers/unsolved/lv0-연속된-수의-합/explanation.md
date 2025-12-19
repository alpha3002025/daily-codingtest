# 연속된 수의 합

## 문제 설명
`num`개의 연속된 정수를 더하여 `total`이 되는 수열을 반환해야 합니다.

## 풀이 개념
**등차수열의 합 공식**을 이용하거나 **평균값**을 이용하여 첫 번째 숫자를 구할 수 있습니다.

### 방법 1: 수식 유도 (추천)
연속된 `num`개의 수 중 첫 번째 수를 `x`라고 하면, 수열은 다음과 같습니다.
`x, (x+1), (x+2), ..., (x + num - 1)`

이들의 합은:
$$
\sum = \text{num} \times x + (0 + 1 + 2 + \dots + (\text{num}-1))
$$
$$
\text{total} = \text{num} \times x + \frac{\text{num} \times (\text{num}-1)}{2}
$$

따라서 첫 번째 수 `x`는 다음과 같이 구할 수 있습니다.
$$
\text{num} \times x = \text{total} - \frac{\text{num} \times (\text{num}-1)}{2}
$$
$$
x = \frac{\text{total} - \frac{\text{num} \times (\text{num}-1)}{2}}{\text{num}}
$$

### 방법 2: 평균값 중심 이용
- 연속된 수의 **평균**은 `total / num`입니다.
- 이 평균값을 기준으로 앞뒤로 숫자를 배치하면 됩니다.
- 시작 값 `x`는 `평균 - (num-1)/2` 에서 구할 수 있습니다 (단, 정수 처리에 주의).

## 코드 (Python)

```python
def solution(num, total):
    # 0 ~ num-1 까지의 합 (등차수열 합 공식의 뒷부분)
    # sum(0..n-1) = n*(n-1)/2
    d_sum = num * (num - 1) // 2
    
    # total에서 d_sum을 뺀 후 num으로 나누면 시작 값 x가 나옴
    start = (total - d_sum) // num
    
    # start부터 num개의 연속된 정수 리스트 생성
    return [i for i in range(start, start + num)]
```
<br/>


## my code (sliding window)
```python
def solution(num, total):
    biggest_n = total // num ### 가장큰수 x num 을 하는 케이스로 끝지점을 먼저 구한다.
    
    for i in range(num): ### 뒤에서부터 카운팅
        curr_range = range(biggest_n - i, biggest_n - i + num) ## 출발지점 (biggest_n -i 로부터 num개의 수를 배열)
        if sum(curr_range) == total:
            return list(curr_range)
```
