class Solution:
    def numSquares(self, n: int) -> int:
        squares = [x ** 2 for x in range(int(math.sqrt(n)) + 1)]
        
        dp = [math.inf] * (n + 1)
        
        dp[0] = 0
        
        for i in range(1, n + 1):
            for square in squares:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        
        return dp[-1]