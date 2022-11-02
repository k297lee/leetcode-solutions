class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        
        for i in reversed(range(len(digits))):
            digit = digits[i]
            
            digit = digit + c
            digits[i] = digit % 10
            
            if digit < 10:
                c = 0
                break
        
        if c == 1:
            digits.insert(0, 1)
        
        return digits