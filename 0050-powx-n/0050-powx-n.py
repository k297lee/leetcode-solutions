class Solution:
    def myPow(self, x: float, n: int) -> float:
        isNeg = False
        if n < 0:
            isNeg = True
        
        n = abs(n)
        
        resNeg = -1 if x < 0 and n % 2 == 1 else 1
        x = abs(x)
        res = 1
        
        for i in range(n):
            if isNeg:
                res *= 1 / x
            else:
                res *= x
            
            if res == 0:
                break
            elif res == 1:
                break
        
        return res * resNeg