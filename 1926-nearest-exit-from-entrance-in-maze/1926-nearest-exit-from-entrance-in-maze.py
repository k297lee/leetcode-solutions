class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = deque()
        
        if maze[entrance[0]][entrance[1]] == "+":
            return -1
        
        q.append((entrance[0], entrance[1]))
        maze[entrance[0]][entrance[1]] = "+"
        
        steps = 0
        while q:
            size = len(q)
            for i in range(size):
                i, j = q.popleft()
                if (i == 0 or j == 0 or i == len(maze) - 1 or j == len(maze[0]) - 1) and [i, j] != entrance:
                    return steps

                for rowOff, colOff in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    newRow = i + rowOff
                    newCol = j + colOff

                    if newRow < 0 or newRow >= len(maze) or newCol < 0 or newCol >= len(maze[0]):
                        continue

                    if maze[newRow][newCol] == "+":
                        continue

                    q.append((newRow, newCol))
                    maze[newRow][newCol] = "+"
            
            steps += 1
        
        return -1