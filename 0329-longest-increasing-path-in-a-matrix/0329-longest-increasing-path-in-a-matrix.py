class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dirs = [(-1, 0), (0, 1), (0, -1), (1, 0)]
        dp = [[0] * (n) for _ in range(m)]
        
        def dfs(row, col):
            if dp[row][col]:
                return dp[row][col]
            
            for rowOff, colOff in dirs:
                newRow = row + rowOff
                newCol = col + colOff
                
                if newRow < 0 or newRow >= m or newCol < 0 or newCol >= n:
                    continue
                
                if matrix[row][col] < matrix[newRow][newCol]:
                    dp[row][col] = max(dfs(newRow, newCol), dp[row][col])
            dp[row][col] += 1
            return dp[row][col]
        
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(dfs(i, j), res)
        return res