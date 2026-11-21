class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #(i, buying) => profit
        memo = {}

        def dfs(i, buying):


            if i >= len(prices):
                return 0 

            if (i, buying) in memo:
                return memo[(i, buying)]

            if buying:
                take = dfs(i+1, False) - prices[i]
                skip = dfs(i+1, True)
                res = max(take, skip)
            #selling
            else:
                take = dfs(i+2, True) + prices[i]
                skip = dfs(i+1, False)
                res = max(take, skip)

            memo[(i, buying)] = res

            return res

        return dfs(0, True)


            