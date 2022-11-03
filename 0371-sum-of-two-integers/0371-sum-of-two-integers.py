class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        
        if x < y:
            return self.getSum(b, a)
    
        sign = 1 if a > 0 else -1
        
        if a * b >= 0:
            while y:
                res = x ^ y
                c = (x & y) << 1
                x, y = res, c
        else:
            while y:
                res = x ^ y
                bor = (~x & y) << 1
                x, y = res, bor
        
        return x * sign