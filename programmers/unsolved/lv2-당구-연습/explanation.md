# 당구 연습

## 문제 설명
당구대 크기 `m x n`이 주어지고, 시작 공 위치 `(startX, startY)`와 목표 공들의 위치 `balls`가 주어집니다.
시작 공을 쳐서 벽(쿠션)에 **최소 한 번** 맞힌 후 목표 공을 맞혀야 합니다.
단, 목표 공을 맞히기 전에 다른 공을 맞히면 안 됩니다. (즉, 쿠션보다 공을 먼저 맞히면 안 됨).
각 목표 공에 대해 최소 이동 거리의 제곱을 구하는 문제입니다.

## 풀이 개념
**대칭 이동(Reflection)** 원리를 사용합니다.
공이 벽에 맞고 튕겨 나가는 것은, 목표 지점을 해당 벽에 대해 대칭 이동시킨 지점으로 직선 이동하는 것과 거리가 같습니다.

1. **대칭 이동 Point**: 목표 공을 4개의 벽(좌, 우, 상, 하)에 대해 각각 대칭 이동시킵니다.
   - 좌 (x=0): `(-x, y)`
   - 우 (x=m): `(2m - x, y)`
   - 상 (y=n): `(x, 2n - y)`
   - 하 (y=0): `(x, -y)`
2. **유효성 검사**: 단순히 대칭 이동 거리만 구하면 안 되고, "쿠션 전에 공을 먼저 맞히는 경우"를 제외해야 합니다.
   - 예를 들어, 시작점과 목표점이 x좌표가 같고, 목표점이 시작점과 위쪽 벽 사이에 있다면 위쪽 벽을 맞히러 갈 때 목표 공에 먼저 부딪히게 됩니다.
   - 따라서 일직선 상에 있고 방향이 벽보다 목표 공 쪽인 경우를 제외합니다.
3. **최소 거리 계산**: 유효한 대칭점들 중 시작점과의 거리 제곱이 가장 작은 값을 선택합니다.

## 코드 (Python)

```python
def solution(m, n, startX, startY, balls):
    answer = []
    
    for targetX, targetY in balls:
        dists = []
        
        # 1. 왼쪽 벽 (x=0) 대칭 -> (-targetX, targetY)
        # 조건: y가 같고 startX > targetX 인 경우 왼쪽 벽으로 갈 때 target을 먼저 맞힘 (제외)
        if not (startY == targetY and startX > targetX):
            d2 = (startX - (-targetX))**2 + (startY - targetY)**2
            dists.append(d2)
            
        # 2. 오른쪽 벽 (x=m) 대칭 -> (2m - targetX, targetY)
        # 조건: y가 같고 startX < targetX 인 경우 제외
        if not (startY == targetY and startX < targetX):
            d2 = (startX - (2*m - targetX))**2 + (startY - targetY)**2
            dists.append(d2)
            
        # 3. 위쪽 벽 (y=n) 대칭 -> (targetX, 2n - targetY)
        # 조건: x가 같고 startY < targetY 인 경우 제외
        if not (startX == targetX and startY < targetY):
            d2 = (startX - targetX)**2 + (startY - (2*n - targetY))**2
            dists.append(d2)
            
        # 4. 아래쪽 벽 (y=0) 대칭 -> (targetX, -targetY)
        # 조건: x가 같고 startY > targetY 인 경우 제외
        if not (startX == targetX and startY > targetY):
            d2 = (startX - targetX)**2 + (startY - (-targetY))**2
            dists.append(d2)
            
        answer.append(min(dists))
        
    return answer
```
