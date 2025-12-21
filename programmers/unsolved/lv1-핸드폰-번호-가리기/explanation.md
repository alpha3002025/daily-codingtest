# 핸드폰 번호 가리기

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12948)

전화번호 문자열 `phone_number`의 뒷 4자리를 제외한 나머지 숫자를 전부 `*`로 가린 문자열을 반환하세요.

## 해결 전략
문자열 슬라이싱과 반복을 이용합니다.
전체 길이에서 4를 뺀 만큼 `*`를 반복하고, 뒷 4자리를 그대로 붙입니다.

### 알고리즘 순서
1. `length` = `len(phone_number)`
2. `stars` = `*` * `(length - 4)`
3. `last4` = `phone_number[-4:]`
4. return `stars + last4`

## Python 코드

```python
def solution(phone_number):
    # 뒷 4자리 제외한 길이만큼 * + 뒷 4자리
    return "*" * (len(phone_number) - 4) + phone_number[-4:]
```

## 배운 점 / 팁
- **문자열 조작**: 가장 기본적인 문자열 인덱싱 문제입니다.
