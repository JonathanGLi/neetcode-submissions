class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        
        res = []
        i = 0

        while (i < len(nums)-2):
            prev = nums[i]
        
            l, r = i+1, len(nums)-1

            target = -nums[i]

            while l < r:
                if nums[l] + nums[r] > target:
                    r-=1
                elif nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    r-=1
                    l+=1
                    while l <r and nums[l] == nums[l-1]:
                        l+=1
                elif nums[l] + nums[r] < target:
                    l+=1

            i += 1
            while (i < len(nums)-2) and nums[i] == prev:
                i+=1

        return res