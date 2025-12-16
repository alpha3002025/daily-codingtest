# 불량 사용자

## 문제 설명
이벤트 당첨자 아이디(`user_id`) 목록과 불량 사용자 아이디(`banned_id`) 목록이 있습니다.
`banned_id`에는 '*' 문자가 포함되어 있으며, 이는 모든 문자와 매칭됩니다.
`banned_id` 배열의 순서대로 모든 패턴과 매칭되는 `user_id`의 목록(제재 아이디 목록)을 구했을 때, 가능한 목록의 **경우의 수**를 구하세요.
단, 목록의 아이디들이 같으면 순서가 달라도 같은 목록으로 취급합니다.

## 문제 해결 전략

1. **매칭 확인 (Regex)**:
   - 각 `banned_id` 패턴에 대해 매칭 가능한 `user_id` 후보들을 미리 찾습니다.
   - 길이가 같고, 문자가 같거나 패턴이 '*'여야 합니다.

2. **완전 탐색 (DFS / Backtracking)**:
   - `banned_id`가 최대 8개, `user_id`도 최대 8개로 매우 작습니다.
   - DFS로 `banned_id`의 인덱스(`idx`)를 하나씩 늘려가며 매칭되는 `user_id`를 선택합니다.
   - 이미 선택된 `user_id`는 중복 선택할 수 없습니다(`visited` set 활용).

3. **결과 집합 관리**:
   - DFS가 끝까지 도달하면, 선택된 아이디들의 집합을 결과 집합(`answer_set`)에 추가합니다.
   - `set` 대신 정렬된 `tuple`을 `set`에 넣으면 자동 중복 제거가 됩니다. (순서 무관하므로 내용물만 같으면 됨)
   - 최종적으로 `len(answer_set)` 반환.

## Python 코드

```python
import re

def solution(user_id, banned_id):
    # 매칭 여부 함수
    def is_match(user, ban):
        if len(user) != len(ban):
            return False
        for u, b in zip(user, ban):
            if b != '*' and u != b:
                return False
        return True
    
    matched_list = []
    for ban in banned_id:
        temp = []
        for user in user_id:
            if is_match(user, ban):
                temp.append(user)
        matched_list.append(temp)
        
    answer_set = set()
    
    def dfs(idx, current_users):
        if idx == len(banned_id):
            # 순서 상관없이 구성 요소가 같으면 같은 것으로 처리
            answer_set.add(tuple(sorted(current_users)))
            return
            
        # 해당 banned_id[idx]에 매칭되는 후보들 순회
        for user in matched_list[idx]:
            if user not in current_users:
                # current_users에 추가하고 다음으로
                # (set을 복사하거나 새 set을 넘김)
                new_users = set(current_users)
                new_users.add(user)
                dfs(idx + 1, new_users)
                
    dfs(0, set())
    
    return len(answer_set)
```
