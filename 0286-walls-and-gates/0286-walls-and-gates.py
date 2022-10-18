class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q = deque()
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append((i, j))
        
        currDist = 1
        q.append((-1, -1))
        
        while q:
            c = q.popleft()
            row = c[0]
            col = c[1]
            
            if row == -1:
                currDist += 1
                if q:
                    q.append((-1, -1))
            
            for rowOff, colOff in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                newRow = row + rowOff
                newCol = col + colOff
                
                if newRow >= 0 and newRow < len(rooms) and newCol >= 0 and newCol < len(rooms[0]):
                    if rooms[newRow][newCol] == 2147483647:
                        rooms[newRow][newCol] = currDist
                        q.append((newRow, newCol))
            