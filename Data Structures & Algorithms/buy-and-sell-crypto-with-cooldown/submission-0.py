class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = len(prices)

        mapp = [0] * l

        for i in range(l):
            for j in range(l):
                if j > i:
                    continue
                elif i == 0 and j == 0:
                    mapp[0] = 0
                elif j == 0:

                    calc = prices[i] - prices[j]

                    mapp[i] = max(calc, mapp[i-1])
                else:
                    calc = prices[i] - prices[j]
                    if j - 2 >= 0:
                        calc += mapp[j-2]

                    mapp[i] = max(calc, mapp[i])

        return mapp[l-1]


                