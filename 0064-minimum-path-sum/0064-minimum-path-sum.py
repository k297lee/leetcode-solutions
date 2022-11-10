class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        prev = [0] * len(grid[0])
        
        for i in range(len(grid)):
            curr = [0] * len(grid[0])
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    curr[j] = grid[i][j]
                elif i == 0:
                    curr[j] = curr[j - 1] + grid[i][j]
                elif j == 0:
                    curr[j] = prev[j] + grid[i][j]
                else:
                    curr[j] = min(prev[j], curr[j - 1]) + grid[i][j]
            prev = curr
        
        return prev[-1]