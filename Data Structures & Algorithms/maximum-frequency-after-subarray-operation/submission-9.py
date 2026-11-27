class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        total_k = 0
        for n in nums:
            if n == k:
                total_k += 1

        max_gain = 0

        
        for target in range(1, 51):

            gain = 0

            for n in nums:

                if n == target:
                    gain += 1
                if n == k:
                    gain -=1

                gain = max(gain, 0)
                max_gain = max(gain, max_gain)

        return max_gain + total_k


        


