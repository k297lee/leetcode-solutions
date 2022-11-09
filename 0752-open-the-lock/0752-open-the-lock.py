class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque()
        q.append(("0000", 0))
        notAllowed = set(deadends)
        if ("0000") in notAllowed:
            return -1
        notAllowed.add("0000")
        while q:
            curr, step = q.popleft()
            
            if curr == target:
                return step
            
            for i in range(4):
                for x in [-1, 1]:
                    newVal = str((int(curr[i]) + x) % 10)

                    newCurr = curr[:i] + newVal + curr[i+1:]

                    if newCurr not in notAllowed:
                        q.append((newCurr, step + 1))
                        notAllowed.add(newCurr)
        
        return -1