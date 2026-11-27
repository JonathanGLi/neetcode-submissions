class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        


        min_p = float('inf')
        max_gain = 0

        for p in prices:

            min_p = min(min_p, p)

            gain = p - min_p
            max_gain = max(max_gain, gain)


        return max_gain
