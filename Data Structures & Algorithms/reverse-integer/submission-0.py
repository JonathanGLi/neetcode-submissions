class Solution:
    def reverse(self, x: int) -> int:
        
        MIN = -2147483648
        MAX = 2147483647


        num = 0

        while x:

            #16
            digit = int(math.fmod(x, 10))

            #1
            x = int(x/10)

            if num > MAX//10 or (num == MAX//10 and digit > MAX%10):
                return 0
            if num < MIN//10 or (num == MIN//10 and digit > MAX%10):
                return 0

            num = num * 10 + digit


        return num 