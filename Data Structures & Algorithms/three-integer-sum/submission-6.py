class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        seen = set()

        for i, n in enumerate(nums):

            S = set()
            target = -n

            for j in range(i+1, len(nums)):
                comp = target - nums[j]

                if comp in S:

                    ssorted = tuple(sorted([n, comp, nums[j]]))

                    if ssorted not in seen:
                        res.append([n, comp, nums[j]])
                    seen.add(ssorted)


                S.add(nums[j])

        return res


