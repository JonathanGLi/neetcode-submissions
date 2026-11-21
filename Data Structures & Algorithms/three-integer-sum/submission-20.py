class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        res = set()
        # outer loop 1
        # sort for no duplcates



        for i in range(len(nums)):

            target = -nums[i]


        # 2 sum on inner loop, start at i+1
        #
            l = i+1
            r = len(nums)-1

            while (l < r):
                if nums[l] + nums[r] == target:
                    res.add((nums[i], nums[l], nums[r]))

                    l += 1
                    r -= 1

                
                elif nums[l] + nums[r] > target:
                    r -=1

                else: 
                    l += 1
                


        return list(res)
            
