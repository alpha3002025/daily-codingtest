def solution(numbers, target):
    # n: 현재 사용하고 있는 numbers의 인덱스
    # current_sum: 현재까지의 합
    def dfs(index, current_sum):
        # Base Case: 모든 숫자를 다 사용했을 때
        if index == len(numbers):
            # 타겟 넘버를 만들었으면 1 반환, 아니면 0 반환
            return 1 if current_sum == target else 0
        
        # Recursive Case:
        # (+)를 선택한 경우와 (-)를 선택한 경우의 합을 구함
        return dfs(index + 1, current_sum + numbers[index]) + \
               dfs(index + 1, current_sum - numbers[index])
               
    return dfs(0, 0)