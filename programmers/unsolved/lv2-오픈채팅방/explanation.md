# 오픈채팅방

## 문제 설명
오픈채팅방에 들어오고(`Enter`), 나가고(`Leave`), 닉네임을 변경(`Change`)하는 기록이 주어집니다.
최종적으로 닉네임이 변경된 상태를 반영하여, "누가 들어왔습니다", "누가 나갔습니다" 메시지를 출력해야 합니다.
**핵심**: 채팅방을 나갔다 들어오면서 닉네임을 바꾸거나, 채팅방 안에서 닉네임을 바꾸면, **이전에 출력된 메시지의 닉네임도 모두 바뀝니다**.

### 핵심 개념
1.  **해시 맵 (Dictionary)**: `User ID`를 Key로, `Nickname`을 Value로 저장하여 최신 닉네임을 관리합니다.
    - `Enter`나 `Change` 이벤트가 발생할 때마다 해당 유저의 닉네임을 갱신합니다.
2.  **로그 분리 저장**:
    - 메시지를 바로 문자열로 만들지 말고, `(Action, UserID)` 형태의 **로그**만 순서대로 저장해둡니다.
    - 모든 기록 처리가 끝난 후(최신 닉네임이 확정된 후), 로그를 순회하며 메시지를 생성합니다.

## Python 풀이

```python
def solution(record):
    user_db = {} # {uid: nickname}
    logs = []    # [(uid, action), ...]
    
    # 1. 기록 순회하며 최신 닉네임 갱신 및 로그 저장
    for entry in record:
        split_entry = entry.split()
        action = split_entry[0]
        uid = split_entry[1]
        
        if action == "Enter":
            nickname = split_entry[2]
            user_db[uid] = nickname
            logs.append((uid, "님이 들어왔습니다."))
            
        elif action == "Leave":
            # 나갈 때는 닉네임 변경 없음. ID만 기록
            logs.append((uid, "님이 나갔습니다."))
            
        elif action == "Change":
            nickname = split_entry[2]
            user_db[uid] = nickname
            # Change는 메시지를 출력하지 않음
            
    # 2. 최종 메시지 생성
    answer = []
    for uid, message in logs:
        # 최종 닉네임 + 메시지
        answer.append(user_db[uid] + message)
        
    return answer
```

### 코드 설명
- `Change`는 메시지를 남기지 않으며, 오직 `user_db`의 닉네임만 업데이트합니다.
- `Leave` 이벤트에는 닉네임 정보가 주어지지 않으므로, 기존 `user_db`에 있는 값을 써야 합니다.
- 모든 이벤트를 한 번 훑어서(`O(N)`) 최종 닉네임을 `user_db`에 완성한 뒤, 다시 로그를 훑어서(`O(N)`) 정답 문자열을 만듭니다.
