class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        
        dp = [[0] * len(nums) for _ in range(len(nums))]
        
        for l in range(len(nums) - 2, 0, -1):
            for r in range(l, len(nums) - 1):
                for i in range(l, r + 1):
                    gain = nums[l - 1] * nums[i] * nums[r + 1]
                    remaining = dp[l][i - 1] + dp[i + 1][r]
                    dp[l][r] = max(remaining + gain, dp[l][r])
        return dp[1][len(nums) - 2]