class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_run = nums[0]
        min_run = nums[0]
        
        res = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            tmp = max(num, max_run * num, min_run * num)
            min_run = min(num, max_run * num, min_run * num)
            max_run = tmp
            res = max(res, max_run)
        
        return res