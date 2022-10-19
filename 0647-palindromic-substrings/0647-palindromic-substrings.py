class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = True
            if i + 1 < n:
                dp[i][i + 1] = s[i] == s[i + 1]
            
        for width in range(2, n):
            for i in range(n - width):
                dp[i][i + width] = dp[i + 1][i + width - 1] and s[i] == s[i + width]
        
        s = 0
        for i in range(n):
            for j in range(n):
                if dp[i][j]:
                    s += 1
        return s