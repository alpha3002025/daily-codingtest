def solution(n, bans):
    # 각 길이별로 가능한 문자열의 개수 누적합 미리 계산
    # cum_counts[k] = 길이가 k 이하인 모든 문자열의 개수
    # 예: cum_counts[1] = 26, cum_counts[2] = 26 + 26^2
    cum_counts = [0] * 12
    current_sum = 0
    pow26 = [1] * 12
    for i in range(1, 12):
        pow26[i] = pow26[i-1] * 26
        current_sum += pow26[i]
        cum_counts[i] = current_sum

    # 문자열을 1-based 인덱스로 변환하는 함수
    def str_to_val(s):
        L = len(s)
        # 길이가 L보다 작은 모든 문자열의 개수를 더함
        val = cum_counts[L-1]
        
        # 길이가 L인 문자열 내에서의 순서(0-based) 계산
        rank = 0
        for i, char in enumerate(s):
            digit = ord(char) - ord('a')
            rank += digit * pow26[L - 1 - i]
        
        # 1-based 인덱스로 반환
        return val + rank + 1

    # 1-based 인덱스를 문자열로 변환하는 함수
    def val_to_str(v):
        # 해당 인덱스가 속하는 길이 L 찾기
        L = 1
        while L <= 11:
            if v <= cum_counts[L]:
                break
            L += 1
        
        # 길이가 L인 문자열 내에서의 순서(0-based)
        rank = v - cum_counts[L-1] - 1
        
        # 26진법 변환
        chars = []
        for i in range(L):
            power = pow26[L - 1 - i]
            digit = rank // power
            chars.append(chr(digit + ord('a')))
            rank %= power
        
        return "".join(chars)

    # bans 배열을 정수로 변환 후 정렬
    ban_vals = []
    for b in bans:
        ban_vals.append(str_to_val(b))
    
    ban_vals.sort()
    
    # n번째 유효한 주문 찾기
    # n에 대해, 자신보다 작거나 같은 삭제된 주문의 개수만큼 n을 증가시킴
    curr = n
    for b in ban_vals:
        if b <= curr:
            curr += 1
        else:
            # 정렬되어 있으므로 더 이상 검사할 필요 없음
            break
            
    return val_to_str(curr)
