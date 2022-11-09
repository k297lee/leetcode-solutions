class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        seen = set()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, res, seen)
        
        return res

    def twoSum(self, nums, i, res, seen):
        l, r = i + 1, len(nums) - 1

        while l < r:
            total = nums[i] + nums[l] + nums[r]

            if total < 0:
                l += 1
            elif total > 0:
                r -= 1
            elif (nums[i], nums[l], nums[r]) not in seen:
                res.append((nums[i], nums[l], nums[r]))
                seen.add((nums[i], nums[l], nums[r]))
                l += 1
                r -= 1
            else:
                l += 1
                r -= 1