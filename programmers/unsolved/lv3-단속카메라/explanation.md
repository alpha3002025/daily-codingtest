# 단속카메라

## 문제 설명
고속도로를 이동하는 차량들의 경로 `routes` (`[진입, 진출]`)가 주어집니다.
모든 차량이 한 번은 단속카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지 구하세요.

## 문제 해결 전략

**그리디 (Greedy)** 알고리즘.
활동 선택 문제(Activity Selection Problem)와 유사합니다.
1. 차량들을 **진출 지점** 기준으로 오름차순 정렬합니다. (빨리 나가는 차부터 잡아야 함)
2. 가장 먼저 나가는 차의 진출 지점에 카메라를 설치합니다. (최대한 뒤에 설치해야 겹치는 다른 차들도 많이 잡음)
3. 그 카메라에 찍힌 차들은 패스합니다.
4. 아직 안 찍힌 차 중 가장 먼저 나가는 차의 진출 지점에 또 설치합니다. 반복.

## Python 코드

```python
def solution(routes):
    # 진출 지점 기준 정렬
    routes.sort(key=lambda x: x[1])
    
    camera_pos = -30001 # 초기값 (범위 밖)
    count = 0
    
    for start, end in routes:
        # 이 차가 마지막 카메라에 안 걸리는가?
        # (카메라 위치 < 진입 지점) -> 안 걸림
        if camera_pos < start:
            count += 1
            camera_pos = end # 이 차의 끝부분에 새 카메라 설치
            
    return count
```
