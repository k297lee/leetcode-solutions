class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        res = 0
        
        def add(s1, s2):
            #print("s1", s1)
            #print("s2", s2)
            i1, i2 = len(s1) - 1, len(s2) - 1
            cr = 0
            ans = ""
            while i1 >= 0 and i2 >= 0:
                d1 = int(s1[i1])
                d2 = int(s2[i2])
                
                total = d1 + d2 + cr
                cr = total // 10
                ans = str(total % 10) + ans
                i1 -=1
                i2 -=1
            
            if i1 < 0 and i2 < 0:
                if cr:
                    ans = "1" + ans
                    cr = 0
            elif i1 < 0:
                while cr and i2 >= 0:
                    d2 = int(s2[i2])
                    total = d2 + cr
                    cr = total // 10
                    ans = str(total % 10) + ans
                    i2 -= 1
                ans = s2[:i2 + 1] + ans
            elif i2 < 0:
                while cr and i1 >= 0:
                    d1 = int(s1[i1])
                    total = d1 + cr
                    cr = total // 10
                    ans = str(total % 10) + ans
                    i1 -=1
                ans = s1[:i1 + 1] + ans
            
            if cr:
                ans = "1" + ans
                cr = 0
            
            #print("ans ", ans)
            return ans
            
        
        for i in range(len(num1)):
            digit1 = int(num1[i])
            subRes = ""
            for j in range(len(num2)):
                digit2 = int(num2[j])
                subTotal = digit1 * digit2
                #print("subtotal ", subTotal)
                if subRes:
                    subRes = add(subRes + "0", str(subTotal))
                else:
                    subRes = str(subTotal)
            if res:
                #print("res", res)
                res = add(res + "0", subRes)
            else:
                res = subRes
        
        return res