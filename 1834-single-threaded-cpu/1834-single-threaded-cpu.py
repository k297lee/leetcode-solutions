class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        available = []
        res = []
        
        tasks_list = [(tasks[i][0], tasks[i][1], i) for i in range(len(tasks))]
        tasks_list.sort()
        
        curr = 0
        i = 0
        
        while i < len(tasks_list) or available:
            if not available and curr < tasks_list[i][0]:
                curr = tasks_list[i][0]
            
            while i < len(tasks_list) and curr >= tasks_list[i][0]:
                _, pt, idx = tasks_list[i]
                heapq.heappush(available, (pt, idx))
                i += 1
            
            pt, idx = heapq.heappop(available)
            curr += pt
            res.append(idx)
        
        return res