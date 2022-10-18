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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dsu = DSU(n)
        
        for edge in edges:
            if not dsu.union(edge[0], edge[1]):
                return False
        
        seen = set()
        count = 0
        for i in range(n):
            p = dsu.find(i)
            if p not in seen:
                count += 1
                seen.add(p)
            if count > 1:
                return False
        
        return True