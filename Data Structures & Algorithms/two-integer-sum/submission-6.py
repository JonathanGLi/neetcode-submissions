class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        D = {}

        for i, n in enumerate(nums):

            complement = target - n

            if complement in D:
                return [D[complement], i]

            D[n] = i
