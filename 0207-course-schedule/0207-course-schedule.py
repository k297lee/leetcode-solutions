class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)
        
        for prereq in prerequisites:
            courses[prereq[1]].append(prereq[0])
        
        seen = set()
        
        def cyclic(curr, courses, path):
            if curr in seen:
                return False
            if path[curr]:
                return True
            
            path[curr] = True
            
            res = False
            for course in courses[curr]:
                res = cyclic(course, courses, path)
                if res:
                    break
            
            path[curr] = False
            seen.add(curr)
            return res
    
        path = [False] * numCourses
    
        for c in range(numCourses):
            if c not in seen and cyclic(c, courses, path):
                return False
        
        return True