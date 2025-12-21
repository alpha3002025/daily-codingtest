# 바탕화면 정리

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/161990)

바탕화면의 파일 상태를 나타내는 문자열 배열 `wallpaper`가 주어집니다.
- `#`: 파일이 있는 위치
- `.`: 빈 공간

모든 파일을 포함하는 **최소 크기의 드래그 영역**을 구해야 합니다.
드래그 영역은 `(lux, luy)`에서 `(rdx, rdy)`까지이며, `[lux, luy, rdx, rdy]`를 반환해야 합니다.
- `lux`, `luy`: 드래그 시작점 (가장 위, 가장 왼쪽 파일의 행/열 인덱스)
- `rdx`, `rdy`: 드래그 끝점 (가장 아래, 가장 오른쪽 파일의 행/열 인덱스 + 1)

## 해결 전략
파일(`#`)이 있는 모든 위치들의 행(row)과 열(col) 인덱스를 수집합니다.
- `lux` (시작 행) = 파일들 중 최소 행 인덱스
- `luy` (시작 열) = 파일들 중 최소 열 인덱스
- `rdx` (끝 행) = 파일들 중 최대 행 인덱스 + 1
- `rdy` (끝 열) = 파일들 중 최대 열 인덱스 + 1

### 알고리즘 순서
1. `lux`, `luy`는 큰 값(무한대 or 배열 크기)으로, `rdx`, `rdy`는 작은 값(-1)으로 초기화합니다.
2. `wallpaper`를 이중 반복문으로 순회하며 `#`을 찾습니다.
3. `#`을 발견하면 현재 `i`(행), `j`(열)로 `lux`, `luy`(min 갱신)와 `rdx`, `rdy`(max 갱신)를 업데이트합니다.
4. 최종적으로 `rdx`, `rdy`에 1을 더해 반환합니다.

## Python 코드

```python
def solution(wallpaper):
    # 초기값 설정
    lux = len(wallpaper)
    luy = len(wallpaper[0])
    rdx = 0
    rdy = 0
    
    # 전체 순회
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                # 최소 좌표 갱신
                lux = min(lux, i)
                luy = min(luy, j)
                # 최대 좌표 갱신 (끝점은 포함해야 하므로 나중에 +1 해줄 것을 고려해 현재 좌표 기록)
                rdx = max(rdx, i)
                rdy = max(rdy, j)
                
    # 드래그 영역은 (시작점) ~ (끝점 + 1)
    return [lux, luy, rdx + 1, rdy + 1]
```

## 배운 점 / 팁
- **좌표계 이해**: 드래그 영역의 시작점은 `inclusive`, 끝점은 `exclusive` 개념(혹은 우하단 꼭짓점)이므로, 최대 인덱스에 **+1**을 해야 함을 주의해야 합니다.
- **최대/최소 갱신**: 2차원 공간에서 bounding box를 구하는 가장 전형적인 알고리즘입니다.
