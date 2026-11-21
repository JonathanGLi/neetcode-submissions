class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_p = 1
        min_p = 1
        res = nums[0]

        for n in nums:

            max_p, min_p = max(max_p * n, min_p * n, n), min(max_p * n, min_p * n, n)
            res = max(res, max_p)

        return res
