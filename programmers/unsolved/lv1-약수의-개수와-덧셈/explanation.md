# 약수의 개수와 덧셈

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/77884)

`left`부터 `right`까지의 모든 수에 대해:
- 약수의 개수가 짝수면 더하고
- 약수의 개수가 홀수면 뺍니다.
총합을 구하세요.

## 해결 전략
약수의 개수가 홀수인 수는 **완전 제곱수(Perfect Square)**뿐입니다.
(예: 4의 약수 1, 2, 4 -> 3개. 9의 약수 1, 3, 9 -> 3개)
일반적인 수는 약수가 쌍(`a * b = n`)을 이루므로 짝수 개입니다.

따라서 각 수 `i`에 대해, `sqrt(i)`가 정수인지 확인하면 됩니다.

### 알고리즘 순서
1. `answer` = 0
2. `i` from `left` to `right`:
    - `if int(i**0.5) == i**0.5`: (완전 제곱수인지)
        - `answer -= i`
    - `else`:
        - `answer += i`
3. 반환.

## Python 코드

```python
def solution(left, right):
    answer = 0
    
    for i in range(left, right + 1):
        # 제곱근이 정수이면 약수 개수가 홀수
        if int(i ** 0.5) == i ** 0.5:
            answer -= i
        else:
            answer += i
            
    return answer
```

## 배운 점 / 팁
- **수학적 성질**: 약수 개수의 홀짝성은 "제곱수인가?"와 동치임을 알면 계산 없이 O(1) 판별이 가능합니다.
