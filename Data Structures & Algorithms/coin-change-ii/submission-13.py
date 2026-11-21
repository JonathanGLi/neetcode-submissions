class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo = [0] * (amount+1)


        n = len(coins)

        for i in range(n):
            memo[0] = 1
            for j in range(amount+1):
                if j - coins[i] >= 0:
                    memo[j] += memo[j - coins[i]]


        return memo[amount]









