class Solution:
    def addBinary(self, a: str, b: str) -> str:
        


        if len(b) > len(a):
            a, b = b, a

        pad = len(a) - len(b)
        b = pad * '0' + b

        res = ""
        rem = 0

        i = len(a)-1

        print(a, b)

        while i >= 0:
            
            sum1 = rem + int(a[i]) + int(b[i])

            if sum1 == 0:
                res += '0'
                rem = 0
            elif sum1 == 1:
                res += '1'
                rem = 0
            elif sum1 == 2:
                res += '0'
                rem = 1
            elif sum1 == 3:
                res += '1'
                rem = 1
            i-=1

        if rem == 1:
            res += '1'

        return res[::-1]



