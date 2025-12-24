from itertools import product

def solution(word):
    words = []
    for curr_len in range(1, 6):
        for w in product(["A", "E", "I", "O", "U"], repeat=curr_len):
            curr_word = "".join(w)
            words.append(curr_word)
    
    words.sort()
    cnt = 0
    for w in words:
        if word == w:
            break
        cnt += 1
    
    answer = cnt+1
    return answer