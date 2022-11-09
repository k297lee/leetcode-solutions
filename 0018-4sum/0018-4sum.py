class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            if nums[i] > target / 4:
                break
            if i == 0 or nums[i] != nums[i - 1]:
                self.threeSum(nums, i, target - nums[i], res)
        
        return list(res)
    
    def threeSum(self, nums, i, target, res):
        for j in range(i + 1, len(nums)):
            if nums[j] > target / 3:
                break
            if j == i + 1 or nums[j] != nums[j - 1]:
                self.twoSum(nums, i, j, target - nums[j], res)
        
    def twoSum(self, nums, i, j, target, res):
        l, r = j + 1, len(nums) - 1
        while l < r:
            s = nums[l] + nums[r]
            
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                res.add((nums[i], nums[j], nums[l], nums[r]))
                l += 1
                r -= 1