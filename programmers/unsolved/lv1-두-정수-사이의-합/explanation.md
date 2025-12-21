# 두 정수 사이의 합

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12912)

두 정수 `a`, `b` 사이에 속한 모든 정수의 합을 구하세요. (대소관계 미정)

## 해결 전략
1. `min(a, b)`와 `max(a, b)`를 구합니다.
2. 등차수열 합 공식 사용. `(start + end) * (count) / 2`

### 알고리즘 순서
1. `start`, `end` = `min(a, b)`, `max(a, b)`
2. return `(start + end) * (end - start + 1) // 2`

## Python 코드

```python
def solution(a, b):
    # a와 b의 대소관계가 정해져 있지 않으므로 min, max 사용
    start = min(a, b)
    end = max(a, b)
    
    # 등차수열 합 공식
    return (start + end) * (end - start + 1) // 2
```

## 배운 점 / 팁
- **수학 공식**: 반복문보다 O(1) 공식이 훨씬 빠릅니다.
