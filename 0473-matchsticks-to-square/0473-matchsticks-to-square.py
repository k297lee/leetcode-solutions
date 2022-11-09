class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        
        if total % 4 != 0:
            return False
        
        sideLength = total // 4
        sides = [0] * 4
        
        def backtrack(start):
            if start == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sideLength

            for i in range(4):
                if sides[i] + matchsticks[start] <= sideLength:
                    sides[i] += matchsticks[start]
                    if backtrack(start + 1):
                        return True
                    sides[i] -= matchsticks[start]
                    if sides[i] == 0:
                        break
            return False
        
        matchsticks.sort(reverse=True)
        
        return backtrack(0)