class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0], reverse=True)
        heap = []
        res = {}
        for q in sorted(queries):
            while intervals and intervals[-1][0] <= q:
                i, j = intervals.pop()
                if j >= q:
                    heapq.heappush(heap, ((j - i + 1), j))
            
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            resVal = heap[0][0] if heap else -1
            res[q] = resVal
        
        return [res[q] for q in queries]