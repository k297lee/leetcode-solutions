class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            grid[row][col] = "0"
            for rowOff, colOff in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                newRow = row + rowOff
                newCol = col + colOff
                
                if newRow < 0 or newRow >= len(grid) or newCol < 0 or newCol >= len(grid[0]):
                    continue
                
                if grid[newRow][newCol] == "1":
                    dfs(newRow, newCol)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        
        return count