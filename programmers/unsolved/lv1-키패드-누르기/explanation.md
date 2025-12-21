# 키패드 누르기

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/67256)

스마트폰 키패드에서 왼손(`*` 시작)과 오른손(`#` 시작) 엄지손가락을 사용하여 숫자를 누릅니다.
- 1, 4, 7: 무조건 왼손 (`L`)
- 3, 6, 9: 무조건 오른손 (`R`)
- 2, 5, 8, 0: 현재 손 위치에서 더 가까운 손이 누름.
    - 거리가 같으면 쪽(`hand`) 손 잡이에 따라 결정.
- 거리: 상하좌우 이동 1칸 = 거리 1 (맨해튼 거리)

## 해결 전략
키패드 위치를 **좌표 (row, col)**로 변환하여 거리를 계산해야 합니다.
- 1:(0,0), 2:(0,1), 3:(0,2) ... 0:(3,1), *:(3,0), #:(3,2)
- 거리 = `abs(x1-x2) + abs(y1-y2)`

1. 키패드 좌표 매핑 딕셔너리 생성.
2. `left_pos`, `right_pos` 초기화.
3. `numbers` 순회하며 누를 손 결정 및 위치 갱신.

### 알고리즘 순서
1. `key_dict` = `{1:(0,0), ... , 0:(3,1), '*':(3,0), '#':(3,2)}`
2. `cur_l` = `*`, `cur_r` = `#`
3. `numbers` 순회 (`num`):
    - `1,4,7`: `L`, `cur_l` 갱신
    - `3,6,9`: `R`, `cur_r` 갱신
    - `2,5,8,0`:
        - `dist_l` = `manhattan(cur_l, num)`
        - `dist_r` = `manhattan(cur_r, num)`
        - 거리 비교 후 결정 (같으면 `hand` 기준)

## Python 코드

```python
def solution(numbers, hand):
    # 키패드 좌표 매핑
    pos = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        '*':(3,0), 0:(3,1), '#':(3,2)
    }
    
    # 초기 손 위치
    left_hand = pos['*']
    right_hand = pos['#']
    
    answer = ''
    
    for num in numbers:
        target = pos[num]
        
        # 1, 4, 7 -> 왼손
        if num in [1, 4, 7]:
            answer += 'L'
            left_hand = target
            
        # 3, 6, 9 -> 오른손
        elif num in [3, 6, 9]:
            answer += 'R'
            right_hand = target
            
        # 2, 5, 8, 0 -> 가까운 손
        else:
            # 맨해튼 거리 계산
            dist_l = abs(target[0] - left_hand[0]) + abs(target[1] - left_hand[1])
            dist_r = abs(target[0] - right_hand[0]) + abs(target[1] - right_hand[1])
            
            if dist_l < dist_r:
                answer += 'L'
                left_hand = target
            elif dist_r < dist_l:
                answer += 'R'
                right_hand = target
            else:
                # 거리가 같으면 주 사용 손
                if hand == 'left':
                    answer += 'L'
                    left_hand = target
                else:
                    answer += 'R'
                    right_hand = target
                    
    return answer
```

## 배운 점 / 팁
- **좌표 변환**: 격자 위에서의 거리 문제는 좌표계로 변환하는 것이 가장 직관적입니다.
- **맨해튼 거리**: 격자 이동 거리(`L1 Distance`) 공식을 사용합니다.
