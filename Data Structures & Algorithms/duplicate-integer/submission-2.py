class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        S = set()
        for i in range(len(nums)):
            if nums[i] in S:
                return True
            else:
                S.add(nums[i])
        return False

