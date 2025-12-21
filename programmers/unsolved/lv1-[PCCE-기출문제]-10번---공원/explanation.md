# [PCCE 기출문제] 10번 / 공원

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/340198)

공원의 평면도 `park`가 2차원 문자열 배열로 주어집니다.
- `"-1"`: 빈 공간 (돗자리 깔 수 있음)
- 알파벳 문자: 이미 사람이 있거나 장애물이 있음

지민이가 가진 돗자리들의 한 변 길이 목록 `mats`가 주어집니다 (모두 정사각형).
가장 큰 돗자리부터 깔아보면서, 공원의 빈 공간에 깔 수 있는 가장 큰 돗자리의 한 변 길이를 반환하세요.
아무런 돗자리도 깔 수 없다면 -1을 반환합니다.

## 해결 전략
완전 탐색(Brute Force) 문제이나, 효율성을 위해 몇 가지 전략을 사용할 수 있습니다.
가장 큰 돗자리부터 차례대로 깔 수 있는지 검사하고, 깔 수 있다면 그 즉시 반환하는 `Greedy`한 접근이 좋습니다.

공원의 크기가 최대 50x50으로 매우 작습니다. 따라서 모든 위치에서 모든 돗자리를 대보는 시도를 해도 충분합니다.
시간 복잡도: (돗자리 개수) * (공원 행) * (공원 열) * (돗자리 크기^2)
= 10 * 50 * 50 * 20^2 ≈ 10,000,000 (충분히 작음)

### 알고리즘 순서
1. `mats`를 내림차순 정렬합니다. (큰 돗자리 우선)
2. 각 돗자리 크기 `size`에 대해:
    - 공원의 모든 칸 `(r, c)`를 순회합니다.
    - 현재 위치 `(r, c)`를 왼쪽 위 모서리로 하여 `size x size` 크기의 정사각형 영역이 모두 `"-1"`인지 검사합니다.
        - 영역이 공원 범위를 벗어나면 검사하지 않습니다.
    - 모두 `"-1"`이라면 해당 `size`를 즉시 반환합니다.
3. 모든 돗자리를 검사했는데도 못 깔았다면 `-1`을 반환합니다.

## Python 코드

```python
def solution(mats, park):
    # 큰 돗자리부터 확인하기 위해 내림차순 정렬
    mats.sort(reverse=True)
    
    rows = len(park)
    cols = len(park[0])
    
    # 각 돗자리 크기에 대해
    for size in mats:
        # 공원의 모든 시작점 (r, c) 탐색
        for r in range(rows):
            for c in range(cols):
                # 돗자리가 공원 범위를 벗어나면 패스
                if r + size > rows or c + size > cols:
                    continue
                
                # 해당 영역이 모두 빈 공간("-1")인지 확인
                is_possible = True
                for i in range(size):
                    for j in range(size):
                        if park[r+i][c+j] != "-1":
                            is_possible = False
                            break
                    if not is_possible:
                        break
                
                # 깔 수 있다면 가장 큰 돗자리이므로 즉시 반환
                if is_possible:
                    return size
                    
    return -1
```

## 배운 점 / 팁
- **탐색 순서 최적화**: "가장 큰 값"을 찾는 문제에서는 가능한 값들을 큰 순서대로 정렬한 뒤, 조건을 만족하는 첫 번째 값을 찾는 것이 효율적입니다.
- **범위 체크**: 2차원 배열 탐색 시 인덱스 에러(`IndexError`)를 방지하기 위해 루프 시작 전이나 내부에서 `r + size > rows` 체크를 잊지 말아야 합니다.
