class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        hmap = Counter([r[0] / r[1] for r in rectangles])
        
        return sum([item * (item - 1) // 2 for _, item in hmap.items()])