# 푸드 파이트 대회

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/134240)

두 선수가 양쪽에서 먹기 시작하여 중앙의 물(0)에서 만나는 대회를 엽니다.
음식 배치 `food`: `[물(1개), 1번음식개수, 2번음식개수, ...]`
- 각 음식은 두 선수가 똑같이 나눠 먹어야 하므로 `food[i] // 2` 개씩 배치합니다.
- 예: 1번 3개 -> 각자 1개씩 (1개 버림)
- 배치 순서: `1번...` `2번...` ... `0` ... `2번...` `1번...` (대칭)

## 해결 전략
문자열 생성 문제입니다.
1. 왼쪽 선수가 먹을 음식 문자열을 만듭니다.
    - 1번부터 끝까지 순회하며 `str(i) * (food[i] // 2)`를 이어 붙입니다.
2. 전체 문자열 = `left_side` + "0" + `left_side` 뒤집은 것.

### 알고리즘 순서
1. `half_str` = ""
2. `i` from 1 to `len(food)-1`:
    - `cnt = food[i] // 2`
    - `half_str += str(i) * cnt`
3. 반환 `half_str + "0" + half_str[::-1]`

## Python 코드

```python
def solution(food):
    left_side = []
    
    for i in range(1, len(food)):
        count = food[i] // 2
        # i번 음식을 count만큼 추가
        left_side.append(str(i) * count)
        
    left_str = "".join(left_side)
    
    # 왼쪽 + 물(0) + 오른쪽(왼쪽의 역순)
    return left_str + "0" + left_str[::-1]
```

## 배운 점 / 팁
- **문자열 뒤집기**: `s[::-1]`이 가장 간편합니다.
- **팰린드롬 생성**: 앞부분만 만들고 역순을 뒤에 붙이면 대칭 문자열이 완성됩니다.
