class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(row, col):
            if row < 0 or row >= len(grid2) or col < 0 or col >= len(grid2[0]) or grid2[row][col] == 0:
                return
            
            grid2[row][col] = 0
            
            for rowOff, colOff in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                newRow = row + rowOff
                newCol = col + colOff
                
                dfs(newRow, newCol)

        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    dfs(i, j)
    
        res = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    dfs(i, j)
                    res += 1

        return res