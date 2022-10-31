class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        
        if target > total:
            return 0
        
        dp = [[0] * (2 * total + 1) for _ in range(len(nums))]
        prev = [0] * (2 * total + 1)
        
        prev[total + nums[0]] = 1
        prev[total - nums[0]] += 1
        
        for i in range(1, len(nums)):
            curr = [0] * (2 * total + 1)
            for j in range(-total, total + 1):
                if prev[j + total]:
                    curr[j + total + nums[i]] += prev[j + total]
                    curr[j + total - nums[i]] += prev[j + total]
            prev = curr
        
        return prev[total + target]