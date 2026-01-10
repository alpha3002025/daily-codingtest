class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        # DP 테이블을 매우 작은 값으로 초기화
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                curr_product = nums1[i-1] * nums2[j-1]
                
                dp[i][j] = max(
                    curr_product,                    # 1. 현재 두 수만 선택 (새로운 시작)
                    dp[i-1][j-1] + curr_product,     # 2. 이전 수열에 현재 두 수 추가
                    dp[i-1][j],                      # 3. nums1[i]를 제외(코드의 nums1[i-1])하고 이전 상태를 가져옴
                    dp[i][j-1]                       # 4. nums2[j]를 제외(코드의 nums2[j-1])하고 이전 상태를 가져옴
                )
        
        return dp[n][m]