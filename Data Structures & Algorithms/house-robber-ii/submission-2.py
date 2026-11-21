class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        def helper(array):
            rob1 = 0
            rob2 = 0

            for n in array:

                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp

            return rob2

        return max(helper(nums[1:]), helper(nums[:len(nums)-1]))