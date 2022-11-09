class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start, curr):
            if len(curr) == k:
                res.append(curr[:])
                return
            
            for i in range(start + 1, n + 1):
                curr.append(i)
                backtrack(i, curr)
                curr.pop()
        
        backtrack(0, [])
        return res