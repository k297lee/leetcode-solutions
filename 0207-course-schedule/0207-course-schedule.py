class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for prereq in prerequisites:
            source = prereq[1]
            dest = prereq[0]
            graph[source].append(dest)
        
        def is_cyclic(curr):
            if curr in seen:
                return False
            
            if path[curr]:
                return True
            
            path[curr] = True
            
            res = False
            for neighbor in graph[curr]:
                if is_cyclic(neighbor):
                    res = True
                    break
            
            path[curr] = False
            seen.add(curr)
            return res
        
        path = [False] * numCourses
        seen = set()
        
        for i in range(numCourses):
            if i not in seen and is_cyclic(i):
                return False
            
        return True