class Solution:
    def numSquares(self, n: int) -> int:
        
        dp = [n] * (n+1)
        dp[0] = 0

        for target in range(n+1):
            for s in range(int(target**0.5)+1):
                square = s*s
                if square > target:
                    continue
                dp[target] = min(dp[target], 1 + dp[target - square])



        return dp[n]
