class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxxDiff = 0
        minn = 0
        i = 0

        while i != len(prices):

            diff = prices[i] - prices[minn]

            if diff < 0:
                minn = i

            elif diff > maxxDiff:
                maxxDiff = diff
            
            i+=1
            
        return maxxDiff