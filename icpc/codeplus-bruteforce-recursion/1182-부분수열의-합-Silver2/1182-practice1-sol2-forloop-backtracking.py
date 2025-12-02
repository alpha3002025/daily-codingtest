def solve():
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))
    count = 0

    def backtracking(start, current_sum):
        nonlocal count

        for i in range(start, n):
            current_sum += nums[i]
            if current_sum == s:
                count += 1
            
            backtracking(i+1, current_sum)
            current_sum -= nums[i]
        
    backtracking(0,0)
    print(count)

solve()