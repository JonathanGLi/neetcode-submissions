class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        N = len(profit)
        dp = [[0] * (capacity+1)for _ in range(-1, N)]

        for i in range(N):
            for c in range(capacity+1):

                take = 0
                
                skip = dp[i-1][c]

                newC = c - weight[i]
                if newC >= 0:
                    take = dp[i-1][newC] + profit[i]

                dp[i][c] = max(skip, take)

        return dp[N-1][capacity]

