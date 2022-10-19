class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for time in times:
            graph[time[0]].append((time[1], time[2]))
        
        heap = []
        heapq.heappush(heap, (0, k))
        maxTimes = [math.inf] * n
        
        while heap:
            currTime, currNode = heapq.heappop(heap)
            maxTimes[currNode - 1] = min(maxTimes[currNode - 1], currTime)
            
            if currTime > maxTimes[currNode - 1]:
                continue
            
            if currNode not in graph:
                continue
                
            for neighbor in graph[currNode]:
                if maxTimes[neighbor[0] - 1] > currTime + neighbor[1]:
                    maxTimes[neighbor[0] - 1] = currTime + neighbor[1]
                    heapq.heappush(heap, (maxTimes[neighbor[0] - 1], neighbor[0]))
        
        res = max(maxTimes)
        if res == math.inf:
            return -1
        
        return res