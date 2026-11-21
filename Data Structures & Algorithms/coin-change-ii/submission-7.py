class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        if amount == 0:
            return 1

        mapp = {}

        def dfs(cost, i):
            if i >= len(coins):
                return 0
            if (cost, i) in mapp:
                return mapp[(cost, i)]

            new_cost = cost - coins[i]
            if new_cost == 0:
                return 1
            elif new_cost < 0:
                return 0
            
            stay = dfs(new_cost, i)
            mapp[(new_cost, i)] = stay

            move = dfs(cost, i+1)
            mapp[(cost, i+1)] = move

            return stay + move

        return dfs(amount, 0)