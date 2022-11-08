class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        
        seqs = set()
        
        currStr = ""
        for i in range(10):
            currStr += s[i]
        
        seqs.add(currStr)
        res = []
        added = set()
        for i in range(10, len(s)):
            currStr = currStr[1:]
            currStr += s[i]
            if currStr in seqs and currStr not in added:
                res.append(currStr)
                added.add(currStr)
            else:
                seqs.add(currStr)
        
        return res