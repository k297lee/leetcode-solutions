class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
            text1, text2 = text2, text1
        
        prev = [0] * (len(text1) + 1)
        
        for col in reversed(range(len(text2))):
            curr = [0] * (len(text1) + 1)
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    curr[row] = 1 + prev[row + 1]
                else:
                    curr[row] = max(curr[row + 1], prev[row])
            prev = curr
        return prev[0]