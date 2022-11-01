class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        
        dp[-1] = True
        
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= len(nums):
                dp[i] = True
            else:
                for j in range(i, i + nums[i] + 1):
                    dp[i] = dp[i] or dp[j]
        return dp[0]