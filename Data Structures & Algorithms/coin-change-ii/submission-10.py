class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # coins.sort()

        dp = [0] * (amount + 1)
        dp[0] = 1

        for j in range(1,amount+1):
            back_index = j - coins[0]
            if back_index >= 0:
                dp[j] = dp[back_index]

        for i in range(1, len(coins)):
            new_dp = [0] * (amount + 1)
            new_dp[0] = 1

            for j in range(1,amount+1):
                back_index = j - coins[i]
                if back_index >= 0:
                    new_dp[j] = new_dp[back_index]

                new_dp[j] += dp[j]

            dp = new_dp

        return dp[-1]