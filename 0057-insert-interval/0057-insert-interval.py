class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        newMerged = []
        isMerged = False
        for interval in intervals:
            if interval[0] > newInterval[0]:
                newMerged.append(newInterval)
                isMerged = True
            newMerged.append(interval)
        if not isMerged:
            newMerged.append(newInterval)
        newNewMerged = []
        for interval in newMerged:
            if not newNewMerged or newNewMerged[-1][1] < interval[0]:
                newNewMerged.append(interval)
            else:
                newNewMerged[-1][1] = max(newNewMerged[-1][1], interval[1])
                
        return newNewMerged