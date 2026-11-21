class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        l = len(nums)

        res = [1] * l
        acc = 1
        
        for i in range(1, l):
            acc *= nums[i-1]
            res[i] *= acc

        acc2 = 1
        
        for i in range(l-2, -1, -1):
            acc2 *= nums[i+1]
            res[i] *= acc2

        return res