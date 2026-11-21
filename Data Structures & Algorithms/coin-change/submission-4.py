class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins.sort()

        if amount == 0:
            return 0
        
        memo = [-1] * (amount+1)

        for i in range(1, amount+1):
            for coin in coins:
                if coin == i:
                    memo[i] = 1

                if i-coin >= 1 and memo[i - coin] > 0:
                    if memo[i] == -1:
                        memo[i] = memo[i-coin] + 1
                    else:
                        memo[i] = min(memo[i-coin] + 1, memo[i])
        print(memo)
        return memo[amount]