def solution(s):
    if len(s) == 1:
        return 1
    
    min_length = len(s)
    n = len(s)
    
    for unit in range(1, n//2 + 1):
        count = 1
        prev = s[:unit]
        compressed = ""
        
        for i in range(unit, n, unit):
            curr = s[i:i+unit]
            
            if curr == prev:
                count += 1
            else:
                if count > 1:
                    compressed += str(count) + prev
                else:
                    compressed += prev
                count = 1
                prev = curr
        
        if count > 1:
            compressed += str(count) + prev
        else:
            compressed += prev
            
        min_length = min(min_length, len(compressed))
    return min_length


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))