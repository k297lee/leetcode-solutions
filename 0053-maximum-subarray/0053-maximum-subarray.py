class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        
        prev = nums[0]
        maxVal = prev
        
        for i in range(1, len(nums)):
            curr = max(nums[i], prev + nums[i])
            maxVal = max(curr, maxVal)
            prev = curr
            
        return maxVal
    