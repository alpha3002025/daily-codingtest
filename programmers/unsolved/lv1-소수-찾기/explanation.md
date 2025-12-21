# 소수 찾기

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12921)

1부터 `n` 사이에 있는 소수의 개수를 반환하세요.
(`n`은 최대 1,000,000)

## 해결 전략
`n`이 100만이므로, 각각 소수 판별하면(`O(N * sqrt(N))`) 느릴 수 있습니다.
**에라토스테네스의 체(Sieve of Eratosthenes)**를 사용해야 `O(N log log N)`으로 효율적입니다.

### 알고리즘 순서
1. `sieve` = `[True] * (n + 1)` (0, 1은 제외해도 됨)
2. `m` = `int(n ** 0.5)`
3. `i` from 2 to `m`:
    - `if sieve[i]`:
        - `i`의 배수들(`i+i`부터 `n`까지)을 `False`로 설정.
4. `sieve[2:]` 중 `True` 개수 반환.

## Python 코드

```python
def solution(n):
    # 0, 1은 소수 아님. n까지 포함해야 하므로 size=n+1
    sieve = [True] * (n + 1)
    
    # 0과 1 처리 (굳이 안하고 마지막에 슬라이싱 해도 됨)
    sieve[0] = sieve[1] = False
    
    # 2부터 sqrt(n)까지만 확인하면 됨
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            # i의 배수들을 모두 제거 (지워지지 않은 경우만)
            # i*2부터 시작해도 되지만, i*i 이전은 이미 2, 3.. 등에 의해 지워짐
            for j in range(i * i, n + 1, i):
                sieve[j] = False
                
    # True인 개수 (2부터 n까지)
    return sum(sieve)
```

## 배운 점 / 팁
- **대량의 소수 판별**: 에라토스테네스의 체는 필수 알고리즘입니다. 범위 내 소수 개수나 목록을 구할 때 가장 빠릅니다.
