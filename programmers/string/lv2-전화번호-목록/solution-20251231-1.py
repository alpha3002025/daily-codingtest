def solution(phone_book):
    phones = sorted(phone_book)
    
    for i in range(len(phones)-1):
        next_phone = phones[i+1]
        curr_phone = phones[i]
        if next_phone.startswith(curr_phone):
            return False
    
    return True