class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        
        subTotal = sum(nums) // 2
        dp = [[False] * (subTotal + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = True
        
        for i in range(1, len(nums) + 1):
            for j in range(subTotal + 1):
                if j < nums[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
        
        return dp[-1][subTotal]
        