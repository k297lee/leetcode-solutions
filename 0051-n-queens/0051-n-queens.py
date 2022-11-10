class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        
        board = [["." for x in range(n)] for y in range(n)]
        
        def backtrack(r, cols, diags, antiDiags, curr):
            if r == n:
                res.append(createBoard(curr))
                return
            
            for c in range(n):
                curr_diag = r - c
                curr_antiDiag = r + c
                if curr_diag in diags or curr_antiDiag in antiDiags or c in cols:
                    continue
                
                cols.add(c)
                diags.add(curr_diag)
                antiDiags.add(curr_antiDiag)
                
                curr[r][c] = "Q"
                backtrack(r + 1, cols, diags, antiDiags, curr)
                
                cols.remove(c)
                diags.remove(curr_diag)
                antiDiags.remove(curr_antiDiag)
                curr[r][c] = "."
        
        def createBoard(curr):
            b = []
            for i in curr:
                b.append("".join(i))
            return b
        
        backtrack(0, set(), set(), set(), board)
        return res