def solution(n, words):
    prev = words[0]
    used = set([prev])
    
    for i in range(1, len(words)):
        curr = words[i]
        
        if not (prev[-1] == curr[0] and curr not in used):
            failed_person = (i % n) + 1
            failed_round = (i // n) + 1
            return [failed_person, failed_round]
        
        prev = curr
        used.add(curr)
    
    return [0,0]