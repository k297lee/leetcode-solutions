class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        shells = n // 2
        
        for shell in range(shells):
            for i in range(shell, n - shell - 1):
                matrix[n - 1 - i][shell], matrix[i][n - shell - 1], matrix[n - shell - 1][n - 1 - i], matrix[shell][i] = \
                matrix[n - shell - 1][n - 1 - i], matrix[shell][i], matrix[i][n - shell - 1], matrix[n - 1 - i][shell]
                