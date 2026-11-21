class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        res = set()
        # outer loop 1
        # sort for no duplcates



        for i in range(len(nums)):

            total = -nums[i]
            
            seen = set()

        # 2 sum on inner loop, start at i+1
        #
            for j in range(i+1, len(nums)):


                if total - nums[j] in seen:
                    res.add((nums[i], total - nums[j], nums[j]))

                seen.add(nums[j])


        return list(res)
            
