class LargerNum(str):
    def __lt__(x, y):
        return x + y > y + x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = []
        for i in range(len(nums)):
            res.append(str(nums[i]))
        
        largestNum = "".join(sorted(res, key = LargerNum))
        
        return "0" if largestNum[0] == "0" else largestNum