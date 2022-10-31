class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        
        if target > total:
            return 0
        
        dp = [[0] * (2 * total + 1) for _ in range(len(nums))]
        dp[0][total + nums[0]] = 1
        dp[0][total - nums[0]] += 1
        
        for i in range(1, len(nums)):
            for j in range(-total, total + 1):
                if dp[i - 1][j + total]:
                    dp[i][j + total + nums[i]] += dp[i - 1][j + total]
                    dp[i][j + total - nums[i]] += dp[i - 1][j + total]
        
        return dp[-1][total + target]