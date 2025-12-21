# 콜라츠 추측

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12943)

어떤 수 `num`이 주어졌을 때, 1이 될 때까지 다음 작업을 반복합니다.
1. 짝수면 2로 나눕니다.
2. 홀수면 3을 곱하고 1을 더합니다.
작업을 반복한 횟수를 반환하세요.
- 단, 500번을 반복해도 1이 되지 않으면 -1을 반환합니다.
- 처음부터 1이면 0을 반환합니다.

## 해결 전략
단순 시뮬레이션입니다. `while` 문으로 조건에 따라 `num`을 갱신하고 `count`를 증가시킵니다.
`count`가 500이 되면 중단하고 -1을 반환합니다.

### 알고리즘 순서
1. `count` = 0
2. `while num != 1`:
    - `if count == 500`: return `-1`
    - `if num % 2 == 0`: `num //= 2`
    - `else`: `num = num * 3 + 1`
    - `count += 1`
3. return `count`

## Python 코드

```python
def solution(num):
    count = 0
    
    while num != 1:
        if count >= 500:
            return -1
        
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
            
        count += 1
        
    return count
```

## 배운 점 / 팁
- **재귀 vs 반복**: 재귀로도 풀 수 있지만, 반복 깊이 제한(Recursion Limit)이나 오버헤드를 고려하면 단순 루프가 더 적절할 때가 많습니다.
