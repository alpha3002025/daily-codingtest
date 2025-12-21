# 최소직사각형

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/86491)

여러 명함들의 가로(`w`), 세로(`h`) 길이가 주어집니다.
모든 명함을 수납할 수 있는 가장 작은 지갑의 크기(`지갑 가로 x 지갑 세로`)를 구하세요.
단, 명함은 **돌려서(가로/세로 바꿔서)** 수납할 수 있습니다.

## 해결 전략
명함을 돌릴 수 있다는 것은, 가로/세로 중 **긴 쪽을 한쪽으로 몰아넣고**, **짧은 쪽을 다른 한쪽으로 몰아넣을 수 있다**는 뜻입니다.
즉, 각 명함의 `(max(w, h), min(w, h))`를 구한 뒤,
- `긴 쪽들의 최대값` x `짧은 쪽들의 최대값`을 구하면 됩니다.

### 알고리즘 순서
1. `max_w` = 0 (긴 변들의 최대)
2. `max_h` = 0 (짧은 변들의 최대)
3. `sizes` 순회 (`w`, `h`):
    - `cur_max = max(w, h)`
    - `cur_min = min(w, h)`
    - `max_w = max(max_w, cur_max)`
    - `max_h = max(max_h, cur_min)`
4. 반환 `max_w * max_h`

## Python 코드

```python
def solution(sizes):
    max_w = 0
    max_h = 0
    
    for w, h in sizes:
        # 가로, 세로 중 큰 값을 가로(명목상)로 두고, 작은 값을 세로로 둠
        # 즉, 명함을 '눕혀서' 정리한다고 생각
        cur_long = max(w, h)
        cur_short = min(w, h)
        
        # 가장 긴 변들 중의 최대값 갱신
        max_w = max(max_w, cur_long)
        # 가장 짧은 변들 중의 최대값 갱신 (그래야 모든 명함이 들어감)
        max_h = max(max_h, cur_short)
        
    return max_w * max_h
```

## 배운 점 / 팁
- **정규화(Normalization)**: 문제의 조건을 단순화하여(돌릴 수 있다 -> 다 눕혀버리자) 생각하면 매우 쉽게 풀리는 유형입니다.
