class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        res = 0
        
        for i in range(len(arr) + 1):
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                currMin = stack.pop()
                l = -1 if not stack else stack[-1]
                r = i
                
                res += (currMin - l) * (r - currMin) * arr[currMin]
            
            stack.append(i)
        
        return res % (10 ** 9 + 7)