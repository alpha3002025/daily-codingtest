# 기지국 설치

## 문제 설명
N개의 아파트가 있고, 일부 아파트에는 기지국이 설치되어 있습니다 (`stations`).
전파 도달 거리는 `w`입니다.
모든 아파트에 전파가 도달하도록 최소한의 기지국을 추가로 설치하세요.

## 문제 해결 전략

**그리디 (Greedy)** & **수학**.
기지국이 커버하지 못하는 **빈 구간의 길이**를 구합니다.
빈 구간의 길이가 `L`일 때, 하나의 기지국은 `2*w + 1`만큼 커버 가능합니다.
따라서 `ceil(L / (2*w + 1))` 개의 기지국이 필요합니다.
`stations`를 순회하며 빈 구간들을 찾고 필요한 기지국 수를 누적합니다.

## Python 코드

```python
import math

def solution(n, stations, w):
    answer = 0
    coverage = 2 * w + 1
    
    # 현재까지 커버된 마지막 위치
    last_covered = 0
    
    for s in stations:
        # 이번 기지국의 영향 범위: s-w ~ s+w
        start = s - w
        end = s + w
        
        # 빈 구간: last_covered + 1 ~ start - 1
        if start > last_covered + 1:
            length = (start - 1) - (last_covered + 1) + 1
            # 필요한 기지국 수
            answer += math.ceil(length / coverage)
            
        last_covered = end
        
    # 마지막 기지국 이후 남은 구간 처리
    if last_covered < n:
        length = n - last_covered
        answer += math.ceil(length / coverage)
        
    return answer
```
