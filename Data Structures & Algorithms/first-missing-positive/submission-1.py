class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        


        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0


        for i in range(len(nums)):
            a = abs(nums[i])
            if 1 <= a <= len(nums):
                if nums[a-1] > 0:
                    nums[a-1] *= -1
                elif nums[a-1] == 0:
                    nums[a-1] = -1 * len(nums)

        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1

        return len(nums)+1