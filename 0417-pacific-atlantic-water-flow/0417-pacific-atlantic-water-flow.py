class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_reachable = set()
        atlantic_reachable = set()
        
        def dfs(row, col, reachable):
            reachable.add((row, col))
            
            for rowOff, colOff in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                newRow = row + rowOff
                newCol = col + colOff
                
                if 0 <= newRow < len(heights) and 0 <= newCol < len(heights[0]) and (newRow, newCol) not in reachable and heights[newRow][newCol] >= heights[row][col]:
                    dfs(newRow, newCol, reachable)
        
        for i in range(len(heights)):
            dfs(i, 0, pacific_reachable)
            dfs(i, len(heights[0]) - 1, atlantic_reachable)
        
        for i in range(len(heights[0])):
            dfs(0, i, pacific_reachable)
            dfs(len(heights) - 1, i, atlantic_reachable)
            
        return list(pacific_reachable.intersection(atlantic_reachable))