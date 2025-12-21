# 기사단원의 무기

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/136798)

1번부터 `number`번까지의 기사들이 무기를 구매합니다.
- 기사 번호의 **약수 개수**가 곧 공격력입니다.
- 단, 공격력이 `limit`를 초과하면 정해진 `power`를 공격력으로 가집니다.
모든 기사가 구매할 무기의 공격력 합(필요한 철의 무게)을 구하세요.

## 해결 전략
1부터 `number`까지 각 수의 약수 개수를 구해야 합니다.
- 약수 개수를 구하는 효율적인 방법:
    - 1부터 `sqrt(n)`까지 나누어 떨어지는지 확인합니다.
    - `i`가 약수라면 `n // i`도 약수입니다.
    - `i * i == n`인 경우(제곱수)는 중복이므로 1개만 카운트합니다.
- 약수 개수가 `limit`보다 크면 `power`를 더하고, 아니면 그대로 더합니다.

### 알고리즘 순서
1. `answer` = 0
2. `i` from 1 to `number`:
    - `cnt` = 0
    - `j` from 1 to `int(sqrt(i))`:
        - `if i % j == 0`:
            - `cnt += 1`
            - `if j * j < i`: `cnt += 1`
    - `if cnt > limit`: `answer += power`
    - `else`: `answer += cnt`
3. 반환.

## Python 코드

```python
def solution(number, limit, power):
    total_weight = 0
    
    for i in range(1, number + 1):
        # i의 약수 개수 구하기
        cnt = 0
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                cnt += 1
                if j * j < i: # 제곱근이 아니면 대칭되는 약수 존재
                    cnt += 1
                    
        # 공격력 제한 확인
        if cnt > limit:
            total_weight += power
        else:
            total_weight += cnt
            
    return total_weight
```

## 배운 점 / 팁
- **약수 구하기 시간 복잡도**: `O(sqrt(N))`로 구해야 `number`가 100,000일 때 전체 `O(N * sqrt(N))`으로 통과 가능합니다. (단순 `O(N)` 반복시 시간 초과 가능성 있음)
