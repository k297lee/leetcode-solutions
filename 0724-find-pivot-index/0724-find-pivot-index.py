class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum, rightSum = 0, total - nums[0]
        
        for i in range(1, len(nums)):
            if leftSum == rightSum:
                return i - 1
            
            leftSum += nums[i - 1]
            rightSum -= nums[i]
        
        return len(nums) - 1 if leftSum == rightSum else -1