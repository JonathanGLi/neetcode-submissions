class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mapp = {}

        def dfs(d, buy):

            if d >= len(prices):
                return 0

            if (d, buy) in mapp:
                return mapp[(d, buy)]

            cooldown = dfs(d+1, buy)

            if buy:
                money = dfs(d+1, False) - prices[d]
            else:
                money = dfs(d+2, True) + prices[d]

            return max(money, cooldown)

        return dfs(0, True)

            


                