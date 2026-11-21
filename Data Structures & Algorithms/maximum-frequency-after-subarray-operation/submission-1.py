class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        k_count = nums.count(k)
        max_window = 0

        for i in range(51):

            if i == k:
                continue
            cur_window = 0
            for n in nums:
                if n == k:
                    cur_window -= 1
                elif n == i:
                    cur_window += 1

                cur_window = max(cur_window, 0)

                if cur_window > max_window:
                    max_window = cur_window

        return max_window+k_count



        