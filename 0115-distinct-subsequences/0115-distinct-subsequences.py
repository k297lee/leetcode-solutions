class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        
        prev = [0] * (len(t) + 1)
        prev[len(t)] = 1
        
        for i in reversed(range(len(s))):
            curr = [0] * (len(t) + 1)
            curr[len(t)] = 1
            for j in reversed(range(len(t))):
                curr[j] = prev[j]
                if s[i] == t[j]:
                    curr[j] += prev[j + 1]
            prev = curr
        
        return prev[0]