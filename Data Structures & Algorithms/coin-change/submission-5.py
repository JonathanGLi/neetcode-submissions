class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        


        memo = defaultdict(int)

        # [3 5]  9 



        def dfs(i, a):
            print(i, a)

            if (i, a) in memo:
                return memo[i, a]

            if i >= len(coins):
                memo[i, a] = -1
                return -1

            if a < 0:
                memo[i, a] = -1
                return -1

            elif a == 0:
                memo[i, a] = 0
                return 0

            #a > 0
            take = 1 + dfs(i, a - coins[i])
            if take == 0: take = -1
            skip = dfs(i+1, a)

            res = -1
            if take == -1:
                res = skip
            elif skip == -1:
                res = take
            else:
                res = min(take, skip)

            memo[i, a] = res
            print("res", res)
            return res

        return dfs(0, amount)
