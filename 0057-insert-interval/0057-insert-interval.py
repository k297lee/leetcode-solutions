class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        start, end = newInterval[0], newInterval[1]
        i, n = 0, len(intervals)
        
        res = []
        while i < n and start > intervals[i][0]:
            res.append(intervals[i])
            i += 1
        
        if res and start <= res[-1][1]:
            start = res[-1][0]
            end = max(end, res[-1][1])
            res[-1][1] = end
        else:
            res.append([start, end])
        
        while i < n and intervals[i][0] <= end:
            end = max(end, intervals[i][1])
            i += 1
        
        res[-1][1] = end
        
        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res
        
        
        