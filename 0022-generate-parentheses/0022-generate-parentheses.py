class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(curr, i, j):
            if len(curr) == n * 2:
                res.append("".join(curr))
                return
            
            if i < n:
                curr.append("(")
                backtrack(curr, i + 1, j)
                curr.pop(len(curr) - 1)
            
            if j < i:
                curr.append(")")
                backtrack(curr, i, j + 1)
                curr.pop(len(curr) - 1)
        
        backtrack([], 0, 0)
        return res