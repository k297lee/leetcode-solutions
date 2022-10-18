class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def bfs(row, col):
            q = deque()
            q.append((row, col))
            while q:
                c = q.popleft()
                for rowOff, colOff in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    newRow = c[0] + rowOff
                    newCol = c[1] + colOff
                    
                    if newRow >= 0 and newRow < len(board) and newCol >= 0 and newCol < len(board[0]) and board[newRow][newCol] == "O":
                        board[newRow][newCol] = "E"
                        q.append((newRow, newCol))
        
        for i in range(len(board)):
            if board[i][0] == "O":
                board[i][0] = "E"
                bfs(i, 0)
            if board[i][len(board[0]) - 1] == "O":
                board[i][len(board[0]) - 1] = "E"
                bfs(i, len(board[0]) - 1)
        for i in range(len(board[0])):
            if board[0][i] == "O":
                board[0][i] = "E"
                bfs(0, i)
            if board[len(board) - 1][i] == "O":
                board[len(board) - 1][i] = "E"
                bfs(len(board) - 1, i)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "E":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"