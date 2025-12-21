# 가운데 글자 가져오기

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12903)

단어 `s`의 가운데 글자를 반환하세요.
- 길이가 짝수면 가운데 2글자 반환.

## 해결 전략
인덱싱/슬라이싱.
- `mid = len(s) // 2`
- 홀수: `s[mid]`
- 짝수: `s[mid-1 : mid+1]`

### 알고리즘 순서
1. `mid` = `len(s) // 2`
2. `if len(s) % 2 == 0`: return `s[mid-1 : mid+1]`
3. `else`: return `s[mid]`

## Python 코드

```python
def solution(s):
    n = len(s)
    mid = n // 2
    
    if n % 2 == 0:
        # 짝수면 가운데 두 글자
        return s[mid-1 : mid+1]
    else:
        # 홀수면 가운데 한 글자
        return s[mid]
```

## 배운 점 / 팁
- **인덱싱**: `//` 연산자로 몫(중앙 인덱스)을 구하는 것이 핵심입니다.
