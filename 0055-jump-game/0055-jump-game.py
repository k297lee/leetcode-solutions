class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        
        dp[-1] = True
        lastPos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastPos:
                dp[i] = True
                lastPos = i
        return dp[0]