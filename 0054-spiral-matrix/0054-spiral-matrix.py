class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        layers = min(m // 2, n // 2)
        
        res = []
        count = 0
        for layer in range(layers + 1):
            # top
            for i in range(layer, n - layer):
                res.append(matrix[layer][i])
                count += 1
            
            if count == m * n:
                return res
            
            for i in range(layer + 1, m - layer):
                res.append(matrix[i][n - layer - 1])
                count += 1
            
            if count == m * n:
                return res
            
            for i in range(layer + 1, n - layer):
                res.append(matrix[m - layer - 1][n - i - 1])
                count += 1
            
            if count == m * n:
                return res
            
            for i in range(layer + 1, m - layer - 1):
                res.append(matrix[m - i - 1][layer])
                count += 1
            
            if count == m * n:
                return res
                
        return res