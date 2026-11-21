class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

        # 1 2 3
        # 1 3 2

        # 1 2 3 4 5 
        # 1 2 3 5 4

        # 1 5 4 3 2 
        # 2 1 3 4 5

        # 3 2 1
        # 1 2 3

        #if monotonically decreasing => increasing order, bc largest


        #start from end suffixes, find smallest monotocinally dec suffix
        #change number nefore suffix to be 1 greater, remaining numbers in suffic to be monotonically inc

        # 1 5 2 4 3
        # 1 5 3 2 4

        n = len(nums)

        i = len(nums) - 1
        print(i)
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        i-=1

        print(i)

        # case mono dec
        if i > 0:
            # find replacement first larger and swap
            j = n-1
            while nums[j] <= nums[i]:
                j-=1

            #swap
            nums[j], nums[i] = nums[i], nums[j]

        #sort
        i = i +1
        j = n-1

        while i < j:
            nums[j], nums[i] = nums[i], nums[j]
            i+=1
            j-=1

    

















