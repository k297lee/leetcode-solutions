class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        res = []
        pCounter = Counter(p)
        sCounter = Counter()
        
        for i in range(len(s)):
            sCounter[s[i]] += 1
            
            if i >= len(p):
                if sCounter[s[i - len(p)]] == 1:
                    sCounter.pop(s[i - len(p)])
                else:
                    sCounter[s[i - len(p)]] -= 1
            
            if pCounter == sCounter:
                res.append(i - len(p) + 1)
        
        return res
                    