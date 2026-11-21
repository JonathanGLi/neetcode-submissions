class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        # find index where element before cur element is greater
        # return cur element
        last_i = len(nums)-1
        l = 0
        r = last_i

        while (l <= r):
            m = (l+r)//2

            if (((m == 0) and (nums[0] <= nums[last_i])) 
                or ((m > 0) and (nums[m] <= nums[m-1]))):
                return nums[m]
            elif ((l != m) and 
                ((nums[l] >= nums[m]) or 
                (nums[r] >= nums[m]))):
                r = m - 1
            else:
                l = m + 1
            
