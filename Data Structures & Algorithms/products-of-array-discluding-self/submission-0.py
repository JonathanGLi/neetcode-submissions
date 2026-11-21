class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        numZeros = 0
        res = []

        acc = 1
        for n in nums:
            if n!= 0:
                acc*=n
            else:
                numZeros+=1

        if numZeros >= 2:
            return [0] * len(nums)
        elif numZeros == 1:
            for n in nums:
                if n != 0:
                    res.append(0)
                else:
                    res.append(int(acc))
        else:
            for n in nums:
                res.append(int(acc/n))

        return res

