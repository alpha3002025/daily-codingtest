def solve():
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))

    count = 0

    def backtrack(idx, current_sum):
        nonlocal count

        # 모든 원소를 확인한 경우
        if idx == n:
            return
        
        # 현재 원소를 포함하는 경우
        current_sum += nums[idx]
        if current_sum == s:
            count += 1
        
        # 다음 원소로 진행 (현재 원소 포함)
        backtrack(idx+1, current_sum)
        # 다음 원소로 진행 (현재 원소 미포함)
        backtrack(idx+1, current_sum - nums[idx])
    
    backtrack(0,0)
    print(count)

solve()