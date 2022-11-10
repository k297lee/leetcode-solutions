class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for src, dest in connections:
            graph[src].append((dest, 1))
            graph[dest].append((src, 0))
        
        q = deque()
        q.append(0)
        seen = set()
        seen.add(0)
        res = 0
        while q:
            node = q.popleft()
            
            for nei, cost in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    res += cost
                    q.append(nei)
        
        return res