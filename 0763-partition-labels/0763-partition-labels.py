class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastSeen = {}
        
        def mergeIntervals(self, intervals):
            intervals.sort(key=lambda x: x[0])
            merged = []
            for interval in intervals:
                if not merged or merged[-1][1] < interval[0]:
                    merged.append(interval)
                else:
                    merged[-1][1] = max(merged[-1][1], interval[1])
            
            return merged
        
        for i, c in enumerate(s):
            if c in lastSeen:
                lastSeen[c] = (lastSeen[c][0], i)
            else:
                lastSeen[c] = (i, i)
        
        res = mergeIntervals(self, [list(kvp[1]) for kvp in lastSeen.items()])
        
        return [x[1] - x[0] + 1 for x in res]
        
    