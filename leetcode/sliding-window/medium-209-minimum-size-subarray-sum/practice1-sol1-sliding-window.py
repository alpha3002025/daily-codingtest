class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
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