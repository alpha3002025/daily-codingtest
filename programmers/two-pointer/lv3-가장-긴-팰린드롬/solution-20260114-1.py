def palindrome_length(left, right, s):    
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    
    ## while 문에 의해 한칸 더 갔으므로 길이 보정
    return (right-1) - (left+1) + 1
    # return right - left - 1


def solution(s):
    if len(s) < 2:
        return len(s)
    
    max_length = -float('inf')
    for i in range(len(s)-1):
        res1 = palindrome_length(i, i, s)
        res2 = palindrome_length(i, i+1, s)
        
        max_length = max(max_length, res1, res2)

    return max_length