class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        max_p = 0

        i, j = 0, 0

        while j < len(prices):
            
            if prices[j] < prices[i]:
                i = j
            
            max_p = max(max_p, prices[j] - prices[i])

    
            j+=1


        return max_p