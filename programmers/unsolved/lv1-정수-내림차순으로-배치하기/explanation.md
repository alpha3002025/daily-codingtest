# 정수 내림차순으로 배치하기

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12933)

정수 `n`의 각 자릿수를 큰 순서(내림차순)로 정렬하여 새로운 정수를 만드세요.
예: `118372` -> `873211`

## 해결 전략
문자열로 변환 -> 리스트 변환 -> 정렬(`reverse=True`) -> 문자열 결합 -> 정수 변환.

### 알고리즘 순서
1. `digits` = `list(str(n))`
2. `digits.sort(reverse=True)`
3. return `int("".join(digits))`

## Python 코드

```python
def solution(n):
    # 문자열로 변환 후 정렬 (문자열도 iterable이므로 sorted 바로 가능)
    sorted_digits = sorted(str(n), reverse=True)
    
    # 다시 합쳐서 정수로 변환
    return int("".join(sorted_digits))
```

## 배운 점 / 팁
- **타입 변환 체인**: `int` <-> `str` <-> `list` 변환은 파이썬 코딩테스트의 기본기입니다.
