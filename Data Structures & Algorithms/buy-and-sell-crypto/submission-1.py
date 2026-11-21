class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        i = 0
        j = i

        maxProf = 0

        while (j < len(prices)):

            if prices[j] < prices[i]:
                i = j

            prof = prices[j] - prices[i]
            maxProf = max(prof, maxProf)

            j+=1

        return maxProf