class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = abs(n)
        
        negResult = False
        if x < 0 and n % 2 == 1:
            negResult = True
        
        if n == 1:
            return x
        
        x = abs(x)
        res = 1
        while n > 0:
            if n % 2 == 1:
                res *= x
            x *= x
            n = n // 2
        
        if negResult:
            res = -res
        
        return res