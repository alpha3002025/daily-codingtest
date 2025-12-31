def solution(record):
    user_db = {}
    logs = []
    
    for entry in record:
        split_entry = entry.split()
        action = split_entry[0]
        uid = split_entry[1]
        
        if action == "Enter":
            nickname = split_entry[2]
            user_db[uid] = nickname
            logs.append((uid, "님이 들어왔습니다."))
            
        elif action == "Leave":
            logs.append((uid, "님이 나갔습니다."))
        
        elif action == "Change":
            nickname = split_entry[2]
            user_db[uid] = nickname
    
    answer = []
    for uid, message in logs:
        answer.append(user_db[uid] + message)
    
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))