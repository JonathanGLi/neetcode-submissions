class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        

        # take size of nums
        # take size of set(nums)

        return len(nums) != len(set(nums))