def solution(s):
    answer = 0
    min_length = len(s)
    for window_size in range(1, len(s)//2 +1):
        prev = s[:window_size]
        
        match_count = 1
        compressed_str = ""
        for idx in range(window_size, len(s), window_size):
            curr = s[idx: idx+window_size]
            
            if prev == curr:
                match_count += 1
            else:
                if match_count == 1:
                    result = prev
                else:
                    result = str(match_count) + curr
                compressed_str += result
                match_count = 1
                prev = curr
        
        if match_count == 1:
            result = prev
        else:
            result = str(match_count) + curr
        compressed_str += result
        
        min_length = min(min_length, len(compressed_str))
            
    return min_length


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))