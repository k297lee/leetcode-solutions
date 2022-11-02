class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        end = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] < end:
                end = min(end, interval[1])
                res += 1
            else:
                end = interval[1]
        
        return res