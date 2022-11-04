class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        numSet = set()
        for num in nums:
            numSet.add(num)
        
        maxSeq = 1
        for num in numSet:
            if num - 1 not in numSet:
                currSeq = 0
                currNum = num
                while currNum in numSet:
                    currSeq += 1
                    currNum += 1
            
                maxSeq = max(maxSeq, currSeq)
        
        return maxSeq