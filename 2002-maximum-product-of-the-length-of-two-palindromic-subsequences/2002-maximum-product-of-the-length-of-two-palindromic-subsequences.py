class Solution:
    def maxProduct(self, s: str) -> int:
        memo = {}
        def isValid(word):
            l, r = 0, len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            
            return True
        
        def backtrack(i, word1, word2):
            if i > len(s):
                return -math.inf
            
            if i == len(s):
                isBothValid = isValid(word1) and isValid(word2)
                if isBothValid:
                    return len(word1) * len(word2)
                else:
                    return -math.inf
            
            key = (i, word1, word2)
            
            if key in memo:
                return memo[key]
            
            memo[key] = max(backtrack(i + 1, word1 + s[i], word2), backtrack(i + 1, word1, word2 + s[i]), backtrack(i + 1, word1, word2))
            
            return memo[key]
        
        return backtrack(0, "", "")