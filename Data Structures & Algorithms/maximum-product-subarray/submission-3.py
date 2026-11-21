class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0]
        curMax = 1
        curMin = 1

        for n in nums:

            if n == 0:
                curMax = 1
                curMin = 1  
                res = max(res, 0)
                continue

            temp = curMax * n
            curMax = max(temp, curMin * n, n)
            curMin = min(temp, curMin * n, n)

            res = max(res, curMax)

        return res