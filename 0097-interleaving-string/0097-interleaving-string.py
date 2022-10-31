class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        if len(s1) == 0:
            return s2 == s3
        elif len(s2) == 0:
            return s1 == s3
        
        prev = [False] * (len(s2) + 1)
        
        for i in range(len(s1) + 1):
            curr = [False] * (len(s2) + 1)
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    curr[j] = True
                elif i == 0:
                    curr[j] = curr[j - 1] and s2[j - 1] == s3[i + j - 1]
                elif j == 0:
                    curr[j] = prev[j] and s1[i - 1] == s3[i + j - 1]
                else:
                    curr[j] = (curr[j - 1] and s2[j - 1] == s3[i + j - 1]) or (prev[j] and s1[i - 1] == s3[i + j - 1])
            prev = curr
        return prev[-1]