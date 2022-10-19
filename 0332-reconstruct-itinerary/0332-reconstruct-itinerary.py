class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = []
        def backtrack(source, currPath):
            if len(currPath) == len(tickets) + 1:
                res.append(currPath)
                return True
            
            for i, nextDest in enumerate(graph[source]):
                if not seen[source][i]:
                    seen[source][i] = True
                    subRes = backtrack(nextDest, currPath + [nextDest])
                    seen[source][i] = False
                    if subRes:
                        return True
            return False
        
        graph = defaultdict(list)
        for ticket in tickets:
            graph[ticket[0]].append(ticket[1])
        
        seen = {}
        
        for source, dests in graph.items():
            dests.sort()
            seen[source] = [False] * len(dests)
        
        path = ["JFK"]
        backtrack("JFK", path)
        return res[0]