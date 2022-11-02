class Solution:
    def countOnes(self, i):
        res = 0
        
        while i:
            res += i & 1
            i >>= 1
        
        return res
    
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            res.append(self.countOnes(i))
        
        return res
    
    