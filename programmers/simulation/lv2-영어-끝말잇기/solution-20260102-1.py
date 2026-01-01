def solution(n, words):
    answer = []

    user_number = 0
    prev = words[0]
    used = set([prev])
    
    for i in range(1, len(words)):
        word = words[i]
        prev = words[i-1]
        
        if word in used or prev[-1] != word[0]:
            user_number = (i % n) + 1
            cnt = (i // n) + 1
            return [user_number, cnt]
            break
        used.add(word)
        
    
    return [0,0]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))

print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))

print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))