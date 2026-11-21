class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1

        a = 1
        b = 2
        
        for i in range(n-3, -1, -1):
            temp = b
            b = a+b
            a = temp

        return b


# 0 1 2 3 4
# 5 3 2 1 0

