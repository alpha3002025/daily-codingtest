# 없는 숫자 더하기

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/86051)

0부터 9까지의 숫자 중 일부가 들어있는 배열 `numbers`가 주어집니다.
`numbers`에서 찾을 수 없는 0부터 9까지의 숫자를 모두 더해 반환하세요.

## 해결 전략
0부터 9까지의 총합은 45(`0+1+...+9`)입니다.
여기서 `numbers`에 있는 숫자들의 합을 빼면, 없는 숫자들의 합이 됩니다.

### 알고리즘 순서
1. `return 45 - sum(numbers)`

## Python 코드

```python
def solution(numbers):
    # 0~9의 합은 45
    return 45 - sum(numbers)
```

## 배운 점 / 팁
- **여집합의 원리**: 전체 집합(0~9)을 알고 있을 때, 포함된 것을 빼면 포함되지 않은 것이 남습니다. `set` 연산을 쓸 수도 있지만 단순 합이 가장 빠릅니다.
