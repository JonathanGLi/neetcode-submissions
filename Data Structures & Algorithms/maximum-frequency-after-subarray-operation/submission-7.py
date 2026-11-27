class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        



# Maps n to k_count - n_count

# max(n cooutn - k count - prev(k_count - n count))

        count = defaultdict(int)
        res = 0
        for n in nums:
            count[n] = max(count[n], count[k]) + 1
            res = max(count[n] - count[k], res)

        return res + count[k]


        


