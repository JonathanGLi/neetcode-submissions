class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        # 1 2 3 4 5 6 7 
        # 1 2 3 5

        if n == 1:
            return 1
        if n == 2 :
            return 2
        
        a = 1
        b = 2
        for i in range(2, n):
            b, a= a + b, b

        return b

