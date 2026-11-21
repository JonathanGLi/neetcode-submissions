class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        counts = Counter(nums)

        res = 0

        for count in counts.values():

            if count == 1:
                return -1

            m = count % 3


            if m == 0:
                res += count //3
            if m == 1:
                res += count //3 +1
            if m == 2:
                res += count //3 +1

        return res