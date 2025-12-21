# 연속된 수의 합
**방법 1) 수식 유도방식**<br/>
직접 이해해본 결과 '평균값 중심'을 이용한 풀이를 요약해보면 다음과 같다.
- n개를 더해서 total 이 되는 경우 (x+0),(x+1),(x+2),...(x+n-1) 의 수열이 된다.
- 이때 x 만 n 개로 모으고, 증분을 따로 모으면 (x+x+ ... x) + (0+1+2+...+n-1)이 된다.
- 그럼 여기서 두 번째 항인 `(0+1+2+...+n-1)` 의 합은 `(n-1)*n/2` 가 된다. 즉, 증분의 총 합은 `(n-1)*n/2` 가 된다.
- 그러면 이 증분의 합을 total 에서 빼면 total - 증분의 합 인데, 이 식의 결과값은 (x+x+ ... x) 이 된다.


즉, 결론만 정리해보면 total - 증분의 합 = K 를 통해 구한 K를 n으로 나누면 연속수열의 시작점이 된다.<br/>
<br/>

**방법 2) sliding window**<br/>
> **참고 - 2025/12/22 풀이기록 코드 확인할 것**<br/>

평균값 A = total // num 라고 할때 수의 개수를 0,1,2, ... num-1 에 대해 
- 0번째 앞에서부터 n개의 숫자의 sum 을 구해서 확인 : A-0, A-0 +1, A-0 +2, ... 
- 1번째 앞에서부터 n개의 숫자의 sum 을 구해서 확인 : A-1, A-1 +1, A-1 +2, ... 

<br/>

이렇게 반복을 하면 코드는 다음과 같이 일반화된다. 
```python
def solution(num, total):
    maybe = total // num
    
    for i in range(num):
        start = maybe - i
        end = maybe - i + num
        
        curr = sum(range(start, end))
        if curr == total:
            return list(range(start,end))
    
    answer = []
    return answer
```

<br/>
<br/>


## 문제 설명
`num`개의 연속된 정수를 더하여 `total`이 되는 수열을 반환해야 합니다.

## 풀이 개념
**등차수열의 합 공식**을 이용하거나 **평균값**을 이용하여 첫 번째 숫자를 구할 수 있습니다.


## 방법 1.수식 유도 (추천) - 평균값 중심 이용
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

## 코드 (Python)
```python
def solution(num, total):
    # 등차수열의 합 공식을 이용해 시작 값(x)을 바로 계산
    d_sum = num * (num - 1) // 2
    start = (total - d_sum) // num
    return [i for i in range(start, start + num)]
```
<br/>

### 방법 1: 구현 (평균값 중심 이용)
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

### 설명

Q. `d_sum = num * (num - 1) // 2` 의 의미는 무엇인가요?

A. 이 부분은 **연속된 정수들의 합을 구할 때, 시작 값 `x`를 제외한 나머지 "증가분"들의 합**을 계산하는 식입니다.

**1. 상세 설명**

연속된 `num`개의 정수 수열이 `start` 값 `x`로 시작한다고 가정해 봅시다.
수열은 다음과 같이 표현됩니다:
- $x$
- $x + 1$
- $x + 2$
- ...
- $x + (\text{num} - 1)$

이 모든 수의 합(`total`)을 식으로 나타내면:
$$
\text{total} = \underbrace{(x + x + \dots + x)}_{\text{num개}} + \underbrace{(0 + 1 + 2 + \dots + (\text{num}-1))}_{\text{증가분들의 합}}
$$

여기서 **두 번째 항 (증가분들의 합)**이 바로 질문하신 코드의 내용입니다.
$$
0 + 1 + 2 + \dots + (\text{num}-1) = \frac{\text{num} \times (\text{num}-1)}{2}
$$
이것은 $1$부터 $n$까지의 합 공식 $\frac{n(n+1)}{2}$에서, $n$ 대신 $\text{num}-1$을 대입한 결과와 같습니다.

**2. 코드에서의 의미**
즉, `d_sum`은 **"시작 값 `x`가 모두 0일 때의 기본 합"** (또는 오프셋의 총합)을 의미합니다.
따라서 전체 합 `total`에서 이 `d_sum`을 먼저 빼주면, 남은 값은 순수하게 `num * x`가 되므로, 이를 `num`으로 나누어 시작 값 `x`를 바로 구할 수 있습니다.

```python
start = (total - d_sum) // num
```



## 방법 3. my code (sliding window)
방법 2 를 이해하고 나니 방법 3는 조금은 브루트포스처럼 푸는 방식이구나 싶었다.<br/>

```python
def solution(num, total):
    biggest_n = total // num ### 가장큰수 x num 을 하는 케이스로 끝지점을 먼저 구한다.
    
    for i in range(num): ### 뒤에서부터 카운팅
        curr_range = range(biggest_n - i, biggest_n - i + num) ## 출발지점 (biggest_n -i 로부터 num개의 수를 배열)
        if sum(curr_range) == total:
            return list(curr_range)
```


# 문제풀이 기록

## 2025/12/22
### 방법 1. 수식 유도 (추천) - 평균값 중심 이용
```python
def solution(num, total):
    diff_sum = (num-1) * num // 2
    even_sum = total - diff_sum
    start = even_sum // num
    
    return [i for i in range(start, start+num)]
```


### 방법 2. sliding window
window 를 옮겨가면서 합을 구한다.
