def solution(numbers):
    answer = []
    
    for n in numbers:
        binary_str = bin(n)[2:]
        ## 트리 높이 구하기
        h = get_tree_height(binary_str) 
        print(h)
        
        ## 이진트리로 바꿔서 모두 리프노드로 펼칠때는 2 ** h -1 의 길이를 가진다.
        zero_padding_str = get_zero_padding_str(binary_str, h)
        
        ## 이진트리 정합성체크
        res = 1 if check_valid_tree(zero_padding_str) else 0
        answer.append(res)
            
    return answer


def get_tree_height(binary_str):
    h = 0
    
    while (2**h - 1) < len(binary_str):
        h += 1
    
    return h


def get_zero_padding_str(binary_str, h):
    full_length = 2**h - 1
    zero_padding_binary_str = binary_str.zfill(full_length)
    return zero_padding_binary_str


def check_valid_tree(binary_str):
    if len(binary_str) == 1:
        return True
    
    mid = len(binary_str) // 2
    root = binary_str[mid]
    l_sub = binary_str[:mid]
    r_sub = binary_str[mid+1:]
    
    if binary_str[mid] == '0':
        if '1' in l_sub or '1' in r_sub:
            return False
    
    l_res = check_valid_tree(l_sub)
    r_res = check_valid_tree(r_sub)
    
    return True if l_res and r_res else False