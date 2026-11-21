class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxx = nums[0]
        s = 0

        for i in range(len(nums)):
            s += nums[i]

            maxx = max(maxx, s)


            if s < 0:
                s = 0

        return maxx