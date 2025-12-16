# 카운트 다운

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181899)

## 문제 설명
정수 `start_num`와 `end_num`가 주어질 때, `start_num`에서 `end_num`까지 1씩 감소하는 수들을 차례로 담은 리스트를 반환하는 함수를 작성합니다.

## 해결 방법

`range()` 함수를 사용하여 시작 숫자부터 끝 숫자까지 역순으로 숫자를 생성하고, 이를 리스트로 변환합니다.

### 추천 풀이 (Python)

```python
def solution(start_num, end_num):
    # start_num부터 end_num까지 -1씩 감소하는 range 객체를 생성하고 리스트로 변환
    return list(range(start_num, end_num - 1, -1))
```

## 주요/필수 개념

### `range(start, stop, step)` 함수
파이썬의 `range` 함수는 특정 구간의 숫자를 생성하는 데 매우 유용합니다.
- `start`: 수열의 시작 값입니다. (포함)
- `stop`: 수열의 끝 값입니다. (미포함)
- `step`: 각 숫자 사이의 간격입니다.

이 문제에서는 **역순**으로 숫자를 생성해야 하므로 `step`을 **-1**로 설정합니다.
또한, `end_num`까지 포함해야 하므로 `stop` 값을 `end_num - 1`로 설정해야 합니다. (range는 stop 값을 포함하지 않기 때문입니다)

예시: `range(10, 3 - 1, -1)` -> `10, 9, 8, ..., 3`
