class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        
        subTotal = sum(nums) // 2
        dp = [False] * (subTotal + 1)
        dp[0] = True
        
        for num in nums:
            for j in range(subTotal, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        return dp[subTotal]
        