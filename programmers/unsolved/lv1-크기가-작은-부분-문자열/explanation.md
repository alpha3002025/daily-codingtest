# 크기가 작은 부분 문자열

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/147355)

숫자로 이루어진 문자열 `t`와 `p`가 주어집니다.
`t`에서 `p`와 길이가 같은 부분 문자열들 중에서, 이 부분 문자열이 나타내는 수가 `p`가 나타내는 수보다 **작거나 같은** 것이 몇 개인지 구하세요.

## 해결 전략
슬라이딩 윈도우(Sliding Window)와 유사하게 `t`를 처음부터 끝까지 `p`의 길이만큼 잘라서 숫자로 변환 비교하면 됩니다.
파이썬은 매우 큰 정수도 기본적으로 처리 가능하므로 오버플로우 걱정 없이 `int()` 변환 비교가 가능합니다.

### 알고리즘 순서
1. `len_p` = `len(p)`
2. `num_p` = `int(p)`
3. `count` = 0
4. `i` from 0 to `len(t) - len_p`:
    - `sub_str` = `t[i : i + len_p]`
    - `sub_num` = `int(sub_str)`
    - `sub_num <= num_p` 이면 `count += 1`
5. `count` 반환.

## Python 코드

```python
def solution(t, p):
    count = 0
    len_p = len(p)
    target = int(p)
    
    # t에서 길이 len_p인 부분 문자열 추출
    # 범위: 0 ~ len(t) - len_p 까지
    for i in range(len(t) - len_p + 1):
        sub_str = t[i : i + len_p]
        if int(sub_str) <= target:
            count += 1
            
    return count
```

## 배운 점 / 팁
- **문자열 슬라이싱**: `string[start:end]` 문법을 자유자재로 다룰 수 있어야 합니다.
- **Python의 정수 자료형**: 파이썬은 Arbitrary-precision integers를 지원하므로, 문자열 길이가 길어도(최대 10,000자리는 int로 변환하기 부담될 수 있지만 문제 제한은 p길이 18이므로 충분) 안심하고 변환 비교할 수 있습니다.
