class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_times = sorted([i[0] for i in intervals])
        end_times = sorted([i[1] for i in intervals])
        
        l, r = 0, 0
        
        res = 0
        while l < len(intervals):
            if start_times[l] >= end_times[r]:
                res -= 1
                r += 1
            
            res += 1
            l += 1
        
        return res