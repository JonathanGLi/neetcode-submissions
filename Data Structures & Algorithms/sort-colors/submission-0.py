class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count_0, count_1, count_2 = 0, 0, 0
        
        for n in nums:
            if n == 0:
                count_0 +=1 
            elif n == 1:
                count_1 +=1 
            elif n == 2:
                count_2 +=1 

        for i in range(len(nums)):
            if i < count_0:
                nums[i] = 0
            elif i < count_0 + count_1:
                nums[i] = 1
            else:
                nums[i] = 2
                




