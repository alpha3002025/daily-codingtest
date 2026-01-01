def solution(n, words):
    answer = []
    
    prev = words[0]
    used = set([prev])
    
    for i in range(1, len(words)):
        curr = words[i]
        
        if not (curr[0] == prev[-1] and curr not in used):
            fail_person = (i % n) + 1
            fail_round = (i // n) + 1
            return [fail_person, fail_round]
        
        prev = curr
        used.add(curr)
            
    
    return [0,0]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))

print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))

print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))