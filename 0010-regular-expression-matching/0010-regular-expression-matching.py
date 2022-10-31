class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[-1][-1] = True
        
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                firstMatch = i < len(s) and p[j] in {s[i], "."}
                if j < len(p) - 1 and p[j + 1] == "*":
                    dp[i][j] = dp[i][j + 2] or (firstMatch and dp[i + 1][j])
                else:
                    dp[i][j] = firstMatch and dp[i + 1][j + 1]
        
        return dp[0][0]