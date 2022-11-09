class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        ans = []
        
        heap = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(heap)
        
        busy = []
        t = 0
        for j in range(len(tasks)):
            t = max(j, t)

            while busy and busy[0][0] <= t:
                newServer = heapq.heappop(busy)
                t = max(newServer[0], t)
                heapq.heappush(heap, (newServer[1], newServer[2]))
            
            if not heap:
                newServer = heapq.heappop(busy)
                t = max(newServer[0], t)
                heapq.heappush(heap, (newServer[1], newServer[2]))
            
            server = heapq.heappop(heap)
            
            ans.append(server[1])
            heapq.heappush(busy, (t + tasks[j], server[0], server[1]))
            
        return ans