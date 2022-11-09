class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        
        for i in range(2, n + 1):
            l, r = 1, i - 1
            curr = 0
            while l <= r:
                curr = max(curr, max(dp[l], l) * max(dp[r], r))
                l += 1
                r -= 1
            
            dp[i] = curr
        
        return dp[n]