class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sums = {0}
        total = sum(stones)
        
        for stone in stones:
            curr = set()
            for s in sums:
                if stone + s < total / 2:
                    curr.add(stone + s)
                elif stone + s == total / 2:
                    return 0
                
            sums |= curr
        
        return min([abs(total - 2 * s) for s in sums])