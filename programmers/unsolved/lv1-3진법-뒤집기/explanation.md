# 3진법 뒤집기

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/68935)

자연수 `n`을 3진법으로 바꾼 뒤, 앞뒤로 뒤집고, 이를 다시 10진법으로 표현한 수를 구하세요.

## 해결 전략
1. **10->3진법 변환**: `n`을 3으로 나눈 나머지를 문자열에 계속 붙여나갑니다.
    - 이때, `result += str(remainder)` 순으로 붙이면 자연스럽게 **뒤집힌 3진법** 문자열이 만들어집니다.
    - (일반적인 진법 변환은 나머지를 앞에 붙이거나, 다 만든 뒤 뒤집지만, 여기선 문제 자체가 "뒤집기"를 요구하므로 그냥 순서대로 붙이면 됨)
2. **3->10진법 변환**: 파이썬의 `int(string, 3)`을 사용하면 한 번에 변환됩니다.

### 알고리즘 순서
1. `base3` = ""
2. `while n > 0`:
    - `n`, `rem` = `divmod(n, 3)`
    - `base3 += str(rem)`
3. return `int(base3, 3)`

## Python 코드

```python
def solution(n):
    # 3진법으로 변환 (앞뒤 반전된 상태로 저장됨)
    base3 = ""
    while n > 0:
        n, remainder = divmod(n, 3)
        base3 += str(remainder)
        
    # 3진법 문자열을 10진수로 변환
    return int(base3, 3)
```

## 배운 점 / 팁
- **진법 변환**: `int(string, base)`는 n진수 문자열을 10진수 정수로 바꾸는 가장 강력한 도구입니다.
- **Divmod**: `divmod(a, b)`는 몫과 나머지를 튜플로 반환합니다.
