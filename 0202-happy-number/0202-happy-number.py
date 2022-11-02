class Solution:
    def isHappy(self, n: int) -> bool:
        num = n
        seen = set()
        seen.add(num)
        while num != 1:
            tmp = num
            currRes = 0
            while tmp != 0:
                digit = tmp % 10
                tmp = tmp // 10
                currRes += digit * digit
            num = currRes
            if num in seen:
                return False
            seen.add(num)
        return True