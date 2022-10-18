class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inEdges = [0] * numCourses
        graph = defaultdict(list)
        for i in range(len(prerequisites)):
            to = prerequisites[i][0]
            fr = prerequisites[i][1]
            graph[fr].append(to)
            inEdges[to] += 1
        
        ordering = []
        
        q = deque()
        for i in range(numCourses):
            if inEdges[i] == 0:
                q.append(i)
                ordering.append(i)
                
        
        numFound = 0
        while q:
            node = q.popleft()
            numFound += 1
            if node in graph:
                for edge in graph[node]:
                    inEdges[edge] -= 1
                    if inEdges[edge] == 0:
                        ordering.append(edge)
                        q.append(edge)
        
        if numFound != numCourses:
            return []
        
        return ordering