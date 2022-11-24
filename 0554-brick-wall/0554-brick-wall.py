class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges = defaultdict(int)
        totalWidth = sum(wall[0])
        for bricks in wall:
            curr = 0
            for brick in bricks:
                if curr + brick >= totalWidth:
                    break
                edges[curr + brick] += 1
                curr += brick
        
        return len(wall) - max([x for x in edges.values()]) if edges else len(wall)