class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        a, b = nums[0], max(nums[0], nums[1])

        i = 2
        while i < len(nums):
            temp = b
            b = max(b, a + nums[i])
            a = temp

            i+=1

        return b



