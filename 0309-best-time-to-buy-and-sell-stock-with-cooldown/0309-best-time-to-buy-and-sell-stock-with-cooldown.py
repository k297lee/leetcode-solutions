class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold, held, reset = -math.inf, -math.inf, 0
        
        for price in prices:
            tmp = sold
            sold = max(held, held + price)
            held = max(held, reset - price)
            reset = max(reset, tmp)
        
        return max(sold, reset)
        
        