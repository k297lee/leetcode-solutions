class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        prev = s
        while True:
            length = len(prev)
            
            curr = []
            i = 0
            while i < len(prev) - 1:
                if prev[i] != prev[i + 1] and prev[i].upper() == prev[i + 1]:
                    i += 2
                    continue
                elif prev[i] != prev[i + 1] and prev[i].lower() == prev[i + 1]:
                    i += 2
                    continue
                
                curr.append(prev[i])
                i += 1
            
            if i != len(prev):
                curr.append(prev[-1])
            
            if len(curr) == len(prev):
                return "".join(curr)
            
            prev = "".join(curr)
        
        return ""