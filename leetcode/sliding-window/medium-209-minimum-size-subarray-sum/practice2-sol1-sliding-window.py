def solution(target, nums):
    left = 0
    right = 0
    current_window_sum = 0
    res = float('inf')

    for right in range(0, len(nums)):
        current_window_sum += nums[right]

        while current_window_sum >= target:
            res = min(res, right - left + 1)
            current_window_sum -= nums[left]
            left+=1
    return res if res != float('inf') else 0


# input1 = (7, [2,3,1,2,4,3])
input2 = (4, [1,4,4])
# input3 = (11, [1,1,1,1,1,1,1,1])

# print(solution(*input1))
print(solution(*input2))
# print(solution(*input3))