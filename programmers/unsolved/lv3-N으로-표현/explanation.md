# N으로 표현

## 문제 설명
숫자 `N`과 사칙연산만 사용하여 `number`를 표현할 때, `N` 사용 횟수의 최솟값을 구하세요.
최솟값이 8보다 크면 -1을 return 합니다.

## 문제 해결 전략

**다이나믹 프로그래밍 (Set DP)**.
`dp[i]` = `N`을 `i`번 사용해서 만들 수 있는수들의 집합.
`dp[i]`는:
1. `NN...N` (N이 i번 반복되는 숫자)
2. `dp[j]`와 `dp[i-j]`의 사칙연산 조합 (`+`, `-`, `*`, `/`) (for `j` in `1` ~ `i-1`)

## Python 코드

```python
def solution(N, number):
    if N == number:
        return 1
        
    s = [set() for _ in range(9)] # 1 ~ 8 use
    
    for i in range(1, 9):
        # 1. N, NN, NNN...
        s[i].add(int(str(N) * i))
        
        # 2. 사칙연산 (j, i-j)
        for j in range(1, i):
            for op1 in s[j]:
                for op2 in s[i-j]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
                        
        if number in s[i]:
            return i
            
    return -1
```
