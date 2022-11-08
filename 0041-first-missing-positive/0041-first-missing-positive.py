class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 1
        
        for i in range(len(nums)):
            if nums[i] < 1:
                nums[i] = 1
            elif nums[i] > len(nums):
                nums[i] = 1
        
        for i in range(len(nums)):
            idx = abs(nums[i])
            if nums[idx - 1] > 0:
                nums[idx - 1] = -nums[idx - 1]
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        
        return len(nums) + 1