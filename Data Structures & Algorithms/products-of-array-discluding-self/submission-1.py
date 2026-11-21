class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [0] * len(nums)
        left = [0] * len(nums)
        right = [0] * len(nums)
        leftAcc = 1
        rightAcc = 1

        for i in range(len(nums)):
            leftAcc *= nums[i]
            left[i] = leftAcc
            j = len(nums)-i-1
            rightAcc *= nums[j]
            right[j] = rightAcc

        for i in range(len(nums)):
            r = 1
            if i>0:
                r*=left[i-1]
            if i<(len(right)-1):
                r*=right[i+1]
            res[i] = r

        return res


