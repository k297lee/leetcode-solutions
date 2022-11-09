class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s1, s2 = "", ""
        
        s += s
        
        for i in range(len(s)):
            if i % 2 == 0:
                s1 += "1"
                s2 += "0"
            else:
                s1 += "0"
                s2 += "1"
        
        curr1, curr2, res = 0, 0, math.inf
        
        l, r = 0, 0
        
        while r < len(s):
            if s[r] != s1[r]:
                curr1 += 1
            elif s[r] != s2[r]:
                curr2 += 1
            
            if r - l + 1 < n:
                r += 1
            else:
                res = min(res, curr1, curr2)
                if s[l] != s1[l]:
                    curr1 -= 1
                elif s[l] != s2[l]:
                    curr2 -= 1
                
                l += 1
                r += 1
        
        return res