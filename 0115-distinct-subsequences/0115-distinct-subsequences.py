class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        
        for i in range(len(s) + 1):
            dp[i][-1] = 1
        for i in range(len(t)):
            dp[-1][i] = 0
            
        
        for i in reversed(range(len(s))):
            for j in reversed(range(len(t))):
                dp[i][j] = dp[i + 1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]
        
        return dp[0][0]