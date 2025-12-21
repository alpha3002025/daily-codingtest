# 직사각형 별찍기

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12969)

표준 입력으로 두 정수 `n`(가로), `m`(세로)이 주어집니다.
가로 길이 `n`, 세로 길이 `m`인 직사각형 형태의 `*`을 출력하세요.

## 해결 전략
파이썬의 문자열 곱하기(`*`) 기능을 사용하면 이중 반복문 없이 매우 간단하게 출력 가능합니다.
한 줄에 `*`이 `n`개(`"*" * n`) 있고, 그것을 `m`번 출력하면 됩니다.

### 알고리즘 순서
1. `n, m = map(int, input().split())`
2. `line = '*' * n`
3. `for _ in range(m): print(line)`

## Python 코드

```python
# 표준 입력 처리
a, b = map(int, input().strip().split(' '))

column = '*' * a

for _ in range(b):
    print(column)
    
# 또는 한 줄로: print(('*' * a + '\n') * b)
```

## 배운 점 / 팁
- **문자열 연산**: 파이썬에서는 `string * int`가 가능하여 반복되는 패턴을 매우 쉽게 만들 수 있습니다.
