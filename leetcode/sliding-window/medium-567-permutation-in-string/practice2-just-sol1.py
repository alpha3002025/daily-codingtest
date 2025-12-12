def solution(s1: str, s2: str) -> bool:
    len_s1, len_s2 = len(s1), len(s2)
    if len_s1 > len_s2:
        return False

    s1_map = [0] * 26
    s2_map = [0] * 26
    
    for i in range(len_s1):
        s1_map[ord(s1[i]) - ord('a')] += 1
        s2_map[ord(s2[i]) - ord('a')] += 1
    
    for i in range(len_s1, len_s2):
        if s1_map == s2_map:
            return True
        s2_map[ord(s2[i]) - ord('a')] += 1
        s2_map[ord(s2[i - len_s1]) - ord('a')] -= 1
    
    return s1_map == s2_map


input1 = ("ab","eidbaooo")
input2 = ("ab","eidboaoo")

print(f"input = {input1}, output = {solution(*input1)}")
print(f"input = {input2}, output = {solution(*input2)}")
