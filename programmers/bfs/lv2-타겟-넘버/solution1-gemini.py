from collections import deque

def solution(numbers, target):
    # 큐에 초기 합계 0을 넣고 시작
    queue = deque([0])
    
    # 각 숫자를 순회하며 트리 확장
    for num in numbers:
        length = len(queue)
        # 현재 레벨(큐에 있는 모든 합계들)에 대해 반복
        for _ in range(length):
            current_sum = queue.popleft()
            
            # 현재 합계에 num을 더하는 경우
            queue.append(current_sum + num)
            # 현재 합계에서 num을 빼는 경우
            queue.append(current_sum - num)
            
    # 모든 숫자를 처리한 후, 큐에 남은 값들 중 target과 일치하는 개수를 반환
    return queue.count(target)