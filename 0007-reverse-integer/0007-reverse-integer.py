class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        MAX = (2 ** 31) - 1
        MIN = -(2 ** 31)
        sign = 1 if x >= 0 else -1
        x = abs(x)
        while x != 0:
            tmp = (abs(x) % 10) * sign
            x = x // 10
            
            if res > MAX // 10 or (res == MAX // 10 and tmp > 7):
                return 0
            
            if res < -((-MIN) // 10) or (res == MIN // 10 and tmp < -8):
                return 0

            res = res * 10 + tmp
            
        return res