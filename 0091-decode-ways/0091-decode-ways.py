class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        
        if s[0] == "0":
            return 0
        elif len(s) == 1:
            return 1
        elif s[1] == "0" and s[0] != "1" and s[0] != "2":
            return 0
        
        dp[0] = 1
        dp[1] = 2 if (s[0] == "1" and s[1] != "0") or (s[0] == "2" and 0 < int(s[1]) < 7) else 1
        
        for i in range(2, len(s)):
            if s[i] == "0" and i == 0:
                return 0
            elif s[i] == "0" and s[i - 1] != "1" and s[i - 1] != "2":
                return 0
            
            if (s[i - 1] == "1" and s[i] != "0") or (s[i - 1] == "2" and 0 < int(s[i]) < 7) :
                dp[i] = dp[i - 1] + dp[i - 2]
            elif s[i] == "0":
                dp[i] = dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        print(dp)
        return dp[-1]