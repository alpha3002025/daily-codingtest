# 음양 더하기

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/76501)

정수 배열 `absolutes`와 부호 배열 `signs`가 주어집니다.
`signs[i]`가 `true`면 양수, `false`면 음수로 처리하여 총합을 구하세요.

## 해결 전략
아주 간단한 매핑 합산 문제입니다.
`zip`을 사용하여 각 수와 부호를 묶고, 조건부 덧셈을 수행합니다.

### 알고리즘 순서
1. `answer` = 0
2. `zip(absolutes, signs)` 순회 (`val`, `sign`):
    - `if sign`: `answer += val`
    - `else`: `answer -= val`
3. 반환.

## Python 코드

```python
def solution(absolutes, signs):
    answer = 0
    
    for val, is_positive in zip(absolutes, signs):
        if is_positive:
            answer += val
        else:
            answer -= val
            
    return answer
```

## 배운 점 / 팁
- **Zip**: 두 배열을 병렬로 순회할 때 가장 파이썬다운 방법입니다.
