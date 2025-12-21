# 부족한 금액 계산하기

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/82612)

놀이기구를 `count`번 타면 이용료가 `n`배씩 증가합니다.
- 1회: `price`
- 2회: `price * 2`
- ...
- count회: `price * count`

총 필요한 이용료와 현재 가진 돈(`money`)의 차액을 구하세요. (돈이 충분하면 0 반환)

## 해결 전략
등차수열의 합 공식(`sigma k`)을 사용하면 O(1)에 계산 가능합니다.
총 비용 = `price * (1 + 2 + ... + count)` = `price * count * (count + 1) // 2`

### 알고리즘 순서
1. `total_cost` = `price * (count * (count + 1) // 2)`
2. `shortage` = `total_cost - money`
3. return `max(0, shortage)`

## Python 코드

```python
def solution(price, money, count):
    # 등차수열 합: n(n+1)/2
    total_cost = price * (count * (count + 1) // 2)
    
    # 부족한 금액 (음수면 0)
    return max(0, total_cost - money)
```

## 배운 점 / 팁
- **수학 공식 활용**: 반복문보다 공식(`Gauss Sum`)을 사용하는 것이 더 효율적이고 깔끔합니다.
