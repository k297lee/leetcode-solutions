class DetectSquares:

    def __init__(self):
        self.y_map = defaultdict(set)
        self.freqs = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.y_map[point[1]].add(point[0])
        self.freqs[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        if point[1] not in self.y_map:
            return 0
        
        x_vals = self.y_map[point[1]]
        res = 0
        for x in x_vals:
            if x == point[0]:
                continue
            d = abs(point[0] - x)
            new_y = point[1] + d
            
            if new_y in self.y_map and x in self.y_map[new_y] and point[0] in self.y_map[new_y]:
                res += self.freqs[(point[0], new_y)] * self.freqs[(x, new_y)] * self.freqs[(x, point[1])]
            
            new_y = point[1] - d
            if new_y < 0:
                continue
            
            if new_y in self.y_map and x in self.y_map[new_y] and point[0] in self.y_map[new_y]:
                res += self.freqs[(point[0], new_y)] * self.freqs[(x, new_y)] * self.freqs[(x, point[1])]
        
        return res
                


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)