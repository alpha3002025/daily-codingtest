# 교점에 별 만들기

## 문제 설명
여러 개의 직선 방정식 $Ax + By + C = 0$ 들이 주어질 때, 이 직선들의 **교점 중 정수 좌표**인 것들만 골라 별(*)을 찍어 출력하는 문제입니다. 좌표평면을 2차원 배열로 옮겨서 '*'을 찍고 나머지는 '.'으로 표현해야 합니다.

### 핵심 개념
1.  **직선의 교점 구하기**: 두 직선 $Ax + By + E = 0$, $Cx + Dy + F = 0$ 의 교점 $(x, y)$는 연립방정식의 해입니다.
    - $x = (BF - ED) / (AD - BC)$
    - $y = (EC - AF) / (AD - BC)$
    - 분모 $(AD - BC)$가 0이면 평행하거나 일치하는 직선입니다 (교점 없음).
2.  **정수 판별**: 교점 좌표가 정수인 경우만 찾으려면, 계산된 $x, y$가 정수로 딱 떨어지는지 확인해야 합니다. (`num % denom == 0`)
3.  **좌표 정규화 (Normalization)**: 문제의 좌표값은 매우 클 수 있지만, 별이 찍히는 영역은 한정적입니다. 구한 정수 교점들의 `min_x`, `min_y`를 찾아 모든 점을 이동시켜 배열의 인덱스(0부터 시작)에 맞게 변환해야 합니다.
4.  **2차원 배열 시각화**: `max_y - min_y + 1` 행, `max_x - min_x + 1` 열 크기의 배열을 만들고, 변환된 좌표에 별을 찍습니다. (주의: 일반적인 수학 좌표계 $(x, y)$와 프로그래밍 배열 인덱스 `(row, col)`의 $y$축 방향이 반대일 수 있음을 고려하거나, 출력 시 뒤집어야 합니다. 보통 배열은 `row`가 증가하면 아래로 내려갑니다.)

## Python 풀이

```python
def solution(line):
    points = set()
    
    n = len(line)
    # 모든 두 직선 쌍에 대해 교점 구하기
    for i in range(n):
        for j in range(i + 1, n):
            A, B, E = line[i]
            C, D, F = line[j]
            
            denom = A * D - B * C
            if denom == 0: # 평행 또는 일치
                continue
                
            # 교점 공식 분자
            x_num = B * F - E * D
            y_num = E * C - A * F
            
            # 정수 좌표 체크
            if x_num % denom == 0 and y_num % denom == 0:
                x = x_num // denom
                y = y_num // denom
                points.add((x, y))
                
    if not points:
        return []

    # 좌표 범위 계산 (Bounding Box)
    # unzip을 이용한 min/max 찾기
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    
    # 격자 크기 결정
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    
    # 빈 격자 생성 (모두 '.')
    # row index 0이 가장 위쪽(max_y), row index height-1이 가장 아래쪽(min_y)
    # 따라서 grid[0] -> y = max_y
    grid = [['.'] * width for _ in range(height)]
    
    for x, y in points:
        # 좌표 변환
        # x좌표: min_x를 0으로 shift -> x - min_x (col index)
        # y좌표: max_y를 0으로 shift -> max_y - y (row index) 
        # (배열은 아래로 갈수록 인덱스 증가, 좌표는 위로 갈수록 y 증가)
        c = x - min_x
        r = max_y - y
        grid[r][c] = '*'
        
    return ["".join(row) for row in grid]
```

### 코드 설명
- **이중 루프**: `line` 배열의 길이가 최대 1,000이므로 $O(N^2)$은 $10^6$ 연산 정도로 충분히 빠릅니다.
- **분모 확인**: `AD - BC`가 0이면 교점이 없습니다(평행).
- **좌표 변환**: 가장 중요한 부분입니다.
    - $x$축: 왼쪽이 작고 오른쪽이 크므로, `col = x - min_x`.
    - $y$축: 위쪽이 크고 아래쪽이 작지만, 2차원 배열 인덱스 `row`는 위쪽이 0이고 아래로 갈수록 커집니다. 따라서 `row = max_y - y`.
- **Set 자료구조**: 중복된 교점을 제거하기 위해 `set`을 사용합니다.
