from itertools import product

def solution(word):
    answer = 0
    
    dictionary = []
    for window_size in range(1, 6):
        for p in product(['A','E', 'I', 'O', 'U'], repeat=window_size):
            dictionary.append("".join(p))
    
    dictionary.sort()
    return dictionary.index(word)+1


print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))