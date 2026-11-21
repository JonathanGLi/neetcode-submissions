class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        memo = {}

        def dfs(a):
            if a < 0:
                return 1e9
            if a == 0:
                return 0
            if a in memo:
                return memo[a]

            res = 1e9
            for c in coins:
                res = min(res, 1 + dfs(a - c))

            memo[a] = res
            return res


        res = dfs(amount)


        return -1 if res >= 1e9 else res