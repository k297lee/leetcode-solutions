class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        prev = [0] * len(s)
        for i in reversed(range(len(s))):
            curr = [0] * len(s)
            for j in range(i, len(s)):
                if i == j:
                    curr[j] = 1
                elif i == j + 1 and s[i] == s[j]:
                    curr[j] = 2
                elif s[i] == s[j]:
                    curr[j] = prev[j - 1] + 2
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr
        
        return prev[-1]