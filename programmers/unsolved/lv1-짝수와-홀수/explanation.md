# 짝수와 홀수

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12937)

정수 `num`이 짝수면 "Even", 홀수면 "Odd"를 반환하세요.

## 해결 전략
나머지 연산(`% 2`)을 사용합니다.

### 알고리즘 순서
1. `if num % 2 == 0`: return `"Even"`
2. `else`: return `"Odd"`

## Python 코드

```python
def solution(num):
    return "Even" if num % 2 == 0 else "Odd"
```

## 배운 점 / 팁
- **삼항 연산자**: 간단한 조건문은 `A if condition else B` 형태로 한 줄에 쓰는 것이 파이썬스럽습니다.
