class Solution:
    def checkValidString(self, s: str) -> bool:
        l, r = 0, 0
        
        for c in s:
            l += 1 if c == "(" else -1
            r += 1 if c != ")" else -1
            
            if r < 0:
                return False
            l = max(l, 0)
        
        return l == 0