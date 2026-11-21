class Solution:
    def integerBreak(self, n: int) -> int:
        


        #5, 2x3
        #6, 3x3
        #7, 3 x 2 2 
        # 8 2 x 2x2x2


        # if num is greaterthan 5, we always split

        if n == 2:
            return 1

        if n == 3:
            return 2

        memo = [0] * (n+1)
        memo[2] = 2
        memo[3] = 3
        memo[1] = 1
        
        for i in range(4, n+1):
            for a in range(2, i):
                
                b = i - a
                print(i, a, b)

                memo[i] = max(memo[i], memo[a] * memo[b])
        print(memo)
        return memo[n]

