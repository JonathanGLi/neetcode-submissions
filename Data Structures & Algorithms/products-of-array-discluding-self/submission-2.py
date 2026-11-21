class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)
        leftAcc = 1
        rightAcc = 1

        for i in range(len(nums)):
            res[i]*=leftAcc
            leftAcc*=nums[i]
        for i in range(len(nums)-1, -1, -1):
            res[i]*=rightAcc
            rightAcc*=nums[i]

        return res


