class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        
        currmin = float("inf")
        ret = 0

        for i in range (len(prices)):
            currmin = min(currmin, prices[i])
            ret = max(ret, prices[i] - currmin)
            print(currmin)
            print(ret)

        if ret > 0:
            return ret
        else:
            return 0
        