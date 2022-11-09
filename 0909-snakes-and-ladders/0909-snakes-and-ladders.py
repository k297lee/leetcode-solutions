class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        q = deque()
        q.append((1, 0))
        seen = set()
        
        while q:
            pos, step = q.popleft()
            row, col = self.convert(pos, n)
            
            if board[row][col] != -1:
                pos = board[row][col]
            
            if pos == n * n:
                return step
            
            for i in range(1, 7):
                newPos = pos + i
                if newPos <= n * n and newPos not in seen:
                    seen.add(newPos)
                    q.append((newPos, step + 1))
        
        return -1
    
    def convert(self, pos, n):
        row = (pos - 1) // n
        col = (pos - 1) % n
        
        
        if row % 2 == 1:
            col = n - 1 - col

        row = n - 1 - row
        return row, col