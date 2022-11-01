class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        overTarget = set()
        
        for i, triplet in enumerate(triplets):
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                overTarget.add(i)
        
        a, b, c = 0, 0, 0
        for i, triplet in enumerate(triplets):
            if i not in overTarget:
                a, b, c = max(a, triplet[0]), max(b, triplet[1]), max(c, triplet[2])
        
        return [a, b, c] == target