# 예산

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12982)

각 부서가 신청한 금액 `d` 배열과 총 예산 `budget`이 있습니다.
신청한 금액을 들어줄 때는 **전액 지원**만 가능합니다.
최대 몇 개의 부서에 지원해 줄 수 있는지 구하세요.

## 해결 전략
최대한 많은 부서를 지원하려면, **신청 금액이 적은 부서**부터 지원해야 합니다.
그리디(Greedy) 알고리즘입니다.
1. `d`를 오름차순 정렬합니다.
2. 예산이 되는 대로 차감하며 카운트합니다.

### 알고리즘 순서
1. `d.sort()`
2. `count` = 0
3. `d` 순회 (`amount`):
    - `if budget >= amount`:
        - `budget -= amount`
        - `count += 1`
    - `else`:
        - `break` (더 이상 지원 불가)
4. `count` 반환.

## Python 코드

```python
def solution(d, budget):
    d.sort() # 적은 금액부터 처리
    count = 0
    
    for amount in d:
        if budget >= amount:
            budget -= amount
            count += 1
        else:
            # 예산 부족하면 중단 (뒤에는 더 큰 금액들이므로 볼 필요 없음)
            break
            
    return count
```

## 배운 점 / 팁
- **그리디+정렬**: "최대 개수"를 묻는 자원 할당 문제에서 비용이 적은 것부터 처리하는 것은 정석입니다.
