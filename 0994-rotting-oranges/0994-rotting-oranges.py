class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        remaining = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    remaining += 1
        
        q.append((-1, -1))

        elapsed = -1
        while q:
            c = q.popleft()
            row = c[0]
            col = c[1]
            
            if row < 0:
                elapsed += 1
                if q:
                    q.append((-1, -1))
                continue
            
            for rowOff, colOff in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                newRow = row + rowOff
                newCol = col + colOff
                
                if newRow >= 0 and newRow < len(grid) and newCol >= 0 and newCol < len(grid[0]):
                    if grid[newRow][newCol] == 1:
                        grid[newRow][newCol] = 2
                        remaining -= 1
                        q.append((newRow, newCol))
        
        return elapsed if remaining == 0 else -1