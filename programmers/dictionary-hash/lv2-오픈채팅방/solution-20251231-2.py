def solution(record):
    users = {}
    messages = []
    for event in record:
        args = event.split()
        command, uid = args[0], args[1]
        
        if command == "Enter":
            messages.append((uid, "님이 들어왔습니다."))
            users[uid] = args[2]
            
        elif command == "Leave":
            messages.append((uid, "님이 나갔습니다."))
        
        elif command == "Change":
            users[uid] = args[2]
    
    answer = []
    
    for message in messages:
        answer.append(users[message[0]] + message[1])
    
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))