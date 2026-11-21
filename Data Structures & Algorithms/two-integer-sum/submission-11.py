class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #maps complemet to index
        sett = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in sett:
                return [sett[complement], i]

            sett[nums[i]] = i

        

        

