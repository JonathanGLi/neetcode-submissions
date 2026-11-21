class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len1 = len(nums)
        #create two arrays
        l1 = [0] * len1
        l2 = [0] * len1


        #fill them with factorial values
        k1 = 1
        k2 = 1

        for i in range(len1):

            k1 *= nums[i]
            l1[i] = k1

            j = len1-i-1

            k2 *= nums[j]
            l2[j] = k2

        # create resulting array
        res = [0] * len1
        for i in range(len1):

            if i == 0:
                res[0] = l2[1]
            elif i == len1-1:
                res[len1-1] = l1[len1-2]
            else:
                res[i] = l1[i-1] * l2[i+1]

        print(l1)
        print(l2)

        return res
