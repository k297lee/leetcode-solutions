class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        topRight, bottomLeft = sum(grid[0]), 0
        res = math.inf
        
        for i in range(len(grid[0])):
            topRight -= grid[0][i]
            res = min(res, max(topRight, bottomLeft))
            bottomLeft += grid[1][i]
        
        return res