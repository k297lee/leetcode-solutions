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
        
        # sentinel
        q.append((-1, -1))
        dist = 1
        while q:
            room = q.popleft()
            
            i = room[0]
            j = room[1]
            
            if i == -1 and j == -1:
                if not q:
                    continue
                q.append((-1, -1))
                dist += 1
                continue
            
            for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                newX = i + x
                newY = j + y
                
                if newX < 0 or newX >= len(rooms) or newY < 0 or newY >= len(rooms[0]):
                    continue
                
                if rooms[newX][newY] == 2147483647:
                    rooms[newX][newY] = dist
                    q.append((newX, newY))