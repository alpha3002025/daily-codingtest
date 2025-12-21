# 콜라 문제

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/132267)

빈 병 `a`개를 가져다주면 콜라 `b`병을 줍니다.
처음에 빈 병 `n`개를 가지고 있을 때, 받을 수 있는 총 콜라 병 수를 구하세요. (받은 콜라도 다 마시면 다시 빈 병이 됩니다)

## 해결 전략
단순 시뮬레이션입니다.
보유 중인 빈 병 `n`이 교환 가능한 최소 개수 `a`보다 작아질 때까지 반복합니다.
1. 교환 가능한 횟수 `pack` = `n // a`
2. 새로 받는 콜라 `new_cokes` = `pack * b`
3. 남은 빈 병 `remain` = `n % a`
4. 새로운 `n` = `new_cokes + remain`
5. `answer += new_cokes`

### 알고리즘 순서
1. `answer` = 0
2. `while n >= a`:
    - `new_bottles = (n // a) * b`
    - `n = (n % a) + new_bottles`
    - `answer += new_bottles`
3. 반환.

## Python 코드

```python
def solution(a, b, n):
    answer = 0
    
    while n >= a:
        # a개씩 묶어서 교환 (묶음 수 * 주는 개수)
        new_coke = (n // a) * b
        
        # 교환하고 남은 병 + 새로 받은 병(마시고 빈 병 됨)
        n = (n % a) + new_coke
        
        answer += new_coke
        
    return answer
```

## 배운 점 / 팁
- **수학적 패턴**: 교환 비율 문제에서는 나머지(`%`)와 몫(`//`)을 잘 관리하며 갱신(Update)하는 루프 구조를 만듭니다.
- **일반화**: 보통 2개 주면 1개 받는 구조(`a=2, b=1`)가 많지만, 여기서는 `b`개라는 점(`a=3, b=2` 가능)을 유의해야 합니다.
