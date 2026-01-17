def check_tree(binary_sub):
    # 기저 사례: 길이가 1이면(리프 노드) 항상 True (1이든 0이든 상관없음)
    if len(binary_sub) == 1:
        return True
    
    mid = len(binary_sub) // 2
    root = binary_sub[mid]
    left_sub = binary_sub[:mid]
    right_sub = binary_sub[mid+1:]
    
    # 루트가 0인데 자식 중에 1이 하나라도 있으면 False (불가능한 트리)
    if root == '0':
        # 자식 서브트리에 '1'이 포함되어 있다면 유효하지 않음
        if '1' in left_sub or '1' in right_sub:
            return False
            
    # 그 외의 경우(루트가 1이거나, 루트가 0이고 자식도 다 0인 경우)
    # 왼쪽과 오른쪽 서브트리도 재귀적으로 확인
    return check_tree(left_sub) and check_tree(right_sub)

def solution(numbers):
    answer = []
    
    for num in numbers:
        # 1. 이진수 변환 (0b 접두어 제거)
        binary_str = bin(num)[2:]
        length = len(binary_str)
        
        # 2. 포화 이진트리 길이로 맞추기 (Padding)
        # 2^h - 1 형태가 될 때까지 h를 증가
        h = 0
        while (2**h - 1) < length:
            h += 1
        
        full_length = 2**h - 1
        # 앞부분에 0을 채워서 길이 맞춤
        padded_binary = binary_str.zfill(full_length)
        
        # 3. 트리 유효성 검사
        if check_tree(padded_binary):
            answer.append(1)
        else:
            answer.append(0)
            
    return answer


print(solution([7,42,5]))
print(solution([63,111,95]))