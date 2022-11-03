class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for flight in flights:
            graph[flight[0]].append((flight[2], flight[1]))
        
        heap = []
        heapq.heappush(heap, (0, src, -1))
        seen = [k] * n
        while heap:
            cost, dest, i = heapq.heappop(heap)
            if i > seen[dest]:
                continue
            
            seen[dest] = i
            if dest == dst:
                return cost
            
            for neiCost, neiDest in graph[dest]:
                heapq.heappush(heap, (cost + neiCost, neiDest, i + 1))
        
        return -1