class DSU:
    def __init__(self):
        self.parents = list(range(2001))
        self.ranks = [0] * 2001
    
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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU()
        count = 0

        for edge in edges:
            dsu.union(edge[0], edge[1])
        
        seen = set()
        for i in range(n):
            p = dsu.find(i)
            if p not in seen:
                seen.add(p)
                count += 1
        
        return count