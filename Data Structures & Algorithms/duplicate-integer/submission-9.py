class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
        D = set()

        for n in nums:

            if n in D:
                return True

            D.add(n)

        return False