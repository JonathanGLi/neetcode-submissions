class Solution:
    def reverse(self, x: int) -> int:

        isNeg = False
        if (x<0):
            isNeg = True
            x = -x
        
        res = 0

        while x > 0:

            digit = x % 10

            if (isNeg is False) and ((res > (2**31-1)//10) or ((res == (2**31-1)//10) and res%10 > (2**31-1)%10)):
                return 0

            if isNeg and ((res > (2**31)//10) or ((res == (2**31)//10) and res%10 > (2**31)%10)):
                return 0

            res *= 10

            res += digit

            x //= 10



        if isNeg:

            return -res

        
        return res

        
