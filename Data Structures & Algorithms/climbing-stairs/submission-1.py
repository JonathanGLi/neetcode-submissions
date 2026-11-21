class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        d = dict()
        d[1] = 1
        d[2] = 2
        k = 3

        while k <= n:
            d[k] = d[k-1] + d[k-2]


            k+=1

        return d[n]