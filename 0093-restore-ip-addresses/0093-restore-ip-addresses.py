class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        if len(s) > 12:
            return []
        
        def backtrack(start, curr, dots):
            intStr = ""
            for i in range(start, len(s)):
                intStr += s[i]
                
                if len(intStr) == 2 and intStr[0] == "0":
                    break
                
                intVal = int(intStr)
                if intVal < 0 or intVal > 255:
                    break
                
                if dots == 3 and len(curr) + len(intStr) - dots == len(s):
                    res.append(curr + intStr)
                    return
                
                backtrack(i + 1, curr + intStr + ".", dots + 1)
            

        backtrack(0, "", 0)
        return res