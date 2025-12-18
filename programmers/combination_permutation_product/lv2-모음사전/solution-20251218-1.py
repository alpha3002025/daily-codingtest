from itertools import product

def solution(word):
    """
    5**1 + 5**2 + 5**3 + 5**4 + 5**5
    5 + 25 + 125 + 625 + 3125 = 3905
    """
    
    dictionary = []
    for len in range(1, 6):
        for p in product(['A','E','I','O','U'], repeat=len):
            dictionary.append("".join(p))
    
    dictionary.sort()
    return dictionary.index(word) + 1