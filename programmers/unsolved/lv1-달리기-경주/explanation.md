# 달리기 경주

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/178871)

달리기 경주에서 해설진이 선수의 이름을 부를 때마다 해당 선수가 바로 앞의 선수를 추월합니다.
- `players`: 현재 등수 순서대로 선수 이름이 담긴 배열 (1등부터)
- `callings`: 해설진이 부른 이름 배열 (추월한 선수 이름)

경주가 끝난 후 선수들의 순서를 1등부터 담아 반환하세요.
(`players` 길이 최대 50,000, `callings` 길이 최대 1,000,000)

## 해결 전략
`callings`의 길이가 최대 100만으로 매우 큽니다. 매번 리스트의 특정 요소를 찾아(`index()`) 앞 요소와 교환(`swap`)하는 방식은 `O(N)` 시간이 걸리므로, 전체 시간 복잡도가 `O(M * N)`이 되어 시간 초과가 발생합니다 (`1,000,000 * 50,000`).

따라서 **O(1) 시간에 선수의 등수를 찾고 위치를 바꿀 수 있는 자료구조**가 필요합니다.
두 개의 딕셔너리(Hash Map)를 사용하여 양방향 매핑을 관리하면 효율적입니다.
1. `name_to_rank`: 선수 이름 -> 현재 등수
2. `rank_to_name`: 현재 등수 -> 선수 이름

이름이 불리면:
1. 해당 선수의 현재 등수(`rank`)를 찾습니다. (`name_to_rank` 사용)
2. 앞선 선수의 이름(`front_player`)을 찾습니다. (`rank_to_name[rank - 1]`)
3. 두 선수의 등수 정보를 갱신합니다. (딕셔너리 업데이트)
4. `rank_to_name`에서도 두 선수의 이름을 교환합니다.

### 알고리즘 순서
1. `name_to_rank`, `rank_to_name` 딕셔너리를 초기화합니다.
2. `callings`를 순회하며 각 `name`에 대해:
    - `current_rank = name_to_rank[name]`
    - `front_rank = current_rank - 1`
    - `front_player = rank_to_name[front_rank]`
    - **Swap**:
        - `name_to_rank[name] = front_rank`, `name_to_rank[front_player] = current_rank`
        - `rank_to_name[front_rank] = name`, `rank_to_name[current_rank] = front_player`
3. 최종적으로 `rank_to_name`을 0등부터 순서대로 리스트로 변환하거나, 갱신된 `players`를 반환합니다.

## Python 코드

```python
def solution(players, callings):
    # 이름 -> 등수 매핑
    player_to_rank = {player: i for i, player in enumerate(players)}
    # 등수 -> 이름 매핑 (리스트 players 자체가 역할 수행 가능)
    
    for call in callings:
        # 호출된 선수의 현재 등수
        current_rank = player_to_rank[call]
        
        # 앞 선수의 이름
        front_player = players[current_rank - 1]
        
        # Swap: players 리스트 업데이트
        players[current_rank], players[current_rank - 1] = players[current_rank - 1], players[current_rank]
        
        # Swap: 딕셔너리 등수 업데이트
        player_to_rank[call] -= 1
        player_to_rank[front_player] += 1
        
    return players
```

## 배운 점 / 팁
- **시간 복잡도 최적화**: 리스트의 `index()` 메서드는 `O(N)`입니다. 빈번한 조회가 필요할 땐 딕셔너리를 사용하여 `O(1)`로 최적화해야 합니다.
- **데이터 동기화**: 리스트(등수->이름)와 딕셔너리(이름->등수)를 동시에 관리할 때, 데이터 불일치가 발생하지 않도록 항상 같이 갱신해줘야 합니다.
