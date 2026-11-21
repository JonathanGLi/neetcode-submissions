class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        nums.append(float('inf'))
        l, r = 0, len(nums) - 1

        res = -1
        while l <= r:
            m = (l+r)//2
            print(m)

            if target <= nums[m]:
                res = m
                r = m-1
            else:
                l = m+1

        return res