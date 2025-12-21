# 폰켓몬

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/1845)

N마리의 폰켓몬 중 `N/2`마리를 가져가야 합니다.
폰켓몬 종류(`nums`)가 주어질 때, 선택할 수 있는 **폰켓몬 종류 개수의 최댓값**을 구하세요.
(같은 종류는 중복해서 세지 않음)

## 해결 전략
가장 많은 종류를 고르려면, 최대한 다양한 종류를 하나씩 선택해야 합니다.
1. 존재하는 총 종류의 수: `len(set(nums))`
2. 선택할 수 있는 최대 마리 수: `len(nums) // 2`
3. 둘 중 작은 값이 정답입니다.
    - 종류가 아무리 많아도 `N/2`마리밖에 못 가져갑니다.
    - `N/2`마리를 다 다른 것으로 채우고 싶어도, 종류 자체가 적으면 그 종류 수만큼이 최대입니다.

### 알고리즘 순서
1. `max_pick` = `len(nums) // 2`
2. `unique_types` = `len(set(nums))`
3. return `min(max_pick, unique_types)`

## Python 코드

```python
def solution(nums):
    # 가져갈 수 있는 최대 개수
    pick_count = len(nums) // 2
    
    # 폰켓몬 종류의 개수
    type_count = len(set(nums))
    
    # 둘 중 작은 값이 정답
    return min(pick_count, type_count)
```

## 배운 점 / 팁
- **논리적 접근**: 복잡한 조합(`Combination`)을 계산할 필요 없이, 제약 조건(`min`)만 파악하면 한 줄로 풀리는 문제입니다.
