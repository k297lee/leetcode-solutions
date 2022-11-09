class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        stack = [(-1, 0)]
        curr = 0
        res = 0
        nums.append(0)
        for num in nums:
            while stack and stack[-1][0] >= num:
                minVal, _ = stack.pop()
                res = max(res, minVal * (curr - stack[-1][1]))
            
            curr += num
            stack.append((num, curr))
        
        return res % (10 ** 9 + 7)