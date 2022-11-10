class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)

        memo = {}
        def dp(i, j):
            if i > j: 
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            parity = (N - (j - i)) % 2
            res = 0
            if parity == 1:  # first player
                res = max(piles[i] + dp(i+1,j), piles[j] + dp(i,j-1))
            else:
                res = min(-piles[i] + dp(i+1,j), -piles[j] + dp(i,j-1))
            
            memo[(i, j)] = res
            return res

        return dp(0, N - 1) > 0