class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        
        for i in reversed(range(len(s))):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = 1
                elif i == j + 1 and s[i] == s[j]:
                    dp[i][j] = 2
                elif s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        return dp[0][-1]