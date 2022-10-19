class DSU:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        
        if xr == yr:
            return False
        elif self.ranks[xr] < self.ranks[yr]:
            self.parents[xr] = yr
        elif self.ranks[xr] > self.ranks[yr]:
            self.parents[yr] = xr
        else:
            self.parents[yr] = xr
            self.ranks[xr] += 1
        return True

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dsu = DSU(len(grid) * len(grid))
        
        seen = [[False] * len(grid) for _ in range(len(grid))]
        sorted_grid = sorted([(i, j) for i in range(len(grid)) for j in range(len(grid))], key=lambda x: grid[x[0]][x[1]])
        for i, j in sorted_grid:
            seen[i][j] = True
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if x >= 0 and x < len(grid) and y >= 0 and y < len(grid) and seen[x][y]:
                    dsu.union(i * len(grid) + j, x * len(grid) + y)

            if dsu.find(0) == dsu.find(len(grid) * len(grid) - 1):
                return grid[i][j]