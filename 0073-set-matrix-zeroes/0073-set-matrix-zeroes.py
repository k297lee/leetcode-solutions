class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        
        colZero = False
        
        for i in range(m):
            if matrix[i][0] == 0:
                colZero = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
                    
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
        
        if colZero:
            for i in range(m):
                matrix[i][0] = 0