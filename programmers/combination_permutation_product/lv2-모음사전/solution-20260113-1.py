from itertools import product

def solution(word):
    answer = 0
    
    dictionary = []
    for window_size in range(1, 6):
        for curr_word in product(["A", "E", "I", "O", "U"], repeat=window_size):
            dictionary.append("".join(curr_word))
    
    dictionary.sort()
    
    idx = 0
    for item in dictionary:
        if item == word:
            break
        idx += 1
    
    return idx + 1


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))