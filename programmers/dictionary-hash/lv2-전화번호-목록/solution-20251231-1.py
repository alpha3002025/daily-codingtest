def solution(phone_book):
    hash = {}
    
    for number in phone_book:
        hash[number] = True
    
    for number in phone_book:
        curr = ""
        for c in number:
            curr += c
            if curr != number and curr in hash:
                return False
                
    return True