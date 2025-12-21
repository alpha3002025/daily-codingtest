# 가장 많이 받은 선물

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/258712)

친구들끼리 선물을 주고받은 기록(`gifts`)을 바탕으로, **다음 달에 선물을 가장 많이 받을 친구가 받을 선물의 수**를 예측하는 문제입니다.

**선물 주고받기 규칙**:
두 사람 A, B 사이에서:
1. **두 사람이 선물을 주고받은 기록이 있다면**: 더 많이 준 사람이 덜 준 사람에게서 **다음 달에 선물 하나를 받습니다.**
2. **기록이 없거나 주고받은 수가 같다면**: **선물 지수**가 더 큰 사람이 작은 사람에게서 **다음 달에 선물 하나를 받습니다.**
    - **선물 지수** = (이번 달에 준 선물 수) - (이번 달에 받은 선물 수)
    - 선물 지수까지 같다면 다음 달에 선물을 주고받지 않습니다.

## 해결 전략
데이터를 효율적으로 관리하고 조회하는 것이 핵심입니다.
각 친구를 인덱스(0부터 N-1)로 매핑하고, 2차원 배열과 1차원 배열을 사용하여 주고받은 횟수와 선물 지수를 관리하면 편리합니다.

1. **친구 매핑**: 이름(`friends`)을 0~N-1 정수 인덱스로 변환하는 딕셔너리(`name_to_idx`)를 만듭니다.
2. **기록 집계 (`record`)**: `N x N` 2차원 배열을 만들어, `record[i][j]`에 i가 j에게 준 선물 개수를 저장합니다.
3. **선물 지수 (`gift_index`)**: 각 친구마다 `(준 선물 총합) - (받은 선물 총합)`을 미리 계산해 둡니다.
    - `record` 배열의 행 합(`sum(record[i])`)은 i가 준 선물 총합입니다.
    - `record` 배열의 열 합(`sum(record[k][i] for k in range(N))`)은 i가 받은 선물 총합입니다.
4. **다음 달 선물 계산**:
    - 모든 친구 쌍 `(i, j)`에 대해 규칙을 적용하여 누가 받는지 판단합니다.
    - `i`가 받을 선물의 개수를 `count[i]`에 누적합니다.
    - 최종적으로 `max(count)`를 반환합니다.

### 알고리즘 순서
1. `friends` 리스트를 이용해 `name_to_idx` 맵 생성.
2. `record` 2차원 배열(NxN) 생성 및 초기화.
3. `gifts` 문자열 배열을 파싱하여 `record` 업데이트.
4. 각 친구별 `gift_index` 계산.
5. `next_month_gifts` 배열(길이 N) 생성.
6. 이중 루프로 모든 쌍 `(i, j)` 비교 (i < j인 경우만 비교해도 됨, 양방향 처리).
    - i가 j에게 준 것 > j가 i에게 준 것: `next_month_gifts[i] += 1`
    - 반대: `next_month_gifts[j] += 1`
    - 같다면: `gift_index` 비교해서 큰 쪽에 `+1`. 같으면 무시.
7. `max(next_month_gifts)` 반환.

## Python 코드

```python
def solution(friends, gifts):
    n = len(friends)
    name_to_idx = {name: i for i, name in enumerate(friends)}
    
    # record[i][j]: i가 j에게 준 선물 개수
    record = [[0] * n for _ in range(n)]
    
    # 선물 지수: 준 선물 - 받은 선물
    gift_index = [0] * n
    given_cnt = [0] * n
    received_cnt = [0] * n
    
    # 1. 주고받은 기록 집계
    for gift in gifts:
        giver_name, receiver_name = gift.split()
        giver = name_to_idx[giver_name]
        receiver = name_to_idx[receiver_name]
        
        record[giver][receiver] += 1
        given_cnt[giver] += 1
        received_cnt[receiver] += 1
        
    # 2. 선물 지수 계산
    for i in range(n):
        gift_index[i] = given_cnt[i] - received_cnt[i]
        
    # 3. 다음 달 받을 선물 계산
    next_month_gifts = [0] * n
    
    for i in range(n):
        for j in range(i + 1, n): # 중복 방지를 위해 i < j 인 경우만 확인
            # i와 j 사이의 관계 판단
            given_i_to_j = record[i][j]
            given_j_to_i = record[j][i]
            
            if given_i_to_j > given_j_to_i:
                next_month_gifts[i] += 1
            elif given_i_to_j < given_j_to_i:
                next_month_gifts[j] += 1
            else:
                # 주고받은 수가 같거나 둘 다 0인 경우 -> 선물 지수 비교
                if gift_index[i] > gift_index[j]:
                    next_month_gifts[i] += 1
                elif gift_index[i] < gift_index[j]:
                    next_month_gifts[j] += 1
                # 선물 지수도 같으면 아무도 안 받음
                
    return max(next_month_gifts) if next_month_gifts else 0
```

## 배운 점 / 팁
- **데이터 구조 설계**: 사람 이름(String)을 인덱스(Integer)로 변환하여 2차원 배열로 관리하면 관계 파악이 매우 빠르고 코드가 깔끔해집니다.
- **조합 탐색**: `for i in range(n): for j in range(i+1, n):` 패턴을 사용하면 모든 쌍을 한 번씩만 비교할 수 있어 효율적입니다.
