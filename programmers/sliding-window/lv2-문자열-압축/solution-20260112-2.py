def solution(s):
    answer = 0
    
    min_length = len(s)
    n = len(s)
    
    for window_size in range(1, len(s)//2 + 1):
        prev = s[:window_size]
        match_count = 1
        compressed = ""
        
        for i in range(window_size,len(s),window_size):
            curr = s[i:i+window_size]
            
            if prev == curr:
                match_count += 1
            else:
                if match_count > 1:
                    compressed += str(match_count) + prev
                else:
                    compressed += prev
                
                match_count = 1
                prev = curr
        
        if match_count > 1:
            compressed += str(match_count) + prev
        else:
            compressed += prev
        
        min_length = min(min_length, len(compressed))
    
    return min_length


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))