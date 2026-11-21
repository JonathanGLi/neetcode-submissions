class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        

        i, j = 0, 0

        sett = set()

        for i in range(min(len(nums), k+1)):
            if nums[i] in sett:
                return True
            sett.add(nums[i])

        for i in range(k+1, len(nums)):

            sett.remove(nums[i-k-1])

            if nums[i] in sett:
                return True
            sett.add(nums[i])

        return False
